"""Tests for the drug-dosing drill module.

SAFETY NOTE: each calc_type is tested with known inputs against exact expected
outputs — these are not approximate. The engine must produce the correct number
deterministically.

Uses the same fresh_db fixture pattern as test_curriculum_coverage.py.
"""
from __future__ import annotations

import json
import math
import os
import tempfile
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# fresh_db fixture (identical to test_curriculum_coverage.py)
# ---------------------------------------------------------------------------

@pytest.fixture(autouse=True)
def fresh_db():
    """Give every test a brand-new, fully isolated SQLite file."""
    import src.student_model as _sm
    from src.config import settings

    tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
    tmp.close()
    new_path = tmp.name

    original_path = settings.sqlite_db_path
    settings.sqlite_db_path = Path(new_path)
    os.environ["SQLITE_DB_PATH"] = new_path
    _sm._WAL_INIT_PATHS.clear()

    from src.student_model import initialize_database
    initialize_database()
    yield

    settings.sqlite_db_path = original_path
    os.environ.pop("SQLITE_DB_PATH", None)
    _sm._WAL_INIT_PATHS.clear()
    try:
        os.unlink(new_path)
    except OSError:
        pass


# Convenience: path to the real starter set
DOSING_RULES_PATH = str(Path(__file__).parent.parent / "data" / "dosing_rules.json")


# ---------------------------------------------------------------------------
# 1. Calc engine — known-input exact numeric tests
# ---------------------------------------------------------------------------

class TestCalcEngineWeightBased:
    def test_succinylcholine_80kg(self):
        """1.5 mg/kg × 80 kg = 120 mg (exactly)."""
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "weight_based", "params_json": {"mg_per_kg": 1.5}}
        answer, steps = compute_answer(rule, {"weight_kg": 80.0})
        assert answer == pytest.approx(120.0, abs=0.001)
        assert any("120" in s for s in steps)

    def test_rocuronium_70kg(self):
        """1.2 mg/kg × 70 kg = 84 mg."""
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "weight_based", "params_json": {"mg_per_kg": 1.2}}
        answer, steps = compute_answer(rule, {"weight_kg": 70.0})
        assert answer == pytest.approx(84.0, abs=0.001)

    def test_dantrolene_60kg(self):
        """2.5 mg/kg × 60 kg = 150 mg."""
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "weight_based", "params_json": {"mg_per_kg": 2.5}}
        answer, steps = compute_answer(rule, {"weight_kg": 60.0})
        assert answer == pytest.approx(150.0, abs=0.001)

    def test_units_per_kg(self):
        """Heparin 60 units/kg × 90 kg = 5400 units."""
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "weight_based", "params_json": {"units_per_kg": 60}}
        answer, steps = compute_answer(rule, {"weight_kg": 90.0})
        assert answer == pytest.approx(5400.0, abs=0.001)

    def test_ml_per_kg(self):
        """Pediatric bolus 20 mL/kg × 15 kg = 300 mL."""
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "weight_based", "params_json": {"mL_per_kg": 20}}
        answer, steps = compute_answer(rule, {"weight_kg": 15.0})
        assert answer == pytest.approx(300.0, abs=0.001)

    def test_worked_steps_present(self):
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "weight_based", "params_json": {"mg_per_kg": 2.0}}
        _, steps = compute_answer(rule, {"weight_kg": 75.0})
        assert isinstance(steps, list) and len(steps) >= 1
        assert any("150" in s for s in steps)  # 2.0 × 75 = 150


class TestCalcEngineInfusionRate:
    def test_norepinephrine_standard(self):
        """NE 0.1 mcg/kg/min × 80 kg × 60 / 16 mcg/mL = 30 mL/hr."""
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "infusion_rate", "params_json": {"concentration_mcg_mL": 16.0}}
        answer, steps = compute_answer(rule, {"weight_kg": 80.0, "dose_mcg_kg_min": 0.1})
        expected = (0.1 * 80.0 * 60) / 16.0  # = 30.0
        assert answer == pytest.approx(expected, abs=0.001)

    def test_phenylephrine_75kg_1mcg(self):
        """Phenyl 1.0 mcg/kg/min × 75 kg × 60 / 100 mcg/mL = 45 mL/hr."""
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "infusion_rate", "params_json": {"concentration_mcg_mL": 100.0}}
        answer, _ = compute_answer(rule, {"weight_kg": 75.0, "dose_mcg_kg_min": 1.0})
        expected = (1.0 * 75.0 * 60) / 100.0  # = 45.0
        assert answer == pytest.approx(expected, abs=0.001)

    def test_insulin_drip_70kg(self):
        """Insulin 0.1 units/kg/hr × 70 kg = 7 units/hr."""
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "infusion_rate",
                "params_json": {"concentration_units_per_mL": 1.0, "dose_units_kg_hr": 0.1}}
        answer, steps = compute_answer(rule, {"weight_kg": 70.0})
        assert answer == pytest.approx(7.0, abs=0.001)

    def test_vasopressin_fixed(self):
        """Vasopressin fixed 0.04 units/min → 0.04 × 60 = 2.4 units/hr."""
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "infusion_rate",
                "params_json": {"fixed_rate_units_per_hr": 0.04,
                                "concentration_units_per_mL": 1.0}}
        answer, steps = compute_answer(rule, {"weight_kg": 80.0})
        assert answer == pytest.approx(0.04 * 60, abs=0.001)

    def test_ne_formula_in_steps(self):
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "infusion_rate", "params_json": {"concentration_mcg_mL": 16.0}}
        _, steps = compute_answer(rule, {"weight_kg": 80.0, "dose_mcg_kg_min": 0.2})
        combined = " ".join(steps)
        assert "mL/hr" in combined


class TestCalcEngineMaxDose:
    def test_lidocaine_no_epi_1pct_80kg(self):
        """Lido no-epi: 4.5 mg/kg × 80 kg = 360 mg; 1% = 10 mg/mL → 36 mL."""
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "max_dose",
                "params_json": {"mg_per_kg": 4.5, "concentration_mg_mL": 10.0}}
        answer, steps = compute_answer(rule, {"weight_kg": 80.0, "concentration_pct": 1.0})
        assert answer == pytest.approx(36.0, abs=0.001)

    def test_bupivacaine_0_5pct_70kg(self):
        """Bupiv: 2.5 mg/kg × 70 = 175 mg; 0.5% = 5 mg/mL → 35 mL."""
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "max_dose",
                "params_json": {"mg_per_kg": 2.5, "concentration_mg_mL": 5.0}}
        answer, steps = compute_answer(rule, {"weight_kg": 70.0, "concentration_pct": 0.5})
        assert answer == pytest.approx(35.0, abs=0.001)

    def test_max_mg_in_steps(self):
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "max_dose",
                "params_json": {"mg_per_kg": 4.5, "concentration_mg_mL": 10.0}}
        _, steps = compute_answer(rule, {"weight_kg": 100.0, "concentration_pct": 1.0})
        combined = " ".join(steps)
        assert "450" in combined  # 4.5 × 100


class TestCalcEngineMassToVolume:
    def test_calcium_gluconate_10pct(self):
        """CaGluc 1000 mg / 100 mg/mL = 10 mL."""
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "mass_to_volume",
                "params_json": {"dose_mg": 1000, "concentration_mg_mL": 100.0}}
        answer, steps = compute_answer(rule, {"weight_kg": 70.0})
        assert answer == pytest.approx(10.0, abs=0.001)

    def test_d50_volume(self):
        """D50W: 25000 mg / 500 mg/mL = 50 mL."""
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "mass_to_volume",
                "params_json": {"dose_mg": 25000, "concentration_mg_mL": 500.0}}
        answer, steps = compute_answer(rule, {"weight_kg": 70.0})
        assert answer == pytest.approx(50.0, abs=0.001)

    def test_amiodarone_acls(self):
        """Amiodarone 300 mg / 50 mg/mL = 6 mL."""
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "mass_to_volume",
                "params_json": {"dose_mg": 300, "concentration_mg_mL": 50.0}}
        answer, steps = compute_answer(rule, {"weight_kg": 80.0})
        assert answer == pytest.approx(6.0, abs=0.001)


class TestCalcEngineRateLimited:
    def test_421_70kg(self):
        """4-2-1: 70 kg → 40 + 20 + 50 = 110 mL/hr."""
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "rate_limited_correction",
                "params_json": {"rule": "4-2-1",
                                "rate_first_10kg": 4, "rate_next_10kg": 2, "rate_above_20kg": 1}}
        answer, steps = compute_answer(rule, {"weight_kg": 70.0})
        assert answer == pytest.approx(110.0, abs=0.001)

    def test_421_10kg(self):
        """4-2-1: 10 kg → 4 × 10 = 40 mL/hr."""
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "rate_limited_correction",
                "params_json": {"rule": "4-2-1",
                                "rate_first_10kg": 4, "rate_next_10kg": 2, "rate_above_20kg": 1}}
        answer, steps = compute_answer(rule, {"weight_kg": 10.0})
        assert answer == pytest.approx(40.0, abs=0.001)

    def test_421_15kg(self):
        """4-2-1: 15 kg → 40 + 2×5 = 50 mL/hr."""
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "rate_limited_correction",
                "params_json": {"rule": "4-2-1",
                                "rate_first_10kg": 4, "rate_next_10kg": 2, "rate_above_20kg": 1}}
        answer, steps = compute_answer(rule, {"weight_kg": 15.0})
        assert answer == pytest.approx(50.0, abs=0.001)

    def test_hyponatremia_max_correction(self):
        """Na correction max: returns max_correction_meq_per_24h (10 mEq/L/24h)."""
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "rate_limited_correction",
                "params_json": {"max_correction_meq_per_24h": 10,
                                "safe_rapid_bolus_meq": 6}}
        answer, steps = compute_answer(rule, {"current_na": 118, "weight_kg": 70.0})
        assert answer == pytest.approx(10.0, abs=0.001)
        assert any("10" in s for s in steps)

    def test_steps_mention_ods(self):
        """Safety term (ODS) should appear in hyponatremia steps."""
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "rate_limited_correction",
                "params_json": {"max_correction_meq_per_24h": 10,
                                "safe_rapid_bolus_meq": 6}}
        _, steps = compute_answer(rule, {"current_na": 120, "weight_kg": 70.0})
        combined = " ".join(steps).upper()
        assert "ODS" in combined or "OSMOTIC" in combined or "DEMYELINATION" in combined


class TestCalcEngineUnitConversion:
    def test_1pct_is_10mg_ml(self):
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "unit_conversion", "params_json": {}}
        answer, steps = compute_answer(rule, {"concentration_pct": 1.0})
        assert answer == pytest.approx(10.0, abs=0.001)

    def test_05pct_is_5mg_ml(self):
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "unit_conversion", "params_json": {}}
        answer, steps = compute_answer(rule, {"concentration_pct": 0.5})
        assert answer == pytest.approx(5.0, abs=0.001)

    def test_2pct_is_20mg_ml(self):
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "unit_conversion", "params_json": {}}
        answer, steps = compute_answer(rule, {"concentration_pct": 2.0})
        assert answer == pytest.approx(20.0, abs=0.001)


class TestCalcEngineInvalidType:
    def test_unknown_calc_type_raises(self):
        from src.dosing_engine import compute_answer
        rule = {"calc_type": "eval_injection", "params_json": {}}
        with pytest.raises(ValueError, match="Unknown calc_type"):
            compute_answer(rule, {"weight_kg": 70.0})


# ---------------------------------------------------------------------------
# 2. Input sampler — randomized inputs land in specified ranges
# ---------------------------------------------------------------------------

class TestInputSampler:
    def test_weight_in_range(self):
        from src.dosing_engine import _sample_inputs
        for _ in range(50):
            inputs = _sample_inputs({"weight_kg": [50, 120]})
            assert 50.0 <= inputs["weight_kg"] <= 120.0

    def test_discrete_concentration_choice(self):
        from src.dosing_engine import _sample_inputs
        valid = {0.5, 1.0, 1.5, 2.0}
        for _ in range(30):
            inputs = _sample_inputs({"concentration_pct": [0.5, 1.0, 1.5, 2.0]})
            assert inputs["concentration_pct"] in valid

    def test_weight_is_whole_number(self):
        """Weight samples are rounded to whole kg."""
        from src.dosing_engine import _sample_inputs
        for _ in range(20):
            inputs = _sample_inputs({"weight_kg": [60, 80]})
            assert inputs["weight_kg"] == round(inputs["weight_kg"])


# ---------------------------------------------------------------------------
# 3. generate_dosing_drill — structure + computed answer correctness
# ---------------------------------------------------------------------------

class TestGenerateDosingDrill:
    def _make_rule(self, calc_type, params, randomize, units="mg", drug="TestDrug"):
        return {
            "drug": drug,
            "context": "test context",
            "calc_type": calc_type,
            "params_json": params,
            "randomize_json": randomize,
            "units": units,
            "source": "test",
            "explanation": "test explanation",
        }

    def test_structure_keys_present(self):
        from src.dosing_engine import generate_dosing_drill
        rule = self._make_rule(
            "weight_based", {"mg_per_kg": 1.5}, {"weight_kg": [60, 80]}
        )
        drill = generate_dosing_drill(rule)
        required = {"drug", "scenario_text", "given", "answer", "units",
                    "tolerance", "worked_steps", "source", "explanation", "calc_type"}
        assert required <= drill.keys(), f"Missing keys: {required - drill.keys()}"

    def test_answer_does_not_appear_in_scenario(self):
        """Scenario text must NOT contain the numeric answer."""
        from src.dosing_engine import generate_dosing_drill
        rule = self._make_rule(
            "weight_based", {"mg_per_kg": 2.5}, {"weight_kg": [70, 70]}  # fixed 70 kg
        )
        drill = generate_dosing_drill(rule)
        answer_str = str(round(drill["answer"]))
        assert answer_str not in drill["scenario_text"], (
            f"Answer {answer_str} leaked into scenario: {drill['scenario_text']}"
        )

    def test_computed_answer_matches_engine_directly(self):
        """Drill answer == calling compute_answer directly with the same inputs."""
        from src.dosing_engine import generate_dosing_drill, compute_answer
        import random
        random.seed(42)
        rule = self._make_rule(
            "infusion_rate",
            {"concentration_mcg_mL": 16.0},
            {"weight_kg": [70, 70], "dose_mcg_kg_min": [0.1, 0.1]},
            units="mL/hr",
        )
        drill = generate_dosing_drill(rule)
        direct, _ = compute_answer(rule, drill["given"])
        assert drill["answer"] == pytest.approx(direct, abs=0.001)

    def test_tolerance_is_5pct(self):
        from src.dosing_engine import generate_dosing_drill
        rule = self._make_rule(
            "weight_based", {"mg_per_kg": 1.5}, {"weight_kg": [60, 100]}
        )
        drill = generate_dosing_drill(rule)
        assert drill["tolerance"] == pytest.approx(0.05, abs=0.001)

    def test_worked_steps_is_list(self):
        from src.dosing_engine import generate_dosing_drill
        rule = self._make_rule(
            "mass_to_volume",
            {"dose_mg": 1000, "concentration_mg_mL": 100.0},
            {"weight_kg": [60, 80]},
            units="mL",
        )
        drill = generate_dosing_drill(rule)
        assert isinstance(drill["worked_steps"], list)
        assert len(drill["worked_steps"]) >= 1

    def test_given_weight_in_range(self):
        from src.dosing_engine import generate_dosing_drill
        rule = self._make_rule(
            "weight_based", {"mg_per_kg": 2.0}, {"weight_kg": [50, 100]}
        )
        for _ in range(20):
            drill = generate_dosing_drill(rule)
            assert 50.0 <= drill["given"]["weight_kg"] <= 100.0


# ---------------------------------------------------------------------------
# 4. seed_dosing_rules — loads the starter set
# ---------------------------------------------------------------------------

class TestSeedDosingRules:
    def test_seed_loads_all_rules(self):
        from src.dosing_engine import seed_dosing_rules
        from src.student_model import conn
        n = seed_dosing_rules(DOSING_RULES_PATH)
        data = json.loads(Path(DOSING_RULES_PATH).read_text(encoding="utf-8"))
        assert n == len(data), f"Expected {len(data)} rules, got {n}"
        with conn() as db:
            count = db.execute("SELECT COUNT(*) FROM dosing_rules").fetchone()[0]
        assert count == len(data)

    def test_seed_idempotent(self):
        from src.dosing_engine import seed_dosing_rules
        n1 = seed_dosing_rules(DOSING_RULES_PATH)
        n2 = seed_dosing_rules(DOSING_RULES_PATH)
        assert n1 == n2

    def test_rules_have_required_fields(self):
        from src.dosing_engine import seed_dosing_rules
        from src.student_model import conn
        seed_dosing_rules(DOSING_RULES_PATH)
        with conn() as db:
            rows = db.execute(
                "SELECT id, drug, calc_type, source FROM dosing_rules"
            ).fetchall()
        for r in rows:
            assert r["id"], "id must not be blank"
            assert r["drug"], "drug must not be blank"
            assert r["calc_type"], "calc_type must not be blank"
            assert r["source"], "source must not be blank"

    def test_all_calc_types_valid(self):
        from src.dosing_engine import seed_dosing_rules, VALID_CALC_TYPES
        from src.student_model import conn
        seed_dosing_rules(DOSING_RULES_PATH)
        with conn() as db:
            rows = db.execute("SELECT id, calc_type FROM dosing_rules").fetchall()
        for r in rows:
            assert r["calc_type"] in VALID_CALC_TYPES, (
                f"Rule '{r['id']}' has invalid calc_type '{r['calc_type']}'"
            )

    def test_anesthesia_and_medicine_rules_present(self):
        from src.dosing_engine import seed_dosing_rules
        from src.student_model import conn
        seed_dosing_rules(DOSING_RULES_PATH)
        with conn() as db:
            anes = db.execute(
                "SELECT COUNT(*) FROM dosing_rules WHERE discipline='anesthesia'"
            ).fetchone()[0]
            med = db.execute(
                "SELECT COUNT(*) FROM dosing_rules WHERE discipline='medicine'"
            ).fetchone()[0]
        assert anes >= 5, f"Expected ≥5 anesthesia rules, got {anes}"
        assert med >= 5, f"Expected ≥5 medicine rules, got {med}"

    def test_critical_care_rules_present(self):
        from src.dosing_engine import seed_dosing_rules
        from src.student_model import conn
        seed_dosing_rules(DOSING_RULES_PATH)
        with conn() as db:
            cc = db.execute(
                "SELECT COUNT(*) FROM dosing_rules WHERE is_critical_care=1"
            ).fetchone()[0]
        assert cc >= 10, f"Expected ≥10 critical-care rules, got {cc}"

    def test_every_seeded_rule_can_generate_a_drill(self):
        """Each non-recall_only rule in the starter set must run end-to-end without errors.
        recall_only rules are expected to raise TypeError — they use generate_recall_drill().
        """
        from src.dosing_engine import (
            seed_dosing_rules, get_all_rules, generate_dosing_drill,
            generate_recall_drill, RECALL_ONLY_TYPE,
        )
        seed_dosing_rules(DOSING_RULES_PATH)
        rules = get_all_rules()
        assert rules, "No rules loaded"
        errors = []
        for rule in rules:
            is_recall_only = bool(rule.get("recall_only")) or rule.get("calc_type") == RECALL_ONLY_TYPE
            try:
                if is_recall_only:
                    drill = generate_recall_drill(rule)
                    assert isinstance(drill["answer"], str) and drill["answer"]
                else:
                    drill = generate_dosing_drill(rule)
                    assert isinstance(drill["answer"], float) and math.isfinite(drill["answer"])
            except Exception as e:
                errors.append(f"{rule['id']}: {e}")
        assert not errors, "Drill generation failed for:\n" + "\n".join(errors)


# ---------------------------------------------------------------------------
# 5. get_dosing_drill MCP tool
# ---------------------------------------------------------------------------

class TestGetDosingDrillTool:
    def setup_method(self):
        from src.dosing_engine import seed_dosing_rules
        seed_dosing_rules(DOSING_RULES_PATH)

    def test_returns_valid_drill(self):
        """mode='calculation' must return a numeric calc drill."""
        from src.mcp_server import get_dosing_drill
        drill = get_dosing_drill(mode="calculation")
        assert "scenario_text" in drill, f"Expected scenario_text in calc drill: {list(drill.keys())}"
        assert "answer" in drill
        assert "worked_steps" in drill
        assert isinstance(drill["answer"], float)

    def test_auto_mode_returns_a_drill(self):
        """mode='auto' (default) must return either a recall or calc drill without error."""
        from src.mcp_server import get_dosing_drill
        drill = get_dosing_drill()
        assert "error" not in drill
        assert "answer" in drill

    def test_filter_by_discipline_anesthesia(self):
        from src.mcp_server import get_dosing_drill
        for _ in range(10):
            drill = get_dosing_drill(discipline="anesthesia")
            assert "error" not in drill

    def test_filter_by_discipline_medicine(self):
        from src.mcp_server import get_dosing_drill
        for _ in range(10):
            drill = get_dosing_drill(discipline="medicine")
            assert "error" not in drill

    def test_filter_by_drug_succinylcholine(self):
        from src.mcp_server import get_dosing_drill
        # Succinylcholine is tier-2 with no recall KP mastered → auto returns recall
        drill = get_dosing_drill(drug="Succinylcholine")
        assert "error" not in drill
        assert "Succinylcholine" in drill["drug"]

    def test_no_matching_rules_returns_error(self):
        from src.mcp_server import get_dosing_drill
        result = get_dosing_drill(drug="NoSuchDrug12345")
        assert "error" in result

    def test_drill_answer_numeric_and_finite(self):
        """Calculation drills must have a finite numeric answer."""
        from src.mcp_server import get_dosing_drill
        for _ in range(5):
            drill = get_dosing_drill(mode="calculation")
            assert math.isfinite(drill["answer"]), "Answer must be finite"
            assert drill["answer"] > 0, "Positive dosing answer expected"

    def test_scenario_text_is_string(self):
        """Calculation drills must have scenario_text."""
        from src.mcp_server import get_dosing_drill
        drill = get_dosing_drill(mode="calculation")
        assert isinstance(drill["scenario_text"], str) and drill["scenario_text"]

    def test_tolerance_in_drill(self):
        """Calculation drills must have tolerance."""
        from src.mcp_server import get_dosing_drill
        drill = get_dosing_drill(mode="calculation")
        assert 0 < drill["tolerance"] <= 0.15


# ---------------------------------------------------------------------------
# 6. submit_dosing_answer — creates FSRS-schedulable knowledge point
# ---------------------------------------------------------------------------

class TestSubmitDosingAnswer:
    def test_correct_answer_creates_knowledge_point(self):
        from src.mcp_server import submit_dosing_answer
        from src.student_model import get_knowledge_points
        # mode='recall' → point key is 'dosing-recall:{drug}'
        result = submit_dosing_answer(
            drug="Norepinephrine",
            is_correct=True,
            confidence=4,
            calc_type="infusion_rate",
            mode="recall",
        )
        assert result["ok"] is True
        pts = get_knowledge_points(topic="Norepinephrine")
        assert len(pts) == 1
        assert pts[0]["point"] == "dosing-recall:Norepinephrine"
        assert pts[0]["mistake_type"] == "drug_dosing"

    def test_correct_calc_answer_creates_calc_knowledge_point(self):
        from src.mcp_server import submit_dosing_answer
        from src.student_model import get_knowledge_points
        # mode='calculation' → point key is 'dosing-calc:{drug}' — keyed on the
        # drug alone, so history can't split across with/without-calc_type keys.
        result = submit_dosing_answer(
            drug="Norepinephrine",
            is_correct=True,
            confidence=4,
            calc_type="infusion_rate",
            mode="calculation",
        )
        assert result["ok"] is True
        pts = get_knowledge_points(topic="Norepinephrine")
        assert any(p["point"] == "dosing-calc:Norepinephrine" for p in pts)
        assert pts[0]["mistake_type"] == "drug_dosing"

    def test_incorrect_answer_is_weak(self):
        from src.mcp_server import submit_dosing_answer
        from src.student_model import get_knowledge_points
        submit_dosing_answer(
            drug="Succinylcholine",
            is_correct=False,
            confidence=2,
            calc_type="weight_based",
        )
        pts = get_knowledge_points(topic="Succinylcholine")
        assert pts[0]["status"] == "weak"

    def test_two_correct_graduates_to_mastered(self):
        from src.mcp_server import submit_dosing_answer
        from src.student_model import get_knowledge_points
        submit_dosing_answer("Propofol", True, 4, "weight_based")
        submit_dosing_answer("Propofol", True, 5, "weight_based")
        pts = get_knowledge_points(topic="Propofol")
        assert pts[0]["status"] == "mastered"

    def test_knowledge_point_has_fsrs_state(self):
        from src.mcp_server import submit_dosing_answer
        from src.student_model import get_knowledge_points
        submit_dosing_answer("Vancomycin", True, 3, "weight_based")
        pts = get_knowledge_points(topic="Vancomycin")
        assert pts[0].get("fsrs_state"), "FSRS state should be persisted"

    def test_creates_dueable_knowledge_point(self):
        """After incorrect answer the knowledge point is created with status 'weak'.
        Force the review date into the past to verify it surfaces in the due queue."""
        from src.mcp_server import submit_dosing_answer
        from src.student_model import get_due_knowledge_points, conn
        submit_dosing_answer("Dantrolene", False, 3, "weight_based", mode="recall")
        # FSRS schedules a first miss for tomorrow by design; push the date back to
        # simulate a lapsed card (same pattern used in test_curriculum_coverage.py).
        with conn() as db:
            db.execute(
                "UPDATE knowledge_points SET next_review_date='2000-01-01' "
                "WHERE point LIKE 'dosing-%:Dantrolene%'"
            )
        due = get_due_knowledge_points(limit=50)
        assert any("Dantrolene" in p["point"] for p in due), (
            "Missed dosing drill should appear in due knowledge points after date override"
        )

    def test_blank_drug_returns_error(self):
        from src.mcp_server import submit_dosing_answer
        result = submit_dosing_answer("", True, 3, "weight_based")
        assert result["ok"] is False

    def test_mistake_type_is_drug_dosing(self):
        from src.mcp_server import submit_dosing_answer
        from src.student_model import conn
        submit_dosing_answer("Magnesium", True, 3, "mass_to_volume")
        with conn() as db:
            row = db.execute(
                "SELECT mistake_type FROM knowledge_points WHERE topic='Magnesium'"
            ).fetchone()
        assert row is not None
        assert row["mistake_type"] == "drug_dosing"


# ---------------------------------------------------------------------------
# 7. get_due_dosing_drills — filters to dosing knowledge points only
# ---------------------------------------------------------------------------

class TestGetDueDosingDrills:
    def test_empty_when_no_dosing_points(self):
        from src.mcp_server import get_due_dosing_drills
        from src.student_model import record_knowledge_point
        # Record a non-dosing knowledge point — should not appear
        record_knowledge_point("PE", "massive PE: tPA", is_correct=False, confidence=3)
        result = get_due_dosing_drills()
        assert result["count"] == 0
        assert result["due_dosing_points"] == []

    def test_incorrect_dosing_answer_appears_in_due(self):
        from src.mcp_server import submit_dosing_answer, get_due_dosing_drills
        from src.student_model import conn
        submit_dosing_answer("Lidocaine", False, 2, "max_dose", mode="recall")
        # Push the review date back to simulate a lapsed card
        with conn() as db:
            db.execute(
                "UPDATE knowledge_points SET next_review_date='2000-01-01' "
                "WHERE point LIKE 'dosing-%:Lidocaine%'"
            )
        result = get_due_dosing_drills()
        assert result["count"] >= 1
        assert any("Lidocaine" in p["point"] for p in result["due_dosing_points"])

    def test_mastered_dosing_not_due(self):
        from src.mcp_server import submit_dosing_answer, get_due_dosing_drills
        # Master it with two corrects
        submit_dosing_answer("Bupivacaine", True, 5, "max_dose")
        submit_dosing_answer("Bupivacaine", True, 5, "max_dose")
        result = get_due_dosing_drills()
        assert not any("dosing:Bupivacaine" in p["point"] for p in result["due_dosing_points"])

    def test_non_dosing_points_excluded(self):
        from src.mcp_server import submit_dosing_answer, get_due_dosing_drills
        from src.student_model import record_knowledge_point
        # Add a non-dosing weak point
        record_knowledge_point("ARDS", "low TV 6 mL/kg IBW", is_correct=False, confidence=3)
        # Add a dosing weak point
        submit_dosing_answer("Heparin", False, 2, "weight_based")
        result = get_due_dosing_drills()
        for p in result["due_dosing_points"]:
            assert p["point"].startswith("dosing:"), (
                f"Non-dosing point leaked: {p['point']}"
            )


# ---------------------------------------------------------------------------
# 8. generate_recall_drill — recall layer
# ---------------------------------------------------------------------------

class TestGenerateRecallDrill:
    def _make_recall_rule(self, drug="Ondansetron"):
        return {
            "id": "test_recall",
            "drug": drug,
            "context": "nausea",
            "calc_type": "recall_only",
            "params_json": {},
            "randomize_json": {},
            "units": "mg",
            "tier": 1,
            "source": "UpToDate",
            "explanation": "Ondansetron 4 mg IV q6–8h.",
            "dose_fact": "Ondansetron: 4 mg IV/PO q6–8h",
            "recall_question": "What is the standard antiemetic dose of ondansetron?",
            "anchor": "Zofran = 4 mg. Watch QTc.",
            "recall_only": True,
        }

    def test_recall_drill_structure(self):
        from src.dosing_engine import generate_recall_drill
        rule = self._make_recall_rule()
        drill = generate_recall_drill(rule)
        required = {"drug", "mode", "question", "answer", "anchor", "source", "explanation"}
        assert required <= drill.keys(), f"Missing keys: {required - drill.keys()}"

    def test_recall_mode_field(self):
        from src.dosing_engine import generate_recall_drill
        rule = self._make_recall_rule()
        drill = generate_recall_drill(rule)
        assert drill["mode"] == "recall"

    def test_anchor_present_and_non_empty(self):
        from src.dosing_engine import generate_recall_drill
        rule = self._make_recall_rule()
        drill = generate_recall_drill(rule)
        assert drill["anchor"], "Anchor must be present and non-empty"
        assert "QTc" in drill["anchor"]

    def test_question_and_answer_from_rule(self):
        from src.dosing_engine import generate_recall_drill
        rule = self._make_recall_rule()
        drill = generate_recall_drill(rule)
        assert "ondansetron" in drill["question"].lower()
        assert "4 mg" in drill["answer"]

    def test_compute_answer_raises_for_recall_only(self):
        """compute_answer should raise TypeError for recall_only rules."""
        from src.dosing_engine import compute_answer
        rule = {"id": "x", "drug": "Zofran", "calc_type": "recall_only", "params_json": {}}
        with pytest.raises(TypeError, match="recall_only"):
            compute_answer(rule, {})

    def test_generate_dosing_drill_raises_for_recall_only(self):
        """generate_dosing_drill should raise TypeError for recall_only rules."""
        from src.dosing_engine import generate_dosing_drill
        rule = self._make_recall_rule()
        with pytest.raises(TypeError, match="recall_only"):
            generate_dosing_drill(rule)

    def test_recall_drill_from_real_rule(self):
        """Real recall_only rules in dosing_rules.json produce valid recall drills."""
        from src.dosing_engine import seed_dosing_rules, get_all_rules, generate_recall_drill
        seed_dosing_rules(DOSING_RULES_PATH)
        rules = get_all_rules()
        recall_only_rules = [r for r in rules if r.get("recall_only")]
        assert recall_only_rules, "Expected at least one recall_only rule in the dataset"
        for rule in recall_only_rules[:5]:  # spot-check first 5
            drill = generate_recall_drill(rule)
            assert drill["mode"] == "recall"
            assert drill["anchor"], f"Missing anchor for {rule['drug']}"
            assert drill["answer"], f"Missing dose_fact for {rule['drug']}"


# ---------------------------------------------------------------------------
# 9. Tier ordering and everyday ward set
# ---------------------------------------------------------------------------

class TestTierOrdering:
    def setup_method(self):
        from src.dosing_engine import seed_dosing_rules
        seed_dosing_rules(DOSING_RULES_PATH)

    def test_tier1_rules_exist(self):
        from src.dosing_engine import get_all_rules
        from src.student_model import conn
        with conn() as db:
            count = db.execute("SELECT COUNT(*) FROM dosing_rules WHERE tier=1").fetchone()[0]
        assert count >= 20, f"Expected ≥20 tier-1 everyday rules, got {count}"

    def test_get_all_rules_tier1_first(self):
        """get_all_rules() without filter returns tier-1 before tier-2."""
        from src.dosing_engine import get_all_rules
        rules = get_all_rules()
        tiers = [r.get("tier", 2) for r in rules]
        # Once a tier-2 appears, no tier-1 should follow
        seen_tier2 = False
        for t in tiers:
            if t == 2:
                seen_tier2 = True
            if seen_tier2 and t == 1:
                assert False, "tier-1 rule appeared after tier-2 in ordered result"

    def test_tier1_contains_everyday_drugs(self):
        from src.dosing_engine import get_all_rules
        tier1_rules = get_all_rules(tier=1)
        tier1_drugs = {r["drug"].lower() for r in tier1_rules}
        must_have = [
            "acetaminophen", "ondansetron", "morphine", "hydromorphone",
            "enoxaparin (dvt prophylaxis)", "vancomycin (weight-based loading dose)",
        ]
        for d in must_have:
            assert any(d in name for name in tier1_drugs), (
                f"Expected tier-1 to contain '{d}', got: {sorted(tier1_drugs)}"
            )

    def test_existing_emergency_rules_are_tier2(self):
        from src.dosing_engine import get_all_rules
        from src.student_model import conn
        # Succinylcholine, dantrolene, epinephrine should be tier 2
        with conn() as db:
            for drug_id in ("succinylcholine_intubation", "dantrolene_mh", "epinephrine_acls_cardiac_arrest"):
                row = db.execute("SELECT tier FROM dosing_rules WHERE id=?", (drug_id,)).fetchone()
                assert row is not None
                assert row["tier"] == 2, f"{drug_id} should be tier 2, got {row['tier']}"

    def test_recall_only_rules_never_in_calc_drill(self):
        """generate_dosing_drill should raise for every recall_only rule in the set."""
        from src.dosing_engine import get_all_rules, generate_dosing_drill, RECALL_ONLY_TYPE
        rules = get_all_rules()
        recall_only = [r for r in rules if r.get("recall_only") or r.get("calc_type") == RECALL_ONLY_TYPE]
        for rule in recall_only:
            with pytest.raises(TypeError):
                generate_dosing_drill(rule)


# ---------------------------------------------------------------------------
# 10. Auto-mode mastery gating (recall → calculation unlock)
# ---------------------------------------------------------------------------

class TestAutoModeGating:
    def setup_method(self):
        from src.dosing_engine import seed_dosing_rules
        seed_dosing_rules(DOSING_RULES_PATH)

    def test_auto_serves_recall_for_unseen_drug(self):
        """An unseen drug should get a recall drill in auto mode."""
        from src.mcp_server import get_dosing_drill
        # Vancomycin: tier-1, has a calculation. Never submitted = unseen → expect recall.
        drill = get_dosing_drill(drug="Vancomycin", mode="auto")
        assert drill.get("mode") == "recall", (
            f"Expected recall drill for unseen drug, got: {drill.get('mode')} / {drill.get('calc_type')}"
        )

    def test_auto_serves_calculation_after_recall_mastered(self):
        """After two correct recall answers (mastered), auto mode serves calc drill."""
        from src.mcp_server import get_dosing_drill, submit_dosing_answer
        drug = "Vancomycin (weight-based loading dose)"
        # Master the recall KP: two correct answers
        submit_dosing_answer(drug, True, 5, mode="recall")
        submit_dosing_answer(drug, True, 5, mode="recall")
        # Verify recall KP is mastered
        from src.student_model import get_knowledge_points
        pts = get_knowledge_points(topic=drug)
        recall_pts = [p for p in pts if p.get("point") == f"dosing-recall:{drug}"]
        assert recall_pts and recall_pts[0]["status"] == "mastered", (
            f"Expected recall KP mastered after 2 corrects, got: {recall_pts}"
        )
        # Now auto should serve a calc drill
        drill = get_dosing_drill(drug="Vancomycin", mode="auto")
        assert drill.get("mode") != "recall", (
            "Expected calculation drill after recall mastered, still got recall"
        )
        assert "answer" in drill and isinstance(drill["answer"], float), (
            "Calculation drill must have a numeric engine answer"
        )

    def test_recall_only_drug_never_gets_calc_drill_in_auto(self):
        """recall_only drugs should always return recall drill even if KP is mastered."""
        from src.mcp_server import get_dosing_drill, submit_dosing_answer
        drug = "Ondansetron"
        # Master the recall KP
        submit_dosing_answer(drug, True, 5, mode="recall")
        submit_dosing_answer(drug, True, 5, mode="recall")
        # Auto mode should still return recall (no calc exists for recall_only drug)
        drill = get_dosing_drill(drug=drug, mode="auto")
        assert drill.get("mode") == "recall", (
            f"recall_only drug should always return recall drill, got: {drill}"
        )

    def test_submit_recall_creates_correct_kp_key(self):
        from src.mcp_server import submit_dosing_answer
        from src.student_model import get_knowledge_points
        submit_dosing_answer("Morphine", True, 4, mode="recall")
        pts = get_knowledge_points(topic="Morphine")
        points_keys = [p["point"] for p in pts]
        assert "dosing-recall:Morphine" in points_keys, (
            f"Expected 'dosing-recall:Morphine' in {points_keys}"
        )

    def test_submit_calc_creates_correct_kp_key(self):
        from src.mcp_server import submit_dosing_answer
        from src.student_model import get_knowledge_points
        submit_dosing_answer("Enoxaparin (DVT/PE treatment)", True, 4,
                             calc_type="weight_based", mode="calculation")
        pts = get_knowledge_points(topic="Enoxaparin (DVT/PE treatment)")
        points_keys = [p["point"] for p in pts]
        assert any("dosing-calc:" in k for k in points_keys), (
            f"Expected 'dosing-calc:...' key, got: {points_keys}"
        )

    def test_due_drills_catches_recall_prefix(self):
        from src.mcp_server import submit_dosing_answer, get_due_dosing_drills
        from src.student_model import conn
        submit_dosing_answer("Furosemide", False, 2, mode="recall")
        with conn() as db:
            db.execute(
                "UPDATE knowledge_points SET next_review_date='2000-01-01' "
                "WHERE point LIKE 'dosing-recall:%'"
            )
        result = get_due_dosing_drills()
        assert any("dosing-recall:Furosemide" in p["point"] for p in result["due_dosing_points"]), (
            "dosing-recall: prefix should be captured by get_due_dosing_drills"
        )

    def test_due_drills_catches_calc_prefix(self):
        from src.mcp_server import submit_dosing_answer, get_due_dosing_drills
        from src.student_model import conn
        submit_dosing_answer("Vancomycin (weight-based loading dose)", False, 2,
                             calc_type="weight_based", mode="calculation")
        with conn() as db:
            db.execute(
                "UPDATE knowledge_points SET next_review_date='2000-01-01' "
                "WHERE point LIKE 'dosing-calc:%'"
            )
        result = get_due_dosing_drills()
        assert any("dosing-calc:" in p["point"] for p in result["due_dosing_points"]), (
            "dosing-calc: prefix should be captured by get_due_dosing_drills"
        )

    def test_example_recall_drill_enoxaparin(self):
        """Spot-check: enoxaparin prophylaxis recall drill returns expected fields."""
        from src.mcp_server import get_dosing_drill
        drill = get_dosing_drill(drug="Enoxaparin (DVT prophylaxis)", mode="recall")
        assert drill.get("mode") == "recall"
        assert "40" in drill.get("answer", ""), f"Expected '40 mg' in answer: {drill.get('answer')}"
        assert drill.get("anchor"), "Anchor must not be empty"

    def test_example_recall_drill_insulin_hyperkalemia(self):
        """Spot-check: regular insulin hyperkalemia recall drill returns 10 units fact."""
        from src.mcp_server import get_dosing_drill
        drill = get_dosing_drill(drug="Regular insulin (hyperkalemia)", mode="recall")
        assert drill.get("mode") == "recall"
        assert "10" in drill.get("answer", ""), f"Expected '10 units' in answer: {drill.get('answer')}"

    def test_example_recall_drill_kcl_anchor_mentions_mg(self):
        """Spot-check: KCl repletion recall drill anchor mentions magnesium."""
        from src.mcp_server import get_dosing_drill
        drill = get_dosing_drill(drug="Potassium chloride", mode="recall")
        anchor_lower = drill.get("anchor", "").lower()
        assert "magnesium" in anchor_lower or "mg" in anchor_lower, (
            f"KCl anchor should mention magnesium: {drill.get('anchor')}"
        )
