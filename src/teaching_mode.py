"""Protégé effect ("learning by teaching") — the user explains a topic to
the GPT, who plays a confused MS3 asking probing questions.

The backend's job: return source-grounded scaffolding so the GPT's "student"
questions are anchored in real material rather than made up. Includes:

- 4-6 student-question seeds (probing the connections the user should hit)
- Top source chunks for the topic (mechanism, dose, indication, contraindication)
- A coverage rubric — concepts the user should mention to score "thorough"
- A grading hint at the end (gaps in user's explanation)

The GPT instructions handle the persona ("play a confused MS3") and the
flow (4-6 turns, end with feedback). This endpoint is pure data.
"""

from __future__ import annotations

from typing import Any

from .retrieval import hybrid_search
from .schemas import SourceChunk


# Standard probes that work for almost any clinical topic. The GPT gets these
# as seeds and picks the ones most relevant.
PROBE_SEEDS_GENERIC = [
    "Wait — why does that work mechanically? I keep mixing up the receptors.",
    "What's the contraindication you'd never want to miss here?",
    "If I told you the patient is also on dialysis, does that change anything?",
    "How would you know if your treatment isn't working?",
    "What's the next step if the first-line fails?",
    "What's the dose, and is it weight-based or flat?",
    "When would you NOT do this?",
]

PROBE_SEEDS_CRISIS = [
    "If I'm at the bedside and this is happening, what's the literal first thing I do?",
    "What's the differential — what else looks like this?",
    "When do I call for help vs handle it myself?",
    "What labs/monitoring tells me it's working or worsening?",
]

PROBE_SEEDS_DRUG = [
    "Why this drug instead of the alternatives in the same class?",
    "What's the half-life and does it matter clinically?",
    "What's the antidote / reversal if it goes wrong?",
    "Renal vs hepatic dosing — which one is this?",
    "What hemodynamic effects do I need to brace for?",
]

PROBE_SEEDS_PHYSIOLOGY = [
    "Walk me through the physiology — what's the upstream driver?",
    "If preload changes, what happens here?",
    "How does this look different in the elderly / pregnant / pediatric patient?",
    "What's the boards-level distinction between A and B that always trips me up?",
]


# Topics that obviously fall into a category get the corresponding probe set.
CRISIS_TOPICS = {"malignant hyperthermia", "anaphylaxis", "code blue", "high spinal",
                 "tension pneumothorax", "last", "aspiration", "bronchospasm",
                 "stroke", "status epilepticus", "stemi"}
DRUG_TOPICS = {"propofol", "etomidate", "ketamine", "succinylcholine", "rocuronium",
               "fentanyl", "remifentanil", "dexmedetomidine", "labetalol",
               "lidocaine", "bupivacaine", "dantrolene", "epinephrine",
               "norepinephrine", "vasopressin", "phenylephrine", "amiodarone"}
PHYSIOLOGY_TOPICS = {"shock", "hypoxemia", "hypotension", "shunt", "v/q",
                     "respiratory physiology", "cardiovascular physiology",
                     "acid base", "ards", "mac"}


def _seeds_for_topic(topic: str) -> list[str]:
    low = topic.lower()
    seeds = list(PROBE_SEEDS_GENERIC[:3])  # always include 3 generic anchors
    if any(t in low for t in CRISIS_TOPICS):
        seeds.extend(PROBE_SEEDS_CRISIS[:3])
    elif any(t in low for t in DRUG_TOPICS):
        seeds.extend(PROBE_SEEDS_DRUG[:3])
    elif any(t in low for t in PHYSIOLOGY_TOPICS):
        seeds.extend(PROBE_SEEDS_PHYSIOLOGY[:3])
    else:
        seeds.extend(PROBE_SEEDS_GENERIC[3:6])
    return seeds


def _coverage_rubric(topic: str, sources: list[SourceChunk]) -> list[str]:
    """Concepts the user should mention to score 'thorough teach-back'.

    Built from the source text — extract distinct medical terms / dose
    patterns / mechanisms — plus a few generic anchors.
    """
    import re
    blob = " ".join(s.text or "" for s in sources[:5]).lower()
    rubric: list[str] = []
    # Mechanism / classification anchors
    for term in ("mechanism", "indication", "contraindication", "dose", "onset", "duration"):
        if term in blob:
            rubric.append(f"the {term}")
    # Specific high-yield extracts
    for pat, label in [
        (r"\b\d+(?:\.\d+)?\s*(?:mg|mcg|ml|g|mEq|cmH2O|mmHg|%)\b", "specific dose or value"),
        (r"\bcontraindicat\w*", "contraindications"),
        (r"\b(adverse|side)\s*effect", "adverse effects"),
        (r"\b(reversal|antidote)", "reversal/antidote"),
        (r"\bpediatric|child|infant", "pediatric considerations"),
        (r"\brenal|hepatic", "organ-specific dosing"),
    ]:
        if re.search(pat, blob, re.I) and label not in rubric:
            rubric.append(label)
    if "mechanism" not in rubric:
        rubric.insert(0, "underlying mechanism / physiology")
    if not rubric:
        rubric = ["mechanism", "indication", "contraindication", "dose"]
    return rubric[:6]


def start_teaching_session(topic: str, mode_hint: str | None = None) -> dict[str, Any]:
    """Return scaffolding for the GPT to play a confused MS3 about `topic`."""
    if not topic or not topic.strip():
        return {
            "topic": topic or "",
            "probe_seeds": [],
            "sources": [],
            "coverage_rubric": [],
            "instructions_for_gpt": "Topic is empty. Ask the user what topic they want to teach.",
        }

    mode = mode_hint or "intern_teach"
    sources, _ = hybrid_search(topic, mode=mode, max_results=5, use_cross_encoder=False)
    seeds = _seeds_for_topic(topic)
    rubric = _coverage_rubric(topic, sources)

    instructions = (
        f"PROTÉGÉ MODE — The user is going to TEACH YOU about {topic}. "
        f"You play a curious but confused MS3. Pick 1-2 probe questions per turn from the seeds, "
        f"or generate your own grounded in the source chunks. Don't volunteer answers — let the user explain. "
        f"After 4-6 turns, say 'Time to wrap up' and give a SHORT feedback summary: which rubric items they "
        f"covered well and which gaps they should fill. Then offer to drill the gaps as cloze questions."
    )

    return {
        "topic": topic,
        "probe_seeds": seeds,
        "sources": sources,
        "coverage_rubric": rubric,
        "instructions_for_gpt": instructions,
    }
