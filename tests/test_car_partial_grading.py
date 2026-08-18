"""Car mode rejected the system's own grading vocabulary.

`submit_answer`, `record_knowledge_point` and the whole fact layer grade
True / False / "partial". `CarAnsweredInput.correct` was still a strict bool, so
a tutor grading a hands-free answer as partial got a pydantic validation error —
three failed `car_next` calls in one session before it guessed a shape that
passed. In car mode a failed call is silence while the user is driving, and the
partial verdict is the common case there: a spoken answer that has the substance
and misses a component.

Run under pytest ONLY. Exercising car_next as an ad-hoc script wrote a probe
topic straight into the live database — twice now, in this project's history.
conftest redirects the DB for the test session; nothing else does.
"""
from __future__ import annotations

import pytest

from src.schemas import CarNextRequest


class TestSchemaAcceptsPartial:
    @pytest.mark.parametrize("verdict", [True, False, "partial"])
    def test_every_grading_verdict_validates(self, verdict):
        req = CarNextRequest(answered={"topic": "T", "point": "P", "correct": verdict})
        assert req.answered.correct == verdict

    def test_secondary_facts_can_be_partial_too(self):
        """A bundled spoken answer half-covering a secondary fact is normal."""
        req = CarNextRequest(answered={
            "topic": "T", "point": "P", "correct": False,
            "also_covered": [{"point": "Q", "correct": "partial"}]})
        assert req.answered.also_covered[0].correct == "partial"

    def test_a_nonsense_verdict_is_still_rejected(self):
        """Loosening the type must not make it accept anything."""
        with pytest.raises(Exception):
            CarNextRequest(answered={"topic": "T", "point": "P", "correct": "sort of"})

    def test_correct_is_still_required(self):
        """Never guess correctness — an omitted verdict must fail loudly."""
        with pytest.raises(Exception):
            CarNextRequest(answered={"topic": "T", "point": "P"})


class TestPartialSurvivesToTheLedger:
    def test_a_partial_car_answer_is_recorded_as_partial_not_a_lapse(self):
        from src.mcp_server import car_next
        from src.student_model import conn

        point = "CarPartialProbe: a distinctive fictional probe-state threshold"
        out = car_next(answered={"topic": "CarPartialProbeTopic", "point": point,
                                 "correct": "partial", "confidence": 3})
        assert out["recorded"]["ok"] is True
        with conn() as db:
            row = db.execute(
                "SELECT status, times_seen, times_correct FROM knowledge_points "
                "WHERE point = ?", (point,)).fetchone()
        assert row is not None, "the partial answer must reach the fact ledger"
        # FSRS "Hard": a success with a smaller stability gain, NOT a lapse back
        # to weak — that collapse is what buried the user in false repeats.
        assert row["status"] == "learning"
        # Exactly once. car_next records the fact itself and then calls
        # submit_answer for the TOPIC schedule, passing question=point because
        # in car mode the fact text is the stem. submit_answer's derived-fact
        # fallback then re-derived that same point and advanced its FSRS state a
        # second time, so every hands-free answer counted twice — halving
        # intervals and letting one spoken answer reach two "corrects".
        assert row["times_seen"] == 1, "car mode double-recorded the fact"

    def test_the_topic_schedule_still_advances_in_car_mode(self):
        """Suppressing the duplicate fact write must not cost the topic-level
        record, which is the other half of what car_next is for."""
        from src.mcp_server import car_next
        from src.student_model import conn

        out = car_next(answered={"topic": "CarTopicProbe",
                                 "point": "CarTopicProbe: another distinctive probe fact",
                                 "correct": True, "confidence": 4})
        assert out["recorded"].get("topic_level", {}).get("ok") is True
        with conn() as db:
            n = db.execute("SELECT COUNT(*) FROM question_attempts WHERE topic=?",
                           ("CarTopicProbe",)).fetchone()[0]
        assert n == 1
