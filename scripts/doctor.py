"""One-command system diagnosis (and repair) for Clinical Attending OS.

The ops console for this system is a Claude Code session driven from a phone —
so any future session must be able to assess EVERYTHING with one command and
fix the common failures with a second. No hunting through logs.

    .venv\\Scripts\\python.exe scripts\\doctor.py          # diagnose
    .venv\\Scripts\\python.exe scripts\\doctor.py --fix    # + restart what's down

Checks: local API, public Funnel endpoint, instructions version, scheduled
tasks, DB integrity + freshness, Drive backup age, repo bundle age, disk
space, git state, recent server-log errors.
Exit code 0 = all green; 1 = something needs attention (listed).
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import subprocess
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
PUBLIC = "https://john-desktop-pavilion-hampton.tail712dd4.ts.net/api"
LOCAL = "http://127.0.0.1:8010"

PROBLEMS: list[str] = []


def ok(label: str, detail: str = "") -> None:
    print(f"  [OK]   {label}" + (f" — {detail}" if detail else ""))


def bad(label: str, detail: str = "") -> None:
    PROBLEMS.append(label)
    print(f"  [FAIL] {label}" + (f" — {detail}" if detail else ""))


def http(url: str, timeout: int = 15) -> tuple[int, str]:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", "replace")[:500]
    except Exception as exc:
        return 0, str(exc)[:200]


def _server_start_utc() -> str | None:
    """UTC start time of the running MCP server, as an ISO string to seconds.

    Used to separate live tool errors from ones already fixed by a restart.
    Returns None if it cannot be determined, in which case every error is
    treated as current — failing loudly beats silently excusing a real fault.
    """
    out = ps("Get-NetTCPConnection -LocalPort 8011 -State Listen -EA SilentlyContinue | "
             "Select-Object -Expand OwningProcess -Unique | "
             "ForEach-Object { (Get-Process -Id $_ -EA SilentlyContinue).StartTime."
             "ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ss') }")
    for line in out.splitlines():
        line = line.strip()
        if len(line) == 19 and line[4] == "-" and line[10] == "T":
            return line
    return None


def ps(cmd: str) -> str:
    r = subprocess.run(["powershell", "-NoProfile", "-Command", cmd],
                       capture_output=True, text=True, timeout=60)
    return (r.stdout or "") + (r.stderr or "")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true",
                    help="restart the API task / server if down")
    args = ap.parse_args()
    now = datetime.now(timezone.utc)
    print(f"DOCTOR — {now.isoformat()[:19]}Z\n")

    # 1. Local API
    code, body = http(f"{LOCAL}/health", 10)
    if code == 200 and "clinical_attending_os" in body:
        ok("local API (8010)")
    else:
        bad("local API (8010)", body)
        if args.fix:
            print("       fixing: restarting ClinicalAttendingOS-API task...")
            ps("Stop-ScheduledTask -TaskName ClinicalAttendingOS-API -ErrorAction SilentlyContinue; "
               "Start-ScheduledTask -TaskName ClinicalAttendingOS-API")
            import time
            for _ in range(24):
                time.sleep(5)
                code, body = http(f"{LOCAL}/health", 5)
                if code == 200:
                    ok("local API after restart")
                    PROBLEMS.pop()
                    break
            else:
                print("       restart did NOT bring it back — check "
                      "storage/logs/api_server.log")

    # 2. Public endpoint (what ChatGPT sees)
    code, body = http(f"{PUBLIC}/health", 20)
    if code == 200 and "clinical_attending_os" in body:
        ok("public Funnel endpoint")
    else:
        bad("public Funnel endpoint", body)
        if args.fix:
            print("       fixing: re-adding funnel path /api -> 8010")
            ps('& "C:\Program Files\Tailscale\tailscale.exe" funnel --bg --set-path /api 8010')
            import time
            time.sleep(5)
            if http(f"{PUBLIC}/health", 15)[0] == 200:
                ok("public Funnel after repair"); PROBLEMS.pop()
        else:
            print("       (re-run with --fix, or: tailscale funnel status)")

    # 2b. MCP server (what phone/web Claude connects to)
    code, body = http("http://127.0.0.1:8011/health", 10)
    if code == 200:
        ok("MCP server (8011)")
    else:
        bad("MCP server (8011)", body)
        if args.fix:
            ps("Stop-ScheduledTask -TaskName ClinicalAttendingOS-MCP -ErrorAction SilentlyContinue; "
               "Start-ScheduledTask -TaskName ClinicalAttendingOS-MCP")
            import time
            for _ in range(24):
                time.sleep(5)
                if http("http://127.0.0.1:8011/health", 5)[0] == 200:
                    ok("MCP server after restart"); PROBLEMS.pop(); break
    code, _ = http(f"{PUBLIC.replace('/api', '')}/mcp/health", 20)
    if code == 200:
        ok("public MCP endpoint")
    else:
        bad("public MCP endpoint", f"HTTP {code}")
        if args.fix:
            print("       fixing: re-adding funnel path /mcp -> 8011")
            ps('& "C:\Program Files\Tailscale\tailscale.exe" funnel --bg --set-path /mcp 8011')

    # 3. Instructions version (fetch fully — http() truncates for display)
    try:
        with urllib.request.urlopen(f"{PUBLIC}/system_instructions", timeout=20) as r:
            payload = json.load(r)
        ok("live instructions", f"version {payload['version']}, {len(payload['instructions'])} chars")
    except Exception as exc:
        bad("live instructions", str(exc)[:150])

    # 4. Scheduled tasks
    out = ps("Get-ScheduledTask -TaskName 'ClinicalAttendingOS-*' | "
             "ForEach-Object { \"$($_.TaskName)=$($_.State)\" }")
    seen = {}
    for line in out.splitlines():
        if "=" in line:
            name, state = line.strip().split("=", 1)
            seen[name] = state
    for name, want in (("ClinicalAttendingOS-API", ("Running",)),
                       ("ClinicalAttendingOS-WeeklyBackup", ("Ready", "Running")),
                       ("ClinicalAttendingOS-MCP", ("Running",)),
                       ("ClinicalAttendingOS-WeeklyDigest", ("Ready", "Running"))):
        state = seen.get(name, "MISSING")
        if state in want:
            ok(f"task {name}", state)
        else:
            bad(f"task {name}", state)
            if args.fix and name in ("ClinicalAttendingOS-API", "ClinicalAttendingOS-MCP") and state != "MISSING":
                ps(f"Start-ScheduledTask -TaskName {name}")
                print(f"       fix attempted: started {name}")

    # 5. Database
    from src.config import settings
    db = Path(settings.sqlite_db_path)
    if not db.exists():
        bad("student DB", "missing")
    else:
        try:
            con = sqlite3.connect(str(db))
            integ = con.execute("PRAGMA integrity_check").fetchone()[0]
            n, newest = con.execute(
                "SELECT COUNT(*), MAX(date) FROM question_attempts").fetchone()
            kp = con.execute("SELECT COUNT(*) FROM knowledge_points").fetchone()[0]
            con.close()
            if integ == "ok":
                ok("student DB", f"integrity ok, {n} attempts (newest {str(newest)[:10]}), {kp} KPs")
            else:
                bad("student DB integrity", integ[:100])
        except Exception as exc:
            bad("student DB", str(exc)[:150])

    # 6. Drive backup freshness (daily task -> should be < 48h old)
    rclone = str(Path.home() / "rclone.exe")
    if Path(rclone).exists():
        r = subprocess.run([rclone, "lsl", "gdrive:tutor_backups/student_model_latest.db"],
                           capture_output=True, text=True, timeout=60)
        line = (r.stdout or "").strip().splitlines()
        if r.returncode == 0 and line:
            parts = line[-1].split()
            try:
                ts = datetime.fromisoformat(parts[1] + "T" + parts[2][:8])
                age_h = (datetime.now() - ts).total_seconds() / 3600
                (ok if age_h < 48 else bad)("Drive DB backup", f"{age_h:.0f}h old")
            except Exception:
                ok("Drive DB backup", "present (age unparsed)")
        else:
            bad("Drive DB backup", (r.stderr or "not found")[:120])
        r2 = subprocess.run([rclone, "lsl", "gdrive:tutor_backups/clinical-attending-os-latest.bundle"],
                            capture_output=True, text=True, timeout=60)
        if r2.returncode == 0 and r2.stdout.strip():
            ok("Drive repo bundle", "present")
        else:
            bad("Drive repo bundle", "missing")
    else:
        bad("rclone", "not at ~/rclone.exe")

    # 7. Disk space
    import shutil as _sh
    free_gb = _sh.disk_usage("C:\\").free / 1e9
    (ok if free_gb > 10 else bad)("disk space", f"{free_gb:.0f} GB free")

    # 8. Git state
    r = subprocess.run(["git", "-C", str(ROOT), "status", "--short"],
                       capture_output=True, text=True, timeout=30)
    dirty = [l for l in r.stdout.splitlines() if "units.json" not in l]
    r2 = subprocess.run(["git", "-C", str(ROOT), "rev-list", "--count",
                         "origin/main..HEAD"], capture_output=True, text=True, timeout=30)
    ahead = (r2.stdout or "0").strip()
    ok("git", f"{ahead} commits unpushed" + (f", {len(dirty)} dirty files" if dirty else ", tree clean"))
    # Push path: SSH key (~/.ssh/id_ed25519_github). Verify it still
    # authenticates — a broken push path is invisible until you need it.
    ssh_test = subprocess.run(
        ["ssh", "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=no",
         "-T", "git@github.com"], capture_output=True, text=True, timeout=45)
    if "successfully authenticated" in (ssh_test.stderr + ssh_test.stdout):
        ok("github push path (SSH)")
    else:
        bad("github push path (SSH)", (ssh_test.stderr or "no response")[:120])

    # 8b. Recording health — is the tutor actually writing BOTH layers?
    #
    # A full 13-question session once recorded every topic-level attempt and
    # zero knowledge points. Nothing errored; the fact-level layer (targeted
    # review, ambient triage, the miss queue) simply got nothing, and the only
    # way to notice was to hand-compare table counts afterwards. The failure is
    # silent by nature, so it needs an explicit check.
    db_path = Path(settings.sqlite_db_path)
    if db_path.exists():
        try:
            con = sqlite3.connect(str(db_path))
            # Judge the MOST RECENT study day, not a 7-day blur. "Did my last
            # session record properly?" is the actual question, and averaging it
            # with older days both hides a fresh regression and keeps flagging
            # one that has already been fixed.
            last_day = con.execute(
                "SELECT date(MAX(date)) FROM question_attempts").fetchone()[0]
            if not last_day:
                ok("recording health", "no sessions recorded yet")
            else:
                attempts = con.execute(
                    "SELECT COUNT(*) FROM question_attempts WHERE date(date) = ?",
                    (last_day,)).fetchone()[0]
                kps = con.execute(
                    "SELECT COUNT(*) FROM knowledge_points WHERE date(updated_at) = ?",
                    (last_day,)).fetchone()[0]
                blank_q = con.execute(
                    "SELECT COUNT(*) FROM question_attempts WHERE date(date) = ? "
                    "  AND (question IS NULL OR question = '' "
                    "       OR question = 'MCP submitted answer')",
                    (last_day,)).fetchone()[0]
                # Count only facts the TUTOR wrote, not ones a migration or
                # repair script stamped. Reading the raw table made a maintenance
                # script look like healthy tutor behaviour and reported OK when
                # the tutor had in fact recorded nothing.
                kps_from_study = con.execute(
                    "SELECT COUNT(*) FROM knowledge_points "
                    "WHERE date(updated_at) = ? AND times_seen > 0",
                    (last_day,)).fetchone()[0]
                label = f"recording health ({last_day})"
                if kps_from_study == 0 and attempts:
                    bad(label, f"{attempts} attempts but 0 knowledge points came "
                               "from answering — the fact-level layer is not being written")
                elif kps == 0:
                    bad(label, f"{attempts} attempts but 0 knowledge points — the "
                               "fact-level layer is not being written")
                else:
                    ratio = kps / max(attempts, 1)
                    # Under ~1 KP per answer means most questions recorded no facts.
                    (ok if ratio >= 1.0 else bad)(
                        label, f"{attempts} attempts, {kps} KPs ({ratio:.1f} per answer)")
                if blank_q:
                    bad("question text missing",
                        f"{blank_q}/{attempts} attempts on {last_day} have no question")
            con.close()
        except Exception as exc:
            bad("recording health", str(exc)[:150])

    # 8b-ii. Is the fact-level queue actually being CONSUMED?
    #
    # Capture, scheduling and serving are three separate things, and only the
    # first two are self-evident. The queue can be perfectly maintained while
    # the tutor never draws from it: 142 due facts sat unserved through a full
    # session that ran topic reviews instead. Nothing errors — the backlog just
    # grows, and the most valuable material (facts already known to be missed)
    # is the part that never gets re-asked.
    if db_path.exists():
        try:
            con = sqlite3.connect(str(db_path))
            due_kp = con.execute(
                "SELECT COUNT(*) FROM knowledge_points "
                "WHERE date(next_review_date) <= date('now')").fetchone()[0]
            weak_kp = con.execute(
                "SELECT COUNT(*) FROM knowledge_points WHERE status='weak'").fetchone()[0]
            served = con.execute(
                "SELECT COUNT(*) FROM knowledge_points "
                "WHERE date(updated_at) = (SELECT date(MAX(date)) FROM question_attempts)"
            ).fetchone()[0]
            con.close()
            detail = f"{due_kp} facts due, {weak_kp} weak, {served} touched last session"
            # A big backlog with nothing touched last session means the tutor is
            # not calling get_due_knowledge_points.
            (bad if (due_kp > 40 and served == 0) else ok)("fact queue", detail)
        except Exception as exc:
            bad("fact queue", str(exc)[:150])

        # 8b-ii. Currency: has the volatile material been rechecked lately?
        #
        # The maintainer's concern, verbatim: "something to watch for is
        # management as these can change drastically with new studies." A
        # one-off audit cannot answer that — it is stale the moment a trial
        # reads out. Facts carry a `volatility` band and a
        # `last_currency_check` stamp so staleness is measurable instead of
        # remembered, and the next audit can target the overdue slice rather
        # than re-reading 6,300 facts that mostly cannot have changed.
        try:
            con = sqlite3.connect(str(db_path))
            cols = {r[1] for r in con.execute("PRAGMA table_info(kp_catalog)")}
            if "volatility" not in cols:
                ok("fact currency", "not yet tagged — run scripts/tag_volatility.py")
            else:
                cutoff = (datetime.now(timezone.utc) - timedelta(days=365)).isoformat()
                n_high = con.execute(
                    "SELECT COUNT(*) FROM kp_catalog WHERE volatility='high'").fetchone()[0]
                overdue = con.execute(
                    "SELECT COUNT(*) FROM kp_catalog WHERE volatility='high' AND "
                    "(last_currency_check IS NULL OR last_currency_check < ?)",
                    (cutoff,)).fetchone()[0]
                detail = (f"{n_high} high-volatility (management/dosing/threshold) "
                          f"facts, {overdue} unchecked in 12 months")
                # Warn only when most of the volatile deck is unverified; a
                # trickle going overdue is normal and should not cry wolf.
                (bad if (n_high and overdue > n_high * 0.75) else ok)("fact currency", detail)
            con.close()
        except Exception as exc:
            bad("fact currency", str(exc)[:150])

    # 8b-iii. Does the queue agree with the history?
    #
    # Three separate "findings" reported to the user during one debugging
    # session were artifacts, and the user had to correct each from memory
    # ("I already did PE today"). Every one of them was the same shape: the
    # queue asking for something the history says was already done. That is
    # cheap to check automatically and expensive to notice by hand.
    try:
        from src.student_model import get_due_reviews
        con = sqlite3.connect(str(db_path))
        clashes = 0
        for d in get_due_reviews(limit=500):
            n = con.execute(
                "SELECT COUNT(*) FROM question_attempts WHERE topic = ? "
                "AND date >= datetime('now','-3 days')", (d["topic"],)).fetchone()[0]
            if n and d["days_overdue"] > 3:
                clashes += 1
        clashes += con.execute(
            # `date(next_review_date) <= date(updated_at)` is the whole test: a
            # schedule that did not ADVANCE past the answer. A fact answered
            # correctly yesterday and due today is spaced repetition working —
            # a first correct on a fragile fact earns stability under 1.0 and a
            # one-day interval by design. Without that clause this reported
            # four false positives in one run, which is how a check that exists
            # to catch real artifacts becomes noise that gets ignored.
            """SELECT COUNT(*) FROM knowledge_points
               WHERE date(next_review_date) <= date('now') AND times_correct > 0
                 AND date(updated_at) >= date('now','-2 days')
                 AND date(next_review_date) <= date(updated_at)""").fetchone()[0]
        con.close()
        (ok if clashes == 0 else bad)(
            "queue vs history",
            "agrees" if clashes == 0 else
            f"{clashes} items are due despite being answered recently "
            "(run: inspect_record.py contradictions)")
    except Exception as exc:
        bad("queue vs history", str(exc)[:150])

    # 8b-iv. Did the user tell the tutor about a problem? Feedback named
    # mid-session used to evaporate — prose never reaches the backend. The
    # tutor now relays it to user_feedback.log; surface anything present so a
    # maintenance session cannot miss it.
    # Handled items are moved to user_feedback.resolved.log with a note on what
    # was done, so this reports what still NEEDS attention rather than a running
    # total that only ever grows. A permanent red light gets ignored, and this
    # channel has now caught a real problem before an audit did — it has to stay
    # worth reading.
    fb = ROOT / "storage" / "logs" / "user_feedback.log"
    if fb.exists() and fb.stat().st_size > 0:
        entries = [l for l in fb.read_text(encoding="utf-8", errors="replace").splitlines() if l.strip()]
        bad("user feedback waiting", f"{len(entries)} unresolved — read storage/logs/user_feedback.log")
        for e in entries[-3:]:
            parts = e.split("	")
            print(f"        {parts[0][:16]}  {parts[1][:90] if len(parts)>1 else e[:90]}")
    else:
        resolved = ROOT / "storage" / "logs" / "user_feedback.resolved.log"
        n = 0
        if resolved.exists():
            n = len([l for l in resolved.read_text(encoding="utf-8", errors="replace").splitlines()
                     if l.strip()])
        ok("user feedback", f"none waiting ({n} resolved to date)")

    # 8c. What the tutor actually called (per-tool-name log)
    tool_log = ROOT / "storage" / "logs" / "tool_calls.log"
    if tool_log.exists():
        from collections import Counter
        all_lines = tool_log.read_text(encoding="utf-8", errors="replace").splitlines()
        lines = all_lines[-400:]
        # Grounding is judged over the MOST RECENT STUDY DAY, not the rolling
        # 400-call window. The window spans several sessions, so sessions that
        # predate a behaviour change keep dragging the verdict down and the
        # check stops describing current behaviour — the same reason the
        # recording-health check is scoped per-day.
        study_days = sorted({l.split("	")[0][:10] for l in all_lines
                             if "	submit_answer	" in l or "	car_next	" in l})
        last_study_day = study_days[-1] if study_days else None
        recent = [l for l in all_lines
                  if last_study_day and l.startswith(last_study_day)]
        gcounts = Counter()
        for ln in recent:
            parts = ln.split("	")
            if len(parts) >= 2:
                gcounts[parts[1]] += 1
        counts, errors, stale_errors = Counter(), Counter(), Counter()
        # An error is only a PROBLEM if it can still happen. The 400-call window
        # spans days, so a bug fixed an hour ago keeps failing the check until
        # 400 fresh calls push it out — car_next's strict-bool validation error
        # was reported as a live problem for exactly this reason after the
        # schema had already been widened. Errors from before the running
        # servers started are history: report them, do not fail on them.
        boot = _server_start_utc()
        for ln in lines:
            parts = ln.split("\t")
            if len(parts) >= 3:
                counts[parts[1]] += 1
                if parts[2] == "ERROR":
                    when = parts[0][:19]
                    if boot and when < boot:
                        stale_errors[parts[1]] += 1
                    else:
                        errors[parts[1]] += 1
        if counts:
            top = ", ".join(f"{n}x{c}" for n, c in counts.most_common(5))
            ok("tool calls (last 400)", top)
            if errors:
                bad("tool call errors (since restart)",
                    ", ".join(f"{n}: {c}" for n, c in errors.most_common(5)))
            elif stale_errors:
                ok("tool call errors",
                   "none since restart; "
                   + ", ".join(f"{n}: {c}" for n, c in stale_errors.most_common(3))
                   + " before it (already addressed)")

            # Was the session GROUNDED? The cardinal rule is that every question
            # comes from the corpus, never from model training. A 32-question
            # session once ran with zero retrieval calls: the questions looked
            # clinically fine, so nothing seemed wrong, but not one was drawn
            # from the vetted sources and none could be cited.
            # Grounding now arrives two ways, and the check must count both.
            # get_next_topic attaches source passages server-side, which removed
            # the tutor's NEED to call search_clinical_sources — so counting
            # only explicit calls reported a correctly-grounded session as
            # "ZERO retrieval calls". The fix had hidden its own evidence.
            explicit = sum(
                gcounts.get(t, 0) for t in
                ("search_clinical_sources", "mcp_retrieval",
                 "answer_from_clinical_sources", "retrieval")
            )
            delivered = gcounts.get("_sources_delivered", 0)
            answers = gcounts.get("submit_answer", 0) + gcounts.get("car_next", 0)
            total = explicit + delivered
            detail = (f"[{last_study_day}] {delivered} topics served with sources, "
                      f"{explicit} explicit retrieval calls, {answers} answers")
            if answers == 0:
                ok("grounding", "no answers recorded in this window")
            elif total == 0:
                bad("grounding",
                    f"{answers} answers with NO sources delivered and NO retrieval "
                    "calls — questions came from model training, not the corpus")
            elif total >= answers * 0.5:
                ok("grounding", detail)
            else:
                bad("grounding", detail + " — under half of answers had grounding")
            # Honest limit: delivery proves the passages reached the tutor, not
            # that the question was built from them. `grounded_in` on
            # submit_answer is the field that evidences actual use.
            cited = gcounts.get("_grounded_declared", 0)
            if answers:
                print(f"        (grounding declared on {cited}/{answers} answers)")

            # Presence is not usefulness. A session declared grounding on every
            # answer while 11 of 17 citations read "<Topic> knowledge point
            # bank" — the system's own fact table, which is precisely what
            # needed corroborating — and this check called it green. Meanwhile
            # the one answer with real page numbers cited Surviving Sepsis for
            # dose thresholds the guideline does not contain. Count what the
            # citations actually say.
            try:
                from src.answer_evidence import citation_quality
                con2 = sqlite3.connect(str(db_path))
                con2.row_factory = sqlite3.Row
                kinds = Counter()
                for row in con2.execute(
                        "SELECT grounded_in FROM question_attempts "
                        "WHERE date(date,'localtime') = ?", (last_study_day,)):
                    kinds[citation_quality(row["grounded_in"])[0]] += 1
                con2.close()
                total_c = sum(kinds.values())
                if total_c:
                    real = kinds.get("real", 0)
                    junk = kinds.get("self_referential", 0) + kinds.get("vague", 0)
                    detail_c = (f"{real}/{total_c} cite a real source, "
                                f"{junk} self-referential/vague, "
                                f"{kinds.get('empty', 0)} empty")
                    (bad if junk > real else ok)("citation quality", detail_c)
            except Exception as exc:
                bad("citation quality", str(exc)[:120])

            # Did the tutor load its instructions at all? Everything else
            # degrades from this one omission.
            if counts.get("get_claude_instructions", 0) == 0:
                bad("tutor instructions",
                    "get_claude_instructions never called — the tutor ran "
                    "without its instructions (check the Project bootstrap)")
            else:
                ok("tutor instructions", "fetched")
        else:
            ok("tool calls", "log present, no calls yet")
    else:
        ok("tool calls", "no calls logged yet (log is created on first call)")

    # 9. Recent server-log errors
    log = ROOT / "storage" / "logs" / "api_server.log"
    if log.exists():
        tail = log.read_text(encoding="utf-8", errors="replace").splitlines()[-200:]
        errs = [l for l in tail if "Traceback" in l or "ERROR" in l]
        (ok if not errs else bad)("server log (last 200 lines)",
                                  f"{len(errs)} error lines" if errs else "clean")
        for e in errs[-3:]:
            print("       ", e[:120])

    print()
    if PROBLEMS:
        print(f"PROBLEMS ({len(PROBLEMS)}): " + "; ".join(PROBLEMS))
        sys.exit(1)
    print("ALL GREEN")


if __name__ == "__main__":
    main()
