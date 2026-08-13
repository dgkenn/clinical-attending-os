from __future__ import annotations

import json
import re

from .config import settings
from .modes import retrieval_mode_for
from .retrieval import hybrid_search, retrieval_confidence
from .schemas import SourceChunk, TutorResponse
from .student_model import generate_session_plan as _generate_session_plan
from .student_model import log_attempt, select_next_question, training_phase_for_mode


CONCEPT_GRADING_RULES = [
    {
        "match": ["last", "local anesthetic"],
        "concepts": [
            ["lipid", "intralipid", "emulsion"],
            ["stop", "discontinue"],
            ["airway", "oxygen", "ventilat", "abc"],
            ["seizure", "benzodiazepine", "midazolam"],
            ["bupivacaine", "cardiotoxic", "arrhythmia"],
        ],
        "critical": [["lipid", "intralipid", "emulsion"]],
        "mistake_type": "crisis_algorithm",
    },
    {
        "match": ["malignant hyperthermia", " mh "],
        "concepts": [
            ["dantrolene"],
            ["volatile", "succinylcholine"],
            ["stop", "discontinue", "remove"],
            ["oxygen", "hyperventilat", "100"],
            ["cool", "ice", "cold", "temperature"],
            ["hyperkalemia", "acidosis", "abg"],
        ],
        "critical": [
            ["dantrolene"],
            ["volatile", "succinylcholine"],
            ["stop", "discontinue", "remove"],
            ["cool", "ice", "cold"],
        ],
        "mistake_type": "crisis_algorithm",
    },
    {
        "match": ["shunt"],
        "concepts": [
            ["perfusion", "perfused"],
            ["ventilation", "ventilated"],
            ["oxygen", "fio2"],
            ["not correct", "poorly", "refractory", "incompletely"],
            ["v/q", "low vq", "venous admixture"],
        ],
        "critical": [["oxygen", "fio2"], ["not correct", "poorly", "refractory", "incompletely"]],
        "mistake_type": "mechanism",
    },
    {
        "match": ["succinylcholine", "sux"],
        "concepts": [
            ["burn"],
            ["denervation", "spinal cord", "stroke", "immobility", "neuromuscular"],
            ["hyperkalemia", "potassium"],
            ["malignant hyperthermia", "mh"],
            ["pseudocholinesterase", "prolonged"],
        ],
        "critical": [["hyperkalemia", "potassium"], ["burn", "denervation", "spinal cord", "stroke", "immobility", "neuromuscular", "malignant hyperthermia", "mh"]],
        "mistake_type": "recall",
    },
    {
        "match": ["high spinal", "total spinal"],
        "concepts": [
            ["hypotension", "bradycardia"],
            ["airway", "ventilation", "intubation"],
            ["vasopressor", "ephedrine", "phenylephrine", "epinephrine"],
            ["fluids"],
        ],
        "critical": [["airway", "ventilation", "intubation"], ["hypotension", "bradycardia", "vasopressor", "ephedrine", "phenylephrine", "epinephrine"]],
        "mistake_type": "crisis_algorithm",
    },
]


def classify_query(query: str, mode: str) -> str:
    q = query.lower()
    if mode not in {"teach", "default", "mixed"}:
        return mode
    oral_terms = ["oral boards", "examiner", "stem"]
    crisis_substrings = [
        "crisis",
        "malignant hyperthermia",
        "local anesthetic systemic toxicity",
        "local anesthetic toxicity",
        "anaphylaxis",
        "cannot intubate",
        "cannot oxygenate",
        "cico",
        "high spinal",
        "bronchospasm",
        "laryngospasm",
        "hypotension after induction",
        "hypoxemia after induction",
        "oxygen failure",
    ]
    crisis_word = bool(re.search(r"\b(LAST|MH)\b", query)) or bool(re.search(r"\bcrisis\b", q))
    drug_terms = [
        "propofol",
        "ketamine",
        "etomidate",
        "rocuronium",
        "succinylcholine",
        "sux",
        "sugammadex",
        "neostigmine",
        "lidocaine",
        "local anesthetic max",
        "bupivacaine",
        "fentanyl",
        "remifentanil",
        "opioid",
        "mac ",
        "volatile",
    ]
    anesthesia_terms = [
        "anesthesia",
        "anesthesiology",
        "anesthetic",
        "basic exam",
        "basics",
        "ca-1",
        "ca1",
        "operating room",
        "induction",
        "emergence",
        "pacu",
        "airway",
        "difficult airway",
        "rsi",
        "neuraxial",
        "spinal",
        "epidural",
        "test dose",
        "obstetric",
        "pediatric inhalational",
        "geriatric anesthetic",
        "one lung",
        "standard monitors",
        "arterial line",
        "capnography",
        "train of four",
        "neuromuscular",
        "ponv",
        "delayed emergence",
        "lap chole",
        "postoperative risk",
        "aortic stenosis",
        "tamponade",
        "intracranial pressure",
        "massive transfusion",
        "extubation",
    ]
    physiology_terms = [
        "physiology",
        "mechanism",
        "shunt",
        "v/q",
        "one lung ventilation",
        "context sensitive",
        "respiratory depression",
        "adrenal suppression",
        "metabolic acidosis compensation",
    ]
    if any(w in q for w in oral_terms):
        return "oral_boards"
    if any(w in q for w in ["or case", "tomorrow", "preop", "lap chole", "prep"]):
        return "OR_prep"
    if "aspiration" in q and any(w in q for w in ["management", "treatment", "during", "after", "induction"]):
        return "crisis"
    if crisis_word or any(w in q for w in crisis_substrings):
        return "crisis"
    if any(w in q for w in physiology_terms) and "drug review" not in q:
        return "physiology"
    if any(w in q for w in drug_terms):
        return "drug"
    if any(w in q for w in ["cross-cover", "cross cover", "night float", "called about", "page for"]):
        return "cross_cover"
    if re.search(r"\bicu\b", q) or any(w in q for w in ["ventilator", "pressor", "vasopressor", "ards"]):
        return "ICU_teach"
    if any(w in q for w in ["admission", "admit", "rounds", "discharge"]):
        return "intern_teach"
    if any(w in q for w in anesthesia_terms) or re.search(r"\bor\b", q):
        return "anesthesia_boards"
    return "intern_teach"


def is_basics_exam_query(query: str) -> bool:
    q = query.lower()
    return any(term in q for term in ["basic exam", "basics exam", "basic board", "basics board", "ca-1", "ca1", "new resident", "starting out", "residency"])


def is_learning_plan_query(query: str) -> bool:
    q = query.lower()
    plan_terms = ["learning plan", "study plan", "build out", "starting out", "just starting", "new resident", "residency"]
    teach_terms = ["teach me", "quiz me", "start studying", "first topic", "learn"]
    return any(term in q for term in plan_terms) and any(term in q for term in teach_terms)


def citations(sources: list[SourceChunk]) -> str:
    if not sources:
        return "Sources: none retrieved."
    seen = set()
    items = []
    for s in sources:
        key = (s.book, s.page)
        if key not in seen:
            seen.add(key)
            items.append(f"{s.book or s.filename} p. {s.page}")
    return "Sources: " + "; ".join(items)


def local_answer(query: str, mode: str, sources: list[SourceChunk], insufficient: bool) -> str:
    prefix = "The available source material is limited for this question.\n\n" if insufficient else ""
    evidence = "\n".join(f"- {s.book} p. {s.page}: {s.text[:350]}" for s in sources[:4])
    if mode == "pimp":
        return prefix + f"What is the key anesthetic issue in: {query}?"
    if mode == "oral_boards":
        return prefix + f"Case stem: {query}\n\nStart with your preop assessment and anesthetic plan. I will escalate after your answer."
    if mode == "drug":
        headings = "Class\nMechanism\nDose range if source-supported\nOnset/duration\nMetabolism/elimination\nHemodynamic effects\nRespiratory effects\nContraindications\nInteractions\nBoard traps\nClinical pearl\nFollow-up question\n"
    elif mode == "crisis":
        headings = "Recognize\nImmediate actions\nDifferential\nDefinitive treatment\nDoses if source-supported\nWhat not to miss\nBoard trap\nFollow-up question\n"
    elif mode in {"intern_teach", "cross_cover", "admission_plan", "wards_rounding", "rapid_response"}:
        headings = "Dangerous possibilities\nWhat to ask\nWhat to examine\nLabs/imaging\nAssessment\nPlan\nWhen to call senior/ICU/consult\nRounds/signout phrasing\nFollow-up question\n"
    elif mode == "ICU_teach":
        headings = "One-line answer\nPhysiology\nImmediate bedside priorities\nVent/hemodynamic implications\nOrders/interventions\nEscalation threshold\nFollow-up question\n"
    elif mode == "anesthesia_transition":
        headings = "Medicine/ICU frame\nWhy it matters in anesthesia\nInduction/airway/monitoring implications\nBoard trap\nFollow-up question\n"
    elif mode == "OR_prep":
        headings = "Case-specific concerns\nPreop evaluation\nMedication considerations\nInduction plan\nAirway plan\nMonitoring\nMaintenance\nFluids/blood\nEmergence\nPACU issues\nAttending pimp questions\n"
    else:
        headings = "One-line answer\nHigh-yield framework\nMechanism\nOR/clinical relevance\nBoard trap\nWhat to say on oral boards\nFollow-up question\n"
    return (
        prefix
        + f"{headings}\n"
        + "Use only these retrieved excerpts for final synthesis. Do not add citations that are not listed here.\n\n"
        + evidence
        + "\n\n"
        + citations(sources)
    )


def llm_answer(query: str, mode: str, sources: list[SourceChunk], insufficient: bool) -> str:
    if not settings.enable_openai_generation or not settings.openai_api_key:
        return local_answer(query, mode, sources, insufficient)
    settings.assert_backend_generation_allowed("OpenAI")
    try:
        from openai import OpenAI
    except Exception:
        return local_answer(query, mode, sources, insufficient)
    context = "\n\n".join(
        f"[{i}] {s.book} page {s.page} section {s.section}\n{s.text}" for i, s in enumerate(sources, start=1)
    )
    prompt = f"""Answer as ANESTHESIA ATTENDING. Mode: {mode}. Use only the retrieved sources for citations. Do not invent citations. If context is weak, start with the required limited-source sentence.

Question: {query}

Retrieved context:
{context}
"""
    client = OpenAI(api_key=settings.openai_api_key)
    resp = client.chat.completions.create(model=settings.openai_chat_model, messages=[{"role": "user", "content": prompt}], temperature=0.2)
    text = resp.choices[0].message.content or ""
    if insufficient and not text.startswith("The available source material is limited"):
        text = "The available source material is limited for this question.\n\n" + text
    return text


def answer_query(query: str, mode: str = "teach", session_id: str | None = None) -> TutorResponse:
    if is_learning_plan_query(query):
        session_mode = "anesthesia_boards" if "anesth" in query.lower() else "default"
        plan = start_session(duration_minutes=20, mode=session_mode, focus_topic=None)
        ordered_targets = [item for item in plan["plan"] if item.get("fact")]
        ordered_targets.extend(item for item in plan["plan"] if not item.get("fact"))
        first_target = ordered_targets[0] if ordered_targets else {"topic": "Hyperkalemia"}
        source_query = first_target.get("fact") or first_target.get("subtopic") or first_target["topic"]
        retrieval_mode = "anesthesia_transition" if plan["training_phase"] == "anesthesia_transition" else "intern_teach"
        source_filter = None
        if plan["training_phase"] == "anesthesia_boards":
            retrieval_mode = "basics_exam"
            source_filter = "Stanford CA-1"
        sources, insufficient = hybrid_search(source_query, mode=retrieval_mode, source_filter=source_filter, max_results=5)
        plan_lines = "\n".join(
            f"{idx}. {item['topic']}{' - ' + item.get('subtopic', '') if item.get('subtopic') else ''}"
            for idx, item in enumerate(ordered_targets[:5], start=1)
        )
        first_topic = first_target["topic"]
        first_subtopic = first_target.get("subtopic", "")
        answer = (
            f"Session started: {plan['session_id']}\n\n"
            f"Learning plan: default phase is {plan['training_phase']}. We will work through the source material at granular fact level, using active recall before teaching.\n\n"
            + ("Stanford CA-1 is the spine for explicit anesthesia/BASICS work; intern notes and Marino remain the default for intern-year medicine.\n\n" if plan["training_phase"].startswith("anesthesia") else "")
            + f"First targets:\n{plan_lines}\n\n"
            + f"First topic: {first_topic}\n"
            + f"{first_subtopic}\n\n"
            + "Before I teach it, answer this in your own words: what is the dangerous issue, and what would you do first?"
        )
        return TutorResponse(
            answer=answer,
            follow_up="Answer the diagnostic question, and I will log what you know before teaching the missing pieces.",
            sources=sources,
            mode="session_start",
            retrieval_confidence=retrieval_confidence(sources),
            insufficient_context=insufficient,
            session_id=plan["session_id"],
        )
    actual_mode = classify_query(query, mode)
    retrieval_mode = "basics_exam" if is_basics_exam_query(query) else retrieval_mode_for(actual_mode)
    sources, insufficient = hybrid_search(query, mode=retrieval_mode, max_results=8)
    answer = llm_answer(query, actual_mode, sources, insufficient)
    follow = "Answer the follow-up question, and I will grade it." if actual_mode in {"pimp", "oral_boards"} else "What mechanism or board trap should I quiz you on next?"
    return TutorResponse(answer=answer, follow_up=follow, sources=sources, mode=actual_mode, retrieval_confidence=retrieval_confidence(sources), insufficient_context=insufficient)


def start_session(duration_minutes: int = 20, mode: str = "default", focus_topic: str | None = None, training_phase: str | None = None) -> dict:
    plan = _generate_session_plan(duration_minutes, mode, focus_topic, training_phase)
    first_target = plan["plan"][0] if plan["plan"] else {}
    if first_target.get("fact"):
        plan["first_question"] = f"Before I teach it, tell me the key point from {first_target['subtopic']}."
    else:
        first_topic = first_target.get("topic") or focus_topic
        plan["first_question"] = select_next_question(first_topic)
    source_query = first_target.get("fact") or first_target.get("subtopic") or first_target.get("topic") or focus_topic or "intern medicine"
    retrieval_mode = retrieval_mode_for(mode if mode != "default" else "intern_teach")
    if plan.get("training_phase") == "ICU":
        retrieval_mode = "ICU_teach"
    elif plan.get("training_phase") == "anesthesia_boards":
        retrieval_mode = "anesthesia_boards"
    elif plan.get("training_phase") == "anesthesia_transition":
        retrieval_mode = "anesthesia_transition"
    source_filter = "Stanford CA-1" if plan.get("training_phase") == "anesthesia_boards" else None
    snippets, insufficient = hybrid_search(source_query, mode=retrieval_mode, source_filter=source_filter, max_results=5)
    plan["source_snippets"] = snippets
    plan["retrieval_confidence"] = retrieval_confidence(snippets)
    plan["insufficient_context"] = insufficient
    return plan


def _contains_any(text: str, variants: list[str]) -> bool:
    return any(variant in text for variant in variants)


def grade_user_answer(question: str, user_answer: str, ideal_answer: str, topic: str, subtopic: str = "") -> tuple[str, str]:
    combined_prompt = f" {question} {topic} {subtopic} ".lower()
    answer = user_answer.lower()
    for rule in CONCEPT_GRADING_RULES:
        if not any(key in combined_prompt for key in rule["match"]):
            continue
        concept_hits = sum(1 for concept in rule["concepts"] if _contains_any(answer, concept))
        critical_hits = sum(1 for concept in rule["critical"] if _contains_any(answer, concept))
        if critical_hits == len(rule["critical"]) and concept_hits >= max(2, len(rule["concepts"]) - 2):
            return "correct", "other"
        if critical_hits >= 1 or concept_hits >= 2:
            if rule["mistake_type"] == "mechanism" and concept_hits < 2:
                return "incorrect", rule["mistake_type"]
            return "partial", rule["mistake_type"]
        return "incorrect", rule["mistake_type"]

    answer_terms = set(re.findall(r"[a-zA-Z]{4,}", answer))
    ideal_terms = set(re.findall(r"[a-zA-Z]{4,}", ideal_answer.lower())) or {"anesthesia"}
    overlap = len(answer_terms & ideal_terms) / max(1, len(ideal_terms))
    if overlap > 0.25 and len(answer_terms) >= 5:
        return "correct", "other"
    if overlap > 0.08 or len(answer_terms) >= 8:
        return "partial", "incomplete_answer"
    return "incorrect", "incomplete_answer"


def evaluate_user_answer(question: str, user_answer: str, ideal_answer: str, topic: str, subtopic: str = "", session_id: str = "") -> dict:
    result, mistake = grade_user_answer(question, user_answer, ideal_answer, topic, subtopic)
    log_attempt(session_id, topic, subtopic, question, user_answer, ideal_answer, result, mistake)
    return {
        "evaluation": result,
        "feedback": "Good enough to advance." if result == "correct" else "Incomplete. Tighten mechanism, priorities, and board phrasing.",
        "ideal_answer": ideal_answer,
        "mistake_type": mistake,
        "next_question": select_next_question(topic),
    }


def record_evaluated_answer(
    session_id: str,
    question: str,
    user_answer: str,
    topic: str,
    subtopic: str = "",
    result: str = "partial",
    mistake_type: str = "other",
    ideal_answer: str = "",
    difficulty: str = "medium",
    hints_used: int = 0,
    confidence_reported: float | None = None,
    retrieval_sources: str = "",
    source_citations: str = "",
    notes: str = "",
    library: str = "",
    training_phase: str = "",
    phase: str = "warm_up_retrieval",
) -> dict:
    log_attempt(
        session_id=session_id,
        topic=topic,
        subtopic=subtopic,
        question=question,
        user_answer=user_answer,
        ideal_answer=ideal_answer,
        result=result,
        mistake_type=mistake_type,
        difficulty=difficulty,
        hints_used=hints_used,
        confidence_reported=confidence_reported,
        retrieval_sources=retrieval_sources,
        source_citations=source_citations,
        notes=notes,
        library=library,
        training_phase=training_phase,
    )
    from .student_model import get_topic_summary

    summary = get_topic_summary(topic)
    feedback = {
        "correct": "Logged as correct. I will space this topic out but keep it in maintenance.",
        "partial": "Logged as partial. I will keep this topic active and retest the weak point soon.",
        "incorrect": "Logged as incorrect. I will prioritize this topic for review.",
    }.get(result, "Logged.")
    snippet_query = f"{topic} {subtopic}".strip() or question
    snippets, _ = hybrid_search(snippet_query, mode="broad_explain", max_results=3, use_cross_encoder=False)

    # Look up the cached lesson for this (unit_id, phase) pair so the GPT
    # receives mini_teach + teachback_prompt + citation HERE — these were
    # stripped from /next_lesson to force per-turn submit calls.
    mini_teach = ""
    teachback_prompt = ""
    citation = ""
    # Forward-testing effect: pretest phase intentionally withholds the answer
    # so the user feels productive failure before content is delivered. Skip
    # the cache lookup entirely.
    if phase == "pretest":
        # Override the mistake_type tag so weak_patterns doesn't count it as
        # a real failure.
        if result == "incorrect":
            mistake_type = "pretest_unstudied"
    elif subtopic:
        try:
            from .lesson_cache import get_cached as _get_cached_lesson
            cached = _get_cached_lesson(subtopic, phase)
            if cached:
                mini_teach = cached.get("mini_teach", "") or ""
                teachback_prompt = cached.get("teachback_prompt", "") or ""
                citation = cached.get("citation", "") or ""
        except Exception:
            pass
    # Fallback for due-topic stubs (subtopic starts with 'due:') or any cache
    # miss: shape teach material live from the retrieved snippets so the GPT
    # always gets something to narrate. Pretests intentionally stay empty.
    if phase != "pretest" and not mini_teach and snippets:
        try:
            from .curriculum import CurriculumUnit
            from .voice_shaper import shape_lesson as _shape
            stub_unit = CurriculumUnit(
                unit_id=subtopic or topic,
                book=snippets[0].book or "",
                library=snippets[0].library or "",
                chapter_number=None,
                chapter_title="",
                section=topic,
                page_start=snippets[0].page or 0,
                page_end=snippets[0].page or 0,
                topic_tags=[topic] if topic else [],
                fact_chunk_ids=[],
                fact_count=0,
                high_yield_score=0.0,
                crossover_priority="normal",
            )
            shaped = _shape(stub_unit, snippets, phase=phase or "warm_up_retrieval")
            mini_teach = shaped.mini_teach
            teachback_prompt = shaped.teachback_prompt
            citation = shaped.citation
        except Exception:
            pass

    return {
        "evaluation": result,
        "feedback": feedback,
        "ideal_answer": ideal_answer,
        "ideal_answer_key_points": [p.strip(" -") for p in re.split(r"[.;\n]", ideal_answer) if p.strip()][:6],
        "mistake_type": mistake_type,
        "updated_mastery": summary.get("mastery_score"),
        "next_review_date": summary.get("next_review_date"),
        "source_snippets": snippets,
        "mini_teach": mini_teach,
        "teachback_prompt": teachback_prompt,
        "citation": citation,
        "next_question": select_next_question(topic),
    }


def generate_next_question(session_id: str) -> str:
    return select_next_question()
