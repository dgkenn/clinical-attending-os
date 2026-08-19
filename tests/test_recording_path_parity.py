"""Every path that records an answer must capture the same evidence.

Two paths have already drifted into verdict-only recording, and neither failed
loudly. `submit_answer` gained verbatim capture, grounding and echo detection;
`car_next` did not, and a real hands-free session logged 5 answers with none of
it. The bug was invisible until the transcript was diffed against the database
by hand.

The generalisable lesson is that capture parity is a property of the SYSTEM, not
of whichever path happened to be improved last. This test enumerates the
recorders and asserts they all accept the same fields, so a third divergence
fails here instead of surfacing weeks later as an unauditable session.

`submit_study_answer` / `record_evaluated_answer` had never been called (0 uses
in the tool log) but are live over MCP and HTTP and are what the ChatGPT Actions
schema drives, so re-importing that schema would have reintroduced the same gap.
"""
from __future__ import annotations

import inspect

import pytest

CAPTURE = ("user_answer_verbatim", "tutor_response", "grounded_in")


def _params(fn):
    return set(inspect.signature(fn).parameters)


class TestAttemptRecordersAcceptCapture:
    @pytest.mark.parametrize("dotted", [
        "src.mcp_endpoints:submit_answer",
        "src.mcp_server:submit_study_answer",
        "src.tutor_engine:record_evaluated_answer",
        "src.student_model:log_attempt",
    ])
    def test_recorder_accepts_the_capture_fields(self, dotted):
        mod_name, fn_name = dotted.split(":")
        mod = __import__(mod_name, fromlist=[fn_name])
        params = _params(getattr(mod, fn_name))
        missing = [f for f in CAPTURE if f not in params]
        assert not missing, f"{dotted} cannot record {missing}"


class TestFactRecordersAcceptEvidence:
    @pytest.mark.parametrize("dotted", [
        "src.student_model:record_knowledge_point",
    ])
    def test_fact_recorder_accepts_evidence(self, dotted):
        mod_name, fn_name = dotted.split(":")
        mod = __import__(mod_name, fromlist=[fn_name])
        assert "evidence" in _params(getattr(mod, fn_name))

    def test_submit_knowledge_points_forwards_evidence(self):
        """It accepted the key and dropped it before writing, so every fact
        recorded through the only fact path car mode uses stored empty
        evidence however carefully the tutor had quoted the answer."""
        import src.mcp_server as m
        src = inspect.getsource(m.submit_knowledge_points)
        assert "evidence" in src, "submit_knowledge_points drops evidence again"


class TestCarModeHasParityWithChat:
    def test_the_car_schema_carries_what_submit_answer_carries(self):
        from src.schemas import CarAnsweredInput
        fields = set(CarAnsweredInput.model_fields)
        missing = [f for f in CAPTURE + ("evidence",) if f not in fields]
        assert not missing, f"car mode cannot record {missing}"

    def test_both_paths_accept_three_way_grading(self):
        """Car mode rejected "partial" while everything else accepted it,
        costing three failed calls in one session before the tutor guessed a
        shape that passed."""
        from src.schemas import CarNextRequest
        from src.mcp_endpoints import submit_answer

        assert "result" in _params(submit_answer)
        req = CarNextRequest(answered={"topic": "T", "point": "P", "correct": "partial"})
        assert req.answered.correct == "partial"
