"""Repair fabricated citations by finding the page that ACTUALLY supports each fact.

Pass 2 of the audit found 404 facts whose cited page doesn't contain them plus
33 citing pages absent from the corpus — mostly right-sounding medicine with a
wrong provenance. Before asking a physician to review 437 items, do the part a
machine can: search the corpus for each fact's own content, and when a chunk
strongly supports it, RE-CITE the fact to that chunk's real book+page.

What's left after this run is the true human queue: facts no page in the
corpus supports. Those are either from outside the 8-book corpus (fine, but
must be marked as such) or fabricated content (must be fixed/deleted).

Updates BOTH the kp_catalog table and data/kp_catalog.json (if present) so a
re-seed doesn't resurrect bad citations.

Run:  .venv\\Scripts\\python.exe scripts\\recite_flagged_kps.py [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.config import settings  # noqa: E402
from src.student_model import conn, initialize_database  # noqa: E402
from src.retrieval import hybrid_search  # noqa: E402

P2 = Path(settings.log_dir) / "kp_audit_pass2.jsonl"
OUT = Path(settings.log_dir) / "kp_recite_results.md"
DATA_JSON = ROOT / "data" / "kp_catalog.json"

_NUM = re.compile(r"\d+(?:\.\d+)?")
_WORD = re.compile(r"[a-zA-Z]{4,}")
_STOP = {"with", "that", "this", "from", "into", "than", "then", "when", "which",
         "should", "must", "does", "have", "been", "were", "will", "only"}


def _support(answer: str, text: str) -> float:
    """0-1: how much of the answer's load-bearing content this text contains."""
    t = text.lower()
    nums = set(_NUM.findall(answer))
    words = {w.lower() for w in _WORD.findall(answer)} - _STOP
    nh = sum(1 for n in nums if n in t)
    wh = sum(1 for w in words if w in t)
    denom = 3 * len(nums) + len(words)
    return (3 * nh + wh) / denom if denom else 0.0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--threshold", type=float, default=0.55,
                    help="min support from a single chunk to accept a re-cite")
    args = ap.parse_args()
    initialize_database()

    targets = []
    for line in P2.read_text(encoding="utf-8").splitlines():
        r = json.loads(line)
        if r.get("verdict") in ("unsupported_by_cited_page", "cite_page_not_found",
                                "cite_unparseable"):
            targets.append(r["id"])
    print(f"targets: {len(targets)}")

    with conn() as db:
        kps = {r["id"]: dict(r) for r in db.execute(
            "SELECT id, topic, stem, answer, source FROM kp_catalog"
        ).fetchall() if r["id"] in set(targets)}

    recited, unsupported = [], []
    for i, (kid, kp) in enumerate(kps.items(), 1):
        # Search on the ANSWER (the content that must be supported), scoped by topic.
        query = f"{kp['topic']} {kp['answer']}"[:300]
        try:
            sources, _ = hybrid_search(query, mode="intern_teach", max_results=6,
                                       use_cross_encoder=False)
        except Exception as exc:
            unsupported.append((kid, f"search error: {exc}"))
            continue
        best, best_score = None, 0.0
        for s in sources:
            sc = _support(kp["answer"], s.text)
            if sc > best_score:
                best, best_score = s, sc
        if best is not None and best_score >= args.threshold:
            new_cite = json.dumps([{"book": best.book or best.source_name or "?",
                                    "page": best.page or 0}])
            recited.append((kid, new_cite, round(best_score, 2), kp["source"]))
        else:
            unsupported.append((kid, f"best support {best_score:.2f}"))
        if i % 50 == 0:
            print(f"  {i}/{len(kps)}  recited={len(recited)}")

    print(f"\nre-citable: {len(recited)} | truly unsupported: {len(unsupported)}")
    if not args.dry_run and recited:
        with conn() as db:
            for kid, cite, _, _ in recited:
                db.execute("UPDATE kp_catalog SET source=? WHERE id=?", (cite, kid))
        print("kp_catalog table updated")
        if DATA_JSON.exists():
            data = json.loads(DATA_JSON.read_text(encoding="utf-8"))
            by_id = {kid: cite for kid, cite, _, _ in recited}
            n = 0
            for item in data:
                if item.get("id") in by_id:
                    item["source"] = by_id[item["id"]]
                    n += 1
            DATA_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False),
                                 encoding="utf-8")
            print(f"data/kp_catalog.json updated ({n} items)")

    lines = [
        "# Citation repair results", "",
        f"- Re-cited to a genuinely supporting page: **{len(recited)}**",
        f"- No supporting page anywhere in the corpus: **{len(unsupported)}** "
        "(the TRUE physician review queue — fix, delete, or mark as "
        "outside-corpus knowledge)", "",
        "## Truly unsupported", "",
    ]
    for kid, why in unsupported:
        kp = kps.get(kid, {})
        lines.append(f"### [ ] {kp.get('topic','?')[:60]} (id {kid}; {why})")
        lines.append(f"- **Q:** {kp.get('stem','')[:140]}")
        lines.append(f"- **A:** {kp.get('answer','')[:200]}")
        lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"report -> {OUT}")


if __name__ == "__main__":
    main()
