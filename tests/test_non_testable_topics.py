"""Topics whose actual source content is administrative, not clinical, must
not be served as graded review material.

"Consults" was served three times in one session and answered zero — the
user identified why themselves: "it's just a checklist, not clinical
knowledge." Verified by checking what a bare-name retrieval query for the
topic actually returns: MGH Housestaff Manual "Calling Consults" — "TIPS FOR
CALLING CONSULTS: To do BEFORE you call: place order in Epic...". That is
workflow, not testable reasoning.

The fix is evidence-based per topic, not a blanket sweep: Shock, Monitoring,
Respiratory physiology, IV anesthetics, and Oxygenation and ventilation were
each checked and confirmed to return real clinical content, so they stay
eligible.
"""
from __future__ import annotations

from src.student_model import _NON_TOPICS, get_due_reviews


def test_verified_administrative_topics_are_excluded():
    assert "consults" in _NON_TOPICS
    assert "cross-cover pages" in _NON_TOPICS
    names = {d["topic"] for d in get_due_reviews(limit=500)}
    assert "Consults" not in names
    assert "Cross-cover pages" not in names


def test_verified_clinical_topics_are_not_swept_in():
    """These returned genuine clinical content when checked and must remain
    eligible — the exclusion is per-topic evidence, not a category sweep."""
    for clinical_topic in ("shock", "monitoring", "respiratory physiology",
                           "iv anesthetics", "oxygenation and ventilation"):
        assert clinical_topic not in _NON_TOPICS
