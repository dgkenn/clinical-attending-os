from __future__ import annotations

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
    results, insufficient = hybrid_search(query, mode=mode, library_filter=library_filter, max_results=max_results)
    return {
        "results": [r.model_dump() for r in results],
        "retrieval_confidence": retrieval_confidence(results),
        "insufficient_context": insufficient,
    }


def answer_from_clinical_sources(query: str, mode: str = "intern_teach") -> dict:
    return answer_query(query, mode).model_dump()


def start_study_session(duration_minutes: int = 20, mode: str = "default", focus_topic: str | None = None, training_phase: str | None = None) -> dict:
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
    return record_evaluated_answer(session_id, question, user_answer, topic, subtopic, result, mistake_type, ideal_answer)


def get_due_reviews() -> list[dict]:
    return _due()


def get_student_dashboard() -> dict:
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


def get_due_knowledge_points(limit: int = 25, car: bool = False) -> dict:
    """Atomic knowledge points due for review on their OWN spaced-repetition schedule
    (independent of topic-level reviews). Weave these in as targeted micro-questions.

    When car=True, returns only short/ear-friendly points (≤120 chars, no heavy
    enumerations) suitable for hands-free voice study while driving.
    """
    pts = _get_due_kp(limit=limit, car=car)
    return {"due_points": pts, "count": len(pts)}


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


def get_mistake_review(window_days: int = 30) -> dict:
    """Weak patterns + the last 7 days of misses WITH their original questions.
    Monday ritual: re-ask recent_misses (shuffled, lightly reworded) before any
    new material — error-focused review has outsized retention returns."""
    from .weak_patterns import compute_weak_patterns
    return compute_weak_patterns(window_days=window_days).model_dump()


def set_default_training_phase_tool(default_training_phase: str) -> dict:
    set_default_training_phase(default_training_phase)
    return {"ok": True, "default_training_phase": default_training_phase}


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
    mcp.tool()(search_clinical_sources)
    mcp.tool()(answer_from_clinical_sources)
    mcp.tool()(start_study_session)
    mcp.tool()(submit_study_answer)
    mcp.tool()(get_due_reviews)
    mcp.tool()(get_student_dashboard)
    mcp.tool()(log_missed_topic)
    mcp.tool(name="submit_knowledge_points")(submit_knowledge_points)
    mcp.tool(name="get_knowledge_points")(get_knowledge_points)
    mcp.tool(name="get_due_knowledge_points")(get_due_knowledge_points)
    mcp.tool(name="get_knowledge_gaps")(get_knowledge_gaps)
    mcp.tool(name="get_illness_script")(get_illness_script)
    mcp.tool(name="set_illness_script")(set_illness_script)
    mcp.tool(name="get_contrastive_case")(get_contrastive_case)
    mcp.tool(name="add_confusable_pair")(add_confusable_pair)
    mcp.tool(name="mark_topic_mastered")(mark_topic_mastered_tool)
    mcp.tool(name="set_default_training_phase")(set_default_training_phase_tool)
    # Phase 1: New MCP endpoints
    mcp.tool(name="mcp_retrieval")(mcp_retrieval)
    mcp.tool(name="get_session_state")(get_session_state)
    mcp.tool(name="get_next_topic")(get_next_topic)
    mcp.tool(name="submit_answer")(submit_answer)
    mcp.tool(name="get_mastery_gates")(get_mastery_gates)
    mcp.tool(name="get_progress")(get_progress)
    # Curriculum coverage tools
    mcp.tool(name="get_mastery_map")(get_mastery_map)
    mcp.tool(name="get_calibration_report")(get_calibration_report)
    mcp.tool(name="get_mistake_review")(get_mistake_review)
    mcp.tool(name="set_medicine_weight")(set_medicine_weight_tool)
    # Dosing-drill tools (CPU-only calc engine — no corpus/Chroma access)
    mcp.tool(name="get_dosing_drill")(get_dosing_drill)
    mcp.tool(name="submit_dosing_answer")(submit_dosing_answer)
    mcp.tool(name="get_due_dosing_drills")(get_due_dosing_drills)

    # Best-effort dosing rules seeding
    _dosing_blueprint = Path(__file__).parent.parent / "data" / "dosing_rules.json"
    if _dosing_blueprint.exists():
        try:
            from .dosing_engine import seed_dosing_rules as _seed_dosing
            _seed_dosing(str(_dosing_blueprint))
        except Exception as _e:
            print(f"[startup] dosing rules seed skipped: {_e}", flush=True)

    # Best-effort KP catalog seeding (file generated separately — may not exist yet)
    mcp.tool(name="get_kp_to_study")(get_kp_to_study)
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
