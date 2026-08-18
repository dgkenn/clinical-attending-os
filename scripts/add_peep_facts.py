"""Fill the PEEP-titration hole in the ICU catalog, grounded in Marino.

A probe of the ICU domains for bread-and-butter critical-care concepts found
PEEP titration / recruitment scoring ZERO facts anywhere in a 6,299-item
catalog — while the corpus holds 72 Marino chunks on driving and plateau
pressure. The gap was extraction, not acquisition.

Every fact below is taken from retrieved passages of "The Little ICU Book"
(Paul Marino), the maintainer's stated preferred ICU source. Nothing here is
written from model training: the numbers, the increments and the thresholds all
appear verbatim in the retrieved text. That constraint is the whole point —
questions built from training look clinically sound, cite nothing, and fail
invisibly, which is why grounding is the project's cardinal rule.

APRV was the other measured hole and is deliberately NOT filled here. Marino's
modes chapter covers assist-control, IMV and CPAP but never mentions airway
pressure release ventilation, and the concept appears nowhere else in the
corpus either. Authoring it would mean inventing content from training and
labelling it as sourced. It is reported as an outstanding corpus gap instead.

    python scripts/add_peep_facts.py --dry-run
    python scripts/add_peep_facts.py
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.config import settings  # noqa: E402

TOPIC = "Lung-Protective Ventilation: PEEP & Plateau Pressure"
DOMAIN = "Internal medicine: ICU & critical care"
SOURCE = "The Little ICU Book - Paul Marino"

FACTS: list[dict[str, str]] = [
    {
        "stem": "During low-tidal-volume ventilation for ARDS, what PEEP do you start at, "
                "and does going higher protect against airway collapse?",
        "answer": "Start at 5-7 cm H2O. Higher PEEP gives NO added benefit for preventing "
                  "end-expiratory airway collapse — higher levels are used for a different "
                  "reason, to bring the FiO2 down to a safe range.",
        "rationale": "Separates the two distinct reasons PEEP gets raised. Confusing them is "
                     "why 'just add PEEP' is a common wrong answer for improving outcomes.",
        "bloom": "understand",
    },
    {
        "stem": "You need an FiO2 above 60% to keep SaO2 at or above 90%. What do you do with "
                "PEEP, and in what increments?",
        "answer": "Add PEEP in increments of 2-4 cm H2O until the FiO2 can be reduced below "
                  "60%. PEEP opens distal airspaces (alveolar recruitment), which improves "
                  "arterial oxygenation and lets you drop the FiO2.",
        "rationale": "The actual titration rule, with the trigger and the step size — this is "
                     "the piece that was missing from the catalog entirely.",
        "bloom": "apply",
    },
    {
        "stem": "What is the plateau pressure target in ARDS, and what do you do if you exceed it?",
        "answer": "Keep plateau pressure under 30 cm H2O. If it is above 30, decrease tidal "
                  "volume in 1 mL/kg steps until either the plateau is under 30 or the tidal "
                  "volume reaches 4 mL/kg.",
        "rationale": "Plateau pressure is the bedside read-out of alveolar overdistension, and "
                     "tidal volume — not PEEP — is the knob you turn to fix it.",
        "bloom": "apply",
    },
    {
        "stem": "How is predicted body weight calculated for setting tidal volume?",
        "answer": "Males: 50 + [2.3 x (height in inches - 60)]. Females: 45.5 + [2.3 x (height "
                  "in inches - 60)]. It is driven by height and sex, never by actual weight.",
        "rationale": "The teach-back on ideal-vs-actual body weight was answered by parroting; "
                     "the formula itself is the testable version of that concept.",
        "bloom": "remember",
    },
    {
        "stem": "Walk through the initial ventilator settings for starting low-volume ventilation.",
        "answer": "Assist-control mode with NO ventilator sighs; tidal volume 8 mL/kg predicted "
                  "body weight; respiratory rate 12-14; PEEP 5-7 cm H2O; FiO2 100%. Then reduce "
                  "tidal volume by 1 mL/kg every 2 hours until it reaches 6 mL/kg.",
        "rationale": "The full initiation protocol, including the stepwise wean to 6 mL/kg that "
                     "is usually omitted when people quote '6 mL/kg' as a starting number.",
        "bloom": "apply",
    },
    {
        "stem": "Low-volume ventilation has produced a respiratory acidosis. How do you respond "
                "at pH 7.15-7.30, and below 7.15?",
        "answer": "For pH 7.15-7.30, increase the respiratory rate until pH is above 7.30 or the "
                  "rate reaches 35 breaths/min. For pH below 7.15, go to a rate of 35.",
        "rationale": "Permissive hypercapnia has explicit limits; knowing where they are is what "
                     "stops you abandoning lung-protective settings too early.",
        "bloom": "apply",
    },
    {
        "stem": "A patient on PEEP has a CVP and wedge pressure that look high. Why might those "
                "numbers be wrong, and what do you do about it?",
        "answer": "Filling pressures recorded at end-expiration are falsely elevated when PEEP "
                  "is applied. To measure CVP and wedge accurately the patient should be "
                  "disconnected from the ventilator.",
        "rationale": "A classic ICU trap: treating a PEEP artifact as real volume overload and "
                     "diuresing a patient who is not wet.",
        "bloom": "analyze",
    },
    {
        "stem": "What is intrinsic PEEP, what causes it, and why does it matter during CPR?",
        "answer": "Intrinsic (auto-) PEEP is positive end-expiratory pressure from incomplete "
                  "lung emptying during exhalation. Overventilating during CPR — rapid rates and "
                  "large volumes — traps air and generates it, which is counterproductive. "
                  "Recommended CPR rate is 8-10 inflations/min, just enough volume to raise the "
                  "chest, inflation time under one second.",
        "rationale": "Auto-PEEP is the mechanism behind both failed resuscitations and "
                     "uninterpretable filling pressures, and it is invisible unless looked for.",
        "bloom": "understand",
    },
    {
        "stem": "What I:E ratio should you allow, and how does it differ between ARDS and asthma?",
        "answer": "Exhalation should get at least twice the time of inflation — an I:E of 1:2. "
                  "Exhalation is FASTER in noncompliant lungs (ARDS) and SLOWER in obstructive "
                  "airway disease (asthma), so the obstructive patient is the one who traps air.",
        "rationale": "Explains why the asthmatic, not the ARDS patient, is the one who develops "
                     "auto-PEEP and breath-stacking.",
        "bloom": "understand",
    },
]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    db = sqlite3.connect(str(settings.sqlite_db_path))
    db.row_factory = sqlite3.Row
    now = datetime.now(timezone.utc).isoformat()
    added = skipped = 0
    for i, f in enumerate(FACTS, 1):
        kid = f"marino-peep-{i:02d}"
        exists = db.execute(
            "SELECT 1 FROM kp_catalog WHERE id = ? OR stem = ?", (kid, f["stem"])).fetchone()
        if exists:
            skipped += 1
            print(f"  skip (already present)  {f['stem'][:70]}")
            continue
        added += 1
        print(f"  add   {f['stem'][:70]}")
        if args.dry_run:
            continue
        db.execute(
            """INSERT INTO kp_catalog
                   (id, topic, domain, discipline, stem, answer, rationale, bloom,
                    source, confusable_with, tier, category, is_critical_care,
                    car_safe, added_at, times_seen, verified)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (kid, TOPIC, DOMAIN, "medicine", f["stem"], f["answer"], f["rationale"],
             f["bloom"], json.dumps([SOURCE]), "", 1, "topic", 1, 0, now, 0, 1))
    if args.dry_run:
        print(f"\ndry run — would add {added}, skip {skipped}")
        return
    db.commit()
    total = db.execute("SELECT COUNT(*) FROM kp_catalog").fetchone()[0]
    icu = db.execute(
        "SELECT COUNT(*) FROM kp_catalog WHERE is_critical_care = 1").fetchone()[0]
    print(f"\nadded {added}, skipped {skipped}; catalog now {total} ({icu} critical-care)")
    db.close()


if __name__ == "__main__":
    main()
