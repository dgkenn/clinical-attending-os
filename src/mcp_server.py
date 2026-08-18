from __future__ import annotations

import functools
import hmac

from .retrieval import hybrid_search, retrieval_confidence
from .student_model import (
    get_due_reviews as _due,
    get_student_dashboard as _dash,
    mark_topic_mastered,
    mark_topic_weak,
    set_default_training_phase,
    initialize_database,
    record_knowledge_gap,
    record_knowledge_point as _record_kp,
    get_knowledge_points as _get_kp,
    get_due_knowledge_points as _get_due_kp,
    get_knowledge_gaps as _get_knowledge_gaps,
    resolve_knowledge_gaps as _resolve_knowledge_gaps,
    upsert_illness_script as _upsert_script,
    get_illness_script as _get_script,
    add_confusable_pair as _add_confusable,
    get_confusable_pairs as _get_confusable,
)
from .tutor_engine import answer_query, record_evaluated_answer, start_session
from .mcp_endpoints import (
    get_calibration_report,
    retrieval as mcp_retrieval,
    get_session_state,
    get_next_topic,
    submit_answer,
    get_mastery_gates,
    get_mastery_map,
    get_progress,
    set_medicine_weight_tool,
    get_kp_to_study,
)


def search_clinical_sources(query: str, mode: str = "intern_teach", library_filter: str | None = None, max_results: int = 8) -> dict:
    """Retrieve source passages from the clinical library (hybrid vector+BM25).

    Use this whenever you need grounded clinical content — every fact, dose, and
    citation you give the user must come from here, never from your training.
    Returns passages plus `insufficient_context`; if that is true, say so rather
    than filling the gap yourself.
    """
    results, insufficient = hybrid_search(query, mode=mode, library_filter=library_filter, max_results=max_results)
    return {
        "results": [r.model_dump() for r in results],
        "retrieval_confidence": retrieval_confidence(results),
        "insufficient_context": insufficient,
    }


def answer_from_clinical_sources(query: str, mode: str = "intern_teach") -> dict:
    """Answer a clinical question with a retrieval-grounded, cited response.

    Higher level than `search_clinical_sources`: it retrieves AND composes the
    answer with citations attached. Prefer this when the user asks a direct
    clinical question; use the search tool when you want raw passages to teach from.
    """
    return answer_query(query, mode).model_dump()


def start_study_session(duration_minutes: int = 20, mode: str = "default", focus_topic: str | None = None, training_phase: str | None = None) -> dict:
    """LEGACY session opener. Prefer `get_session_state` + `get_next_topic`.

    Kept for older clients. New sessions do not need to be explicitly started.
    """
    return start_session(duration_minutes, mode, focus_topic, training_phase)


def submit_study_answer(
    session_id: str,
    question: str,
    user_answer: str,
    topic: str,
    result: str,
    mistake_type: str = "other",
    subtopic: str = "",
    ideal_answer: str = "",
) -> dict:
    """LEGACY answer recorder. Use `submit_answer` instead — it drives FSRS
    scheduling, captures confidence, and accepts inline knowledge points.

    This one does not update the spaced-repetition schedule the same way.
    """
    return record_evaluated_answer(session_id, question, user_answer, topic, subtopic, result, mistake_type, ideal_answer)


def get_due_reviews() -> list[dict]:
    """List TOPICS whose FSRS spaced-repetition review is due now.

    This is the topic-level layer. It is NOT the fact-level queue — for that use
    `get_due_knowledge_points`, which returns the specific facts the user has
    previously missed. A good session covers both.
    """
    return _due()


def get_student_dashboard() -> dict:
    """Overall progress snapshot: mastery by topic, streaks, and coverage.

    Use for "how am I doing?" questions. For choosing what to study next, use
    `get_next_topic` or `get_due_reviews` instead.
    """
    return _dash()


def log_missed_topic(topic: str, subtopic: str = "", gap_note: str = "", mistake_type: str = "other") -> dict:
    """Flag a topic weak AND persist the SPECIFIC missed micro-fact so it can be
    re-targeted next session.

    Pass the granular misconception in `gap_note` (preferred) — e.g.
    "ARDS: low tidal volume 6 mL/kg IBW is the mortality move, not high PEEP".
    For backward compatibility, if `gap_note` is empty the `subtopic` text is used
    as the gap note. The parent topic gets the FSRS weak signal; the gap is stored
    structured/deduped in knowledge_gaps (no junk pseudo-topic rows).
    """
    from .topic_resolver import resolve_topic
    topic, _ = resolve_topic(topic)
    note = (gap_note or subtopic or "").strip()
    mark_topic_weak(topic, "")  # weak signal on the parent topic only
    if note:
        record_knowledge_gap(topic, note, mistake_type)
    return {"ok": True, "topic": topic, "gap_logged": bool(note)}


def submit_knowledge_points(topic: str, points: list) -> dict:
    """Record per-knowledge-point results for a (usually compound) question.

    `points` is a list of objects, one per atomic fact the question tested:
        {"point": "<canonical fact>", "correct": true/false,
         "confidence": 1-5 (optional), "mistake_type": "recall"|... (optional)}

    Each point gets its OWN correctness history, confidence/calibration, and
    INDEPENDENT spaced-repetition schedule — so on a compound question you can be
    confident on some parts and unsure on others, and each part is scheduled on its
    own. Use this alongside the topic-level `submit_answer`.
    """
    from .topic_resolver import resolve_topic
    topic, _topic_resolved = resolve_topic(topic)
    results = []
    skipped = []
    for p in points or []:
        if not isinstance(p, dict):
            skipped.append({"point": repr(p)[:80], "reason": "not an object"})
            continue
        if "correct" not in p and "is_correct" not in p:
            # A missing/misspelled correctness key used to default to False and
            # get recorded as a genuine failure — status weak, streak reset,
            # FSRS lapse — with ok:true returned. Refuse to guess.
            skipped.append({"point": str(p.get("point", ""))[:120],
                            "reason": "missing 'correct' field"})
            continue
        r = _record_kp(
            topic=topic,
            point=str(p.get("point", "")),
            is_correct=bool(p.get("correct", p.get("is_correct", False))),
            confidence=p.get("confidence"),
            mistake_type=str(p.get("mistake_type", "other")),
            triage=bool(p.get("triage", False)),
        )
        if r:
            results.append(r)
        else:
            skipped.append({"point": str(p.get("point", ""))[:120], "reason": "blank topic or point"})
    return {
        "ok": True,
        "recorded": len(results),
        "canonical_topic": topic,
        "topic_was_canonicalized": _topic_resolved,
        "skipped": skipped,
        "points": results,
        "weak_or_learning": [r["point"] for r in results if r["status"] != "mastered"],
    }


def _existing_points() -> list:
    """All knowledge points, for duplicate matching at capture time."""
    try:
        import sqlite3
        from .student_model import conn
        with conn() as db:
            db.row_factory = sqlite3.Row
            return list(db.execute(
                "SELECT id, topic, point, status, times_seen FROM knowledge_points"))
    except Exception:
        return []


def log_user_feedback(message: str, context: str = "") -> dict:
    """Relay something the user said ABOUT THE SYSTEM to the maintainer.

    Call this whenever the user names a problem, annoyance, or wish about the
    tutoring system itself — "it keeps repeating questions", "grading felt
    harsh", "this is too slow", "I wish it would X". Quote them as closely as
    you can in `message`; put what was happening at the time in `context`.

    Why this exists: the user once reported an issue mid-session and it
    vanished — conversational prose never reaches the backend, so the
    maintainer's audit found nothing. The tutor is the only surface the user
    has while studying; anything they say about the system must survive the
    session. This costs one call and the maintainer reads it directly.

    System feedback only. Clinical content goes through the normal tools.
    """
    try:
        from datetime import datetime, timezone
        from pathlib import Path as _P
        from .config import settings
        log = _P(settings.log_dir) / "user_feedback.log"
        log.parent.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).isoformat()[:19]
        line = "\t".join([stamp, (message or "").strip()[:500],
                          (context or "").strip()[:200]])
        with log.open("a", encoding="utf-8") as f:
            f.write(line + "\n")
        return {"ok": True,
                "note": "Relayed to the maintainer. Tell the user it is logged, "
                        "then continue the session."}
    except Exception as exc:
        return {"ok": False, "error": str(exc)[:200]}


def log_tangent(topic: str, question_asked: str = "", facts: list | None = None,
                trigger: str = "") -> dict:
    """Capture a question the USER asked. Their question is a self-identified gap.

    Call this whenever the user asks their own clinical question — mid-session,
    off-plan, or as a rabbit hole. `question_asked` is the important field:
    record what they actually asked, in their words.

    Why the question matters more than the answer given: an unprompted question
    is the highest-quality gap signal the system gets. A wrong answer only tells
    you they missed something you chose to ask. A question they raise themselves
    tells you they noticed the hole, cared enough to chase it, and usually hit it
    on a real patient. Nothing prompted it, so it is not an artifact of the
    curriculum — it is what they actually need.

    `facts` (optional) is what got covered while answering, phrased as canonical
    facts ("Digoxin toxicity is potentiated by hypokalemia").

    Everything here is recorded as EXPOSED-BUT-UNPROVEN — weak, never counted
    correct, scheduled to come back. Exposure is not knowledge: they were told
    it, they did not recall it, and marking discussion correct would inflate
    mastery with material they cannot reproduce.

    This does NOT replace testing. Close the tangent by asking them the very
    question they asked you, back to them, through `submit_answer` — that turns
    a question they could not answer into retrieval practice and a graded
    record. A digoxin rabbit hole once ran a whole session and left no trace at
    all, which is what this exists to prevent.
    """
    from .topic_resolver import resolve_topic
    topic, resolved = resolve_topic(topic)
    recorded, skipped = [], []

    items: list[tuple[str, str]] = []
    q = (question_asked or "").strip()
    if q:
        # Store the gap as a fact-shaped prompt so it is testable later. The
        # user asking "why do HF patients need higher K+" means the answer to
        # that question is the thing to drill.
        items.append((f"[asked] {q}"[:300], "self_identified_gap"))
    for f in facts or []:
        text = (f if isinstance(f, str)
                else str(f.get("point", "") if isinstance(f, dict) else f)).strip()
        items.append((text[:300], "covered_in_tangent"))

    # Dedupe against the whole existing record before writing anything. Three
    # verdicts, because the risks are asymmetric: a wrong merge silently
    # destroys a distinct fact (near-identical clinical strings routinely
    # carry opposite meanings), while a wrong split just leaves a duplicate.
    # So confident matches merge, confident non-matches create, and the gray
    # zone is RETURNED to the tutor to resolve — never silently decided.
    # The matcher is validated against every pair in the live database in
    # tests/test_fact_matcher.py: 46/46 true duplicates merged, 0 false merges.
    from .fact_matcher import find_matching_point
    existing_rows = _existing_points()
    merged, needs_review = [], []

    for text, kind in items:
        if len(text.replace("[asked] ", "")) < 12:
            skipped.append({"item": text[:60], "reason": "too short to be testable"})
            continue

        match, unsure = find_matching_point(topic, text, existing_rows)
        if match:
            # Same fact already tracked (possibly under another topic, possibly
            # worded better). Touch THAT one — the exposure lands on its real
            # history instead of a parallel copy — keeping its canonical text.
            r = _record_kp(
                topic=match["topic"], point=match["point"],
                is_correct=False, confidence=None,
                mistake_type="pretest_unstudied", triage=False,
            )
            if r:
                r["kind"] = kind
                r["merged_into_existing"] = True
                r["match_reason"] = match["why"]
                merged.append(r)
            continue
        if unsure:
            # Do not guess. Hand both texts back for the tutor to decide:
            # either re-log using the existing wording (which will then merge)
            # or restate the fact so it is clearly distinct.
            needs_review.append({
                "new": text,
                "existing": unsure["point"],
                "existing_topic": unsure["topic"],
                "why": unsure["why"],
            })
            continue

        r = _record_kp(
            topic=topic,
            point=text,
            is_correct=False,        # exposure/curiosity, not demonstrated knowledge
            confidence=None,
            mistake_type="pretest_unstudied",
            triage=False,
        )
        if r:
            r["kind"] = kind
            recorded.append(r)
        else:
            skipped.append({"item": text[:60], "reason": "blank topic or item"})

    return {
        "ok": True,
        "recorded": len(recorded),
        "merged_with_existing": len(merged),
        "merged": [{"point": m["point"][:120], "why": m.get("match_reason", "")}
                   for m in merged],
        "needs_review": needs_review,
        "question_logged": bool(q),
        "canonical_topic": topic,
        "topic_was_canonicalized": resolved,
        "trigger": trigger,
        "skipped": skipped,
        "note": (("Logged as a self-identified gap, unproven and due for testing. "
                  "Now ask the user their OWN question back — answering it is the "
                  "retrieval practice, and it produces a graded record."
                  if q else
                  "Captured as exposed-but-unproven. Ask a recall question on at "
                  "least one of these before moving on.")
                 + (" NEEDS_REVIEW is non-empty: for each entry, decide whether "
                    "the new fact is the same as the existing one — if so, "
                    "re-log using the EXISTING wording; if genuinely distinct, "
                    "restate it so the difference is explicit and log again."
                    if needs_review else "")),
    }


def get_knowledge_points(topic: str = "", status: str = "", due_only: bool = False) -> dict:
    """List atomic knowledge points with calibration + schedule. Filter by `topic`,
    `status` ('weak'|'learning'|'mastered'), and/or `due_only` (due on their own
    schedule). Use to see exactly which specific facts are weak / mis-calibrated."""
    pts = _get_kp(topic=topic or None, status=status, due_only=due_only)
    return {
        "points": pts,
        "count": len(pts),
        "weak_count": sum(1 for p in pts if p["status"] == "weak"),
        "overconfident": [p["point"] for p in pts if p.get("calibration") == "overconfident"],
    }


_DAILY_FACT_RATION = 20  # ~30 min at ~1.5 min/fact — a session, not a shift


def get_due_knowledge_points(limit: int = 25, car: bool = False) -> dict:
    """TODAY'S RATION of due facts, with the honest load picture attached.

    Serve `todays_set` and stop. Do NOT present the total backlog as today's
    obligation: the tutor once told the user their reviews would take 2-3
    hours, which was arithmetically true of the whole backlog and completely
    wrong as advice. The backlog was a one-time hump of stale items from
    before this queue was consulted at all — and FSRS makes carrying it
    SAFE: answering a late fact correctly schedules it 31-65 days out
    (measured on this database), so each cleared item stays gone. Rationing
    beats grinding: ~20/day clears the hump in under a week at ~30 min/day
    without burning the user out of the habit that makes any of this work.

    Returns:
        todays_set        — the facts to actually serve (ration-capped)
        backlog_total     — everything due, for honesty
        carried           — due items NOT served today (safe to carry)
        estimated_minutes — for todays_set, not the backlog
        note              — how to present this to the user

    When car=True, returns only short/ear-friendly points (≤120 chars).
    """
    ration = min(limit, _DAILY_FACT_RATION)
    # Over-fetch so the ration can be chosen by priority, not arrival order.
    pts = _get_due_kp(limit=500, car=car)

    def priority(p):
        # Weakest first, then most overdue: a weak fact is a known hole, and
        # the longest-unseen items are closest to being lost entirely.
        status_rank = {"weak": 0, "learning": 1, "mastered": 2}
        return (status_rank.get(p.get("status"), 1),
                str(p.get("next_review_date") or "9999"))

    pts_sorted = sorted(pts, key=priority)
    todays = pts_sorted[:ration]
    carried = max(0, len(pts_sorted) - len(todays))
    return {
        "todays_set": todays,
        "due_points": todays,          # backward-compat alias
        "count": len(todays),
        "backlog_total": len(pts_sorted),
        "carried": carried,
        "estimated_minutes": round(len(todays) * 1.5),
        "note": (
            f"Serve todays_set (~{round(len(todays) * 1.5)} min). "
            + (f"{carried} more are due but carried to later days — tell the "
               f"user the backlog is shrinking on schedule and carrying is "
               f"safe: a late fact answered correctly is scheduled weeks out "
               f"by FSRS, so it will not come back tomorrow. NEVER quote the "
               f"whole backlog as today's workload." if carried else
               "The queue is clear after this set.")
        ),
    }


def get_knowledge_gaps(topic: str = "", status: str = "open") -> dict:
    """(Compat) List not-yet-mastered knowledge points as 'gaps'. Prefer
    get_knowledge_points for the full model. Filter by `topic`/`status`."""
    gaps = _get_knowledge_gaps(topic=topic or None, status=status)
    return {"gaps": gaps, "open_count": sum(1 for g in gaps if g.get("status") == "open")}


def get_illness_script(topic: str) -> dict:
    """Get the 5-field illness script for a diagnosis (enabling conditions,
    pathophysiology, time course, key discriminating features, consequence if missed).
    Returns {"found": bool, "script": {...}}."""
    s = _get_script(topic)
    return {"found": bool(s), "script": s or {}}


def set_illness_script(topic: str, enabling_conditions: str = "", pathophysiology: str = "",
                       time_course: str = "", key_features: str = "",
                       consequence_if_missed: str = "", discipline: str = "", source: str = "") -> dict:
    """Store/update the 5-field illness script for a diagnosis (build it from retrieved
    sources, never invented). Fields: enabling_conditions, pathophysiology, time_course,
    key_features, consequence_if_missed."""
    _upsert_script(topic, enabling_conditions, pathophysiology, time_course,
                   key_features, consequence_if_missed, discipline, source)
    return {"ok": True, "topic": topic}


def get_contrastive_case(topic: str) -> dict:
    """Entities this topic is commonly confused with (+ the discriminating feature),
    for building contrastive cases. Returns {"topic", "confusables": [...]}."""
    pairs = _get_confusable(topic)
    return {"topic": topic, "confusables": pairs, "count": len(pairs)}


def add_confusable_pair(topic_a: str, topic_b: str, discriminator: str = "") -> dict:
    """Register two commonly-confused entities and the key feature that separates them."""
    _add_confusable(topic_a, topic_b, discriminator)
    return {"ok": True}


def mark_topic_mastered_tool(topic: str, subtopic: str = "") -> dict:
    """Force a topic to mastered status, pushing its next review far out.

    Only when the user explicitly says they already know it. Do NOT call this
    just because they answered correctly once — mastery is earned through the
    normal FSRS schedule, and short-circuiting it hides real gaps.
    """
    mark_topic_mastered(topic, subtopic)
    return {"ok": True, "knowledge_points_mastered": True}


# ---------------------------------------------------------------------------
# Dosing-drill tools
# ---------------------------------------------------------------------------

def get_dosing_drill(
    category: str = "",
    discipline: str = "",
    drug: str = "",
    mode: str = "auto",
) -> dict:
    """Return a drug-dosing drill.

    mode:
      'recall'      — always serve a recall drill (dose memorization).
      'calculation' — always serve a calculation drill (numeric computation).
      'auto'        — DEFAULT. For the chosen drug, check whether its recall
                      knowledge point ("dosing-recall:{drug}") is mastered.
                      If NOT mastered → serve recall drill.
                      If mastered AND rule is not recall_only → serve calc drill.
                      Selection order: tier ASC (tier-1 everyday first), then
                      drugs whose recall KP is weakest/unseen first.

    SAFETY: for calculation drills the answer field is computed deterministically
    by Python — the tutor must NOT recompute it from memory. Trust the engine.

    Filter by category (partial match on context), discipline ('anesthesia'|'medicine'),
    or drug name (partial match). If no filter, picks from the full set.
    """
    from .dosing_engine import (
        get_all_rules, generate_dosing_drill, generate_recall_drill, RECALL_ONLY_TYPE
    )
    import random as _random

    rules = get_all_rules(category=category, discipline=discipline, drug=drug)
    if not rules:
        return {"error": "No dosing rules found matching the given filters. "
                         "Seed the rules first with seed_dosing_rules()."}

    if mode == "recall":
        rule = _random.choice(rules)
        return generate_recall_drill(rule)

    if mode == "calculation":
        calc_rules = [r for r in rules
                      if not r.get("recall_only") and r.get("calc_type") != RECALL_ONLY_TYPE]
        if not calc_rules:
            return {"error": "No calculation rules found (all matching rules are recall_only)."}
        rule = _random.choice(calc_rules)
        return generate_dosing_drill(rule)

    # ---- AUTO MODE: mastery-gated selection (tier-1 first, recall before calc) ----
    # Sort: tier ASC is already guaranteed by get_all_rules ORDER BY tier ASC, drug ASC.
    # Within tier, prefer rules whose recall KP is unseen/weak.
    from .student_model import get_knowledge_points as _get_kp

    def _recall_status(drug_name: str) -> str:
        """Return status of dosing-recall:{drug} KP, or 'unseen' if not found."""
        pts = _get_kp(topic=drug_name)
        for p in pts:
            if p.get("point") == f"dosing-recall:{drug_name}":
                return p.get("status", "unseen")
        return "unseen"

    STATUS_ORDER = {"unseen": 0, "weak": 1, "learning": 2, "mastered": 3}

    # Score each rule: (tier, recall_status_rank)
    scored = sorted(
        rules,
        key=lambda r: (r.get("tier", 2), STATUS_ORDER.get(_recall_status(r["drug"]), 0)),
    )

    # Pick from the top band (rules sharing lowest composite score)
    if scored:
        best_key = (scored[0].get("tier", 2), STATUS_ORDER.get(_recall_status(scored[0]["drug"]), 0))
        top_band = [r for r in scored
                    if (r.get("tier", 2), STATUS_ORDER.get(_recall_status(r["drug"]), 0)) == best_key]
        rule = _random.choice(top_band)
    else:
        rule = _random.choice(rules)

    drug_name = rule["drug"]
    recall_mastered = _recall_status(drug_name) == "mastered"
    is_recall_only = bool(rule.get("recall_only")) or rule.get("calc_type") == RECALL_ONLY_TYPE

    if recall_mastered and not is_recall_only:
        return generate_dosing_drill(rule)
    else:
        return generate_recall_drill(rule)


def submit_dosing_answer(
    drug: str,
    is_correct: bool,
    confidence: int = 3,
    calc_type: str = "",
    mode: str = "recall",
) -> dict:
    """Record a dosing-drill result via the FSRS knowledge-point system.

    mode: 'recall' | 'calculation' (default 'recall').
      'recall'      → point key 'dosing-recall:{drug}'
      'calculation' → point key 'dosing-calc:{drug}:{calc_type}'

    Both are matched by get_due_dosing_drills (LIKE 'dosing-%').
    mistake_type is always 'drug_dosing'.

    Returns the updated knowledge-point state (status, interval_days, next_review_date).
    """
    topic = str(drug or "").strip()
    if not topic:
        return {"ok": False, "error": "blank drug or calc_type"}

    clean_mode = mode.strip().lower()
    if clean_mode == "calculation":
        # Key on the drug alone. Including calc_type made the key depend on
        # whether the caller happened to pass it, splitting one drill's FSRS
        # history across 'dosing-calc:{drug}' and 'dosing-calc:{drug}:{ct}' —
        # so neither row ever accumulated the consecutive-correct streak.
        point = f"dosing-calc:{drug}"
    else:
        # Default to recall — covers mode='recall' and legacy calls
        point = f"dosing-recall:{drug}"

    result = _record_kp(
        topic=topic,
        point=point,
        is_correct=bool(is_correct),
        confidence=max(1, min(5, int(confidence))) if confidence else 3,
        mistake_type="drug_dosing",
    )
    if result is None:
        return {"ok": False, "error": "blank drug or calc_type"}
    return {"ok": True, **result}


def get_due_dosing_drills(limit: int = 10) -> dict:
    """Return dosing knowledge points that are due for review on their own
    FSRS schedule.

    Matches point keys: 'dosing-recall:{drug}', 'dosing-calc:{drug}:{calc_type}',
    and legacy 'dosing:{drug}:{calc_type}' keys (backward compatible).

    Tutor uses these to decide whether to include a dosing drill in the session.
    """
    # Over-fetch: the dosing filter runs in Python, so a small SQL page
    # hides due dosing points behind non-dosing ones (same failure mode
    # as the car filter in get_due_knowledge_points).
    all_due = _get_due_kp(limit=1000)
    dosing_due = [
        p for p in all_due
        if p.get("point", "").startswith("dosing-recall:")
        or p.get("point", "").startswith("dosing-calc:")
        or p.get("point", "").startswith("dosing:")
    ][:limit]
    return {
        "due_dosing_points": dosing_due,
        "count": len(dosing_due),
    }


def car_next(answered: dict | None = None, mode: str = "full",
             record_topic_level: bool = True, include_dosing: bool = True) -> dict:
    """ONE call per hands-free item: records the answer just given AND returns
    the next item. `answered` = {topic, point (echo the previous item's
    point_key), correct, confidence, mistake_type, user_answer, also_covered:
    [{point, topic?, correct, confidence?, mistake_type?}]}. mode="full"
    (default) serves the whole due queue + breadth-first new material;
    "lite" = short facts only. Same implementation as the HTTP /car/next."""
    from .api import car_next as _http_car_next
    from .schemas import CarNextRequest
    req = CarNextRequest(answered=answered, mode=mode,
                         record_topic_level=record_topic_level,
                         include_dosing=include_dosing)
    return _http_car_next(req)


def get_claude_instructions() -> dict:
    """Full tutor instructions for the Claude side + a version hash. Call once
    at the start of every conversation and follow the returned `instructions`
    exactly. This mirrors the GPT's getSystemInstructions: editing
    CLAUDE_PROJECT_INSTRUCTIONS.md updates behavior on the next conversation,
    with no re-pasting into the Project UI (the Project keeps only a short
    bootstrap)."""
    import hashlib
    from pathlib import Path
    md = Path(__file__).resolve().parent.parent / "CLAUDE_PROJECT_INSTRUCTIONS.md"
    if not md.exists():
        return {"version": "missing", "instructions": ""}
    text = md.read_text(encoding="utf-8")
    return {"version": hashlib.sha1(text.encode()).hexdigest()[:12],
            "instructions": text}


def get_mistake_review(window_days: int = 30) -> dict:
    """Weak patterns + the last 7 days of misses WITH their original questions.
    Monday ritual: re-ask recent_misses (shuffled, lightly reworded) before any
    new material — error-focused review has outsized retention returns."""
    from .weak_patterns import compute_weak_patterns
    return compute_weak_patterns(window_days=window_days).model_dump()


def set_default_training_phase_tool(default_training_phase: str) -> dict:
    """Set the training phase that shapes question depth and framing
    (e.g. 'intern_year', 'ca1'). Persists across sessions — change it only when
    the user says their stage or rotation has actually changed.
    """
    set_default_training_phase(default_training_phase)
    return {"ok": True, "default_training_phase": default_training_phase}


def _log_tool_call(name: str, ok: bool, detail: str = "") -> None:
    """Append one line per tool call to storage/logs/tool_calls.log.

    The MCP transport log only records 'CallToolRequest' with no tool NAME, so
    "which tools did the tutor actually call?" — the first question when a
    session behaves oddly — was unanswerable after the fact. That gap cost a
    real diagnosis: a session recorded 13 attempts but zero knowledge points,
    and the logs could not distinguish "the tutor never called
    submit_knowledge_points" from "the call failed".
    """
    try:
        from pathlib import Path
        from datetime import datetime, timezone
        from .config import settings
        log = Path(settings.log_dir) / "tool_calls.log"
        log.parent.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).isoformat()[:19]
        status = "ok" if ok else "ERROR"
        with log.open("a", encoding="utf-8") as f:
            f.write("\t".join([stamp, name, status, detail[:120]]) + "\n")
    except Exception:
        pass  # logging must never break a tool call


# Fields worth keeping verbatim: these ARE the conversation. Everything else is
# truncated hard, because retrieval results are ~1 kB per passage and would
# bury the transcript in source text within a session or two.
_TRANSCRIPT_VERBATIM = {
    "question", "user_answer", "topic", "subtopic", "point", "points", "facts",
    "trigger", "query", "gap_note", "knowledge_points", "is_correct",
    "confidence_reported", "mistake_type", "teach_back_quality",
    "transfer_success", "result", "answered",
}
# Never echoed into the transcript, however they arrive.
_TRANSCRIPT_NEVER = {"instructions", "sources", "results", "api_key", "token", "key"}
_TRANSCRIPT_MAX_BYTES = 8_000_000  # ~8 MB, then rotate to .1


def _compact(value, depth: int = 0):
    """Shrink a payload to what a human auditor would actually read."""
    if depth > 3:
        return "..."
    if isinstance(value, dict):
        out = {}
        for k, v in value.items():
            if k in _TRANSCRIPT_NEVER:
                out[k] = f"<{k} omitted>"
            elif k in _TRANSCRIPT_VERBATIM:
                out[k] = _compact(v, depth + 1)
            else:
                s = str(v)
                out[k] = s if len(s) <= 120 else s[:120] + "..."
        return out
    if isinstance(value, (list, tuple)):
        return [_compact(v, depth + 1) for v in value[:12]]
    if isinstance(value, str):
        return value if len(value) <= 1200 else value[:1200] + "..."
    return value


def _log_transcript(name: str, args: dict, kwargs: dict, result, error: str = "") -> None:
    """Append the full substance of a tool call to a JSONL transcript.

    tool_calls.log records only tool NAMES, which answers "what did it call?"
    but not "what did it ask, and what did I say?". That gap made a real audit
    impossible: a session went down a digoxin tangent and afterwards there was
    no way to see any of it — the questions, the answers, the facts covered
    were nowhere, because only records that reached the database survived.

    Tool arguments carry the substance of the session: every question asked,
    every answer given, every grade, every retrieval query, every tangent fact.
    Logging them makes a session auditable after the fact without depending on
    the chat UI. The tutor's prose between questions is not visible here — it
    never reaches the backend.

    Local file, the user's own study data, never transmitted. Truncated and
    rotated so it cannot grow without bound.
    """
    try:
        import json
        from datetime import datetime, timezone
        from pathlib import Path
        from .config import settings

        path = Path(settings.log_dir) / "tool_transcript.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists() and path.stat().st_size > _TRANSCRIPT_MAX_BYTES:
            path.replace(path.with_suffix(".jsonl.1"))

        payload = dict(kwargs)
        if args:
            payload["_positional"] = list(args)
        entry = {
            "ts": datetime.now(timezone.utc).isoformat()[:19],
            "tool": name,
            "args": _compact(payload),
        }
        if error:
            entry["error"] = error[:300]
        elif isinstance(result, dict):
            # Keep the decisions, not the source text.
            entry["result"] = _compact({
                k: v for k, v in result.items()
                if k in ("ok", "recorded", "knowledge_points_recorded",
                         "knowledge_points_derived", "canonical_topic", "topic",
                         "status", "reason", "days_overdue", "retrieval_confidence",
                         "insufficient_context", "next_review_date", "count",
                         "setup_warning")
            })
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False, default=str) + "\n")
    except Exception:
        pass  # auditing must never break a tool call


def _logged(fn, name: str):
    """Wrap a tool fn so every invocation is recorded by name AND in full.

    Two logs on purpose: tool_calls.log stays a one-line-per-call ledger that is
    cheap to scan and grep, and tool_transcript.jsonl carries the substance for
    replaying a session.
    """
    import functools

    @functools.wraps(fn)
    def wrapper(*a, **kw):
        try:
            result = fn(*a, **kw)
            _log_tool_call(name, True)
            _log_transcript(name, a, kw, result)
            return result
        except Exception as exc:
            _log_tool_call(name, False, str(exc))
            _log_transcript(name, a, kw, None, error=str(exc))
            raise
    return wrapper


_SETUP_NOTICE = (
    "SETUP PROBLEM — you have not called `get_claude_instructions` in this "
    "conversation, so you are running WITHOUT the tutor instructions. Call it "
    "NOW and follow what it returns before asking anything else. Without it a "
    "session silently degrades: questions get written from your own training "
    "instead of the retrieval corpus (which is forbidden), due reviews and due "
    "knowledge points are never fetched, and answers are recorded without "
    "their knowledge points so the fact-level layer stays empty."
)


def _instructions_loaded_recently(hours: int = 18) -> bool:
    """Has get_claude_instructions been called in the recent past?

    A whole 32-question session once ran without ever fetching the
    instructions: the tutor improvised from tool NAMES alone, so it called
    get_next_topic and submit_answer (self-explanatory) and never called
    retrieval at all. Every question came from model training rather than the
    corpus, no due review or fact queue was consulted, and zero knowledge
    points were written — with no error anywhere, because nothing failed.

    The backend cannot make a client load its instructions, but it can decline
    to stay quiet about it. Read from the tool-call log rather than process
    state so a server restart mid-session does not read as "never loaded".
    A false positive here is harmless: it prompts one extra instruction fetch.
    """
    try:
        from datetime import datetime, timedelta, timezone
        from pathlib import Path
        from .config import settings
        log = Path(settings.log_dir) / "tool_calls.log"
        if not log.exists():
            return False
        cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)
        # Only the tail matters; the log is append-only and line-oriented.
        for line in log.read_text(encoding="utf-8", errors="replace").splitlines()[-2000:]:
            parts = line.split("\t")
            if len(parts) >= 2 and parts[1] == "get_claude_instructions":
                try:
                    when = datetime.fromisoformat(parts[0]).replace(tzinfo=timezone.utc)
                except ValueError:
                    continue
                if when >= cutoff:
                    return True
        return False
    except Exception:
        return True  # never let this check break a tool call


def _with_setup_check(payload: dict) -> dict:
    """Attach the setup warning to a response when instructions are missing."""
    if isinstance(payload, dict) and not _instructions_loaded_recently():
        payload = dict(payload)
        payload["setup_warning"] = _SETUP_NOTICE
    return payload


def _attach_sources(payload: dict, max_results: int = 5) -> dict:
    """Retrieve for the topic being served, and return the passages with it.

    Grounding is the cardinal rule — every question must come from the corpus —
    and it was being skipped almost entirely: 0 retrieval calls across 22
    answers on 2026-08-17, 1 across 13 on 2026-08-18. The questions that
    resulted looked clinically sound, which is exactly what makes it dangerous:
    they came from model training, cited nothing, and no failure was visible.

    Two rounds of instruction changes did not fix it, so stop depending on the
    tutor making a second call. The backend already computes `retrieval_query`
    for the topic it is serving; running that retrieval here means the material
    arrives WITH the topic and grounding costs no extra round trip. The tutor
    can still call search_clinical_sources for depth, and should — this is a
    floor, not a ceiling.
    """
    if not isinstance(payload, dict):
        return payload
    query = (payload.get("retrieval_query") or payload.get("topic") or "").strip()
    if not query:
        return payload
    try:
        results, insufficient = hybrid_search(
            query, mode="intern_teach", max_results=max_results)
        payload = dict(payload)
        payload["sources"] = [r.model_dump() for r in results]
        payload["retrieval_confidence"] = retrieval_confidence(results)
        payload["insufficient_context"] = insufficient
        payload["sources_note"] = (
            "Build the question ONLY from these passages. They were retrieved "
            "for you so grounding needs no extra call. If they are insufficient, "
            "say so or call search_clinical_sources — never fill the gap from "
            "your own training."
        )
    except Exception as exc:  # retrieval must never break topic selection
        payload = dict(payload)
        payload["sources"] = []
        payload["sources_error"] = str(exc)[:200]
    return payload


@functools.wraps(get_next_topic)
def get_next_topic_checked(*args, **kwargs) -> dict:
    """Next topic to study, WITH its grounding passages already retrieved.

    This is the tool a tutor reaches for first and calls most, which makes it
    the reliable place both to surface a missing-instructions state and to
    deliver the source material. functools.wraps keeps the real signature and
    docstring, which FastMCP reads to build the tool schema — without it the
    parameters collapse to (args, kwargs).
    """
    return _with_setup_check(_attach_sources(get_next_topic(*args, **kwargs)))


def build_server():
    """Create and return a configured FastMCP instance with all tools registered."""
    import os
    from pathlib import Path
    from mcp.server.fastmcp import FastMCP
    from .student_model import seed_curriculum as _seed_curriculum
    initialize_database()  # ensure the SQLite schema (topics, etc.) exists at startup

    # Best-effort curriculum seeding: load blueprint if present, never crash startup.
    _blueprint = Path(__file__).parent.parent / "data" / "curriculum_blueprint.json"
    if _blueprint.exists():
        try:
            _seed_curriculum(str(_blueprint))
        except Exception as _e:
            print(f"[startup] curriculum seed skipped: {_e}", flush=True)

    mcp = FastMCP("clinical-attending-os")
    # Legacy endpoints
    mcp.tool()(_logged(search_clinical_sources, "search_clinical_sources"))
    mcp.tool()(_logged(answer_from_clinical_sources, "answer_from_clinical_sources"))
    mcp.tool()(_logged(start_study_session, "start_study_session"))
    mcp.tool()(_logged(submit_study_answer, "submit_study_answer"))
    mcp.tool()(_logged(get_due_reviews, "get_due_reviews"))
    mcp.tool()(_logged(get_student_dashboard, "get_student_dashboard"))
    mcp.tool()(_logged(log_missed_topic, "log_missed_topic"))
    mcp.tool(name="submit_knowledge_points")(_logged(submit_knowledge_points, "submit_knowledge_points"))
    mcp.tool(name="log_tangent")(_logged(log_tangent, "log_tangent"))
    mcp.tool(name="log_user_feedback")(_logged(log_user_feedback, "log_user_feedback"))
    mcp.tool(name="get_knowledge_points")(_logged(get_knowledge_points, "get_knowledge_points"))
    mcp.tool(name="get_due_knowledge_points")(_logged(get_due_knowledge_points, "get_due_knowledge_points"))
    mcp.tool(name="get_knowledge_gaps")(_logged(get_knowledge_gaps, "get_knowledge_gaps"))
    mcp.tool(name="get_illness_script")(_logged(get_illness_script, "get_illness_script"))
    mcp.tool(name="set_illness_script")(_logged(set_illness_script, "set_illness_script"))
    mcp.tool(name="get_contrastive_case")(_logged(get_contrastive_case, "get_contrastive_case"))
    mcp.tool(name="add_confusable_pair")(_logged(add_confusable_pair, "add_confusable_pair"))
    mcp.tool(name="mark_topic_mastered")(_logged(mark_topic_mastered_tool, "mark_topic_mastered"))
    mcp.tool(name="set_default_training_phase")(_logged(set_default_training_phase_tool, "set_default_training_phase"))
    # Phase 1: New MCP endpoints
    mcp.tool(name="mcp_retrieval")(_logged(mcp_retrieval, "mcp_retrieval"))
    mcp.tool(name="get_session_state")(_logged(get_session_state, "get_session_state"))
    mcp.tool(name="get_next_topic")(_logged(get_next_topic_checked, "get_next_topic"))
    mcp.tool(name="submit_answer")(_logged(submit_answer, "submit_answer"))
    mcp.tool(name="get_mastery_gates")(_logged(get_mastery_gates, "get_mastery_gates"))
    mcp.tool(name="get_progress")(_logged(get_progress, "get_progress"))
    # Curriculum coverage tools
    mcp.tool(name="get_mastery_map")(_logged(get_mastery_map, "get_mastery_map"))
    mcp.tool(name="get_calibration_report")(_logged(get_calibration_report, "get_calibration_report"))
    mcp.tool(name="get_mistake_review")(_logged(get_mistake_review, "get_mistake_review"))
    mcp.tool(name="car_next")(_logged(car_next, "car_next"))
    mcp.tool(name="get_claude_instructions")(_logged(get_claude_instructions, "get_claude_instructions"))
    mcp.tool(name="set_medicine_weight")(_logged(set_medicine_weight_tool, "set_medicine_weight"))
    # Dosing-drill tools (CPU-only calc engine — no corpus/Chroma access)
    mcp.tool(name="get_dosing_drill")(_logged(get_dosing_drill, "get_dosing_drill"))
    mcp.tool(name="submit_dosing_answer")(_logged(submit_dosing_answer, "submit_dosing_answer"))
    mcp.tool(name="get_due_dosing_drills")(_logged(get_due_dosing_drills, "get_due_dosing_drills"))

    # Best-effort dosing rules seeding
    _dosing_blueprint = Path(__file__).parent.parent / "data" / "dosing_rules.json"
    if _dosing_blueprint.exists():
        try:
            from .dosing_engine import seed_dosing_rules as _seed_dosing
            _seed_dosing(str(_dosing_blueprint))
        except Exception as _e:
            print(f"[startup] dosing rules seed skipped: {_e}", flush=True)

    # Best-effort KP catalog seeding (file generated separately — may not exist yet)
    mcp.tool(name="get_kp_to_study")(_logged(get_kp_to_study, "get_kp_to_study"))
    _kp_catalog = Path(__file__).parent.parent / "data" / "kp_catalog.json"
    if _kp_catalog.exists():
        try:
            from .student_model import seed_kp_catalog as _seed_kp_catalog
            _seed_kp_catalog(str(_kp_catalog))
        except Exception as _e:
            print(f"[startup] kp_catalog seed skipped: {_e}", flush=True)

    return mcp


def build_http_app(server, auth_token: str):
    """Wrap the FastMCP streamable-http Starlette app with bearer-token auth
    and an unauthenticated /health route."""
    if not auth_token:
        raise ValueError("auth_token must be non-empty")
    from starlette.responses import JSONResponse, PlainTextResponse
    from starlette.middleware.base import BaseHTTPMiddleware
    from starlette.routing import Route
    from mcp.server.transport_security import TransportSecuritySettings

    # Behind a trusted reverse proxy (HF Space), the upstream Host header is the
    # public domain, which MCP's DNS-rebinding protection rejects ("Invalid Host
    # header"). Our bearer token is the real access gate, so disable the host check.
    server.settings.transport_security = TransportSecuritySettings(
        enable_dns_rebinding_protection=False
    )
    # Stateless transport: each request is self-contained, so a Space restart or a
    # proxy hiccup can't orphan a session and drop the client's tool list. Robust
    # for restart-prone / proxied hosting (HF Spaces). Tutor state lives in SQLite,
    # not the MCP session, so this is safe.
    server.settings.stateless_http = True
    # Mount the MCP endpoint at the app ROOT. Behind the Tailscale Funnel the
    # public path (/mcp) is stripped before proxying, so the default /mcp mount
    # would only be reachable at the awkward https://<host>/mcp/mcp. Mounting
    # at "/" makes the connector URL simply https://<host>/mcp.
    server.settings.streamable_http_path = "/"

    app = server.streamable_http_app()

    async def health(_request):
        return PlainTextResponse("ok")
    app.router.routes.append(Route("/health", health, methods=["GET"]))

    # /warm: load the retrieval models + indices into cache (idempotent). Hitting
    # this on a schedule keeps the heavy ML stack resident so the first real user
    # query is never a ~50s cold start. Unauthenticated like /health (no secrets).
    async def warm(_request):
        import anyio
        result = await anyio.to_thread.run_sync(warm_retrieval)
        return JSONResponse(result)
    app.router.routes.append(Route("/warm", warm, methods=["GET"]))

    expected = f"Bearer {auth_token}"

    class _AuthMiddleware(BaseHTTPMiddleware):
        async def dispatch(self, request, call_next):
            if request.url.path in ("/health", "/warm"):
                return await call_next(request)
            header = request.headers.get("authorization", "")
            query_key = request.query_params.get("key", "")
            ok = hmac.compare_digest(header, expected) or (
                bool(query_key) and hmac.compare_digest(query_key, auth_token)
            )
            if not ok:
                return JSONResponse({"error": "unauthorized"}, status_code=401)
            return await call_next(request)

    app.add_middleware(_AuthMiddleware)
    return app


def _db_fingerprint(db_path: str) -> str:
    """Cheap content fingerprint so we only sync when study state actually changed."""
    import sqlite3
    import hashlib
    parts = []
    try:
        con = sqlite3.connect(db_path)
        for q in (
            "SELECT COUNT(*), COALESCE(MAX(attempt_id),0) FROM question_attempts",
            "SELECT COUNT(*), COALESCE(MAX(updated_at),'') FROM topics",
            "SELECT COUNT(*) FROM sessions",
        ):
            try:
                parts.append(str(con.execute(q).fetchone()))
            except Exception:
                parts.append("-")
        con.close()
    except Exception:
        return ""
    return hashlib.sha1("|".join(parts).encode()).hexdigest()


def _state_sync_loop(interval: int) -> None:
    """Periodically snapshot the student DB to the private STATE_DATASET so
    progress survives Space restarts. Only uploads when study state changed
    (avoids dataset storage bloat). No-op unless STATE_DATASET + HF_TOKEN set."""
    import os
    import time
    import sqlite3
    state_repo = os.getenv("STATE_DATASET", "")
    hf_token = os.getenv("HF_TOKEN", "")
    if not (state_repo and hf_token):
        return  # persistence disabled (local/dev)
    from huggingface_hub import HfApi
    from .config import settings
    db_path = str(settings.sqlite_db_path)
    api = HfApi(token=hf_token)
    last_fp = _db_fingerprint(db_path) if os.path.exists(db_path) else None
    while True:
        time.sleep(interval)
        try:
            if not os.path.exists(db_path):
                continue
            fp = _db_fingerprint(db_path)
            if fp and fp == last_fp:
                continue  # nothing changed since last sync -> skip (no storage bloat)
            tmp = db_path + ".sync"
            src = sqlite3.connect(db_path)
            dst = sqlite3.connect(tmp)
            with dst:
                src.backup(dst)  # consistent snapshot (incl. WAL)
            dst.close()
            src.close()
            api.upload_file(
                path_or_fileobj=tmp, path_in_repo="student_model.db",
                repo_id=state_repo, repo_type="dataset",
                commit_message="state sync",
            )
            os.remove(tmp)
            last_fp = fp
        except Exception as exc:  # never let persistence crash the server
            print(f"[state-sync] skipped: {exc}", flush=True)


def start_state_sync() -> None:
    """Start the background state-persistence thread (daemon)."""
    import os
    import threading
    interval = int(os.getenv("STATE_SYNC_SECONDS", "180"))
    threading.Thread(target=_state_sync_loop, args=(interval,), daemon=True).start()


def warm_retrieval() -> dict:
    """Best-effort: run one tiny hybrid_search to pull the embedding model, reranker,
    Chroma collection, and BM25/phrase indices into the process lru_cache. The first
    cold retrieval is ~50s+ on a 2-vCPU Space; once warmed it's a couple seconds.
    Idempotent and cheap once warm. Never raises."""
    import time
    t0 = time.time()
    try:
        hybrid_search("warmup", max_results=1)
        return {"ok": True, "warm": True, "seconds": round(time.time() - t0, 1)}
    except Exception as exc:
        return {"ok": False, "warm": False, "error": str(exc), "seconds": round(time.time() - t0, 1)}


def start_warmup() -> None:
    """Preload the retrieval stack in a background daemon thread at startup so the
    container is query-ready right after boot (and after every HF restart), without
    blocking the /health route. Eliminates the cold-first-query flap."""
    import threading

    def _run():
        print("[warmup] preloading retrieval models + indices ...", flush=True)
        r = warm_retrieval()
        print(f"[warmup] {'ready' if r.get('warm') else 'FAILED'} in {r.get('seconds')}s "
              f"{r.get('error','')}".strip(), flush=True)

    threading.Thread(target=_run, daemon=True).start()


def _serve_http(app, host, port):  # pragma: no cover - thin uvicorn wrapper
    import uvicorn
    uvicorn.run(app, host=host, port=port)


def main() -> None:
    import os
    try:
        import mcp  # noqa: F401
    except Exception as exc:
        raise SystemExit("Install mcp to run the MCP server: pip install mcp") from exc
    server = build_server()
    transport = os.getenv("MCP_TRANSPORT", "stdio")
    if transport == "stdio":
        server.run()
        return
    if transport == "streamable-http":
        host = os.getenv("MCP_HOST", "127.0.0.1")
        port = int(os.getenv("MCP_PORT", "8000"))
        token = os.getenv("MCP_AUTH_TOKEN", "")
        if not token:
            raise SystemExit("MCP_AUTH_TOKEN must be set for HTTP transport")
        app = build_http_app(server, token)
        start_state_sync()  # persist progress to STATE_DATASET across restarts
        start_warmup()      # preload ML models so the first query isn't a ~50s cold start
        _serve_http(app, host, port)
        return
    raise SystemExit(f"Unknown MCP_TRANSPORT: {transport}")


if __name__ == "__main__":
    main()
