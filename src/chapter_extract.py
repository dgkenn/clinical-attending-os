"""Chapter resolution from PDFs.

Primary source: PyMuPDF `doc.get_toc()` — works for textbooks with embedded
bookmarks (Miller, Morgan & Mikhail, Marino).

Fallback for TOC-less PDFs (some intern guides, MGH): scan each page for the
first heading-like line (`^Chapter \\d+`, all-caps long line, or numbered
section header) and forward-fill the most recent chapter title across pages.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any


CHAPTER_PATTERNS = (
    re.compile(r"^\s*chapter\s+(\d+)[\s:.\-]*(.{3,80})?$", re.I),
    re.compile(r"^\s*(\d+)\.\s+([A-Z][A-Z\s/&,'\-]{6,80})$"),
    re.compile(r"^\s*([A-Z][A-Z\s/&,'\-]{12,80})$"),
)


def _toc_chapter_map(doc) -> dict[int, tuple[int | None, str]]:
    """Map page_number (1-indexed) -> (chapter_number, chapter_title) using TOC."""
    try:
        toc = doc.get_toc(simple=True) or []
    except Exception:
        return {}
    if not toc:
        return {}
    top_level = [(lvl, title.strip(), page) for lvl, title, page in toc if lvl == 1]
    if not top_level:
        return {}
    page_map: dict[int, tuple[int | None, str]] = {}
    chapter_index = 0
    for i, (_lvl, title, start_page) in enumerate(top_level):
        chapter_index += 1
        end_page = top_level[i + 1][2] - 1 if i + 1 < len(top_level) else doc.page_count
        for p in range(max(1, start_page), max(1, end_page) + 1):
            page_map[p] = (chapter_index, title)
    return page_map


def _heading_from_text(text: str) -> str | None:
    for line in text.splitlines()[:10]:
        line = line.strip()
        if not line:
            continue
        for pattern in CHAPTER_PATTERNS:
            m = pattern.match(line)
            if m:
                groups = [g for g in m.groups() if g]
                return " ".join(groups).strip()[:90]
    return None


def build_chapter_map(path: Path) -> dict[int, tuple[int | None, str]]:
    """Return {page_number: (chapter_number_or_None, chapter_title)} for every page."""
    try:
        import fitz
    except Exception as exc:  # pragma: no cover
        raise RuntimeError("PyMuPDF required for chapter extraction.") from exc
    doc = fitz.open(path)
    try:
        page_map = _toc_chapter_map(doc)
        if page_map:
            for p in range(1, doc.page_count + 1):
                page_map.setdefault(p, (None, ""))
            return page_map
        # Fallback: forward-fill heuristic headings
        current: tuple[int | None, str] = (None, "")
        chapter_idx = 0
        result: dict[int, tuple[int | None, str]] = {}
        for p in range(1, doc.page_count + 1):
            heading = _heading_from_text(doc[p - 1].get_text("text"))
            if heading and heading != current[1]:
                chapter_idx += 1
                current = (chapter_idx, heading)
            result[p] = current
        return result
    finally:
        doc.close()


def page_has_bold(page: Any) -> bool:
    """True if the page contains bold runs — used as a high-yield signal."""
    try:
        d = page.get_text("dict")
    except Exception:
        return False
    for block in d.get("blocks", []):
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                flags = span.get("flags", 0)
                font = (span.get("font") or "").lower()
                if flags & 16 or "bold" in font:
                    return True
    return False
