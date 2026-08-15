"""Is FSRS's forgetting model calibrated to THIS student? Measure, don't guess.

For every review of a previously-seen knowledge point, reconstruct what FSRS
predicted for recall probability (retrievability at the elapsed interval) and
compare against what actually happened. Buckets the predictions and reports
observed accuracy per bucket — a calibration curve.

If observed recall in the 0.9-predicted bucket is, say, 0.75, intervals are too
long for you (or your ratings too generous) and the default FSRS weights are
worth refitting. If the curve tracks the diagonal, leave the weights alone.

GATED: refuses to conclude anything below MIN_REVIEWS spaced reviews — early
numbers are noise, and refitting weights on noise makes scheduling worse.
Re-run quarterly:  .venv\\Scripts\\python.exe scripts\\fsrs_calibration_check.py
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.student_model import conn, initialize_database  # noqa: E402
from src.fsrs import _retrievability, deserialize  # noqa: E402

MIN_REVIEWS = 300  # spaced re-reviews needed before the curve means anything


def main() -> None:
    initialize_database()
    # Reconstruct per-point review history from knowledge_points state we have.
    # We can't replay historical states (only the latest is stored), so measure
    # on the TOPIC layer, where question_attempts is a full event log.
    with conn() as db:
        rows = db.execute(
            """SELECT qa.topic, qa.date, qa.result, t.fsrs_state
               FROM question_attempts qa
               JOIN topics t ON t.topic = qa.topic AND t.subtopic = ''
               ORDER BY qa.topic, qa.date"""
        ).fetchall()

    # Group attempts per topic; a "review" is any attempt after the first with
    # >= 1 day elapsed (same-day retries measure short-term memory, not retention).
    by_topic: dict[str, list] = defaultdict(list)
    for r in rows:
        by_topic[r["topic"]].append(r)

    points = []  # (predicted_retrievability, was_correct)
    for topic, attempts in by_topic.items():
        state = deserialize(attempts[-1]["fsrs_state"])
        stability = float(state.get("stability") or 0)
        if stability <= 0:
            continue
        for prev, cur in zip(attempts, attempts[1:]):
            try:
                t0 = datetime.fromisoformat(prev["date"])
                t1 = datetime.fromisoformat(cur["date"])
            except Exception:
                continue
            elapsed_days = (t1 - t0).total_seconds() / 86400.0
            if elapsed_days < 1.0:
                continue
            # NOTE: uses the CURRENT stability as a proxy for stability at the
            # time of review (historical states aren't stored). Biased toward
            # the mature value — stated here so nobody mistakes this for exact
            # replay. Good enough to detect gross miscalibration; not good
            # enough to fit weights from. A fit needs logged per-review state,
            # which record_knowledge_point could start persisting if this
            # check ever shows a real gap.
            pred = _retrievability(stability, elapsed_days)
            points.append((pred, cur["result"] == "correct"))

    n = len(points)
    print(f"spaced re-reviews measurable: {n} (gate: {MIN_REVIEWS})")
    if n < MIN_REVIEWS:
        print(
            "\nNOT ENOUGH DATA — no conclusion drawn. This is expected early in "
            "the campaign; re-run after a few months of daily reviews.\n"
            "(Refitting FSRS weights on this little data would make scheduling "
            "worse, not better.)"
        )
        return

    buckets: dict[str, list] = defaultdict(list)
    for pred, ok in points:
        key = f"{int(pred * 10) / 10:.1f}"
        buckets[key].append(ok)
    print("\npredicted-recall bucket -> observed accuracy (n)")
    gaps = []
    for key in sorted(buckets):
        obs = sum(buckets[key]) / len(buckets[key])
        mid = float(key) + 0.05
        gaps.append(abs(obs - mid))
        print(f"  {key}-{float(key)+0.1:.1f}   observed {obs:.2f}   (n={len(buckets[key])})")
    mean_gap = sum(gaps) / len(gaps)
    print(f"\nmean |observed - predicted| = {mean_gap:.3f}")
    print(
        "VERDICT: " + (
            "well calibrated — leave FSRS weights alone."
            if mean_gap < 0.10 else
            "miscalibrated — worth persisting per-review FSRS state and fitting "
            "personal weights. Open an issue/task for it; do not hand-tune."
        )
    )


if __name__ == "__main__":
    main()
