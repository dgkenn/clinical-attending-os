from __future__ import annotations

import os
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.security import APIKeyHeader

from .case_prep import case_prep
from .config import settings
from .curriculum import load_curriculum, _band_for_unit
from .follow_up import answer_follow_up
from .retrieval import hybrid_search, retrieval_confidence
from .schemas import (
    AddConfusablePairRequest,
    CarNextRequest,
    AnswerRequest,
    AnswerResponse,
    CA1CoverageResponse,
    CasePrepRequest,
    CasePrepResponse,
    FollowUpRequest,
    FollowUpResponse,
    HealthResponse,
    KnowledgePointInput,
    LogMissedTopicRequest,
    MarkTopicRequest,
    OkResponse,
    SetDefaultPhaseResponse,
    SetIllnessScriptRequest,
    SetMedicineWeightRequest,
    SourceCoverageResponse,
    StudentDashboardResponse,
    SubmitAnswerFSRSRequest,
    SubmitDosingAnswerRequest,
    SubmitKnowledgePointsRequest,
    SystemInstructionsResponse,
    TeachingModeRequest,
    TeachingModeResponse,
    NextLessonRequest,
    NextLessonResponse,
    ProgressResponse,
    SearchRequest,
    SearchResponse,
    SetDefaultPhaseRequest,
    StartSessionRequest,
    StartSessionResponse,
    TutorRequest,
    TutorResponse,
    WeakPatternsResponse,
)
from .weak_patterns import compute_weak_patterns
from .session_runner import next_lesson as runner_next_lesson, start_voice_session
from .student_model import (
    conn,
    get_ca1_coverage,
    get_due_reviews,
    get_source_coverage,
    get_student_dashboard,
    initialize_database,
    mark_topic_mastered,
    mark_topic_weak,
    set_default_training_phase,
)
from .tutor_engine import (
    answer_query,
    evaluate_user_answer,
    is_basics_exam_query,
    record_evaluated_answer,
    start_session,
)
# Parity layer: import the SAME plain functions the MCP server (src/mcp_server.py)
# registers as tools, so Claude (via MCP) and ChatGPT (via these HTTP routes) drive
# identical code paths against the identical SQLite state — no divergent logic to
# keep in sync, no risk of the two front ends disagreeing about what happened.
from .mcp_endpoints import (
    get_session_state as _get_session_state,
    get_next_topic as _get_next_topic,
    submit_answer as _submit_answer_fsrs,
    get_mastery_gates as _get_mastery_gates,
    get_mastery_map as _get_mastery_map,
    get_progress as _get_discipline_progress,
    set_medicine_weight_tool as _set_medicine_weight_tool,
    get_kp_to_study as _get_kp_to_study,
)
from .mcp_server import (
    submit_knowledge_points as _submit_knowledge_points,
    get_knowledge_points as _get_knowledge_points,
    get_due_knowledge_points as _get_due_knowledge_points,
    get_knowledge_gaps as _get_knowledge_gaps,
    log_missed_topic as _log_missed_topic,
    get_illness_script as _get_illness_script,
    set_illness_script as _set_illness_script,
    get_contrastive_case as _get_contrastive_case,
    add_confusable_pair as _add_confusable_pair,
    get_dosing_drill as _get_dosing_drill,
    submit_dosing_answer as _submit_dosing_answer,
    get_due_dosing_drills as _get_due_dosing_drills,
)

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)
LOOPBACK_HOSTS = {"127.0.0.1", "localhost", "::1"}


def require_api_key(request: Request, x_api_key: str | None = Depends(api_key_header)) -> None:
    """Auth guard. Fail-closed when listening on a non-loopback host without an API_KEY."""
    if settings.api_key:
        import hmac as _hmac
        if not (x_api_key and _hmac.compare_digest(x_api_key, settings.api_key)):
            raise HTTPException(status_code=401, detail="Invalid API key")
        return
    client_host = (request.client.host if request.client else "") or ""
    if os.getenv("ALLOW_NO_API_KEY") == "1":
        return
    if client_host not in LOOPBACK_HOSTS:
        raise HTTPException(
            status_code=401,
            detail=(
                "API_KEY is unset and the request did not come from loopback. "
                "Set API_KEY in .env, or export ALLOW_NO_API_KEY=1 if you really intend to run open."
            ),
        )


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings.ensure_dirs()
    initialize_database()
    # Warm embedding model + chroma client + chunk index so the first user
    # query doesn't pay a 30s cold-start. Runs synchronously at startup.
    try:
        hybrid_search("warmup", mode="intern_teach", max_results=1, use_cross_encoder=False)
    except Exception:
        pass
    yield


app = FastAPI(title="Clinical Attending OS", version="0.2.0", lifespan=lifespan)


# Response shapes for the parity endpoints, which return plain dicts built at
# runtime rather than Pydantic models. FastAPI can only emit `{"type":"object"}`
# for those, and ChatGPT's Actions validator rejects that with "object schema
# missing properties". Declaring response_model= instead would make FastAPI
# FILTER the payload down to the declared fields, silently dropping data — so
# the shapes are documented here and patched into the schema only, leaving
# serialization untouched. Keys mirror the returning functions in
# mcp_endpoints.py / mcp_server.py; `additionalProperties` stays true so an
# undocumented key is never a lie.
_S = {"type": "string"}
_I = {"type": "integer"}
_N = {"type": "number"}
_B = {"type": "boolean"}
_O = {"type": "object"}
_A = {"type": "array", "items": {"type": "object"}}
_AS = {"type": "array", "items": {"type": "string"}}

_RESPONSE_SHAPES: dict[str, dict] = {
    "get_session_state": {
        "fsrs_due_today": _A, "weak_topics": _A, "mastery_matrix": _O, "load": _O,
        "due_knowledge_points": _A, "due_knowledge_points_count": _I,
        "open_knowledge_gaps": _A, "open_knowledge_gaps_count": _I,
        "phase": _S, "progress_pct": _N, "total_attempts": _I,
        "days_since_last_session": _I, "hours_since_last_session": _N,
        "attempts_today": _I, "session_id": _S,
    },
    "get_next_topic": {
        "topic": _S, "domain": _S, "discipline": _S, "is_critical_care": _B,
        "priority_tier": _I, "category": _S, "subtopics": _AS, "open_gaps": _AS,
        "reason": _S, "retrieval_query": _S, "suggested_phase": _S, "is_nested": _B,
        "new_items_today": _I, "daily_new_item_cap": _I, "message": _S,
    },
    "submit_answer": {
        "ok": _B, "next_review_date": _S, "mastery_updated": _B,
        "level_achieved": _S, "mastery_score": _N, "status": _S,
        "strategy_for_next": _S, "confidence_calibration": _S, "error": _S,
    },
    "get_mastery_map": {
        "total_curriculum_topics": _I, "topics_studied": _I, "coverage_pct": _N,
        "mastery_levels": _O, "knowledge_points": _O, "by_discipline": _O,
        "by_domain": _A, "critical_care": _O, "on_call_approaches": _O,
        "weakest_domains": _AS, "untouched_count": _I, "next_suggested_domain": _S,
    },
    "get_progress": {
        "intern_medicine_pct": _N, "icu_pct": _N, "anesthesia_pct": _N,
        "overall_pct": _N, "hours_studied": _N, "total_attempts": _I,
        "accuracy_overall": _N,
    },
    "set_medicine_weight": {"ok": _B, "medicine_weight": _N, "anesthesia_weight": _N},
    "submit_knowledge_points": {
        "ok": _B, "recorded": _I, "points": _A, "weak_or_learning": _AS,
    },
    "get_knowledge_points": {
        "points": _A, "count": _I, "weak_count": _I, "overconfident": _AS,
    },
    "get_due_knowledge_points": {"due_points": _A, "count": _I},
    "log_missed_topic": {"ok": _B, "topic": _S, "gap_logged": _B},
    "get_illness_script": {"found": _B, "script": _O},
    "set_illness_script": {"ok": _B, "topic": _S},
    "get_contrastive_case": {"topic": _S, "confusables": _A, "count": _I},
    "add_confusable_pair": {"ok": _B},
    "get_dosing_drill": {
        "drug": _S, "mode": _S, "context": _S, "question": _S, "answer": _S,
        "anchor": _S, "units": _S, "source": _S, "explanation": _S,
        "scenario_text": _S, "given": _O, "tolerance": _N, "worked_steps": _AS,
        "calc_type": _S, "error": _S,
    },
    "submit_dosing_answer": {
        "ok": _B, "topic": _S, "point": _S, "status": _S,
        "consecutive_correct": _I, "interval_days": _I, "next_review_date": _S,
        "error": _S,
    },
    "get_due_dosing_drills": {"due_dosing_points": _A, "count": _I},
    "car_next": {"recorded": _O, "next": _O, "queue": _O},
}


def _custom_openapi() -> dict:
    """Serve the OpenAPI schema with a `servers` entry pointing at the public
    base URL, and with concrete response shapes for the dict-returning parity
    endpoints. Without `servers`, a Custom GPT that imported the schema has no
    idea what host to call; without response `properties`, ChatGPT's Actions
    validator refuses the import. Mirrors the committed openapi.json."""
    if app.openapi_schema:
        return app.openapi_schema
    from fastapi.openapi.utils import get_openapi
    schema = get_openapi(
        title=app.title, version=app.version, routes=app.routes,
        description=app.description or None,
    )
    if settings.public_base_url:
        schema["servers"] = [{"url": settings.public_base_url}]

    for path_item in schema.get("paths", {}).values():
        for operation in path_item.values():
            if not isinstance(operation, dict):
                continue
            shape = _RESPONSE_SHAPES.get(operation.get("operationId", ""))
            if not shape:
                continue
            media = (
                operation.get("responses", {})
                .get("200", {})
                .get("content", {})
                .get("application/json", {})
            )
            # Only fill in the empty `{"type": "object"}` FastAPI emits for an
            # undeclared dict return — never clobber a real generated schema.
            if media.get("schema", {}).get("type") == "object" and "properties" not in media.get("schema", {}):
                media["schema"] = {
                    "type": "object",
                    "properties": shape,
                    "additionalProperties": True,
                }

    app.openapi_schema = schema
    return schema


app.openapi = _custom_openapi  # type: ignore[method-assign]


@app.get("/system_instructions", response_model=SystemInstructionsResponse, operation_id="getSystemInstructions")
def system_instructions() -> SystemInstructionsResponse:
    """Returns current GPT instructions text. Call once at conversation start."""
    import hashlib
    from pathlib import Path
    md_path = Path(__file__).resolve().parent.parent / "CUSTOM_GPT_INSTRUCTIONS.md"
    if not md_path.exists():
        return SystemInstructionsResponse(version="missing", instructions="")
    text = md_path.read_text(encoding="utf-8")
    version = hashlib.sha1(text.encode("utf-8")).hexdigest()[:12]
    return SystemInstructionsResponse(version=version, instructions=text)


@app.get("/health", response_model=HealthResponse, operation_id="health", include_in_schema=False)
def health() -> HealthResponse:
    return HealthResponse(
        ok=True,
        service="clinical_attending_os",
        backend_mode=settings.backend_mode,
        free_local_mode=settings.free_local_mode,
    )


@app.post("/tutor", response_model=TutorResponse, dependencies=[Depends(require_api_key)], operation_id="answer_from_clinical_sources")
def tutor(req: TutorRequest) -> TutorResponse:
    """Grounded answer to a mid-lesson follow-up question. Mirrors the MCP tool
    `answer_from_clinical_sources` exactly (same answer_query() call)."""
    return answer_query(req.query, req.mode, req.session_id)


@app.post("/start_session", response_model=StartSessionResponse, dependencies=[Depends(require_api_key)], operation_id="start_study_session")
def start(req: StartSessionRequest) -> dict:
    """Mirrors the MCP tool `start_study_session` exactly (same start_session() call)."""
    return start_session(req.duration_minutes, req.mode, req.focus_topic, req.training_phase)


@app.post("/answer", response_model=AnswerResponse, dependencies=[Depends(require_api_key)], operation_id="submit_study_answer")
def answer(req: AnswerRequest) -> dict:
    """Mirrors the MCP tool `submit_study_answer` exactly (same record_evaluated_answer()
    call). Do NOT also call /submit_answer_fsrs for the same answer: both paths
    end in log_attempt() -> update_mastery_score(), so the pair writes two
    attempt rows and advances FSRS twice. They are alternatives, not a pair
    (a same-answer duplicate within 3 minutes is now dropped server-side as a
    backstop, but don't rely on it)."""
    if req.result:
        return record_evaluated_answer(
            session_id=req.session_id,
            question=req.question,
            user_answer=req.user_answer,
            topic=req.topic,
            subtopic=req.subtopic or "",
            result=req.result,
            mistake_type=req.mistake_type or "other",
            ideal_answer=req.ideal_answer or "",
            difficulty=req.difficulty,
            hints_used=req.hints_used,
            confidence_reported=req.confidence_reported,
            retrieval_sources=req.retrieval_sources or "",
            source_citations=req.source_citations or req.retrieval_sources or "",
            notes=req.notes or "",
        )
    ideal = answer_query(req.question, "teach", req.session_id).answer
    return evaluate_user_answer(req.question, req.user_answer, ideal, req.topic, req.subtopic or "", req.session_id)


@app.post("/submit_answer", response_model=AnswerResponse, dependencies=[Depends(require_api_key)], operation_id="submitAnswer", include_in_schema=False)
def submit_answer(req: AnswerRequest) -> dict:
    if not req.result:
        raise HTTPException(status_code=400, detail="submit_answer requires Custom GPT-provided result and mistake_type.")
    return record_evaluated_answer(
        session_id=req.session_id,
        question=req.question,
        user_answer=req.user_answer,
        topic=req.topic,
        subtopic=req.subtopic or "",
        result=req.result,
        mistake_type=req.mistake_type or "other",
        ideal_answer=req.ideal_answer or "",
        difficulty=req.difficulty,
        hints_used=req.hints_used,
        confidence_reported=req.confidence_reported,
        retrieval_sources=req.retrieval_sources or "",
        source_citations=req.source_citations or req.retrieval_sources or "",
        notes=req.notes or "",
        phase=req.phase,
    )


@app.get("/due_reviews", dependencies=[Depends(require_api_key)], operation_id="getDueReviews")
def due_reviews() -> list[dict]:
    return get_due_reviews()


@app.get("/student_dashboard", response_model=StudentDashboardResponse, dependencies=[Depends(require_api_key)], operation_id="getStudentDashboard", include_in_schema=False)
def student_dashboard() -> dict:
    return get_student_dashboard()


@app.get("/ca1_coverage", response_model=CA1CoverageResponse, dependencies=[Depends(require_api_key)], operation_id="getCA1Coverage", include_in_schema=False)
def ca1_coverage() -> dict:
    return get_ca1_coverage()


@app.get("/source_coverage", response_model=SourceCoverageResponse, dependencies=[Depends(require_api_key)], operation_id="getSourceCoverage", include_in_schema=False)
def source_coverage() -> dict:
    return get_source_coverage()


@app.post("/mark_mastered", response_model=OkResponse, dependencies=[Depends(require_api_key)], operation_id="markMastered")
def mastered(req: MarkTopicRequest) -> OkResponse:
    mark_topic_mastered(req.topic, req.subtopic)
    return OkResponse(ok=True)


@app.post("/mark_weak", response_model=OkResponse, dependencies=[Depends(require_api_key)], operation_id="markWeak", include_in_schema=False)
def weak(req: MarkTopicRequest) -> OkResponse:
    mark_topic_weak(req.topic, req.subtopic)
    return OkResponse(ok=True)


@app.post("/set_default_phase", response_model=SetDefaultPhaseResponse, dependencies=[Depends(require_api_key)], operation_id="setDefaultPhase", include_in_schema=False)
def set_default_phase(req: SetDefaultPhaseRequest) -> SetDefaultPhaseResponse:
    set_default_training_phase(req.default_training_phase)
    return SetDefaultPhaseResponse(ok=True, default_training_phase=req.default_training_phase)


@app.post("/next_lesson", response_model=NextLessonResponse, dependencies=[Depends(require_api_key)], operation_id="nextLesson", include_in_schema=False)
def next_lesson(req: NextLessonRequest) -> NextLessonResponse:
    session = req.session or start_voice_session()
    lesson, new_session = runner_next_lesson(session)
    return NextLessonResponse(lesson=lesson, session=new_session)


@app.get("/progress", response_model=ProgressResponse, dependencies=[Depends(require_api_key)], operation_id="getProgress", include_in_schema=False)
def progress() -> ProgressResponse:
    initialize_database()
    curriculum = load_curriculum()
    by_band: dict[str, dict[str, int]] = {}
    for u in curriculum:
        band = _band_for_unit(u)
        by_band.setdefault(band, {"total": 0, "completed": 0})
        by_band[band]["total"] += 1
    with conn() as db:
        completed_rows = db.execute(
            "SELECT topic FROM topics WHERE topic LIKE 'unit:%' AND mastery_score >= 0.6 AND times_seen >= 1"
        ).fetchall()
        weakest = db.execute(
            "SELECT topic, subtopic, mastery_score, next_review_date FROM topics ORDER BY mastery_score ASC LIMIT 10"
        ).fetchall()
    completed_ids = {r["topic"][len("unit:"):] for r in completed_rows}
    n_completed = 0
    for u in curriculum:
        if u.unit_id in completed_ids:
            band = _band_for_unit(u)
            by_band.setdefault(band, {"total": 0, "completed": 0})
            by_band[band]["completed"] += 1
            n_completed += 1
    return ProgressResponse(
        n_units=len(curriculum),
        n_completed=n_completed,
        pct_complete=(n_completed / len(curriculum)) if curriculum else 0.0,
        by_band=by_band,
        weakest_topics=[dict(r) for r in weakest],
    )


@app.post("/case_prep", response_model=CasePrepResponse, dependencies=[Depends(require_api_key)], operation_id="casePrep")
def case_prep_endpoint(req: CasePrepRequest) -> CasePrepResponse:
    return case_prep(req.case_stem, duration_minutes=req.duration_minutes)


@app.post("/teaching_mode", response_model=TeachingModeResponse, dependencies=[Depends(require_api_key)], operation_id="startTeachingMode")
def teaching_mode_endpoint(req: TeachingModeRequest) -> TeachingModeResponse:
    """User teaches the GPT (protégé effect). Returns probe seeds + grounded sources + rubric."""
    from .teaching_mode import start_teaching_session
    return TeachingModeResponse(**start_teaching_session(req.topic, req.mode_hint))


@app.post("/follow_up", response_model=FollowUpResponse, dependencies=[Depends(require_api_key)], operation_id="followUp")
def follow_up_endpoint(req: FollowUpRequest) -> FollowUpResponse:
    return FollowUpResponse(**answer_follow_up(
        question=req.question,
        lesson_topic=req.lesson_topic,
        mode_hint=req.mode_hint,
    ))


@app.get("/weak_patterns", response_model=WeakPatternsResponse, dependencies=[Depends(require_api_key)], operation_id="getWeakPatterns")
def weak_patterns_endpoint(window_days: int = 30) -> WeakPatternsResponse:
    return compute_weak_patterns(window_days=window_days)


@app.post("/search", response_model=SearchResponse, dependencies=[Depends(require_api_key)], operation_id="searchSources")
def search(req: SearchRequest) -> SearchResponse:
    retrieval_mode = req.mode or ("basics_exam" if is_basics_exam_query(req.query) else "intern_teach")
    results, insufficient = hybrid_search(
        req.query,
        mode=retrieval_mode,
        source_filter=req.source_filter,
        topic_filter=req.topic_filter,
        library_filter=req.library_filter,
        training_phase=req.training_phase,
        clinical_context=req.clinical_context,
        max_results=req.max_results,
    )
    return SearchResponse(query=req.query, retrieval_confidence=retrieval_confidence(results), insufficient_context=insufficient, results=results)


# ---------------------------------------------------------------------------
# Parity endpoints — same functions the MCP server exposes as tools (imported
# above from mcp_endpoints/mcp_server), just wrapped as HTTP routes so the
# Custom GPT connector has the same capabilities as Claude's MCP connector.
# ---------------------------------------------------------------------------

@app.get("/session_state", dependencies=[Depends(require_api_key)], operation_id="get_session_state")
def session_state() -> dict:
    return _get_session_state()


@app.get("/next_topic", dependencies=[Depends(require_api_key)], operation_id="get_next_topic")
def next_topic(session_id: str | None = None) -> dict:
    return _get_next_topic(session_id)


@app.post("/submit_answer_fsrs", dependencies=[Depends(require_api_key)], operation_id="submit_answer")
def submit_answer_fsrs(req: SubmitAnswerFSRSRequest) -> dict:
    return _submit_answer_fsrs(
        topic=req.topic,
        user_answer=req.user_answer,
        question=req.question,
        is_correct=req.is_correct,
        confidence_reported=req.confidence_reported,
        teach_back_quality=req.teach_back_quality,
        mistake_type=req.mistake_type,
        subtopic=req.subtopic,
        transfer_success=req.transfer_success,
        bloom_level=req.bloom_level,
        session_id=req.session_id,
    )


@app.get("/mastery_gates", dependencies=[Depends(require_api_key)], operation_id="get_mastery_gates", include_in_schema=False)
def mastery_gates() -> dict:
    return _get_mastery_gates()


@app.get("/mastery_map", dependencies=[Depends(require_api_key)], operation_id="get_mastery_map")
def mastery_map() -> dict:
    return _get_mastery_map()


@app.get("/discipline_progress", dependencies=[Depends(require_api_key)], operation_id="get_progress")
def discipline_progress() -> dict:
    """Medicine/ICU/anesthesia % breakdown — the MCP tool `get_progress`. Distinct
    from GET /progress (operation_id getProgress), which reports curriculum-unit
    band completion; both exist, ask for whichever you need."""
    return _get_discipline_progress()


@app.post("/medicine_weight", dependencies=[Depends(require_api_key)], operation_id="set_medicine_weight")
def medicine_weight(req: SetMedicineWeightRequest) -> dict:
    return _set_medicine_weight_tool(req.weight, rotation=req.rotation)


@app.get("/kp_to_study", dependencies=[Depends(require_api_key)], operation_id="get_kp_to_study")
def kp_to_study(limit: int = 10, discipline: str = "", topic: str = "", format: str = "") -> list:
    return _get_kp_to_study(limit=limit, discipline=discipline, topic=topic, format=format)


@app.post("/knowledge_points/submit", dependencies=[Depends(require_api_key)], operation_id="submit_knowledge_points")
def knowledge_points_submit(req: SubmitKnowledgePointsRequest) -> dict:
    return _submit_knowledge_points(req.topic, [p.model_dump() for p in req.points])


@app.get("/knowledge_points", dependencies=[Depends(require_api_key)], operation_id="get_knowledge_points")
def knowledge_points_get(topic: str = "", status: str = "", due_only: bool = False) -> dict:
    return _get_knowledge_points(topic=topic, status=status, due_only=due_only)


@app.get("/knowledge_points/due", dependencies=[Depends(require_api_key)], operation_id="get_due_knowledge_points")
def knowledge_points_due(limit: int = 25, car: bool = False) -> dict:
    return _get_due_knowledge_points(limit=limit, car=car)


@app.get("/knowledge_gaps", dependencies=[Depends(require_api_key)], operation_id="get_knowledge_gaps", include_in_schema=False)
def knowledge_gaps(topic: str = "", status: str = "open") -> dict:
    return _get_knowledge_gaps(topic=topic, status=status)


@app.post("/log_missed_topic", dependencies=[Depends(require_api_key)], operation_id="log_missed_topic")
def log_missed_topic_endpoint(req: LogMissedTopicRequest) -> dict:
    return _log_missed_topic(req.topic, req.subtopic, req.gap_note, req.mistake_type)


@app.get("/illness_script", dependencies=[Depends(require_api_key)], operation_id="get_illness_script")
def illness_script_get(topic: str) -> dict:
    return _get_illness_script(topic)


@app.post("/illness_script", dependencies=[Depends(require_api_key)], operation_id="set_illness_script")
def illness_script_set(req: SetIllnessScriptRequest) -> dict:
    return _set_illness_script(
        req.topic, req.enabling_conditions, req.pathophysiology, req.time_course,
        req.key_features, req.consequence_if_missed, req.discipline, req.source,
    )


@app.get("/contrastive_case", dependencies=[Depends(require_api_key)], operation_id="get_contrastive_case")
def contrastive_case(topic: str) -> dict:
    return _get_contrastive_case(topic)


@app.post("/confusable_pair", dependencies=[Depends(require_api_key)], operation_id="add_confusable_pair")
def confusable_pair(req: AddConfusablePairRequest) -> dict:
    return _add_confusable_pair(req.topic_a, req.topic_b, req.discriminator)


@app.get("/dosing_drill", dependencies=[Depends(require_api_key)], operation_id="get_dosing_drill")
def dosing_drill(category: str = "", discipline: str = "", drug: str = "", mode: str = "auto") -> dict:
    return _get_dosing_drill(category=category, discipline=discipline, drug=drug, mode=mode)


@app.post("/dosing_drill/submit", dependencies=[Depends(require_api_key)], operation_id="submit_dosing_answer")
def dosing_drill_submit(req: SubmitDosingAnswerRequest) -> dict:
    return _submit_dosing_answer(
        drug=req.drug, is_correct=req.is_correct, confidence=req.confidence,
        calc_type=req.calc_type, mode=req.mode,
    )


@app.get("/dosing_drill/due", dependencies=[Depends(require_api_key)], operation_id="get_due_dosing_drills")
def dosing_drill_due(limit: int = 10) -> dict:
    return _get_due_dosing_drills(limit=limit)


@app.post("/car/next", dependencies=[Depends(require_api_key)], operation_id="car_next")
def car_next(req: CarNextRequest) -> dict:
    """ONE round trip per hands-free item: records the answer just given AND
    returns the next ear-friendly item.

    Latency, not backend speed, is what kills car mode. The backend answers a
    car-mode query in ~40 ms over the network, but each separate tool call costs
    a full model round trip (seconds). Doing this the granular way —
    get_due_knowledge_points -> submit_knowledge_points -> submit_answer ->
    get_kp_to_study — is four of those per question. This collapses them to one.

    It also makes the always-submit rule structural rather than advisory: the
    answer is recorded by the same call that fetches the next item, so a tutor
    that keeps asking questions cannot silently stop recording them.

    Selection order mirrors the car-mode rules: overdue knowledge points first
    (they decay), then unseen catalog KPs, then a dosing recall drill.
    """
    recorded = None
    if req.answered is not None:
        a = req.answered
        from .topic_resolver import resolve_topic as _resolve_topic
        a.topic = _resolve_topic(a.topic)[0]
        recorded = _submit_knowledge_points(
            a.topic,
            [{"point": a.point, "correct": a.correct,
              "confidence": a.confidence, "mistake_type": a.mistake_type}],
        )
        # Credit every other fact the same verbal answer covered or missed —
        # an open-ended spoken response is usually a compound answer.
        for extra in (a.also_covered or []):
            try:
                r_extra = _submit_knowledge_points(
                    (extra.topic or a.topic),
                    [{"point": extra.point, "correct": extra.correct,
                      "confidence": extra.confidence,
                      "mistake_type": extra.mistake_type or a.mistake_type}],
                )
                recorded.setdefault("also_recorded", []).append(
                    {"point": extra.point[:80], "ok": r_extra.get("ok", False)})
            except Exception as exc:
                recorded.setdefault("also_recorded", []).append(
                    {"point": extra.point[:80], "error": str(exc)[:100]})
        if req.record_topic_level:
            try:
                recorded["topic_level"] = _submit_answer_fsrs(
                    topic=a.topic,
                    user_answer=a.user_answer or ("correct" if a.correct else "incorrect"),
                    question=a.point,  # in car mode the point/stem IS the question
                    is_correct=a.correct,
                    confidence_reported=a.confidence,
                    mistake_type=a.mistake_type,
                )
            except Exception as exc:  # never lose the KP record over a topic-level failure
                recorded["topic_level_error"] = str(exc)[:200]

    # The answer is already recorded above; nothing past this point may turn
    # the response into an error, or the client retries and double-records
    # (two corrects = 'mastered'). Failures degrade to next=None.
    nxt = None
    queue = {"due_knowledge_points": 0, "due_dosing": 0}
    lite = (req.mode or "full").strip().lower() == "lite"
    try:
        # 1. Overdue knowledge points. Full mode serves ANY due point — the
        # tutor rephrases long/enumerated facts for the ear (chunked, signposted)
        # — so spaced repetition in the car covers the same queue as at a desk.
        # Lite keeps the old short-facts-only filter.
        due = _get_due_knowledge_points(limit=5, car=lite).get("due_points", [])
        if due:
            p = due[0]
            nxt = {
                "kind": "due_knowledge_point",
                "topic": p.get("topic", ""),
                "prompt": p.get("point", ""),
                # Echo THIS back as answered.point — for due KPs the point text
                # is its own key.
                "point_key": p.get("point", ""),
                "answer": "",  # the point text IS the fact; quiz on it directly
                "days_overdue": p.get("days_overdue", 0),
                "calibration": p.get("calibration"),
                "status": p.get("status"),
                # 3+ consecutive corrects: ask this as a NOVEL vignette, not
                # verbatim recall (transfer is the test of functional knowledge).
                "serve_as_transfer": p.get("serve_as_transfer", False),
            }
        # 2. Otherwise NEW material — breadth-first (triage ordering): with no
        # reviews due, the most valuable next item is one that maps unprobed
        # territory. Full mode drops the car_safe restriction (tutor verbalizes);
        # lite keeps it.
        if nxt is None:
            cat = _get_kp_to_study(limit=1, format="car" if lite else "triage")
            if cat:
                k = cat[0]
                nxt = {
                    "kind": "catalog_kp",
                    "topic": k.get("topic", ""),
                    "prompt": k.get("stem", ""),
                    "point_key": k.get("stem", ""),  # stem IS the point key
                    "answer": k.get("answer", ""),
                    "rationale": k.get("rationale", ""),
                    "source": k.get("source", ""),
                    "bloom": k.get("bloom", ""),
                }
        # 3. Otherwise a dosing recall drill (never a calculation in car mode).
        if nxt is None and req.include_dosing:
            d = _get_dosing_drill(mode="recall")
            if isinstance(d, dict) and not d.get("error"):
                drug = d.get("drug", "")
                nxt = {
                    "kind": "dosing_recall",
                    "topic": drug,
                    "prompt": d.get("question", ""),
                    # The canonical key the dosing graduation logic reads
                    # (_recall_status matches exactly 'dosing-recall:{drug}').
                    # Without it, car-recorded dosing answers landed under the
                    # question text and the drug stayed "unseen" forever.
                    "point_key": f"dosing-recall:{drug}",
                    "mistake_type_hint": "drug_dosing",
                    "answer": d.get("answer", ""),
                    "anchor": d.get("anchor", ""),
                    "source": d.get("source", ""),
                }
        queue = {
            "due_knowledge_points": _get_due_knowledge_points(limit=200, car=lite).get("count", 0),
            "due_dosing": _get_due_dosing_drills(limit=100).get("count", 0),
        }
    except Exception as exc:
        return {"recorded": recorded, "next": None, "queue": queue,
                "next_error": str(exc)[:200]}

    return {"recorded": recorded, "next": nxt, "queue": queue}
