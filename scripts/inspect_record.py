"""Inspect the study record with provenance. The troubleshooting console.

Why this exists: over one debugging session, three separate "findings" reported
to the user were artifacts rather than facts, and the user had to correct each
one from memory:

  * "112 topics overdue"  — 112 ROWS, 28 topic names. `topics` holds one row per
    (topic, subtopic).
  * "PE is 56 days overdue" — the day after PE was studied. Phantom rows (June
    fact-notes written as pseudo-topics, unreviewable by anything) were driving
    the topic's schedule.
  * "35 facts are gaps" — 23 had already been answered, most of them the day
    before.

The common failure was reading a number without asking where it came from. So
every number here carries provenance, artifacts are separated from real signal
by default, and `contradictions` exists specifically to catch "the queue is
telling you to study something you already did" — the exact class of bug that
took three user corrections to find.

    python scripts/inspect_record.py overview
    python scripts/inspect_record.py session [YYYY-MM-DD]
    python scripts/inspect_record.py why "PE"
    python scripts/inspect_record.py contradictions
    python scripts/inspect_record.py artifacts
"""
from __future__ import annotations

import argparse
import io
import re
import sqlite3
import sys
from pathlib import Path

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.config import settings  # noqa: E402


def db() -> sqlite3.Connection:
    con = sqlite3.connect(str(settings.sqlite_db_path))
    con.row_factory = sqlite3.Row
    return con


def _tool_calls_by_day() -> dict[str, dict[str, int]]:
    """Tool usage per day, from the per-name call log."""
    out: dict[str, dict[str, int]] = {}
    log = Path(settings.log_dir) / "tool_calls.log"
    if not log.exists():
        return out
    for line in log.read_text(encoding="utf-8", errors="replace").splitlines():
        parts = line.split("\t")
        if len(parts) >= 2:
            out.setdefault(parts[0][:10], {}).setdefault(parts[1], 0)
            out[parts[0][:10]][parts[1]] += 1
    return out


# --------------------------------------------------------------------------- #

def cmd_overview(_args) -> int:
    con = db()
    print("STUDY RECORD — with provenance\n")

    rows = con.execute("SELECT COUNT(*) n FROM topics").fetchone()["n"]
    names = con.execute("SELECT COUNT(DISTINCT topic) n FROM topics").fetchone()["n"]
    print(f"topics table      : {rows} rows / {names} distinct topic names")
    print("                    (rows != topics: one row per topic+subtopic —")
    print("                     counting rows overstated the backlog 4x once)")

    att = con.execute("SELECT COUNT(*) n FROM question_attempts").fetchone()["n"]
    real_q = con.execute(
        "SELECT COUNT(*) n FROM question_attempts WHERE question IS NOT NULL "
        "AND question <> '' AND question <> 'MCP submitted answer'").fetchone()["n"]
    print(f"\nattempts          : {att}  ({real_q} with the real question text)")

    kp_total = con.execute("SELECT COUNT(*) n FROM knowledge_points").fetchone()["n"]
    kp_studied = con.execute(
        "SELECT COUNT(*) n FROM knowledge_points WHERE times_seen > 0").fetchone()["n"]
    kp_due = con.execute(
        "SELECT COUNT(*) n FROM knowledge_points "
        "WHERE date(next_review_date) <= date('now')").fetchone()["n"]
    print(f"knowledge points  : {kp_total} total, {kp_studied} actually answered, {kp_due} due")
    print("                    (total-answered = imported/repaired, not studied)")

    from src.student_model import get_due_reviews
    due = get_due_reviews(limit=500)
    print(f"\ndue TOPICS (as the tutor sees them): {len(due)}")
    for d in due[:8]:
        print(f"   {d['topic'][:34]:34} {d['days_overdue']:3}d overdue")
    con.close()
    return 0


def cmd_session(args) -> int:
    con = db()
    day = args.date
    if not day:
        day = con.execute("SELECT date(MAX(date)) d FROM question_attempts").fetchone()["d"]
    print(f"SESSION — {day}\n")

    calls = _tool_calls_by_day().get(day, {})
    if calls:
        print("tools called:")
        for name, n in sorted(calls.items(), key=lambda x: -x[1]):
            print(f"   {name:32} {n}")
    else:
        print("tools called: (nothing logged — tool logging began 2026-08-17)")

    # The two failures that are invisible in the transcript.
    retrieval = sum(calls.get(t, 0) for t in
                    ("search_clinical_sources", "mcp_retrieval",
                     "answer_from_clinical_sources", "retrieval"))
    print(f"\ngrounded?         : {retrieval} retrieval calls "
          f"{'-- OK' if retrieval else '-- NO: questions came from model training'}")
    print(f"instructions      : {'fetched' if calls.get('get_claude_instructions') else 'NEVER FETCHED'}")

    att = con.execute(
        "SELECT COUNT(*) n, SUM(result='correct') ok FROM question_attempts "
        "WHERE date(date) = ?", (day,)).fetchone()
    kp_written = con.execute(
        "SELECT COUNT(*) n FROM knowledge_points "
        "WHERE date(updated_at) = ? AND times_seen > 0", (day,)).fetchone()["n"]
    print(f"\nattempts recorded : {att['n']}  ({att['ok'] or 0} correct)")
    print(f"facts recorded    : {kp_written}   <- from ANSWERING, excludes migrations")

    print("\nquestions asked:")
    for r in con.execute(
            "SELECT question, result, topic FROM question_attempts "
            "WHERE date(date) = ? ORDER BY attempt_id", (day,)):
        q = (r["question"] or "")[:96]
        print(f"   [{r['result'][:9]:9}] {r['topic'][:20]:20} {q}")
    con.close()
    return 0


def cmd_why(args) -> int:
    """Explain a topic's state: every row behind it, and what drives its schedule."""
    con = db()
    topic = args.topic
    print(f"WHY IS '{topic}' IN THE STATE IT IS?\n")

    rows = list(con.execute(
        "SELECT subtopic, times_seen, last_seen, next_review_date, mastery_score "
        "FROM topics WHERE topic = ? ORDER BY (subtopic = '') DESC", (topic,)))
    if not rows:
        print("  no rows in `topics` under that exact name")
    print(f"  {len(rows)} row(s) in `topics`:")
    for r in rows:
        kind = "PARENT (drives schedule)" if not (r["subtopic"] or "").strip() else "subtopic row"
        phantom = " <- PHANTOM: never reviewable" if (
            (r["subtopic"] or "").strip() and not r["times_seen"] and not r["last_seen"]) else ""
        print(f"    [{kind:24}] seen={r['times_seen']:2} last={str(r['last_seen'])[:10]:10} "
              f"next={str(r['next_review_date'])[:10]}{phantom}")

    n = con.execute("SELECT COUNT(*) n FROM question_attempts WHERE topic = ?",
                    (topic,)).fetchone()["n"]
    last = con.execute("SELECT MAX(date) d FROM question_attempts WHERE topic = ?",
                       (topic,)).fetchone()["d"]
    print(f"\n  answered {n} times, most recently {str(last)[:16]}")

    kps = list(con.execute(
        "SELECT point, status, times_seen, next_review_date FROM knowledge_points "
        "WHERE topic = ? ORDER BY status", (topic,)))
    print(f"\n  {len(kps)} knowledge point(s):")
    for k in kps[:12]:
        due = "DUE" if str(k["next_review_date"])[:10] <= str(
            con.execute("SELECT date('now') d").fetchone()["d"]) else "   "
        print(f"    {due} [{k['status']:8} seen={k['times_seen']}] {k['point'][:70]}")

    print("\n  NOTE: a topic with knowledge points is tracked at FACT level and")
    print("        intentionally drops out of the topic-level due queue.")
    con.close()
    return 0


def cmd_contradictions(_args) -> int:
    """Find queue entries that disagree with what was recently answered.

    This is the check that would have caught all three misreports. If something
    is due but was answered correctly in the last few days, either the schedule
    failed to advance or the queue is showing an artifact.
    """
    con = db()
    print("CONTRADICTIONS — queue says study it, history says you did\n")
    problems = 0

    from src.student_model import get_due_reviews
    for d in get_due_reviews(limit=500):
        r = con.execute(
            "SELECT MAX(date) last, COUNT(*) n FROM question_attempts "
            "WHERE topic = ? AND date >= datetime('now','-3 days')",
            (d["topic"],)).fetchone()
        if r["n"] and d["days_overdue"] > 3:
            problems += 1
            print(f"  TOPIC {d['topic']}: {d['days_overdue']}d overdue, but answered "
                  f"{r['n']}x on {str(r['last'])[:10]}")

    for k in con.execute(
            """SELECT topic, point, times_correct, times_seen, updated_at
               FROM knowledge_points
               WHERE date(next_review_date) <= date('now')
                 AND times_correct > 0
                 AND date(updated_at) >= date('now','-2 days')"""):
        problems += 1
        print(f"  FACT  [{k['topic']}] answered correctly {k['times_correct']}/"
              f"{k['times_seen']} on {str(k['updated_at'])[:10]} but is due again: "
              f"{k['point'][:60]}")

    print(f"\n{problems} contradiction(s)." if problems else "\nNone — queue agrees with history.")
    con.close()
    return 1 if problems else 0


def cmd_artifacts(_args) -> int:
    """Everything in the record that is NOT a product of studying."""
    con = db()
    print("ARTIFACTS — present in the data, not produced by studying\n")

    from src.student_model import _NON_TOPICS
    ph = list(con.execute(
        """SELECT topic, subtopic FROM topics
           WHERE subtopic <> '' AND subtopic IS NOT NULL
             AND times_seen = 0 AND last_seen IS NULL"""))
    print(f"phantom topic rows (fact notes as pseudo-topics): {len(ph)}")
    for r in ph[:5]:
        print(f"   [{r['topic']}] {r['subtopic'][:70]}")
    if ph:
        print("   -> fix: scripts/migrate_phantom_topic_rows.py")

    junk = list(con.execute(
        "SELECT DISTINCT topic FROM topics WHERE lower(topic) IN ({})".format(
            ",".join("?" * len(_NON_TOPICS))), _NON_TOPICS))
    print(f"\ndocument-structure topics: {len(junk)}  {[r['topic'] for r in junk]}")

    asked = list(con.execute(
        "SELECT topic, point, status FROM knowledge_points "
        "WHERE point LIKE '[asked]%' ORDER BY topic"))
    print(f"\nSELF-IDENTIFIED GAPS (questions YOU asked): {len(asked)}")
    print("   these are the highest-value signal in the record — unprompted,")
    print("   so they reflect what you actually hit, not what was served to you")
    for r in asked[:10]:
        print(f"   [{r['status']:8}] {r['topic'][:18]:18} {r['point'][:78]}")

    unstudied = con.execute(
        "SELECT COUNT(*) n FROM knowledge_points WHERE times_seen = 0").fetchone()["n"]
    print(f"\nknowledge points never answered (imported/repaired): {unstudied}")
    print("   -> these are real gaps, but they were not produced by a session")

    blank = con.execute(
        "SELECT COUNT(*) n FROM question_attempts WHERE question IS NULL "
        "OR question = '' OR question = 'MCP submitted answer'").fetchone()["n"]
    print(f"\nattempts with no question text: {blank}  (pre-dates the question fix)")
    con.close()
    return 0


def cmd_transcript(args) -> int:
    """Replay a session from the tool transcript, as conversation.

    The database only keeps what was successfully recorded, so anything the
    tutor did NOT write — a tangent, a question it forgot to submit — was
    invisible after the fact. A digoxin rabbit hole ran a whole session and
    left nothing to audit. This reads the raw call log instead, so what
    happened is legible whether or not it made it into a table.
    """
    import json
    path = Path(settings.log_dir) / "tool_transcript.jsonl"
    if not path.exists():
        print("no transcript yet — it starts recording on the next tool call")
        return 0

    day = args.date
    rows = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            e = json.loads(line)
        except Exception:
            continue
        if day and not e.get("ts", "").startswith(day):
            continue
        rows.append(e)
    if not rows:
        print(f"nothing in the transcript for {day or 'any date'}")
        return 0

    print(f"TRANSCRIPT — {day or 'all'}   ({len(rows)} calls)\n")
    for e in rows:
        ts, tool = e.get("ts", "")[11:19], e.get("tool", "?")
        a = e.get("args", {}) or {}
        res = e.get("result", {}) or {}
        if e.get("error"):
            print(f"  {ts}  !! {tool} FAILED: {e['error'][:90]}")
            continue
        if tool == "submit_answer":
            print(f"  {ts}  Q [{a.get('topic', '?')}] {str(a.get('question', ''))[:110]}")
            print(f"           A {str(a.get('user_answer', ''))[:110]}")
            kp = a.get("knowledge_points")
            n = len(kp) if isinstance(kp, list) else 0
            print(f"           graded={'correct' if a.get('is_correct') else 'incorrect'} "
                  f"conf={a.get('confidence_reported')} teach_back={a.get('teach_back_quality')} "
                  f"| facts sent={n} recorded={res.get('knowledge_points_recorded')}"
                  f"{' (DERIVED)' if res.get('knowledge_points_derived') else ''}")
        elif tool == "log_tangent":
            facts = a.get("facts") or []
            print(f"  {ts}  ~~ TANGENT [{a.get('topic')}] trigger={str(a.get('trigger'))[:60]}")
            for f in facts[:8]:
                print(f"           - {str(f)[:100]}")
        elif tool in ("search_clinical_sources", "mcp_retrieval",
                      "answer_from_clinical_sources"):
            print(f"  {ts}  >> retrieved: {str(a.get('query', ''))[:90]}")
        elif tool == "get_next_topic":
            warn = " [SETUP WARNING]" if res.get("setup_warning") else ""
            print(f"  {ts}  -> served topic: {res.get('topic', '?')} "
                  f"({res.get('reason', '')}){warn}")
        else:
            print(f"  {ts}     {tool}")
    return 0


def cmd_conversation(args) -> int:
    """Replay a session as the ACTUAL conversation, verbatim, with timestamps.

    `session` shows what the tutor recorded; this shows what was really said.
    The distinction matters because user_answer is the tutor's graded summary
    ("correctly identified lactulose, wrong mechanism") — its account of the
    user, not the user's words. Auditing a strange session needs the latter.
    """
    con = db()
    day = args.date or con.execute(
        "SELECT date(MAX(date)) d FROM question_attempts").fetchone()["d"]
    rows = list(con.execute(
        """SELECT time(date,'localtime') t, topic, question, result,
                  confidence_reported conf, user_answer, user_answer_verbatim,
                  tutor_response
           FROM question_attempts WHERE date(date,'localtime') = ?
           ORDER BY attempt_id""", (day,)))
    print(f"CONVERSATION — {day}  ({len(rows)} exchanges)\n")
    have_verbatim = 0
    for r in rows:
        print(f"[{r['t']}] {r['topic']}  ({r['result']}, conf {r['conf']})")
        print(f"  TUTOR ASKED : {(r['question'] or '')[:300]}")
        if r["user_answer_verbatim"]:
            have_verbatim += 1
            print(f"  YOU SAID    : {r['user_answer_verbatim'][:600]}")
        else:
            print(f"  (verbatim not captured — graded summary follows)")
            print(f"  GRADED AS   : {(r['user_answer'] or '')[:300]}")
        if r["tutor_response"]:
            print(f"  TUTOR SAID  : {r['tutor_response'][:600]}")
        print()
    if rows and not have_verbatim:
        print("NOTE: no verbatim capture in this session — the tutor is not yet")
        print("passing user_answer_verbatim/tutor_response on submit_answer.")
    con.close()
    return 0


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("overview").set_defaults(fn=cmd_overview)
    s = sub.add_parser("session"); s.add_argument("date", nargs="?"); s.set_defaults(fn=cmd_session)
    t = sub.add_parser("transcript"); t.add_argument("date", nargs="?"); t.set_defaults(fn=cmd_transcript)
    v = sub.add_parser("conversation"); v.add_argument("date", nargs="?"); v.set_defaults(fn=cmd_conversation)
    w = sub.add_parser("why"); w.add_argument("topic"); w.set_defaults(fn=cmd_why)
    sub.add_parser("contradictions").set_defaults(fn=cmd_contradictions)
    sub.add_parser("artifacts").set_defaults(fn=cmd_artifacts)
    args = ap.parse_args()
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
