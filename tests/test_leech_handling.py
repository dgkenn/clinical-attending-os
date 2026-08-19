"""A fact asked repeatedly and never answered right is not a review problem.

Spaced repetition assumes the item eventually gets learned; the schedule only
decides WHEN to re-test. An item that is never learned has nothing to space, so
it loops: every miss pins it at a one-day interval, it returns tomorrow, it is
missed again. Four such facts were generating review load out of all proportion
to what they taught.

The fix is not scheduling. It is recognising that a fourth interrogation records
nothing useful and the fact needs teaching — or the card is unanswerable as
written and needs rewriting.
"""
from __future__ import annotations

from src.mcp_server import get_due_knowledge_points
from src.student_model import conn, record_knowledge_point

TOPIC = "LeechProbeTopic"


def test_a_repeatedly_missed_fact_is_flagged_for_teaching():
    point = "Leech probe: a distinctive fictional threshold never answered right"
    for _ in range(3):
        record_knowledge_point(topic=TOPIC, point=point, is_correct=False, confidence=1)
    # Make it due despite the same-day guard.
    with conn() as db:
        db.execute("UPDATE knowledge_points SET next_review_date=date('now','-1 day'), "
                   "updated_at=datetime('now','-2 days') WHERE point=?", (point,))
    served = get_due_knowledge_points(limit=500)
    hit = next((p for p in served["todays_set"] if p["point"] == point), None)
    assert hit is not None, "the leech should still be served — it is a real gap"
    assert hit.get("leech") is True
    assert "teach" in hit["leech_note"].lower()
    assert point in served["leeches"]
    assert "leech" in served["note"]


def test_a_fact_answered_right_at_least_once_is_not_a_leech():
    """Getting it right once means the item IS learnable — that is ordinary
    spaced repetition, not a loop."""
    point = "Leech probe: a distinctive fictional threshold answered once"
    record_knowledge_point(topic=TOPIC, point=point, is_correct=True, confidence=4)
    for _ in range(3):
        record_knowledge_point(topic=TOPIC, point=point, is_correct=False, confidence=1)
    with conn() as db:
        db.execute("UPDATE knowledge_points SET next_review_date=date('now','-1 day'), "
                   "updated_at=datetime('now','-2 days') WHERE point=?", (point,))
    served = get_due_knowledge_points(limit=500)
    hit = next((p for p in served["todays_set"] if p["point"] == point), None)
    if hit:
        assert not hit.get("leech")


def test_two_misses_is_not_yet_a_leech():
    """The threshold has to be high enough that ordinary early failure — which
    is what learning looks like — is not mistaken for a stuck item."""
    point = "Leech probe: a distinctive fictional threshold missed twice"
    for _ in range(2):
        record_knowledge_point(topic=TOPIC, point=point, is_correct=False, confidence=1)
    with conn() as db:
        db.execute("UPDATE knowledge_points SET next_review_date=date('now','-1 day'), "
                   "updated_at=datetime('now','-2 days') WHERE point=?", (point,))
    served = get_due_knowledge_points(limit=500)
    hit = next((p for p in served["todays_set"] if p["point"] == point), None)
    if hit:
        assert not hit.get("leech")
