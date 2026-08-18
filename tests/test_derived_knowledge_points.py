"""Answering a question must always leave a fact-level record.

This is the most persistent failure the system has had. Recording a fact
required a SECOND deliberate act by the tutor — decomposing the answer into
knowledge points — on top of recording the attempt, and that act was skipped
most of the time:

    2026-06-21    27 attempts  ->   0 knowledge points
    2026-08-17    30 attempts  ->   0 knowledge points

So studying registered at topic level and vanished at fact level. The fact
queue kept re-serving material already covered, and the user had to keep
correcting the record by hand ("I already did those").

The backend always held what it needed: the question, the answer, the result,
the confidence. When the tutor supplies nothing, one point is now derived from
the question — coarser than a hand-decomposed fact, but it makes the fact-level
schedule real instead of empty, and re-asking the same question updates the
same point rather than creating another.
"""
from __future__ import annotations

from src.mcp_endpoints import submit_answer
from src.student_model import conn


def _kp_count() -> int:
    with conn() as db:
        return db.execute("SELECT COUNT(*) FROM knowledge_points").fetchone()[0]


def test_a_bare_answer_still_records_a_fact():
    before = _kp_count()
    result = submit_answer(
        topic="Hyperkalemia",
        question="K of 7.1 with peaked T waves - what is your first move?",
        user_answer="calcium gluconate to stabilise the membrane",
        is_correct=True,
        confidence_reported=4,
    )
    assert result["ok"] is True
    assert result["knowledge_points_derived"] is True
    assert result["knowledge_points_recorded"] == 1
    assert _kp_count() == before + 1


def test_reasking_updates_the_same_fact_rather_than_duplicating():
    """Otherwise every re-ask would mint a new 'weak' fact and the queue would
    grow forever instead of converging."""
    q = "Which vasopressor is first-line in septic shock?"
    submit_answer(topic="Vasopressors", question=q,
                  user_answer="norepinephrine", is_correct=True, confidence_reported=4)
    before = _kp_count()
    submit_answer(topic="Vasopressors", question=q,
                  user_answer="norepinephrine, phrased differently this time",
                  is_correct=True, confidence_reported=5)
    assert _kp_count() == before


def test_explicit_points_take_precedence_over_derivation():
    before = _kp_count()
    result = submit_answer(
        topic="Hyperkalemia",
        question="a distinct question about potassium shifts",
        user_answer="insulin and D50 shift it intracellularly",
        is_correct=True,
        knowledge_points=[
            {"point": "Insulin with D50 shifts K intracellularly", "correct": True,
             "confidence": 4},
            {"point": "Calcium does not lower serum K", "correct": True, "confidence": 3},
        ],
    )
    assert result["knowledge_points_derived"] is False
    assert result["knowledge_points_recorded"] == 2
    assert _kp_count() == before + 2


def test_nothing_is_invented_without_a_real_question():
    """The fallback identity IS the question. With no question there is no fact
    to name, and inventing one would put junk in the review queue."""
    before = _kp_count()
    result = submit_answer(
        topic="Hyperkalemia",
        user_answer="an answer with no question recorded",
        is_correct=False,
    )
    assert result["knowledge_points_derived"] is False
    assert result["knowledge_points_recorded"] == 0
    assert _kp_count() == before


def test_a_wrong_answer_derives_a_weak_fact():
    """The point of the fact layer is to resurface misses — a derived point must
    carry the failure, not be recorded as neutral."""
    q = "What is the maximum sodium correction rate in 24 hours?"
    submit_answer(topic="Hyponatremia", question=q,
                  user_answer="no idea", is_correct=False, confidence_reported=2)
    with conn() as db:
        row = db.execute(
            "SELECT status, times_correct FROM knowledge_points WHERE point = ?",
            (q,)).fetchone()
    assert row is not None, "a missed question must leave a fact behind"
    assert row[1] == 0
