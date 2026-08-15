"""Audit the generated KP catalog's grounding against the retrieval corpus.

The 946 curated units are human-fact-checked; the other ~5,250 catalog KPs are
generated. For a system used to treat patients, "probably right" isn't a
standard. This audit retrieves each KP's own topic+answer against the corpus
and scores how well the sources support the answer's load-bearing terms
(numbers, doses, named drugs/thresholds get extra weight).

It CANNOT prove a fact wrong — only flag weak grounding for physician review.
Output: storage/logs/kp_audit.jsonl (every KP, resumable) and
storage/logs/kp_audit_flagged.md (the review queue, worst first).

Run in batches (it's retrieval-bound, ~0.3s/KP):
    .venv\\Scripts\\python.exe scripts\\audit_kp_catalog.py --limit 500
Re-running resumes: already-audited KP ids are skipped.
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

OUT_JSONL = Path(settings.log_dir) / "kp_audit.jsonl"
OUT_FLAGGED = Path(settings.log_dir) / "kp_audit_flagged.md"

_NUM = re.compile(r"\d+(?:\.\d+)?")
_WORD = re.compile(r"[a-zA-Z]{4,}")
_STOP = {
    "with", "that", "this", "from", "into", "than", "then", "when", "which",
    "should", "must", "does", "have", "been", "were", "will", "only", "most",
    "more", "less", "very", "also", "each", "them", "they", "their", "because",
}


def _key_terms(text: str) -> tuple[set[str], set[str]]:
    """(numbers, salient words) — numbers are the load-bearing clinical content."""
    nums = set(_NUM.findall(text))
    words = {w.lower() for w in _WORD.findall(text)} - _STOP
    return nums, words


def audit_one(kp: dict) -> dict:
    query = f"{kp['topic']} {kp['stem']}"[:300]
    try:
        sources, insufficient = hybrid_search(
            query, mode="intern_teach", max_results=5, use_cross_encoder=False
        )
    except Exception as exc:
        return {"id": kp["id"], "score": None, "error": str(exc)[:120]}
    corpus_text = " ".join(s.text.lower() for s in sources)
    nums, words = _key_terms(kp["answer"])
    num_hits = sum(1 for n in nums if n in corpus_text)
    word_hits = sum(1 for w in words if w in corpus_text)
    # Numbers weigh 3x: a dose or threshold unsupported by the sources is the
    # dangerous case; prose overlap alone is cheap.
    denom = 3 * len(nums) + len(words)
    score = round((3 * num_hits + word_hits) / denom, 3) if denom else None
    return {
        "id": kp["id"], "topic": kp["topic"], "score": score,
        "numbers_total": len(nums), "numbers_supported": num_hits,
        "insufficient_context": insufficient,
        "source": kp.get("source", ""),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=200, help="KPs to audit this run")
    ap.add_argument("--flag-below", type=float, default=0.45)
    args = ap.parse_args()

    initialize_database()
    OUT_JSONL.parent.mkdir(parents=True, exist_ok=True)
    done: set = set()
    if OUT_JSONL.exists():
        for line in OUT_JSONL.read_text(encoding="utf-8").splitlines():
            try:
                done.add(json.loads(line)["id"])
            except Exception:
                pass

    with conn() as db:
        rows = [dict(r) for r in db.execute(
            "SELECT id, topic, stem, answer, source FROM kp_catalog ORDER BY tier ASC, id ASC"
        ).fetchall()]
    todo = [r for r in rows if r["id"] not in done][: args.limit]
    print(f"catalog: {len(rows)} | audited: {len(done)} | this run: {len(todo)}")

    with OUT_JSONL.open("a", encoding="utf-8") as f:
        for i, kp in enumerate(todo, 1):
            res = audit_one(kp)
            f.write(json.dumps(res) + "\n")
            if i % 50 == 0:
                print(f"  {i}/{len(todo)}")

    # Rebuild the flagged review queue from the full JSONL.
    flagged = []
    for line in OUT_JSONL.read_text(encoding="utf-8").splitlines():
        try:
            r = json.loads(line)
        except Exception:
            continue
        s = r.get("score")
        unsupported_numbers = (r.get("numbers_total") or 0) > 0 and (
            r.get("numbers_supported", 0) < r.get("numbers_total", 0)
        )
        if (s is not None and s < args.flag_below) or unsupported_numbers:
            flagged.append(r)
    flagged.sort(key=lambda r: (r.get("score") if r.get("score") is not None else 0))

    by_id = {r["id"]: r for r in rows}
    lines = [
        "# KP catalog — flagged for physician review",
        "",
        f"{len(flagged)} of {len(done) + len(todo)} audited KPs have weak retrieval "
        f"grounding (score < {args.flag_below}) or numeric claims the top-5 sources "
        "don't contain. **Weak grounding is a review flag, not a verdict of wrong** — "
        "check each against the cited source; fix or delete bad ones in "
        "data/kp_catalog.json and re-seed.",
        "",
    ]
    for r in flagged[:200]:
        kp = by_id.get(r["id"], {})
        lines.append(
            f"## [ ] {r.get('topic','?')} (id {r['id']}, score {r.get('score')}, "
            f"numbers {r.get('numbers_supported',0)}/{r.get('numbers_total',0)})"
        )
        lines.append(f"- **Stem:** {kp.get('stem','?')}")
        lines.append(f"- **Answer:** {kp.get('answer','?')}")
        lines.append(f"- **Cites:** {r.get('source','')}")
        lines.append("")
    OUT_FLAGGED.write_text("\n".join(lines), encoding="utf-8")
    print(f"flagged: {len(flagged)} -> {OUT_FLAGGED}")


if __name__ == "__main__":
    main()
