"""One-shot cleanup of test pollution written to the live DB on 2026-08-14/15.

What it removes (all verified against the attempt log in-session):
  * attempts #77-89 — Claude's car_next tests and latency benchmarks
    (topic Sepsis/Afib, answers like 'x' and 'lactate first', session mcp_session)
  * attempts #76 and #91 — the GPT's double-submit duplicates of the user's two
    REAL DVT/PE answers (#75, #90 are kept)
  * the fabricated KP 'Sepsis hour-1 bundle order: lactate first' (created and
    'mastered' cc=12 entirely by benchmark runs; the real fact has longer text)
  * restores the real Afib TEE knowledge point to weak/due-today (a fake
    'correct' had pushed it from 46-days-overdue-weak out to November)
  * recomputes topic counters for the three touched topics from surviving rows
  * drops the mastery_vector rows fed by fake data (recomputed on next submit)

Run once:  .venv\\Scripts\\python.exe scripts\\cleanup_20260815_test_pollution.py
Idempotent: re-running deletes nothing further and re-derives the same counters.
A timestamped safety copy is written next to the DB first.
"""
import shutil
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.config import settings  # noqa: E402

DB = Path(settings.sqlite_db_path)


def main() -> None:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = DB.with_name(f"student_model.pre_cleanup_{stamp}.db")
    shutil.copy(DB, backup)
    print(f"safety copy: {backup}")

    c = sqlite3.connect(str(DB))
    c.row_factory = sqlite3.Row
    today = datetime.now(timezone.utc).date().isoformat()

    n = c.execute(
        "DELETE FROM question_attempts WHERE attempt_id BETWEEN 77 AND 89"
    ).rowcount
    n2 = c.execute("DELETE FROM question_attempts WHERE attempt_id IN (76, 91)").rowcount
    print(f"deleted {n} test attempts + {n2} double-submit dupes")

    n3 = c.execute(
        "DELETE FROM knowledge_points WHERE topic='Sepsis' "
        "AND point='Sepsis hour-1 bundle order: lactate first'"
    ).rowcount
    print(f"deleted {n3} fabricated KP row")

    c.execute(
        """UPDATE knowledge_points
           SET times_seen=MAX(0,times_seen-1), times_correct=MAX(0,times_correct-1),
               consecutive_correct=0, status='weak', next_review_date=?
           WHERE topic='Afib with RVR'
             AND point LIKE 'Alternative to waiting 3-4 weeks: TEE%'
             AND status != 'weak'""",
        (today,),
    )
    print("restored Afib TEE KP to weak/due-today (if not already)")

    for topic in ("Sepsis", "Afib with RVR", "DVT/PE"):
        r = c.execute(
            """SELECT COUNT(*) n, SUM(result='correct') c, SUM(result='partial') p,
                      SUM(result='incorrect') i, MAX(date) last
               FROM question_attempts WHERE topic=?""",
            (topic,),
        ).fetchone()
        c.execute(
            """UPDATE topics SET times_seen=?, times_correct=?, times_partial=?,
                      times_incorrect=?, last_seen=?, next_review_date=?
               WHERE topic=? AND subtopic=''""",
            (r["n"], r["c"] or 0, r["p"] or 0, r["i"] or 0, r["last"], today, topic),
        )
        print(f"  {topic}: counters -> seen={r['n']} correct={r['c'] or 0}")

    c.execute("DELETE FROM mastery_vector WHERE topic_name IN ('Sepsis','Afib with RVR')")
    c.commit()
    total = c.execute("SELECT COUNT(*) FROM question_attempts").fetchone()[0]
    print(f"attempts total now: {total} (expect 76: the 74 restored + your 2 real answers)")


if __name__ == "__main__":
    main()
