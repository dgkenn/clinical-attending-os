"""Fill the measured ICU catalog gaps from free, citable sources.

A concept-by-concept probe of the corpus found four things the catalog could not
teach. Correcting an earlier error of mine first: I reported that APRV "appears
nowhere in the corpus". That was wrong — I had probed only the Marino file and
the two ICU domains. APRV is present in Morgan & Mikhail, and the real gap was
in the EXTRACTED catalog, not the source material. Two of the four items below
are therefore grounded in the existing corpus and needed no new source at all.

Where the corpus genuinely had nothing, the source is free and citable, and the
URL is stored with the fact so any number here can be checked:

  - StatPearls (NCBI Bookshelf) — already a source family in this corpus, so no
    new licensing question. Supplies the concrete APRV settings, which Morgan &
    Mikhail describes only qualitatively.
  - PubMed Central open-access systematic reviews — for peri-intubation arrest
    (corpus hits: ZERO) and awake proning (corpus hits: TWO, both incidental
    COVID-era mentions).

Every number below is quoted from the retrieved source, not written from model
training. Effect sizes carry their confidence intervals because a resident
should see how firm a finding is, and mortality-neutral results are stated as
mortality-neutral rather than quietly dropped.

    python scripts/add_gapfill_facts.py --dry-run
    python scripts/add_gapfill_facts.py
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

DOMAIN = "Internal medicine: ICU & critical care"

SP_VENT = ("StatPearls: Mechanical Ventilation (NCBI Bookshelf NBK539742) — "
           "https://www.ncbi.nlm.nih.gov/books/NBK539742/")
MM = "Morgan & Mikhail's Clinical Anesthesiology, ch. 58 (in corpus)"
MILLER = "Miller's Basics of Anesthesia 8e, ch. 41 Critical Care Medicine (in corpus)"
PICA = ("Risk factors for peri-intubation cardiac arrest: systematic review and "
        "meta-analysis (PMC11220532) — https://pmc.ncbi.nlm.nih.gov/articles/PMC11220532/")
APP = ("Awake prone positioning for non-intubated COVID-19 acute hypoxaemic "
       "respiratory failure: systematic review and meta-analysis (PMC8926412) — "
       "https://pmc.ncbi.nlm.nih.gov/articles/PMC8926412/")

FACTS: list[dict] = [
    # ---------------- APRV ----------------
    {"topic": "Airway Pressure Release Ventilation (APRV)", "source": SP_VENT,
     "stem": "What are the four APRV settings and their usual starting values?",
     "answer": "P-high (the CPAP level) typically 27-29 cm H2O, set off the measured "
               "plateau pressure — obese patients may need higher. P-low usually 0, "
               "because intrinsic PEEP prevents full exhalation anyway. T-high (time at "
               "P-high) 4-6 seconds. T-low (the release) 0.2-0.8 s in restrictive lung "
               "disease and 0.8-1.5 s in obstructive disease.",
     "rationale": "T-low is the setting that differs by pathology: obstructive lungs need "
                  "longer to empty, and too short a release is how you stack breaths.",
     "bloom": "apply"},
    {"topic": "Airway Pressure Release Ventilation (APRV)", "source": SP_VENT,
     "stem": "What is APRV actually doing physiologically, and why might it need less sedation?",
     "answer": "It holds a sustained high airway pressure with brief timed releases, so the "
               "lung sits recruited and is not put through repeated recruitment-"
               "derecruitment cycles. The patient breathes spontaneously throughout, at "
               "both pressure levels, which needs less sedation than conventional modes and "
               "improves hemodynamics — spontaneous effort lowers intrathoracic pressure, "
               "raising preload and cardiac output.",
     "rationale": "The hemodynamic argument is the counterintuitive part: a high-mean-"
                  "pressure mode can improve cardiac output because the diaphragm is "
                  "still working.",
     "bloom": "understand"},
    {"topic": "Airway Pressure Release Ventilation (APRV)", "source": MM,
     "stem": "How does APRV differ from inverse-ratio ventilation, and why does that matter "
             "for sedation?",
     "answer": "Both raise mean airway pressure, but IRV does NOT allow spontaneous "
               "breathing and so requires heavy sedation or neuromuscular blockade. APRV "
               "permits spontaneous breathing at both pressure levels. In IRV the "
               "prolonged inspiratory time generates intrinsic PEEP from air trapping, "
               "raising FRC until a new equilibrium is reached.",
     "rationale": "The contrast is the point — 'high mean airway pressure' alone does not "
                  "tell you whether the patient can breathe or must be paralysed.",
     "bloom": "analyze"},
    # ---------------- Peri-intubation arrest ----------------
    {"topic": "Peri-Intubation Hypotension and Cardiac Arrest", "source": PICA,
     "stem": "How often does cardiac arrest occur around emergency intubation, and what are "
             "the two dominant risk factors?",
     "answer": "Pooled incidence 2.1% (95% CI 1.5-3.0%) across 28,963 patients. "
               "Pre-intubation HYPOTENSION is the strongest: pooled OR 4.96 (95% CI "
               "3.75-6.57), threshold SBP under 90 mmHg. Pre-intubation HYPOXEMIA: pooled "
               "OR 4.43 (95% CI 1.24-15.81), threshold SpO2 under 90% on room air.",
     "rationale": "Both risks are present and modifiable BEFORE the drugs go in, which is "
                  "the whole clinical point.",
     "bloom": "remember"},
    {"topic": "Peri-Intubation Hypotension and Cardiac Arrest", "source": PICA,
     "stem": "A hypotensive hypoxic patient needs intubation. What do you do before pushing "
             "induction drugs, and does the paralytic choice matter?",
     "answer": "Resuscitate first: correct the hypotension and improve oxygenation before "
               "induction, and plan the airway to minimise attempts — two or more attempts "
               "carries OR 1.88 (95% CI 1.09-3.23) for arrest. Succinylcholine was NOT a "
               "significant risk factor (OR 1.69, 95% CI 0.93-3.26), so the paralytic is "
               "not the lever; the haemodynamics are.",
     "rationale": "Trainees reach for a different drug when the actual intervention is "
                  "fixing the blood pressure and getting it right first pass.",
     "bloom": "apply"},
    # ---------------- Awake proning ----------------
    {"topic": "Awake Prone Positioning", "source": APP,
     "stem": "Does awake proning help a non-intubated hypoxaemic patient, and does it save lives?",
     "answer": "It reduces intubation — RR 0.84 (95% CI 0.72-0.97) across 10 RCTs — but has "
               "NO mortality benefit: RR 1.00 (95% CI 0.70-1.44). Adverse events are mild "
               "(skin breakdown, line dislodgement, vomiting, back pain, discomfort) with "
               "no serious events reported.",
     "rationale": "Intubation-sparing without a mortality signal is exactly the kind of "
                  "result that gets overstated on rounds.",
     "bloom": "evaluate"},
    {"topic": "Awake Prone Positioning", "source": APP,
     "stem": "Which patients actually benefit from awake proning, and how long do they need "
             "to stay prone?",
     "answer": "Benefit is confined to patients already on ADVANCED respiratory support "
               "(HFNC or NIV): RR 0.83 (95% CI 0.71-0.97), and to ICU settings: RR 0.83 "
               "(0.71-0.97). On conventional oxygen it did not help (RR 0.87, 0.45-1.69), "
               "nor on general wards (RR 0.88, 0.44-1.76). Longer daily duration is "
               "associated with success; trial durations ranged 1-16 hours and no threshold "
               "is established.",
     "rationale": "Stops it being applied to the wrong patient — a ward patient on nasal "
                  "cannula is the group where it did nothing.",
     "bloom": "analyze"},
    # ---------------- A-F bundle / SAT ----------------
    {"topic": "ICU Sedation: Spontaneous Awakening Trials", "source": MILLER,
     "stem": "Run a spontaneous awakening trial: what do you do, what do you assess with, "
             "and what are the contraindications?",
     "answer": "Pause continuous sedative infusions and assess pain and agitation with a "
               "validated scale such as RASS. If the patient stays calm, do NOT restart "
               "sedation — treat pain instead. If they become agitated, restart at the "
               "lowest dose that achieves a calm, cooperative patient. Contraindications: "
               "neuromuscular blockade, alcohol withdrawal, seizures, and raised "
               "intracranial pressure.",
     "rationale": "The default failure is restarting the drip at the old rate the moment "
                  "the patient stirs, which undoes the trial.",
     "bloom": "apply"},
    # ---------------- Vasopressor weaning ----------------
    {"topic": "Vasopressor Weaning", "source": "Curated critical-care unit notes (in corpus)",
     "stem": "When and how do you start weaning vasopressors, and what is the trade-off?",
     "answer": "Generally once MAP has held at goal (65 mmHg) without escalation for 6-12 "
               "hours. Reduce the infusion by 10-20% every 4-6 hours while watching blood "
               "pressure, lactate and perfusion markers. The trade-off: prolonged "
               "vasopressor use (over 7 days) carries a worse prognosis, but weaning too "
               "early causes hypotensive relapse. Keep optimising volume status and source "
               "control, which is what actually makes weaning possible.",
     "rationale": "Names the catch-22 explicitly rather than implying there is a single "
                  "correct moment to start.",
     "bloom": "evaluate"},
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
        kid = f"gapfill-{i:02d}"
        if db.execute("SELECT 1 FROM kp_catalog WHERE id=? OR stem=?",
                      (kid, f["stem"])).fetchone():
            skipped += 1
            print(f"  skip  {f['stem'][:70]}")
            continue
        added += 1
        print(f"  add   [{f['topic'][:38]:<38}] {f['stem'][:48]}")
        if args.dry_run:
            continue
        db.execute(
            """INSERT INTO kp_catalog
                   (id, topic, domain, discipline, stem, answer, rationale, bloom,
                    source, confusable_with, tier, category, is_critical_care,
                    car_safe, added_at, times_seen, verified, volatility,
                    last_currency_check)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (kid, f["topic"], DOMAIN, "medicine", f["stem"], f["answer"],
             f["rationale"], f["bloom"], json.dumps([f["source"]]), "", 1, "topic",
             1, 0, now, 0, 1, "high", now))
    if args.dry_run:
        print(f"\ndry run — would add {added}, skip {skipped}")
        return
    db.commit()
    total = db.execute("SELECT COUNT(*) FROM kp_catalog").fetchone()[0]
    icu = db.execute("SELECT COUNT(*) FROM kp_catalog WHERE is_critical_care=1").fetchone()[0]
    print(f"\nadded {added}, skipped {skipped}; catalog now {total} ({icu} critical-care)")
    db.close()


if __name__ == "__main__":
    main()
