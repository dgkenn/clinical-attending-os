"""Tests for the iterative follow-up answer endpoint."""

import json

import pytest
from fastapi.testclient import TestClient

from src import follow_up
from src.api import app
from src.config import settings
from src.schemas import SourceChunk


API_KEY = settings.api_key
HAS_CORPUS = (settings.chroma_dir / "chunks.jsonl").exists()


# ===== unit tests on the helpers =====

def test_content_terms_drops_stopwords():
    terms = follow_up._content_terms("is the calcium gluconate dose weight based?")
    assert "calcium" in terms
    assert "gluconate" in terms
    assert "dose" in terms
    assert "weight" in terms
    assert "based" not in terms
    assert "is" not in terms
    assert "the" not in terms


def test_extract_answer_sentences_filters_to_question_terms():
    chunks = [
        SourceChunk(text="Calcium gluconate 1 g IV is given for hyperkalemia. Reproduced with permission.", book="X", page=5),
        SourceChunk(text="Other text without any answers here. Just narrative.", book="X", page=6),
    ]
    out = follow_up._extract_answer_sentences(
        chunks, ["calcium", "gluconate", "1", "dose"], max_sentences=4
    )
    assert any("1 g" in a.text or "1 gram" in a.text for a in out)
    assert all("calcium" in a.text.lower() or "gluconate" in a.text.lower() for a in out)


def test_query_variants_builds_three_distinct_rounds():
    variants = follow_up._build_query_variants(
        question="is the calcium gluconate 1g for every patient or weight-based?",
        lesson_topic="Hyperkalemia",
        mode_hint="intern_teach",
    )
    assert len(variants) >= 2
    queries = [q for q, _ in variants]
    # First query must include both topic and content terms
    assert "hyperkalemia" in queries[0].lower()
    assert "calcium" in queries[0].lower()
    # Modes should diversify across rounds
    modes = [m for _, m in variants]
    assert len(set(modes)) >= 2


def test_empty_question_returns_insufficient():
    out = follow_up.answer_follow_up("", "Hyperkalemia", "intern_teach")
    assert out["insufficient_context"] is True
    assert out["answer_sentences"] == []
    assert out["top_chunks"] == []


# ===== integration tests against real corpus =====

@pytest.mark.skipif(not HAS_CORPUS, reason="corpus not ingested")
def test_calcium_gluconate_dose_question_returns_answer():
    out = follow_up.answer_follow_up(
        question="is the calcium gluconate 1g for every patient or weight-based?",
        lesson_topic="Hyperkalemia",
        mode_hint="intern_teach",
    )
    assert out["confidence"] in ("medium", "high")
    assert out["answer_sentences"], "no answer sentences extracted"
    text = " ".join(s["text"].lower() for s in out["answer_sentences"])
    assert "calcium" in text or "gluconate" in text
    assert "1 g" in text or "1 gm" in text or "1 amp" in text or "10%" in text


@pytest.mark.skipif(not HAS_CORPUS, reason="corpus not ingested")
def test_norepinephrine_first_line_question():
    out = follow_up.answer_follow_up(
        question="why is norepinephrine first line in septic shock?",
        lesson_topic="Sepsis",
        mode_hint="ICU_teach",
    )
    assert out["answer_sentences"], "no answer sentences"
    text = " ".join(s["text"].lower() for s in out["answer_sentences"])
    assert "norepinephrine" in text


@pytest.mark.skipif(not HAS_CORPUS, reason="corpus not ingested")
def test_mh_post_dantrolene_monitoring():
    out = follow_up.answer_follow_up(
        question="after dantrolene what monitoring labs need follow up",
        lesson_topic="Malignant hyperthermia",
        mode_hint="anesthesia_boards",
    )
    # Should at least find the MH treatment pages even if "follow up" is sparse
    assert out["top_chunks"], "no chunks found at all"
    text_blob = " ".join(c.text.lower() for c in out["top_chunks"])
    assert any(t in text_blob for t in ("dantrolene", "hyperkalemia", "rhabdo", "creatinine", "urine"))


@pytest.mark.skipif(not HAS_CORPUS, reason="corpus not ingested")
def test_iterative_search_attempts_multiple_rounds_when_first_misses():
    # A question that's likely to need refinement
    out = follow_up.answer_follow_up(
        question="contraindications to spinal anesthesia in obstetric patient",
        lesson_topic="Neuraxial",
        mode_hint="intern_teach",  # intentionally wrong primary mode
    )
    assert len(out["queries_tried"]) >= 1
    assert len(out["modes_tried"]) >= 1


# ===== endpoint integration =====

def test_follow_up_endpoint_requires_api_key():
    if not API_KEY:
        pytest.skip("API_KEY unset")
    c = TestClient(app)
    r = c.post("/follow_up", json={"question": "test"})
    assert r.status_code == 401


@pytest.mark.skipif(not HAS_CORPUS, reason="corpus not ingested")
def test_follow_up_endpoint_returns_structured_payload():
    c = TestClient(app)
    r = c.post(
        "/follow_up",
        json={
            "question": "is the calcium gluconate 1g for every patient or weight-based?",
            "lesson_topic": "Hyperkalemia",
            "mode_hint": "intern_teach",
        },
        headers={"X-API-Key": API_KEY},
    )
    assert r.status_code == 200, r.text
    body = r.json()
    assert "answer_sentences" in body
    assert "top_chunks" in body
    assert "confidence" in body
    assert body["confidence"] in ("low", "medium", "high")
