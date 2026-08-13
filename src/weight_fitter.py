"""Fit reranking weights against the gold-set MRR@5.

Strategy: deterministic coordinate-descent random restarts. Avoids scipy
to stay free of heavy numerical deps; converges quickly on the 11-D weight
vector defined in `reranking.DEFAULT_WEIGHTS`.

CLI:
    python -m src.weight_fitter
    python -m src.weight_fitter --max-queries 50 --restarts 8
"""

from __future__ import annotations

import argparse
import json
import random
import statistics
from copy import deepcopy
from pathlib import Path
from typing import Any

from .config import settings
from .eval_runner import GOLD_PATH, _evaluate_case
from .reranking import DEFAULT_WEIGHTS, load_weights


WEIGHT_BOUNDS = {
    "vector": (0.0, 0.6),
    "bm25": (0.0, 0.4),
    "keyword": (0.0, 0.6),
    "source_priority": (0.0, 0.4),
    "library_priority": (0.0, 0.4),
    "topic_score": (0.0, 0.3),
    "phrase_score": (0.0, 0.4),
    "mode_bonus": (0.0, 0.4),
    "high_yield": (0.0, 0.3),
    "cross_encoder": (0.0, 0.6),
    "basics_source_boost": (1.0, 8.0),
}


def _output_path() -> Path:
    return Path(settings.chroma_dir).parent / "reranking_weights.json"


def _score_weights(weights: dict[str, float], cases: list[dict], use_cross_encoder: bool) -> float:
    _output_path().write_text(json.dumps(weights), encoding="utf-8")
    load_weights.cache_clear()
    rrs = []
    for c in cases:
        row = _evaluate_case(c, use_cross_encoder=use_cross_encoder)
        rrs.append(row["rr5"])
    return statistics.mean(rrs) if rrs else 0.0


def fit_kfold(
    k: int = 5,
    iters_per_restart: int = 8,
    use_cross_encoder: bool = False,
    seed: int = 0,
) -> dict[str, Any]:
    """K-fold cross-validated weight fit.

    For each fold: hold out 1/k as dev, fit on the other k-1/k via random
    restart coord-descent, evaluate on dev. Average held-out MRR@5 across
    folds. Only commit weights if held-out MRR@5 beats the default-weights
    held-out MRR@5.
    """
    if not GOLD_PATH.exists():
        raise SystemExit(f"gold set missing at {GOLD_PATH}")
    cases = json.loads(GOLD_PATH.read_text(encoding="utf-8"))["queries"]
    rng = random.Random(seed)
    indices = list(range(len(cases)))
    rng.shuffle(indices)
    fold_size = max(1, len(cases) // k)
    folds = [indices[i * fold_size : (i + 1) * fold_size] for i in range(k)]
    # any leftover go to last fold
    if len(indices) > k * fold_size:
        folds[-1].extend(indices[k * fold_size :])

    initial_path = _output_path()
    backup = initial_path.read_text(encoding="utf-8") if initial_path.exists() else None

    fold_holdout_default: list[float] = []
    fold_holdout_fit: list[float] = []
    aggregated_weights: list[dict[str, float]] = []

    try:
        for fold_idx, dev_idxs in enumerate(folds):
            train_cases = [cases[i] for i in indices if i not in set(dev_idxs)]
            dev_cases = [cases[i] for i in dev_idxs]

            # Default-weight baseline on dev
            _output_path().write_text(json.dumps(DEFAULT_WEIGHTS), encoding="utf-8")
            load_weights.cache_clear()
            default_dev_score = sum(_evaluate_case(c, use_cross_encoder=use_cross_encoder)["rr5"] for c in dev_cases) / max(1, len(dev_cases))
            fold_holdout_default.append(default_dev_score)

            # Coord-descent on train
            current = dict(DEFAULT_WEIGHTS)
            current_train_score = _score_weights(current, train_cases, use_cross_encoder)
            best_train = current
            best_train_score = current_train_score
            for it in range(iters_per_restart):
                key = rng.choice(list(WEIGHT_BOUNDS.keys()))
                lo, hi = WEIGHT_BOUNDS[key]
                step = (hi - lo) * 0.10 * (1.0 - it / max(1, iters_per_restart))
                proposal = dict(current)
                proposal[key] = max(lo, min(hi, current[key] + rng.uniform(-step, step)))
                proposed_score = _score_weights(proposal, train_cases, use_cross_encoder)
                if proposed_score > current_train_score:
                    current = proposal
                    current_train_score = proposed_score
                    if proposed_score > best_train_score:
                        best_train = current
                        best_train_score = proposed_score

            # Held-out dev score
            _output_path().write_text(json.dumps(best_train), encoding="utf-8")
            load_weights.cache_clear()
            fit_dev_score = sum(_evaluate_case(c, use_cross_encoder=use_cross_encoder)["rr5"] for c in dev_cases) / max(1, len(dev_cases))
            fold_holdout_fit.append(fit_dev_score)
            aggregated_weights.append(best_train)
    finally:
        if backup is not None:
            _output_path().write_text(backup, encoding="utf-8")
        elif _output_path().exists():
            _output_path().unlink()
        load_weights.cache_clear()

    avg_default = sum(fold_holdout_default) / len(fold_holdout_default)
    avg_fit = sum(fold_holdout_fit) / len(fold_holdout_fit)

    # Average the per-fold weights
    avg_weights = {k: sum(w[k] for w in aggregated_weights) / len(aggregated_weights) for k in DEFAULT_WEIGHTS}

    # Validate the averaged weights on the FULL gold set
    _output_path().write_text(json.dumps(avg_weights), encoding="utf-8")
    load_weights.cache_clear()
    full_avg_score = sum(_evaluate_case(c, use_cross_encoder=use_cross_encoder)["rr5"] for c in cases) / len(cases)
    # And the default's full-set score
    _output_path().write_text(json.dumps(DEFAULT_WEIGHTS), encoding="utf-8")
    load_weights.cache_clear()
    full_default_score = sum(_evaluate_case(c, use_cross_encoder=use_cross_encoder)["rr5"] for c in cases) / len(cases)

    # Commit only if averaged weights beat defaults on the FULL set
    committed = full_avg_score > full_default_score
    if committed:
        _output_path().write_text(json.dumps(avg_weights, indent=2), encoding="utf-8")
    else:
        if backup is not None:
            _output_path().write_text(backup, encoding="utf-8")
        elif _output_path().exists():
            _output_path().unlink()
    load_weights.cache_clear()

    return {
        "k": k,
        "fold_holdout_default": fold_holdout_default,
        "fold_holdout_fit": fold_holdout_fit,
        "avg_holdout_default_mrr5": avg_default,
        "avg_holdout_fit_mrr5": avg_fit,
        "full_set_default_mrr5": full_default_score,
        "full_set_avg_weights_mrr5": full_avg_score,
        "committed": committed,
        "weights": avg_weights if committed else dict(DEFAULT_WEIGHTS),
    }


def fit(
    max_queries: int | None = None,
    restarts: int = 4,
    iters_per_restart: int = 30,
    use_cross_encoder: bool = True,
    seed: int = 0,
) -> dict[str, Any]:
    if not GOLD_PATH.exists():
        raise SystemExit(f"gold set missing at {GOLD_PATH}")
    cases = json.loads(GOLD_PATH.read_text(encoding="utf-8"))["queries"]
    if max_queries:
        cases = cases[:max_queries]

    random.seed(seed)
    initial_path = _output_path()
    backup = initial_path.read_text(encoding="utf-8") if initial_path.exists() else None

    baseline_weights = dict(DEFAULT_WEIGHTS)
    baseline_score = _score_weights(baseline_weights, cases, use_cross_encoder)
    best_weights = dict(baseline_weights)
    best_score = baseline_score

    try:
        for restart in range(restarts):
            current = (
                {k: random.uniform(*WEIGHT_BOUNDS[k]) for k in DEFAULT_WEIGHTS}
                if restart > 0
                else dict(DEFAULT_WEIGHTS)
            )
            current_score = _score_weights(current, cases, use_cross_encoder)
            for it in range(iters_per_restart):
                key = random.choice(list(WEIGHT_BOUNDS.keys()))
                lo, hi = WEIGHT_BOUNDS[key]
                step = (hi - lo) * 0.10 * (1.0 - it / max(1, iters_per_restart))
                proposal = dict(current)
                proposal[key] = max(lo, min(hi, current[key] + random.uniform(-step, step)))
                proposed_score = _score_weights(proposal, cases, use_cross_encoder)
                if proposed_score > current_score:
                    current = proposal
                    current_score = proposed_score
            if current_score > best_score:
                best_weights = current
                best_score = current_score
    finally:
        # ensure file ends up holding the best weights, not the last trial
        _output_path().write_text(json.dumps(best_weights, indent=2), encoding="utf-8")
        load_weights.cache_clear()

    return {
        "baseline_mrr5": baseline_score,
        "best_mrr5": best_score,
        "improvement_pct": (best_score - baseline_score) / baseline_score * 100 if baseline_score > 0 else 0.0,
        "weights": best_weights,
        "n_queries": len(cases),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-queries", type=int, default=None)
    parser.add_argument("--restarts", type=int, default=4)
    parser.add_argument("--iters", type=int, default=30)
    parser.add_argument("--no-cross-encoder", action="store_true")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--kfold", type=int, default=None, help="Run k-fold CV instead of single-fold fit. e.g. --kfold 5")
    args = parser.parse_args()
    if args.kfold:
        summary = fit_kfold(
            k=args.kfold,
            iters_per_restart=args.iters,
            use_cross_encoder=not args.no_cross_encoder,
            seed=args.seed,
        )
        print(f"k-fold ({summary['k']}) cross-validated weight fit:")
        print(f"  avg holdout MRR@5 (default): {summary['avg_holdout_default_mrr5']:.3f}")
        print(f"  avg holdout MRR@5 (fit):     {summary['avg_holdout_fit_mrr5']:.3f}")
        print(f"  full-set MRR@5 (default):    {summary['full_set_default_mrr5']:.3f}")
        print(f"  full-set MRR@5 (avg weights):{summary['full_set_avg_weights_mrr5']:.3f}")
        print(f"  committed: {summary['committed']}")
        return
    summary = fit(
        max_queries=args.max_queries,
        restarts=args.restarts,
        iters_per_restart=args.iters,
        use_cross_encoder=not args.no_cross_encoder,
        seed=args.seed,
    )
    print(f"baseline MRR@5={summary['baseline_mrr5']:.3f}")
    print(f"best     MRR@5={summary['best_mrr5']:.3f}  ({summary['improvement_pct']:+.1f}%)")
    print(f"weights written to {_output_path()}")


if __name__ == "__main__":
    main()
