"""Weak-pattern aggregator.

Reads `question_attempts` and surfaces:
- Per-mistake-type counts (rolling 30 days)
- Repeat-offender (topic, mistake_type) pairs with >=2 incorrect attempts
- Overconfidence rate (incorrect attempts where confidence_reported >= 4 / total
  incorrect attempts that recorded confidence)

The Custom GPT calls this to focus next sessions, e.g. "you keep failing
prioritization on electrolyte topics — let's drill those."
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any

from .schemas import WeakPatternEntry, WeakPatternsResponse
from .student_model import conn, initialize_database


def compute_weak_patterns(window_days: int = 30) -> WeakPatternsResponse:
    initialize_database()
    cutoff = (datetime.now(timezone.utc) - timedelta(days=window_days)).isoformat()
    with conn() as db:
        rows = db.execute(
            """SELECT topic, mistake_type, result, confidence_reported, date
               FROM question_attempts
               WHERE date >= ?""",
            (cutoff,),
        ).fetchall()
    rows = [dict(r) for r in rows]

    by_mistake_type: dict[str, int] = {}
    pair_failures: dict[tuple[str, str], dict[str, Any]] = {}
    confident_total = 0
    confident_wrong = 0

    for r in rows:
        if r["result"] != "incorrect":
            if r.get("confidence_reported") is not None and r["confidence_reported"] >= 4:
                confident_total += 1
            continue
        mt = r.get("mistake_type") or "other"
        by_mistake_type[mt] = by_mistake_type.get(mt, 0) + 1
        topic = r.get("topic") or ""
        key = (topic, mt)
        rec = pair_failures.setdefault(key, {"failures": 0, "last_seen": None})
        rec["failures"] += 1
        if not rec["last_seen"] or r["date"] > rec["last_seen"]:
            rec["last_seen"] = r["date"]
        if r.get("confidence_reported") is not None:
            if r["confidence_reported"] >= 4:
                confident_total += 1
                confident_wrong += 1

    repeat_offenders = [
        WeakPatternEntry(
            topic=topic,
            mistake_type=mt,
            failures=rec["failures"],
            last_seen=rec["last_seen"],
        )
        for (topic, mt), rec in pair_failures.items()
        if rec["failures"] >= 2
    ]
    repeat_offenders.sort(key=lambda e: -e.failures)
    overconfidence_rate = (confident_wrong / confident_total) if confident_total else 0.0
    return WeakPatternsResponse(
        by_mistake_type=by_mistake_type,
        repeat_offenders=repeat_offenders,
        rolling_30d_attempts=len(rows),
        overconfidence_rate=round(overconfidence_rate, 3),
    )
