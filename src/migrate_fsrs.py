"""One-shot migration: seed topics.fsrs_state from existing mastery_score.

Idempotent: rows with non-empty fsrs_state are skipped. Backs up the DB
to <db_path>.bak before mutating.
"""

from __future__ import annotations

import shutil
from datetime import datetime, timedelta, timezone
from pathlib import Path

from .config import settings
from .fsrs import fsrs_init, serialize
from .student_model import conn, initialize_database


def _seed_state(mastery: float) -> dict:
    state = fsrs_init()
    if mastery <= 0:
        return state
    stability = max(0.5, mastery * 30.0)
    difficulty = max(1.0, min(10.0, 10.0 * (1.0 - mastery)))
    now = datetime.now(timezone.utc)
    state.update(
        {
            "stability": stability,
            "difficulty": difficulty,
            "reps": 1,
            "state": "review",
            "last_review": now.isoformat(),
            "next_due": (now + timedelta(days=max(1, int(stability)))).isoformat(),
        }
    )
    return state


def migrate(dry_run: bool = False) -> dict:
    initialize_database()
    db_path = Path(settings.sqlite_db_path)
    if db_path.exists() and not dry_run:
        bak = db_path.with_suffix(db_path.suffix + ".bak")
        if not bak.exists():
            shutil.copy2(db_path, bak)
    seeded = 0
    skipped = 0
    with conn() as db:
        rows = db.execute(
            "SELECT topic_id, mastery_score, fsrs_state FROM topics"
        ).fetchall()
        for row in rows:
            existing = row["fsrs_state"] if "fsrs_state" in row.keys() else None
            if existing:
                skipped += 1
                continue
            state = _seed_state(float(row["mastery_score"] or 0.0))
            if not dry_run:
                db.execute(
                    "UPDATE topics SET fsrs_state=? WHERE topic_id=?",
                    (serialize(state), int(row["topic_id"])),
                )
            seeded += 1
    return {"seeded": seeded, "skipped": skipped, "total": seeded + skipped}


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    summary = migrate(dry_run=args.dry_run)
    print(f"FSRS migration: {summary}")


if __name__ == "__main__":
    main()
