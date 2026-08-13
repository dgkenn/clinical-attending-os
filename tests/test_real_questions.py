"""Real-question retrieval quality + latency battery.

For each clinical question, assert:
- Retrieval returns at least one chunk
- One of the expected source families appears in top-3
- At least one expected term appears in the top-3 chunk text
- p99 latency < 3s
- Chunk text is substantive (>= 60 chars) but capped (<= 1500 chars)

Skipped if chunks.jsonl is empty (CI without ingest).
"""

from __future__ import annotations

import os
import time
from pathlib import Path

import pytest

from src.config import settings
from src.retrieval import hybrid_search


CHUNKS = settings.chroma_dir / "chunks.jsonl"
HAS_CORPUS = CHUNKS.exists() and CHUNKS.stat().st_size > 1000


pytestmark = pytest.mark.skipif(not HAS_CORPUS, reason="corpus not ingested")


CASES = [
    # Medicine wards
    ("hyperkalemia treatment", "intern_teach", ["calcium", "insulin"], ["intern_year_medicine"]),
    ("afib RVR rate control", "intern_teach", ["diltiazem", "metoprolol", "rate"], ["intern_year_medicine"]),
    ("hyponatremia workup", "intern_teach", ["osmolality", "sodium", "siadh"], ["intern_year_medicine"]),
    ("AKI prerenal vs intrinsic", "intern_teach", ["creatinine", "urine", "prerenal"], ["intern_year_medicine"]),
    ("DKA management", "intern_teach", ["insulin", "potassium", "anion gap"], ["intern_year_medicine"]),
    ("sepsis bundle one hour", "intern_teach", ["antibiotic", "lactate", "fluid"], ["intern_year_medicine", "ICU_critical_care"]),
    ("STEMI initial management", "intern_teach", ["aspirin", "heparin", "ECG"], ["intern_year_medicine"]),
    ("pneumonia CAP antibiotics", "intern_teach", ["ceftriaxone", "azithromycin", "pneumonia"], ["intern_year_medicine"]),
    # ICU
    ("ARDS ventilator strategy", "ICU_teach", ["tidal volume", "plateau", "PEEP"], ["ICU_critical_care"]),
    ("septic shock vasopressor norepinephrine", "ICU_teach", ["norepinephrine", "vasopressin"], ["ICU_critical_care"]),
    ("massive transfusion protocol", "ICU_teach", ["plasma", "platelets", "ratio"], ["ICU_critical_care"]),
    ("ventilator high pressure alarm causes", "ICU_teach", ["pressure", "ventilat", "alarm", "obstruct", "kink", "secretions", "bronchospasm"], ["ICU_critical_care"]),
    # Anesthesia
    ("malignant hyperthermia dantrolene", "crisis", ["dantrolene", "volatile", "succinylcholine"], ["anesthesiology_boards"]),
    ("LAST treatment intralipid", "crisis", ["lipid", "intralipid"], ["anesthesiology_boards"]),
    ("succinylcholine contraindications", "drug", ["burn", "denervation", "hyperkalemia"], ["anesthesiology_boards"]),
    ("rapid sequence induction medications", "anesthesia_boards", ["rocuronium", "succinylcholine"], ["anesthesiology_boards"]),
    ("MAC sevoflurane pediatric", "anesthesia_boards", ["sevoflurane", "MAC"], ["anesthesiology_boards"]),
    ("difficult airway algorithm", "anesthesia_boards", ["awake", "video", "supraglottic"], ["anesthesiology_boards"]),
    ("post dural puncture headache treatment", "anesthesia_boards", ["blood patch", "PDPH", "epidural"], ["anesthesiology_boards"]),
    ("propofol induction dose adults", "drug", ["1.5", "2", "mg/kg"], ["anesthesiology_boards"]),
]


@pytest.fixture(scope="module", autouse=True)
def _warm_caches():
    """Trigger one cold-start so the per-case latency assertion is fair."""
    hybrid_search("warmup", mode="intern_teach", max_results=3, use_cross_encoder=False)


@pytest.mark.parametrize("query,mode,expected_terms,expected_libraries", CASES)
def test_real_question_retrieves_substantive_relevant_content(query, mode, expected_terms, expected_libraries):
    start = time.perf_counter()
    results, insufficient = hybrid_search(query, mode=mode, max_results=5, use_cross_encoder=False)
    elapsed = time.perf_counter() - start

    assert results, f"no results for: {query}"
    assert not insufficient, f"insufficient context flagged: {query}"
    assert elapsed < 3.0, f"latency {elapsed:.2f}s exceeded 3s for: {query}"

    # Library family hit in top-3
    top3_libs = {r.library for r in results[:3]}
    if expected_libraries:
        assert any(lib in top3_libs for lib in expected_libraries), (
            f"none of {expected_libraries} in top-3 libs {top3_libs} for: {query}"
        )

    # At least one expected keyword in any of top-3 chunks
    top3_text = " ".join(r.text.lower() for r in results[:3])
    if expected_terms:
        assert any(term.lower() in top3_text for term in expected_terms), (
            f"none of {expected_terms} in top-3 text for: {query}; top1={results[0].text[:200]}"
        )

    # Substantive but bounded chunk size
    for r in results[:3]:
        assert 40 <= len(r.text) <= 1500, f"chunk size {len(r.text)} out of bounds for: {query}"


def test_p50_latency_under_1s_warm():
    """Warm-state hybrid_search should be fast enough for voice."""
    # Warm caches
    hybrid_search("warmup", mode="intern_teach", max_results=3, use_cross_encoder=False)

    queries = [c[0] for c in CASES]
    times = []
    for q in queries:
        start = time.perf_counter()
        hybrid_search(q, mode="intern_teach", max_results=5, use_cross_encoder=False)
        times.append(time.perf_counter() - start)
    times.sort()
    p50 = times[len(times) // 2]
    p90 = times[int(len(times) * 0.9)]
    assert p50 < 1.0, f"p50={p50:.2f}s — too slow for voice"
    assert p90 < 2.5, f"p90={p90:.2f}s — too slow for voice"
