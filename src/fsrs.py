"""FSRS-4 (Free Spaced Repetition Scheduler) — pure-dict state.

Implements the algorithm used by Anki's FSRS-4 scheduler. State is a JSON-
serializable dict so it can be stored in a SQLite TEXT column.

Ratings: 1=Again, 2=Hard, 3=Good, 4=Easy.
"""

from __future__ import annotations

import json
import math
from datetime import datetime, timedelta, timezone
from typing import Any

from src.confidence_weighter import apply_confidence_weight_to_interval


W = (
    0.4072, 1.1829, 3.1262, 15.4722,
    7.2102, 0.5316, 1.0651, 0.0234,
    1.616, 0.1544, 1.0824, 1.9813,
    0.0953, 0.2975, 2.2042, 0.2407, 2.9466,
)

REQUEST_RETENTION = 0.9
MAX_INTERVAL_DAYS = 365 * 3
DECAY = -0.5
FACTOR = 19.0 / 81.0


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _to_dt(iso: str | None) -> datetime | None:
    if not iso:
        return None
    return datetime.fromisoformat(iso.replace("Z", "+00:00"))


def fsrs_init() -> dict[str, Any]:
    return {
        "stability": 0.0,
        "difficulty": 0.0,
        "lapses": 0,
        "reps": 0,
        "last_review": None,
        "next_due": None,
        "state": "new",
    }


def _retrievability(stability: float, elapsed_days: float) -> float:
    if stability <= 0:
        return 0.0
    return (1.0 + FACTOR * elapsed_days / stability) ** DECAY


def _interval_days(stability: float) -> int:
    if stability <= 0:
        return 1
    days = (stability / FACTOR) * (REQUEST_RETENTION ** (1.0 / DECAY) - 1.0)
    return max(1, min(MAX_INTERVAL_DAYS, round(days)))


def _initial_difficulty(rating: int) -> float:
    d = W[4] - math.exp(W[5] * (rating - 1)) + 1.0
    return min(10.0, max(1.0, d))


def _initial_stability(rating: int) -> float:
    return max(0.1, W[max(0, rating - 1)])


def _next_difficulty(d: float, rating: int) -> float:
    delta = -W[6] * (rating - 3)
    new_d = d + delta * (10.0 - d) / 9.0
    target = W[4] - math.exp(W[5] * (4 - 1)) + 1.0
    new_d = W[7] * target + (1.0 - W[7]) * new_d
    return min(10.0, max(1.0, new_d))


def _next_stability_success(d: float, s: float, r: float, rating: int) -> float:
    hard_penalty = W[15] if rating == 2 else 1.0
    easy_bonus = W[16] if rating == 4 else 1.0
    growth = (
        math.exp(W[8])
        * (11.0 - d)
        * (s ** -W[9])
        * (math.exp(W[10] * (1.0 - r)) - 1.0)
        * hard_penalty
        * easy_bonus
        + 1.0
    )
    return max(0.1, s * growth)


def _next_stability_lapse(d: float, s: float, r: float) -> float:
    new_s = (
        W[11]
        * (d ** -W[12])
        * (((s + 1.0) ** W[13]) - 1.0)
        * math.exp(W[14] * (1.0 - r))
    )
    return max(0.1, new_s)


def fsrs_review(
    state: dict[str, Any],
    rating: int,
    now: datetime | None = None,
    confidence_reported: int | None = None,
) -> tuple[dict[str, Any], str]:
    if rating not in (1, 2, 3, 4):
        raise ValueError(f"rating must be 1-4, got {rating}")
    now = now or _now()
    s = dict(state) if state else fsrs_init()
    last = _to_dt(s.get("last_review"))
    elapsed = max(0.0, (now - last).total_seconds() / 86400.0) if last else 0.0

    if s.get("state", "new") == "new" or s.get("stability", 0.0) <= 0.0:
        s["stability"] = _initial_stability(rating)
        s["difficulty"] = _initial_difficulty(rating)
    else:
        retr = _retrievability(s["stability"], elapsed)
        s["difficulty"] = _next_difficulty(s["difficulty"], rating)
        if rating == 1:
            s["stability"] = _next_stability_lapse(s["difficulty"], s["stability"], retr)
            s["lapses"] = int(s.get("lapses", 0)) + 1
        else:
            s["stability"] = _next_stability_success(
                s["difficulty"], s["stability"], retr, rating
            )

    interval = _interval_days(s["stability"])

    # Apply confidence-based weighting if confidence_reported is provided
    if confidence_reported is not None and confidence_reported >= 1 and confidence_reported <= 5:
        is_correct = rating in (3, 4)  # ratings 3=good, 4=easy are correct
        weighted_interval = apply_confidence_weight_to_interval(
            interval, is_correct, confidence_reported
        )
        # Re-floor AFTER weighting: _interval_days floors at 1 day, but x0.7 on
        # a 1-day lapse gives 0.7 days, and date-truncated storage then makes
        # the item due again the SAME day — each same-day re-fail re-runs the
        # lapse (elapsed≈0, retrievability≈1), stacking lapses/stability loss
        # for what is pedagogically a single day's failure.
        interval = max(1.0, weighted_interval)

    next_due = (now + timedelta(days=interval)).isoformat()
    s["last_review"] = now.isoformat()
    s["next_due"] = next_due
    s["reps"] = int(s.get("reps", 0)) + 1
    s["state"] = "review" if rating != 1 else "relearning"
    return s, next_due


def due_now(state: dict[str, Any] | None, now: datetime | None = None) -> bool:
    if not state:
        return True
    next_due = _to_dt(state.get("next_due"))
    if next_due is None:
        return True
    return (now or _now()) >= next_due


def retrievability_now(state: dict[str, Any] | None, now: datetime | None = None) -> float:
    if not state or state.get("stability", 0.0) <= 0:
        return 0.0
    last = _to_dt(state.get("last_review"))
    if last is None:
        return 0.0
    elapsed = max(0.0, ((now or _now()) - last).total_seconds() / 86400.0)
    return _retrievability(state["stability"], elapsed)


def serialize(state: dict[str, Any]) -> str:
    return json.dumps(state, sort_keys=True, separators=(",", ":"))


def deserialize(text: str | None) -> dict[str, Any]:
    if not text:
        return fsrs_init()
    try:
        return json.loads(text)
    except Exception:
        return fsrs_init()


def mastery_proxy(state: dict[str, Any] | None) -> float:
    """Derive a 0-1 mastery score from FSRS state for backward compat."""
    if not state:
        return 0.0
    s = float(state.get("stability", 0.0))
    if s <= 0:
        return 0.0
    return min(1.0, math.log1p(s) / math.log1p(180.0))


def next_review_date_from_state(state: dict[str, Any] | None) -> str:
    if state and state.get("next_due"):
        return state["next_due"][:10]
    return _now().date().isoformat()
