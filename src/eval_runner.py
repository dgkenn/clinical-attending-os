"""Retrieval evaluation harness.

Loads tests/data/gold_set.json, runs hybrid_search per query, and reports
MRR@5, nDCG@5, recall@10, and per-query latency.

CLI:
    python -m src.eval_runner                # full eval, default settings
    python -m src.eval_runner --no-cross-encoder
    python -m src.eval_runner --json out.json
    python -m src.eval_runner --max 20       # smoke run
"""

from __future__ import annotations

import argparse
import json
import math
import statistics
import time
from pathlib import Path
from typing import Any

from .config import settings
from .retrieval import hybrid_search


GOLD_PATH = Path(__file__).resolve().parents[1] / "tests" / "data" / "gold_set.json"


def _result_matches(result_meta: dict[str, Any], result_text: str, case: dict) -> bool:
    libs = case.get("expected_libraries") or []
    sources = case.get("expected_sources") or []
    must_terms = case.get("must_appear_top_5") or []
    if libs and result_meta.get("library", "") not in libs:
        if not sources:
            return False
    if sources and not any(s.lower() in (result_meta.get("source_name") or result_meta.get("book") or "").lower() for s in sources):
        if not libs or result_meta.get("library", "") not in libs:
            return False
    if must_terms:
        low = (result_text or "").lower()
        if not any(t.lower() in low for t in must_terms):
            return False
    return True


def _evaluate_case(case: dict, *, use_cross_encoder: bool) -> dict[str, Any]:
    start = time.perf_counter()
    results, insufficient = hybrid_search(
        case["query"],
        mode=case.get("mode", "broad_explain"),
        max_results=10,
        use_cross_encoder=use_cross_encoder,
    )
    latency = time.perf_counter() - start
    relevant_positions: list[int] = []
    for idx, r in enumerate(results, start=1):
        meta = {"library": r.library, "source_name": r.source_name, "book": r.book}
        if _result_matches(meta, r.text, case):
            relevant_positions.append(idx)
    rr5 = 1.0 / relevant_positions[0] if relevant_positions and relevant_positions[0] <= 5 else 0.0
    dcg5 = sum(1.0 / math.log2(p + 1) for p in relevant_positions if p <= 5)
    idcg5 = sum(1.0 / math.log2(p + 1) for p in range(1, min(5, len(relevant_positions)) + 1))
    ndcg5 = dcg5 / idcg5 if idcg5 > 0 else 0.0
    recall10 = 1.0 if any(p <= 10 for p in relevant_positions) else 0.0
    return {
        "query": case["query"],
        "mode": case.get("mode"),
        "rr5": rr5,
        "ndcg5": ndcg5,
        "recall10": recall10,
        "first_hit_position": relevant_positions[0] if relevant_positions else None,
        "n_hits_top10": sum(1 for p in relevant_positions if p <= 10),
        "latency_s": latency,
        "insufficient_context": insufficient,
        "top5_sources": [f"{r.book} p.{r.page}" for r in results[:5]],
    }


def run(use_cross_encoder: bool = True, max_queries: int | None = None) -> dict[str, Any]:
    settings.ensure_dirs()
    if not GOLD_PATH.exists():
        raise SystemExit(f"gold set not found at {GOLD_PATH}")
    cases = json.loads(GOLD_PATH.read_text(encoding="utf-8"))["queries"]
    if max_queries:
        cases = cases[:max_queries]
    rows = [_evaluate_case(c, use_cross_encoder=use_cross_encoder) for c in cases]
    latencies = [r["latency_s"] for r in rows]
    return {
        "n_queries": len(rows),
        "use_cross_encoder": use_cross_encoder,
        "mrr5": statistics.mean(r["rr5"] for r in rows) if rows else 0.0,
        "ndcg5": statistics.mean(r["ndcg5"] for r in rows) if rows else 0.0,
        "recall10": statistics.mean(r["recall10"] for r in rows) if rows else 0.0,
        "latency_p50": statistics.median(latencies) if latencies else 0.0,
        "latency_p99": (sorted(latencies)[-max(1, len(latencies) // 100)] if latencies else 0.0),
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-cross-encoder", action="store_true")
    parser.add_argument("--json", help="write detailed report to a JSON file")
    parser.add_argument("--max", type=int, default=None)
    args = parser.parse_args()
    summary = run(use_cross_encoder=not args.no_cross_encoder, max_queries=args.max)
    print(
        f"n={summary['n_queries']}  "
        f"MRR@5={summary['mrr5']:.3f}  "
        f"nDCG@5={summary['ndcg5']:.3f}  "
        f"recall@10={summary['recall10']:.3f}  "
        f"p50={summary['latency_p50']*1000:.0f}ms  "
        f"p99={summary['latency_p99']*1000:.0f}ms  "
        f"cross_encoder={'on' if summary['use_cross_encoder'] else 'off'}"
    )
    failures = [r for r in summary["rows"] if r["recall10"] < 1.0]
    if failures:
        print(f"\nMissed (recall@10 = 0): {len(failures)}/{summary['n_queries']}")
        for r in failures[:10]:
            print(f"  - {r['query']}  (mode={r['mode']})  top5: {r['top5_sources'][:3]}")
    if args.json:
        Path(args.json).write_text(json.dumps(summary, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
