"""Weekly learning digest: coverage velocity, accuracy, calibration, load forecast.

Writes storage/logs/digest_latest.md (plus a dated copy) and, when rclone is
available, uploads to gdrive:tutor_backups/digest_latest.md so the report is
readable from a phone. Registered as the ClinicalAttendingOS-WeeklyDigest
scheduled task (Sundays 03:10, after the backup).

Read it Monday morning: it answers "am I on pace, where am I weak, and is my
confidence honest?" — the three questions that decide what this week's
sessions should do.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.config import settings  # noqa: E402
from src.student_model import conn, initialize_database  # noqa: E402
from src.mcp_endpoints import get_mastery_map, get_calibration_report  # noqa: E402


def _review_load_forecast(days: int = 14) -> list[tuple[str, int]]:
    """Knowledge points coming due per day for the next `days` days."""
    today = datetime.now(timezone.utc).date()
    out = []
    with conn() as db:
        for i in range(days):
            day = (today + timedelta(days=i)).isoformat()
            n = db.execute(
                "SELECT COUNT(*) FROM knowledge_points WHERE next_review_date = ?",
                (day,),
            ).fetchone()[0]
            out.append((day, n))
    return out


def main() -> None:
    initialize_database()
    now = datetime.now(timezone.utc)
    week_ago = (now - timedelta(days=7)).isoformat()

    with conn() as db:
        attempts_week = db.execute(
            "SELECT COUNT(*), SUM(result='correct') FROM question_attempts WHERE date >= ?",
            (week_ago,),
        ).fetchone()
        kp_week = db.execute(
            "SELECT COUNT(*) FROM knowledge_points WHERE updated_at >= ?", (week_ago,)
        ).fetchone()[0]
        overdue_now = db.execute(
            "SELECT COUNT(*) FROM knowledge_points WHERE next_review_date <= ? AND status != 'mastered'",
            (now.date().isoformat(),),
        ).fetchone()[0]

    mm = get_mastery_map()
    cal = mm.get("calibration") or get_calibration_report(30)
    kp = mm.get("knowledge_points", {})
    n_att = attempts_week[0] or 0
    n_corr = attempts_week[1] or 0

    lines = [
        f"# Weekly digest — {now.date().isoformat()}",
        "",
        "## This week",
        f"- Attempts: **{n_att}** ({n_corr} correct, "
        f"{round(n_corr / n_att * 100) if n_att else 0}%)",
        f"- Knowledge points touched: **{kp_week}**",
        f"- Overdue right now: **{overdue_now}** knowledge points",
        "",
        "## Campaign",
        f"- Facts tracked: **{kp.get('facts_tracked', 0)}** of ~{kp.get('catalog_total', 0)} "
        f"catalog ({kp.get('catalog_pct', 0)}%) — mastered {kp.get('mastered', 0)}, "
        f"learning {kp.get('learning', 0)}, weak {kp.get('weak', 0)}",
        f"- Blueprint topics studied: {mm.get('topics_studied', 0)}/"
        f"{mm.get('total_curriculum_topics', 0)} "
        f"(+{mm.get('topics_studied_off_blueprint', 0)} off-blueprint)",
        f"- Critical care: {mm.get('critical_care', {}).get('coverage_pct', 0)}% | "
        f"On-call approaches: {mm.get('on_call_approaches', {}).get('coverage_pct', 0)}%",
        f"- Weakest domains: {', '.join(d[:40] for d in mm.get('weakest_domains', [])[:3])}",
        "",
        "## Calibration (30d)",
        f"- Reading: **{cal.get('reading', '?')}** "
        f"(gap {cal.get('overconfidence_gap')}, n={cal.get('attempts_with_confidence', 0)})",
    ]
    for bucket, label in (("low_1_2", "unsure (1-2)"), ("mid_3", "mid (3)"), ("high_4_5", "confident (4-5)")):
        b = cal.get("by_confidence", {}).get(bucket, {})
        lines.append(f"  - {label}: {b.get('n', 0)} answers, accuracy {b.get('accuracy')}")
    oc = cal.get("overconfident_points", [])
    if oc:
        lines.append("- Drill these overconfident facts first:")
        for p in oc[:5]:
            lines.append(f"  - {p['topic']}: {p['point'][:90]}")
    lines += ["", "## Review load, next 14 days", "```"]
    for day, n in _review_load_forecast():
        lines.append(f"{day}  {'#' * min(n, 60)} {n}")
    lines += ["```", ""]

    log_dir = Path(settings.log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)
    latest = log_dir / "digest_latest.md"
    dated = log_dir / f"digest_{now.strftime('%Y%m%d')}.md"
    text = "\n".join(lines)
    latest.write_text(text, encoding="utf-8")
    dated.write_text(text, encoding="utf-8")
    print(f"wrote {latest}")

    rclone = str(Path.home() / "rclone.exe")
    if not Path(rclone).exists():
        rclone = shutil.which("rclone") or ""
    if rclone:
        try:
            subprocess.run(
                [rclone, "copyto", str(latest), "gdrive:tutor_backups/digest_latest.md"],
                capture_output=True, text=True, timeout=120,
            )
            print("uploaded to gdrive:tutor_backups/digest_latest.md")
        except Exception as exc:
            print(f"(Drive upload skipped: {exc})")


if __name__ == "__main__":
    main()
