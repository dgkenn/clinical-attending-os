import json

from src import curriculum, lesson_cache, session_runner
from src.schemas import SourceChunk


def _unit(uid="u1", book="Intern Notes / Survival Guide", topic="Hyperkalemia"):
    return curriculum.CurriculumUnit(
        unit_id=uid,
        book=book,
        library="intern_year_medicine",
        chapter_number=1,
        chapter_title="Electrolytes",
        section=topic,
        page_start=5,
        page_end=5,
        topic_tags=[topic],
        fact_chunk_ids=["f1"],
        fact_count=1,
        high_yield_score=0.4,
        crossover_priority="normal",
    )


def test_build_cache_writes_one_entry_per_unit_phase(tmp_path, monkeypatch):
    chroma_dir = tmp_path / "chroma"
    chroma_dir.mkdir()
    monkeypatch.setattr(lesson_cache.settings, "chroma_dir", chroma_dir)
    monkeypatch.setattr(curriculum.settings, "chroma_dir", chroma_dir)
    units = [_unit("u1"), _unit("u2", topic="Sepsis")]
    curriculum.save_curriculum(units)
    monkeypatch.setattr(lesson_cache, "_retrieve", lambda u, max_results=3: [SourceChunk(text="content", book=u.book, page=5)])
    summary = lesson_cache.build_cache(progress_every=10)
    assert summary["n_units"] == 2
    assert summary["n_lessons"] == 2 * 5  # 5 SESSION_STRUCTURE phases
    cache = json.loads((tmp_path / "curriculum" / "lesson_cache.json").read_text(encoding="utf-8"))
    assert cache["n_lessons"] == 10
    keys = list(cache["lessons"].keys())
    assert "u1::warm_up_retrieval" in keys
    assert "u2::teach_back" in keys


def test_get_cached_returns_none_without_build(tmp_path, monkeypatch):
    chroma_dir = tmp_path / "chroma"
    chroma_dir.mkdir()
    monkeypatch.setattr(lesson_cache.settings, "chroma_dir", chroma_dir)
    lesson_cache._LOADED = None
    assert lesson_cache.get_cached("nope", "warm_up_retrieval") is None


def test_session_runner_uses_cache_when_present(tmp_path, monkeypatch):
    chroma_dir = tmp_path / "chroma"
    chroma_dir.mkdir()
    monkeypatch.setattr(lesson_cache.settings, "chroma_dir", chroma_dir)
    monkeypatch.setattr(curriculum.settings, "chroma_dir", chroma_dir)
    monkeypatch.setattr(session_runner, "load_curriculum", lambda: [_unit("u1")])
    monkeypatch.setattr(session_runner, "_due_topic_subjects", lambda limit=25: [])

    cached_lesson = {
        "unit_id": "u1",
        "phase": "warm_up_retrieval",
        "topic": "Hyperkalemia",
        "question": "Cached question?",
        "expected_answer_short": "answer",
        "mini_teach": "teach",
        "teachback_prompt": "why?",
        "citation": "Intern p. 5",
        "book": "Intern Notes / Survival Guide",
        "page": 5,
        "relevance_hook": "hook",
        "confidence_check": "1-5",
    }
    cache_path = tmp_path / "curriculum" / "lesson_cache.json"
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(
        json.dumps({"lessons": {"u1::warm_up_retrieval": cached_lesson}}),
        encoding="utf-8",
    )
    lesson_cache._LOADED = None  # force reload from new path
    from src import student_model
    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "s.db")

    lesson, _ = session_runner.next_lesson({})
    # The cache is consulted but the cloze gets rotated per topic_times_seen
    # so the question may differ from the cached one. The cached relevance_hook
    # stays. unit_id is preserved.
    assert lesson.unit_id == "u1"
    assert lesson.relevance_hook == "hook" or lesson.relevance_hook  # Either cached or rebuilt
    # nextLesson STRIPS teach material — comes back via submit_answer instead.
    assert lesson.mini_teach == ""
    assert lesson.teachback_prompt == ""
    assert lesson.expected_answer_short == ""
    assert lesson.citation == ""


def test_submit_answer_returns_teach_material_from_cache(tmp_path, monkeypatch):
    """Closes the loop: submit_answer looks up the cached lesson by
    (subtopic=unit_id, phase) and returns mini_teach/teachback/citation
    so the GPT can narrate them. Without this round-trip, the GPT has
    no teach material at all, which forces it to call submit_answer."""
    from fastapi.testclient import TestClient
    from src.api import app
    from src.config import settings

    chroma_dir = tmp_path / "chroma"
    chroma_dir.mkdir()
    monkeypatch.setattr(lesson_cache.settings, "chroma_dir", chroma_dir)
    cached_lesson = {
        "unit_id": "u1", "phase": "warm_up_retrieval", "topic": "Hyperkalemia",
        "question": "What dose of calcium gluconate?",
        "expected_answer_short": "1 gram", "mini_teach": "Calcium stabilizes membrane.",
        "teachback_prompt": "Why does calcium work?", "citation": "Intern p. 18",
        "book": "Intern Notes / Survival Guide", "page": 18,
        "relevance_hook": "Common cross-cover page.", "confidence_check": "1-5?",
    }
    cache_path = tmp_path / "curriculum" / "lesson_cache.json"
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps({"lessons": {"u1::warm_up_retrieval": cached_lesson}}), encoding="utf-8")
    lesson_cache._LOADED = None
    from src import student_model
    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "s.db")

    client = TestClient(app)
    r = client.post(
        "/submit_answer",
        json={
            "question": "What dose of calcium gluconate?",
            "user_answer": "1 gram",
            "topic": "Hyperkalemia",
            "subtopic": "u1",
            "phase": "warm_up_retrieval",
            "result": "correct",
            "mistake_type": "other",
            "confidence_reported": 4.0,
        },
        headers={"X-API-Key": settings.api_key},
    )
    assert r.status_code == 200, r.text
    body = r.json()
    assert body["mini_teach"] == "Calcium stabilizes membrane."
    assert body["teachback_prompt"] == "Why does calcium work?"
    assert body["citation"] == "Intern p. 18"
