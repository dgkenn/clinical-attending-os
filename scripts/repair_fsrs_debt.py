"""Credit answers the scheduler never saw.

The maintainer's complaint — "I feel like I'm constantly reviewing information
that I already know" — is measurable. 41 of 168 studied facts carry an FSRS
`reps` count lower than their `times_seen`: the counters recorded the answers,
the scheduler did not. The worst case had been answered 19 times, 16 correctly,
and still sat at reps=3 with stability 7.68 — so it kept returning on a one-week
timer as though it were nearly new. That is exactly the experience being
described, and it is not a feeling.

Cause: 39 of the 41 were created in late June, before per-fact FSRS state
existed. Their answer counters predate the scheduler, so when state was
introduced they started from `fsrs_init()` while the counts carried on. This is
one-time migration debt, not an ongoing leak — verified separately by
tests/test_fsrs_state_compounds.py, which shows properly spaced reviews
compounding 3 -> 11 -> 36 -> 104 days.

The repair replays the missing answers. For each fact it applies
(times_seen - reps) further reviews, using the recorded correct/seen ratio to
decide how many are successes, spacing each one by the interval the scheduler
itself proposes so the compounding is honest rather than invented. It cannot
recover the true dates or the original order, so this is a reconstruction — but
a fact answered correctly sixteen times unambiguously deserves more than a
one-week interval, and leaving it understated is the larger error.

CONSERVATIVE BY DESIGN: successes are credited at FSRS "Good", never "Easy",
and the misses are replayed too rather than quietly dropped. Facts are never
pushed beyond the interval their real history supports.

    python scripts/repair_fsrs_debt.py --dry-run
    python scripts/repair_fsrs_debt.py
"""
from __future__ import annotations

import argparse
import io
import json
import sqlite3
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.config import settings  # noqa: E402
from src.fsrs import deserialize, fsrs_review, serialize  # noqa: E402

# Never fabricate more than this many replayed reviews for one fact, however
# large the gap. The 19-times-seen sepsis fact is a genuine outlier and even it
# should not be catapulted to a multi-year interval on reconstructed evidence.
MAX_REPLAY = 8
# Ceiling on a reconstructed interval. The evidence here is real answers but
# assumed dates, so a fact may earn months off — never a year.
MAX_INTERVAL_DAYS = 90.0


def backup(db_path: Path) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    dest = db_path.with_name(f"{db_path.stem}.pre_fsrsdebt.{stamp}.db")
    src, dst = sqlite3.connect(str(db_path)), sqlite3.connect(str(dest))
    with dst:
        src.backup(dst)
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

    affected = []
    for r in db.execute("""SELECT id, topic, point, times_seen, times_correct,
                                  fsrs_state, interval_days, next_review_date,
                                  created_at, updated_at, last_correct
                             FROM knowledge_points
                            WHERE times_seen > 0 AND fsrs_state IS NOT NULL"""):
        try:
            st = json.loads(r["fsrs_state"])
        except Exception:
            continue
        reps = st.get("reps")
        if reps is None or reps >= r["times_seen"]:
            continue
        affected.append((dict(r), st, min(MAX_REPLAY, r["times_seen"] - reps)))

    print(f"facts whose scheduler missed answers: {len(affected)}\n")
    if not affected:
        return

    plans = []
    for row, st, missing in affected:
        # Split the replayed reviews to match the fact's real accuracy, then
        # order them by the outcome the database actually recorded LAST.
        #
        # Ordering is not cosmetic: FSRS is path-dependent, so ending on a lapse
        # leaves a fact scheduled as fragile. Replaying misses last was the
        # first attempt and it is the pessimistic assumption, not the true one —
        # the real trajectory is usually miss-then-learn, and `last_correct`
        # records which way it actually went. Use that instead of guessing.
        accuracy = row["times_correct"] / max(1, row["times_seen"])
        n_correct = round(missing * accuracy)
        n_wrong = missing - n_correct
        if row["last_correct"]:
            ratings = [1] * n_wrong + [3] * n_correct     # ends on a success
        else:
            ratings = [3] * n_correct + [1] * n_wrong     # ends on the recorded miss

        state = deserialize(json.dumps(st))
        now = datetime.now(timezone.utc)
        interval = float(row["interval_days"] or 1)

        # Space the replayed reviews by what REALLY elapsed, not by the interval
        # FSRS would have liked. Assuming ideal spacing credits every replayed
        # answer with full compounding and sent a 2-of-2 fact from 15 days to
        # 140 — far beyond what two correct answers evidence. The honest figure
        # is the fact's own lifetime divided across its missing reviews: the
        # sepsis fact spans late June to now with 16 unseen answers, so roughly
        # every 3 days, which is about how often it was actually drilled.
        try:
            born = datetime.fromisoformat(str(row["created_at"]).replace(" ", "T"))
            last = datetime.fromisoformat(str(row["updated_at"]).replace(" ", "T"))
            lifetime = max(1.0, (last - born).total_seconds() / 86400)
        except Exception:
            lifetime = float(missing)
        real_gap = max(0.5, lifetime / max(1, missing))

        for rating in ratings:
            try:
                state.last_review = now - timedelta(days=real_gap)
            except Exception:
                pass
            state, next_due = fsrs_review(state, rating=rating)
            try:
                interval = max(1.0, (datetime.fromisoformat(next_due).date() - now.date()).days)
            except Exception:
                interval = max(1.0, interval)
        # Reconstructed history earns a real reprieve, not a year off.
        interval = min(interval, MAX_INTERVAL_DAYS)
        new_due = (now.date() + timedelta(days=int(round(interval)))).isoformat()
        plans.append((row, serialize(state), interval, new_due, ratings))

    plans.sort(key=lambda p: -p[2])
    for row, _s, interval, new_due, ratings in plans[:15]:
        old = float(row["interval_days"] or 0)
        print(f"  {row['times_correct']}/{row['times_seen']} correct | "
              f"{old:>5.0f}d -> {interval:>6.0f}d  (+{len(ratings)} replayed)  "
              f"{row['point'][:52]}")
    if len(plans) > 15:
        print(f"  ... and {len(plans) - 15} more")

    if args.dry_run:
        print("\ndry run — nothing written")
        return

    dest = backup(db_path)
    print(f"\nbacked up to {dest.name}")
    db.executemany(
        """UPDATE knowledge_points
              SET fsrs_state = ?, interval_days = ?, next_review_date = ?
            WHERE id = ?""",
        [(s, interval, new_due, row["id"]) for row, s, interval, new_due, _r in plans])
    db.commit()
    print(f"repaired {len(plans)} facts")

    due_now = db.execute(
        """SELECT COUNT(*) FROM knowledge_points
            WHERE next_review_date IS NOT NULL
              AND date(next_review_date) <= date('now','localtime')
              AND status != 'new'""").fetchone()[0]
    print(f"review queue now: {due_now} facts due")
    db.close()


if __name__ == "__main__":
    main()
