"""One-shot row merger for the topics table.

Earlier debug sessions left fragments — e.g. four `Respiratory physiology`
rows with subtopics `due:Respiratory physiology:due`, `due:Respiratory
physiology:shu`, `shunt`, and ``. Each has its own FSRS state, so retention
data fragments across rows. This script merges all duplicates of the same
canonical (topic, subtopic_canonical) pair into one row.

Canonical subtopic: strip 'due:' prefixes and any trailing-after-colon
fragments. Empty stays empty.

Idempotent. Backs up topics.bak before mutating.
"""

from __future__ import annotations

import json
import shutil
import sqlite3
from collections import defaultdict
from pathlib import Path

from .config import settings


def canonicalize_subtopic(subtopic: str | None) -> str:
    """Strip leading 'due:Topic:due:' style noise from earlier debug sessions."""
    if not subtopic:
        return ""
    s = subtopic.strip()
    # Drop everything before the LAST occurrence of 'due:'
    while s.lower().startswith("due:"):
        # Strip the 'due:Topic:' prefix
        parts = s.split(":", 2)
        if len(parts) <= 2:
            return parts[-1].strip() if parts else ""
        s = parts[2].strip()
    return s


def _max_or_none(values: list) -> int | None:
    cleaned = [v for v in values if v is not None]
    if not cleaned:
        return None
    return max(cleaned)


def _max_str(values: list[str | None]) -> str | None:
    cleaned = [v for v in values if v]
    if not cleaned:
        return None
    return max(cleaned)


def _most_recent_fsrs_state(rows: list[dict]) -> str | None:
    """Pick the fsrs_state from the row with most recent last_seen / updated_at."""
    candidates = [r for r in rows if r.get("fsrs_state")]
    if not candidates:
        return None
    candidates.sort(key=lambda r: (r.get("last_seen") or "", r.get("updated_at") or ""), reverse=True)
    return candidates[0]["fsrs_state"]


def merge_topic_rows(dry_run: bool = False) -> dict:
    db_path = Path(settings.sqlite_db_path)
    if not db_path.exists():
        return {"error": f"db not found at {db_path}"}
    if not dry_run:
        bak = db_path.with_suffix(db_path.suffix + ".bak.dedupe")
        if not bak.exists():
            shutil.copy2(db_path, bak)

    db = sqlite3.connect(db_path)
    db.row_factory = sqlite3.Row
    rows = [dict(r) for r in db.execute("SELECT * FROM topics").fetchall()]

    # Group by (topic, canonical_subtopic)
    groups: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for r in rows:
        key = (r["topic"], canonicalize_subtopic(r["subtopic"]))
        groups[key].append(r)

    merged_count = 0
    deleted_ids: list[int] = []
    canonical_writes: list[tuple] = []

    for (topic, canon_subtopic), group in groups.items():
        if len(group) <= 1:
            # Even a single-row group needs its subtopic canonicalized if dirty
            r = group[0]
            if r["subtopic"] != canon_subtopic:
                if not dry_run:
                    db.execute(
                        "UPDATE topics SET subtopic=? WHERE topic_id=?",
                        (canon_subtopic, r["topic_id"]),
                    )
                merged_count += 1
            continue

        # Multi-row group: pick the one with most recent activity as the keeper
        group.sort(key=lambda r: (r.get("last_seen") or "", r.get("updated_at") or ""), reverse=True)
        keeper = group[0]
        losers = group[1:]

        merged = {
            "topic": topic,
            "subtopic": canon_subtopic,
            "library": keeper.get("library") or "",
            "training_phase": keeper.get("training_phase") or "",
            "source": keeper.get("source") or "",
            "mastery_score": max(float(r.get("mastery_score") or 0) for r in group),
            "confidence_score": max(float(r.get("confidence_score") or 0) for r in group),
            "status": keeper.get("status") or "new",
            "last_seen": _max_str([r.get("last_seen") for r in group]),
            "last_correct": _max_str([r.get("last_correct") for r in group]),
            "last_partial": _max_str([r.get("last_partial") for r in group]),
            "last_incorrect": _max_str([r.get("last_incorrect") for r in group]),
            "times_seen": sum(int(r.get("times_seen") or 0) for r in group),
            "times_correct": sum(int(r.get("times_correct") or 0) for r in group),
            "times_partial": sum(int(r.get("times_partial") or 0) for r in group),
            "times_incorrect": sum(int(r.get("times_incorrect") or 0) for r in group),
            "next_review_date": _max_str([r.get("next_review_date") for r in group]),
            "forgetting_risk": min(float(r.get("forgetting_risk") or 1.0) for r in group),
            "created_at": min((r.get("created_at") or "9999") for r in group),
            "updated_at": _max_str([r.get("updated_at") for r in group]) or keeper.get("updated_at"),
            "fsrs_state": _most_recent_fsrs_state(group),
        }

        if not dry_run:
            # Delete losers FIRST so the UPDATE on the keeper can take the
            # canonical subtopic without colliding with an existing row.
            for loser in losers:
                db.execute("DELETE FROM topics WHERE topic_id=?", (loser["topic_id"],))
                deleted_ids.append(int(loser["topic_id"]))
            db.execute(
                """UPDATE topics SET
                    subtopic=?, library=?, training_phase=?, source=?,
                    mastery_score=?, confidence_score=?, status=?,
                    last_seen=?, last_correct=?, last_partial=?, last_incorrect=?,
                    times_seen=?, times_correct=?, times_partial=?, times_incorrect=?,
                    next_review_date=?, forgetting_risk=?, fsrs_state=?, updated_at=?
                  WHERE topic_id=?""",
                (
                    merged["subtopic"], merged["library"], merged["training_phase"], merged["source"],
                    merged["mastery_score"], merged["confidence_score"], merged["status"],
                    merged["last_seen"], merged["last_correct"], merged["last_partial"], merged["last_incorrect"],
                    merged["times_seen"], merged["times_correct"], merged["times_partial"], merged["times_incorrect"],
                    merged["next_review_date"], merged["forgetting_risk"], merged["fsrs_state"], merged["updated_at"],
                    keeper["topic_id"],
                ),
            )
        merged_count += 1

    if not dry_run:
        db.commit()
    db.close()

    return {
        "groups_with_dupes": sum(1 for g in groups.values() if len(g) > 1),
        "rows_merged": merged_count,
        "rows_deleted": len(deleted_ids),
        "remaining_rows": len(groups),
        "dry_run": dry_run,
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    summary = merge_topic_rows(dry_run=args.dry_run)
    print("topic dedupe summary:")
    for k, v in summary.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
