"""
PHASE 5: First Principles Integration

Ensures every topic gets comprehensive coverage across all question layers.
Maps physiology + pathophysiology questions for deep understanding.
"""

from typing import List, Dict, Optional
from enum import Enum


class QuestionLayer(Enum):
    """Question depth layers."""
    WHAT = "what"
    MECHANISM = "mechanism"
    PATHOPHYSIOLOGY = "pathophysiology"
    APPLICATION = "application"
    TRANSFER = "transfer"


# Comprehensive mapping of topics to first-principles questions
# This would be expanded to cover all 1,321+ topics in the curriculum
TOPIC_LAYER_QUESTIONS = {
    "shock": {
        "what": "Define shock in terms of cellular perfusion.",
        "mechanism": "Walk me through cardiovascular physiology: CO = HR × SV. When CO drops, what happens to tissue perfusion? Why?",
        "pathophysiology": "In SEPTIC shock, what breaks at the cellular level? Explain vasodilation, endothelial dysfunction, and mitochondrial dysfunction.",
        "application": "65-year-old with septic shock, BP 85/50. Walk through your immediate management priorities.",
        "transfer": "Same patient now deteriorating on pressors. You consider ECMO. How does mechanical support change your physiology understanding?"
    },

    "pneumonia": {
        "what": "What is pneumonia? How does it differ from acute bronchitis?",
        "mechanism": "Normal lung physiology: alveolar-capillary interface, diffusion, ventilation-perfusion. What happens when infected?",
        "pathophysiology": "Why does pneumonia cause hypoxia? Mechanism of consolidation, edema, inflammation.",
        "application": "45-year-old with fever, cough, infiltrate on CXR. When do you give antibiotics? What's the decision logic?",
        "transfer": "Same patient is immunocompromised (HIV CD4<200). Does your organism suspicion change? Management?"
    },

    "vasopressors": {
        "what": "What is the difference between inotropes and vasopressors?",
        "mechanism": "Catecholamine physiology: alpha-1, beta-1, beta-2, dopamine receptors and their effects.",
        "pathophysiology": "Why does septic shock cause vasodilation? Why don't vasopressors alone work?",
        "application": "Patient in septic shock on fluids + norepinephrine, MAP still 55. Do you add epinephrine or increase norepinephrine?",
        "transfer": "Same patient now has ACS on the EKG. How do you balance shock management with cardiology?"
    },

    "ARDS": {
        "what": "What are the Berlin Criteria for ARDS?",
        "mechanism": "Alveolar-capillary membrane: normal permeability vs. increased permeability in ARDS.",
        "pathophysiology": "What is DAD (diffuse alveolar damage)? Timeline: exudative vs. fibroproliferative phase.",
        "application": "Patient post-aspiration, now with O2 req 60%, bilateral infiltrates. Are they ARDS? How do you manage?",
        "transfer": "ARDS from COVID. How does the inflammatory pattern differ from bacterial sepsis-induced ARDS?"
    },

    "hypoxemia": {
        "what": "Define hypoxemia. What is the A-a gradient?",
        "mechanism": "5 mechanisms of hypoxemia: hypoventilation, diffusion impairment, V/Q mismatch, shunt, low FiO2.",
        "pathophysiology": "Why does atelectasis cause shunt? Why doesn't supplemental O2 fix shunt?",
        "application": "O2 sat 88% on RA, 92% on 3L NC, 94% on 15L NRB. What's the likely mechanism? Next step?",
        "transfer": "Same patient with known intracardiac shunt (PFO). How does that change your interpretation?"
    },

    "hyperkalemia": {
        "what": "What is hyperkalemia? When is it dangerous?",
        "mechanism": "Potassium handling: renal excretion, cellular uptake, GI losses. K+ physiology in cardiac and skeletal muscle.",
        "pathophysiology": "Why does hyperkalemia cause peaked T waves? EKG progression of hyperkalemia.",
        "application": "K 7.2, peaked Ts on EKG. What's your immediate management? Order the interventions by speed.",
        "transfer": "Same patient has DKA. How does the insulin/glucose effect on potassium change your approach?"
    },

    "hypokalemia": {
        "what": "What is hypokalemia?",
        "mechanism": "Potassium depletion vs. shifts. Mechanisms of K+ wasting: diuretics, diarrhea, renal tubular disease.",
        "pathophysiology": "Why does hypokalemia cause atrial fibrillation? U waves on EKG.",
        "application": "K 2.8, patient on furosemide. Risk/benefit of correction? How aggressively?",
        "transfer": "Same patient now has VT (K 2.8). Does that change your aggressiveness of K+ repletion?"
    },

    "acute_kidney_injury": {
        "what": "Define AKI. What are the KDIGO stages?",
        "mechanism": "Renal physiology: glomerular filtration, tubular function. What breaks in AKI?",
        "pathophysiology": "Three types of AKI: prerenal, intrinsic (ATN, GN, interstitial), postrenal. Pathophysiology of ATN.",
        "application": "Cr 2.8 (baseline 1.0), UOP 200mL/day, FENa 0.2%. Type of AKI? Management?",
        "transfer": "Same patient with rhabdo (CK 10,000). Does that change your fluid strategy vs. typical ATN?"
    },

    "sepsis": {
        "what": "Sepsis-3 criteria? SIRS vs. sepsis.",
        "mechanism": "Inflammatory cascade: pattern recognition receptors, cytokines, complement, coagulation.",
        "pathophysiology": "Distributive shock: why is vasodilatation inappropriate? Mitochondrial dysfunction.",
        "application": "Patient with fever, lactate 3, meets sepsis criteria. Empiric antibiotics or culture first? Why?",
        "transfer": "Same patient has fungal risk (neutropenic). Antibiotic coverage changes?"
    }

    # ... Add for all 1,321+ topics in the curriculum
    # Structure: topic_name -> {layer -> question}
}


def ensure_first_principles_coverage(
    topic: str,
    question_count: int = 1,
    layers_to_test: Optional[List[str]] = None
) -> List[Dict[str, str]]:
    """
    Generate questions across all conceptual layers for a topic.

    Ensures comprehensive coverage of what/mechanism/pathophysiology/application/transfer.

    Args:
        topic: Topic name (e.g., "shock")
        question_count: Number of questions to generate
        layers_to_test: Optional list of layers to prioritize (e.g., ["mechanism", "pathophysiology"])

    Returns:
        List of dicts with 'topic', 'layer', 'question', 'hint'
    """

    # Get topic questions, fallback to generic template
    topic_questions = TOPIC_LAYER_QUESTIONS.get(
        topic.lower().replace(" ", "_"),
        _generate_generic_template(topic)
    )

    # Determine which layers to test
    if layers_to_test:
        layer_list = layers_to_test
    else:
        # Default: cycle through all layers
        layer_list = ["mechanism", "pathophysiology", "application", "transfer", "what"]

    # Generate questions by cycling through layers
    questions = []
    for i in range(question_count):
        layer = layer_list[i % len(layer_list)]
        question_text = topic_questions.get(layer, f"Explain {topic} at the {layer} level.")

        questions.append({
            "topic": topic,
            "layer": layer,
            "question": question_text,
            "hint": _get_hint_for_layer(layer, topic),
            "layer_enum": QuestionLayer[layer.upper()].value
        })

    return questions


def _generate_generic_template(topic: str) -> Dict[str, str]:
    """
    Generate a generic question template for topics not explicitly mapped.

    Args:
        topic: Topic name

    Returns:
        Dict with questions for each layer
    """

    return {
        "what": f"What is {topic}? Define it clinically.",
        "mechanism": f"Explain the physiological mechanism of {topic}. How does normal physiology relate to pathophysiology?",
        "pathophysiology": f"What breaks down in {topic}? Explain the pathophysiological cascade at cellular/organ level.",
        "application": f"Clinical scenario: You encounter a patient with {topic}. Walk through your diagnostic and management approach.",
        "transfer": f"Novel scenario: Apply your understanding of {topic} to a complex patient with multiple comorbidities. How would you adapt?"
    }


def _get_hint_for_layer(layer: str, topic: str) -> str:
    """
    Get a helpful hint for a specific layer.

    Args:
        layer: Question layer ("what", "mechanism", etc.)
        topic: Topic name

    Returns:
        Hint string
    """

    hints = {
        "what": f"Start with a clear definition. What is the key distinguishing feature of {topic}?",
        "mechanism": f"Think about normal physiology first. How does the body's normal function apply to {topic}?",
        "pathophysiology": f"What goes wrong at the cellular, tissue, or organ level? Why?",
        "application": f"Consider a real patient you've seen. What's the clinical presentation? What would you do?",
        "transfer": f"Can you apply this to a patient with different risk factors or comorbidities? Would your approach change?"
    }

    return hints.get(layer, "Think carefully about this question.")


def score_mechanism_quality(
    student_answer: str,
    layer: str,
    topic: str
) -> float:
    """
    Score how well the student demonstrated understanding at a specific layer.

    Simple heuristic scoring based on answer length and key terms.
    In production, this would use Claude for semantic evaluation.

    Args:
        student_answer: Student's written answer
        layer: Question layer
        topic: Topic name

    Returns:
        Score 0-1 indicating quality of mechanism understanding
    """

    # Minimum length expectations
    min_lengths = {
        "what": 20,
        "mechanism": 80,
        "pathophysiology": 100,
        "application": 150,
        "transfer": 150
    }

    answer_length = len(student_answer.split())
    min_length = min_lengths.get(layer, 50)

    # Score based on length as proxy for depth
    if answer_length < min_length * 0.3:
        score = 0.2
    elif answer_length < min_length * 0.6:
        score = 0.4
    elif answer_length < min_length * 0.9:
        score = 0.6
    elif answer_length < min_length * 1.2:
        score = 0.8
    else:
        score = 0.95

    # Bonus for mentioning mechanisms/pathophysiology keywords
    mechanism_keywords = {
        "mechanism": ["physiology", "pathway", "process", "function", "normal", "how"],
        "pathophysiology": ["breaks", "fails", "damage", "dysfunction", "abnormal", "why"],
        "application": ["patient", "clinical", "diagnosis", "manage", "treat", "assess"],
        "transfer": ["novel", "different", "change", "adapt", "apply", "complex"]
    }

    keywords = mechanism_keywords.get(layer, [])
    keyword_hits = sum(1 for kw in keywords if kw.lower() in student_answer.lower())

    if keyword_hits > 0:
        score = min(1.0, score + keyword_hits * 0.05)

    return score


def get_layer_progression(topic: str) -> List[str]:
    """
    Get recommended question layer progression for learning a new topic.

    Standard progression: what -> mechanism -> pathophysiology -> application -> transfer

    Args:
        topic: Topic name

    Returns:
        Ordered list of layers (as strings)
    """

    return ["what", "mechanism", "pathophysiology", "application", "transfer"]


def is_topic_fully_covered(
    topic: str,
    layers_tested: List[str]
) -> bool:
    """
    Determine if a topic has been tested across enough layers for mastery.

    Requirements:
    - Mechanism: must be tested
    - Pathophysiology: must be tested
    - Application: should be tested
    - Transfer: should be tested (for advanced mastery)

    Args:
        topic: Topic name
        layers_tested: List of layers already tested

    Returns:
        True if coverage is adequate for mastery
    """

    must_have = {"mechanism", "pathophysiology"}
    should_have = {"application"}
    ideal_have = {"transfer"}

    tested_set = set(layers_tested)

    if not must_have.issubset(tested_set):
        return False

    if not should_have.issubset(tested_set):
        return False

    # For full mastery, should have transfer
    # (but basic mastery okay without it)

    return True
