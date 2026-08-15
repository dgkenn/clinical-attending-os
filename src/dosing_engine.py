"""Deterministic drug-dosing calculation engine.

SAFETY PRINCIPLE: Python computes every numeric answer. The LLM never does the
arithmetic — it poses the scenario and grades the student's number against the
engine's computed answer (within tolerance). This is dosing; arithmetic errors
are unacceptable.

calc_type dispatch is a closed enum — no eval() of arbitrary strings. Add new
calc_types only by extending _HANDLERS below.
"""
from __future__ import annotations

import json
import random
import sqlite3
from pathlib import Path
from typing import Any

from .student_model import conn, initialize_database, now


# ---------------------------------------------------------------------------
# Table definition (called from initialize_database via the module-import path)
# ---------------------------------------------------------------------------

def create_dosing_rules_table(db: sqlite3.Connection) -> None:
    """Create dosing_rules table if absent. Idempotent."""
    db.execute("""
        CREATE TABLE IF NOT EXISTS dosing_rules (
            id TEXT PRIMARY KEY,
            drug TEXT NOT NULL,
            context TEXT NOT NULL,
            calc_type TEXT NOT NULL,
            params_json TEXT NOT NULL,
            randomize_json TEXT NOT NULL,
            units TEXT NOT NULL,
            discipline TEXT DEFAULT '',
            is_critical_care INTEGER DEFAULT 0,
            tier INTEGER DEFAULT 2,
            source TEXT DEFAULT '',
            explanation TEXT DEFAULT '',
            dose_fact TEXT DEFAULT '',
            recall_question TEXT DEFAULT '',
            anchor TEXT DEFAULT '',
            recall_only INTEGER DEFAULT 0,
            created_at TEXT
        )
    """)
    # Migrate: add new columns if the table existed before this version.
    _migrate_dosing_table(db)


def _migrate_dosing_table(db: sqlite3.Connection) -> None:
    """Add new recall-layer columns to an existing dosing_rules table. Idempotent."""
    existing = {row[1] for row in db.execute("PRAGMA table_info(dosing_rules)").fetchall()}
    migrations = [
        ("tier", "INTEGER DEFAULT 2"),
        ("dose_fact", "TEXT DEFAULT ''"),
        ("recall_question", "TEXT DEFAULT ''"),
        ("anchor", "TEXT DEFAULT ''"),
        ("recall_only", "INTEGER DEFAULT 0"),
    ]
    for col, typedef in migrations:
        if col not in existing:
            db.execute(f"ALTER TABLE dosing_rules ADD COLUMN {col} {typedef}")


def ensure_dosing_table() -> None:
    initialize_database()
    with conn() as db:
        create_dosing_rules_table(db)


# ---------------------------------------------------------------------------
# Seeder
# ---------------------------------------------------------------------------

def seed_dosing_rules(path: str) -> int:
    """Load dosing_rules JSON and UPSERT into the dosing_rules table.

    Each entry mirrors the JSON schema in data/dosing_rules.json.
    Returns the number of rows processed. Idempotent — safe to call multiple
    times (ON CONFLICT REPLACE refreshes every field).
    """
    ensure_dosing_table()
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    ts = now()
    count = 0
    with conn() as db:
        for item in data:
            rule_id = str(item.get("id", "")).strip()
            if not rule_id:
                continue
            db.execute(
                """INSERT INTO dosing_rules
                       (id, drug, context, calc_type, params_json, randomize_json,
                        units, discipline, is_critical_care, tier,
                        source, explanation, dose_fact, recall_question, anchor, recall_only,
                        created_at)
                   VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                   ON CONFLICT(id) DO UPDATE SET
                       drug=excluded.drug,
                       context=excluded.context,
                       calc_type=excluded.calc_type,
                       params_json=excluded.params_json,
                       randomize_json=excluded.randomize_json,
                       units=excluded.units,
                       discipline=excluded.discipline,
                       is_critical_care=excluded.is_critical_care,
                       tier=excluded.tier,
                       source=excluded.source,
                       explanation=excluded.explanation,
                       dose_fact=excluded.dose_fact,
                       recall_question=excluded.recall_question,
                       anchor=excluded.anchor,
                       recall_only=excluded.recall_only""",
                (
                    rule_id,
                    str(item.get("drug", "")),
                    str(item.get("context", "")),
                    str(item.get("calc_type", "")),
                    json.dumps(item.get("params_json", {})),
                    json.dumps(item.get("randomize_json", {})),
                    str(item.get("units", "")),
                    str(item.get("discipline", "")),
                    1 if item.get("is_critical_care") else 0,
                    int(item.get("tier", 2)),
                    str(item.get("source", "")),
                    str(item.get("explanation", "")),
                    str(item.get("dose_fact", "")),
                    str(item.get("recall_question", "")),
                    str(item.get("anchor", "")),
                    1 if item.get("recall_only") else 0,
                    ts,
                ),
            )
            count += 1
    return count


# ---------------------------------------------------------------------------
# Calculation handlers — closed dispatch table
# ---------------------------------------------------------------------------

def _round_sig(value: float, sig: int = 4) -> float:
    """Round to sig significant figures (for readable worked steps)."""
    if value == 0:
        return 0.0
    import math
    d = math.ceil(math.log10(abs(value)))
    power = sig - d
    factor = 10 ** power
    return round(value * factor) / factor


def _calc_weight_based(params: dict, inputs: dict) -> tuple[float, list[str]]:
    """total = rate * weight_kg  (mg_per_kg OR units_per_kg OR mL_per_kg)."""
    weight_kg = float(inputs["weight_kg"])

    # Support three rate keys
    if "mg_per_kg" in params and params["mg_per_kg"]:
        rate = float(params["mg_per_kg"])
        rate_label = f"{rate} mg/kg"
        unit_label = "mg"
    elif "units_per_kg" in params:
        rate = float(params["units_per_kg"])
        rate_label = f"{rate} units/kg"
        unit_label = "units"
    elif "mL_per_kg" in params:
        rate = float(params["mL_per_kg"])
        rate_label = f"{rate} mL/kg"
        unit_label = "mL"
    else:
        raise ValueError("weight_based params must have mg_per_kg, units_per_kg, or mL_per_kg")

    total = rate * weight_kg
    steps = [
        f"Formula: total = rate × weight_kg",
        f"  = {rate_label} × {weight_kg} kg",
        f"  = {_round_sig(total)} {unit_label}",
    ]
    return total, steps


def _calc_infusion_rate(params: dict, inputs: dict) -> tuple[float, list[str]]:
    """mL/hr = (dose_mcg_kg_min × weight_kg × 60) / concentration_mcg_mL.

    Also handles units/hr (insulin, vasopressin) where concentration is in units/mL.
    """
    weight_kg = float(inputs["weight_kg"])

    # Insulin / vasopressin: dose in units/kg/hr directly
    if "dose_units_kg_hr" in params:
        dose = float(params["dose_units_kg_hr"])
        rate = dose * weight_kg
        steps = [
            "Formula: rate (units/hr) = dose_units/kg/hr × weight_kg",
            f"  = {dose} units/kg/hr × {weight_kg} kg",
            f"  = {_round_sig(rate)} units/hr",
        ]
        return rate, steps

    # Vasopressin fixed dose (not weight-based). The value is UNITS PER MINUTE
    # (0.04 units/min standard) — the old key name said "_per_hr" while the
    # code multiplied by 60 and printed "units/min", so a future rule storing a
    # true per-hour value would have been graded 60x too high. Accept the old
    # key for backward compatibility.
    _vaso_fixed = params.get("fixed_rate_units_per_min", params.get("fixed_rate_units_per_hr"))
    if _vaso_fixed is not None:
        fixed = float(_vaso_fixed)
        steps = [
            "Vasopressin is a FIXED dose (not weight-based).",
            f"Standard dose: {fixed} units/min = {fixed * 60:.3f} units/hr",
            "Typical concentration: 1 unit/mL → {:.2f} mL/hr".format(fixed * 60),
        ]
        return fixed * 60, steps  # return units/hr for mL/hr at 1 unit/mL

    # Standard mcg/kg/min infusion
    dose_mcg_kg_min = float(inputs["dose_mcg_kg_min"])
    conc_mcg_mL = float(params["concentration_mcg_mL"])

    mL_hr = (dose_mcg_kg_min * weight_kg * 60) / conc_mcg_mL
    steps = [
        "Formula: mL/hr = (dose_mcg/kg/min × weight_kg × 60) / concentration_mcg/mL",
        f"  = ({dose_mcg_kg_min} mcg/kg/min × {weight_kg} kg × 60 min/hr)",
        f"  ÷ {conc_mcg_mL} mcg/mL",
        f"  = {_round_sig(dose_mcg_kg_min * weight_kg * 60)} mcg/hr ÷ {conc_mcg_mL} mcg/mL",
        f"  = {_round_sig(mL_hr)} mL/hr",
    ]
    return mL_hr, steps


def _calc_max_dose(params: dict, inputs: dict) -> tuple[float, list[str]]:
    """Max allowable VOLUME given a percentage-concentration solution.

    Drill: given weight and a vial concentration (% or mg/mL), compute the max
    safe volume before exceeding the mg/kg ceiling.

    max_mg = mg_per_kg * weight_kg
    mL = max_mg / concentration_mg_per_mL
    """
    weight_kg = float(inputs["weight_kg"])
    mg_per_kg = float(params["mg_per_kg"])

    # Concentration can come from randomize_json as a % (e.g. 1.0 %) or from
    # inputs directly if sampled as mg/mL.
    if "concentration_pct" in inputs:
        # % solution → mg/mL: 1% = 10 mg/mL
        conc_pct = float(inputs["concentration_pct"])
        conc_mg_mL = conc_pct * 10.0
        conc_label = f"{conc_pct}% = {conc_mg_mL} mg/mL"
    else:
        conc_mg_mL = float(params["concentration_mg_mL"])
        conc_label = f"{conc_mg_mL} mg/mL"

    max_mg = mg_per_kg * weight_kg
    max_mL = max_mg / conc_mg_mL
    steps = [
        "Step 1 — Max safe dose (mg):",
        f"  max_mg = {mg_per_kg} mg/kg × {weight_kg} kg = {_round_sig(max_mg)} mg",
        "Step 2 — Convert to volume:",
        f"  Concentration: {conc_label}",
        f"  max_mL = {_round_sig(max_mg)} mg ÷ {conc_mg_mL} mg/mL = {_round_sig(max_mL)} mL",
    ]
    return max_mL, steps


def _calc_mass_to_volume(params: dict, inputs: dict) -> tuple[float, list[str]]:
    """mL = dose_mg / concentration_mg_mL (fixed non-weight-based dose)."""
    dose_mg = float(params["dose_mg"])
    conc_mg_mL = float(params["concentration_mg_mL"])
    mL = dose_mg / conc_mg_mL
    steps = [
        "Formula: volume (mL) = dose (mg) / concentration (mg/mL)",
        f"  = {dose_mg} mg ÷ {conc_mg_mL} mg/mL",
        f"  = {_round_sig(mL)} mL",
    ]
    return mL, steps


def _calc_rate_limited_correction(params: dict, inputs: dict) -> tuple[float, list[str]]:
    """Handles two sub-modes:
    1. Hyponatremia Na-correction limit → answer is the max allowable 24h delta.
    2. 4-2-1 maintenance fluids → answer is mL/hr.
    """
    rule = params.get("rule", "")

    if rule == "4-2-1":
        weight_kg = float(inputs["weight_kg"])
        r1 = float(params["rate_first_10kg"])   # 4
        r2 = float(params["rate_next_10kg"])     # 2
        r3 = float(params["rate_above_20kg"])    # 1

        if weight_kg <= 10:
            rate = r1 * weight_kg
            steps = [
                "4-2-1 rule (weight ≤ 10 kg):",
                f"  rate = {r1} mL/kg/hr × {weight_kg} kg = {rate} mL/hr",
            ]
        elif weight_kg <= 20:
            rate = r1 * 10 + r2 * (weight_kg - 10)
            steps = [
                "4-2-1 rule (10 < weight ≤ 20 kg):",
                f"  First 10 kg: {r1} × 10 = {r1 * 10} mL/hr",
                f"  Next {weight_kg - 10} kg: {r2} × {weight_kg - 10} = {r2 * (weight_kg - 10)} mL/hr",
                f"  Total = {rate} mL/hr",
            ]
        else:
            rate = r1 * 10 + r2 * 10 + r3 * (weight_kg - 20)
            steps = [
                "4-2-1 rule (weight > 20 kg):",
                f"  First 10 kg: {r1} × 10 = {r1 * 10} mL/hr",
                f"  Next 10 kg:  {r2} × 10 = {r2 * 10} mL/hr",
                f"  Remaining {weight_kg - 20} kg: {r3} × {weight_kg - 20} = {r3 * (weight_kg - 20)} mL/hr",
                f"  Total = {rate} mL/hr",
            ]
        return rate, steps

    # Hyponatremia correction limit
    max_meq_24h = float(params["max_correction_meq_per_24h"])
    current_na = float(inputs.get("current_na", 120))
    # Answer: maximum Na you can target in 24h = current_na + max_correction
    target_max = current_na + max_meq_24h
    steps = [
        f"Max safe Na correction: {max_meq_24h} mEq/L per 24h (to prevent ODS)",
        f"Current Na: {current_na} mEq/L",
        f"Max allowable Na at 24h: {current_na} + {max_meq_24h} = {target_max} mEq/L",
        "DO NOT EXCEED this target. For symptomatic patients: first raise by 4–6 mEq quickly,",
        "then slow the rate to stay within the 24h ceiling.",
    ]
    return max_meq_24h, steps  # answer is the max delta in mEq/L/24h


def _calc_unit_conversion(params: dict, inputs: dict) -> tuple[float, list[str]]:
    """% solution → mg/mL: 1% = 10 mg/mL."""
    conc_pct = float(inputs.get("concentration_pct", params.get("concentration_pct", 1.0)))
    mg_mL = conc_pct * 10.0
    steps = [
        "Unit conversion: % solution to mg/mL",
        "Rule: 1% = 10 mg/mL",
        f"  {conc_pct}% × 10 = {mg_mL} mg/mL",
    ]
    return mg_mL, steps


# Closed dispatch table — add new handlers here only
_HANDLERS: dict[str, Any] = {
    "weight_based": _calc_weight_based,
    "infusion_rate": _calc_infusion_rate,
    "max_dose": _calc_max_dose,
    "mass_to_volume": _calc_mass_to_volume,
    "rate_limited_correction": _calc_rate_limited_correction,
    "unit_conversion": _calc_unit_conversion,
}

# recall_only rules have no numeric calculation — they are pure dose-fact recall.
# This constant is checked in compute_answer and generate_dosing_drill.
RECALL_ONLY_TYPE: str = "recall_only"

VALID_CALC_TYPES: frozenset[str] = frozenset(_HANDLERS) | {RECALL_ONLY_TYPE}


# ---------------------------------------------------------------------------
# Input sampler
# ---------------------------------------------------------------------------

def _sample_inputs(randomize_json: dict) -> dict:
    """Sample physiologic inputs from the rule's randomize spec.

    Supported specs per key:
      - {"choices": [...]} → random choice from an explicit discrete list.
            Required for 2-option lists: a bare 2-element numeric list is a
            RANGE, which turned bupivacaine's two marketed concentrations
            [0.25, 0.5] into fictional 0.3%/0.4% solutions.
      - [min, max]       → uniform float in range (rounded to 1 decimal)
      - [v1, v2, v3, …]  → random choice from discrete list
    """
    sampled: dict[str, float] = {}
    for key, spec in randomize_json.items():
        if isinstance(spec, dict) and isinstance(spec.get("choices"), list) and spec["choices"]:
            sampled[key] = random.choice(spec["choices"])
            continue
        if not isinstance(spec, list) or len(spec) < 2:
            continue
        if len(spec) == 2 and all(isinstance(v, (int, float)) for v in spec):
            lo, hi = float(spec[0]), float(spec[1])
            # For weight, round to whole kg; others to 1 decimal
            if "weight" in key:
                sampled[key] = float(round(random.uniform(lo, hi)))
            else:
                sampled[key] = round(random.uniform(lo, hi), 1)
        else:
            # Discrete list — pick one
            sampled[key] = random.choice(spec)
    return sampled


# ---------------------------------------------------------------------------
# Drill generator
# ---------------------------------------------------------------------------

def _load_rule_from_db(rule_id: str) -> dict | None:
    ensure_dosing_table()
    with conn() as db:
        row = db.execute(
            "SELECT * FROM dosing_rules WHERE id=?", (rule_id,)
        ).fetchone()
    return dict(row) if row else None


def _rule_dict_from_row(row: Any) -> dict:
    d = dict(row)
    d["params_json"] = json.loads(d["params_json"])
    d["randomize_json"] = json.loads(d["randomize_json"])
    return d


def compute_answer(rule: dict, inputs: dict) -> tuple[float, list[str]]:
    """Dispatch to the correct handler and return (answer, worked_steps).

    Raises ValueError for unknown calc_types (never eval() anything).
    recall_only rules have no numeric calculation — raises TypeError if called.
    """
    calc_type = rule["calc_type"]
    if calc_type == RECALL_ONLY_TYPE:
        raise TypeError(
            f"Rule '{rule.get('id', rule.get('drug', '?'))}' is recall_only — "
            "use generate_recall_drill() instead of compute_answer()."
        )
    if calc_type not in _HANDLERS:
        raise ValueError(
            f"Unknown calc_type '{calc_type}'. Valid types: {sorted(VALID_CALC_TYPES)}"
        )
    params = rule["params_json"] if isinstance(rule["params_json"], dict) else json.loads(rule["params_json"])
    return _HANDLERS[calc_type](params, inputs)


def _build_scenario_text(rule: dict, inputs: dict) -> str:
    """Construct the scenario presented to the student.

    Does NOT reveal the numeric answer — only the clinical context and sampled
    inputs. The tutor reads this, the student computes.
    """
    drug = rule["drug"]
    context = rule["context"]
    calc_type = rule["calc_type"]

    lines = [f"DRUG-DOSING DRILL — {context}"]
    if "weight_kg" in inputs:
        lines.append(f"Patient weight: {inputs['weight_kg']} kg")

    if calc_type == "weight_based":
        lines.append(f"Drug: {drug}")
        lines.append("Calculate the total dose (in the units specified).")

    elif calc_type == "infusion_rate":
        if "dose_mcg_kg_min" in inputs:
            lines.append(f"Drug: {drug}")
            lines.append(f"Ordered rate: {inputs['dose_mcg_kg_min']} mcg/kg/min")
            # Pull concentration from params for context
            params = rule["params_json"] if isinstance(rule["params_json"], dict) else json.loads(rule["params_json"])
            if params.get("concentration_mcg_mL"):
                lines.append(f"Available concentration: {params['concentration_mcg_mL']} mcg/mL")
            lines.append("Calculate the infusion rate in mL/hr.")
        else:
            lines.append(f"Drug: {drug}")
            lines.append("Calculate the infusion rate.")

    elif calc_type == "max_dose":
        params = rule["params_json"] if isinstance(rule["params_json"], dict) else json.loads(rule["params_json"])
        if "concentration_pct" in inputs:
            lines.append(f"Drug: {drug} {inputs['concentration_pct']}% solution")
        elif params.get("concentration_mg_mL"):
            lines.append(f"Drug: {drug} — concentration {params['concentration_mg_mL']} mg/mL")
        else:
            lines.append(f"Drug: {drug}")
        lines.append("What is the MAXIMUM safe volume (mL) you can administer?")

    elif calc_type == "mass_to_volume":
        params = rule["params_json"] if isinstance(rule["params_json"], dict) else json.loads(rule["params_json"])
        lines.append(f"Drug: {drug}")
        lines.append(f"Required dose: {params['dose_mg']} mg")
        lines.append(f"Available concentration: {params['concentration_mg_mL']} mg/mL")
        lines.append("What volume (mL) do you draw up?")

    elif calc_type == "rate_limited_correction":
        params = rule["params_json"] if isinstance(rule["params_json"], dict) else json.loads(rule["params_json"])
        if params.get("rule") == "4-2-1":
            lines.append(f"Calculate the maintenance fluid rate (mL/hr) using the 4-2-1 rule.")
        else:
            if "current_na" in inputs:
                lines.append(f"Current serum sodium: {inputs['current_na']} mEq/L")
            lines.append("What is the MAXIMUM safe Na correction over 24 hours (mEq/L/24h)?")
            lines.append("State the absolute maximum — and why.")

    elif calc_type == "unit_conversion":
        if "concentration_pct" in inputs:
            lines.append(f"Convert: {inputs['concentration_pct']}% solution → mg/mL")

    return "\n".join(lines)


def generate_dosing_drill(rule: dict) -> dict:
    """Generate a fully-computed dosing drill from a rule dict.

    Returns:
        drug: str
        scenario_text: str   — does NOT reveal the answer
        given: dict          — sampled inputs shown to student
        answer: float        — deterministically computed by the engine
        units: str
        tolerance: float     — ±fraction (default 0.05 = ±5%)
        worked_steps: list[str]
        source: str
        explanation: str
        calc_type: str

    Raises TypeError if rule is recall_only (no numeric calculation exists).
    """
    if rule.get("recall_only") or rule.get("calc_type") == RECALL_ONLY_TYPE:
        raise TypeError(
            f"Rule for '{rule.get('drug', '?')}' is recall_only — "
            "use generate_recall_drill() instead."
        )
    params = rule["params_json"] if isinstance(rule["params_json"], dict) else json.loads(rule["params_json"])
    randomize = rule["randomize_json"] if isinstance(rule["randomize_json"], dict) else json.loads(rule["randomize_json"])

    inputs = _sample_inputs(randomize)
    answer, worked_steps = compute_answer({**rule, "params_json": params}, inputs)

    scenario_text = _build_scenario_text({**rule, "params_json": params}, inputs)

    # Tolerance: 5% for most numeric answers; for Na correction the answer is an
    # integer delta so allow ±1 mEq/L absolute (represented as fraction of answer).
    if rule["calc_type"] == "rate_limited_correction" and params.get("rule") != "4-2-1":
        tolerance = 0.10  # ±1 on 10 = 10%
    else:
        tolerance = 0.05  # ±5%

    return {
        "drug": rule["drug"],
        "context": rule.get("context", ""),
        "calc_type": rule["calc_type"],
        "scenario_text": scenario_text,
        "given": inputs,
        "answer": round(answer, 3),
        "units": rule["units"],
        "tolerance": tolerance,
        "worked_steps": worked_steps,
        "source": rule.get("source", ""),
        "explanation": rule.get("explanation", ""),
    }


def generate_recall_drill(rule: dict) -> dict:
    """Generate a RECALL drill (dose memorization) from a rule dict.

    Returns:
        drug: str
        mode: "recall"
        question: str  — the recall_question from the rule
        answer: str    — the dose_fact to memorize (graded by tutor, not engine)
        anchor: str    — memory aid / mnemonic to teach after reveal
        source: str
        explanation: str
        units: str
        context: str

    The tutor asks the question, student tries to state the dose, tutor reveals
    the answer + anchor regardless of correctness, then records via
    submit_dosing_answer(mode='recall').
    """
    dose_fact = str(rule.get("dose_fact") or rule.get("explanation", ""))
    recall_question = str(rule.get("recall_question") or f"What is the dose of {rule['drug']}?")
    anchor = str(rule.get("anchor") or "")

    return {
        "drug": rule["drug"],
        "mode": "recall",
        "context": rule.get("context", ""),
        "question": recall_question,
        "answer": dose_fact,
        "anchor": anchor,
        "units": rule.get("units", ""),
        "source": rule.get("source", ""),
        "explanation": rule.get("explanation", ""),
    }


# ---------------------------------------------------------------------------
# DB query helpers used by MCP tools
# ---------------------------------------------------------------------------

def get_all_rules(
    category: str = "",
    discipline: str = "",
    drug: str = "",
    tier: int | None = None,
    exclude_recall_only: bool = False,
) -> list[dict]:
    """Fetch rules from the DB with optional filters.

    Results are ordered by tier ASC (everyday tier-1 first), then drug name.
    """
    ensure_dosing_table()
    with conn() as db:
        q = "SELECT * FROM dosing_rules WHERE 1=1"
        params: list = []
        if discipline:
            q += " AND discipline=?"
            params.append(discipline)
        if drug:
            q += " AND drug LIKE ?"
            params.append(f"%{drug}%")
        if category:
            # category maps to context (partial match)
            q += " AND context LIKE ?"
            params.append(f"%{category}%")
        if tier is not None:
            q += " AND tier=?"
            params.append(tier)
        if exclude_recall_only:
            q += " AND recall_only=0 AND calc_type != 'recall_only'"
        q += " ORDER BY tier ASC, drug ASC"
        rows = db.execute(q, params).fetchall()
    return [_rule_dict_from_row(r) for r in rows]
