"""Two failures the digoxin session exposed.

1. GROUNDING. Retrieval was being skipped almost entirely — 0 calls across 22
   answers on 2026-08-17, 1 across 13 on 2026-08-18 — so questions came from
   model training rather than the corpus. They read as clinically sound, which
   is what makes it dangerous: nothing looks wrong and nothing is citable. Two
   rounds of instruction changes failed to fix it, so get_next_topic now ships
   the passages with the topic and grounding needs no second call.

2. TANGENTS. A self-directed digoxin rabbit hole ran a whole session and left
   zero trace — no attempt, no fact. That is the most engaged learning the user
   does and the only kind the system could not see. log_tangent captures it,
   but as EXPOSURE rather than knowledge: recording discussion as a correct
   answer would inflate mastery with things the user was merely told.
"""
from __future__ import annotations

import pytest

from src.config import settings
from src.mcp_server import _attach_sources, log_tangent
from src.student_model import conn

CHUNKS = settings.chroma_dir / "chunks.jsonl"
HAS_CORPUS = CHUNKS.exists() and CHUNKS.stat().st_size > 1000


@pytest.mark.skipif(not HAS_CORPUS, reason="corpus not ingested")
def test_next_topic_carries_its_own_grounding():
    out = _attach_sources({"topic": "Hyperkalemia", "retrieval_query": "hyperkalemia treatment"})
    assert out["sources"], "a served topic must arrive with passages"
    assert "retrieval_confidence" in out
    assert "sources_note" in out
    joined = " ".join(s["text"].lower() for s in out["sources"])
    assert any(t in joined for t in ("calcium", "insulin", "potassium"))


def test_attaching_sources_never_breaks_topic_selection():
    """Retrieval is a bonus on this call; it must not be able to fail it."""
    payload = {"topic": "", "retrieval_query": ""}
    assert _attach_sources(payload) == payload          # nothing to search for
    assert _attach_sources({"topic": "x"}) is not None
    assert _attach_sources("not a dict") == "not a dict"


def test_tangent_is_recorded_as_exposure_not_knowledge():
    """The whole point: the user heard it, they did not demonstrate it."""
    result = log_tangent(
        topic="Digoxin",
        trigger="asked why heart failure patients need a higher K+",
        facts=[
            "Digoxin toxicity is potentiated by hypokalemia because digoxin and "
            "potassium compete for the same Na/K-ATPase site",
            "Digoxin is renally cleared and has a narrow therapeutic index, so AKI "
            "precipitates toxicity",
        ],
    )
    assert result["ok"] is True
    assert result["recorded"] == 2
    with conn() as db:
        rows = db.execute(
            "SELECT times_correct, status FROM knowledge_points WHERE topic = 'Digoxin'"
        ).fetchall()
    assert rows, "the tangent must leave a record"
    assert all(r[0] == 0 for r in rows), "exposure must never be counted correct"
    assert all(r[1] == "weak" for r in rows), "unproven material must be weak"


def test_tangent_facts_are_deduped_not_stacked():
    """A tangent revisited across sessions must converge, not inflate the queue."""
    fact = "Digoxin toxicity classically causes visual disturbance and bidirectional VT"
    log_tangent(topic="Digoxin", facts=[fact])
    with conn() as db:
        before = db.execute(
            "SELECT COUNT(*) FROM knowledge_points WHERE topic='Digoxin'").fetchone()[0]
    log_tangent(topic="Digoxin", facts=[fact])
    with conn() as db:
        after = db.execute(
            "SELECT COUNT(*) FROM knowledge_points WHERE topic='Digoxin'").fetchone()[0]
    assert after == before


def test_fragments_are_rejected():
    """Free-text capture invites junk; a two-word 'fact' is not testable."""
    result = log_tangent(topic="Digoxin", facts=["short", "", "ok"])
    assert result["recorded"] == 0
    assert len(result["skipped"]) == 3
