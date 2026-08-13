from src.curriculum import CurriculumUnit
from src.pedagogy import SESSION_STRUCTURE
from src.schemas import SourceChunk
from src.voice_shaper import shape_lesson


def _unit() -> CurriculumUnit:
    return CurriculumUnit(
        unit_id="intern-1-hyperk-5",
        book="Intern Notes / Survival Guide",
        library="intern_year_medicine",
        chapter_number=1,
        chapter_title="Electrolytes",
        section="Hyperkalemia",
        page_start=5,
        page_end=5,
        topic_tags=["Hyperkalemia"],
        fact_chunk_ids=["f1", "f2"],
        fact_count=2,
        high_yield_score=0.4,
        crossover_priority="normal",
    )


def _source() -> SourceChunk:
    return SourceChunk(
        text="Hyperkalemia: confirm with ECG, give calcium gluconate 1g IV, then insulin 10u with D50.",
        book="Intern Notes / Survival Guide",
        page=5,
        section="Hyperkalemia",
    )


def test_voice_lesson_fields_short():
    lesson = shape_lesson(_unit(), [_source()], phase="warm_up_retrieval")
    for field in (lesson.question, lesson.expected_answer_short, lesson.mini_teach, lesson.teachback_prompt, lesson.citation):
        assert len(field) <= 240
        # at most 2 sentences
        assert field.count(".") + field.count("!") + field.count("?") <= 3


def test_voice_lesson_per_phase_question_differs():
    questions = set()
    for phase in SESSION_STRUCTURE:
        lesson = shape_lesson(_unit(), [_source()], phase=phase)
        questions.add(lesson.question)
    assert len(questions) == len(SESSION_STRUCTURE)


def test_voice_lesson_falls_back_when_no_source():
    lesson = shape_lesson(_unit(), [], phase="new_material")
    assert lesson.unit_id == "intern-1-hyperk-5"
    assert lesson.book == "Intern Notes / Survival Guide"
    assert lesson.page == 5
    assert lesson.expected_answer_short == ""


def test_voice_lesson_topic_label_falls_back_to_section():
    u = _unit()
    u.topic_tags = []
    lesson = shape_lesson(u, [_source()], phase="warm_up_retrieval")
    assert lesson.topic == "Hyperkalemia"
