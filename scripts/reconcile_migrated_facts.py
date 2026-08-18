"""Give migrated facts the schedule their real answers earned.

The phantom-row migration imported 35 June-era missed facts into
knowledge_points as "weak, due today". That was too blunt: the user pointed
out they had already covered most of them, and the attempt history agrees —
23 of the 35 map onto questions actually asked, most on 2026-08-17.

"Weak and due" is right for the ones that were answered WRONG. It is wrong for
the ones answered CORRECTLY: it would re-drill demonstrated knowledge and bury
the genuine gaps underneath it, which is the opposite of what the fact queue is
for.

So each migrated fact is linked to the attempt that actually tested it and
recorded through the normal FSRS path with that attempt's real result and
confidence — not a fabricated one. Linking is by term overlap against the
question plus the user's answer, at a deliberately conservative threshold;
anything below it keeps the honest default of weak-and-due, because failing to
re-drill a known gap is worse than re-drilling something once more.

    python scripts/reconcile_migrated_facts.py --dry-run
    python scripts/reconcile_migrated_facts.py --apply
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
from src.student_model import conn, record_knowledge_point  # noqa: E402

# Validated by inspection: at 0.40 the links are real ("SIADH diagnosis" ->
# the small-cell/Na-118 question, "DKA: do not start insulin if K+<3.3" -> the
# DKA/K-3.1 question). Below it, matches start being topical coincidence.
THRESHOLD = 0.40

_STOP = set(
    "the a an of to in for and or with not is are be as on at by from if this "
    "that what which when why how do does you your it its more than less most "
    "only".split()
)


def _toks(s: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", (s or "").lower())
            if len(w) > 3 and w not in _STOP}


def main() -> None:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true")
    g.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    with conn() as db:
        db.row_factory = sqlite3.Row
        facts = list(db.execute(
            """SELECT id, topic, point FROM knowledge_points
               WHERE date(created_at) = date('now') AND status = 'weak'
                 AND times_seen = 0"""))
        attempts = list(db.execute(
            """SELECT question, user_answer, topic, result, confidence_reported, date
               FROM question_attempts"""))

    linked, unlinked = [], []
    for f in facts:
        ft = _toks(f["point"])
        best_score, best = 0.0, None
        for a in attempts:
            ct = _toks((a["question"] or "") + " " + (a["user_answer"] or ""))
            score = len(ft & ct) / len(ft) if ft else 0.0
            # Same-topic evidence is stronger than a chance term overlap.
            if a["topic"] == f["topic"]:
                score += 0.05
            if score > best_score:
                best_score, best = score, a
        (linked if best_score >= THRESHOLD else unlinked).append((best_score, f, best))

    right = [x for x in linked if x[2]["result"] == "correct"]
    wrong = [x for x in linked if x[2]["result"] != "correct"]
    print(f"migrated facts pending reconciliation : {len(facts)}")
    print(f"  linked to a real attempt            : {len(linked)}")
    print(f"     answered CORRECTLY (schedule forward): {len(right)}")
    print(f"     answered WRONG (stay weak + due)     : {len(wrong)}")
    print(f"  no confident link (stay weak + due)  : {len(unlinked)}")

    if args.dry_run:
        print("\nWOULD SCHEDULE FORWARD (answered correctly):")
        for s, f, a in sorted(right, key=lambda x: -x[0]):
            print(f"  [{s:.0%} {str(a['date'])[:10]}] {f['point'][:82]}")
        print("\nWOULD STAY WEAK (answered wrong):")
        for s, f, a in sorted(wrong, key=lambda x: -x[0]):
            print(f"  [{s:.0%} {str(a['date'])[:10]}] {f['point'][:82]}")
        print("\n(dry run — nothing written)")
        return

    # Remove the placeholder rows, then re-record through the real FSRS path so
    # stability/difficulty/next_review are computed rather than hand-set.
    with conn() as db:
        db.executemany("DELETE FROM knowledge_points WHERE id = ?",
                       [(f["id"],) for _, f, _ in linked])

    for _, f, a in linked:
        record_knowledge_point(
            topic=f["topic"],
            point=f["point"],
            is_correct=(a["result"] == "correct"),
            confidence=a["confidence_reported"],
            mistake_type="recall" if a["result"] != "correct" else "other",
        )

    with conn() as db:
        db.row_factory = sqlite3.Row
        n_due = db.execute(
            "SELECT COUNT(*) n FROM knowledge_points "
            "WHERE date(next_review_date) <= date('now')").fetchone()["n"]
        total = db.execute("SELECT COUNT(*) n FROM knowledge_points").fetchone()["n"]
    print(f"\nreconciled {len(linked)} facts against their real answers")
    print(f"knowledge_points: {total} total, {n_due} due now")


if __name__ == "__main__":
    main()
