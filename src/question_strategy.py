"""
PHASE 1: Question Strategy Engine

Determines what type of question to ask next based on student performance context.
Matches question difficulty and style to learning needs.
"""

from enum import Enum
from dataclasses import dataclass
from typing import Dict, List, Optional


class QuestionStrategy(Enum):
    """Enum for different question strategy types."""
    TRANSFER = "transfer"  # Novel scenario - test deep understanding
    DEEPER_PRINCIPLE = "deeper_principle"  # Ask WHY at first-principles level
    CONFIDENCE_BUILDER = "confidence_builder"  # Similar difficulty, build confidence
    DRILL_HARD = "drill_hard"  # Hammer until they understand (overconfidence)
    BACK_TO_BASICS = "back_to_basics"  # Go to fundamentals (wrong + low confidence)
    BUILD_ON_ANSWER = "build_on_answer"  # Scaffold from partial credit


class QuestionLayer(Enum):
    """Enum for levels of questioning depth."""
    WHAT = "what"  # Definition/facts
    MECHANISM = "mechanism"  # Physiology - how does it work?
    PATHOPHYSIOLOGY = "pathophysiology"  # What breaks? Why?
    APPLICATION = "application"  # Clinical scenario
    TRANSFER = "transfer"  # Novel scenario


@dataclass
class PerformanceContext:
    """Context for decision-making on question strategy."""
    accuracy: bool
    confidence_reported: int  # 1-5
    mechanism_quality: float  # 0-1 (teach-back quality)
    topic: str
    recent_accuracy_rate: float  # Last 5 questions
    topic_accuracy_rate: float  # All time for this topic


def decide_question_strategy(context: PerformanceContext) -> QuestionStrategy:
    """
    Decision tree for what type of question to ask next.

    Logic:
    - CORRECT + HIGH_CONFIDENCE + GOOD_MECHANISM -> TRANSFER (test novel scenario)
    - CORRECT + HIGH_CONFIDENCE + WEAK_MECHANISM -> DEEPER_PRINCIPLE (why?)
    - CORRECT + LOW_CONFIDENCE -> CONFIDENCE_BUILDER (same difficulty, build up)
    - WRONG + HIGH_CONFIDENCE -> DRILL_HARD (overconfidence is dangerous)
    - WRONG + LOW_CONFIDENCE -> BACK_TO_BASICS (fundamentals)
    - PARTIAL -> BUILD_ON_ANSWER (scaffold from what they know)

    Args:
        context: PerformanceContext with student performance data

    Returns:
        QuestionStrategy enum indicating what type of question to ask
    """

    # IF CORRECT + HIGH_CONFIDENCE + GOOD_MECHANISM
    if context.accuracy and context.confidence_reported >= 4 and context.mechanism_quality >= 0.75:
        return QuestionStrategy.TRANSFER

    # IF CORRECT + HIGH_CONFIDENCE + WEAK_MECHANISM (overconfident in understanding)
    if context.accuracy and context.confidence_reported >= 4 and context.mechanism_quality < 0.75:
        return QuestionStrategy.DEEPER_PRINCIPLE

    # IF CORRECT + LOW_CONFIDENCE (need confidence building)
    if context.accuracy and context.confidence_reported <= 2:
        return QuestionStrategy.CONFIDENCE_BUILDER

    # IF WRONG + HIGH_CONFIDENCE (dangerous overconfidence - drill hard)
    if not context.accuracy and context.confidence_reported >= 4:
        return QuestionStrategy.DRILL_HARD

    # IF WRONG + LOW_CONFIDENCE (need fundamentals)
    if not context.accuracy and context.confidence_reported <= 2:
        return QuestionStrategy.BACK_TO_BASICS

    # IF PARTIAL (mechanism quality 0.3-0.7, mixed accuracy)
    if 0.3 <= context.mechanism_quality < 0.75:
        return QuestionStrategy.BUILD_ON_ANSWER

    # Default fallback
    return QuestionStrategy.DRILL_HARD


def select_question_layer(strategy: QuestionStrategy) -> QuestionLayer:
    """
    Select which conceptual layer to emphasize based on strategy.

    Each strategy has a preferred sequence of layers:
    - TRANSFER: Novel scenario first, then application, then mechanism
    - DEEPER_PRINCIPLE: Mechanism and pathophysiology to understand WHY
    - CONFIDENCE_BUILDER: Easy application to build confidence
    - DRILL_HARD: Pathophysiology first (why are they wrong?), then mechanism
    - BACK_TO_BASICS: Start with mechanism and facts
    - BUILD_ON_ANSWER: Build on partial understanding through mechanism

    Args:
        strategy: QuestionStrategy enum

    Returns:
        QuestionLayer enum (randomly selected from preferred sequence)
    """
    import random

    layer_sequences = {
        QuestionStrategy.TRANSFER: [
            QuestionLayer.TRANSFER,  # Primary
            QuestionLayer.APPLICATION,
            QuestionLayer.MECHANISM
        ],
        QuestionStrategy.DEEPER_PRINCIPLE: [
            QuestionLayer.MECHANISM,
            QuestionLayer.PATHOPHYSIOLOGY,
            QuestionLayer.WHAT
        ],
        QuestionStrategy.CONFIDENCE_BUILDER: [
            QuestionLayer.APPLICATION,
            QuestionLayer.WHAT,
            QuestionLayer.MECHANISM
        ],
        QuestionStrategy.DRILL_HARD: [
            QuestionLayer.PATHOPHYSIOLOGY,  # Why are they wrong?
            QuestionLayer.MECHANISM,
            QuestionLayer.APPLICATION,
            QuestionLayer.TRANSFER
        ],
        QuestionStrategy.BACK_TO_BASICS: [
            QuestionLayer.MECHANISM,
            QuestionLayer.WHAT,
            QuestionLayer.PATHOPHYSIOLOGY
        ],
        QuestionStrategy.BUILD_ON_ANSWER: [
            QuestionLayer.MECHANISM,
            QuestionLayer.APPLICATION,
            QuestionLayer.TRANSFER
        ]
    }

    sequence = layer_sequences.get(strategy, [QuestionLayer.MECHANISM])
    return random.choice(sequence)


def explain_strategy(strategy: QuestionStrategy, context: PerformanceContext) -> str:
    """
    Generate a human-readable explanation of the chosen strategy.

    Args:
        strategy: The chosen QuestionStrategy
        context: The PerformanceContext that led to this choice

    Returns:
        String explanation of why this strategy was chosen
    """

    explanations = {
        QuestionStrategy.TRANSFER: (
            f"You nailed that with confidence and deep understanding. "
            f"Let's test it on a novel scenario."
        ),
        QuestionStrategy.DEEPER_PRINCIPLE: (
            f"You got it right, but your explanation showed some gaps. "
            f"Let's dig deeper into the mechanism."
        ),
        QuestionStrategy.CONFIDENCE_BUILDER: (
            f"You got it right but seemed unsure. Let's build confidence "
            f"with a similar question."
        ),
        QuestionStrategy.DRILL_HARD: (
            f"You were confident but wrong - that's dangerous. "
            f"Time to drill hard on this concept."
        ),
        QuestionStrategy.BACK_TO_BASICS: (
            f"You were wrong and unsure. Let's go back to fundamentals "
            f"on {context.topic}."
        ),
        QuestionStrategy.BUILD_ON_ANSWER: (
            f"You partially understood. Let's build on what you know "
            f"and fill in the gaps."
        )
    }

    return explanations.get(strategy, "Let's try another approach.")
