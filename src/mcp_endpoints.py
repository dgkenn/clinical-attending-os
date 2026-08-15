"""
MCP Endpoints - 7 core tools for autonomous tutoring system

Tool 1: retrieval - Search knowledge base
Tool 2: get_session_state - Current learning state
Tool 3: get_next_topic - Next topic to study
Tool 4: submit_answer - Submit answer and update mastery
Tool 5: get_mastery_gates - Mastery matrix and phase gates
Tool 6: get_progress - Progress statistics
Tool 7: request_follow_up - Request follow-up on subtopic
"""

import json
import sqlite3
from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, List, Any
from pathlib import Path

from .retrieval import hybrid_search, retrieval_confidence
from .question_strategy import decide_question_strategy, select_question_layer, PerformanceContext, QuestionStrategy
from .lesson_planner import generate_lesson_plan, LessonMode
from .drill_decision import decide_drill_action, DrillContext, DrillDecision, estimate_mastery_time
from .student_model import conn, get_topic_summary, log_attempt, get_or_create_topic, get_due_reviews as _get_due_reviews, get_medicine_weight, set_medicine_weight as _set_medicine_weight, get_knowledge_points as _get_knowledge_points, get_due_knowledge_points as _get_due_knowledge_points, get_daily_new_item_cap, get_daily_review_budget, count_new_topics_today, initialize_database
from .fsrs import fsrs_review, deserialize, serialize, next_review_date_from_state
from .mastery_gates import compute_mastery_vector, update_mastery_in_db


# ============================================================================
# TOOL 1: RETRIEVAL - Search knowledge base
# ============================================================================

def retrieval(
    query: str,
    mode: str = "intern_teach",
    max_results: int = 8,
    library_filter: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Search knowledge base by query.

    Args:
        query: Search query
        mode: Retrieval mode (intern_teach, rapid_response, pimp, etc.)
        max_results: Max results to return
        library_filter: Filter by library/source

    Returns:
        {
            "results": [{"text": ..., "book": ..., "page": ..., "score": ...}, ...],
            "retrieval_confidence": float 0-1,
            "insufficient_context": bool
        }
    """
    try:
        sources, insufficient = hybrid_search(
            query,
            mode=mode,
            max_results=max_results,
            source_filter=library_filter
        )

        results = []
        for source in sources:
            results.append({
                "text": source.text[:500],  # Truncate for readability
                "book": source.book or source.filename or "Unknown",
                "page": source.page or 0,
                "section": source.section or "",
                "score": source.score or 0.0,
                "topic_tags": source.topic_tags or []
            })

        confidence_label = retrieval_confidence(sources)
        _confidence_map = {"low": 0.2, "medium": 0.6, "high": 0.9}
        confidence = _confidence_map.get(confidence_label, 0.0) if isinstance(confidence_label, str) else float(confidence_label)

        return {
            "results": results,
            "retrieval_confidence": confidence,
            "insufficient_context": insufficient,
            "total_results": len(results)
        }
    except Exception as e:
        print(f"Retrieval error: {e}")
        return {
            "results": [],
            "retrieval_confidence": 0.0,
            "insufficient_context": True,
            "error": str(e)
        }


# ============================================================================
# TOOL 2: SESSION STATE - Get current learning state
# ============================================================================

def get_session_state() -> Dict[str, Any]:
    """
    Get current student session state: FSRS due topics, weak areas, progress.

    Returns:
        {
            "fsrs_due_today": [{"topic_id": ..., "topic": ..., "reason": ...}, ...],
            "weak_topics": [{"topic": ..., "accuracy": ..., "last_seen": ...}, ...],
            "mastery_matrix": {"topic": {"level": ..., "vector": {...}}, ...},
            "phase": str (intern_year, ICU, anesthesia, etc.),
            "progress_pct": float 0-100,
            "total_attempts": int,
            "session_id": str
        }
    """
    try:
        with conn() as db:
            # Get FSRS due topics
            due_rows = db.execute("""
                SELECT DISTINCT topic FROM topics
                WHERE next_review_date IS NOT NULL
                AND next_review_date <= date('now')
                ORDER BY next_review_date ASC
                LIMIT 10
            """).fetchall()
            due_topics = [
                {"topic_id": f"topic_{row[0]}", "topic": row[0], "reason": "fsrs_due"}
                for row in due_rows
            ]
            # Full backlog count (the list above is a LIMIT-10 page; reporting
            # its len() as reviews_due_count told the tutor "10 due" when 200
            # were, so sessions under-budgeted review volume).
            due_total = db.execute("""
                SELECT COUNT(DISTINCT topic) FROM topics
                WHERE next_review_date IS NOT NULL
                AND next_review_date <= date('now')
            """).fetchone()[0]

            # Get weak topics (error rate > 30% in last 7 days)
            weak_rows = db.execute("""
                SELECT topic,
                       SUM(CASE WHEN result != 'correct' THEN 1 ELSE 0 END) as errors,
                       COUNT(*) as total,
                       MAX(date) as last_seen
                FROM question_attempts
                WHERE date >= date('now', '-7 days')
                GROUP BY topic
                HAVING (errors * 1.0 / total) > 0.30
                ORDER BY (errors * 1.0 / total) DESC
                LIMIT 5
            """).fetchall()
            weak_topics = [
                {
                    "topic": row[0],
                    "accuracy": 1.0 - (row[1] / row[2]) if row[2] > 0 else 0.0,
                    "error_count": row[1],
                    "total_attempts": row[2],
                    "last_seen": row[3] or ""
                }
                for row in weak_rows
            ]

            # Build mastery matrix from all topics; use mastery_vector table for
            # actual vector values (written by submit_answer after each attempt).
            topic_rows = db.execute("""
                SELECT DISTINCT topic FROM topics
                ORDER BY topic ASC
            """).fetchall()
            mv_rows = db.execute(
                "SELECT topic_name, accuracy, transfer_auc, mechanism_quality "
                "FROM mastery_vector"
            ).fetchall()
            mv_by_topic = {r["topic_name"]: r for r in mv_rows}

            _s2l = {
                "new": "baseline", "weak": "baseline", "unstable": "baseline",
                "learning": "intermediate", "strong": "intermediate",
                "maintenance": "advanced",
            }
            mastery_matrix = {}
            for (topic,) in topic_rows:
                summary = get_topic_summary(topic)
                raw_status = summary.get("status", "new")
                mv = mv_by_topic.get(topic)
                mastery_matrix[topic] = {
                    "level": _s2l.get(raw_status, "baseline"),
                    "mastery_score": round(summary.get("mastery_score", 0.0), 3),
                    "vector": {
                        "accuracy": float(mv["accuracy"]) if mv else 0.0,
                        "transfer_auc": float(mv["transfer_auc"]) if mv else 0.0,
                        "mechanism_quality": float(mv["mechanism_quality"]) if mv else 0.0,
                    }
                }

            # Get overall progress — use `status` column (topics table has no mastery_level)
            mastered_count = db.execute("""
                SELECT COUNT(DISTINCT topic) FROM topics
                WHERE status IN ('maintenance', 'strong', 'learning')
            """).fetchone()[0]

            total_count = db.execute(
                "SELECT COUNT(DISTINCT topic) FROM topics"
            ).fetchone()[0]

            progress_pct = (mastered_count / total_count * 100) if total_count > 0 else 0.0

            # Get total attempts
            total_attempts = db.execute(
                "SELECT COUNT(*) FROM question_attempts"
            ).fetchone()[0]

            # Time since last study activity + same-day activity (time-aware planning)
            last_row = db.execute("SELECT MAX(date) FROM question_attempts").fetchone()
            last_attempt = last_row[0] if last_row else None
            days_since_last_session = None
            hours_since_last_session = None
            if last_attempt:
                try:
                    last_dt = datetime.fromisoformat(last_attempt)
                    now = datetime.now(last_dt.tzinfo) if last_dt.tzinfo else datetime.now()
                    delta = now - last_dt
                    hours_since_last_session = round(delta.total_seconds() / 3600.0, 1)
                    days_since_last_session = delta.days
                except Exception:
                    pass
            try:
                from .student_model import local_day_start_utc_iso
                attempts_today = db.execute(
                    "SELECT COUNT(*) FROM question_attempts WHERE date >= ?",
                    (local_day_start_utc_iso(),),
                ).fetchone()[0]
            except Exception:
                attempts_today = 0

        # Atomic knowledge points due on their own schedule + weakest points — so a
        # fresh conversation re-drills exactly the specific facts that tripped the
        # student up, with their per-point calibration.
        try:
            _due_points = _get_due_knowledge_points(limit=25)
        except Exception:
            _due_points = []
        try:
            _weak_points = [p for p in _get_knowledge_points(status="weak", limit=25)]
        except Exception:
            _weak_points = []
        due_knowledge_points = [
            {"topic": p["topic"], "point": p["point"], "status": p["status"],
             "days_overdue": p.get("days_overdue", 0), "calibration": p.get("calibration")}
            for p in _due_points
        ]
        # Back-compat alias (older instructions referenced open_knowledge_gaps)
        open_knowledge_gaps = [
            {"topic": p["topic"], "gap_note": p["point"], "mistake_type": p.get("mistake_type", "other")}
            for p in _weak_points
        ]

        # Daily load economics — so the tutor paces new material and review volume.
        try:
            _new_today = count_new_topics_today()
            _new_cap = get_daily_new_item_cap()
            _review_budget = get_daily_review_budget()
        except Exception:
            _new_today, _new_cap, _review_budget = 0, 20, 200
        load = {
            "new_topics_today": _new_today,
            "daily_new_item_cap": _new_cap,
            "new_items_remaining_today": max(0, _new_cap - _new_today),
            "daily_review_budget": _review_budget,
            "reviews_due_count": due_total,
        }

        return {
            "fsrs_due_today": due_topics,
            "weak_topics": weak_topics,
            "mastery_matrix": mastery_matrix,
            "load": load,
            "due_knowledge_points": due_knowledge_points,
            "due_knowledge_points_count": len(due_knowledge_points),
            "open_knowledge_gaps": open_knowledge_gaps,
            "open_knowledge_gaps_count": len(open_knowledge_gaps),
            "phase": "intern_year",
            "progress_pct": progress_pct,
            "total_attempts": total_attempts,
            "days_since_last_session": days_since_last_session,
            "hours_since_last_session": hours_since_last_session,
            "attempts_today": attempts_today,
            "session_id": f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        }
    except Exception as e:
        print(f"Session state error: {e}")
        return {
            "fsrs_due_today": [],
            "weak_topics": [],
            "mastery_matrix": {},
            "phase": "intern_year",
            "progress_pct": 0.0,
            "total_attempts": 0,
            "error": str(e)
        }


# ============================================================================
# TOOL 3: NEXT TOPIC - Get next topic to study
# ============================================================================

def get_next_topic(session_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Determine the next topic to study based on FSRS due reviews and curriculum coverage.

    Priority order:
      1. FSRS due reviews (reason="due_review")
      2. Untouched curriculum topics, high-yield first (reason="new_coverage")
      3. Lesson-planner fallback (reason="due_today" | "weak")

    Returns:
        {
            "topic": str,
            "domain": str,
            "subtopics": list[str],
            "reason": str,
            "retrieval_query": str,
            "suggested_phase": str,
            "is_nested": bool
        }
    """
    # --- 1. Due reviews take priority ---
    try:
        due = _get_due_reviews(limit=1)
        if due:
            r = due[0]
            topic = r["topic"]
            # Try to enrich with curriculum metadata
            with conn() as db:
                crow = db.execute(
                    "SELECT domain, subtopics FROM curriculum WHERE topic=?", (topic,)
                ).fetchone()
            domain = crow["domain"] if crow else ""
            subtopics = json.loads(crow["subtopics"] or "[]") if crow else []
            # Resurface the SPECIFIC weak knowledge points on this topic so the tutor
            # re-targets them (still without telegraphing) instead of re-asking a
            # generic question. Not-yet-mastered points only.
            open_gaps = [p["point"] for p in _get_knowledge_points(topic=topic)
                         if p["status"] != "mastered"]
            return {
                "topic": topic,
                "domain": domain,
                "subtopics": subtopics,
                "open_gaps": open_gaps,
                "reason": "due_review",
                "retrieval_query": topic,
                "suggested_phase": "drilling",
                "is_nested": False,
            }
    except Exception:
        pass  # fall through

    # --- 2. Coverage-driven new topic from curriculum ---
    try:
        with conn() as db:
            # Has the curriculum table been seeded at all?
            curr_count = db.execute("SELECT COUNT(*) FROM curriculum").fetchone()[0]
            if curr_count > 0:
                # --- Daily new-item cap: bound how much NEW material enters per day
                # so the future review pile never collapses (FSRS assumes this). Due
                # reviews already had priority above and are never capped.
                new_today = count_new_topics_today()
                cap = get_daily_new_item_cap()
                if new_today >= cap:
                    return {
                        "topic": "",
                        "domain": "",
                        "reason": "daily_new_limit_reached",
                        "new_items_today": new_today,
                        "daily_new_item_cap": cap,
                        "message": (
                            f"Daily new-topic cap reached ({new_today}/{cap}). Stop adding "
                            "new material — consolidate with reviews and weak knowledge "
                            "points, or end the session. New topics resume tomorrow."
                        ),
                        "is_nested": False,
                    }

                medicine_weight = get_medicine_weight()  # default 0.8

                # Interleave across domains: deprioritize the most recently studied
                # domain so consecutive new picks span different systems.
                _ld = db.execute(
                    "SELECT c.domain FROM question_attempts qa JOIN curriculum c "
                    "ON c.topic = qa.topic ORDER BY qa.date DESC LIMIT 1"
                ).fetchone()
                last_domain = (_ld["domain"] if _ld else "") or ""

                # Use a deterministic counter to interleave medicine/anesthesia picks.
                # Counter = number of new_coverage topics already studied from curriculum.
                studied_curriculum = db.execute(
                    """SELECT COUNT(*) FROM curriculum c
                       JOIN topics t ON t.topic = c.topic
                       WHERE t.times_seen > 0"""
                ).fetchone()[0]

                # Determine desired discipline for this slot.
                # Critical-care topics always jump the queue regardless of discipline.
                # For non-CC topics, interleave: every Nth slot gets anesthesia.
                # N = round(1 / (1 - medicine_weight)), but cap to avoid division errors.
                if medicine_weight >= 1.0:
                    anesthesia_slot_every = 9999  # effectively never
                elif medicine_weight <= 0.0:
                    anesthesia_slot_every = 1
                else:
                    anesthesia_slot_every = max(1, round(1.0 / (1.0 - medicine_weight)))

                # Slot index: is this an anesthesia slot?
                is_anesthesia_slot = (studied_curriculum % anesthesia_slot_every == (anesthesia_slot_every - 1))

                # 2a-0. On-call "Approach to X" presentation topics — interleave one
                # every 3rd new-coverage slot, AHEAD of the critical-care/disease passes,
                # so cross-cover survival skills get a steady ~1/3 share from the very
                # start (otherwise the 570 untouched CC topics would bury them). Within
                # the set, the immediately life-threatening approaches come first.
                is_presentation_slot = (studied_curriculum % 3 == 1)
                if is_presentation_slot:
                    untouched_pres = db.execute(
                        """SELECT topic, domain, discipline, is_critical_care, subtopics, priority_tier, category
                           FROM curriculum
                           WHERE category = 'presentation'
                             AND topic NOT IN (SELECT topic FROM topics WHERE times_seen > 0)
                           ORDER BY is_critical_care DESC, high_yield DESC, priority_tier ASC, topic ASC
                           LIMIT 1"""
                    ).fetchone()
                    if untouched_pres:
                        row = untouched_pres
                        return {
                            "topic": row["topic"],
                            "domain": row["domain"] or "",
                            "discipline": row["discipline"] or "medicine",
                            "is_critical_care": bool(row["is_critical_care"]),
                            "priority_tier": int(row["priority_tier"] or 2),
                            "category": row["category"] or "presentation",
                            "subtopics": json.loads(row["subtopics"] or "[]"),
                            "reason": "new_coverage",
                            "retrieval_query": row["topic"],
                            "suggested_phase": "new_material",
                            "is_nested": False,
                        }

                # 2a. Critical-care untouched (highest priority, ignores discipline weight)
                untouched_cc = db.execute(
                    """SELECT topic, domain, discipline, is_critical_care, subtopics, priority_tier, category
                       FROM curriculum
                       WHERE is_critical_care = 1
                         AND topic NOT IN (SELECT topic FROM topics WHERE times_seen > 0)
                       ORDER BY high_yield DESC, priority_tier ASC, topic ASC
                       LIMIT 1"""
                ).fetchone()

                if untouched_cc:
                    row = untouched_cc
                    return {
                        "topic": row["topic"],
                        "domain": row["domain"] or "",
                        "discipline": row["discipline"] or "medicine",
                        "is_critical_care": bool(row["is_critical_care"]),
                        "priority_tier": int(row["priority_tier"] or 2),
                        "category": row["category"] or "topic",
                        "subtopics": json.loads(row["subtopics"] or "[]"),
                        "reason": "new_coverage",
                        "retrieval_query": row["topic"],
                        "suggested_phase": "new_material",
                        "is_nested": False,
                    }

                # 2b. Discipline-weighted non-CC untouched topic
                preferred_discipline = "anesthesia" if is_anesthesia_slot else "medicine"
                untouched_row = db.execute(
                    """SELECT topic, domain, discipline, is_critical_care, subtopics, priority_tier, category
                       FROM curriculum
                       WHERE is_critical_care = 0
                         AND discipline = ?
                         AND topic NOT IN (SELECT topic FROM topics WHERE times_seen > 0)
                       ORDER BY (CASE WHEN domain = ? THEN 1 ELSE 0 END) ASC,
                                high_yield DESC, priority_tier ASC, topic ASC
                       LIMIT 1""",
                    (preferred_discipline, last_domain),
                ).fetchone()

                # Fall back to any untouched topic if preferred discipline is exhausted
                if not untouched_row:
                    untouched_row = db.execute(
                        """SELECT topic, domain, discipline, is_critical_care, subtopics, priority_tier, category
                           FROM curriculum
                           WHERE topic NOT IN (SELECT topic FROM topics WHERE times_seen > 0)
                           ORDER BY high_yield DESC, priority_tier ASC, topic ASC
                           LIMIT 1"""
                    ).fetchone()

                if untouched_row:
                    row = untouched_row
                    return {
                        "topic": row["topic"],
                        "domain": row["domain"] or "",
                        "discipline": row["discipline"] or "medicine",
                        "is_critical_care": bool(row["is_critical_care"]),
                        "priority_tier": int(row["priority_tier"] or 2),
                        "category": row["category"] or "topic",
                        "subtopics": json.loads(row["subtopics"] or "[]"),
                        "reason": "new_coverage",
                        "retrieval_query": row["topic"],
                        "suggested_phase": "new_material",
                        "is_nested": False,
                    }
    except Exception:
        pass  # curriculum empty or unavailable — fall through to lesson planner

    # --- 3. Lesson-planner fallback (existing behavior) ---
    try:
        plan = generate_lesson_plan(
            duration_minutes=20,
            mode=LessonMode.STANDARD,
            db_conn=conn()
        )

        primary = plan.primary_topic
        reason = "due_today" if plan.focus_areas == "fsrs_overdue_only" else "weak"

        return {
            "topic": primary,
            "domain": "",
            "subtopics": [],
            "reason": reason,
            "retrieval_query": primary,
            "suggested_phase": "drilling" if plan.drill_aggressiveness == "heavy" else "new_material",
            "is_nested": False,
        }
    except Exception as e:
        print(f"Next topic error: {e}")
        return {
            "topic": "shock",
            "domain": "",
            "subtopics": [],
            "reason": "error_fallback",
            "retrieval_query": "shock management",
            "suggested_phase": "new_material",
            "is_nested": False,
            "error": str(e)
        }


# ============================================================================
# TOOL 4: SUBMIT ANSWER - Submit answer and update mastery
# ============================================================================

def submit_answer(
    topic: str,
    user_answer: str,
    is_correct: bool,
    confidence_reported: int = 3,
    teach_back_quality: float = 0.5,
    mistake_type: str = "other",
    subtopic: str = "",
    transfer_success: bool = False,
    bloom_level: str = "",
    session_id: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Submit an answer and update FSRS/mastery tracking.

    Args:
        topic: Topic being tested
        user_answer: Student's answer
        is_correct: Whether answer was correct
        confidence_reported: 1-5 scale
        teach_back_quality: 0-1 mechanism quality
        mistake_type: Type of error (mechanism, recall, etc.)
        subtopic: Nested subtopic (if applicable)
        transfer_success: Did they succeed on transfer question?

    Returns:
        {
            "ok": bool,
            "next_review_date": ISO datetime,
            "mastery_updated": bool,
            "level_achieved": str (baseline, intermediate, advanced),
            "strategy_for_next": str (transfer, drill_hard, deeper_principle, etc.)
        }
    """
    try:
        # Clamp confidence to 1-5 range
        confidence = max(1, min(5, confidence_reported))

        # Clamp teach_back_quality to 0-1
        mechanism_quality = max(0.0, min(1.0, teach_back_quality))

        # Ensure topic row exists and get its id
        topic_id = get_or_create_topic(topic, subtopic or "")

        # Structural double-submit guard. Both front ends have been observed
        # calling submit_study_answer AND submit_answer for the same answer
        # (twice, on different days, despite instructions forbidding it), which
        # writes two attempt rows and advances FSRS twice — halving intervals.
        # If an attempt with the same topic + same non-trivial user_answer +
        # same result already landed in the last 3 minutes, treat this call as
        # the duplicate leg: skip the second log_attempt (no second FSRS
        # advance) but still refresh the mastery vector and return normally.
        # Matching on the answer text keeps false positives implausible —
        # rapid-fire re-asks of one topic produce different answers.
        duplicate_of_recent = False
        if (user_answer or "").strip() and user_answer.strip().lower() not in ("correct", "incorrect"):
            with conn() as _db:
                recent = _db.execute(
                    """SELECT COUNT(*) FROM question_attempts
                       WHERE topic = ? AND user_answer = ? AND result = ?
                         AND date >= datetime('now', '-3 minutes')""",
                    (topic, user_answer, "correct" if is_correct else "incorrect"),
                ).fetchone()[0]
            duplicate_of_recent = recent > 0

        # Log the attempt — this calls update_mastery_score internally, which
        # advances FSRS once and writes mastery_score + status to topics table.
        # Do NOT do a second fsrs_review call after this; that would double-advance.
        if not duplicate_of_recent:
            log_attempt(
                session_id="mcp_session",
                topic=topic,
                subtopic=subtopic or "",
                question="MCP submitted answer",
                user_answer=user_answer,
                ideal_answer="",
                result="correct" if is_correct else "incorrect",
                mistake_type=mistake_type,
                difficulty="medium",
                hints_used=0,
                confidence_reported=confidence,
                retrieval_sources="",
                source_citations="",
                notes="",
                library="",
                training_phase="intern_year",
                bloom_level=bloom_level,
            )

        # Re-read the updated topic row (mastery_score/status written by log_attempt)
        summary = get_topic_summary(topic)

        # Map topics.status → level vocabulary used by the API contract
        _STATUS_TO_LEVEL = {
            "new": "baseline", "weak": "baseline", "unstable": "baseline",
            "learning": "intermediate", "strong": "intermediate",
            "maintenance": "advanced",
        }
        current_status = summary.get("status", "new")
        level_achieved = _STATUS_TO_LEVEL.get(current_status, "baseline")
        next_review_iso = summary.get("next_review_date") or (
            datetime.now() + timedelta(days=1)
        ).date().isoformat()

        # Build mastery vector from all question_attempts for this topic and
        # persist it to mastery_vector table so get_mastery_gates sees real data.
        with conn() as db:
            attempt_rows = db.execute(
                """SELECT result, confidence_reported, teach_back_quality, transfer_success
                   FROM question_attempts WHERE topic=? ORDER BY attempt_id""",
                (topic,),
            ).fetchall()
            attempts_for_vector = [
                {
                    "correct": r["result"] == "correct",
                    "confidence_reported": float(r["confidence_reported"] or 3),
                    "mechanism_quality": float(r["teach_back_quality"] or 0.0),
                    "transfer_success": bool(r["transfer_success"]),
                }
                for r in attempt_rows
            ]
            vector = compute_mastery_vector(attempts_for_vector)
            # Upsert keyed on topic_NAME, not topic_id.
            #
            # mastery_vector.topic_id is the PK but topic_name is also UNIQUE, while
            # topics has one row per (topic, subtopic) — so a single topic name owns
            # many topic_ids ("Electrolytes" has 17). The previous
            # `ON CONFLICT(topic_id)` therefore hit the topic_name UNIQUE constraint
            # for every subtopic after the first and the whole submit_answer failed
            # with "UNIQUE constraint failed: mastery_vector.topic_name", returning
            # ok=False and mastery_updated=False. The mastery vector silently stopped
            # updating for exactly the most-studied topics, on the MCP path too.
            #
            # The vector is computed from all attempts WHERE topic=<name>, so the name
            # is the correct key. UPDATE-then-INSERT rather than a multi-target
            # ON CONFLICT so behaviour does not depend on the SQLite version.
            vector_row = (
                vector["accuracy"], vector["transfer_auc"],
                vector["mechanism_quality"], vector["calibration_icc"],
                vector["retention_6mo"], vector["integration_score"],
                int(vector["accuracy"] >= 0.70 and vector["mechanism_quality"] > 0.0),
            )
            cur = db.execute(
                """UPDATE mastery_vector
                      SET accuracy=?, transfer_auc=?, mechanism_quality=?,
                          calibration_icc=?, retention_6mo=?, integration_score=?,
                          mastery_achieved=?, last_updated=CURRENT_TIMESTAMP
                    WHERE topic_name=?""",
                (*vector_row, topic),
            )
            if cur.rowcount == 0:
                db.execute(
                    """INSERT INTO mastery_vector
                           (topic_id, topic_name, accuracy, transfer_auc, mechanism_quality,
                            calibration_icc, retention_6mo, integration_score,
                            mastery_achieved, last_updated)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)""",
                    (topic_id, topic, *vector_row),
                )

        # Determine strategy for next question
        accuracy_rate = summary.get("accuracy", float(is_correct))

        context = PerformanceContext(
            accuracy=is_correct,
            confidence_reported=confidence,
            mechanism_quality=mechanism_quality,
            topic=topic,
            recent_accuracy_rate=accuracy_rate,
            topic_accuracy_rate=accuracy_rate
        )

        strategy = decide_question_strategy(context)

        return {
            "ok": True,
            "next_review_date": next_review_iso,
            "mastery_updated": True,
            "level_achieved": level_achieved,
            "mastery_score": round(summary.get("mastery_score", 0.0), 3),
            "status": current_status,
            "strategy_for_next": strategy.value,
            "confidence_calibration": "good" if confidence == 3 else ("low" if confidence <= 2 else "high")
        }
    except Exception as e:
        print(f"Submit answer error: {e}")
        return {
            "ok": False,
            "next_review_date": (datetime.now() + timedelta(days=1)).isoformat(),
            "mastery_updated": False,
            "level_achieved": "baseline",
            "error": str(e)
        }


# ============================================================================
# TOOL 5: MASTERY GATES - Mastery matrix and phase advancement
# ============================================================================

def get_mastery_gates() -> Dict[str, Any]:
    """
    Get mastery matrix and check readiness for phase advancement.

    Returns:
        {
            "mastery_matrix": {
                "topic": {
                    "level": "baseline|intermediate|advanced",
                    "vector": {"accuracy": ..., "transfer_auc": ..., "mechanism_quality": ...}
                }, ...
            },
            "ready_for_phase_advance": bool
        }
    """
    try:
        with conn() as db:
            topic_rows = db.execute("""
                SELECT topic FROM topics
                ORDER BY topic ASC
            """).fetchall()

        mastery_matrix = {}
        phase_ready_count = 0

        _status_to_level = {
            "new": "baseline",
            "weak": "baseline",
            "unstable": "baseline",
            "learning": "intermediate",
            "maintenance": "advanced",
            "strong": "advanced",
            "intermediate": "intermediate",
            "advanced": "advanced",
            "baseline": "baseline",
        }
        # Load mastery_vector rows in bulk for O(1) lookup per topic
        with conn() as mv_db:
            mv_rows = mv_db.execute(
                "SELECT topic_name, accuracy, transfer_auc, mechanism_quality, "
                "calibration_icc, retention_6mo, integration_score FROM mastery_vector"
            ).fetchall()
        mv_by_topic = {r["topic_name"]: r for r in mv_rows}

        for (topic,) in topic_rows:
            summary = get_topic_summary(topic)
            raw_status = summary.get("status") or summary.get("mastery_level") or None
            if raw_status in (None, ""):
                level = None
            else:
                level = _status_to_level.get(raw_status, "baseline")

            # Prefer the mastery_vector table (populated by submit_answer);
            # fall back to zeros when the topic has never been attempted.
            mv = mv_by_topic.get(topic)
            mastery_matrix[topic] = {
                "level": level,
                "mastery_score": round(summary.get("mastery_score", 0.0), 3),
                "vector": {
                    "accuracy": float(mv["accuracy"]) if mv else 0.0,
                    "transfer_auc": float(mv["transfer_auc"]) if mv else 0.0,
                    "mechanism_quality": float(mv["mechanism_quality"]) if mv else 0.0,
                    "calibration_icc": float(mv["calibration_icc"]) if mv else 0.0,
                    "retention_6mo": float(mv["retention_6mo"]) if mv else 0.0,
                    "integration_score": float(mv["integration_score"]) if mv else 0.0,
                }
            }

            if level in ["maintenance", "intermediate", "advanced"]:
                phase_ready_count += 1

        # Check if ready for phase advance (50% of topics mastered to intermediate+)
        total_topics = len(mastery_matrix)
        ready_for_advance = (phase_ready_count / total_topics >= 0.5) if total_topics > 0 else False

        return {
            "mastery_matrix": mastery_matrix,
            "ready_for_phase_advance": ready_for_advance,
            "mastered_count": phase_ready_count,
            "total_topics": total_topics
        }
    except Exception as e:
        print(f"Mastery gates error: {e}")
        return {
            "mastery_matrix": {},
            "ready_for_phase_advance": False,
            "error": str(e)
        }


# ============================================================================
# TOOL 5b: MASTERY MAP - Curriculum coverage overview
# ============================================================================

def get_mastery_map() -> Dict[str, Any]:
    """
    Return a curriculum-coverage map showing how much of the full blueprint
    has been studied and at what mastery level.

    Returns:
        {
            "total_curriculum_topics": int,
            "topics_studied": int,
            "coverage_pct": float,
            "mastery_levels": {"baseline": int, "intermediate": int, "advanced": int},
            "by_domain": [{"domain": str, "total": int, "studied": int,
                           "coverage_pct": float, "avg_accuracy": float}, ...],
            "weakest_domains": [str, ...],          # top 3 by lowest coverage_pct
            "untouched_count": int,
            "next_suggested_domain": str            # lowest-coverage domain with untouched high-yield
        }
    Robust to empty curriculum (returns zeros, not errors).
    """
    _STATUS_TO_LEVEL = {
        "new": "baseline", "weak": "baseline", "unstable": "baseline",
        "learning": "intermediate", "strong": "intermediate",
        "maintenance": "advanced",
    }
    try:
        with conn() as db:
            # Curriculum totals
            total_curriculum = db.execute(
                "SELECT COUNT(*) FROM curriculum"
            ).fetchone()[0]

            # Studied topics: those in topics table with times_seen > 0
            studied_rows = db.execute(
                """SELECT t.topic, t.status, t.times_correct, t.times_seen
                   FROM topics t
                   WHERE t.times_seen > 0"""
            ).fetchall()
            studied_set = {r["topic"] for r in studied_rows}
            # A topic counts as studied if it has topic-level activity OR any
            # fact-level (knowledge_point) activity — otherwise coverage badly
            # understates real learning done through submit_knowledge_points.
            try:
                kp_topic_rows = db.execute(
                    "SELECT DISTINCT topic FROM knowledge_points"
                ).fetchall()
                studied_set |= {r["topic"] for r in kp_topic_rows}
            except Exception:
                pass
            # Coverage is (studied CURRICULUM topics) / (curriculum total): the
            # numerator must be intersected with the blueprint, or freeform
            # topic names and unit:% bookkeeping rows inflate it (and can push
            # untouched_count negative). Freeform study is still real learning —
            # it is reported via knowledge_points below — it just isn't
            # blueprint coverage.
            curriculum_names = {r[0] for r in db.execute("SELECT topic FROM curriculum").fetchall()}
            studied_offblueprint = len(studied_set - curriculum_names)
            studied_set &= curriculum_names
            topics_studied = len(studied_set)

            coverage_pct = round((topics_studied / total_curriculum * 100), 1) if total_curriculum > 0 else 0.0

            # Mastery levels: only for topics that are in the curriculum
            mastery_levels = {"baseline": 0, "intermediate": 0, "advanced": 0}
            for r in studied_rows:
                level = _STATUS_TO_LEVEL.get(r["status"] or "new", "baseline")
                mastery_levels[level] = mastery_levels.get(level, 0) + 1

            # Per-domain breakdown (include discipline column)
            domain_rows = db.execute(
                "SELECT domain, discipline, COUNT(*) as total FROM curriculum GROUP BY domain, discipline"
            ).fetchall()

            by_domain = []
            for dr in domain_rows:
                domain = dr["domain"] or "(unassigned)"
                discipline = dr["discipline"] or "medicine"
                total_d = dr["total"]

                # Topics in this domain that have been studied
                studied_d_rows = db.execute(
                    """SELECT t.topic, t.times_correct, t.times_seen
                       FROM topics t
                       JOIN curriculum c ON c.topic = t.topic
                       WHERE c.domain = ? AND t.times_seen > 0""",
                    (dr["domain"],),
                ).fetchall()
                studied_d = len(studied_d_rows)

                cov_d = round((studied_d / total_d * 100), 1) if total_d > 0 else 0.0

                # Average accuracy for studied topics in domain
                total_correct = sum(r["times_correct"] or 0 for r in studied_d_rows)
                total_seen = sum(r["times_seen"] or 0 for r in studied_d_rows)
                avg_acc = round(total_correct / total_seen, 3) if total_seen > 0 else 0.0

                by_domain.append({
                    "domain": domain,
                    "discipline": discipline,
                    "total": total_d,
                    "studied": studied_d,
                    "coverage_pct": cov_d,
                    "avg_accuracy": avg_acc,
                })

            # Sort weakest-covered first
            by_domain.sort(key=lambda x: (x["coverage_pct"], x["avg_accuracy"]))

            weakest_domains = [d["domain"] for d in by_domain[:3]]

            untouched_count = total_curriculum - topics_studied

            # Next suggested domain: lowest coverage that still has untouched high-yield
            next_suggested_domain = ""
            for d in by_domain:
                raw_domain = d["domain"] if d["domain"] != "(unassigned)" else ""
                hy_untouched = db.execute(
                    """SELECT COUNT(*) FROM curriculum
                       WHERE domain = ? AND high_yield = 1
                         AND topic NOT IN (SELECT topic FROM topics WHERE times_seen > 0)""",
                    (raw_domain,),
                ).fetchone()[0]
                if hy_untouched > 0:
                    next_suggested_domain = d["domain"]
                    break

            # --- By-discipline breakdown ---
            by_discipline: Dict[str, Any] = {}
            for disc in ("medicine", "anesthesia"):
                disc_rows = db.execute(
                    "SELECT COUNT(*) as total FROM curriculum WHERE discipline = ?", (disc,)
                ).fetchone()
                total_disc = disc_rows["total"] if disc_rows else 0
                studied_disc = db.execute(
                    """SELECT COUNT(*) FROM curriculum c
                       JOIN topics t ON t.topic = c.topic
                       WHERE c.discipline = ? AND t.times_seen > 0""",
                    (disc,),
                ).fetchone()[0]
                by_discipline[disc] = {
                    "total": total_disc,
                    "studied": studied_disc,
                    "coverage_pct": round(studied_disc / total_disc * 100, 1) if total_disc > 0 else 0.0,
                }

            # --- Critical-care breakdown ---
            cc_total = db.execute(
                "SELECT COUNT(*) FROM curriculum WHERE is_critical_care = 1"
            ).fetchone()[0]
            cc_studied = db.execute(
                """SELECT COUNT(*) FROM curriculum c
                   JOIN topics t ON t.topic = c.topic
                   WHERE c.is_critical_care = 1 AND t.times_seen > 0"""
            ).fetchone()[0]
            critical_care = {
                "total": cc_total,
                "studied": cc_studied,
                "coverage_pct": round(cc_studied / cc_total * 100, 1) if cc_total > 0 else 0.0,
            }

            # --- On-call / chief-complaint ("Approach to X") coverage ---
            # These presentation topics are the cross-cover survival skill set; surface
            # their coverage separately so the intern can track them as a distinct goal.
            pres_total = db.execute(
                "SELECT COUNT(*) FROM curriculum WHERE category = 'presentation'"
            ).fetchone()[0]
            pres_studied = db.execute(
                """SELECT COUNT(*) FROM curriculum c
                   JOIN topics t ON t.topic = c.topic
                   WHERE c.category = 'presentation' AND t.times_seen > 0"""
            ).fetchone()[0]
            on_call_approaches = {
                "total": pres_total,
                "studied": pres_studied,
                "coverage_pct": round(pres_studied / pres_total * 100, 1) if pres_total > 0 else 0.0,
            }

            # --- Fact-level (knowledge-point) progress — the REAL measure of learning ---
            # This is where the day-to-day work actually lands, so report it prominently
            # rather than only the topic-level coverage (which lags far behind reality).
            kp_rows = db.execute(
                "SELECT status, COUNT(*) n FROM knowledge_points GROUP BY status"
            ).fetchall()
            kp_by_status = {r["status"]: r["n"] for r in kp_rows}
            kp_total = sum(kp_by_status.values())
            catalog_total = db.execute("SELECT COUNT(*) FROM kp_catalog").fetchone()[0]
            knowledge_points = {
                "facts_tracked": kp_total,
                "weak": kp_by_status.get("weak", 0),
                "learning": kp_by_status.get("learning", 0),
                "mastered": kp_by_status.get("mastered", 0),
                "catalog_total": catalog_total,
                "catalog_pct": round(kp_total / catalog_total * 100, 1) if catalog_total > 0 else 0.0,
            }

        return {
            "total_curriculum_topics": total_curriculum,
            "topics_studied": topics_studied,
            "topics_studied_off_blueprint": studied_offblueprint,
            "coverage_pct": coverage_pct,
            "mastery_levels": mastery_levels,
            "knowledge_points": knowledge_points,
            "by_discipline": by_discipline,
            "by_domain": by_domain,
            "critical_care": critical_care,
            "on_call_approaches": on_call_approaches,
            "weakest_domains": weakest_domains,
            "untouched_count": untouched_count,
            "next_suggested_domain": next_suggested_domain,
        }
    except Exception as e:
        print(f"Mastery map error: {e}")
        return {
            "total_curriculum_topics": 0,
            "topics_studied": 0,
            "coverage_pct": 0.0,
            "mastery_levels": {"baseline": 0, "intermediate": 0, "advanced": 0},
            "knowledge_points": {"facts_tracked": 0, "weak": 0, "learning": 0, "mastered": 0,
                                 "catalog_total": 0, "catalog_pct": 0.0},
            "by_discipline": {"medicine": {"total": 0, "studied": 0, "coverage_pct": 0.0},
                              "anesthesia": {"total": 0, "studied": 0, "coverage_pct": 0.0}},
            "by_domain": [],
            "critical_care": {"total": 0, "studied": 0, "coverage_pct": 0.0},
            "on_call_approaches": {"total": 0, "studied": 0, "coverage_pct": 0.0},
            "weakest_domains": [],
            "untouched_count": 0,
            "next_suggested_domain": "",
            "error": str(e),
        }


# ============================================================================
# TOOL 6: PROGRESS - Get progress statistics
# ============================================================================

def get_progress() -> Dict[str, Any]:
    """
    Get comprehensive progress statistics across learning domains.

    Returns:
        {
            "intern_medicine_pct": float 0-100,
            "icu_pct": float 0-100,
            "anesthesia_pct": float 0-100,
            "overall_pct": float 0-100,
            "hours_studied": float,
            "total_attempts": int,
            "accuracy_overall": float 0-1
        }
    """
    try:
        with conn() as db:
            # Count mastered topics by domain (use `status` column, not non-existent mastery_level)
            mastered = db.execute("""
                SELECT COUNT(DISTINCT topic) FROM topics
                WHERE status IN ('maintenance', 'strong', 'learning')
            """).fetchone()[0]

            total = db.execute(
                "SELECT COUNT(DISTINCT topic) FROM topics"
            ).fetchone()[0]

            overall_pct = (mastered / total * 100) if total > 0 else 0.0

            # Real per-discipline coverage (% of curriculum studied), mirroring
            # get_mastery_map — not the old fixed multipliers.
            def _disc_cov(where_sql: str, params: tuple) -> float:
                tot = db.execute(
                    f"SELECT COUNT(*) FROM curriculum WHERE {where_sql}", params
                ).fetchone()[0]
                stud = db.execute(
                    f"""SELECT COUNT(*) FROM curriculum c JOIN topics t ON t.topic = c.topic
                        WHERE {where_sql} AND t.times_seen > 0""",
                    params,
                ).fetchone()[0]
                return round(stud / tot * 100, 1) if tot else 0.0

            intern_medicine_pct = _disc_cov("discipline = ?", ("medicine",))
            anesthesia_pct = _disc_cov("discipline = ?", ("anesthesia",))
            icu_pct = _disc_cov("is_critical_care = 1", ())

            # Compute hours studied from question_attempts
            total_attempts = db.execute(
                "SELECT COUNT(*) FROM question_attempts"
            ).fetchone()[0]
            hours_studied = total_attempts * 0.02  # Rough estimate: 1.2 min per question

            # Overall accuracy
            row = db.execute("""
                SELECT
                    SUM(CASE WHEN result = 'correct' THEN 1 ELSE 0 END) as correct,
                    COUNT(*) as total
                FROM question_attempts
            """).fetchone()
            accuracy = (row[0] / row[1]) if row[1] > 0 else 0.0

        return {
            "intern_medicine_pct": min(100.0, intern_medicine_pct),
            "icu_pct": min(100.0, icu_pct),
            "anesthesia_pct": min(100.0, anesthesia_pct),
            "overall_pct": overall_pct,
            "hours_studied": hours_studied,
            "total_attempts": total_attempts,
            "accuracy_overall": accuracy
        }
    except Exception as e:
        print(f"Progress error: {e}")
        return {
            "intern_medicine_pct": 0.0,
            "icu_pct": 0.0,
            "anesthesia_pct": 0.0,
            "overall_pct": 0.0,
            "hours_studied": 0.0,
            "total_attempts": 0,
            "accuracy_overall": 0.0,
            "error": str(e)
        }


# ============================================================================
# TOOL 5c: SET MEDICINE WEIGHT - Flip the discipline study bias
# ============================================================================

def set_medicine_weight_tool(weight: float) -> Dict[str, Any]:
    """
    Set the fraction of new study picks that come from medicine (vs anesthesia).

    Args:
        weight: Float 0.0–1.0. Default 0.8 means ~80% medicine, 20% anesthesia.
                Critical-care / overlap topics always jump the queue regardless.

    Returns:
        {"ok": bool, "medicine_weight": float, "anesthesia_weight": float}
    """
    try:
        _set_medicine_weight(weight)
        clamped = max(0.0, min(1.0, float(weight)))
        return {
            "ok": True,
            "medicine_weight": round(clamped, 3),
            "anesthesia_weight": round(1.0 - clamped, 3),
        }
    except Exception as e:
        return {"ok": False, "error": str(e)}


# ============================================================================
# TOOL 7: REQUEST FOLLOW-UP - Request follow-up on subtopic
# ============================================================================

def get_kp_to_study(
    limit: int = 10,
    discipline: str = "",
    topic: str = "",
    format: str = "",
) -> List[Dict[str, Any]]:
    """Return the highest-priority kp_catalog entries not yet mastered.

    Priority order mirrors get_next_topic exactly:
      1. category='presentation' first (on-call survival set)
      2. is_critical_care DESC (CC topics before non-CC)
      3. tier ASC (tier-1 everyday topics before tier-2/3)
      4. discipline: 'medicine' before 'anesthesia'
      5. topic ASC (stable tiebreaker)

    Excludes rows where the stem already exists in knowledge_points with
    status='mastered' (LEFT JOIN, filter out mastered stems).

    Optional filters:
      discipline ('medicine'|'anesthesia') — restrict to a single discipline.
      topic (exact match) — restrict to a single topic.
      format ('car') — restrict to car_safe=1 entries only (short/ear-friendly
          KPs suitable for hands-free voice study while driving).

    Returns a list of dicts with keys:
      id, topic, stem, answer, rationale, bloom, source, discipline, tier,
      category, is_critical_care, car_safe.
    """
    initialize_database()
    with conn() as db:
        clauses = ["(kp.id IS NOT NULL)"]
        params: list = []
        if discipline:
            clauses.append("kp.discipline = ?")
            params.append(discipline)
        if topic:
            clauses.append("kp.topic = ?")
            params.append(topic)
        if format == "car":
            clauses.append("kp.car_safe = 1")
        where = " AND ".join(clauses)
        params.append(limit)
        rows = db.execute(
            f"""
            SELECT kp.id, kp.topic, kp.stem, kp.answer, kp.rationale,
                   kp.bloom, kp.source, kp.discipline, kp.tier,
                   kp.category, kp.is_critical_care, kp.car_safe
            FROM kp_catalog kp
            LEFT JOIN knowledge_points kpp
                   ON kpp.topic = kp.topic AND kpp.point = kp.stem
            WHERE {where}
              AND (kpp.id IS NULL OR kpp.status != 'mastered')
            ORDER BY
                kp.times_seen ASC,                                          -- least-served first: ADVANCE, don't repeat
                CASE WHEN kp.category = 'presentation' THEN 0 ELSE 1 END ASC,
                kp.is_critical_care DESC,
                kp.tier ASC,
                CASE WHEN kp.discipline = 'medicine' THEN 0 ELSE 1 END ASC,
                kp.topic ASC
            LIMIT ?
            """,
            params,
        ).fetchall()
        # Mark these as served so the next call moves on to fresh material
        # (the stem-text join above is fragile because the tutor paraphrases points;
        # times_seen guarantees forward progress regardless).
        served_ids = [r["id"] for r in rows]
        if served_ids:
            db.execute(
                f"UPDATE kp_catalog SET times_seen = times_seen + 1 WHERE id IN "
                f"({','.join('?' * len(served_ids))})",
                served_ids,
            )
    return [
        {
            "id": r["id"],
            "topic": r["topic"],
            "stem": r["stem"],
            "answer": r["answer"],
            "rationale": r["rationale"],
            "bloom": r["bloom"],
            "source": r["source"],
            "discipline": r["discipline"],
            "tier": r["tier"],
            "category": r["category"],
            "is_critical_care": bool(r["is_critical_care"]),
            "car_safe": bool(r["car_safe"]),
        }
        for r in rows
    ]


def request_follow_up(
    parent_topic: str,
    requested_subtopic: str,
    session_id: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Request a follow-up session on a subtopic related to parent topic.

    Used when student wants to drill deeper on a specific aspect (e.g.,
    parent="shock" -> subtopic="vasopressor_dosing").

    Args:
        parent_topic: Parent topic name
        requested_subtopic: Subtopic to focus on

    Returns:
        {
            "ok": bool,
            "parent_topic": str,
            "child_topic": str,
            "follow_up_session_id": str,
            "retrieval_query": str,
            "suggested_phase": str,
            "related_subtopics": [str, ...],
            "lesson_duration_minutes": int
        }
    """
    try:
        # Check if parent topic exists
        with conn() as db:
            exists = db.execute(
                "SELECT COUNT(*) FROM topics WHERE topic = ?", (parent_topic,)
            ).fetchone()[0] > 0

        if not exists:
            return {
                "ok": False,
                "parent_topic": parent_topic,
                "child_topic": requested_subtopic,
                "error": "Parent topic not found"
            }

        # Generate lesson plan for follow-up
        plan = generate_lesson_plan(
            duration_minutes=15,
            mode=LessonMode.DEEP_DIVE,
            focus_topic=requested_subtopic,
            db_conn=conn()
        )

        # Related subtopics (simplified - would use knowledge graph in production)
        related = [
            f"{parent_topic}_mechanism",
            f"{parent_topic}_clinical_application",
            f"{parent_topic}_edge_cases"
        ]

        follow_up_session_id = f"followup_{parent_topic}_{requested_subtopic}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        return {
            "ok": True,
            "parent_topic": parent_topic,
            "child_topic": requested_subtopic,
            "follow_up_session_id": follow_up_session_id,
            "retrieval_query": requested_subtopic,
            "suggested_phase": "drilling",
            "related_subtopics": related,
            "lesson_duration_minutes": 15
        }
    except Exception as e:
        print(f"Follow-up request error: {e}")
        return {
            "ok": False,
            "parent_topic": parent_topic,
            "child_topic": requested_subtopic,
            "error": str(e)
        }
