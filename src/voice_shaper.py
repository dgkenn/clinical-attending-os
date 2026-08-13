"""Shape retrieved evidence + a curriculum unit into a voice-mode lesson.

ChatGPT voice mode wants short, conversational turns (≤ ~2 sentences each).
The Custom GPT narrates the fields one at a time with pauses for the user
to answer; it must never read JSON keys or long citations aloud.
"""

from __future__ import annotations

import re
from typing import Any

from functools import lru_cache

from .cloze import ClozeCard, deck_by_unit_topic_tag
from .curriculum import CurriculumUnit
from .pedagogy import active_recall_instruction
from .schemas import SourceChunk, VoiceLesson


MAX_CHARS = 240
MAX_SENTENCES = 2


def _trim(text: str, max_chars: int = MAX_CHARS, max_sentences: int = MAX_SENTENCES) -> str:
    if not text:
        return ""
    text = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r"(?<=[.!?])\s+", text)
    parts = [p for p in parts if p]
    truncated = " ".join(parts[:max_sentences]) if parts else text
    if len(truncated) > max_chars:
        truncated = truncated[: max_chars - 1].rstrip() + "…"
    return truncated


def _first_fact(sources: list[SourceChunk]) -> str:
    for s in sources:
        if s.text:
            return s.text
    return ""


def _topic_label(unit: CurriculumUnit) -> str:
    if unit.topic_tags:
        return unit.topic_tags[0]
    return unit.section or unit.chapter_title or unit.book


def _retrieval_mode_for_band(unit: CurriculumUnit) -> str:
    from .curriculum import _band_for_unit  # local import to avoid cycle on module load

    band = _band_for_unit(unit)
    if band == "icu":
        return "ICU_teach"
    if band == "anesthesia":
        return "anesthesia_boards"
    if band == "deep_medicine":
        return "intern_teach"
    return "intern_teach"


_TOPIC_SCHEMAS_PATH = "data/topic_schemas.json"
_TOPIC_SCHEMAS_CACHE: dict[str, str] | None = None


def _topic_schemas() -> dict[str, str]:
    """Load topic→schema-mnemonic map. Falls back to a built-in seed if the
    JSON file is missing or malformed."""
    global _TOPIC_SCHEMAS_CACHE
    if _TOPIC_SCHEMAS_CACHE is not None:
        return _TOPIC_SCHEMAS_CACHE
    import json
    from pathlib import Path
    seed = {
        # The keys here are matched substring-style against the topic name (case-insensitive)
        "hypotension": "preload → contractility → afterload → rate → rhythm",
        "hypertensive": "rate-pressure → end-organ check → workup",
        "hypoxemia": "FiO2 → V/Q → shunt → diffusion → hypoventilation",
        "shock": "cardiogenic / hypovolemic / distributive / obstructive",
        "sepsis": "lactate → cultures → broad antibiotics → fluids → pressors",
        "altered mental status": "AEIOU TIPS",
        "ams": "AEIOU TIPS",
        "hyperkalemia": "stabilize (calcium) → shift (insulin/albuterol) → eliminate (kayexalate/dialysis)",
        "hyponatremia": "volume status → osm → urine na → tonicity-based correction",
        "afib": "rate vs rhythm → anticoagulation (CHA2DS2-VASc)",
        "ards": "low Vt 6 mL/kg PBW → plateau <30 → PEEP → proning if P/F<150",
        "aki": "prerenal / intrinsic / postrenal — FENa + UA + ultrasound",
        "dka": "fluids → insulin → potassium → close gap",
        "gi bleed": "ABCs → IV access → type+cross → PPI → endoscopy",
        "anaphylaxis": "epi IM → airway → IVF → H1/H2 + steroid",
        "code blue": "compressions → defib → epi → ABCs → reversible Hs/Ts",
        "acs": "MONA-B + dual antiplatelet + heparin + cath",
        "pe": "anticoag (heparin) → consider thrombolysis if massive",
    }
    path = Path(__file__).resolve().parent.parent / _TOPIC_SCHEMAS_PATH
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                seed.update({str(k).lower(): str(v) for k, v in data.items()})
        except Exception:
            pass
    _TOPIC_SCHEMAS_CACHE = seed
    return seed


def _schema_for(topic: str) -> str:
    """Return the schema mnemonic for this topic, or empty if no match."""
    if not topic:
        return ""
    low = topic.lower()
    schemas = _topic_schemas()
    if low in schemas:
        return schemas[low]
    for key, schema in schemas.items():
        if key in low or low in key:
            return schema
    return ""


def _relevance_hook(unit: CurriculumUnit, topic: str) -> str:
    """One-line 'why this matters today' framing (Roediger relevance bump).

    When the topic matches a schema mnemonic, the mnemonic is prepended so the
    user gets the framework before each repetition. Schema-based instruction
    is what attendings actually do; this drills it implicitly."""
    from .curriculum import _band_for_unit

    band = _band_for_unit(unit)
    schema = _schema_for(topic)
    schema_prefix = f"Walk: {schema}. " if schema else ""

    if unit.crossover_priority == "high":
        body = f"You'll see {topic} on every ICU bedside and most cross-cover pages."
    elif band == "icu":
        body = f"This will come up at every ICU bedside discussion of {topic}."
    elif band == "anesthesia":
        body = f"Common BASICS-exam stem on {topic}."
    elif band == "deep_medicine":
        body = f"You'll be expected to know {topic} on rounds and signout."
    else:
        body = f"High-yield for cross-cover and admission questions on {topic}."
    return _trim(schema_prefix + body, 240, 2)


CONFIDENCE_CHECK = "On a 1-5 scale, how sure are you before I check?"


@lru_cache(maxsize=1)
def _cached_cloze_deck() -> dict[str, list[ClozeCard]]:
    return deck_by_unit_topic_tag()


def _cloze_for_topic(
    topic: str,
    seed: int,
    preferred_types: tuple[str, ...] | None = None,
) -> ClozeCard | None:
    """Pick a cloze card for this topic. `seed` rotates across repetitions
    so the same topic never serves the same card twice in a row.

    `preferred_types` filters to cloze types matching difficulty or distributed-
    practice constraints (e.g. ('label', 'condition') for an "easier" target).
    Falls back to all cards if no match.
    """
    deck = _cached_cloze_deck()
    cards = deck.get(topic) or []
    if not cards:
        return None
    pool = cards
    if preferred_types:
        filtered = [c for c in cards if c.mask_type in preferred_types]
        if filtered:
            pool = filtered
    return pool[seed % len(pool)]


_CLOZE_PROMPTS = {
    "dose": "What dose goes here?",
    "drug": "What drug fits this blank?",
    "condition": "What condition fits this blank?",
    "label": "What abbreviation or term fits this blank?",
}


def _cloze_question(card: ClozeCard) -> str:
    prompt = _CLOZE_PROMPTS.get(card.mask_type, "Fill in the blank.")
    return _trim(f"{prompt} {card.masked_text}")


_DIFFICULTY_PREFERRED = {
    "easier": ("label", "condition"),
    "default": None,
    "harder": ("drug", "dose"),
}


_CRITIQUE_TRAPS_PATH = "data/critique_traps.json"
_CRITIQUE_TRAPS_CACHE: dict[str, list[dict]] | None = None


def _critique_traps() -> dict[str, list[dict]]:
    """Load topic→[critique trap dicts] from data/critique_traps.json.

    Each entry is a dict with keys: wrong, why_wrong, right.
    """
    global _CRITIQUE_TRAPS_CACHE
    if _CRITIQUE_TRAPS_CACHE is not None:
        return _CRITIQUE_TRAPS_CACHE
    import json
    from pathlib import Path
    path = Path(__file__).resolve().parent.parent / _CRITIQUE_TRAPS_PATH
    if not path.exists():
        _CRITIQUE_TRAPS_CACHE = {}
        return _CRITIQUE_TRAPS_CACHE
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            _CRITIQUE_TRAPS_CACHE = {str(k).lower(): list(v) for k, v in data.items() if isinstance(v, list)}
        else:
            _CRITIQUE_TRAPS_CACHE = {}
    except Exception:
        _CRITIQUE_TRAPS_CACHE = {}
    return _CRITIQUE_TRAPS_CACHE


def _critique_trap_for(topic: str) -> dict | None:
    if not topic:
        return None
    low = topic.lower()
    traps = _critique_traps()
    if low in traps and traps[low]:
        return traps[low][0]
    for key, items in traps.items():
        if (key in low or low in key) and items:
            return items[0]
    return None


def shape_lesson(
    unit: CurriculumUnit,
    sources: list[SourceChunk],
    phase: str,
    fact_text: str | None = None,
    cloze_seed: int = 0,
    topic_times_seen: int = 0,
    difficulty_target: str = "default",
) -> VoiceLesson:
    """Build a VoiceLesson for the given (unit, phase).

    `topic_times_seen` rotates the cloze card across repetitions so the user
    never gets the same question twice in a row.

    `difficulty_target` ∈ {"easier", "default", "harder"} biases cloze type
    selection (Bjork's desirable-difficulty zone, ~70-80% correct).

    `phase="pretest"` asks the question but instructs callers to withhold
    teach material — the forward-testing effect comes from productive failure.

    `phase="critique"` injects a plausible-wrong answer for the user to find;
    backed by data/critique_traps.json.
    """
    topic = _topic_label(unit)
    fact = fact_text or _first_fact(sources)
    citation = ""
    if sources:
        s = sources[0]
        citation = f"{s.book or s.source_name or unit.book} p. {s.page if s.page is not None else unit.page_start}"

    preferred_types = _DIFFICULTY_PREFERRED.get(difficulty_target)

    cloze: ClozeCard | None = None
    if phase in ("warm_up_retrieval", "weak_topic_drilling", "pretest", "critique"):
        # Per-repetition rotation: combine cloze_seed (phase offset) with
        # topic_times_seen (repetition counter) so the card changes every time
        # the topic comes back in the queue.
        phase_offset = {"warm_up_retrieval": 0, "weak_topic_drilling": 1,
                        "pretest": 3, "critique": 5}.get(phase, 0)
        seed = cloze_seed * 7 + topic_times_seen * 2 + phase_offset
        cloze = _cloze_for_topic(topic, seed, preferred_types=preferred_types)

    if phase == "pretest":
        # Forward-testing effect: ask the question without revealing the
        # answer. The voice loop will withhold mini_teach in submitAnswer
        # response on this phase. Even getting it wrong primes attention.
        if cloze:
            question = _cloze_question(cloze)
        else:
            question = _trim(f"Pretest on {topic} — your best guess?")
        teach = ""  # withheld by design
        teachback = _trim(f"Don't worry if unsure — we'll teach {topic} after.")
    elif phase == "critique":
        # Errorful learning: present a plausible-wrong answer; user identifies
        # the error. The trap content comes from data/critique_traps.json
        # (loaded by callers); fall back to a generic critique prompt.
        trap = _critique_trap_for(topic)
        if trap:
            question = _trim(f"Resident says: \"{trap['wrong']}\". What's wrong with that?")
        else:
            question = _trim(f"You hear a plausible-but-wrong claim about {topic}. Walk me through the trap.")
        teach = _trim(fact)
        teachback = _trim(f"Why is the wrong answer wrong, mechanically?")
    elif phase == "warm_up_retrieval":
        if cloze:
            question = _cloze_question(cloze)
            teach = _trim(fact)
            teachback = _trim(f"Why is {cloze.answer} the right answer here? One-sentence mechanism.")
        else:
            question = _trim(f"Quick recall on {topic}: what is the first thing you check or do?")
            teach = _trim(fact)
            teachback = _trim(f"Why does that first step matter for {topic}? Mechanism, one sentence.")
    elif phase == "weak_topic_drilling":
        if cloze:
            question = _cloze_question(cloze)
            teach = _trim(fact)
            teachback = _trim(f"Walk me through why {cloze.answer} is correct — physiology, talk it out.")
        else:
            question = _trim(active_recall_instruction(_retrieval_mode_for_band(unit)) + f" Topic: {topic}.")
            teach = _trim(fact)
            teachback = _trim(f"Walk me through the mechanism that explains {topic} — talk it out.")
    elif phase == "new_material":
        question = _trim(f"Before I teach {topic}, what is the dangerous issue and what would you do first?")
        teach = _trim(fact)
        teachback = _trim(f"Now explain why the management of {topic} works — what's the underlying physiology?")
    elif phase == "clinical_case_application":
        question = _trim(f"Case: a patient with {topic}. What is your first action and what would you ask next?")
        teach = _trim(fact)
        teachback = _trim(f"On rounds, justify why this plan works for {topic} — physiology in one sentence.")
    elif phase == "teach_back":
        question = _trim(f"Without looking, what are the two highest-yield points about {topic}?")
        teach = _trim(fact)
        teachback = _trim(f"Explain to an MS3 why {topic} is dangerous and what the mechanism of the fix is.")
    else:
        question = _trim(f"What do you know about {topic}?")
        teach = _trim(fact)
        teachback = _trim(f"Why does {topic} matter? One-sentence mechanism.")

    if phase == "pretest":
        expected = ""  # withheld in pretest by design
    elif cloze:
        expected = cloze.answer
    else:
        expected = _trim(fact, max_chars=160, max_sentences=1)
    return VoiceLesson(
        unit_id=unit.unit_id,
        phase=phase,
        topic=topic,
        question=question,
        expected_answer_short=expected,
        mini_teach=teach,
        teachback_prompt=teachback,
        citation=_trim(citation, max_chars=120, max_sentences=1),
        book=unit.book,
        page=unit.page_start,
        relevance_hook=_relevance_hook(unit, topic),
        confidence_check=CONFIDENCE_CHECK,
    )


def shape_no_lesson_available() -> VoiceLesson:
    return VoiceLesson(
        unit_id="none",
        phase="teach_back",
        topic="",
        question="No more units in the queue right now. Want me to mix in spaced reviews instead?",
        expected_answer_short="",
        mini_teach="",
        teachback_prompt="",
        citation="",
        book="",
        page=0,
        relevance_hook="",
        confidence_check="",
    )
