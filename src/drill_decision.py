"""
PHASE 3: Drill Decision Logic

Determines when to auto-drill, when to ask permission, and when to defer.
Controls pacing and respects student time constraints while maximizing learning.
"""

from enum import Enum
from dataclasses import dataclass
from typing import Optional, List, Tuple


class DrillDecision(Enum):
    """Enum for drill action decisions."""
    AUTO_DRILL = "auto_drill"  # Keep going immediately without asking
    ASK_PERMISSION = "ask_permission"  # Surface control point, ask student
    MARK_FOR_LATER = "mark_for_later"  # Defer to next session/focus area


@dataclass
class DrillContext:
    """Context for drill decision-making."""
    accuracy: bool
    confidence_reported: int  # 1-5
    mechanism_quality: float  # 0-1
    topic_accuracy_rate: float  # Overall accuracy on this topic
    is_overdue: bool  # FSRS overdue?
    is_main_topic: bool  # Primary topic for this lesson?
    time_remaining_minutes: float
    estimated_drill_time_minutes: float = 5.0  # How long to achieve mastery?


def decide_drill_action(context: DrillContext) -> DrillDecision:
    """
    Determine: auto-drill, ask permission, or defer drilling?

    Logic:
    - AUTO_DRILL: Student got it wrong OR overconfident but shallow
      AND sufficient time remains
    - ASK_PERMISSION: Student is doing well on this topic, not the main focus,
      and time is getting tight - offer but don't force
    - MARK_FOR_LATER: Main topic has low accuracy and time is tight - focus on core

    Args:
        context: DrillContext with performance and time constraints

    Returns:
        DrillDecision enum indicating how to proceed
    """

    # AUTO-DRILL: Drill immediately when student is wrong or dangerously overconfident
    if (not context.accuracy) or \
       (context.accuracy and context.confidence_reported >= 4 and context.mechanism_quality < 0.6):
        # Student got it wrong OR overconfident but shallow understanding
        if context.time_remaining_minutes > context.estimated_drill_time_minutes:
            return DrillDecision.AUTO_DRILL

    # ASK_PERMISSION: Respect their time when doing well on secondary topics
    if (context.topic_accuracy_rate > 0.7 and  # Doing well overall
            not context.is_main_topic and  # Not the primary focus
            context.time_remaining_minutes < context.estimated_drill_time_minutes * 2):
        return DrillDecision.ASK_PERMISSION

    # MARK_FOR_LATER: Don't overwhelm on main topic if time is tight
    if (context.topic_accuracy_rate < 0.5 and  # Struggling on main topic
            context.is_main_topic and
            context.time_remaining_minutes < context.estimated_drill_time_minutes * 1.5):
        return DrillDecision.MARK_FOR_LATER

    # Default: Auto-drill if there's time and performance indicates need
    if context.time_remaining_minutes > context.estimated_drill_time_minutes * 0.5:
        return DrillDecision.AUTO_DRILL

    return DrillDecision.MARK_FOR_LATER


def get_drill_prompt(decision: DrillDecision, context: DrillContext, topic: str) -> str:
    """
    Generate appropriate prompt for student based on drill decision.

    Args:
        decision: The DrillDecision
        context: The DrillContext
        topic: Topic name

    Returns:
        String with prompt or question for student
    """

    if decision == DrillDecision.AUTO_DRILL:
        if not context.accuracy:
            return f"Let's drill harder on {topic}. Next question:"
        else:
            return f"You know the facts, but let's test your understanding deeper. Next question:"

    elif decision == DrillDecision.ASK_PERMISSION:
        return f"You're doing well on {topic}. Want to drill deeper, or move on to something else?"

    else:  # MARK_FOR_LATER
        return f"This is important - {topic} is key to master. I'm noting it for our next session. Moving on to cover more ground for now."


def estimate_mastery_time(
    topic_accuracy_rate: float,
    mechanism_quality: float,
    recent_confidence_calibration: float
) -> float:
    """
    Estimate minutes needed to reach mastery on a topic.

    Factors:
    - Current accuracy: lower accuracy = longer drill
    - Mechanism quality: lower mechanism = need more explanation time
    - Confidence calibration: poor calibration = harder to know when done

    Args:
        topic_accuracy_rate: Current accuracy (0-1)
        mechanism_quality: Quality of mechanism understanding (0-1)
        recent_confidence_calibration: Calibration ICC (0-1)

    Returns:
        Estimated minutes to mastery
    """

    # Base time depends on current accuracy
    if topic_accuracy_rate < 0.5:
        base_minutes = 10  # Need significant rework
    elif topic_accuracy_rate < 0.7:
        base_minutes = 6
    elif topic_accuracy_rate < 0.85:
        base_minutes = 4
    else:
        base_minutes = 2

    # Adjust for mechanism quality (conceptual understanding)
    if mechanism_quality < 0.5:
        base_minutes *= 1.5  # Need more explanation time
    elif mechanism_quality < 0.7:
        base_minutes *= 1.2

    # Adjust for confidence calibration (harder to know when done)
    if recent_confidence_calibration < 0.5:
        base_minutes *= 1.3  # More verification needed

    return max(2, base_minutes)  # Minimum 2 minutes


def should_drill_topic(
    is_overdue: bool,
    topic_accuracy_rate: float,
    is_main_topic: bool,
    time_available: float
) -> bool:
    """
    Simple boolean: should we drill this topic at all?

    Prioritizes overdue topics and main topics. Respects time.

    Args:
        is_overdue: FSRS overdue?
        topic_accuracy_rate: Current accuracy
        is_main_topic: Is this the primary focus?
        time_available: Minutes available

    Returns:
        True if drilling would be appropriate
    """

    # Overdue topics are priority
    if is_overdue:
        return time_available >= 3

    # Low accuracy needs drilling
    if topic_accuracy_rate < 0.7:
        return time_available >= 5

    # Main topic should get some drilling
    if is_main_topic:
        return time_available >= 4

    # Secondary topics only if time permits
    return time_available >= 8


def recommend_next_drill_topic(
    weak_topics: List[Tuple[str, float]],  # [(topic, accuracy_rate), ...]
    due_topics: List[str],
    time_remaining_minutes: float,
    is_main_topic_weak: bool
) -> Optional[str]:
    """
    Recommend which topic to drill next given constraints.

    Priority:
    1. Main topic if it's weak
    2. FSRS overdue topics
    3. Weakest secondary topic

    Args:
        weak_topics: List of (topic_name, accuracy_rate) tuples
        due_topics: List of FSRS due topic names
        time_remaining_minutes: Minutes left in session
        is_main_topic_weak: Is the main topic below 70%?

    Returns:
        Recommended topic name, or None if no drilling recommended
    """

    # Main topic has priority if weak
    if is_main_topic_weak and time_remaining_minutes >= 5:
        return weak_topics[0][0] if weak_topics else None

    # FSRS due topics are high priority
    if due_topics and time_remaining_minutes >= 4:
        return due_topics[0]

    # Drill weakest secondary topic if time permits
    if weak_topics and time_remaining_minutes >= 6:
        return weak_topics[0][0]

    # Not enough time for drilling
    return None
