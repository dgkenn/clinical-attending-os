from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from collections import Counter
import math

from .chapter_extract import build_chapter_map, page_has_bold
from .chunking import clean_page_text, normalize_line


@dataclass(frozen=True)
class PageText:
    path: Path
    page_number: int
    total_pages: int
    text: str
    chapter_number: int | None = None
    chapter_title: str = ""
    has_bold: bool = False


def discover_pdfs(data_dir: Path, source_files: tuple[Path, ...] = (), source_filter: str | None = None) -> list[Path]:
    files = list(source_files) if source_files else list(data_dir.rglob("*.pdf"))
    existing = [p for p in files if p.exists() and p.suffix.lower() == ".pdf"]
    if source_filter:
        sf = source_filter.lower()
        existing = [p for p in existing if sf in p.name.lower()]
    return sorted(set(existing), key=lambda p: str(p).lower())


def load_pdf_pages(path: Path) -> list[PageText]:
    try:
        import fitz
    except Exception as exc:  # pragma: no cover
        raise RuntimeError("PyMuPDF is required for PDF ingestion. Install pymupdf.") from exc
    chapter_map = build_chapter_map(path)
    doc = fitz.open(path)
    raw_pages = [page.get_text("text") for page in doc]
    bold_flags = [page_has_bold(page) for page in doc]
    candidates: Counter[str] = Counter()
    for raw in raw_pages:
        lines = [normalize_line(line) for line in raw.splitlines() if normalize_line(line)]
        edge_lines = lines[:6] + lines[-6:]
        for line in edge_lines:
            low = line.lower()
            if 3 <= len(line) <= 120 and not low.endswith("."):
                candidates[low] += 1
    threshold = max(3, math.ceil(doc.page_count * 0.20))
    repeated = {line for line, count in candidates.items() if count >= threshold}
    pages: list[PageText] = []
    for idx, raw in enumerate(raw_pages, start=1):
        text = clean_page_text(raw, repeated)
        if not text:
            continue
        chap_num, chap_title = chapter_map.get(idx, (None, ""))
        pages.append(
            PageText(
                path=path,
                page_number=idx,
                total_pages=doc.page_count,
                text=text,
                chapter_number=chap_num,
                chapter_title=chap_title,
                has_bold=bool(bold_flags[idx - 1]) if idx - 1 < len(bold_flags) else False,
            )
        )
    doc.close()
    return pages
