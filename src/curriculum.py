"""Curriculum builder.

Groups ingested chunks into ordered lesson units (book -> chapter -> section)
and interleaves them per the user's training mix:

- Spine: intern survival guides + OnlineMedEd (medicine).
- Deep medicine: MGH Housestaff Manual.
- ICU spine: Marino ICU Book (90% medicine + ICU bias prefers Marino content
  for ICU-overlap topics like sepsis, ARDS, vent, vasopressors, transfusion).
- Anesthesia interleave: Stanford CA-1 (then Morgan & Mikhail, Miller) at
  `settings.anesthesia_crossover_percent` of total units (default 10%).

Units are persisted to `storage/curriculum/units.json`. The session_runner
picks the next due unit from this list using FSRS state from the topic store.
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from .config import settings
from .fact_extraction import high_yield_score
from .source_classifier import (
    ANESTHESIA_LIBRARY,
    ICU_LIBRARY,
    INTERN_LIBRARY,
)


SPINE_SOURCES = (
    "Intern Notes / Survival Guide",
    "OnlineMedEd Intern Guide",
)
DEEP_MEDICINE = ("MGH Housestaff Manual", "Hospitalist / Intern Guide")
ICU_SPINE = ("Marino ICU Book",)
ANESTHESIA_SOURCES = (
    "Stanford CA-1",
    "Morgan & Mikhail",
    "Miller/Baby Miller",
)
ICU_OVERLAP_TOPICS = (
    "Sepsis",
    "ARDS",
    "Mechanical ventilation",
    "Vasopressors",
    "Shock",
    "Massive transfusion",
    "Ventilator alarms",
    "Weaning/extubation",
    "Sedation",
    "Acid base",
    "AKI",
    "Hyperkalemia",
)


@dataclass
class CurriculumUnit:
    unit_id: str
    book: str
    library: str
    chapter_number: int | None
    chapter_title: str
    section: str
    page_start: int
    page_end: int
    topic_tags: list[str] = field(default_factory=list)
    fact_chunk_ids: list[str] = field(default_factory=list)
    fact_count: int = 0
    high_yield_score: float = 0.0
    crossover_priority: str = "normal"  # 'high' for ICU overlap


def _load_chunks() -> list[dict[str, Any]]:
    path = settings.chroma_dir / "chunks.jsonl"
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            try:
                rows.append(json.loads(line))
            except Exception:
                pass
    return rows


def _slug(value: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return s[:80] or "unit"


def _unit_key(meta: dict[str, Any]) -> tuple[str, int | None, str, str]:
    book = meta.get("source_name") or meta.get("book") or ""
    chapter_number = meta.get("chapter_number")
    chapter_title = meta.get("chapter_title") or ""
    section = meta.get("section") or meta.get("section_heading") or ""
    return (book, chapter_number, chapter_title, section)


def build_units(rows: list[dict[str, Any]] | None = None) -> list[CurriculumUnit]:
    rows = rows if rows is not None else _load_chunks()
    grouped: dict[tuple, dict[str, Any]] = {}
    for row in rows:
        meta = row.get("metadata", {})
        if meta.get("chunk_type") != "fact":
            continue
        key = _unit_key(meta)
        bucket = grouped.setdefault(
            key,
            {
                "book": key[0],
                "library": meta.get("library", ""),
                "chapter_number": key[1],
                "chapter_title": key[2],
                "section": key[3],
                "pages": set(),
                "topic_tags": set(),
                "fact_ids": [],
                "high_yield_sum": 0.0,
                "high_yield_n": 0,
            },
        )
        if meta.get("page"):
            bucket["pages"].add(int(meta["page"]))
        for tag in (meta.get("topic_tags") or "").split(","):
            tag = tag.strip()
            if tag:
                bucket["topic_tags"].add(tag)
        bucket["fact_ids"].append(meta.get("chunk_id") or row.get("id", ""))
        bucket["high_yield_sum"] += high_yield_score(meta, row.get("text", ""))
        bucket["high_yield_n"] += 1

    units: list[CurriculumUnit] = []
    for key, bucket in grouped.items():
        if not bucket["fact_ids"]:
            continue
        pages = sorted(bucket["pages"]) or [0]
        topic_tags = sorted(bucket["topic_tags"])
        crossover = "high" if any(t in ICU_OVERLAP_TOPICS for t in topic_tags) else "normal"
        unit_id = _slug(f"{bucket['book']}-{bucket['chapter_number'] or 0}-{bucket['section']}-{pages[0]}")
        avg_hy = bucket["high_yield_sum"] / max(1, bucket["high_yield_n"])
        units.append(
            CurriculumUnit(
                unit_id=unit_id,
                book=bucket["book"],
                library=bucket["library"],
                chapter_number=bucket["chapter_number"],
                chapter_title=bucket["chapter_title"],
                section=bucket["section"],
                page_start=pages[0],
                page_end=pages[-1],
                topic_tags=topic_tags,
                fact_chunk_ids=bucket["fact_ids"],
                fact_count=len(bucket["fact_ids"]),
                high_yield_score=round(avg_hy, 4),
                crossover_priority=crossover,
            )
        )
    return units


def _band_for_unit(unit: CurriculumUnit) -> str:
    if unit.book in SPINE_SOURCES:
        return "spine"
    if unit.book in DEEP_MEDICINE:
        return "deep_medicine"
    if unit.book in ICU_SPINE:
        return "icu"
    if unit.book in ANESTHESIA_SOURCES:
        return "anesthesia"
    if unit.library == INTERN_LIBRARY:
        return "spine"
    if unit.library == ICU_LIBRARY:
        return "icu"
    if unit.library == ANESTHESIA_LIBRARY:
        return "anesthesia"
    return "deep_medicine"


def _ordered_within_band(units: list[CurriculumUnit]) -> list[CurriculumUnit]:
    return sorted(
        units,
        key=lambda u: (
            u.book,
            u.chapter_number if u.chapter_number is not None else 999,
            u.page_start,
            u.section,
        ),
    )


def _interleave(
    spine: list[CurriculumUnit],
    deep_medicine: list[CurriculumUnit],
    icu: list[CurriculumUnit],
    anesthesia: list[CurriculumUnit],
    anesthesia_pct: float,
) -> list[CurriculumUnit]:
    """Interleave bands. Default mix per `anesthesia_pct`:
    every block of 1/anesthesia_pct medicine units gets 1 anesthesia unit.
    Within medicine: alternate spine -> deep_medicine -> spine; ICU sliced when
    a high-crossover spine unit is reached.
    """
    out: list[CurriculumUnit] = []
    spine_q = list(spine)
    deep_q = list(deep_medicine)
    icu_q = list(icu)
    anes_q = list(anesthesia)
    anesthesia_every = max(1, round(1.0 / max(0.01, anesthesia_pct)))
    medicine_count = 0

    while spine_q or deep_q or icu_q or anes_q:
        added_this_round = False

        if spine_q:
            unit = spine_q.pop(0)
            out.append(unit)
            medicine_count += 1
            added_this_round = True
            if unit.crossover_priority == "high" and icu_q:
                out.append(icu_q.pop(0))
                medicine_count += 1
            if medicine_count and medicine_count % 2 == 0 and deep_q:
                out.append(deep_q.pop(0))
                medicine_count += 1
            if medicine_count and medicine_count % 4 == 0 and icu_q:
                out.append(icu_q.pop(0))
                medicine_count += 1

        elif deep_q:
            out.append(deep_q.pop(0))
            medicine_count += 1
            added_this_round = True
            if medicine_count and medicine_count % 3 == 0 and icu_q:
                out.append(icu_q.pop(0))
                medicine_count += 1
        elif icu_q:
            out.append(icu_q.pop(0))
            medicine_count += 1
            added_this_round = True

        if anes_q and medicine_count and medicine_count % anesthesia_every == 0:
            out.append(anes_q.pop(0))

        if not added_this_round and anes_q:
            out.append(anes_q.pop(0))

    return out


def build_curriculum(
    units: list[CurriculumUnit] | None = None,
    anesthesia_pct: float | None = None,
) -> list[CurriculumUnit]:
    if units is None:
        units = build_units()
    pct = settings.anesthesia_crossover_percent if anesthesia_pct is None else anesthesia_pct
    bands: dict[str, list[CurriculumUnit]] = {
        "spine": [],
        "deep_medicine": [],
        "icu": [],
        "anesthesia": [],
    }
    for u in units:
        bands[_band_for_unit(u)].append(u)
    for k in bands:
        bands[k] = _ordered_within_band(bands[k])
    return _interleave(
        bands["spine"], bands["deep_medicine"], bands["icu"], bands["anesthesia"], pct
    )


def curriculum_path() -> Path:
    return Path(settings.chroma_dir).parent / "curriculum" / "units.json"


def save_curriculum(units: list[CurriculumUnit]) -> Path:
    path = curriculum_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "version": "1",
        "n_units": len(units),
        "units": [asdict(u) for u in units],
    }
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


def load_curriculum() -> list[CurriculumUnit]:
    path = curriculum_path()
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    return [CurriculumUnit(**u) for u in data.get("units", [])]


def main() -> None:
    units = build_units()
    ordered = build_curriculum(units)
    path = save_curriculum(ordered)
    bands = {b: 0 for b in ("spine", "deep_medicine", "icu", "anesthesia")}
    for u in ordered:
        bands[_band_for_unit(u)] += 1
    print(f"curriculum: {len(ordered)} units written to {path}")
    print(f"  bands: {bands}")
    crossovers = sum(1 for u in ordered if u.crossover_priority == "high")
    print(f"  high-crossover (ICU overlap) units: {crossovers}")


if __name__ == "__main__":
    main()
