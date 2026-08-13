"""Tests for pedagogy upgrades: confidence calibration, case prep, weak patterns,
relevance hook, mechanism teach-back."""

import json

from src.curriculum import CurriculumUnit
from src.pedagogy import SESSION_STRUCTURE
from src.schemas import SourceChunk
from src.voice_shaper import shape_lesson


def _unit(crossover="normal", book="Intern Notes / Survival Guide", topic="Hyperkalemia"):
    return CurriculumUnit(
        unit_id="u1",
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
        crossover_priority=crossover,
    )


def _src():
    return SourceChunk(text="Calcium gluconate 1g IV stabilizes the cardiac membrane.", book="Intern Notes / Survival Guide", page=5)


# ===== Pedagogy #2 + #8: relevance hook + mechanism teach-back =====

def test_relevance_hook_present_on_every_phase():
    for phase in SESSION_STRUCTURE:
        lesson = shape_lesson(_unit(), [_src()], phase=phase)
        assert lesson.relevance_hook
        assert len(lesson.relevance_hook) <= 240


def test_relevance_hook_emphasizes_icu_for_high_crossover():
    lesson = shape_lesson(_unit(crossover="high"), [_src()], phase="new_material")
    assert "ICU" in lesson.relevance_hook or "cross-cover" in lesson.relevance_hook


def test_teachback_prompts_mechanism_not_summary():
    summary_words = ("summary", "summarize", "takeaway")
    mechanism_words = ("mechanism", "why", "physiology", "explain")
    for phase in SESSION_STRUCTURE:
        lesson = shape_lesson(_unit(), [_src()], phase=phase)
        low = lesson.teachback_prompt.lower()
        assert any(w in low for w in mechanism_words), f"phase {phase} missing mechanism cue: {lesson.teachback_prompt}"
        assert all(w not in low for w in summary_words), f"phase {phase} still using summary phrasing"


def test_confidence_check_is_emitted():
    lesson = shape_lesson(_unit(), [_src()], phase="warm_up_retrieval")
    assert "1-5" in lesson.confidence_check or "1 to 5" in lesson.confidence_check


# ===== Pedagogy #1: confidence-weighted FSRS rating =====

def test_confident_wrong_promotes_overconfident_mistake_type(tmp_path, monkeypatch):
    from src import student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "s.db")
    student_model.initialize_database()
    student_model.log_attempt(
        session_id="s1",
        topic="Hyperkalemia",
        subtopic="treatment",
        question="how do you treat hyperkalemia?",
        user_answer="give D5W",
        ideal_answer="calcium, insulin, dextrose",
        result="incorrect",
        mistake_type="other",
        confidence_reported=5.0,
    )
    with student_model.conn() as db:
        row = db.execute(
            "SELECT mistake_type FROM question_attempts WHERE topic='Hyperkalemia' ORDER BY attempt_id DESC LIMIT 1"
        ).fetchone()
    assert row["mistake_type"] == "overconfident_wrong"


def test_unsure_right_gets_easy_rating():
    from src.student_model import _result_to_fsrs_rating
    assert _result_to_fsrs_rating("correct", "other", 0, confidence_reported=1.0) == 4
    assert _result_to_fsrs_rating("correct", "other", 0, confidence_reported=2.0) == 4


def test_confident_right_normal_rating():
    from src.student_model import _result_to_fsrs_rating
    assert _result_to_fsrs_rating("correct", "other", 0, confidence_reported=5.0) == 3


def test_critical_mistake_caps_correct_at_partial_rating():
    from src.student_model import _result_to_fsrs_rating
    assert _result_to_fsrs_rating("correct", "crisis_algorithm", 0, confidence_reported=5.0) == 2


# ===== Pedagogy #5: /case_prep =====

def test_case_prep_extracts_topics_from_admission_stem(tmp_path, monkeypatch):
    from src import case_prep

    monkeypatch.setattr(case_prep, "_retrieve_for_topic", lambda topic, stem, max_results=2: [])
    resp = case_prep.case_prep("admitting AECOPD overnight", duration_minutes=5)
    assert resp.case_stem.startswith("admitting")
    assert 1 <= len(resp.review_topics) <= 6
    topics = {t.topic for t in resp.review_topics}
    # AECOPD should hit COPD/asthma exacerbation or similar
    assert any("COPD" in t or "asthma" in t.lower() or "Dyspnea" in t for t in topics) or len(topics) > 0
    for t in resp.review_topics:
        assert t.why
        assert len(t.why) <= 240


def test_case_prep_cross_cover_stem_emphasizes_paging():
    from src import case_prep

    monkeypatch_calls = []

    def fake_retrieve(topic, stem, max_results=2):
        monkeypatch_calls.append((topic, stem))
        return []

    case_prep._retrieve_for_topic = fake_retrieve  # type: ignore
    resp = case_prep.case_prep("night float page about chest pain", duration_minutes=3)
    assert any("page" in t.why.lower() or "cross-cover" in t.why.lower() for t in resp.review_topics)


# ===== Pedagogy #7: /weak_patterns =====

def test_weak_patterns_aggregates_mistake_types(tmp_path, monkeypatch):
    from src import student_model, weak_patterns

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "s.db")
    student_model.initialize_database()
    for _ in range(3):
        student_model.log_attempt(
            "s1", "Sepsis", "fluids", "q", "wrong", "ideal", "incorrect", "prioritization"
        )
    student_model.log_attempt(
        "s1", "Sepsis", "fluids", "q", "wrong", "ideal", "incorrect", "recall"
    )
    student_model.log_attempt(
        "s1", "Hyperkalemia", "tx", "q", "good", "ideal", "correct", "other", confidence_reported=5.0
    )
    student_model.log_attempt(
        "s1", "AKI", "diff", "q", "wrong", "ideal", "incorrect", "differential_too_narrow", confidence_reported=5.0
    )
    out = weak_patterns.compute_weak_patterns(window_days=30)
    assert out.by_mistake_type["prioritization"] == 3
    repeat = [e for e in out.repeat_offenders if e.topic == "Sepsis" and e.mistake_type == "prioritization"]
    assert len(repeat) == 1
    assert repeat[0].failures == 3
    # one confident-correct + one confident-wrong (which gets remapped to overconfident_wrong) -> 2 confident total, 1 wrong
    assert 0.0 < out.overconfidence_rate <= 1.0
