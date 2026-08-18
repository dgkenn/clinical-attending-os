"""Merge duplicate knowledge points, preserving every point of history.

The record accumulated near-copies of the same fact before capture-time dedupe
existed (48 SAME-verdict pairs at last sweep). Each copy carries its own FSRS
schedule, so the same fact could be served twice and its history was split.

Merging uses the validated matcher (src/fact_matcher.py — three-way verdict,
structural conflict checks, zero false merges across 17,020 audited pairs) and
only ever acts on confident SAME verdicts. UNCERTAIN pairs are left alone.

Duplicates can chain (A~B, B~C), so SAME pairs are clustered transitively and
each cluster collapses to ONE canonical row:

  * canonical TEXT: the longest point in the cluster — detail is why the
    wordings differ, and the longest carries the most of it.
  * history is SUMMED (times_seen, times_correct, confidence_sum/n): every
    exposure the user actually had is retained, none double-counted since the
    rows were alternatives, not repeats.
  * schedule comes from the most recently REVIEWED row in the cluster — its
    next_review_date was computed by FSRS from the latest actual
    demonstration. The first version used "earliest date wins" instead, and
    the contradiction check caught it immediately: stale June dates from
    never-rereviewed copies overrode schedules earned by answering correctly
    the same day, making 27 just-answered facts due again.
  * status likewise follows the most recently reviewed row;
    consecutive_correct takes the minimum (conservative).
  * earliest created_at wins (the fact has been tracked since then).

    python scripts/merge_duplicate_facts.py --dry-run
    python scripts/merge_duplicate_facts.py --apply     (requires a backup)
"""
from __future__ import annotations

import argparse
import io
import itertools
import sqlite3
import sys
from pathlib import Path

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.config import settings              # noqa: E402
from src.fact_matcher import compare_facts   # noqa: E402

_STATUS_RANK = {"weak": 0, "learning": 1, "mastered": 2}


def find_clusters(rows) -> list[list[sqlite3.Row]]:
    """Union-find over confident SAME verdicts."""
    parent = {r["id"]: r["id"] for r in rows}

    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in itertools.combinations(rows, 2):
        if compare_facts(a["point"], b["point"]).verdict == "same":
            ra, rb = root(a["id"]), root(b["id"])
            if ra != rb:
                parent[ra] = rb

    groups: dict[int, list] = {}
    for r in rows:
        groups.setdefault(root(r["id"]), []).append(r)
    return [g for g in groups.values() if len(g) > 1]


def merge_plan(cluster) -> dict:
    """Compute the merged row for one cluster."""
    canonical = max(cluster, key=lambda r: len(r["point"] or ""))
    # The schedule authority is the most recently reviewed copy: FSRS computed
    # its dates from the latest real demonstration. A never-reviewed copy's
    # date is just the day it was imported and must not drag the fact due.
    reviewed = [r for r in cluster if (r["times_seen"] or 0) > 0]
    sched = (max(reviewed, key=lambda r: str(r["updated_at"] or "")) if reviewed
             else min(cluster, key=lambda r: str(r["next_review_date"] or "9999")))
    return {
        "keep_id": canonical["id"],
        "point": canonical["point"],
        # Every topic row keeps its own topic; the canonical row's topic wins.
        "topic": canonical["topic"],
        "times_seen": sum(r["times_seen"] or 0 for r in cluster),
        "times_correct": sum(r["times_correct"] or 0 for r in cluster),
        "consecutive_correct": min(r["consecutive_correct"] or 0 for r in cluster),
        "confidence_sum": sum(r["confidence_sum"] or 0 for r in cluster),
        "confidence_n": sum(r["confidence_n"] or 0 for r in cluster),
        "status": sched["status"] or "weak",
        "next_review_date": sched["next_review_date"],
        "interval_days": sched["interval_days"],
        "fsrs_state": sched["fsrs_state"],
        "created_at": min(str(r["created_at"] or "9999") for r in cluster),
        "drop_ids": [r["id"] for r in cluster if r["id"] != canonical["id"]],
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true")
    g.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    db = Path(settings.sqlite_db_path)
    if args.apply and not list(db.parent.glob("student_model_premerge_*.db")):
        raise SystemExit("refusing to --apply without a student_model_premerge_*.db "
                         "backup beside the database")

    con = sqlite3.connect(str(db))
    con.row_factory = sqlite3.Row
    rows = list(con.execute("SELECT * FROM knowledge_points"))
    clusters = find_clusters(rows)

    print(f"knowledge points: {len(rows)}")
    print(f"duplicate clusters: {len(clusters)} "
          f"({sum(len(c) for c in clusters)} rows -> {len(clusters)} rows)\n")

    plans = [merge_plan(c) for c in clusters]
    for c, p in zip(clusters, plans):
        print(f"cluster of {len(c)} -> keep: {p['point'][:86]}")
        for r in c:
            marker = "KEEP" if r["id"] == p["keep_id"] else "fold"
            print(f"    [{marker}] seen={r['times_seen']} ok={r['times_correct']} "
                  f"{r['status']:8} {r['point'][:70]}")
        print(f"    merged: seen={p['times_seen']} ok={p['times_correct']} "
              f"status={p['status']} next={p['next_review_date'][:10]}\n")

    if args.dry_run:
        print("(dry run — nothing written)")
        return

    with con:
        for p in plans:
            con.execute(
                """UPDATE knowledge_points
                      SET times_seen=?, times_correct=?, consecutive_correct=?,
                          confidence_sum=?, confidence_n=?, status=?,
                          next_review_date=?, interval_days=?, fsrs_state=?,
                          created_at=?, updated_at=CURRENT_TIMESTAMP
                    WHERE id=?""",
                (p["times_seen"], p["times_correct"], p["consecutive_correct"],
                 p["confidence_sum"], p["confidence_n"], p["status"],
                 p["next_review_date"], p["interval_days"], p["fsrs_state"],
                 p["created_at"], p["keep_id"]))
            con.executemany("DELETE FROM knowledge_points WHERE id=?",
                            [(i,) for i in p["drop_ids"]])

    n = con.execute("SELECT COUNT(*) FROM knowledge_points").fetchone()[0]
    print(f"merged {sum(len(p['drop_ids']) for p in plans)} rows away; "
          f"knowledge_points now {n}")
    # Sanity: total exposure history must be conserved.
    seen = con.execute("SELECT SUM(times_seen) FROM knowledge_points").fetchone()[0]
    print(f"total times_seen after merge: {seen}")


if __name__ == "__main__":
    main()
