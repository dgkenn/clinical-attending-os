"""Sample-audit canonical facts for medical-content quality.

Prints a stratified sample (per-book, per-band) plus boilerplate-suspect
facts that survived the medical gate, so the user can eyeball quality.

CLI:
    python -m src.fact_audit                          # 5 facts/book
    python -m src.fact_audit --per-book 10 --suspects 50
    python -m src.fact_audit --json audit.json
"""

from __future__ import annotations

import argparse
import json
import random
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

from .config import settings
from .dedupe_facts import is_medical_fact


SUSPECT_PATTERNS = [
    re.compile(r"^\s*(?:see|refer to|cf\.?|cited)\b", re.I),
    re.compile(r"^\s*(?:figure|table|fig\.?)\s*\d+", re.I),
    re.compile(r"^\s*(?:reproduced|adapted|courtesy of|with permission)", re.I),
    re.compile(r"^\s*(?:abstract|introduction|background|conclusion|discussion)\s*$", re.I),
    re.compile(r"^\s*\d+\s*$"),
    re.compile(r"^[\W\s]+$"),
]


def _iter_facts() -> list[dict[str, Any]]:
    path = settings.chroma_dir / "chunks.jsonl"
    if not path.exists():
        return []
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            try:
                row = json.loads(line)
            except Exception:
                continue
            if (row.get("metadata") or {}).get("chunk_type") == "fact":
                rows.append(row)
    return rows


def _is_suspect(text: str) -> bool:
    if any(p.search(text) for p in SUSPECT_PATTERNS):
        return True
    if not is_medical_fact(text):
        return True
    if len(text.strip()) < 20:
        return True
    return False


def stratified_sample(facts: list[dict[str, Any]], per_book: int = 5) -> dict[str, list[dict]]:
    by_book: dict[str, list[dict]] = defaultdict(list)
    for f in facts:
        book = f["metadata"].get("source_name") or f["metadata"].get("book", "")
        by_book[book].append(f)
    out: dict[str, list[dict]] = {}
    rng = random.Random(42)
    for book, items in by_book.items():
        sample = rng.sample(items, k=min(per_book, len(items)))
        out[book] = [
            {
                "page": f["metadata"].get("page"),
                "chapter": f["metadata"].get("chapter_title"),
                "section": f["metadata"].get("section"),
                "text": (f.get("text") or "").strip()[:280],
            }
            for f in sample
        ]
    return out


def find_suspects(facts: list[dict[str, Any]], limit: int = 50) -> list[dict[str, Any]]:
    suspects = []
    for f in facts:
        text = (f.get("text") or "").strip()
        if _is_suspect(text):
            suspects.append(
                {
                    "book": f["metadata"].get("source_name") or f["metadata"].get("book", ""),
                    "page": f["metadata"].get("page"),
                    "text": text[:280],
                }
            )
            if len(suspects) >= limit:
                break
    return suspects


def stats(facts: list[dict[str, Any]]) -> dict[str, Any]:
    by_book: dict[str, int] = defaultdict(int)
    by_library: dict[str, int] = defaultdict(int)
    canonical = 0
    chapters_per_book: dict[str, set] = defaultdict(set)
    for f in facts:
        meta = f["metadata"]
        book = meta.get("source_name") or meta.get("book", "")
        by_book[book] += 1
        by_library[meta.get("library", "")] += 1
        if meta.get("is_canonical_fact"):
            canonical += 1
        if meta.get("chapter_title"):
            chapters_per_book[book].add(meta["chapter_title"])
    return {
        "total_facts": len(facts),
        "canonical_facts": canonical,
        "by_book": dict(by_book),
        "by_library": dict(by_library),
        "chapters_per_book": {k: len(v) for k, v in chapters_per_book.items()},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--per-book", type=int, default=5)
    parser.add_argument("--suspects", type=int, default=20)
    parser.add_argument("--json", type=str, default=None)
    args = parser.parse_args()

    facts = _iter_facts()
    sample = stratified_sample(facts, per_book=args.per_book)
    suspects = find_suspects(facts, limit=args.suspects)
    summary = stats(facts)

    print("=== Stats ===")
    for k, v in summary.items():
        print(f"  {k}: {v}")
    print("\n=== Stratified sample ===")
    for book, items in sample.items():
        print(f"\n[{book}]")
        for item in items:
            print(f"  p{item['page']} | {item['section'] or item['chapter'] or ''}\n    {item['text']}")
    print(f"\n=== Suspect facts (first {len(suspects)}) ===")
    for s in suspects:
        print(f"  [{s['book']} p{s['page']}] {s['text']}")
    if args.json:
        Path(args.json).write_text(
            json.dumps({"summary": summary, "sample": sample, "suspects": suspects}, indent=2),
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
