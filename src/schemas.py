from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


TutorMode = Literal[
    "intern_teach",
    "cross_cover",
    "ICU_teach",
    "admission_plan",
    "wards_rounding",
    "rapid_response",
    "anesthesia_transition",
    "anesthesia_boards",
    "anesthesia_pimp",
    "teach",
    "pimp",
    "oral_boards",
    "rapid_review",
    "drug",
    "crisis",
    "OR_prep",
    "physiology",
    "missed_topic_review",
    "session_start",
    "mixed",
    "default",
]

AttemptResult = Literal["correct", "partial", "incorrect"]
MistakeType = Literal[
    "recall",
    "mechanism",
    "prioritization",
    "drug_dosing",
    "monitoring",
    "crisis_algorithm",
    "oral_boards_framing",
    "oral_presentation",
    "incomplete_answer",
    "overconfident_wrong",
    "failure_to_escalate",
    "differential_too_narrow",
    "pretest_unstudied",
    "critique_caught",
    "critique_missed",
    "other",
]


class SourceChunk(BaseModel):
    text: str
    excerpt: str = ""
    book: str = ""
    source_name: str = ""
    source: str = ""
    library: str = ""
    training_phase: str = ""
    clinical_context: str = ""
    filename: str = ""
    page: int | None = None
    section: str = ""
    topic_tags: list[str] = Field(default_factory=list)
    score: float = 0.0
    retrieval_method: str = ""
    vector_score: float | None = None
    bm25_score: float | None = None
    reranker_score: float | None = None
    chunk_id: str = ""


class TutorRequest(BaseModel):
    query: str
    mode: TutorMode = "teach"
    session_id: str | None = None


class TutorResponse(BaseModel):
    answer: str
    follow_up: str = ""
    sources: list[SourceChunk] = Field(default_factory=list)
    mode: str = "teach"
    retrieval_confidence: str = "low"
    insufficient_context: bool = False
    session_id: str | None = None


class StartSessionRequest(BaseModel):
    duration_minutes: int = 20
    mode: str = "default"
    training_phase: str | None = None
    focus_topic: str | None = None


class StartSessionResponse(BaseModel):
    session_id: str
    training_phase: str = "intern_year"
    plan: list[dict[str, Any]]
    rationale: str
    first_question: str
    retrieval_confidence: str = "low"
    insufficient_context: bool = False
    source_snippets: list[SourceChunk] = Field(default_factory=list)


class AnswerRequest(BaseModel):
    session_id: str = "voice"
    question: str
    user_answer: str
    topic: str
    # Echo back which lesson phase this answer is for, so the backend can
    # look up the exact cached teach material to return in the response.
    # If omitted, the backend falls back to "warm_up_retrieval".
    phase: str = "warm_up_retrieval"
    subtopic: str | None = None
    result: AttemptResult | None = None
    mistake_type: MistakeType | None = None
    ideal_answer: str | None = None
    difficulty: str = "medium"
    hints_used: int = 0
    confidence_reported: float | None = None
    retrieval_sources: str | None = None
    source_citations: str | None = None
    notes: str | None = None


class AnswerResponse(BaseModel):
    evaluation: str
    feedback: str
    ideal_answer: str
    ideal_answer_key_points: list[str] = Field(default_factory=list)
    mistake_type: str
    updated_mastery: float | None = None
    next_review_date: str | None = None
    source_snippets: list[SourceChunk] = Field(default_factory=list)
    next_question: str
    # Teach material for THIS just-submitted lesson — the GPT cannot get this
    # by guessing; it must call submitAnswer to receive it. This forces the
    # call-answer-call-answer pattern instead of freelancing from one
    # nextLesson response.
    mini_teach: str = ""
    teachback_prompt: str = ""
    citation: str = ""


class SearchRequest(BaseModel):
    query: str
    library_filter: str | None = None
    source_filter: str | None = None
    topic_filter: str | None = None
    training_phase: str | None = None
    clinical_context: str | None = None
    mode: str | None = None
    max_results: int = 8


class SearchResponse(BaseModel):
    query: str = ""
    retrieval_confidence: str = "low"
    insufficient_context: bool = False
    results: list[SourceChunk]


class SetDefaultPhaseRequest(BaseModel):
    default_training_phase: Literal["intern_year", "ICU", "anesthesia_transition", "anesthesia_boards"]


class MarkTopicRequest(BaseModel):
    topic: str
    subtopic: str = ""


class FollowUpRequest(BaseModel):
    question: str
    lesson_topic: str | None = None
    mode_hint: str | None = None


class FollowUpAnswerSentence(BaseModel):
    text: str
    book: str
    page: int | None = None
    matched_terms: list[str] = Field(default_factory=list)


class FollowUpResponse(BaseModel):
    question: str
    lesson_topic: str = ""
    queries_tried: list[str] = Field(default_factory=list)
    modes_tried: list[str] = Field(default_factory=list)
    answer_sentences: list[FollowUpAnswerSentence] = Field(default_factory=list)
    top_chunks: list[SourceChunk] = Field(default_factory=list)
    confidence: str = "low"
    insufficient_context: bool = True


class VoiceLesson(BaseModel):
    unit_id: str
    phase: str
    topic: str
    question: str
    expected_answer_short: str
    mini_teach: str
    teachback_prompt: str
    citation: str
    book: str
    page: int = 0
    relevance_hook: str = ""
    confidence_check: str = ""


class CasePrepRequest(BaseModel):
    case_stem: str
    duration_minutes: int = 5


class CasePrepTopic(BaseModel):
    topic: str
    why: str
    sources: list[SourceChunk] = Field(default_factory=list)


class CasePrepResponse(BaseModel):
    case_stem: str
    review_topics: list[CasePrepTopic]
    rationale: str = ""


class WeakPatternEntry(BaseModel):
    topic: str
    mistake_type: str
    failures: int
    last_seen: str | None = None


class HealthResponse(BaseModel):
    ok: bool
    service: str
    backend_mode: str
    free_local_mode: bool


class SystemInstructionsResponse(BaseModel):
    """Full GPT-side instruction text + a stable version hash. The Custom GPT
    calls this on every NEW conversation to get the latest behavior, instead
    of having to re-paste the markdown into ChatGPT every time we change it."""
    version: str
    instructions: str


class TeachingModeRequest(BaseModel):
    topic: str
    mode_hint: str | None = None


class TeachingModeResponse(BaseModel):
    """Protégé-mode scaffolding: the GPT plays a confused MS3 asking probing
    questions while the user teaches the topic. Source-grounded so the GPT's
    questions stay anchored in real material."""
    topic: str
    probe_seeds: list[str] = Field(default_factory=list)
    sources: list[SourceChunk] = Field(default_factory=list)
    coverage_rubric: list[str] = Field(default_factory=list)
    instructions_for_gpt: str


class OkResponse(BaseModel):
    ok: bool = True
    detail: str = ""


class SetDefaultPhaseResponse(BaseModel):
    ok: bool = True
    default_training_phase: str


class TopicSummary(BaseModel):
    status: str = ""
    n: int = 0
    avg_mastery: float | None = None


class WeakTopic(BaseModel):
    topic: str
    subtopic: str = ""
    mastery_score: float | None = None
    next_review_date: str | None = None


class StudentDashboardResponse(BaseModel):
    summary: list[TopicSummary] = Field(default_factory=list)
    weakest_topics: list[WeakTopic] = Field(default_factory=list)


class CoverageTarget(BaseModel):
    target_id: str = ""
    topic: str = ""
    subtopic: str = ""
    fact: str = ""
    page: int | None = None
    status: str = "new"
    mastery_score: float = 0.0
    times_seen: int = 0
    next_review_date: str | None = None
    covered: bool = False


class CA1CoverageResponse(BaseModel):
    source: str = "Stanford CA-1"
    granularity: str = "fact"
    total_topics: int = 0
    total_facts: int = 0
    covered_topics: int = 0
    remaining_topics: int = 0
    covered_facts: int = 0
    remaining_facts: int = 0
    coverage_percent: float = 0.0
    next_targets: list[CoverageTarget] = Field(default_factory=list)
    targets: list[CoverageTarget] = Field(default_factory=list)


class SourceCoverageSummary(BaseModel):
    source: str
    total_facts: int = 0
    covered_facts: int = 0
    remaining_facts: int = 0
    coverage_percent: float = 0.0


class SourceCoverageResponse(BaseModel):
    granularity: str = "fact"
    source_summaries: list[SourceCoverageSummary] = Field(default_factory=list)
    next_targets: list[CoverageTarget] = Field(default_factory=list)


class RecentMiss(BaseModel):
    """A wrong/partial answer with the ORIGINAL question, for mistake review.
    (Question text is only available for attempts recorded after 2026-08-15,
    when the submit path started storing it.)"""
    date: str
    topic: str
    question: str
    user_answer: str
    result: str
    mistake_type: str = "other"


class WeakPatternsResponse(BaseModel):
    by_mistake_type: dict[str, int] = Field(default_factory=dict)
    repeat_offenders: list[WeakPatternEntry] = Field(default_factory=list)
    rolling_30d_attempts: int = 0
    overconfidence_rate: float = 0.0
    # Last 7 days of non-correct attempts, newest first — the Monday
    # mistake-review queue. Re-ask these (shuffled, reworded) before new
    # material at the start of the week.
    recent_misses: list[RecentMiss] = Field(default_factory=list)


class NextLessonRequest(BaseModel):
    session: dict[str, Any] = Field(default_factory=dict)
    voice_mode: bool = True


class NextLessonResponse(BaseModel):
    lesson: VoiceLesson
    session: dict[str, Any] = Field(default_factory=dict)


class ProgressResponse(BaseModel):
    n_units: int
    n_completed: int
    pct_complete: float
    by_band: dict[str, dict[str, int]]
    weakest_topics: list[dict[str, Any]] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# Parity endpoints — mirror the MCP tool surface (src/mcp_endpoints.py,
# src/mcp_server.py) over HTTP for the Custom GPT connector. Field names and
# defaults match the corresponding MCP tool signature exactly so the two
# front ends (Claude via MCP, ChatGPT via these HTTP actions) stay behaviorally
# identical — see CUSTOM_GPT_INSTRUCTIONS.md / CLAUDE_PROJECT_INSTRUCTIONS.md.
# ---------------------------------------------------------------------------

class SubmitAnswerFSRSRequest(BaseModel):
    topic: str
    user_answer: str
    # The actual question asked — REQUIRED in spirit (kept optional for
    # backward compat). Without it the attempt log cannot support
    # mistake-review or bad-question analytics.
    question: str = ""
    is_correct: bool
    confidence_reported: int = 3
    teach_back_quality: float = 0.5
    mistake_type: MistakeType = "other"
    subtopic: str = ""
    transfer_success: bool = False
    bloom_level: str = ""
    session_id: str | None = None


class KnowledgePointInput(BaseModel):
    point: str
    correct: bool
    confidence: int | None = None
    mistake_type: MistakeType = "other"


class SubmitKnowledgePointsRequest(BaseModel):
    topic: str
    points: list[KnowledgePointInput] = Field(default_factory=list)


class SetMedicineWeightRequest(BaseModel):
    weight: float = 0.8
    # Optional: also set the current rotation ("wards", "ICU", "cardiology",
    # "anesthesia", ...) — new-topic picks then prefer matching domains.
    # "" clears it; omit to leave unchanged. Shares this endpoint to stay
    # under ChatGPT's 30-operation Actions cap.
    rotation: str | None = None


class LogMissedTopicRequest(BaseModel):
    topic: str
    subtopic: str = ""
    gap_note: str = ""
    mistake_type: MistakeType = "other"


class SetIllnessScriptRequest(BaseModel):
    topic: str
    enabling_conditions: str = ""
    pathophysiology: str = ""
    time_course: str = ""
    key_features: str = ""
    consequence_if_missed: str = ""
    discipline: str = ""
    source: str = ""


class AddConfusablePairRequest(BaseModel):
    topic_a: str
    topic_b: str
    discriminator: str = ""


class SubmitDosingAnswerRequest(BaseModel):
    drug: str
    is_correct: bool
    confidence: int = 3
    calc_type: str = ""
    mode: str = "recall"


class CarAlsoCovered(BaseModel):
    """An ADDITIONAL fact the same open-ended verbal answer covered (or
    conspicuously missed), OR a misconception it revealed. Open-ended spoken
    prompts routinely resolve several knowledge points in one breath — each
    deserves its own credit, its own error type, and its own schedule."""
    point: str
    topic: str = ""  # defaults to the main answered.topic
    correct: bool = True
    confidence: int = 3
    # For misconceptions caught mid-ramble ("morphine is renally cleared"):
    # correct=false with the point phrased as the CORRECTED fact, and the
    # mistake_type that fits (mechanism, drug_dosing, ...).
    mistake_type: MistakeType = "other"


class CarAnsweredInput(BaseModel):
    """The item just answered, submitted together with the request for the next
    one so a hands-free turn costs a single round trip."""
    topic: str
    point: str
    correct: bool
    confidence: int = 3
    mistake_type: MistakeType = "other"
    user_answer: str = ""
    # Other facts this same verbal answer demonstrated (correct=true) or
    # conspicuously missed (correct=false). Recorded as knowledge points in
    # the same round trip.
    also_covered: list[CarAlsoCovered] = Field(default_factory=list)


class CarNextRequest(BaseModel):
    answered: CarAnsweredInput | None = None
    # "full" (default): the complete learning experience in audio form — due
    # reviews (any length; the tutor rephrases for the ear), then breadth-first
    # NEW material with teach content, transfer flags honored. "lite": the old
    # short-facts-only review mode (choppy connection / heavy traffic).
    mode: str = "full"
    # Also advance the parent topic's schedule, not just the knowledge point's.
    # These are two independent schedules, so doing both is correct — unlike
    # calling submit_answer and submit_study_answer, which both advance the
    # TOPIC schedule and double-count.
    record_topic_level: bool = True
    include_dosing: bool = True
