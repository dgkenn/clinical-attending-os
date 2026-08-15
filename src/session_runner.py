"""Pedagogy-driven session orchestrator.

Wires `pedagogy.SESSION_STRUCTURE` (warm_up_retrieval -> weak_topic_drilling
-> new_material -> clinical_case_application -> teach_back) over the
curriculum and FSRS-tracked topic state.

Public API:
    next_lesson(student_session) -> (VoiceLesson, dict update for session)
    start_voice_session() -> initial session dict
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from functools import lru_cache

from .curriculum import CurriculumUnit, load_curriculum as _load_curriculum_raw
from .fsrs import deserialize as fsrs_deserialize, due_now
from .lesson_cache import get_cached as get_cached_lesson
from .pedagogy import SESSION_STRUCTURE
from .retrieval import hybrid_search
from .schemas import VoiceLesson
from .student_model import conn, get_or_create_topic, initialize_database
from .voice_shaper import shape_lesson, shape_no_lesson_available


@lru_cache(maxsize=1)
def _curriculum_cached(units_path: str, mtime_ns: int) -> list:
    return _load_curriculum_raw()


def load_curriculum() -> list:
    from .config import settings
    path = (settings.chroma_dir).parent / "curriculum" / "units.json"
    if not path.exists():
        return []
    return _curriculum_cached(str(path), path.stat().st_mtime_ns)


def _due_topic_subjects(limit: int = 25) -> list[dict[str, Any]]:
    initialize_database()
    today = datetime.now(timezone.utc).date().isoformat()
    with conn() as db:
        # Same exclusions as student_model.get_due_reviews, for the same reasons:
        # unit:% rows are session bookkeeping (never rescheduled -> permanently
        # due), KP-tracked topics review through the knowledge-point queue (the
        # "stale card that never clears" problem), blank topics retrieve nothing.
        rows = db.execute(
            """SELECT topic_id, topic, subtopic, mastery_score, fsrs_state, library, training_phase, source
               FROM topics
               WHERE (next_review_date IS NULL OR next_review_date <= ?)
                 AND topic NOT IN (SELECT DISTINCT topic FROM knowledge_points)
                 AND topic NOT LIKE 'unit:%'
                 AND topic != ''
               ORDER BY mastery_score ASC LIMIT ?""",
            (today, limit),
        ).fetchall()
    return [dict(r) for r in rows]


def _completed_unit_ids() -> set[str]:
    """Units that have been served (regardless of mastery).

    FSRS handles re-exposure of weak topics via due_topics. The curriculum
    walker only needs to know which units have been *served* so it can move
    forward through the corpus rather than re-emitting unit #1 forever.
    """
    initialize_database()
    with conn() as db:
        rows = db.execute(
            """SELECT topic FROM topics WHERE times_seen >= 1 AND topic LIKE 'unit:%'"""
        ).fetchall()
    return {r["topic"][len("unit:"):] for r in rows}


def _next_unmastered_unit(curriculum: list[CurriculumUnit], completed: set[str]) -> CurriculumUnit | None:
    for u in curriculum:
        if u.unit_id not in completed:
            return u
    return None


def _retrieval_mode(unit: CurriculumUnit) -> str:
    from .curriculum import _band_for_unit

    band = _band_for_unit(unit)
    if band == "icu":
        return "ICU_teach"
    if band == "anesthesia":
        return "anesthesia_boards"
    return "intern_teach"


def _retrieve_for_unit(unit: CurriculumUnit, query: str, max_results: int = 3) -> list:
    sources, _ = hybrid_search(
        query,
        mode=_retrieval_mode(unit),
        source_filter=unit.book,
        topic_filter=unit.topic_tags[0] if unit.topic_tags else None,
        max_results=max_results,
        use_cross_encoder=False,
    )
    return sources


def _retrieve_for_due_topic(topic_row: dict[str, Any], max_results: int = 3) -> list:
    query = f"{topic_row['topic']} {topic_row.get('subtopic', '')}".strip()
    sources, _ = hybrid_search(
        query,
        mode="broad_explain",
        max_results=max_results,
        use_cross_encoder=False,
    )
    return sources


def start_voice_session() -> dict[str, Any]:
    return {
        "phase_index": 0,
        "phases_completed": [],
        "current_unit_id": None,
    }


def _pick_due_topic_for_phase(
    phase: str, due_topics: list[dict[str, Any]]
) -> dict[str, Any] | None:
    if not due_topics:
        return None
    if phase == "warm_up_retrieval":
        return due_topics[0]
    if phase == "weak_topic_drilling":
        weakest = min(due_topics, key=lambda r: r.get("mastery_score") or 1.0)
        return weakest
    return None


def _mark_unit_served(unit: CurriculumUnit, lesson_topic: str) -> None:
    """Record that we served this unit so the curriculum walker advances.

    Creates the `unit:<unit_id>` topic row if missing, then increments
    times_seen + last_seen. The user-facing topic ('Hyperkalemia') is tracked
    separately via submitAnswer for FSRS spaced review.
    """
    initialize_database()
    topic_id = get_or_create_topic(
        topic=f"unit:{unit.unit_id}",
        subtopic=lesson_topic,
        source=unit.book,
        library=unit.library,
        training_phase="",
    )
    now_iso = datetime.now(timezone.utc).isoformat()
    with conn() as db:
        db.execute(
            "UPDATE topics SET times_seen=times_seen+1, last_seen=?, updated_at=? WHERE topic_id=?",
            (now_iso, now_iso, int(topic_id)),
        )


def _topic_record_to_unit_stub(topic_row: dict[str, Any]) -> CurriculumUnit:
    return CurriculumUnit(
        unit_id=f"due:{topic_row['topic']}:{topic_row.get('subtopic') or ''}",
        book=topic_row.get("source") or "",
        library=topic_row.get("library") or "",
        chapter_number=None,
        chapter_title="",
        section=topic_row.get("subtopic") or "",
        page_start=0,
        page_end=0,
        topic_tags=[topic_row["topic"]],
        fact_chunk_ids=[],
        fact_count=0,
        high_yield_score=0.0,
        crossover_priority="normal",
    )


def _find_unit_by_id(curriculum: list, unit_id: str) -> CurriculumUnit | None:
    for u in curriculum:
        if u.unit_id == unit_id:
            return u
    return None


def _strip_teach(lesson: VoiceLesson) -> VoiceLesson:
    """Remove teach material from the lesson before returning to /next_lesson.

    The GPT must call /submit_answer to receive mini_teach, teachback_prompt,
    expected_answer_short, and citation. This forces the call→answer→call→
    answer pattern and prevents the GPT from freelancing whole lessons from
    one /next_lesson response.
    """
    return lesson.model_copy(update={
        "mini_teach": "",
        "teachback_prompt": "",
        "expected_answer_short": "",
        "citation": "",
    })


def next_lesson(session: dict[str, Any]) -> tuple[VoiceLesson, dict[str, Any]]:
    """Return the next VoiceLesson for the session and the updated session dict.

    Deep-dive coherence: all 5 phases of a session pass stay on the SAME unit.
    Walker advance: every 3rd pass the warm_up phase is FORCED to pick a fresh
    unit even if FSRS-due topics exist, so the curriculum keeps progressing.
    Force-advance: if the same unit_id has been served 5+ times across passes,
    the walker abandons it and picks the next.
    Pretesting: a unit's very first encounter inserts a `pretest` phase before
    SESSION_STRUCTURE runs, so the user attempts the question without the
    teach (forward-testing effect).
    Adaptive difficulty: rolling 5-answer correct rate sets `difficulty_target`
    for cloze type selection (Bjork's desirable difficulty zone).
    """
    initialize_database()
    curriculum = load_curriculum()
    completed = _completed_unit_ids()
    due_topics = _due_topic_subjects()

    # Counters carried across calls in the session dict
    pass_counter = int(session.get("pass_counter") or 0)
    since_last_new_unit = int(session.get("since_last_new_unit") or 0)
    unit_serve_counts: dict[str, int] = dict(session.get("unit_serve_counts") or {})
    recent_results: list[str] = list(session.get("recent_results") or [])
    pretests_done: set[str] = set(session.get("pretests_done") or [])

    phase_index = int(session.get("phase_index") or 0) % len(SESSION_STRUCTURE)
    phase = SESSION_STRUCTURE[phase_index]

    unit: CurriculumUnit | None = None
    sources: list = []

    # Reuse current_unit_id mid-pass (phases 1-4 stick to the unit set at phase 0)
    sticky_unit_id = session.get("current_unit_id") if phase_index > 0 else None
    if sticky_unit_id and not sticky_unit_id.startswith("due:"):
        # Force-advance if this unit has been served 5+ times — even mid-pass we
        # bail rather than serve a 6th time.
        if unit_serve_counts.get(sticky_unit_id, 0) >= 5:
            sticky_unit_id = None
        else:
            unit = _find_unit_by_id(curriculum, sticky_unit_id)
            if unit is not None:
                query = unit.topic_tags[0] if unit.topic_tags else (unit.section or unit.chapter_title)
                sources = _retrieve_for_unit(unit, query)

    # Phase 0: choose between FSRS-due review vs fresh curriculum unit.
    # Force a fresh unit every 3rd pass to break the due-review lock.
    force_fresh = since_last_new_unit >= 2
    if unit is None and phase == "warm_up_retrieval" and not force_fresh:
        topic_row = _pick_due_topic_for_phase(phase, due_topics)
        if topic_row:
            unit = _topic_record_to_unit_stub(topic_row)
            sources = _retrieve_for_due_topic(topic_row)

    if unit is None:
        unit = _next_unmastered_unit(curriculum, completed)
        if unit is not None:
            query = unit.topic_tags[0] if unit.topic_tags else (unit.section or unit.chapter_title)
            sources = _retrieve_for_unit(unit, query)

    if unit is None:
        return shape_no_lesson_available(), session

    # Pretest gate: if this is a real curriculum unit AND we've never run a
    # pretest on it, override phase=pretest for this single turn.
    is_real_unit = not unit.unit_id.startswith("due:")
    if is_real_unit and unit.unit_id not in pretests_done and phase_index == 0:
        phase = "pretest"

    # Resolve adaptive difficulty target from rolling window
    difficulty_target = _difficulty_from(recent_results)

    # Look up topic_times_seen for cloze rotation
    topic = unit.topic_tags[0] if unit.topic_tags else (unit.section or unit.chapter_title)
    topic_times_seen = _topic_times_seen(topic) if topic else 0

    # Build the lesson
    cached = None
    if is_real_unit and phase not in ("pretest", "critique"):
        cached = get_cached_lesson(unit.unit_id, phase)
    if cached:
        lesson = VoiceLesson(**cached)
        # Even cached lessons need their cloze rotated for THIS user's repetition.
        # Override the cached question with a freshly rotated cloze if applicable.
        rotated = shape_lesson(
            unit=unit, sources=sources, phase=phase,
            topic_times_seen=topic_times_seen,
            difficulty_target=difficulty_target,
        )
        # Replace just the rotation-sensitive fields; keep the cached relevance hook etc.
        lesson = lesson.model_copy(update={
            "question": rotated.question,
            "expected_answer_short": rotated.expected_answer_short,
            "teachback_prompt": rotated.teachback_prompt,
        })
    else:
        lesson = shape_lesson(
            unit=unit, sources=sources, phase=phase,
            topic_times_seen=topic_times_seen,
            difficulty_target=difficulty_target,
        )

    # Mark unit served and update session counters. Pretests do NOT mark the
    # unit as "served" via _mark_unit_served — otherwise the walker would kick
    # the unit out of the pool before the regular 5-phase pass runs over it.
    if is_real_unit and phase != "pretest":
        _mark_unit_served(unit, lesson.topic)
        unit_serve_counts[unit.unit_id] = unit_serve_counts.get(unit.unit_id, 0) + 1
        since_last_new_unit = 0
    elif is_real_unit and phase == "pretest":
        pretests_done.add(unit.unit_id)
    else:
        since_last_new_unit += 1

    new_session = dict(session)
    # Only advance the phase index if this wasn't a pretest insertion
    if phase == "pretest":
        # Stay at phase_index 0 so the next call serves warm_up_retrieval for the same unit
        new_session["phase_index"] = phase_index
    else:
        new_session["phase_index"] = (phase_index + 1) % len(SESSION_STRUCTURE)
    new_session["current_unit_id"] = unit.unit_id
    completed_phases = list(new_session.get("phases_completed") or [])
    completed_phases.append(phase)
    new_session["phases_completed"] = completed_phases[-25:]
    new_session["pass_counter"] = pass_counter + (1 if phase_index == 4 else 0)
    new_session["since_last_new_unit"] = since_last_new_unit
    new_session["unit_serve_counts"] = unit_serve_counts
    new_session["recent_results"] = recent_results[-5:]
    new_session["pretests_done"] = sorted(pretests_done)
    new_session["difficulty_target"] = difficulty_target
    return _strip_teach(lesson), new_session


def _topic_times_seen(topic: str) -> int:
    """Look up the user-facing topic row's times_seen counter for cloze rotation."""
    initialize_database()
    with conn() as db:
        row = db.execute(
            "SELECT MAX(times_seen) AS n FROM topics WHERE topic = ? AND topic NOT LIKE 'unit:%'",
            (topic,),
        ).fetchone()
    return int(row["n"] or 0) if row else 0


def _difficulty_from(recent: list[str]) -> str:
    """Map rolling 5-answer history → difficulty target with hysteresis.

    <60% correct → easier; 60-85% → default; >85% → harder.
    Default to 'default' until we have at least 3 data points."""
    if len(recent) < 3:
        return "default"
    n = max(1, len(recent))
    correct = sum(1 for r in recent if r == "correct")
    rate = correct / n
    if rate < 0.6:
        return "easier"
    if rate > 0.85:
        return "harder"
    return "default"
