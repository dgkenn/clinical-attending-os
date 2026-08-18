"""Retire phantom topic rows: rescue the real facts, delete the boilerplate.

`topics` has one row per (topic, subtopic). The OLD log_missed_topic wrote each
missed fact as a pseudo-topic row, so 45 rows carry fact-level content with
times_seen=0, last_seen NULL, and a next_review_date frozen in June 2026.

Nothing can ever review them: the tutor reviews "PE", never "Wells PE score:
D-dimer only useful if...". They sit permanently overdue and, while the due
queue ranked a topic by its most-overdue row, they pinned PE / Delirium /
Hyponatremia at ~56 days overdue the day after those topics were studied — so
studying a topic never visibly cleared it.

Two populations, handled differently:

  * Real clinical facts (~35) — "DKA: do NOT start insulin if K+ <3.3 mEq/L",
    "Variceal bleed: ceftriaxone IV is mandatory". These are exactly what
    knowledge_points exists for, and they are genuine gaps the user missed in
    June. MIGRATED into knowledge_points as weak and due, not discarded.

  * Ingest boilerplate (~10) — "Intern Notes / Survival Guide p. 2: All
    information contained within...", plus table-of-contents lines misfiled
    under Airway. DELETED.

Usage:
    python scripts/migrate_phantom_topic_rows.py --dry-run   # report only
    python scripts/migrate_phantom_topic_rows.py --apply     # perform it

Idempotent: a fact already present in knowledge_points is not inserted twice.
Always back the database up first; --apply refuses to run without a backup
present alongside it.
"""
from __future__ import annotations

import argparse
import io
import re
import sqlite3
import sys
from pathlib import Path

# The facts carry clinical typography (arrows, en-dashes) and the Windows
# console defaults to cp1252, which raises on them mid-report.
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.config import settings  # noqa: E402
from src.student_model import _NON_TOPICS  # noqa: E402

# Page-anchored ingest artifacts: "<Book> p. 4: Allergy ......" — a table of
# contents line or a disclaimer paragraph, never a fact worth drilling.
_BOILERPLATE = re.compile(r'\bp\.\s*\d+\s*:', re.I)


def is_boilerplate(topic: str, subtopic: str) -> bool:
    if (topic or "").strip().lower() in _NON_TOPICS:
        return True
    if _BOILERPLATE.search(subtopic or ""):
        return True
    # A "fact" that is mostly dot-leaders is a contents line.
    return (subtopic or "").count(".") > 12


def find_phantoms(con: sqlite3.Connection) -> list[sqlite3.Row]:
    con.row_factory = sqlite3.Row
    return list(con.execute(
        """SELECT topic_id, topic, subtopic FROM topics
           WHERE subtopic <> '' AND subtopic IS NOT NULL
             AND times_seen = 0 AND last_seen IS NULL
           ORDER BY topic, subtopic"""))


def main() -> None:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true")
    g.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    db = Path(settings.sqlite_db_path)
    if args.apply and not list(db.parent.glob("student_model_prephantom_*.db")):
        raise SystemExit(
            "refusing to --apply with no student_model_prephantom_*.db backup "
            "beside the database; make one first")

    con = sqlite3.connect(str(db))
    con.row_factory = sqlite3.Row
    rows = find_phantoms(con)
    existing = {(r["topic"].lower(), r["point"].lower())
                for r in con.execute("SELECT topic, point FROM knowledge_points")}

    migrate, drop, skip = [], [], []
    for r in rows:
        if is_boilerplate(r["topic"], r["subtopic"]):
            drop.append(r)
        elif (r["topic"].lower(), r["subtopic"].lower()) in existing:
            skip.append(r)          # already a knowledge point; just drop the row
        else:
            migrate.append(r)

    print(f"phantom rows found : {len(rows)}")
    print(f"  -> migrate to knowledge_points : {len(migrate)}")
    print(f"  -> delete as ingest boilerplate: {len(drop)}")
    print(f"  -> already a knowledge point   : {len(skip)}")

    if args.dry_run:
        print("\nWOULD MIGRATE:")
        for r in migrate[:60]:
            print(f"   [{r['topic']}] {r['subtopic'][:88]}")
        print("\nWOULD DELETE:")
        for r in drop[:60]:
            print(f"   [{r['topic']}] {r['subtopic'][:88]}")
        print("\n(dry run — nothing written)")
        return

    with con:
        for r in migrate:
            # Weak and due now: these are facts that were MISSED and never
            # revisited. Recording them as anything softer would overstate what
            # the user knows.
            con.execute(
                """INSERT INTO knowledge_points
                       (topic, point, status, times_seen, times_correct,
                        consecutive_correct, mistake_type, interval_days,
                        next_review_date, created_at, updated_at)
                   VALUES (?, ?, 'weak', 0, 0, 0, 'other', 1,
                           date('now'), CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)""",
                (r["topic"], r["subtopic"]))
        ids = [r["topic_id"] for r in (migrate + drop + skip)]
        con.executemany("DELETE FROM topics WHERE topic_id = ?",
                        [(i,) for i in ids])

    print(f"\nmigrated {len(migrate)} facts into knowledge_points")
    print(f"deleted  {len(drop) + len(skip) + len(migrate)} phantom topic rows")
    print(f"topics rows now: {con.execute('SELECT COUNT(*) FROM topics').fetchone()[0]}")
    print(f"knowledge_points now: "
          f"{con.execute('SELECT COUNT(*) FROM knowledge_points').fetchone()[0]}")


if __name__ == "__main__":
    main()
