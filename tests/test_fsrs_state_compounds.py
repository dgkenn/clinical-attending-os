"""Repeated correct answers must actually buy longer intervals.

The maintainer's complaint — "I feel like I'm constantly reviewing information
that I already know" — turned out to be measurable rather than a feeling. A
sweep found 41 of 168 studied facts whose FSRS `reps` did not match
`times_seen`: counters climbing while the scheduling state stayed near its
initial value. The worst case had been answered 19 times, 16 of them correctly,
and still carried reps=3 and stability 7.68, so it kept returning as though it
were nearly new.

39 of the 41 were created in late June, before per-fact FSRS state existed, so
the cause was one-time migration debt rather than an ongoing leak. These tests
pin the CURRENT behaviour so it stays that way: state must load, compound, and
survive the paths that write it.
"""
from __future__ import annotations

import json

import pytest

from src.student_model import conn, record_knowledge_point

TOPIC = "FsrsCompoundProbe"


def _state(point):
    with conn() as db:
        row = db.execute(
            "SELECT fsrs_state, interval_days, times_seen FROM knowledge_points "
            "WHERE topic=? AND point=?", (TOPIC, point)).fetchone()
    return (json.loads(row["fsrs_state"] or "{}"), row["interval_days"],
            row["times_seen"]) if row else ({}, 0, 0)


def test_reps_track_every_recorded_answer():
    """The exact invariant that was violated: counters and state must agree."""
    point = "Fsrs probe: a distinctive fictional threshold for compounding"
    for _ in range(4):
        record_knowledge_point(topic=TOPIC, point=point, is_correct=True, confidence=4)
    st, _interval, seen = _state(point)
    assert seen == 4
    assert st.get("reps") == 4, (
        f"FSRS state lost answers: reps={st.get('reps')} vs times_seen={seen}")


def test_same_day_repeats_deliberately_earn_nothing():
    """Answering the same fact four times in one minute must NOT quadruple the
    interval. FSRS gives near-zero credit for zero elapsed time, and that is
    correct: massed repetition does not build durable memory.

    Written down because the first version of this test asserted the opposite
    and "failed", which briefly looked like a broken scheduler.
    """
    point = "Fsrs probe: another distinctive fictional consolidation threshold"
    intervals = []
    for _ in range(4):
        record_knowledge_point(topic=TOPIC, point=point, is_correct=True, confidence=4)
        intervals.append(_state(point)[1])
    assert intervals[-1] == intervals[0], f"massed repetition paid off: {intervals}"


def test_spaced_corrects_compound_hard():
    """The property that actually matters: when the scheduled interval really
    elapses, repetition buys exponentially more time. Measured 3 -> 11 -> 36 ->
    104 days, so a well-known fact leaves the rotation instead of nagging."""
    import json as _json
    from datetime import datetime, timedelta, timezone

    point = "Fsrs probe: a spaced distinctive fictional retention threshold"
    intervals = []
    for _ in range(4):
        record_knowledge_point(topic=TOPIC, point=point, is_correct=True, confidence=4)
        st, interval, _ = _state(point)
        intervals.append(interval)
        # Fast-forward so the next review happens when it was actually due.
        elapsed = max(1.0, float(interval or 1))
        st["last_review"] = (datetime.now(timezone.utc) - timedelta(days=elapsed)).isoformat()
        with conn() as db:
            db.execute("UPDATE knowledge_points SET fsrs_state=?, updated_at=? "
                       "WHERE topic=? AND point=?",
                       (_json.dumps(st),
                        (datetime.now(timezone.utc) - timedelta(days=elapsed)).isoformat(),
                        TOPIC, point))
    assert intervals == sorted(intervals), f"intervals did not grow: {intervals}"
    assert intervals[-1] >= 30, f"four spaced corrects still returns in {intervals[-1]:.0f}d"


def test_a_partial_does_not_wipe_accumulated_stability():
    """A partial is FSRS 'Hard' — a smaller gain, never a reset to baseline."""
    point = "Fsrs probe: a fourth distinctive fictional partial-credit threshold"
    for _ in range(3):
        record_knowledge_point(topic=TOPIC, point=point, is_correct=True, confidence=4)
    before = _state(point)[0].get("stability", 0)
    record_knowledge_point(topic=TOPIC, point=point, is_correct="partial", confidence=3)
    after, interval, _ = _state(point)[0], _state(point)[1], None
    assert after.get("reps") == 4
    assert after.get("lapses", 0) == 0, "a partial must not count as a lapse"
    assert after.get("stability", 0) > before * 0.5, (
        f"partial collapsed stability {before:.1f} -> {after.get('stability'):.1f}")


def test_a_miss_lapses_without_erasing_the_history():
    point = "Fsrs probe: a fifth distinctive fictional lapse threshold"
    for _ in range(3):
        record_knowledge_point(topic=TOPIC, point=point, is_correct=True, confidence=4)
    record_knowledge_point(topic=TOPIC, point=point, is_correct=False, confidence=2)
    st, interval, seen = _state(point)
    assert st.get("lapses") == 1
    assert st.get("reps") == 4, "a miss must not roll the rep count back"
    assert seen == 4
