"""Correcting a grade must amend the answer, not record a second one.

A tamponade answer was graded partial; the user pointed out it was
mechanistically complete; the tutor "reclassified" it by calling submit_answer
again. The result: two attempt rows for one answer, the original partial still
standing in the record, and the fact's FSRS state advanced TWICE. Two advances
halve the interval and can reach 'mastered' off a single exchange — the same
double-count that car mode produced by a different route.
"""
from __future__ import annotations

import pytest

from src.mcp_server import revise_last_answer
from src.mcp_endpoints import submit_answer
from src.student_model import conn

TOPIC = "RegradeProbeTopic"


def _attempts():
    with conn() as db:
        return db.execute(
            "SELECT attempt_id, result, notes FROM question_attempts WHERE topic=? "
            "ORDER BY attempt_id", (TOPIC,)).fetchall()


def test_a_regrade_amends_in_place_instead_of_appending():
    submit_answer(topic=TOPIC, question="probe question for regrade",
                  user_answer="a partial-looking answer", is_correct=False,
                  result="partial", user_answer_verbatim="a partial-looking answer",
                  tutor_response="Close, but let me tighten one piece.")
    before = len(_attempts())
    out = revise_last_answer(TOPIC, "correct", reason="user was right")
    assert out["ok"] is True
    after = _attempts()
    assert len(after) == before, "a regrade must not write a second attempt"
    assert after[-1]["result"] == "correct"
    assert "regraded" in (after[-1]["notes"] or ""), "the change must be auditable"
    assert out["was"] == "partial" and out["now"] == "correct"


def test_the_fact_is_not_credited_twice():
    point = "Regrade probe: the fictional Quandel threshold sits at 12 units"
    submit_answer(topic=TOPIC, question="probe question two",
                  user_answer="answer two", is_correct=False, result="partial",
                  user_answer_verbatim="answer two", tutor_response="Nearly.",
                  knowledge_points=[{"point": point, "correct": False}])
    with conn() as db:
        before = db.execute(
            "SELECT times_seen, times_correct FROM knowledge_points WHERE point=?",
            (point,)).fetchone()
    revise_last_answer(TOPIC, "correct", point=point)
    with conn() as db:
        after = db.execute(
            "SELECT times_seen, times_correct FROM knowledge_points WHERE point=?",
            (point,)).fetchone()
    assert after["times_seen"] == before["times_seen"], "regrade must not re-count the attempt"
    assert after["times_correct"] == before["times_correct"] + 1


@pytest.mark.parametrize("bad", ["", "sort-of", "right"])
def test_a_nonsense_verdict_is_refused(bad):
    assert revise_last_answer(TOPIC, bad)["ok"] is False


def test_regrading_an_untouched_topic_fails_loudly():
    out = revise_last_answer("NeverAnsweredProbeTopic", "correct")
    assert out["ok"] is False and "no recorded answer" in out["error"]
