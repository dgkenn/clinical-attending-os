"""Car mode had quietly become a second, poorer recording path.

A real hands-free session on 2026-08-19 recorded 5 answers with ZERO verbatim,
ZERO tutor response, ZERO grounding and ZERO per-fact evidence — not because the
tutor was careless, but because `CarAnsweredInput` had no such fields. Every
capture improvement built over the preceding days landed on `submit_answer`
alone, and nothing errored: the session simply produced an unauditable record,
with echo detection unable to run because it compares the user's words against
the tutor's previous turn and both were absent.

Car mode is where verbatim matters MOST. The answer is spoken, there is no chat
log to fall back on, and the maintainer cannot inspect what was recorded while
driving. Same reason the clock matters more here: a driver cannot glance at a
screen to see how long is left.

Also guarded: `submit_knowledge_points` accepted an `evidence` key and dropped
it before calling record_knowledge_point, so every fact written through the only
fact path car mode uses stored empty evidence no matter how well it was quoted.
"""
from __future__ import annotations

import pytest

from src.schemas import CarAnsweredInput, CarNextRequest


class TestSchemaAcceptsCapture:
    def test_the_capture_fields_exist(self):
        fields = set(CarAnsweredInput.model_fields)
        for f in ("user_answer_verbatim", "tutor_response", "grounded_in", "evidence"):
            assert f in fields, f"car mode cannot record {f}"

    def test_secondary_facts_can_carry_evidence(self):
        req = CarNextRequest(answered={
            "topic": "T", "point": "P", "correct": True,
            "also_covered": [{"point": "Q", "correct": True, "evidence": "his words"}]})
        assert req.answered.also_covered[0].evidence == "his words"

    def test_the_fields_are_optional(self):
        """A terse hands-free call must still work — this must not become a
        validation error while the user is driving."""
        req = CarNextRequest(answered={"topic": "T", "point": "P", "correct": True})
        assert req.answered.user_answer_verbatim == ""


class TestCaptureReachesTheDatabase:
    def test_a_car_answer_stores_the_verbatim_and_the_teaching(self):
        from src.mcp_server import car_next
        from src.student_model import conn

        point = "CarCaptureProbe: a distinctive fictional probe threshold"
        car_next(answered={
            "topic": "CarCaptureTopic", "point": point, "correct": "partial",
            "confidence": 3, "user_answer": "graded summary",
            "user_answer_verbatim": "I said about four grams a day I think",
            "tutor_response": "Right on the daily max; the per-dose figure is what you missed.",
            "grounded_in": "MGH Housestaff Manual - Analgesia p.12",
            "evidence": "about four grams a day"})
        with conn() as db:
            att = db.execute(
                "SELECT user_answer_verbatim, tutor_response, grounded_in "
                "FROM question_attempts WHERE topic=? ORDER BY attempt_id DESC LIMIT 1",
                ("CarCaptureTopic",)).fetchone()
            kp = db.execute(
                "SELECT evidence FROM knowledge_points WHERE point=?", (point,)).fetchone()
        assert "four grams" in att["user_answer_verbatim"]
        assert "per-dose" in att["tutor_response"]
        assert att["grounded_in"].startswith("MGH")
        assert kp is not None and "four grams" in kp["evidence"], (
            "submit_knowledge_points dropped the evidence again")

    def test_missing_capture_is_warned_back_to_the_tutor(self):
        """The old behaviour returned nothing, so under-recording was invisible."""
        from src.mcp_server import car_next

        out = car_next(answered={
            "topic": "CarCaptureTopic2",
            "point": "CarCaptureProbe2: another distinctive probe threshold",
            "correct": True, "confidence": 4})
        warnings = out["recorded"].get("warnings") or []
        assert any("verbatim" in w for w in warnings), out["recorded"]

    def test_pacing_rides_along_on_every_car_turn(self):
        """A driver cannot check a clock. Car mode never touched one at all."""
        from src.mcp_server import car_next
        from src.session_clock import start_clock

        start_clock(30)
        out = car_next()
        assert "pacing" in out
        assert out["pacing"]["clock_running"] is True
        assert out["pacing"]["remaining_minutes"] > 0

    def test_echo_detection_now_works_in_car_mode(self):
        """It compares the answer against the previous tutor turn; with both
        fields absent it could never fire on a spoken session."""
        from src.mcp_server import car_next

        topic = "CarEchoTopic"
        point = "CarEchoProbe: a distinctive fictional mechanism fact"
        car_next(answered={
            "topic": topic, "point": point, "correct": False, "confidence": 2,
            "user_answer_verbatim": "I don't know that one",
            "tutor_response": "It works because the probe-state gradient collapses at the membrane."})
        out = car_next(answered={
            "topic": topic, "point": point, "correct": True, "confidence": 3,
            "user_answer_verbatim": "You just told me, because the probe-state gradient collapses at the membrane.",
            "tutor_response": "Right."})
        assert out["recorded"].get("graded_as_exposure") is True
