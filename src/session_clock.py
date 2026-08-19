"""A real clock for the session, because the tutor was guessing at time.

The maintainer asked for a 30-minute session, got 8 questions in 11.6 minutes,
and was being wound down well before the time he had. The tutor has no wall
clock: it cannot see how long the conversation has run, so "we're coming up on
time" is invented. Left alone it wastes the study time he actually set aside,
which is the scarce resource in an intern year.

Everything here is measured rather than assumed. Across 127 recorded
inter-question gaps his pace is a median of 77 seconds per question (p25 53s,
p75 121s), and whole sessions run 69-99 s/question. So a 30-minute session is
roughly 21 questions, not 8, and a 15-minute one is about 10. The planner uses
the observed median until the current session has enough of its own gaps to
speak for itself, at which point it switches to the live pace — a session where
he is thinking hard about ARDS physiology genuinely runs slower than one
clearing familiar review cards, and the plan should follow the session rather
than the average.

"As much time as we need" is a distinct mode, not a very large number: the goal
becomes clearing the overdue backlog, and the honest report is how many facts
are actually due and what that costs in minutes.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any

from .student_model import conn

# Fallback until the live session has spoken for itself. Measured, not guessed:
# median of 127 recorded inter-question gaps.
DEFAULT_SECONDS_PER_QUESTION = 85
# Below this many answers the session's own pace is too noisy to trust — one
# long think would halve the estimated question budget.
MIN_SAMPLES_FOR_LIVE_PACE = 3
# Reserve at the end for the wrap-up: recap, what to hit next time.
WRAP_UP_MINUTES = 2


def _ensure_table() -> None:
    with conn() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS session_clock (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                started_at TEXT NOT NULL,
                planned_minutes INTEGER NOT NULL,  -- 0 means unlimited/backlog mode
                ended_at TEXT
            )
        """)


def start_clock(planned_minutes: int) -> dict[str, Any]:
    """Begin (or restart) the session clock. planned_minutes=0 means unlimited."""
    _ensure_table()
    started = datetime.now(timezone.utc)
    with conn() as db:
        db.execute(
            """INSERT INTO session_clock (id, started_at, planned_minutes, ended_at)
               VALUES (1, ?, ?, NULL)
               ON CONFLICT(id) DO UPDATE SET
                   started_at=excluded.started_at,
                   planned_minutes=excluded.planned_minutes,
                   ended_at=NULL""",
            (started.isoformat(), max(0, int(planned_minutes))))
    return pacing(now=started)


def end_clock() -> None:
    _ensure_table()
    with conn() as db:
        db.execute("UPDATE session_clock SET ended_at=? WHERE id=1",
                   (datetime.now(timezone.utc).isoformat(),))


def _observed_pace(db, started: datetime) -> tuple[float, str]:
    """Seconds per question, from THIS session if it has said enough."""
    rows = [r[0] for r in db.execute(
        "SELECT date FROM question_attempts WHERE datetime(date) >= datetime(?) ORDER BY attempt_id",
        (started.isoformat(),)).fetchall()]
    if len(rows) < MIN_SAMPLES_FOR_LIVE_PACE:
        return float(DEFAULT_SECONDS_PER_QUESTION), "historical median"
    stamps = []
    for r in rows:
        try:
            stamps.append(datetime.fromisoformat(r))
        except ValueError:
            continue
    if len(stamps) < MIN_SAMPLES_FOR_LIVE_PACE:
        return float(DEFAULT_SECONDS_PER_QUESTION), "historical median"
    span = (stamps[-1] - stamps[0]).total_seconds()
    per = span / max(1, len(stamps) - 1)
    # Guard against a pause for coffee turning into a 20-minute "pace".
    per = max(20.0, min(300.0, per))
    return per, "this session"


def pacing(now: datetime | None = None) -> dict[str, Any]:
    """Where the session stands against the time the user actually asked for.

    Returned inline from submit_answer so the tutor never has to spend a round
    trip — and never has to guess — to know whether to keep going.
    """
    _ensure_table()
    now = now or datetime.now(timezone.utc)
    with conn() as db:
        row = db.execute(
            "SELECT started_at, planned_minutes, ended_at FROM session_clock WHERE id=1"
        ).fetchone()
        if row is None:
            return {
                "clock_running": False,
                "now_local": now.astimezone().strftime("%H:%M"),
                "note": ("No session clock. Call start_study_session with the minutes "
                         "the user actually has before asking questions."),
            }
        started = datetime.fromisoformat(row["started_at"])
        planned = int(row["planned_minutes"] or 0)
        asked = db.execute(
            "SELECT COUNT(*) FROM question_attempts WHERE datetime(date) >= datetime(?)",
            (started.isoformat(),)).fetchone()[0]
        per_q, pace_source = _observed_pace(db, started)
        backlog = db.execute(
            """SELECT COUNT(*) FROM knowledge_points
                WHERE next_review_date IS NOT NULL
                  AND date(next_review_date) <= date('now','localtime')
                  AND date(updated_at,'localtime') < date('now','localtime')"""
        ).fetchone()[0]

    elapsed_min = (now - started).total_seconds() / 60.0

    # A clock left running is worse than no clock. One session called
    # start_study_session at 09:29 — five minutes AFTER its last answer at
    # 09:24 — and never ended it, so the row sat "running" indefinitely and
    # every later reading was nonsense. Treat a clock that has overrun its plan
    # by a wide margin, or an unlimited one idle for hours, as expired.
    stale = (row["ended_at"] is None and (
        (planned > 0 and elapsed_min > planned + 60)
        or (planned <= 0 and elapsed_min > 240)))
    if stale:
        return {
            "clock_running": False,
            "now_local": now.astimezone().strftime("%H:%M"),
            "stale_clock": True,
            "note": (f"The last session clock started {elapsed_min/60:.1f} h ago and "
                     f"was never closed, so it says nothing about now. Call "
                     f"start_study_session with the minutes the user has before "
                     f"asking questions."),
        }

    out: dict[str, Any] = {
        "clock_running": row["ended_at"] is None,
        "now_local": now.astimezone().strftime("%H:%M"),
        "started_local": started.astimezone().strftime("%H:%M"),
        "elapsed_minutes": round(elapsed_min, 1),
        "questions_asked": asked,
        "seconds_per_question": round(per_q),
        "pace_source": pace_source,
        "overdue_backlog": backlog,
    }

    if planned <= 0:  # "as much time as we need"
        out["mode"] = "unlimited"
        out["goal"] = "clear the overdue backlog"
        out["questions_remaining"] = backlog
        out["estimated_minutes_to_clear"] = round(backlog * per_q / 60)
        out["guidance"] = (
            f"Unlimited session: {backlog} facts overdue, about "
            f"{round(backlog * per_q / 60)} min to clear at the current pace. "
            f"{asked} done, {elapsed_min:.0f} min elapsed. Keep going until the "
            f"backlog is empty or the user calls it; do NOT wrap up early."
        ) if backlog else (
            f"Unlimited session and the backlog is clear. {asked} questions in "
            f"{elapsed_min:.0f} min. Move to new material or ask what they want."
        )
        return out

    remaining_min = planned - elapsed_min
    usable = max(0.0, remaining_min - WRAP_UP_MINUTES)
    can_fit = int(usable * 60 // per_q)
    out.update({
        "mode": "timed",
        "planned_minutes": planned,
        "ends_local": (started + timedelta(minutes=planned)).astimezone().strftime("%H:%M"),
        "remaining_minutes": round(remaining_min, 1),
        "questions_remaining": max(0, can_fit),
    })

    if remaining_min <= 0:
        out["guidance"] = (f"Time is up ({planned} min). Wrap up now: recap what was "
                           f"weak and name what to hit next session.")
    elif remaining_min <= WRAP_UP_MINUTES:
        out["guidance"] = (f"{remaining_min:.0f} min left — finish the current item and "
                           f"wrap up.")
    else:
        out["guidance"] = (
            f"{remaining_min:.0f} of {planned} min left; room for about {can_fit} more "
            f"questions at {round(per_q)}s each ({asked} asked so far). Do NOT wind down "
            f"until under {WRAP_UP_MINUTES + 1} min remain."
        )
    return out


def plan_for(minutes: int) -> dict[str, Any]:
    """How many questions a stated duration actually buys, before it starts."""
    if minutes <= 0:
        with conn() as db:
            backlog = db.execute(
                """SELECT COUNT(*) FROM knowledge_points
                    WHERE next_review_date IS NOT NULL
                      AND date(next_review_date) <= date('now','localtime')
                      AND date(updated_at,'localtime') < date('now','localtime')"""
            ).fetchone()[0]
        return {"mode": "unlimited", "overdue_backlog": backlog,
                "question_budget": backlog,
                "estimated_minutes": round(backlog * DEFAULT_SECONDS_PER_QUESTION / 60)}
    usable = max(0, minutes - WRAP_UP_MINUTES)
    return {"mode": "timed", "planned_minutes": minutes,
            "question_budget": int(usable * 60 // DEFAULT_SECONDS_PER_QUESTION),
            "seconds_per_question": DEFAULT_SECONDS_PER_QUESTION}
