"""submit_answer must record the fact-level layer in the same call.

Regression guard for a silent, whole-session data loss: a real 13-question
session recorded every topic-level attempt and ZERO knowledge points. Nothing
errored — the tutor simply never made the separate `submit_knowledge_points`
call, so fact scheduling, ambient triage, and the miss queue got nothing for
that session and no signal said so.

Folding the fact layer into `submit_answer` makes the two writes succeed
together. These tests pin the properties that matter:
  - the points actually land, under the same canonical topic as the attempt
  - a bad point never fails or double-writes the attempt (a raised error would
    invite a client retry, which double-submits the answer and double-advances
    FSRS)
  - correctness is never guessed when the caller omits it
"""
from __future__ import annotations

import pytest

from src.mcp_endpoints import submit_answer
from src.student_model import conn


def _kp_count() -> int:
    with conn() as db:
        return db.execute("SELECT COUNT(*) FROM knowledge_points").fetchone()[0]


def _attempt_count() -> int:
    with conn() as db:
        return db.execute("SELECT COUNT(*) FROM question_attempts").fetchone()[0]


def test_inline_points_are_recorded_under_the_canonical_topic():
    before_kp, before_att = _kp_count(), _attempt_count()

    result = submit_answer(
        topic="Hyperkalemia",
        question="K of 7.1 with peaked T waves - first move?",
        user_answer="calcium gluconate to stabilize, then insulin and glucose to shift",
        is_correct=True,
        confidence_reported=4,
        knowledge_points=[
            {"point": "Calcium stabilizes the myocardium but does not lower K",
             "correct": True, "confidence": 4},
            {"point": "Insulin with glucose shifts K intracellularly", "correct": True,
             "confidence": 3},
        ],
    )

    assert result["ok"] is True
    assert result["knowledge_points_recorded"] == 2
    assert result["knowledge_points_error"] is None
    assert _attempt_count() == before_att + 1
    assert _kp_count() == before_kp + 2

    # Both layers must land on the SAME topic string, or the fact-level queue
    # and the topic-level schedule describe different things.
    canonical = result["canonical_topic"]
    with conn() as db:
        topics = {
            r[0] for r in db.execute(
                "SELECT topic FROM knowledge_points ORDER BY rowid DESC LIMIT 2")
        }
    assert topics == {canonical}


def test_a_bad_point_never_breaks_the_attempt():
    """The attempt is the more important write and is already durable when the
    points are processed. A malformed point must degrade, not raise."""
    before_att = _attempt_count()

    result = submit_answer(
        topic="Hyperkalemia",
        question="follow-up on potassium",
        user_answer="a distinct answer so the dedupe guard does not swallow this",
        is_correct=True,
        knowledge_points=["not an object", None, 42],
    )

    assert result["ok"] is True
    assert result["knowledge_points_recorded"] == 0
    assert _attempt_count() == before_att + 1


def test_missing_correctness_is_skipped_not_guessed():
    """A point with no `correct` key used to default to False and be recorded as
    a genuine failure — weak status, streak reset, FSRS lapse — while returning
    ok. Refusing to guess is the whole point."""
    before_kp = _kp_count()

    result = submit_answer(
        topic="Hyperkalemia",
        question="another follow-up",
        user_answer="yet another distinct answer body for the dedupe guard",
        is_correct=True,
        knowledge_points=[{"point": "a fact with no correctness key"}],
    )

    assert result["ok"] is True
    assert result["knowledge_points_recorded"] == 0
    assert _kp_count() == before_kp


def test_omitting_points_now_derives_one_from_the_question():
    """Backward compatible for CALLERS, but no longer silent.

    This test previously asserted that omitting knowledge_points recorded
    nothing. That contract was the bug: 27 attempts on 2026-06-21 and 30 on
    2026-08-17 produced zero facts, because the tutor almost never supplies
    them. The backend now derives one point from the question rather than
    losing the answer at fact level — see tests/test_derived_knowledge_points.py.
    """
    result = submit_answer(
        topic="Hyperkalemia",
        question="a question with no points supplied",
        user_answer="an answer distinct from the others in this module",
        is_correct=False,
    )
    assert result["ok"] is True
    assert result["knowledge_points_recorded"] == 1
    assert result["knowledge_points_derived"] is True
