from __future__ import annotations

import hashlib
import re
from typing import Any


FACT_MIN_WORDS = 5
FACT_MAX_CHARS = 220
SKIP_SECTION_TERMS = (
    "table of contents",
    "acknowledg",
    "contributors",
    "suggested checklist",
    "goals of the ca-1",
    "key points and expectations",
    "references",
    "suggested readings",
    "further reading",
    "bibliography",
    "index",
    "glossary",
    "copyright",
    "preface",
    "foreword",
    "appendix",
)

NUMERIC_UNIT_RE = re.compile(
    r"\d+(?:\.\d+)?\s*(?:mg|mcg|µg|ug|ml|l/min|mmHg|mEq|mmol|kg|cmH2O|%|hr|min|sec|bpm|fr|gauge|units?)\b",
    re.I,
)
TRIGGER_PHRASES = (
    "pearl:",
    "note:",
    "key point",
    "key points",
    "remember:",
    "clinical scenario",
    "must know",
    "high yield",
    "danger",
    "warning",
    "first-line",
    "first line",
    "treatment of choice",
    "contraindication",
    "indication:",
    "dose:",
)
NUMBERED_LIST_RE = re.compile(r"^\s*\d+[\).]\s+", re.M)
BULLET_RE = re.compile(r"^\s*[•\*\-]\s+", re.M)
NARRATIVE_PROSE_BOOKS = {"Morgan & Mikhail", "Miller/Baby Miller"}


def clean_fact_text(text: str) -> str:
    text = re.sub(r"(\w)-\s+(\w)", r"\1\2", text)
    text = re.sub(r"\s+", " ", text).strip(" -:;,.")
    return text


def split_fact_units(text: str, max_chars: int = FACT_MAX_CHARS, max_facts: int | None = None) -> list[str]:
    text = clean_fact_text(text)
    raw_parts = re.split(
        r"\s+(?:\u2022|\*|-{1,2}|\d+[\).])\s+|(?<=[.!?])\s+|;\s+(?=[A-Z0-9])",
        text,
    )
    facts: list[str] = []
    seen: set[str] = set()
    for part in raw_parts:
        fact = clean_fact_text(part)
        words = fact.split()
        if len(words) < FACT_MIN_WORDS:
            continue
        if len(fact) > max_chars:
            fact = clean_fact_text(" ".join(words[:36]))
        low = fact.lower()
        if not fact or low in seen or low in {"references", "suggested readings"}:
            continue
        seen.add(low)
        facts.append(fact)
        if max_facts and len(facts) >= max_facts:
            break
    return facts


def _has_high_yield_signal(text: str, meta: dict[str, Any]) -> bool:
    if meta.get("has_bold"):
        return True
    low = text.lower()
    if NUMERIC_UNIT_RE.search(text):
        return True
    if any(phrase in low for phrase in TRIGGER_PHRASES):
        return True
    if NUMBERED_LIST_RE.search(text) or BULLET_RE.search(text):
        return True
    return False


def _looks_like_references(text: str) -> bool:
    if text.count("http") >= 2:
        return True
    citation_markers = sum(text.count(token) for token in (" et al", "doi:", "PMID", "p. ", "pp."))
    return citation_markers >= 4


def is_testable_chunk(meta: dict[str, Any], text: str) -> bool:
    """Inclusive filter: drop only structural noise (refs, TOC, index, etc.).

    Goal is maximum recall — the user wants every testable fact across all
    books. The high-yield signal helpers exist for downstream prioritization,
    not gatekeeping ingestion.
    """
    source = meta.get("source_name") or meta.get("book", "")
    page = int(meta.get("page") or meta.get("page_number") or 0)
    section = str(meta.get("section") or meta.get("section_heading") or "").lower()
    chapter_title = str(meta.get("chapter_title") or "").lower()
    beginning = clean_fact_text(text[:240]).lower()
    # Use startswith for section/chapter so a content chapter whose title
    # incidentally contains "index" (e.g. "NF Index final.pdf") is not dropped.
    if any(
        section.startswith(term) or chapter_title.startswith(term) or beginning.startswith(term)
        for term in SKIP_SECTION_TERMS
    ):
        return False
    if source == "Stanford CA-1" and page < 13:
        return False
    if _looks_like_references(text):
        return False
    return True


def high_yield_score(meta: dict[str, Any], text: str) -> float:
    """0-1 priority score; used by curriculum/session planner, NOT to gate ingestion."""
    score = 0.0
    if meta.get("has_bold"):
        score += 0.35
    if NUMERIC_UNIT_RE.search(text):
        score += 0.30
    low = text.lower()
    if any(phrase in low for phrase in TRIGGER_PHRASES):
        score += 0.25
    if NUMBERED_LIST_RE.search(text) or BULLET_RE.search(text):
        score += 0.10
    return min(1.0, score)


def fact_target_id(source: str, page: int | None, fact: str, idx: int = 1) -> str:
    digest = hashlib.sha1(f"{source}|{page}|{idx}|{fact}".encode("utf-8")).hexdigest()[:12]
    source_slug = source.lower().replace(" ", "-").replace("&", "and").replace("/", "-")
    source_slug = re.sub(r"[^a-z0-9-]+", "-", source_slug).strip("-")
    return f"{source_slug}-p{page}-f{idx}-{digest}"


def fact_subtopic(source: str, page: int | None, fact: str) -> str:
    label = "CA-1" if source == "Stanford CA-1" else source
    return f"{label} p. {page}: {fact}"
