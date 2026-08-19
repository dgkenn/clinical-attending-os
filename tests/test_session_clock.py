"""The tutor was guessing at time and getting it badly wrong.

The maintainer asked for 30 minutes, was given 8 questions in 11.6 minutes, and
was wound down well before the time he had set aside. The tutor has no wall
clock, so every statement it made about remaining time was invented. In an
intern year the protected study block is the scarce resource; spending half of
it and stopping is a real cost.

Pacing is measured, not assumed: 127 recorded inter-question gaps give a median
of 77 s/question, and whole sessions run 69-99 s/question. So 30 minutes is
about 20 questions.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pytest

from src.session_clock import (
    DEFAULT_SECONDS_PER_QUESTION,
    WRAP_UP_MINUTES,
    end_clock,
    pacing,
    plan_for,
    start_clock,
)
from src.student_model import conn


class TestPlanning:
    def test_thirty_minutes_buys_about_twenty_questions_not_eight(self):
        """The concrete regression."""
        plan = plan_for(30)
        assert plan["mode"] == "timed"
        assert 15 <= plan["question_budget"] <= 25, plan

    def test_fifteen_minutes_is_planned_smaller(self):
        assert plan_for(15)["question_budget"] < plan_for(30)["question_budget"]

    def test_an_hour_scales_up(self):
        assert plan_for(60)["question_budget"] >= 2 * plan_for(30)["question_budget"] - 2

    def test_zero_minutes_means_backlog_mode_not_zero_questions(self):
        """"As much time as we need" is a different goal, not a tiny session."""
        plan = plan_for(0)
        assert plan["mode"] == "unlimited"
        assert "overdue_backlog" in plan
        assert plan["question_budget"] == plan["overdue_backlog"]


class TestClock:
    def test_a_fresh_clock_reports_the_full_duration(self):
        out = start_clock(30)
        assert out["mode"] == "timed"
        assert out["planned_minutes"] == 30
        assert out["remaining_minutes"] > 25
        assert out["questions_asked"] == 0
        assert "now_local" in out and "ends_local" in out

    def test_guidance_forbids_winding_down_early(self):
        start_clock(30)
        out = pacing()
        assert "do NOT wind down" in out["guidance"].lower() or \
               "not wind down" in out["guidance"].lower()

    def test_time_up_says_wrap_up(self):
        start_clock(30)
        out = pacing(now=datetime.now(timezone.utc) + timedelta(minutes=31))
        assert out["remaining_minutes"] <= 0
        assert "wrap up" in out["guidance"].lower()

    def test_the_final_minutes_trigger_wrap_up_not_a_new_question(self):
        start_clock(30)
        out = pacing(now=datetime.now(timezone.utc) + timedelta(minutes=29))
        assert out["questions_remaining"] == 0
        assert "wrap up" in out["guidance"].lower()

    def test_midsession_still_offers_a_real_question_budget(self):
        start_clock(30)
        out = pacing(now=datetime.now(timezone.utc) + timedelta(minutes=10))
        assert out["questions_remaining"] >= 8, out
        assert out["remaining_minutes"] == pytest.approx(20, abs=1)

    def test_unlimited_mode_targets_the_backlog_and_refuses_to_wrap_early(self):
        out = start_clock(0)
        assert out["mode"] == "unlimited"
        assert out["goal"] == "clear the overdue backlog"
        assert "overdue_backlog" in out
        if out["overdue_backlog"]:
            assert "do NOT wrap up early" in out["guidance"]

    def test_a_wrap_up_reserve_is_held_back(self):
        """The budget must not consume the recap."""
        start_clock(20)
        out = pacing()
        usable = (20 - WRAP_UP_MINUTES) * 60
        assert out["questions_remaining"] <= usable // DEFAULT_SECONDS_PER_QUESTION

    def test_no_clock_tells_the_tutor_to_start_one(self):
        with conn() as db:
            db.execute("CREATE TABLE IF NOT EXISTS session_clock ("
                       "id INTEGER PRIMARY KEY CHECK (id=1), started_at TEXT NOT NULL,"
                       " planned_minutes INTEGER NOT NULL, ended_at TEXT)")
            db.execute("DELETE FROM session_clock")
        out = pacing()
        assert out["clock_running"] is False
        assert "start_study_session" in out["note"]

    def test_ending_the_clock_stops_it_without_losing_the_numbers(self):
        start_clock(30)
        end_clock()
        out = pacing()
        assert out["clock_running"] is False
        assert "elapsed_minutes" in out


class TestPacingReachesTheTutor:
    def test_submit_answer_returns_pacing_inline(self):
        """A separate call would be forgettable and would cost a round trip
        mid-explanation — the latency the maintainer already complained about."""
        from src.mcp_endpoints import submit_answer

        start_clock(30)
        out = submit_answer(
            topic="ClockProbeTopic", question="probe question for pacing",
            user_answer="a distinct probe answer", is_correct=True,
            user_answer_verbatim="a distinct probe answer",
            tutor_response="Correct, and here is the mechanism behind it.")
        assert "pacing" in out
        assert out["pacing"]["clock_running"] is True
        assert out["pacing"]["remaining_minutes"] > 0

    def test_missing_verbatim_is_warned_and_salvaged_from_evidence(self):
        """A whole session sent grounded_in and per-fact evidence but zero
        verbatim and zero tutor_response, silently disabling echo detection."""
        from src.mcp_endpoints import submit_answer

        out = submit_answer(
            topic="ClockProbeTopic2", question="probe question",
            user_answer="graded summary only", is_correct=True,
            knowledge_points=[{"point": "ClockProbe: a distinctive probe threshold fact",
                               "correct": True,
                               "evidence": "the user's own phrasing here"}])
        assert any("verbatim" in w for w in out["warnings"])
        assert any("tutor_response" in w for w in out["warnings"])

    def test_a_taught_fact_is_not_filed_as_untested_when_tutor_response_is_missing(self):
        """Missing evidence must not be read as evidence of absence: without the
        tutor's words there is nothing to judge coverage against, and real gaps
        (hyperkalemia calcium, vasopressin second agent) were being filed as
        never-presented new material instead of queued for drilling."""
        from src.mcp_endpoints import submit_answer

        out = submit_answer(
            topic="ClockProbeTopic3", question="what is the first step?",
            user_answer="missed it", is_correct=False, result="incorrect",
            user_answer_verbatim="I don't know that one",
            knowledge_points=[{"point": "ClockProbe: an unrelated distinctive threshold fact",
                               "correct": False}])
        assert out["facts_not_covered_this_turn"] == []


class TestStaleClocks:
    """A clock left running is worse than no clock.

    One session called start_study_session at 09:29 — five minutes AFTER its
    last answer at 09:24 — and never closed it, so the row stayed "running" and
    every later reading was nonsense. Pacing that confidently reports the wrong
    time is how a 30-minute session gets wound up at 11 minutes.
    """

    def _plant(self, started_minutes_ago: int, planned: int):
        from datetime import datetime, timedelta, timezone
        from src.student_model import conn
        started = datetime.now(timezone.utc) - timedelta(minutes=started_minutes_ago)
        with conn() as db:
            db.execute("CREATE TABLE IF NOT EXISTS session_clock ("
                       "id INTEGER PRIMARY KEY CHECK (id=1), started_at TEXT NOT NULL,"
                       " planned_minutes INTEGER NOT NULL, ended_at TEXT)")
            db.execute("INSERT INTO session_clock (id, started_at, planned_minutes, ended_at) "
                       "VALUES (1,?,?,NULL) ON CONFLICT(id) DO UPDATE SET "
                       "started_at=excluded.started_at, planned_minutes=excluded.planned_minutes, "
                       "ended_at=NULL", (started.isoformat(), planned))

    def test_a_long_overrun_timed_clock_is_treated_as_expired(self):
        self._plant(started_minutes_ago=400, planned=20)
        out = pacing()
        assert out["clock_running"] is False
        assert out.get("stale_clock") is True
        assert "start_study_session" in out["note"]

    def test_an_abandoned_unlimited_clock_expires_too(self):
        self._plant(started_minutes_ago=600, planned=0)
        out = pacing()
        assert out.get("stale_clock") is True

    def test_a_session_running_slightly_long_is_NOT_stale(self):
        """Overrunning by a few minutes is normal and must still report time."""
        self._plant(started_minutes_ago=35, planned=30)
        out = pacing()
        assert out["clock_running"] is True
        assert out.get("stale_clock") is None
        assert out["remaining_minutes"] < 0
