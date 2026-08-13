"""
PHASE 2: Lesson Planning

Generates structured lesson plans based on student goals, time, and learning state.
Coordinates FSRS due topics, weak areas, and new material.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Callable
from enum import Enum
from datetime import datetime, timedelta
import re
import sqlite3

# Front/back-matter and boilerplate that can leak in from PDF section headings and
# should never be served as a study topic.
_JUNK_TOPIC = re.compile(
    r"(?i)(disclaimer|copyright|^references?$|bibliograph|^index$|acknowledg|"
    r"table of contents|^contents$|preface|foreword|^appendix|isbn|978-|"
    r"about the author|errata|glossary|dedication|permissions|^credits?$|"
    r"title page|front matter|back matter)"
)


def _is_junk_topic(name: Optional[str]) -> bool:
    return bool(name) and bool(_JUNK_TOPIC.search(name.strip()))


class LessonMode(Enum):
    """Enum for different lesson modes."""
    STANDARD = "standard"  # Single deep topic
    EXAM_PREP = "exam_prep"  # Many topics, single Q each
    DEEP_DIVE = "deep_dive"  # One topic, very thorough
    CATCH_UP = "catch_up"  # FSRS overdue topics
    WEAK_AREA_FOCUS = "weak_area_focus"  # Fix weak topics
    MIXED_REVIEW = "mixed_review"  # Maintain past topics


@dataclass
class LessonPlan:
    """Structure representing a complete lesson plan."""
    mode: LessonMode
    duration_minutes: int
    primary_topic: str
    secondary_topics: List[str] = field(default_factory=list)
    objectives: List[str] = field(default_factory=list)
    estimated_questions: int = 0
    strategy_notes: str = ""
    drill_aggressiveness: str = "medium"  # "light", "medium", "heavy"
    focus_areas: str = ""  # "single_topic", "weak_areas", "all_due", etc.
    skip_new_material: bool = False
    include_transfer: bool = True


def generate_lesson_plan(
    duration_minutes: int = 20,
    mode: LessonMode = LessonMode.STANDARD,
    focus_topic: Optional[str] = None,
    db_conn: Optional[sqlite3.Connection] = None
) -> LessonPlan:
    """
    Generate structured lesson plan based on user goals.

    Queries FSRS state and attempts history to determine:
    - Which topics are due for review
    - Which topics have high error rates
    - Overall progress toward mastery

    Args:
        duration_minutes: How long the lesson should be
        mode: LessonMode enum indicating type of lesson
        focus_topic: Optional topic to focus on (overrides auto-selection)
        db_conn: Database connection to query FSRS state

    Returns:
        LessonPlan with structured objectives, topics, and strategy
    """

    # Get due topics (FSRS overdue)
    due_topics = []
    weak_topics = []

    if db_conn:
        cursor = db_conn.cursor()

        # Get FSRS due topics (next_review_date <= today)
        cursor.execute("""
            SELECT topic FROM topics
            WHERE next_review_date IS NOT NULL
            AND next_review_date <= date('now')
            ORDER BY next_review_date ASC
            LIMIT 10
        """)
        due_topics = [row[0] for row in cursor.fetchall() if not _is_junk_topic(row[0])]

        # Get weak topics (error_rate > 30% in last 7 days)
        cursor.execute("""
            SELECT topic,
                   COUNT(*) as total,
                   SUM(CASE WHEN result != 'correct' THEN 1 ELSE 0 END) as errors
            FROM question_attempts
            WHERE date >= date('now', '-7 days')
            GROUP BY topic
            HAVING (errors * 1.0 / total) > 0.30
            ORDER BY (errors * 1.0 / total) DESC
            LIMIT 5
        """)
        weak_topics = [row[0] for row in cursor.fetchall() if not _is_junk_topic(row[0])]

    # Build plan based on mode
    if mode == LessonMode.EXAM_PREP:
        primary = focus_topic or (due_topics[0] if due_topics else "cardiology")
        secondary = due_topics[1:4] if len(due_topics) > 1 else []

        plan = LessonPlan(
            mode=mode,
            duration_minutes=duration_minutes,
            primary_topic=primary,
            secondary_topics=secondary,
            objectives=[
                "Cover breadth of key topics",
                "Quick mastery checks",
                "Identify remaining weak areas"
            ],
            estimated_questions=int(duration_minutes / 2),  # ~1 Q per 2 min
            strategy_notes="Single question per topic to assess mastery, then transfer Q",
            drill_aggressiveness="light",
            focus_areas="all_due_topics",
            include_transfer=True,
            skip_new_material=True
        )

    elif mode == LessonMode.DEEP_DIVE:
        primary = focus_topic or (due_topics[0] if due_topics else "shock")

        plan = LessonPlan(
            mode=mode,
            duration_minutes=duration_minutes,
            primary_topic=primary,
            secondary_topics=[],
            objectives=[
                f"Master fundamentals of {primary}",
                "Understand mechanisms at first-principles level",
                "Apply to novel clinical scenarios",
                "Build confidence and calibration"
            ],
            estimated_questions=int(duration_minutes / 3),  # ~1 Q per 3 min
            strategy_notes="Deep dive: test all layers (what/mechanism/patho/app/transfer), multiple angles",
            drill_aggressiveness="heavy",
            focus_areas="single_topic",
            include_transfer=True,
            skip_new_material=True
        )

    elif mode == LessonMode.CATCH_UP:
        primary = due_topics[0] if due_topics else "shock"
        secondary = due_topics[1:3] if len(due_topics) > 1 else []

        plan = LessonPlan(
            mode=mode,
            duration_minutes=duration_minutes,
            primary_topic=primary,
            secondary_topics=secondary,
            objectives=[
                "Catch up on overdue FSRS topics",
                "Refresh knowledge before decay",
                "Rebuild spaced repetition schedule"
            ],
            estimated_questions=int(duration_minutes / 2.5),
            strategy_notes="Intensive drilling on overdue topics only",
            drill_aggressiveness="heavy",
            focus_areas="fsrs_overdue_only",
            include_transfer=True,
            skip_new_material=True
        )

    elif mode == LessonMode.WEAK_AREA_FOCUS:
        primary = weak_topics[0] if weak_topics else "vasopressors"
        secondary = weak_topics[1:3] if len(weak_topics) > 1 else []

        plan = LessonPlan(
            mode=mode,
            duration_minutes=duration_minutes,
            primary_topic=primary,
            secondary_topics=secondary,
            objectives=[
                f"Fix weak areas in {primary}",
                "Build understanding from first principles",
                "Increase accuracy on common mistakes"
            ],
            estimated_questions=int(duration_minutes / 2),
            strategy_notes="Focus entirely on weak areas, drill hard on mechanisms",
            drill_aggressiveness="heavy",
            focus_areas="weak_topics_only",
            include_transfer=True,
            skip_new_material=True
        )

    elif mode == LessonMode.MIXED_REVIEW:
        primary = weak_topics[0] if weak_topics else (due_topics[0] if due_topics else "shock")
        secondary = (weak_topics[1:2] if len(weak_topics) > 1 else []) + (due_topics[0:2] if due_topics else [])

        plan = LessonPlan(
            mode=mode,
            duration_minutes=duration_minutes,
            primary_topic=primary,
            secondary_topics=secondary,
            objectives=[
                "Maintain previously mastered topics",
                "Strengthen weak areas",
                "Keep spaced repetition on schedule"
            ],
            estimated_questions=int(duration_minutes / 2),
            strategy_notes="Quick refresh on medium mastery, intensive drill on weak areas",
            drill_aggressiveness="medium",
            focus_areas="weak_and_medium",
            include_transfer=False,
            skip_new_material=True
        )

    else:  # STANDARD (default)
        primary = focus_topic or (due_topics[0] if due_topics else "shock")
        secondary = due_topics[1:2] if len(due_topics) > 1 and duration_minutes >= 20 else []

        plan = LessonPlan(
            mode=mode,
            duration_minutes=duration_minutes,
            primary_topic=primary,
            secondary_topics=secondary,
            objectives=[
                f"Master fundamentals of {primary}",
                "Test transfer to novel scenarios",
                "Build confidence"
            ],
            estimated_questions=int(duration_minutes / 2.5),
            strategy_notes="Standard: teach mechanism -> apply clinically -> test transfer",
            drill_aggressiveness="medium",
            focus_areas="single_topic",
            include_transfer=True,
            skip_new_material=False
        )

    return plan


def format_lesson_plan_for_display(plan: LessonPlan) -> str:
    """
    Format lesson plan as human-readable text.

    Args:
        plan: LessonPlan to format

    Returns:
        Formatted string representation
    """

    lines = [
        f"\n=== LESSON PLAN: {plan.mode.value.upper()} ===",
        f"Duration: {plan.duration_minutes} minutes",
        f"Primary Topic: {plan.primary_topic}",
    ]

    if plan.secondary_topics:
        lines.append(f"Secondary Topics: {', '.join(plan.secondary_topics)}")

    lines.append(f"\nObjectives:")
    for obj in plan.objectives:
        lines.append(f"  • {obj}")

    lines.extend([
        f"\nEstimated Questions: {plan.estimated_questions}",
        f"Drill Aggressiveness: {plan.drill_aggressiveness.upper()}",
        f"\nStrategy: {plan.strategy_notes}",
    ])

    return "\n".join(lines)
