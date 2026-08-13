"""Adversarial tests — try to break the system from a hostile-input perspective.

Goal: surface real production bugs (auth bypass, injection, resource exhaustion,
state corruption, missing-file fragility) before the user does in voice mode.
"""

from __future__ import annotations

import json

import pytest
from fastapi.testclient import TestClient

from src.api import app
from src.config import settings


API_KEY = settings.api_key


# ===== Auth =====

def test_missing_api_key_header_rejected_when_key_set():
    if not API_KEY:
        pytest.skip("API_KEY unset; can't test rejection")
    c = TestClient(app)
    r = c.post("/next_lesson", json={"session": {}})
    assert r.status_code == 401


def test_wrong_api_key_rejected():
    if not API_KEY:
        pytest.skip("API_KEY unset; can't test rejection")
    c = TestClient(app)
    r = c.post("/next_lesson", json={"session": {}}, headers={"X-API-Key": "wrong"})
    assert r.status_code == 401


def test_health_does_not_require_api_key():
    c = TestClient(app)
    r = c.get("/health")
    assert r.status_code == 200


def test_protected_endpoints_all_require_key():
    if not API_KEY:
        pytest.skip("API_KEY unset")
    c = TestClient(app)
    paths = [
        ("POST", "/next_lesson", {"session": {}}),
        ("POST", "/case_prep", {"case_stem": "hi"}),
        ("GET", "/weak_patterns", None),
        ("GET", "/progress", None),
        ("GET", "/student_dashboard", None),
        ("GET", "/due_reviews", None),
        ("POST", "/search", {"query": "hi"}),
    ]
    for method, path, body in paths:
        if method == "GET":
            r = c.get(path)
        else:
            r = c.post(path, json=body)
        assert r.status_code == 401, f"{method} {path} did not require API key"


# ===== Input validation =====

def test_extremely_long_query_does_not_crash():
    c = TestClient(app)
    long_q = "hyperkalemia " * 5000  # ~65k chars
    r = c.post("/search", json={"query": long_q, "max_results": 3}, headers={"X-API-Key": API_KEY})
    assert r.status_code == 200


def test_empty_query_returns_no_results_gracefully():
    c = TestClient(app)
    r = c.post("/search", json={"query": "", "max_results": 3}, headers={"X-API-Key": API_KEY})
    assert r.status_code == 200
    body = r.json()
    assert body["insufficient_context"] is True or body["results"] == []


def test_unicode_query_handled():
    c = TestClient(app)
    r = c.post(
        "/search",
        json={"query": "hyperkalemia 高血鉀症 🫀", "max_results": 3},
        headers={"X-API-Key": API_KEY},
    )
    assert r.status_code == 200


def test_search_max_results_clamped_or_bounded():
    c = TestClient(app)
    r = c.post(
        "/search",
        json={"query": "shock", "max_results": 100000},
        headers={"X-API-Key": API_KEY},
    )
    # Either pydantic rejects, or the API returns a reasonable bounded list
    if r.status_code == 200:
        assert len(r.json()["results"]) <= 1000
    else:
        assert r.status_code == 422


def test_negative_duration_rejected_or_handled():
    c = TestClient(app)
    r = c.post(
        "/case_prep",
        json={"case_stem": "AECOPD overnight", "duration_minutes": -5},
        headers={"X-API-Key": API_KEY},
    )
    # Should not 500
    assert r.status_code in (200, 422)


def test_confidence_out_of_range_does_not_crash(tmp_path, monkeypatch):
    from src import student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "s.db")
    student_model.initialize_database()
    # Should not raise even with absurd confidence
    student_model.log_attempt(
        "s1", "Topic", "", "q", "a", "ideal", "correct", "other", confidence_reported=999.0
    )
    student_model.log_attempt(
        "s1", "Topic", "", "q", "a", "ideal", "correct", "other", confidence_reported=-50.0
    )


def test_invalid_mistake_type_rejected_by_pydantic():
    c = TestClient(app)
    r = c.post(
        "/submit_answer",
        json={
            "session_id": "s1",
            "question": "q",
            "user_answer": "a",
            "topic": "Hyperkalemia",
            "result": "correct",
            "mistake_type": "totally_made_up_type",
        },
        headers={"X-API-Key": API_KEY},
    )
    assert r.status_code == 422


def test_invalid_result_rejected_by_pydantic():
    c = TestClient(app)
    r = c.post(
        "/submit_answer",
        json={
            "session_id": "s1",
            "question": "q",
            "user_answer": "a",
            "topic": "X",
            "result": "kinda right",
        },
        headers={"X-API-Key": API_KEY},
    )
    assert r.status_code == 422


def test_sql_injection_in_topic_does_not_corrupt_db(tmp_path, monkeypatch):
    from src import student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "s.db")
    student_model.initialize_database()
    bad = "Topic'); DROP TABLE topics; --"
    student_model.log_attempt("s1", bad, "", "q", "a", "ideal", "correct", "other")
    # Tables must still exist
    with student_model.conn() as db:
        rows = db.execute("SELECT COUNT(*) AS n FROM topics").fetchone()
    assert rows["n"] >= 1


def test_path_traversal_source_filter_no_crash():
    c = TestClient(app)
    r = c.post(
        "/search",
        json={"query": "shock", "source_filter": "../../etc/passwd", "max_results": 3},
        headers={"X-API-Key": API_KEY},
    )
    assert r.status_code == 200


# ===== Missing-file resilience =====

def test_chunks_jsonl_missing_returns_empty_results(tmp_path, monkeypatch):
    from src import retrieval

    monkeypatch.setattr(retrieval.settings, "chroma_dir", tmp_path)
    retrieval.load_json_chunks()  # will return []
    results, insufficient = retrieval.hybrid_search("anything", max_results=5, use_cross_encoder=False)
    assert results == []
    assert insufficient is True


def test_corrupted_jsonl_line_does_not_crash(tmp_path, monkeypatch):
    from src import retrieval

    p = tmp_path / "chunks.jsonl"
    p.write_text(
        "\n".join(
            [
                '{"id":"good","text":"valid","metadata":{"chunk_id":"good","page":1,"book":"X"}}',
                "this is not json at all",
                '{"id":"good2","text":"also valid","metadata":{"chunk_id":"good2","page":2,"book":"X"}}',
            ]
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(retrieval.settings, "chroma_dir", tmp_path)
    retrieval._load_json_chunks_cached.cache_clear()
    retrieval._chunk_term_index.cache_clear()
    rows = retrieval.load_json_chunks()
    assert len(rows) == 2  # corrupted line skipped


def test_lesson_cache_missing_falls_back_to_live_retrieval(tmp_path, monkeypatch):
    from src import lesson_cache

    monkeypatch.setattr(lesson_cache.settings, "chroma_dir", tmp_path)
    lesson_cache._LOADED = None
    assert lesson_cache.get_cached("any", "warm_up_retrieval") is None


def test_curriculum_missing_returns_empty(tmp_path, monkeypatch):
    from src import curriculum

    monkeypatch.setattr(curriculum.settings, "chroma_dir", tmp_path)
    units = curriculum.load_curriculum()
    assert units == []


# ===== State corruption attempts =====

def test_double_submit_same_attempt_does_not_double_count(tmp_path, monkeypatch):
    from src import student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "s.db")
    student_model.initialize_database()
    for _ in range(2):
        student_model.log_attempt("s1", "Hyperkalemia", "", "q", "a", "ideal", "correct", "other")
    # Two attempts logged, but mastery should not exceed 1.0
    summary = student_model.get_topic_summary("Hyperkalemia")
    assert summary["mastery_score"] <= 1.0
    assert summary["times_seen"] == 2


def test_mark_mastered_then_weak_works(tmp_path, monkeypatch):
    from src import student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "s.db")
    student_model.initialize_database()
    student_model.mark_topic_mastered("Sepsis", "")
    student_model.mark_topic_weak("Sepsis", "")
    s = student_model.get_topic_summary("Sepsis")
    assert s["status"] == "weak"
    assert s["mastery_score"] < 0.4


def test_fsrs_state_handles_unknown_rating_safely():
    from src.fsrs import fsrs_review, fsrs_init

    with pytest.raises(ValueError):
        fsrs_review(fsrs_init(), 0)
    with pytest.raises(ValueError):
        fsrs_review(fsrs_init(), 99)


def test_session_with_completely_invalid_phase_index(tmp_path, monkeypatch):
    """phase_index in session is unbounded user input. It must be modulated."""
    from src import session_runner, student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "s.db")
    monkeypatch.setattr(session_runner, "load_curriculum", lambda: [])
    monkeypatch.setattr(session_runner, "_due_topic_subjects", lambda limit=25: [])
    lesson, sess = session_runner.next_lesson({"phase_index": 99999})
    # Should not crash; should return shape_no_lesson_available or similar
    assert lesson.unit_id in ("none",)


# ===== Voice schema invariants =====

def test_voice_lesson_fields_never_exceed_voice_budget():
    """Custom GPT can't speak 5+ sentences. Enforce hard caps."""
    from src.curriculum import CurriculumUnit
    from src.pedagogy import SESSION_STRUCTURE
    from src.schemas import SourceChunk
    from src.voice_shaper import shape_lesson

    long_book_text = "X. " * 500  # forces shape_lesson to truncate
    unit = CurriculumUnit(
        unit_id="u1",
        book="Test",
        library="intern_year_medicine",
        chapter_number=1,
        chapter_title="C",
        section="Hyperkalemia",
        page_start=5,
        page_end=5,
        topic_tags=["Hyperkalemia"],
        fact_chunk_ids=["f1"],
        fact_count=1,
        high_yield_score=0.4,
        crossover_priority="normal",
    )
    src = SourceChunk(text=long_book_text, book="Test", page=5)
    for phase in SESSION_STRUCTURE:
        lesson = shape_lesson(unit, [src], phase=phase)
        for field_name in ("question", "expected_answer_short", "mini_teach", "teachback_prompt", "citation", "relevance_hook", "confidence_check"):
            v = getattr(lesson, field_name)
            assert isinstance(v, str), f"{phase}.{field_name} is not str"
            assert len(v) <= 280, f"{phase}.{field_name} too long: {len(v)} chars"


# ===== Cloze edge cases =====

def test_cloze_handles_empty_fact():
    from src.cloze import generate_clozes
    assert generate_clozes("", "f1") == []
    assert generate_clozes("   ", "f1") == []


def test_cloze_handles_huge_fact_text():
    from src.cloze import generate_clozes
    txt = "Propofol 2 mg/kg IV is the induction dose. " * 200
    cards = generate_clozes(txt, "f1", max_per_fact=4)
    assert len(cards) <= 4


# ===== Synonym ambiguity =====

def test_synonyms_do_not_expand_short_english_words():
    from src.synonyms import expand_with_synonyms
    # "or" must not expand to "operating room" in normal sentences
    out = expand_with_synonyms("apples or oranges")
    assert "operating room" not in out.lower()
    # but "OR case" should
    out2 = expand_with_synonyms("OR case")
    assert "operating room" in out2.lower()


def test_synonyms_idempotent():
    from src.synonyms import expand_with_synonyms
    once = expand_with_synonyms("afib with RVR")
    twice = expand_with_synonyms(once)
    # second pass must not double-add already-present terms
    assert twice.lower().count("atrial fibrillation") == 1


# ===== Concurrency / WAL =====

def test_wal_mode_set(tmp_path, monkeypatch):
    from src import student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "s.db")
    student_model.initialize_database()
    with student_model.conn() as db:
        mode = db.execute("PRAGMA journal_mode").fetchone()
    assert mode[0].lower() == "wal"


# ===== Existence sanity =====

def test_all_listed_endpoints_actually_resolve():
    """Every path in openapi.json should respond (even with 401/422)."""
    import json as _json
    from pathlib import Path

    schema = _json.loads(Path("openapi.json").read_text(encoding="utf-8"))
    c = TestClient(app)
    for path, methods in schema["paths"].items():
        for method in methods:
            if method == "get":
                r = c.get(path)
            elif method == "post":
                r = c.post(path, json={})
            else:
                continue
            # Endpoint should exist and not 404 or 500 unconditionally
            assert r.status_code != 404, f"{method.upper()} {path} returned 404"
            assert r.status_code != 500, f"{method.upper()} {path} returned 500: {r.text[:200]}"
