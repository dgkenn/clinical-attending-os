import pytest

from src.tutor_engine import local_answer
from src.schemas import SourceChunk
from src.tutor_engine import grade_user_answer, llm_answer


def test_citations_not_fabricated_without_sources():
    answer = local_answer("What does Miller say?", "teach", [], True)
    assert "Sources: none retrieved." in answer
    assert answer.startswith("The available source material is limited")


def test_backend_generation_disabled_even_if_openai_key_present(monkeypatch):
    from src import tutor_engine

    monkeypatch.setattr(tutor_engine.settings, "enable_openai_generation", False)
    monkeypatch.setattr(tutor_engine.settings, "openai_api_key", "fake-key")
    source = SourceChunk(text="Shunt does not correct fully with oxygen.", book="Miller/Baby Miller", page=85)
    answer = llm_answer("Teach shunt", "teach", [source], False)
    assert "Use only these retrieved excerpts" in answer
    assert "Miller/Baby Miller p. 85" in answer


def test_free_local_mode_hard_guard_blocks_openai_generation(monkeypatch):
    from src import tutor_engine

    monkeypatch.setattr(tutor_engine.settings, "free_local_mode", True)
    monkeypatch.setattr(tutor_engine.settings, "backend_mode", "retrieval_only")
    monkeypatch.setattr(tutor_engine.settings, "api_generation_enabled", True)
    monkeypatch.setattr(tutor_engine.settings, "enable_openai_generation", True)
    monkeypatch.setattr(tutor_engine.settings, "openai_api_key", "fake-key")
    source = SourceChunk(text="Shunt does not correct fully with oxygen.", book="Miller/Baby Miller", page=85)
    with pytest.raises(RuntimeError, match="retrieval-only mode"):
        llm_answer("Teach shunt", "teach", [source], False)


def test_concept_grader_accepts_reasonable_correct_answers():
    result, _ = grade_user_answer(
        "How do you treat LAST?",
        "Stop the local anesthetic, support ABCs, treat seizures with benzodiazepines, and give intralipid.",
        "",
        "LAST",
        "treatment",
    )
    assert result == "correct"


def test_concept_grader_marks_dangerous_wrong_answers_incorrect():
    result, mistake = grade_user_answer(
        "How do you treat LAST?",
        "Give more bupivacaine and wait.",
        "",
        "LAST",
        "treatment",
    )
    assert result == "incorrect"
    assert mistake == "crisis_algorithm"


def test_mh_grader_full_correct_answer():
    result, _ = grade_user_answer(
        "How do you manage malignant hyperthermia?",
        "Stop the volatile agent and succinylcholine, give dantrolene 2.5 mg/kg IV, hyperventilate with 100% oxygen, cool the patient, and treat hyperkalemia and acidosis.",
        "",
        "Malignant hyperthermia",
        "treatment",
    )
    assert result == "correct"


def test_mh_grader_missing_dantrolene_not_correct():
    result, mistake = grade_user_answer(
        "How do you manage malignant hyperthermia?",
        "Stop the volatile agent, hyperventilate with 100% oxygen, cool the patient, and treat hyperkalemia.",
        "",
        "Malignant hyperthermia",
        "treatment",
    )
    assert result != "correct"
    assert mistake == "crisis_algorithm"


def test_mh_grader_missing_trigger_removal_not_correct():
    result, mistake = grade_user_answer(
        "How do you manage malignant hyperthermia?",
        "Give dantrolene, hyperventilate with 100% oxygen, cool the patient, and treat hyperkalemia.",
        "",
        "Malignant hyperthermia",
        "treatment",
    )
    assert result != "correct"
    assert mistake == "crisis_algorithm"


def test_mh_grader_missing_cooling_not_correct():
    result, mistake = grade_user_answer(
        "How do you manage malignant hyperthermia?",
        "Stop the volatile agent, give dantrolene, hyperventilate with 100% oxygen, treat hyperkalemia.",
        "",
        "Malignant hyperthermia",
        "treatment",
    )
    assert result != "correct"
    assert mistake == "crisis_algorithm"
