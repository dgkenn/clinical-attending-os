"""A fact you cannot trace is a fact you cannot check.

`knowledge_points` recorded no provenance, so when the tutor served a stored
fact for review it had nothing to cite and honestly wrote "<Topic> knowledge
point bank" on 11 of 17 answers. That looked like a lazy tutor and was actually
a missing column — blaming the tutor would have fixed nothing.

It also matters more than tidiness: an invented vasopressor threshold was
drilled five times because nothing recorded where it supposedly came from, so
there was nothing to check it against.
"""
from __future__ import annotations

import pytest

from src.student_model import conn, record_knowledge_point

TOPIC = "ProvenanceProbeTopic"


def _row(point):
    with conn() as db:
        return db.execute(
            "SELECT source, evidence FROM knowledge_points WHERE topic=? AND point=?",
            (TOPIC, point)).fetchone()


def test_a_fact_records_where_it_came_from():
    point = "Provenance probe alpha: the fictional Zetamine clearance ceiling is 40 units"
    record_knowledge_point(topic=TOPIC, point=point, is_correct=True, confidence=4,
                           source="Marino ICU Book, Hemodynamic Monitoring, p.127")
    assert _row(point)["source"] == "Marino ICU Book, Hemodynamic Monitoring, p.127"


def test_provenance_is_sticky_once_known():
    """A later answer that omits the citation must not erase it — otherwise one
    careless review discards work that was done properly."""
    point = "Provenance probe beta: the imaginary Korrin index inverts above pH 7.9"
    record_knowledge_point(topic=TOPIC, point=point, is_correct=True, confidence=4,
                           source="Marino ICU Book, p.42")
    record_knowledge_point(topic=TOPIC, point=point, is_correct=True, confidence=4)
    assert _row(point)["source"] == "Marino ICU Book, p.42"


def test_submit_answer_passes_the_question_citation_down_to_the_fact():
    """The question's citation IS the fact's provenance — without this a fact
    born in a well-grounded session still has nothing to cite next time."""
    from src.mcp_endpoints import submit_answer

    point = "Provenance probe gamma: the notional Vandel maneuver requires left lateral tilt"
    submit_answer(
        topic=TOPIC, question="probe question", user_answer="probe answer",
        is_correct=True, user_answer_verbatim="probe answer",
        tutor_response="Right, and here is why.",
        grounded_in="MGH Housestaff Manual, Hyperkalemia, p.21",
        knowledge_points=[{"point": point, "correct": True, "evidence": "probe answer"}])
    assert _row(point)["source"] == "MGH Housestaff Manual, Hyperkalemia, p.21"


def test_served_facts_expose_their_source():
    """The tutor cannot cite what it is not given."""
    from src.mcp_server import get_due_knowledge_points

    served = get_due_knowledge_points(limit=200)["todays_set"]
    if served:
        assert "source" in served[0], "served facts must carry provenance"


def test_a_self_referential_citation_is_not_stored_as_provenance():
    """The symptom must not be copied forward as though it were a source."""
    from src.answer_evidence import citation_quality

    assert citation_quality("Delirium knowledge point bank")[0] == "self_referential"
    assert citation_quality("Marino ICU Book, p.127")[0] == "real"
