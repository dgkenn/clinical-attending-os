"""
PHASE 4: Special Modes Handler

Applies mode-specific rules and modifications to lesson behavior.
Coordinates with question strategy and drill decision engines.
"""

from enum import Enum
from typing import Dict, List, Any
from dataclasses import dataclass


class SpecialMode(Enum):
    """Enum for special lesson modes."""
    EXAM_PREP = "exam_prep"
    DEEP_DIVE = "deep_dive"
    CATCH_UP = "catch_up"
    WEAK_AREA_FOCUS = "weak_area_focus"
    MIXED_REVIEW = "mixed_review"
    STANDARD = "standard"


@dataclass
class ModeRules:
    """Configuration rules for a lesson mode."""
    max_drill_per_topic: int
    min_drill_per_topic: int
    include_transfer: bool
    prioritize_coverage: bool = False
    prioritize_depth: bool = False
    show_feedback: str = "immediate"  # "immediate" | "batched" | "end_of_session"
    focus_areas: str = ""
    aggressive_drilling: bool = False
    skip_new_material: bool = False
    test_all_layers: bool = False
    mechanism_emphasis: bool = False
    quick_questions: bool = False
    mechanism_confidence_threshold: float = 0.7  # When to consider mechanism understood


def apply_special_mode_rules(mode: SpecialMode) -> Dict[str, Any]:
    """
    Get configuration rules for a lesson mode.

    Defines how the tutor should behave for each mode:
    - Question selection and drilling intensity
    - Feedback timing
    - Coverage vs. depth priorities
    - Transfer question inclusion

    Args:
        mode: SpecialMode enum

    Returns:
        Dict with mode configuration rules
    """

    rules_map = {
        SpecialMode.EXAM_PREP: {
            "max_drill_per_topic": 1,
            "min_drill_per_topic": 1,
            "include_transfer": True,
            "prioritize_coverage": True,
            "prioritize_depth": False,
            "show_feedback": "end_of_session",  # Batch feedback
            "focus_areas": "all_due_topics",
            "aggressive_drilling": False,
            "skip_new_material": True,
            "test_all_layers": False,
            "mechanism_emphasis": False,
            "quick_questions": True,
            "mechanism_confidence_threshold": 0.5,  # Lower bar for exam prep
            "description": "Rapid coverage of key topics. Single Q per topic, then transfer."
        },

        SpecialMode.DEEP_DIVE: {
            "max_drill_per_topic": 999,  # Unlimited
            "min_drill_per_topic": 5,
            "include_transfer": True,
            "prioritize_coverage": False,
            "prioritize_depth": True,
            "show_feedback": "immediate",
            "focus_areas": "single_topic",
            "aggressive_drilling": True,
            "skip_new_material": True,
            "test_all_layers": True,  # Test WHAT, MECHANISM, PATHO, APP, TRANSFER
            "mechanism_emphasis": True,
            "quick_questions": False,
            "mechanism_confidence_threshold": 0.85,  # High bar
            "description": "Deep mastery on one topic. All layers, multiple angles, transfer testing."
        },

        SpecialMode.CATCH_UP: {
            "max_drill_per_topic": 999,
            "min_drill_per_topic": 3,
            "include_transfer": True,
            "prioritize_coverage": False,
            "prioritize_depth": True,
            "show_feedback": "immediate",
            "focus_areas": "fsrs_overdue_only",
            "aggressive_drilling": True,
            "skip_new_material": True,
            "test_all_layers": False,
            "mechanism_emphasis": True,
            "quick_questions": False,
            "mechanism_confidence_threshold": 0.7,
            "description": "Intensive on overdue FSRS topics only."
        },

        SpecialMode.WEAK_AREA_FOCUS: {
            "max_drill_per_topic": 999,
            "min_drill_per_topic": 4,
            "include_transfer": True,
            "prioritize_coverage": False,
            "prioritize_depth": True,
            "show_feedback": "immediate",
            "focus_areas": "weak_topics_only",
            "aggressive_drilling": True,
            "skip_new_material": True,
            "test_all_layers": False,
            "mechanism_emphasis": True,
            "quick_questions": False,
            "mechanism_confidence_threshold": 0.8,  # High bar to fix weak areas
            "description": "Focus entirely on weak areas. Heavy drilling on mechanisms."
        },

        SpecialMode.MIXED_REVIEW: {
            "max_drill_per_topic": 3,
            "min_drill_per_topic": 1,
            "include_transfer": False,
            "prioritize_coverage": True,
            "prioritize_depth": False,
            "show_feedback": "immediate",
            "focus_areas": "weak_and_medium",
            "aggressive_drilling": False,
            "skip_new_material": True,
            "test_all_layers": False,
            "mechanism_emphasis": False,
            "quick_questions": True,
            "mechanism_confidence_threshold": 0.6,
            "description": "Quick refresh on medium mastery, drill weak areas."
        },

        SpecialMode.STANDARD: {
            "max_drill_per_topic": 5,
            "min_drill_per_topic": 1,
            "include_transfer": True,
            "prioritize_coverage": False,
            "prioritize_depth": True,
            "show_feedback": "immediate",
            "focus_areas": "single_topic",
            "aggressive_drilling": False,
            "skip_new_material": False,
            "test_all_layers": False,
            "mechanism_emphasis": True,
            "quick_questions": False,
            "mechanism_confidence_threshold": 0.75,
            "description": "Standard lesson: teach mechanism -> apply -> test transfer."
        }
    }

    return rules_map.get(mode, rules_map[SpecialMode.STANDARD])


def get_mode_description(mode: SpecialMode) -> str:
    """
    Get human-readable description of lesson mode.

    Args:
        mode: SpecialMode enum

    Returns:
        String description
    """

    rules = apply_special_mode_rules(mode)
    return rules.get("description", "Standard learning mode.")


def should_include_layer_in_mode(mode: SpecialMode, layer: str) -> bool:
    """
    Determine if a question layer should be included in this mode.

    Some modes skip certain layers for efficiency:
    - Exam prep: skip mechanism/pathophysiology depth
    - Mixed review: skip TRANSFER questions
    - etc.

    Args:
        mode: SpecialMode enum
        layer: Question layer ("what", "mechanism", "pathophysiology", "application", "transfer")

    Returns:
        True if this layer should be included
    """

    skip_rules = {
        SpecialMode.EXAM_PREP: [],  # Include all but manage drilling
        SpecialMode.DEEP_DIVE: [],  # Include all
        SpecialMode.CATCH_UP: [],  # Include all
        SpecialMode.WEAK_AREA_FOCUS: [],  # Include all
        SpecialMode.MIXED_REVIEW: ["transfer"],  # Skip transfer for speed
        SpecialMode.STANDARD: [],  # Include all
    }

    skip_list = skip_rules.get(mode, [])
    return layer.lower() not in skip_list


def get_feedback_style_for_mode(mode: SpecialMode) -> Dict[str, Any]:
    """
    Get feedback display style recommendations for this mode.

    Args:
        mode: SpecialMode enum

    Returns:
        Dict with feedback style configuration
    """

    rules = apply_special_mode_rules(mode)

    feedback_timing = rules.get("show_feedback", "immediate")

    return {
        "timing": feedback_timing,
        "detail_level": "comprehensive" if rules.get("mechanism_emphasis") else "summary",
        "show_mechanism_gaps": rules.get("mechanism_emphasis"),
        "show_confidence_calibration": rules.get("prioritize_depth"),
        "batch_feedback_at_end": (feedback_timing == "end_of_session"),
        "emphasize_transfer": rules.get("include_transfer"),
    }


def adapt_question_difficulty_for_mode(
    mode: SpecialMode,
    base_difficulty: float,  # 0-1, where 0.5 is medium
    current_accuracy: float
) -> float:
    """
    Adjust question difficulty based on mode.

    Exam prep should stay at medium difficulty (assess not teach).
    Deep dive should progressively increase difficulty.

    Args:
        mode: SpecialMode enum
        base_difficulty: Base difficulty of question (0-1)
        current_accuracy: Student's current accuracy (0-1)

    Returns:
        Adjusted difficulty value (0-1)
    """

    if mode == SpecialMode.EXAM_PREP:
        # Exam prep: stay at medium difficulty (assess, not teach)
        return 0.5

    elif mode == SpecialMode.DEEP_DIVE:
        # Deep dive: progressively increase difficulty as accuracy improves
        if current_accuracy > 0.85:
            return min(1.0, base_difficulty + 0.3)
        elif current_accuracy > 0.7:
            return min(1.0, base_difficulty + 0.15)
        else:
            return base_difficulty

    elif mode == SpecialMode.CATCH_UP:
        # Catch up: keep at moderate difficulty, focus on mechanism
        return 0.55

    elif mode == SpecialMode.WEAK_AREA_FOCUS:
        # Weak area: start lower, ramp up gradually
        if current_accuracy < 0.4:
            return 0.3
        elif current_accuracy < 0.6:
            return 0.4
        else:
            return 0.5

    elif mode == SpecialMode.MIXED_REVIEW:
        # Mixed review: keep moderate for speed
        return 0.5

    else:  # STANDARD
        # Standard: adaptive difficulty
        if current_accuracy > 0.8:
            return min(1.0, base_difficulty + 0.2)
        elif current_accuracy < 0.6:
            return max(0.2, base_difficulty - 0.2)
        else:
            return base_difficulty
