"""Every dosing rule is machine-validated at boundary inputs.

Motivated by the mannitol_icp bug: a weight_based rule computed milligrams
(1000 mg/kg x 96 kg = 96,000) while its `units` field said "mL (of 20%
solution)" — so the drill graded "96,000 mL" as the correct answer. Nothing
checked that a rule's computed quantity matches its declared unit label.

These tests iterate data/dosing_rules.json directly (not the DB) so a bad
edit fails CI before it is ever seeded.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

from src.dosing_engine import compute_answer, RECALL_ONLY_TYPE

RULES = json.loads(
    (Path(__file__).resolve().parents[1] / "data" / "dosing_rules.json").read_text(
        encoding="utf-8"
    )
)
CALC_RULES = [
    r for r in RULES if not r.get("recall_only") and r.get("calc_type") != RECALL_ONLY_TYPE
]


def _boundary_inputs(rule: dict) -> list[dict]:
    """Low/high corner of every randomized input (plus midpoint weight)."""
    spec = rule.get("randomize_json", {}) or {}
    corners: list[dict] = [{}, {}]
    for key, val in spec.items():
        if isinstance(val, dict) and val.get("choices"):
            corners[0][key] = min(val["choices"])
            corners[1][key] = max(val["choices"])
        elif isinstance(val, list) and len(val) == 2 and all(
            isinstance(v, (int, float)) for v in val
        ):
            corners[0][key] = float(val[0])
            corners[1][key] = float(val[1])
        elif isinstance(val, list) and val:
            corners[0][key] = val[0]
            corners[1][key] = val[-1]
    return corners


@pytest.mark.parametrize("rule", CALC_RULES, ids=lambda r: r["id"])
def test_rule_computes_finite_positive_answer_at_boundaries(rule):
    for inputs in _boundary_inputs(rule):
        answer, steps = compute_answer(rule, dict(inputs))
        assert isinstance(answer, (int, float)), f"{rule['id']}: non-numeric answer"
        assert math.isfinite(answer), f"{rule['id']}: non-finite answer {answer}"
        assert answer > 0, f"{rule['id']}: non-positive answer {answer} for {inputs}"
        assert steps, f"{rule['id']}: no worked steps"


@pytest.mark.parametrize("rule", CALC_RULES, ids=lambda r: r["id"])
def test_rule_units_label_matches_computed_quantity(rule):
    """The units field must agree with what the calc actually returns.

    weight_based with mg_per_kg  -> milligrams (units must mention mg, and NOT
                                    claim mL: that is the mannitol bug)
    weight_based with units_per_kg -> units
    mass_to_volume               -> mL
    infusion_rate                -> a per-hour rate (mL/hr or units/hr)
    max_dose                     -> mg or mL (dose ceiling may be expressed
                                    as volume via concentration)
    """
    units = (rule.get("units") or "").lower()
    calc = rule.get("calc_type")
    params = rule.get("params_json", {}) or {}
    rid = rule["id"]

    if calc == "weight_based":
        if params.get("mg_per_kg"):
            assert "mg" in units, f"{rid}: mg_per_kg rule but units {units!r}"
            assert "ml" not in units, (
                f"{rid}: computes MILLIGRAMS but labels the answer {units!r} — "
                "this is the mannitol-class unit bug; use mass_to_volume or "
                "recall_only instead"
            )
        elif params.get("units_per_kg"):
            assert "unit" in units, f"{rid}: units_per_kg rule but units {units!r}"
    elif calc == "mass_to_volume":
        assert "ml" in units, f"{rid}: mass_to_volume rule but units {units!r}"
    elif calc == "infusion_rate":
        assert "/hr" in units or "per hour" in units, (
            f"{rid}: infusion_rate rule but units {units!r}"
        )


def test_no_two_element_range_that_should_be_choices():
    """A 2-element numeric list is a RANGE. Concentrations and other discrete
    clinical options must use {"choices": [...]} — a range invents products
    that don't exist (bupivacaine 0.3%/0.4%)."""
    for rule in CALC_RULES:
        for key, val in (rule.get("randomize_json") or {}).items():
            if "concentration" in key and isinstance(val, list) and len(val) == 2:
                pytest.fail(
                    f"{rule['id']}: {key} is a 2-element list (continuous range); "
                    "use {\"choices\": [...]} for discrete concentrations"
                )


def test_recall_only_rules_have_recall_material():
    for rule in RULES:
        if rule.get("recall_only"):
            assert rule.get("recall_question"), f"{rule['id']}: recall_only without recall_question"
            assert rule.get("dose_fact") or rule.get("anchor"), (
                f"{rule['id']}: recall_only without dose_fact/anchor"
            )
