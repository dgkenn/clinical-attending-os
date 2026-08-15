"""Second-pass audit: re-check pass-1 flags against the fact's own CITED page.

Pass 1 (audit_kp_catalog.py) scored grounding via open retrieval, which flags a
fact whenever top-5 search misses the right chunk — a retrieval-recall miss
looks identical to an ungrounded fact. Spot-checks showed exactly that pattern.

This pass goes straight to the citation: for every flagged KP, pull all corpus
chunks from the cited book within +/-2 pages and check the answer's numbers and
salient terms against THAT text. A fact its own cited page supports is cleared;
what remains is the real review queue:
  - CITE-MISS: cited book/page yields no chunks at all (bad citation)
  - UNSUPPORTED: page found, but the numbers aren't there

Run after pass 1 completes:
    .venv\\Scripts\\python.exe scripts\\audit_kp_catalog_pass2.py
Reads  storage/logs/kp_audit.jsonl
Writes storage/logs/kp_audit_pass2.jsonl + kp_audit_review_queue.md
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.config import settings  # noqa: E402
from src.student_model import conn, initialize_database  # noqa: E402

CHUNKS = Path("storage/chroma/chunks.jsonl")
P1 = Path(settings.log_dir) / "kp_audit.jsonl"
OUT = Path(settings.log_dir) / "kp_audit_pass2.jsonl"
QUEUE = Path(settings.log_dir) / "kp_audit_review_queue.md"

_NUM = re.compile(r"\d+(?:\.\d+)?")
_WORD = re.compile(r"[a-zA-Z]{4,}")


def _norm_book(b: str) -> str:
    return " ".join((b or "").lower().split())[:30]


def main() -> None:
    initialize_database()

    # 1. Which KPs did pass 1 flag?
    flagged_ids = []
    for line in P1.read_text(encoding="utf-8").splitlines():
        try:
            r = json.loads(line)
        except Exception:
            continue
        nt, ns = r.get("numbers_total") or 0, r.get("numbers_supported") or 0
        if (r.get("score") is not None and r["score"] < 0.45) or (nt > 0 and ns < nt):
            flagged_ids.append(r["id"])
    flagged_ids = set(flagged_ids)
    print(f"pass-1 flags: {len(flagged_ids)}")

    with conn() as db:
        kps = {
            r["id"]: dict(r)
            for r in db.execute(
                "SELECT id, topic, stem, answer, source FROM kp_catalog"
            ).fetchall()
            if r["id"] in flagged_ids
        }

    # 2. Citation targets per KP: (book_norm, page) pairs.
    wanted: dict[tuple, list] = defaultdict(list)  # (book, page) -> [kp_id]
    bad_cite = []
    for kid, kp in kps.items():
        try:
            cites = json.loads(kp["source"] or "[]")
            assert isinstance(cites, list) and cites
        except Exception:
            bad_cite.append(kid)
            continue
        for c in cites:
            book = _norm_book(str(c.get("book", "")))
            page = c.get("page")
            if not book or page is None:
                continue
            for p in range(int(page) - 2, int(page) + 3):
                wanted[(book, p)].append(kid)
    print(f"KPs with unparseable citations: {len(bad_cite)}")

    # 3. One linear scan of the chunk manifest, collecting text for wanted pages.
    page_text: dict[str, list] = defaultdict(list)  # kp_id -> [chunk texts]
    found_pages = set()
    with CHUNKS.open(encoding="utf-8") as f:
        for line in f:
            try:
                rec = json.loads(line)
            except Exception:
                continue
            m = rec.get("metadata", {})
            key = (_norm_book(m.get("book") or m.get("source_name") or ""), m.get("page"))
            if key in wanted:
                found_pages.add(key)
                text = (rec.get("text") or "").lower()
                for kid in wanted[key]:
                    if len(page_text[kid]) < 40:  # cap per KP
                        page_text[kid].append(text)

    # 4. Score each flagged KP against its cited text.
    cleared, unsupported, cite_miss = [], [], []
    with OUT.open("w", encoding="utf-8") as f:
        for kid, kp in kps.items():
            if kid in bad_cite:
                cite_miss.append(kid)
                f.write(json.dumps({"id": kid, "verdict": "cite_unparseable"}) + "\n")
                continue
            texts = page_text.get(kid)
            if not texts:
                cite_miss.append(kid)
                f.write(json.dumps({"id": kid, "verdict": "cite_page_not_found"}) + "\n")
                continue
            corpus = " ".join(texts)
            nums = set(_NUM.findall(kp["answer"]))
            words = {w.lower() for w in _WORD.findall(kp["answer"])}
            num_hits = sum(1 for n in nums if n in corpus)
            word_hits = sum(1 for w in words if w in corpus)
            num_ok = (not nums) or (num_hits / len(nums) >= 0.6)
            word_ok = (not words) or (word_hits / max(1, len(words)) >= 0.4)
            verdict = "cleared" if (num_ok and word_ok) else "unsupported_by_cited_page"
            (cleared if verdict == "cleared" else unsupported).append(kid)
            f.write(json.dumps({
                "id": kid, "verdict": verdict,
                "num_support": f"{num_hits}/{len(nums)}",
                "word_support": f"{word_hits}/{len(words)}",
            }) + "\n")

    print(f"cleared by own citation : {len(cleared)}")
    print(f"UNSUPPORTED by citation : {len(unsupported)}")
    print(f"citation missing/broken : {len(cite_miss)}")

    lines = [
        "# KP audit — final physician review queue (pass 2)",
        "",
        f"Pass 1 flagged {len(flagged_ids)} of 6,200 by open retrieval; checking each",
        f"against its OWN cited page cleared {len(cleared)}. What remains needs eyes:",
        f"**{len(unsupported)} facts whose cited page does not support their numbers/terms**",
        f"and {len(cite_miss)} with broken citations (lower priority — fact may be fine,",
        "citation is not).",
        "",
        "## Unsupported by their own citation (check → fix or delete in data/kp_catalog.json)",
        "",
    ]
    for kid in unsupported[:300]:
        kp = kps[kid]
        lines.append(f"### [ ] {kp['topic'][:60]}  (id {kid})")
        lines.append(f"- **Q:** {kp['stem'][:150]}")
        lines.append(f"- **A:** {kp['answer'][:200]}")
        lines.append(f"- **Cites:** {kp['source'][:100]}")
        lines.append("")
    lines.append(f"## Broken citations ({len(cite_miss)}) — ids")
    lines.append(", ".join(str(k) for k in cite_miss[:400]))
    QUEUE.write_text("\n".join(lines), encoding="utf-8")
    print(f"review queue -> {QUEUE}")


if __name__ == "__main__":
    main()
