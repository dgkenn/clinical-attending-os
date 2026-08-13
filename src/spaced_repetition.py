from __future__ import annotations

from datetime import datetime, timedelta, timezone


def interval_for_mastery(mastery: float) -> int:
    if mastery < 0.4:
        return 1
    if mastery < 0.6:
        return 3
    if mastery < 0.8:
        return 7
    if mastery < 0.9:
        return 21
    return 60


def next_review_date(mastery: float) -> str:
    return (datetime.now(timezone.utc) + timedelta(days=interval_for_mastery(mastery))).date().isoformat()


def forgetting_risk(mastery: float, days_since_seen: int, times_correct: int) -> float:
    risk = 0.1 + (1.0 - mastery) * 0.65 + min(days_since_seen / 90, 0.35) - min(times_correct * 0.025, 0.15)
    return round(max(0.05, min(1.0, risk)), 3)


def status_for_mastery(mastery: float) -> str:
    if mastery < 0.3:
        return "weak"
    if mastery < 0.6:
        return "unstable"
    if mastery < 0.8:
        return "learning"
    if mastery < 0.9:
        return "strong"
    return "maintenance"

