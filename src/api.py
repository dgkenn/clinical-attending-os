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
    AnswerRequest,
    AnswerResponse,
    CA1CoverageResponse,
    CasePrepRequest,
    CasePrepResponse,
    FollowUpRequest,
    FollowUpResponse,
    HealthResponse,
    MarkTopicRequest,
    OkResponse,
    SetDefaultPhaseResponse,
    SourceCoverageResponse,
    StudentDashboardResponse,
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


@app.post("/tutor", response_model=TutorResponse, dependencies=[Depends(require_api_key)], operation_id="tutor", include_in_schema=False)
def tutor(req: TutorRequest) -> TutorResponse:
    return answer_query(req.query, req.mode, req.session_id)


@app.post("/start_session", response_model=StartSessionResponse, dependencies=[Depends(require_api_key)], operation_id="startSession", include_in_schema=False)
def start(req: StartSessionRequest) -> dict:
    return start_session(req.duration_minutes, req.mode, req.focus_topic, req.training_phase)


@app.post("/answer", response_model=AnswerResponse, dependencies=[Depends(require_api_key)], operation_id="answerLegacy", include_in_schema=False)
def answer(req: AnswerRequest) -> dict:
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
