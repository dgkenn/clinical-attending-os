"""Partial answers must not be recorded as full misses.

Grading was binary (is_correct: bool), so "named lactulose but gave rifaximin's
mechanism" was recorded identically to "don't know this one at all". In one
30-question session that produced 20 "incorrect" grades where most answers were
substantially right — every one taking a full FSRS lapse: streak reset, lapse
counted, interval collapsed to a day.

The damage is double: the user is buried in false repeats, and the signal that
identifies genuinely fragile facts is destroyed, because near-misses and blanks
look the same in the record.
"""
from __future__ import annotations

from src.mcp_endpoints import submit_answer
from src.student_model import _kp_rating, conn, record_knowledge_point


def _state(point):
    with conn() as db:
        r = db.execute(
            "SELECT status, times_seen, times_correct, consecutive_correct, "
            "interval_days FROM knowledge_points WHERE point = ?", (point,)).fetchone()
    return dict(zip(("status", "seen", "correct", "streak", "interval"), r)) if r else None


def test_fsrs_rating_partial_is_hard_not_again():
    assert _kp_rating(True, 4) == 3       # Good
    assert _kp_rating("partial", 3) == 2  # Hard — a success, not a lapse
    assert _kp_rating(False, 1) == 1      # Again


def test_partial_holds_the_streak_a_miss_resets_it():
    point = "partial streak probe: a distinctive clinical threshold fact"
    for _ in range(2):
        record_knowledge_point(topic="ProbeA", point=point, is_correct=True, confidence=4)
    assert _state(point)["streak"] == 2

    record_knowledge_point(topic="ProbeA", point=point, is_correct="partial", confidence=3)
    after_partial = _state(point)
    assert after_partial["streak"] == 2, "a partial must not reset the streak"
    assert after_partial["status"] == "learning", "a partial is not 'weak'"
    assert after_partial["correct"] == 2, "a partial is not a correct either"

    record_knowledge_point(topic="ProbeA", point=point, is_correct=False, confidence=1)
    assert _state(point)["streak"] == 0
    assert _state(point)["status"] == "weak"


def test_partial_earns_a_longer_interval_than_a_miss():
    # Genuinely distinct wording: record_knowledge_point now fuzzy-dedupes
    # near-identical phrasing onto one row (tests/test_record_kp_dedupe.py),
    # so two probes sharing boilerplate text would merge and defeat this
    # comparison rather than testing partial-vs-miss scheduling.
    a = "Naloxone reverses opioid-induced respiratory depression within minutes of IV administration"
    b = "Ketamine causes emergence reactions more often in adults than in young children"
    for p in (a, b):
        for _ in range(2):
            record_knowledge_point(topic="ProbeB", point=p, is_correct=True, confidence=4)
    record_knowledge_point(topic="ProbeB", point=a, is_correct="partial", confidence=3)
    record_knowledge_point(topic="ProbeB", point=b, is_correct=False, confidence=3)
    assert _state(a)["interval"] > _state(b)["interval"]


def test_submit_answer_records_the_partial_grade():
    r = submit_answer(
        topic="Hepatic disease",
        question="What is first-line for hepatic encephalopathy and why?",
        user_answer="lactulose, but described rifaximin's mechanism",
        is_correct=False, result="partial", confidence_reported=3,
    )
    assert r["ok"] is True
    with conn() as db:
        row = db.execute(
            "SELECT result FROM question_attempts ORDER BY attempt_id DESC LIMIT 1").fetchone()
    assert row[0] == "partial"


def test_is_correct_still_works_for_callers_that_predate_partials():
    r = submit_answer(topic="Hepatic disease", question="back-compat probe",
                      user_answer="a distinct answer body", is_correct=True)
    assert r["ok"] is True
    with conn() as db:
        row = db.execute(
            "SELECT result FROM question_attempts ORDER BY attempt_id DESC LIMIT 1").fetchone()
    assert row[0] == "correct"


def test_a_partial_can_never_confer_mastery():
    point = "mastery probe: partials alone must not master a fact"
    for _ in range(4):
        record_knowledge_point(topic="ProbeC", point=point, is_correct="partial", confidence=4)
    assert _state(point)["status"] != "mastered"


def test_verbatim_exchange_is_stored_with_the_attempt():
    """Auditing a session needs what was actually SAID, not the tutor's account
    of it. `user_answer` is the graded summary ("correctly identified lactulose,
    wrong mechanism") — the tutor's account of the user, not the user's words.
    Repeated audits stalled on exactly this: the user asked whether their stated
    reason for declining a topic was recorded and it was not, because prose
    never reaches the backend unless a tool carries it."""
    from src.student_model import conn
    said = "I'd give calcium first, then insulin and D50. Not sure about kayexalate."
    taught = "Right sequence — calcium stabilises the membrane but does not lower K."
    submit_answer(
        topic="Hyperkalemia",
        question="K 7.1 with peaked T waves, first move?",
        user_answer="correctly sequenced calcium then insulin",
        user_answer_verbatim=said,
        tutor_response=taught,
        is_correct=True, result="correct", confidence_reported=4,
    )
    with conn() as db:
        r = db.execute(
            "SELECT date, user_answer, user_answer_verbatim, tutor_response "
            "FROM question_attempts ORDER BY attempt_id DESC LIMIT 1").fetchone()
    assert r["user_answer_verbatim"] == said, "the user's own words must survive"
    assert r["tutor_response"] == taught, "the teaching must survive"
    assert r["user_answer"] != r["user_answer_verbatim"], "graded summary is kept separately"
    assert r["date"], "every exchange carries a timestamp"


def test_verbatim_capture_is_optional_and_back_compatible():
    """Callers that never learned about it must keep working."""
    r = submit_answer(topic="Hyperkalemia", question="back-compat verbatim probe",
                      user_answer="an answer distinct from others here", is_correct=True)
    assert r["ok"] is True
