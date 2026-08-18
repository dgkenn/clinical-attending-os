"""The user's own correction of the knowledge ledger.

Both directions matter and they fail differently. A fact wrongly believed KNOWN
is silently never asked again, so the gap surfaces on a patient rather than in a
session. A fact wrongly believed UNKNOWN wastes review time, which is the
failure the maintainer says would make him abandon the system.

The precedent is concrete: he declined the "consults" card out loud mid-session,
reasoning that it was a checklist rather than clinical knowledge, and that
judgement reached the backend nowhere — he had to raise it again later and ask
whether it had been recorded anywhere. It had not.
"""
from __future__ import annotations

import pytest

from src.mcp_server import mark_known, mark_unknown
from src.student_model import conn, record_knowledge_point

TOPIC = "OverrideProbeTopic"
POINT = "Override probe: a distinctive fictional threshold for the probe index"


@pytest.fixture
def seeded_fact():
    record_knowledge_point(topic=TOPIC, point=POINT, is_correct=False, confidence=2)
    with conn() as db:
        row = db.execute(
            "SELECT point FROM knowledge_points WHERE topic=? ORDER BY id DESC LIMIT 1",
            (TOPIC,)).fetchone()
    return row["point"]


def _row(point):
    with conn() as db:
        return db.execute(
            "SELECT * FROM knowledge_points WHERE topic=? AND point=?",
            (TOPIC, point)).fetchone()


def test_marking_known_parks_the_fact_and_stops_the_drilling(seeded_fact):
    out = mark_known(TOPIC, seeded_fact, reason="it's a checklist, not clinical knowledge")
    assert out["ok"] is True
    row = _row(seeded_fact)
    assert row["status"] == "mastered"
    assert row["interval_days"] == 90, "must actually leave the rotation, not just re-rank"


def test_the_users_stated_reason_is_preserved(seeded_fact):
    """The whole failure was a reason that existed only in conversation."""
    mark_known(TOPIC, seeded_fact, reason="it's a checklist, not clinical knowledge")
    assert "checklist" in _row(seeded_fact)["evidence"]


def test_marking_unknown_resets_it_and_brings_it_back(seeded_fact):
    mark_known(TOPIC, seeded_fact)
    out = mark_unknown(TOPIC, seeded_fact, reason="I was parroting you, I don't have this")
    assert out["ok"] is True
    row = _row(seeded_fact)
    assert row["status"] == "weak"
    assert row["consecutive_correct"] == 0
    assert row["mistake_type"] == "self_reported_gap"
    assert row["fsrs_state"] is None, "the schedule that produced the wrong belief must go"
    assert "parroting" in row["evidence"]


def test_unknown_overrides_a_previously_earned_mastery(seeded_fact):
    """A fact can reach 'mastered' through parroting. The user saying they do
    not have it must win over the accumulated record."""
    for _ in range(3):
        record_knowledge_point(topic=TOPIC, point=seeded_fact, is_correct=True, confidence=5)
    assert _row(seeded_fact)["status"] == "mastered"
    mark_unknown(TOPIC, seeded_fact, reason="never actually knew this")
    assert _row(seeded_fact)["status"] == "weak"


def test_an_unrecognised_fact_reports_failure_rather_than_silently_passing():
    """A no-op that returns ok is how the consults report was lost the first
    time — the tutor would tell the user it was handled when nothing happened."""
    out = mark_known(TOPIC, "a point that was never served to anyone")
    assert out["ok"] is False
    assert "no such fact" in out["error"]


@pytest.mark.parametrize("fn", [mark_known, mark_unknown])
def test_blank_arguments_are_rejected(fn):
    assert fn("", "something")["ok"] is False
    assert fn(TOPIC, "")["ok"] is False
