"""Separate facts the user was actually ASKED from facts merely INGESTED.

The bug, found by comparing the 2026-08-18 session transcript against the
database: bulk ingestion (the Strong Medicine workup videos) wrote every
extracted fact through the same path an answered question uses, so each landed
as `times_seen=1, times_correct=0, status='weak'` — byte-identical to "the user
was asked this and got it wrong."

Three things broke at once:

1. COVERAGE INFLATED. 417 facts looked "tracked" when 212 had never been shown
   to anyone. The tutor reported 6.6% catalog coverage; the honest figure was
   about half that. The maintainer spotted it immediately ("the numerator looks
   high") — the same class of artifact-reported-as-fact that has cost several
   sessions already.

2. ACCURACY POISONED. 212 facts scored 0-for-1 without ever being asked, so
   every per-topic accuracy figure was dragged toward zero by questions that
   were never put to the user.

3. THE REVIEW AVALANCHE REGREW. All 287 facts created that day were scheduled
   for the next morning as 'weak' — the highest-priority bucket — which would
   have pushed genuine due reviews out of the ration and recreated exactly the
   "2-3 hours of reviews today" problem that rationing was built to solve.

Fix: a `first_presented_at` column is the single source of truth for "the user
has actually seen this." NULL means ingested-but-never-asked. Those rows are
reset to a true never-seen state and given status 'new', which sorts BEHIND
'weak' and 'learning' in the due query — new material can no longer crowd out
real reviews.

Idempotent. Backs up the DB (via the sqlite3 backup API, because a WAL-mode
copy through the filesystem silently omits un-checkpointed frames — that
mistake previously appeared to "lose" 9 exposures).

    python scripts/fix_ghost_facts.py --dry-run
    python scripts/fix_ghost_facts.py
"""
from __future__ import annotations

import argparse
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.config import settings  # noqa: E402


def backup(db_path: Path) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    dest = db_path.with_name(f"{db_path.stem}.pre_ghostfix.{stamp}.db")
    src = sqlite3.connect(str(db_path))
    dst = sqlite3.connect(str(dest))
    with dst:
        src.backup(dst)          # NOT shutil.copy2 — WAL frames would be lost
    src.close()
    dst.close()
    return dest


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    db_path = Path(settings.sqlite_db_path)
    db = sqlite3.connect(str(db_path))
    db.row_factory = sqlite3.Row

    cols = {r["name"] for r in db.execute("PRAGMA table_info(knowledge_points)")}
    if "first_presented_at" not in cols and not args.dry_run:
        db.execute("ALTER TABLE knowledge_points ADD COLUMN first_presented_at TEXT")
        db.commit()
        print("added column first_presented_at")

    # Identify ingestion by its WRITE SIGNATURE, not by correlating with
    # question_attempts. The attempt-correlation heuristic was tried first and
    # was badly wrong: many genuine facts are written by record_knowledge_point
    # without any paired topic-level attempt row, or seconds after the last
    # attempt of the session, so it condemned real study history — including a
    # DKA fact standing at 2-correct-of-2 and a hyponatremia fact at 1-of-1.
    #
    # The signature is unmistakable in the data. A real session writes 1-5
    # facts in a minute, all on the ONE topic being discussed, and some of them
    # are answered correctly. The video ingestion wrote 161 facts across 10
    # topics inside a single minute, with not one ever answered correctly.
    #
    # So: a burst minute is >= BURST_MIN facts spanning >= BURST_TOPICS topics.
    # times_correct > 0 is an absolute veto — being right about something is
    # proof it was asked — so no genuinely studied fact can be caught even if a
    # future bulk write somehow lands inside a real session.
    BURST_MIN, BURST_TOPICS = 20, 3
    burst_minutes = [
        r["m"] for r in db.execute(
            """SELECT strftime('%Y-%m-%dT%H:%M', created_at) m
                 FROM knowledge_points
                GROUP BY m
               HAVING COUNT(*) >= ? AND COUNT(DISTINCT topic) >= ?
                  AND SUM(CASE WHEN times_correct > 0 THEN 1 ELSE 0 END) = 0""",
            (BURST_MIN, BURST_TOPICS))
    ]
    print(f"bulk-ingestion bursts detected: {len(burst_minutes)}"
          + (f" ({', '.join(burst_minutes)})" if burst_minutes else ""))
    if not burst_minutes:
        ghosts, real = [], db.execute(
            "SELECT COUNT(*) FROM knowledge_points WHERE times_seen > 0").fetchone()[0]
    else:
        marks = ",".join("?" * len(burst_minutes))
        ghosts = db.execute(
            f"""SELECT id, topic, point, times_seen, next_review_date
                  FROM knowledge_points
                 WHERE times_seen > 0 AND times_correct = 0
                   AND strftime('%Y-%m-%dT%H:%M', created_at) IN ({marks})
                 ORDER BY topic""", burst_minutes).fetchall()
        real = db.execute(
            f"""SELECT COUNT(*) FROM knowledge_points
                 WHERE times_seen > 0
                   AND NOT (times_correct = 0
                            AND strftime('%Y-%m-%dT%H:%M', created_at) IN ({marks}))""",
            burst_minutes).fetchone()[0]

    total = db.execute("SELECT COUNT(*) FROM knowledge_points").fetchone()[0]
    print(f"\n{total} knowledge points total")
    print(f"  genuinely presented (an attempt backs them) : {real}")
    print(f"  ingested only, never asked                  : {len(ghosts)}")
    by_topic: dict[str, int] = {}
    for g in ghosts:
        by_topic[g["topic"]] = by_topic.get(g["topic"], 0) + 1
    for t, n in sorted(by_topic.items(), key=lambda kv: -kv[1]):
        print(f"     {n:>4}  {t}")

    if args.dry_run:
        print("\ndry run — nothing written")
        return
    if not ghosts:
        print("\nnothing to fix")
    else:
        dest = backup(db_path)
        print(f"\nbacked up to {dest.name}")
        ids = [g["id"] for g in ghosts]
        db.executemany(
            """UPDATE knowledge_points
                  SET times_seen = 0, times_correct = 0, consecutive_correct = 0,
                      last_correct = NULL, last_confidence = NULL,
                      confidence_sum = 0, confidence_n = 0,
                      interval_days = 0, fsrs_state = NULL,
                      next_review_date = NULL, status = 'new',
                      first_presented_at = NULL
                WHERE id = ?""",
            [(i,) for i in ids],
        )
        # Everything else HAS been presented; stamp it so the distinction holds
        # from here on without needing this reconstruction again.
        db.execute(
            """UPDATE knowledge_points
                  SET first_presented_at = COALESCE(first_presented_at, updated_at)
                WHERE times_seen > 0 AND first_presented_at IS NULL""")
        db.commit()
        print(f"reset {len(ids)} ingested facts to never-presented ('new')")

    print("\nafter:")
    for r in db.execute(
            "SELECT status, COUNT(*) n FROM knowledge_points GROUP BY status ORDER BY n DESC"):
        print(f"  {r['status']:<10} {r['n']}")
    seen = db.execute(
        "SELECT COUNT(*) FROM knowledge_points WHERE first_presented_at IS NOT NULL").fetchone()[0]
    print(f"\n  honest coverage numerator (actually studied): {seen}")
    db.close()


if __name__ == "__main__":
    main()
