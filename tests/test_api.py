from fastapi.testclient import TestClient

from src.api import app
from src.config import settings


API_KEY = settings.api_key


def test_health():
    client = TestClient(app)
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["ok"] is True


def test_api_key_required_for_protected_endpoints():
    client = TestClient(app)
    r = client.post("/search", json={"query": "hyperkalemia"})
    assert r.status_code == 401


def test_next_lesson_returns_voice_shaped_lesson(tmp_path, monkeypatch):
    from src import api, curriculum, session_runner, student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "student.db")
    monkeypatch.setattr(api.settings, "sqlite_db_path", tmp_path / "student.db")

    sample_unit = curriculum.CurriculumUnit(
        unit_id="intern-1-hyperk-5",
        book="Intern Notes / Survival Guide",
        library="intern_year_medicine",
        chapter_number=1,
        chapter_title="Electrolytes",
        section="Hyperkalemia",
        page_start=5,
        page_end=5,
        topic_tags=["Hyperkalemia"],
        fact_chunk_ids=["f1"],
        fact_count=1,
        high_yield_score=0.4,
        crossover_priority="normal",
    )
    monkeypatch.setattr(session_runner, "load_curriculum", lambda: [sample_unit])
    monkeypatch.setattr(session_runner, "_due_topic_subjects", lambda limit=25: [])
    from src.schemas import SourceChunk

    monkeypatch.setattr(
        session_runner,
        "_retrieve_for_unit",
        lambda u, q, max_results=3: [SourceChunk(text="Hyperkalemia: ECG, calcium, insulin.", book="Intern Notes / Survival Guide", page=5)],
    )

    client = TestClient(app)
    r = client.post("/next_lesson", json={"session": {}}, headers={"X-API-Key": API_KEY})
    assert r.status_code == 200
    body = r.json()
    assert body["lesson"]["unit_id"] == "intern-1-hyperk-5"
    assert body["lesson"]["topic"] == "Hyperkalemia"
    assert body["lesson"]["question"]
    assert len(body["lesson"]["question"]) <= 240
    # First turn for a fresh unit serves a pretest (forward-testing effect)
    # and intentionally stays at phase_index=0 so the next turn delivers
    # warm_up_retrieval. After the pretest, phase advances normally.
    assert body["session"]["phase_index"] in (0, 1)
    assert body["lesson"]["phase"] in ("pretest", "warm_up_retrieval")


def test_progress_returns_band_breakdown(tmp_path, monkeypatch):
    from src import api, student_model
    from src.curriculum import CurriculumUnit

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "student.db")
    monkeypatch.setattr(api.settings, "sqlite_db_path", tmp_path / "student.db")
    sample = [
        CurriculumUnit(
            unit_id=f"u{i}", book="Intern Notes / Survival Guide", library="intern_year_medicine",
            chapter_number=1, chapter_title="C", section=f"S{i}", page_start=i, page_end=i,
            topic_tags=[], fact_chunk_ids=[], fact_count=0, high_yield_score=0.0, crossover_priority="normal",
        )
        for i in range(3)
    ]
    monkeypatch.setattr(api, "load_curriculum", lambda: sample)
    client = TestClient(app)
    r = client.get("/progress", headers={"X-API-Key": API_KEY})
    assert r.status_code == 200
    body = r.json()
    assert body["n_units"] == 3
    assert body["n_completed"] == 0
    assert "spine" in body["by_band"]


def test_tutor_returns_answer():
    client = TestClient(app)
    r = client.post(
        "/tutor",
        json={"query": "Teach me shunt physiology", "mode": "teach"},
        headers={"X-API-Key": API_KEY},
    )
    assert r.status_code == 200
    body = r.json()
    assert "answer" in body
    assert "sources" in body


def test_tutor_learning_plan_prompt_starts_session():
    client = TestClient(app)
    r = client.post(
        "/tutor",
        json={
            "query": "i am just starting out my anesthisology resiendcy, lets build out a learning plan. teach me the first topic",
            "mode": "teach",
        },
        headers={"X-API-Key": API_KEY},
    )
    assert r.status_code == 200
    body = r.json()
    assert body["mode"] == "session_start"
    assert body["session_id"]
    assert "Stanford CA-1 is the spine" in body["answer"]
    assert "First topic:" in body["answer"]


def test_start_session_defaults_to_intern_year(tmp_path, monkeypatch):
    from src import api, student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "student.db")
    monkeypatch.setattr(api.settings, "sqlite_db_path", tmp_path / "student.db")
    monkeypatch.setattr(
        student_model,
        "get_intern_fact_catalog",
        lambda: [
            {
                "target_id": "intern-sepsis",
                "topic": "Sepsis",
                "subtopic": "Intern Notes / Survival Guide p. 8: cultures before antibiotics if feasible",
                "fact": "cultures before antibiotics if feasible",
                "page": 8,
                "source": "Intern Notes / Survival Guide",
                "library": "intern_year_medicine",
                "training_phase": "intern_year",
            }
        ],
    )
    client = TestClient(app)
    r = client.post("/start_session", json={"duration_minutes": 30, "mode": "default"}, headers={"X-API-Key": API_KEY})
    assert r.status_code == 200
    body = r.json()
    assert body["training_phase"] == "intern_year"
    assert "retrieval_confidence" in body
    assert "insufficient_context" in body


def test_submit_answer_accepts_gpt_structured_evaluation(tmp_path, monkeypatch):
    from src import api, student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "student.db")
    monkeypatch.setattr(api.settings, "sqlite_db_path", tmp_path / "student.db")
    client = TestClient(app)
    r = client.post(
        "/answer",
        json={
            "session_id": "voice-session",
            "question": "How do you treat LAST?",
            "user_answer": "Give lipid emulsion and support ABCs.",
            "topic": "LAST",
            "subtopic": "treatment",
            "result": "correct",
            "mistake_type": "other",
            "ideal_answer": "Stop local anesthetic, support ABCs, treat seizures, and give intralipid.",
            "retrieval_sources": "Stanford CA-1 p. 82",
        },
        headers={"X-API-Key": API_KEY},
    )
    assert r.status_code == 200
    assert r.json()["evaluation"] == "correct"
    summary = student_model.get_topic_summary("LAST")
    assert summary["times_correct"] == 1


def test_ca1_coverage_endpoint(tmp_path, monkeypatch):
    from src import api, student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "student.db")
    monkeypatch.setattr(api.settings, "sqlite_db_path", tmp_path / "student.db")
    monkeypatch.setattr(
        student_model,
        "get_ca1_fact_catalog",
        lambda: [{"target_id": "ca1-last", "topic": "LAST", "subtopic": "CA-1 p. 82: lipid rescue", "fact": "lipid rescue", "page": 82, "source": "Stanford CA-1"}],
    )
    client = TestClient(app)
    r = client.get("/ca1_coverage", headers={"X-API-Key": API_KEY})
    assert r.status_code == 200
    assert r.json()["source"] == "Stanford CA-1"
    assert r.json()["granularity"] == "fact"


def test_source_coverage_endpoint(tmp_path, monkeypatch):
    from src import api, student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "student.db")
    monkeypatch.setattr(api.settings, "sqlite_db_path", tmp_path / "student.db")
    monkeypatch.setattr(
        student_model,
        "get_fact_catalog",
        lambda source, max_facts_per_chunk=8: [{"target_id": source, "topic": "Airway", "subtopic": f"{source} fact", "fact": "fact", "page": 1, "source": source}],
    )
    client = TestClient(app)
    r = client.get("/source_coverage", headers={"X-API-Key": API_KEY})
    assert r.status_code == 200
    assert len(r.json()["source_summaries"]) >= 3


def test_search_basics_query_prioritizes_ca1_sources():
    client = TestClient(app)
    r = client.post(
        "/search",
        json={"query": "LAST treatment BASICS exam", "max_results": 3},
        headers={"X-API-Key": API_KEY},
    )
    assert r.status_code == 200
    assert r.json()["results"][0]["book"] == "Stanford CA-1"
