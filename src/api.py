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
        if x_api_key != settings.api_key:
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


def _custom_openapi() -> dict:
    """Serve the OpenAPI schema with a `servers` entry pointing at the public
    base URL. Without this, FastAPI emits no `servers` block and a Custom GPT
    that imported the schema from /openapi.json has no idea what host to call,
    so every action fails. Mirrors the committed openapi.json."""
    if app.openapi_schema:
        return app.openapi_schema
    from fastapi.openapi.utils import get_openapi
    schema = get_openapi(
        title=app.title, version=app.version, routes=app.routes,
        description=app.description or None,
    )
    if settings.public_base_url:
        schema["servers"] = [{"url": settings.public_base_url}]
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


@app.get("/health", response_model=HealthResponse, operation_id="health")
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
    call). Use alongside /submit_answer_fsrs (MCP tool `submit_answer`) — the FSRS/mastery
    engine — just like Claude calls both submit_study_answer and submit_answer."""
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


@app.post("/submit_answer", response_model=AnswerResponse, dependencies=[Depends(require_api_key)], operation_id="submitAnswer")
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


@app.get("/student_dashboard", response_model=StudentDashboardResponse, dependencies=[Depends(require_api_key)], operation_id="getStudentDashboard")
def student_dashboard() -> dict:
    return get_student_dashboard()


@app.get("/ca1_coverage", response_model=CA1CoverageResponse, dependencies=[Depends(require_api_key)], operation_id="getCA1Coverage")
def ca1_coverage() -> dict:
    return get_ca1_coverage()


@app.get("/source_coverage", response_model=SourceCoverageResponse, dependencies=[Depends(require_api_key)], operation_id="getSourceCoverage")
def source_coverage() -> dict:
    return get_source_coverage()


@app.post("/mark_mastered", response_model=OkResponse, dependencies=[Depends(require_api_key)], operation_id="markMastered")
def mastered(req: MarkTopicRequest) -> OkResponse:
    mark_topic_mastered(req.topic, req.subtopic)
    return OkResponse(ok=True)


@app.post("/mark_weak", response_model=OkResponse, dependencies=[Depends(require_api_key)], operation_id="markWeak")
def weak(req: MarkTopicRequest) -> OkResponse:
    mark_topic_weak(req.topic, req.subtopic)
    return OkResponse(ok=True)


@app.post("/set_default_phase", response_model=SetDefaultPhaseResponse, dependencies=[Depends(require_api_key)], operation_id="setDefaultPhase")
def set_default_phase(req: SetDefaultPhaseRequest) -> SetDefaultPhaseResponse:
    set_default_training_phase(req.default_training_phase)
    return SetDefaultPhaseResponse(ok=True, default_training_phase=req.default_training_phase)


@app.post("/next_lesson", response_model=NextLessonResponse, dependencies=[Depends(require_api_key)], operation_id="nextLesson")
def next_lesson(req: NextLessonRequest) -> NextLessonResponse:
    session = req.session or start_voice_session()
    lesson, new_session = runner_next_lesson(session)
    return NextLessonResponse(lesson=lesson, session=new_session)


@app.get("/progress", response_model=ProgressResponse, dependencies=[Depends(require_api_key)], operation_id="getProgress")
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
        is_correct=req.is_correct,
        confidence_reported=req.confidence_reported,
        teach_back_quality=req.teach_back_quality,
        mistake_type=req.mistake_type,
        subtopic=req.subtopic,
        transfer_success=req.transfer_success,
        bloom_level=req.bloom_level,
        session_id=req.session_id,
    )


@app.get("/mastery_gates", dependencies=[Depends(require_api_key)], operation_id="get_mastery_gates")
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
    return _set_medicine_weight_tool(req.weight)


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


@app.get("/knowledge_gaps", dependencies=[Depends(require_api_key)], operation_id="get_knowledge_gaps")
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
