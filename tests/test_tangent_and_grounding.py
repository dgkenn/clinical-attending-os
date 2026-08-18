"""Two failures the digoxin session exposed.

1. GROUNDING. Retrieval was being skipped almost entirely — 0 calls across 22
   answers on 2026-08-17, 1 across 13 on 2026-08-18 — so questions came from
   model training rather than the corpus. They read as clinically sound, which
   is what makes it dangerous: nothing looks wrong and nothing is citable. Two
   rounds of instruction changes failed to fix it, so get_next_topic now ships
   the passages with the topic and grounding needs no second call.

2. TANGENTS. A self-directed digoxin rabbit hole ran a whole session and left
   zero trace — no attempt, no fact. That is the most engaged learning the user
   does and the only kind the system could not see. log_tangent captures it,
   but as EXPOSURE rather than knowledge: recording discussion as a correct
   answer would inflate mastery with things the user was merely told.
"""
from __future__ import annotations

import pytest

from src.config import settings
from src.mcp_server import _attach_sources, log_tangent
from src.student_model import conn

CHUNKS = settings.chroma_dir / "chunks.jsonl"
HAS_CORPUS = CHUNKS.exists() and CHUNKS.stat().st_size > 1000


@pytest.mark.skipif(not HAS_CORPUS, reason="corpus not ingested")
def test_next_topic_carries_its_own_grounding():
    out = _attach_sources({"topic": "Hyperkalemia", "retrieval_query": "hyperkalemia treatment"})
    assert out["sources"], "a served topic must arrive with passages"
    assert "retrieval_confidence" in out
    assert "sources_note" in out
    joined = " ".join(s["text"].lower() for s in out["sources"])
    assert any(t in joined for t in ("calcium", "insulin", "potassium"))


def test_attaching_sources_never_breaks_topic_selection():
    """Retrieval is a bonus on this call; it must not be able to fail it."""
    payload = {"topic": "", "retrieval_query": ""}
    assert _attach_sources(payload) == payload          # nothing to search for
    assert _attach_sources({"topic": "x"}) is not None
    assert _attach_sources("not a dict") == "not a dict"


def test_the_users_own_question_is_recorded_as_the_gap():
    """An unprompted question is the highest-quality gap signal available.

    A wrong answer only shows the user missed something the tutor chose to ask.
    A question they raise themselves shows they noticed the hole, cared enough
    to chase it, and usually met it on a real patient — nothing prompted it, so
    it reflects what they actually need. Previously it was recorded nowhere.
    """
    result = log_tangent(
        topic="Digoxin",
        question_asked="Why does hypokalemia make digoxin toxicity worse?",
        trigger="the heart failure potassium question",
        facts=["Digoxin and potassium compete for the same Na/K-ATPase site"],
    )
    assert result["ok"] is True
    assert result["question_logged"] is True
    assert result["recorded"] == 2      # the question itself, plus the fact
    with conn() as db:
        asked = db.execute(
            "SELECT point, times_correct, status FROM knowledge_points "
            "WHERE topic = 'Digoxin' AND point LIKE '[asked]%'").fetchall()
    assert asked, "the question the user asked must be recorded as a gap"
    assert "hypokalemia" in asked[0][0].lower()
    assert asked[0][1] == 0, "a question they had to ask is not a correct answer"
    assert asked[0][2] == "weak"


def test_tangent_without_a_question_still_captures_ground_covered():
    # Deliberately invented probe content. The original fixture used a real
    # digoxin pharmacology fact, which later became a genuine card when the
    # Strong Medicine afib video was ingested — the matcher then correctly
    # refused to write a duplicate and the test failed. A fixture asserting
    # "a new fact is written" must use content that is not real curriculum.
    result = log_tangent(
        topic="ProbeTangentTopic",
        facts=["Probe fixture fact: the fictional Zetamine receptor antagonist "
               "requires dose adjustment in probe-state hepatic clearance"],
    )
    assert result["question_logged"] is False
    assert result["recorded"] == 1


def test_exposure_is_never_counted_as_knowledge():
    """The whole point: the user heard it, they did not demonstrate it."""
    log_tangent(topic="Digoxin",
                question_asked="What causes bidirectional VT in digoxin toxicity?")
    with conn() as db:
        rows = db.execute(
            "SELECT times_correct, status FROM knowledge_points WHERE topic='Digoxin'"
        ).fetchall()
    assert rows
    assert all(r[0] == 0 for r in rows), "exposure must never be counted correct"
    assert all(r[1] == "weak" for r in rows), "unproven material must be weak"


def test_tangent_facts_are_deduped_not_stacked():
    """A tangent revisited across sessions must converge, not inflate the queue."""
    fact = "Digoxin toxicity classically causes visual disturbance and bidirectional VT"
    log_tangent(topic="Digoxin", facts=[fact])
    with conn() as db:
        before = db.execute(
            "SELECT COUNT(*) FROM knowledge_points WHERE topic='Digoxin'").fetchone()[0]
    log_tangent(topic="Digoxin", facts=[fact])
    with conn() as db:
        after = db.execute(
            "SELECT COUNT(*) FROM knowledge_points WHERE topic='Digoxin'").fetchone()[0]
    assert after == before


def test_fragments_are_rejected():
    """Free-text capture invites junk; a two-word 'fact' is not testable."""
    result = log_tangent(topic="Digoxin", facts=["short", "", "ok"])
    assert result["recorded"] == 0
    assert len(result["skipped"]) == 3


def test_due_facts_are_rationed_not_dumped():
    """The tutor once converted the whole backlog into '2-3 hours of reviews
    today'. Arithmetically true, terrible advice: the backlog was a one-time
    hump, FSRS schedules a late-correct fact weeks out, and a 3-hour demand
    kills the daily habit that makes spaced repetition work. The serving
    function now rations."""
    from src.mcp_server import get_due_knowledge_points
    r = get_due_knowledge_points()
    assert r["count"] <= 20, "todays_set must be a session, not a shift"
    assert r["backlog_total"] >= r["count"]
    assert r["carried"] == r["backlog_total"] - r["count"]
    assert r["estimated_minutes"] <= 30
    if r["carried"]:
        assert "NEVER quote the whole backlog" in r["note"]
    # weakest facts must come first — they are the known holes
    statuses = [p.get("status") for p in r["todays_set"]]
    if "weak" in statuses and "learning" in statuses:
        assert statuses.index("weak") < statuses.index("learning")


def test_bundles_group_related_reviews_without_crossing_topics():
    """User's proposal: related due REVIEWS share one vignette to cut review
    time. Rules: same topic only, real content overlap within the topic (the
    AKI-category facts bundle; DKA is not forced in with them), max 3 parts,
    and grading stays per-fact."""
    from src.mcp_server import get_due_knowledge_points
    r = get_due_knowledge_points()
    assert "bundles" in r
    total = sum(b["size"] for b in r["bundles"])
    assert total == r["count"], "every served fact appears in exactly one bundle"
    for b in r["bundles"]:
        assert 1 <= b["size"] <= 3
        topics = {f.get("topic") for f in b["facts"]}
        assert len(topics) == 1, f"bundle crosses topics: {topics}"
    # bundling must reduce the time estimate versus serial single questions
    assert r["estimated_minutes"] <= round(r["count"] * 1.5)


def test_long_intervals_get_deterministic_jitter():
    """Facts cleared together must not all come due together again — the
    single-day wave is what produced the '2-3 hours today' scare. Jitter is
    seeded by fact text: stable per fact, spread across facts."""
    import json
    import sqlite3
    from src.student_model import record_knowledge_point, conn

    # Seed mature cards: high stability so one correct earns a month-plus
    # interval, where jitter applies. Same-day repeat answers cannot build
    # that much stability, so the states are planted directly.
    mature = json.dumps({"stability": 30.0, "difficulty": 5.0, "reps": 4,
                         "lapses": 0, "state": "review",
                         "last_review": "2026-07-01T00:00:00+00:00",
                         "next_due": "2026-08-01T00:00:00+00:00"})
    with conn() as db:
        for i in range(8):
            db.execute(
                """INSERT INTO knowledge_points
                       (topic, point, status, times_seen, times_correct,
                        consecutive_correct, interval_days, fsrs_state,
                        next_review_date, created_at, updated_at)
                   VALUES ('JitterProbe', ?, 'learning', 3, 3, 3, 30, ?,
                           date('now'), CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)""",
                (f"jitter probe fact number {i} about a distinct clinical threshold",
                 mature))
    for i in range(8):
        record_knowledge_point(
            topic="JitterProbe",
            point=f"jitter probe fact number {i} about a distinct clinical threshold",
            is_correct=True, confidence=4)
    with conn() as db:
        rows = db.execute(
            "SELECT next_review_date, interval_days FROM knowledge_points "
            "WHERE topic='JitterProbe'").fetchall()
    assert all(r[1] >= 7 for r in rows), "cards must have reached jitter range"
    dates = {str(r[0])[:10] for r in rows}
    # 8 identical-history facts would land on ONE date without jitter.
    assert len(dates) >= 3, f"jitter failed to spread due dates: {dates}"


def test_a_fact_answered_today_is_not_served_again_today():
    """User report: "I'm reviewing the same cards multiple times a day."
    Root causes fixed together: scheduling ran on UTC days (from 8pm EDT the
    'day' had flipped, so afternoon answers came due the same evening), and
    nothing stopped a due-today fact from being served twice. Now the study
    day is the user's LOCAL day and a fact touched today is done for today."""
    from src.mcp_server import get_due_knowledge_points
    from src.student_model import record_knowledge_point

    point = "same-day guard probe: a distinctive clinical threshold fact"
    record_knowledge_point(topic="GuardProbe", point=point,
                           is_correct=False, confidence=2)  # wrong -> due soon
    served = {p["point"] for p in get_due_knowledge_points(limit=500)["todays_set"]}
    assert point not in served, "a fact answered today must not re-serve today"
