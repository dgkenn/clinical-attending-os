"""Retrieval must return teachable content, not scaffolding.

Every case here is a real failure that reached the tutor. The common thread is
that a passage can be lexically perfect for a query while teaching nothing —
a heading, a bibliography, an intake checklist — and those score well on
exactly the components (BM25, keyword overlap) that reward term density.
"""
from __future__ import annotations

import pytest

from src.config import settings
from src.reranking import (
    _actionability,
    _citation_density,
    _has_management_intent,
)
from src.retrieval import _is_contentless, _strip_citation_header, hybrid_search

CHUNKS = settings.chroma_dir / "chunks.jsonl"
HAS_CORPUS = CHUNKS.exists() and CHUNKS.stat().st_size > 1000


def test_heading_only_chunks_are_contentless():
    # BM25 normalises by length, so a heading whose every token matches the
    # query outscores the real passage. One took a top-3 slot on afib RVR.
    assert _is_contentless("Section: Atrial Fibrillation & Flutter")
    assert _is_contentless("Section: Summary of EKG Changes")
    assert _is_contentless("")


def test_short_but_useful_chunks_survive():
    """Dose and threshold lines are legitimately terse — the digit rule keeps
    them, and over-filtering would delete exactly the facts worth drilling."""
    assert not _is_contentless("Propofol 1.5-2 mg/kg IV")
    assert not _is_contentless("clinically apparent with 5 g/dl desaturated Hb")
    assert not _is_contentless(
        "Section: CHEST PAIN. CHEST PAIN Details of pain: onset, site, nature."
    )


def test_citation_header_is_stripped_but_content_survives():
    raw = ("Section: Source: StatPearls. Source: StatPearls NCBI Bookshelf "
           "NBK ID: NBK545267 URL: https://www.ncbi.nlm.nih.gov/books/NBK545267/ "
           "Topic: STEMI: Diagnosis and Acute Management")
    assert "NBK545267" not in _strip_citation_header(raw + " " + "x" * 60)
    # A chunk that is ONLY a header must not be stripped to nothing.
    assert _strip_citation_header(raw)


def test_management_intent_is_detected_narrowly():
    assert _has_management_intent("STEMI initial management")
    assert _has_management_intent("how do you treat hyperkalemia")
    # A differential question is NOT a management question — the actionability
    # boost must not hijack it and bury the diagnostic algorithm.
    assert not _has_management_intent("differential of chest pain")
    assert not _has_management_intent("causes of hyponatremia")


def test_actionability_prefers_treatment_over_checklist():
    treatment = ("If STEMI, immediately call cardiology and start heparin drip, "
                 "aspirin load, and plavix or brilinta load")
    checklist = ("Details of pain: Onset, site, nature. Hemodynamic stability. "
                 "Associated symptoms. Interventions already performed.")
    assert _actionability(treatment) > _actionability(checklist)


def test_citation_density_flags_bibliography_not_cited_prose():
    biblio = ("6. Chioncel O, Mebazaa A, Maggioni AP, et al. Acute heart failure. "
              "7. Smith J, Brown K, et al. Something else. "
              "8. Doe A, Roe B, et al. A third citation here.")
    prose = ("Acute decompensated heart failure is managed with IV diuresis; "
             "titrate furosemide to urine output and monitor renal function "
             "closely throughout the admission (Circulation 2022;145:e895).")
    assert _citation_density(biblio) > _citation_density(prose)


@pytest.mark.skipif(not HAS_CORPUS, reason="corpus not ingested")
def test_stemi_management_reaches_actual_management():
    """The regression this whole module exists for: 'STEMI initial management'
    returned a chest-pain intake checklist and a bibliography, while the
    passage naming aspirin and heparin sat at rank 5."""
    results, insufficient = hybrid_search(
        "STEMI initial management", mode="intern_teach", max_results=5,
        use_cross_encoder=False,
    )
    assert results and not insufficient
    top3 = " ".join(r.text.lower() for r in results[:3])
    assert any(t in top3 for t in ("aspirin", "heparin", "ecg", "pci")), (
        f"no management content in top-3; got: {[r.text[:70] for r in results[:3]]}"
    )


@pytest.mark.skipif(not HAS_CORPUS, reason="corpus not ingested")
def test_differential_query_still_returns_the_algorithm():
    """Guard the other side of the actionability boost: a differential question
    must still get the diagnostic passage, not a drug list."""
    results, _ = hybrid_search(
        "differential of chest pain", mode="intern_teach", max_results=3,
        use_cross_encoder=False,
    )
    joined = " ".join(r.text.lower() for r in results[:3])
    assert any(t in joined for t in ("differential", "ddx", "algorithm", "dissection"))


@pytest.mark.skipif(not HAS_CORPUS, reason="corpus not ingested")
def test_no_heading_only_chunk_is_ever_returned():
    for query in ("afib RVR rate control", "hyperkalemia treatment",
                  "sepsis bundle one hour"):
        results, _ = hybrid_search(query, mode="intern_teach", max_results=5,
                                   use_cross_encoder=False)
        for r in results:
            assert not _is_contentless(r.text), f"{query!r} returned {r.text!r}"
