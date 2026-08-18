"""Preferring a source must not mean teaching its expired numbers.

The maintainer named Marino as his preferred ICU source, so ICU queries were
routed to mode "ICU_teach", which ranks "Marino ICU Book" first. A probe
immediately afterwards for the first-line vasopressor in septic shock returned
four Marino passages, one of them stating verbatim:

    "Norepinephrine is often used as a second-line vasopressor behind dopamine"

That is the reverse of current practice, and the Surviving Sepsis 2021 guideline
sitting in the same corpus had been pushed off the page. The Little ICU Book is
a mid-2000s text: its physiology, mechanism and bedside approach do not age, but
its numeric targets and drug-of-choice calls have.

So source preference is now intent-dependent. Ask what the target, threshold or
first-line choice IS and society guidelines are promoted above any textbook.
Ask why something works, or how to approach it, and the preference stands.
"""
from __future__ import annotations

import pytest

from src.config import settings
from src.reranking import (
    _has_currency_sensitive_intent,
    _is_guideline_source,
)

CHUNKS = settings.chroma_dir / "chunks.jsonl"
HAS_CORPUS = CHUNKS.exists() and CHUNKS.stat().st_size > 1000


class TestIntentDetection:
    @pytest.mark.parametrize("q", [
        "what is the first-line vasopressor in septic shock",
        "what is the glucose target for critically ill patients",
        "what hemoglobin threshold is recommended for transfusion",
        "what is the current standard of care for ARDS",
        "what dose of hydrocortisone is indicated in septic shock",
        "what are the criteria for extubation",
    ])
    def test_asking_for_a_number_or_a_choice_is_currency_sensitive(self, q):
        assert _has_currency_sensitive_intent(q)

    @pytest.mark.parametrize("q", [
        "why does PEEP improve oxygenation",
        "how does hemodialysis clear solute",
        "what is the mechanism of intrinsic PEEP",
        "explain the Frank-Starling relationship in heart failure",
    ])
    def test_mechanism_questions_are_not_currency_sensitive(self, q):
        """These are exactly where the textbook should keep winning."""
        assert not _has_currency_sensitive_intent(q)


class TestGuidelineDetection:
    @pytest.mark.parametrize("meta", [
        {"source_name": "Society Guideline"},
        {"book": "Society Guideline: Guideline   KDIGO 2024 CKD"},
        {"filename": "Guideline - Surviving Sepsis Campaign 2021 (sepsis.ch backup).pdf"},
        {"filename": "Guideline - ACC AHA 2022 Heart Failure.pdf"},
    ])
    def test_guideline_sources_are_recognised(self, meta):
        assert _is_guideline_source(meta)

    @pytest.mark.parametrize("meta", [
        {"book": "Marino ICU Book"},
        {"book": "Morgan & Mikhail"},
        {"source_name": "MGH Housestaff Manual"},
    ])
    def test_textbooks_are_not_guidelines(self, meta):
        assert not _is_guideline_source(meta)

    def test_empty_metadata_is_not_a_guideline(self):
        assert not _is_guideline_source({})


class TestIntentIsReadFromTheUserNotTheExpansion:
    """Intent must come from the user's words, never from the retriever's own.

    Queries are expanded with synonyms before ranking, and the expansion for
    "norepinephrine" appends the literal phrase "first-line". So a plain lookup
    of "septic shock vasopressor norepinephrine" — which asks nothing about
    current standards — was classified as a what-is-the-first-line question,
    every textbook was demoted, and the ICU library fell out of the top 3. The
    system was inferring intent from vocabulary it had generated itself.
    """

    def test_the_expansion_injects_the_trigger_phrase(self):
        from src.retrieval import expand_query
        expanded = expand_query("septic shock vasopressor norepinephrine")
        assert "first-line" in expanded
        assert _has_currency_sensitive_intent(expanded), (
            "precondition: the expanded form does look currency-sensitive")

    def test_but_the_raw_query_does_not(self):
        assert not _has_currency_sensitive_intent(
            "septic shock vasopressor norepinephrine")

    @pytest.mark.skipif(not HAS_CORPUS, reason="corpus not ingested")
    def test_a_plain_lookup_keeps_the_icu_library(self):
        from src.retrieval import hybrid_search
        res, _ = hybrid_search("septic shock vasopressor norepinephrine",
                               mode="ICU_teach", max_results=3)
        libs = [r.model_dump().get("library") for r in res]
        assert "ICU_critical_care" in libs, f"expansion-driven demotion returned: {libs}"


@pytest.mark.skipif(not HAS_CORPUS, reason="corpus not ingested")
class TestEndToEndRanking:
    def _books(self, query, mode="ICU_teach", n=4):
        from src.retrieval import hybrid_search
        res, _ = hybrid_search(query, mode=mode, max_results=n)
        return [(r.model_dump().get("book") or r.model_dump().get("source_name") or "")
                for r in res]

    def test_a_target_question_surfaces_a_guideline(self):
        """The concrete regression: Marino's expired numbers must not monopolise
        a question about what the current target is."""
        books = self._books("what is the glucose target for critically ill patients")
        assert any("Guideline" in b for b in books), (
            f"no guideline in top results for a target question: {books}")

    def test_the_vasopressor_question_returns_the_guideline_not_the_textbook(self):
        """The worst case, and the one promotion-to-parity did not fix.

        Marino states "norepinephrine is often used as a second-line vasopressor
        behind dopamine" — the reverse of current practice. Ranked first for ICU
        topics, it took all eight top slots while the Surviving Sepsis chunk
        that says "we recommend using norepinephrine as the first-line agent"
        sat at rank 9, off the page. Parity was not enough; the textbook has to
        be actively out-ranked on this class of question.
        """
        books = self._books(
            "what is the first-line vasopressor recommended in septic shock", n=4)
        assert any("Guideline" in b for b in books), (
            f"the guideline lost its own recommendation question: {books}")

    def test_a_mechanism_question_still_prefers_the_icu_textbook(self):
        """The guard must not cost us the source preference it was built around."""
        books = self._books("why does PEEP improve oxygenation alveolar recruitment mechanism")
        assert any("Marino" in b for b in books), (
            f"Marino lost its own mechanism question: {books}")

    def test_an_approach_question_still_prefers_the_icu_textbook(self):
        books = self._books(
            "approach to spontaneous breathing trial rapid shallow breathing index")
        assert any("Marino" in b for b in books), f"Marino lost an approach question: {books}"

    def test_icu_topics_still_route_to_marino_at_all(self):
        """Guards the original fix: _attach_sources hardcoded mode='intern_teach',
        under which Marino ranks fifth of eight and never appeared."""
        from src.mcp_server import _attach_sources
        out = _attach_sources({"topic": "ARDS",
                               "retrieval_query": "lung protective ventilation tidal volume"})
        if not out.get("sources"):
            pytest.skip("retrieval returned nothing")
        assert out.get("retrieval_mode") == "ICU_teach"
        books = [s.get("book") or s.get("source_name") or "" for s in out["sources"]]
        assert any("Marino" in b for b in books), f"ICU topic did not reach Marino: {books}"
