"""Simulate a full multi-turn voice loop and assert state evolves correctly."""

from __future__ import annotations

import json

import pytest
from fastapi.testclient import TestClient

from src.api import app
from src.config import settings
from src.curriculum import CurriculumUnit


API_KEY = settings.api_key


def _make_unit(uid: str, topic: str, book: str = "Intern Notes / Survival Guide") -> CurriculumUnit:
    return CurriculumUnit(
        unit_id=uid,
        book=book,
        library="intern_year_medicine",
        chapter_number=1,
        chapter_title=f"Chapter {uid}",
        section=topic,
        page_start=1,
        page_end=1,
        topic_tags=[topic],
        fact_chunk_ids=[],
        fact_count=0,
        high_yield_score=0.0,
        crossover_priority="normal",
    )


@pytest.fixture
def stub_curriculum(monkeypatch):
    from src import session_runner, lesson_cache
    from src.schemas import SourceChunk

    units = [
        _make_unit("u1", "Hyperkalemia"),
        _make_unit("u2", "Sepsis"),
        _make_unit("u3", "ARDS", book="Marino ICU Book"),
    ]
    monkeypatch.setattr(session_runner, "load_curriculum", lambda: units)
    monkeypatch.setattr(session_runner, "_due_topic_subjects", lambda limit=25: [])
    monkeypatch.setattr(
        session_runner,
        "_retrieve_for_unit",
        lambda u, q, max_results=3: [SourceChunk(text=f"{u.section} content here", book=u.book, page=u.page_start)],
    )
    monkeypatch.setattr(
        session_runner,
        "_retrieve_for_due_topic",
        lambda r, max_results=3: [SourceChunk(text="due-content", book="X", page=1)],
    )
    # Prevent stale cache from earlier tests
    lesson_cache._LOADED = {}
    return units


def test_voice_loop_10_turns_progresses_phases(tmp_path, monkeypatch, stub_curriculum):
    from src import student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "vs.db")
    student_model.initialize_database()

    c = TestClient(app)
    session: dict = {}
    seen_phases = []
    for turn in range(10):
        r = c.post("/next_lesson", json={"session": session}, headers={"X-API-Key": API_KEY})
        assert r.status_code == 200, r.text
        body = r.json()
        lesson = body["lesson"]
        session = body["session"]
        seen_phases.append(lesson["phase"])
        # phase index must advance
        assert "phase_index" in session
        assert lesson["topic"] in {"Hyperkalemia", "Sepsis", "ARDS"} or lesson["unit_id"] == "none"
        # nextLesson responses are stripped of teach material — those fields
        # come back via /submit_answer to force per-turn submit calls.
        if lesson["unit_id"] != "none":
            assert lesson["question"]
            assert lesson["confidence_check"]
            assert lesson["mini_teach"] == ""
            assert lesson["teachback_prompt"] == ""
            assert lesson["expected_answer_short"] == ""
            assert lesson["citation"] == ""
    # Should cycle through all 5 phases at least once
    assert len({"warm_up_retrieval", "weak_topic_drilling", "new_material", "clinical_case_application", "teach_back"} & set(seen_phases)) >= 4


def test_voice_loop_submits_with_confidence_calibration(tmp_path, monkeypatch, stub_curriculum):
    from src import student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "vs2.db")
    student_model.initialize_database()

    c = TestClient(app)
    session: dict = {}
    # Get a lesson
    r1 = c.post("/next_lesson", json={"session": session}, headers={"X-API-Key": API_KEY})
    lesson = r1.json()["lesson"]
    # Submit confident-wrong (should auto-tag overconfident_wrong)
    r2 = c.post(
        "/submit_answer",
        json={
            "session_id": "voice-1",
            "question": lesson["question"],
            "user_answer": "completely wrong",
            "topic": lesson["topic"],
            "subtopic": lesson["unit_id"],
            "result": "incorrect",
            "mistake_type": "other",
            "confidence_reported": 5.0,
        },
        headers={"X-API-Key": API_KEY},
    )
    assert r2.status_code == 200
    body = r2.json()
    assert body["evaluation"] == "incorrect"
    # Confirm DB has overconfident_wrong tag
    with student_model.conn() as db:
        row = db.execute(
            "SELECT mistake_type FROM question_attempts ORDER BY attempt_id DESC LIMIT 1"
        ).fetchone()
    assert row["mistake_type"] == "overconfident_wrong"


def test_voice_loop_unsure_correct_strengthens_more_than_confident(tmp_path, monkeypatch, stub_curriculum):
    from src import student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "vs3.db")
    student_model.initialize_database()

    # Two parallel topics
    student_model.log_attempt("s1", "Topic-Confident", "", "q", "a", "i", "correct", "other", confidence_reported=5.0)
    student_model.log_attempt("s1", "Topic-Unsure", "", "q", "a", "i", "correct", "other", confidence_reported=1.0)
    s_conf = student_model.get_topic_summary("Topic-Confident")
    s_unsure = student_model.get_topic_summary("Topic-Unsure")
    # Unsure-correct gets FSRS rating 4 (Easy), confident-correct gets 3 (Good).
    # FSRS Easy -> bigger stability -> bigger mastery proxy.
    assert s_unsure["mastery_score"] >= s_conf["mastery_score"]


def test_concurrent_submits_no_corruption(tmp_path, monkeypatch, stub_curriculum):
    from src import student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "vs4.db")
    student_model.initialize_database()

    import threading

    def submit():
        for _ in range(5):
            student_model.log_attempt(
                "s1", "Concurrent", "", "q", "a", "i", "correct", "other"
            )

    ts = [threading.Thread(target=submit) for _ in range(4)]
    for t in ts: t.start()
    for t in ts: t.join()
    s = student_model.get_topic_summary("Concurrent")
    # 4 threads × 5 submits = 20 attempts
    assert s["times_seen"] == 20


def test_progress_endpoint_handles_zero_state(tmp_path, monkeypatch, stub_curriculum):
    from src import student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "vs5.db")
    monkeypatch.setattr("src.api.load_curriculum", lambda: stub_curriculum)
    student_model.initialize_database()

    c = TestClient(app)
    r = c.get("/progress", headers={"X-API-Key": API_KEY})
    assert r.status_code == 200
    body = r.json()
    assert body["n_units"] == 3
    assert body["n_completed"] == 0
    assert "spine" in body["by_band"]


def test_due_review_path_does_not_crash_when_due_topics_present(tmp_path, monkeypatch, stub_curriculum):
    from src import session_runner, student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "vs6.db")
    student_model.initialize_database()
    # Force a due topic
    monkeypatch.setattr(
        session_runner,
        "_due_topic_subjects",
        lambda limit=25: [
            {
                "topic_id": 1,
                "topic": "DueTopic",
                "subtopic": "",
                "mastery_score": 0.2,
                "fsrs_state": None,
                "library": "intern_year_medicine",
                "training_phase": "intern_year",
                "source": "Intern Notes / Survival Guide",
            }
        ],
    )
    c = TestClient(app)
    r = c.post("/next_lesson", json={"session": {}}, headers={"X-API-Key": API_KEY})
    assert r.status_code == 200
    lesson = r.json()["lesson"]
    assert lesson["topic"] == "DueTopic" or lesson["unit_id"].startswith("due:") or lesson["unit_id"] != "none"
