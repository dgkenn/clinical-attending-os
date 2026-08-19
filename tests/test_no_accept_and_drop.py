"""A parameter the system accepts but never stores is a lie it tells quietly.

This is the single most repeated defect in the project's history, and every
instance looked like success at the time:

  - `teach_back_quality` was accepted by submit_answer and dropped before
    log_attempt, so mechanism_quality sat at 0.0 forever and mastery was
    unreachable by construction — topics at 100% accuracy reported
    mastery_achieved = 0.
  - `transfer_success` the same, which made the intermediate and advanced
    mastery gates impossible to pass.
  - `grounded_in` was accepted, written only to a text log, and never added as
    a column — an audit that selected it died with "no such column".
  - `evidence` was accepted by submit_knowledge_points and discarded before
    record_knowledge_point, so every fact recorded through the only path car
    mode uses stored empty evidence however carefully the tutor quoted the user.

Each returned ok:true. None raised. All four were found weeks later by diffing a
session transcript against the database by hand.

So: for the recorders that matter, a parameter in the signature must be visibly
routed onward in the source. This is a coarse check — it reads the function body
for the parameter name rather than proving persistence — but every one of the
four failures above would have tripped it, because in each case the name simply
never appeared after the signature.
"""
from __future__ import annotations

import inspect

import pytest

# (import path, function, parameters that MUST be forwarded or persisted)
CONTRACTS = [
    ("src.mcp_endpoints", "submit_answer",
     ["teach_back_quality", "transfer_success", "user_answer_verbatim",
      "tutor_response", "grounded_in", "knowledge_points"]),
    ("src.student_model", "log_attempt",
     ["teach_back_quality", "transfer_success", "user_answer_verbatim",
      "tutor_response", "grounded_in", "graded_as_exposure"]),
    ("src.student_model", "record_knowledge_point",
     ["evidence", "confidence", "mistake_type", "triage"]),
    ("src.tutor_engine", "record_evaluated_answer",
     ["user_answer_verbatim", "tutor_response", "grounded_in"]),
]

# Fields carried inside a dict/list argument rather than as named parameters.
# submit_knowledge_points takes `points: list`, and each entry may carry
# `evidence` — which it accepted and silently discarded before calling
# record_knowledge_point, so the only fact path car mode uses stored empty
# evidence no matter how well the tutor quoted the answer.
DICT_KEY_CONTRACTS = [
    ("src.mcp_server", "submit_knowledge_points", ["evidence", "triage", "mistake_type"]),
]


@pytest.mark.parametrize("mod_name,fn_name,keys", DICT_KEY_CONTRACTS)
def test_dict_keys_are_forwarded_not_dropped(mod_name, fn_name, keys):
    fn = _fn(mod_name, fn_name)
    src = inspect.getsource(fn)
    for k in keys:
        assert k in src, (
            f"{mod_name}.{fn_name} never references the `{k}` key it accepts on "
            f"its input dicts — accept-and-drop")


def _fn(mod_name, fn_name):
    mod = __import__(mod_name, fromlist=[fn_name])
    return getattr(mod, fn_name)


@pytest.mark.parametrize("mod_name,fn_name,params", CONTRACTS)
def test_accepted_parameters_are_used_not_dropped(mod_name, fn_name, params):
    fn = _fn(mod_name, fn_name)
    sig = inspect.signature(fn)
    src = inspect.getsource(fn)
    # Everything after the signature — a parameter mentioned ONLY in the
    # signature is accepted and dropped.
    body = src.split(")", 1)[-1] if ")" in src else src

    for p in params:
        assert p in sig.parameters, f"{mod_name}.{fn_name} no longer accepts {p}"
        # Count occurrences outside the signature line(s).
        uses = body.count(p)
        assert uses >= 1, (
            f"{mod_name}.{fn_name} accepts `{p}` but never references it again — "
            f"accept-and-drop, the defect that made mastery unreachable and left "
            f"grounded_in unstored")


def test_the_capture_columns_actually_exist_on_the_table():
    """The other half: a parameter can be forwarded to a column that was never
    created. `grounded_in` was written to a log and queried as a column."""
    from src.student_model import conn, initialize_database

    initialize_database()
    with conn() as db:
        attempt_cols = {r[1] for r in db.execute("PRAGMA table_info(question_attempts)")}
        kp_cols = {r[1] for r in db.execute("PRAGMA table_info(knowledge_points)")}

    for col in ("teach_back_quality", "transfer_success", "user_answer_verbatim",
                "tutor_response", "grounded_in", "graded_as_exposure"):
        assert col in attempt_cols, f"question_attempts is missing {col}"
    for col in ("evidence", "first_presented_at"):
        assert col in kp_cols, f"knowledge_points is missing {col}"


def test_a_value_written_through_submit_answer_can_be_read_back():
    """End-to-end proof, not just a source-text heuristic."""
    from src.mcp_endpoints import submit_answer
    from src.student_model import conn

    submit_answer(
        topic="AcceptDropProbe", question="probe question for persistence",
        user_answer="graded summary", is_correct=True, confidence_reported=4,
        teach_back_quality=0.9, transfer_success=True,
        user_answer_verbatim="the exact words the user said",
        tutor_response="the exact teaching that came back",
        grounded_in="Marino ICU Book, p.42")
    with conn() as db:
        row = db.execute(
            "SELECT teach_back_quality, transfer_success, user_answer_verbatim, "
            "tutor_response, grounded_in FROM question_attempts "
            "WHERE topic=? ORDER BY attempt_id DESC LIMIT 1",
            ("AcceptDropProbe",)).fetchone()
    assert row["teach_back_quality"] == pytest.approx(0.9)
    assert row["transfer_success"] == 1
    assert row["user_answer_verbatim"] == "the exact words the user said"
    assert row["tutor_response"] == "the exact teaching that came back"
    assert row["grounded_in"] == "Marino ICU Book, p.42"
