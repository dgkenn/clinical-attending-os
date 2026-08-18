"""record_knowledge_point must dedupe fuzzy near-matches, not just exact text.

The fuzzy matcher (src/fact_matcher.py) was wired into log_tangent only. The
much more common write path — submit_answer's derived-knowledge-point
fallback, which keys point text off the QUESTION asked — had no dedupe beyond
exact string equality. Different questions routinely probe the same fact with
different wording, and a sweep of the live database found two such duplicates
had already formed from ordinary graded answers, not tangents:

    "STEMI: oxygen only if SpO2 <90%..." / "...SpO2 less than 90..."
    "Variceal bleed transfusion strategy: restrictive — target Hgb 7-8..."
      / "...transfusion strategy is restrictive, target Hgb 7-8..."

Fixed at the lowest layer (record_knowledge_point itself) so every caller
gets it for free, rather than depending on each call site to remember.
"""
from __future__ import annotations

from src.student_model import conn, record_knowledge_point


def _row(point):
    with conn() as db:
        return db.execute(
            "SELECT topic, point, times_seen, times_correct FROM knowledge_points "
            "WHERE point = ?", (point,)).fetchone()


def _count():
    with conn() as db:
        return db.execute("SELECT COUNT(*) FROM knowledge_points").fetchone()[0]


def test_a_reworded_fact_merges_onto_the_existing_row():
    original = "Dedupe probe: naloxone reverses opioid-induced respiratory depression rapidly"
    reworded = "Dedupe probe: naloxone rapidly reverses respiratory depression from opioids"

    before = _count()
    record_knowledge_point(topic="ProbeDedupe", point=original, is_correct=True, confidence=4)
    after_first = _count()
    assert after_first == before + 1

    record_knowledge_point(topic="ProbeDedupe", point=reworded, is_correct=True, confidence=4)
    after_second = _count()
    assert after_second == after_first, "a reworded duplicate must not create a second row"

    row = _row(original)
    assert row is not None
    assert row[2] == 2, "the ORIGINAL row's history must advance, not a new row's"


def test_a_genuinely_different_fact_still_creates_its_own_row():
    a = "Dedupe probe distinct A: propranolol is nonselective and used for variceal prophylaxis"
    b = "Dedupe probe distinct B: metoprolol is cardioselective and inadequate for that purpose"
    before = _count()
    record_knowledge_point(topic="ProbeDedupe", point=a, is_correct=True, confidence=4)
    record_knowledge_point(topic="ProbeDedupe", point=b, is_correct=True, confidence=4)
    assert _count() == before + 2


def test_dedupe_never_blocks_a_write_even_on_ambiguous_overlap():
    """Unlike log_tangent, this path must always succeed — a graded answer
    can never be left half-recorded pending a judgement call."""
    a = "Dedupe probe gray zone: sepsis bundle draws lactate and cultures first"
    b = "Dedupe probe gray zone: sepsis hour-1 bundle orders lactate then cultures then antibiotics"
    r1 = record_knowledge_point(topic="ProbeDedupe", point=a, is_correct=True, confidence=3)
    r2 = record_knowledge_point(topic="ProbeDedupe", point=b, is_correct=True, confidence=3)
    assert r1 is not None and r2 is not None


def test_existing_facts_are_surfaced_with_the_topic():
    """Root cause of most duplicates: the tutor wrote facts blind.

    11 of 21 near-duplicate pairs in the live database spanned sessions — a
    June card and an August card for one fact — because the tutor re-taught a
    topic with no idea what was already tracked. The backend knew and never
    said so. get_next_topic now ships the existing facts so the tutor can
    reinforce (reuse the exact wording, which the matcher then merges) instead
    of forking a parallel history that costs two reviews forever.
    """
    from src.mcp_server import _attach_existing_facts
    from src.student_model import record_knowledge_point

    point = "Existing-facts probe: a distinctive clinical threshold worth reinforcing"
    record_knowledge_point(topic="ProbeExisting", point=point, is_correct=False, confidence=2)

    out = _attach_existing_facts({"topic": "ProbeExisting"})
    facts = out.get("existing_facts", [])
    assert any(f["point"] == point for f in facts), "the tutor must see what already exists"
    assert "REUSE ITS EXACT WORDING" in out.get("existing_facts_note", "")


def test_attaching_existing_facts_never_breaks_topic_selection():
    from src.mcp_server import _attach_existing_facts
    assert _attach_existing_facts({}) == {}
    assert _attach_existing_facts("not a dict") == "not a dict"
    out = _attach_existing_facts({"topic": "NoSuchTopicAnywhere"})
    assert out["existing_facts"] == []
