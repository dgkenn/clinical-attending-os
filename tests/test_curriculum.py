import json

import pytest

from src import curriculum


def _fact_row(idx: int, book: str, library: str, page: int, section: str, topic: str = "", chapter_number: int | None = 1) -> dict:
    return {
        "id": f"f-{book}-{idx}",
        "text": f"Fact {idx} about {topic or section} from {book}.",
        "metadata": {
            "book": book,
            "source_name": book,
            "library": library,
            "page": page,
            "section": section,
            "chapter_number": chapter_number,
            "chapter_title": f"Chapter {chapter_number}",
            "chunk_id": f"f-{book}-{idx}",
            "chunk_type": "fact",
            "topic_tags": topic,
        },
    }


def test_build_units_groups_by_book_chapter_section():
    rows = [
        _fact_row(1, "Intern Notes / Survival Guide", "intern_year_medicine", 5, "Hyperkalemia", "Hyperkalemia"),
        _fact_row(2, "Intern Notes / Survival Guide", "intern_year_medicine", 5, "Hyperkalemia", "Hyperkalemia"),
        _fact_row(3, "Intern Notes / Survival Guide", "intern_year_medicine", 6, "AKI", "AKI"),
        _fact_row(4, "Marino ICU Book", "ICU_critical_care", 100, "Vasopressors", "Vasopressors"),
    ]
    units = curriculum.build_units(rows)
    assert len(units) == 3
    intern_units = [u for u in units if u.book == "Intern Notes / Survival Guide"]
    assert len(intern_units) == 2
    hyper = [u for u in intern_units if u.section == "Hyperkalemia"][0]
    assert hyper.fact_count == 2


def test_icu_overlap_topics_get_high_crossover_priority():
    rows = [
        _fact_row(1, "Intern Notes / Survival Guide", "intern_year_medicine", 5, "Sepsis", "Sepsis"),
    ]
    units = curriculum.build_units(rows)
    assert units[0].crossover_priority == "high"


def test_curriculum_interleave_intern_first_then_anesthesia():
    rows = []
    for i in range(20):
        rows.append(_fact_row(i, "Intern Notes / Survival Guide", "intern_year_medicine", i + 1, f"Sec{i}", f"Topic{i}"))
    for i in range(5):
        rows.append(_fact_row(100 + i, "Stanford CA-1", "anesthesiology_boards", i + 1, f"Anes{i}", f"Anes{i}"))
    units = curriculum.build_units(rows)
    ordered = curriculum.build_curriculum(units, anesthesia_pct=0.10)
    # First unit must be from the spine
    assert ordered[0].book in curriculum.SPINE_SOURCES
    # An anesthesia unit must appear within the first 12 (1 in every 10 medicine)
    assert any(u.book == "Stanford CA-1" for u in ordered[:12])


def test_save_and_load_curriculum_round_trip(tmp_path, monkeypatch):
    monkeypatch.setattr(curriculum.settings, "chroma_dir", tmp_path)
    rows = [_fact_row(1, "Intern Notes / Survival Guide", "intern_year_medicine", 5, "Hyperkalemia", "Hyperkalemia")]
    units = curriculum.build_units(rows)
    ordered = curriculum.build_curriculum(units)
    path = curriculum.save_curriculum(ordered)
    assert path.exists()
    loaded = curriculum.load_curriculum()
    assert len(loaded) == len(ordered)
    assert loaded[0].unit_id == ordered[0].unit_id
