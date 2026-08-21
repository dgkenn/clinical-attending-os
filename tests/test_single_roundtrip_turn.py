"""One tool call per turn, because every call cuts the audio.

The maintainer studies by voice. A tool call stops the model's generation and
restarts it, and the speech stops with it — he hears the explanation break off
mid-sentence, which he reports as the most annoying thing about using the
system. The instructions have told the tutor to batch calls at the top of a turn
for weeks and it still interleaves them, because obeying that rule requires
planning two calls ahead.

So the second call was removed instead of re-explained. submit_answer records
the last answer AND returns the next topic with its passages, making
"call once, then speak" the path of least resistance rather than a discipline.

The backend was never the problem: a warm submit_answer measures ~114 ms, and
~880 ms with retrieval folded in — which is what the separate get_next_topic
cost anyway. Same total work, half the stalls, and the remaining one lands
before the tutor starts talking.
"""
from __future__ import annotations

import pytest


def test_submit_answer_returns_the_next_topic_with_sources():
    from src.mcp_endpoints import submit_answer

    out = submit_answer(
        topic="RoundTripProbeTopic", question="probe question",
        user_answer="a probe answer", is_correct=True,
        user_answer_verbatim="a probe answer",
        tutor_response="Right, and here is the mechanism.",
        grounded_in="Marino ICU Book, p.42")
    assert "next" in out, "the turn still needs a second call for the next topic"
    nxt = out["next"]
    assert isinstance(nxt, dict) and nxt.get("topic"), f"no next topic: {nxt}"
    # Sources ride along so the tutor never needs a separate retrieval call.
    assert "sources" in nxt


def test_pacing_rides_along_too():
    """The clock must not cost its own round trip either."""
    from src.mcp_endpoints import submit_answer
    from src.session_clock import start_clock

    start_clock(30)
    out = submit_answer(
        topic="RoundTripProbeTopic2", question="probe question two",
        user_answer="another probe answer", is_correct=True,
        user_answer_verbatim="another probe answer",
        tutor_response="Correct.")
    assert out["pacing"]["clock_running"] is True
    assert out["next"] is not None


def test_prefetch_can_be_disabled_for_scripts():
    """Backfills and migrations should not pay for retrieval they never read."""
    from src.mcp_endpoints import submit_answer

    out = submit_answer(
        topic="RoundTripProbeTopic3", question="probe question three",
        user_answer="a third probe answer", is_correct=True,
        user_answer_verbatim="a third probe answer",
        tutor_response="Correct.", with_next=False)
    assert out["next"] is None


def test_a_prefetch_failure_never_breaks_the_recording():
    """The answer is the thing that must survive; the prefetch is a bonus."""
    import src.mcp_server as ms
    from src.mcp_endpoints import submit_answer

    original = ms.get_next_topic_checked
    ms.get_next_topic_checked = lambda *a, **k: (_ for _ in ()).throw(RuntimeError("boom"))
    try:
        out = submit_answer(
            topic="RoundTripProbeTopic4", question="probe question four",
            user_answer="a fourth probe answer", is_correct=True,
            user_answer_verbatim="a fourth probe answer", tutor_response="Correct.")
    finally:
        ms.get_next_topic_checked = original
    assert out["ok"] is True, "a prefetch failure must not lose the answer"
    assert "error" in (out["next"] or {})
