"""Mine The Little ICU Book for the thinnest ICU topics.

Measured gap: the two ICU domains held 346 facts across ~72 topics — about 4.8
per topic, a survey rather than intensivist depth — with septic shock at ONE
fact, ICU nutrition at one, ventilator modes at two. Meanwhile the corpus holds
7,134 Marino chunks. The shortfall was extraction, not acquisition.

DELIBERATELY RESTRICTED TO WHAT DOES NOT AGE. Marino is a mid-2000s text, and a
retrieval probe surfaced it stating "norepinephrine is often used as a
second-line vasopressor behind dopamine", plus intensive insulin at 80-110 and
Rivers-protocol EGDT — all superseded. Physiology, mechanism, bedside approach
and arithmetic do not move; numeric treatment targets and drug-of-choice calls
do. Everything below is the former. Nothing here encodes a therapeutic target
that current guidance has revised, and the separate currency audit covers the
rest of the corpus.

Every fact is drawn from a retrieved Marino passage, not from model training.

    python scripts/add_marino_icu_facts.py --dry-run
    python scripts/add_marino_icu_facts.py
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
SOURCE = "The Little ICU Book - Paul Marino"

FACTS: list[dict[str, str]] = [
    # ---- Liberation from the ventilator (was: 9 facts, all schedule-level) ----
    {"topic": "Weaning and Liberation from Mechanical Ventilation",
     "stem": "What is the rapid shallow breathing index, how is it calculated, "
             "and what threshold predicts a successful wean?",
     "answer": "RSBI = respiratory rate divided by tidal volume in litres (RR/VT), "
               "measured during spontaneous breathing. Below 100/L predicts success; "
               "above 100/L predicts failure. In the original study an RSBI under "
               "105/L gave an 80% success rate.",
     "rationale": "The single most-quoted weaning number, and it is a ratio you can "
                  "compute at the bedside from the ventilator screen.",
     "bloom": "apply"},
    {"topic": "Weaning and Liberation from Mechanical Ventilation",
     "stem": "Run the checklist for who is a candidate for a spontaneous breathing trial.",
     "answer": "Respiratory: PaO2 at least 60 mmHg on FiO2 under 40-50% with PEEP 5-8 "
               "or less, PaCO2 normal or at baseline, able to initiate an inspiratory "
               "effort. Cardiovascular: no myocardial ischemia, HR at or under 140, "
               "BP normal on no or minimal vasopressor. Mental status: arousable or "
               "GCS at least 13. Plus afebrile and no significant electrolyte "
               "abnormalities.",
     "rationale": "Extubation failure is usually a screening failure. This is the "
                  "list you actually run on rounds.",
     "bloom": "apply"},
    {"topic": "Weaning and Liberation from Mechanical Ventilation",
     "stem": "What does a maximum inspiratory pressure (PImax) above -20 cm H2O tell "
             "you about weaning, and what does a better value tell you?",
     "answer": "If PImax is less than -20 cm H2O (i.e. weaker than -20) there is little "
               "or no chance of weaning. But a PImax stronger than -20 does NOT ensure "
               "success — it rules out, it does not rule in.",
     "rationale": "An asymmetric test. Treating a good PImax as a green light is the "
                  "common misreading.",
     "bloom": "understand"},
    {"topic": "Weaning and Liberation from Mechanical Ventilation",
     "stem": "How can a spontaneous breathing trial be conducted, and is one method better?",
     "answer": "Either through the ventilator circuit, or fully disconnected and "
               "breathing from an independent oxygen source via a T-piece. There is no "
               "evidence that either method is superior.",
     "rationale": "Stops the bedside argument about T-piece versus pressure support "
                  "being a decision that matters for outcome.",
     "bloom": "remember"},
    # ---- Renal replacement (was: 4 facts) ----
    {"topic": "Renal Replacement Therapy",
     "stem": "What are the indications for renal replacement therapy in acute renal "
             "failure, and which demand it immediately?",
     "answer": "Indications: uremic encephalopathy, volume overload, and "
               "life-threatening hyperkalemia or metabolic acidosis. Immediate dialysis "
               "is indicated for severe acidemia (pH under 7.1) and for end-organ damage "
               "such as coma or seizures. About 70% of patients with acute renal failure "
               "will require RRT.",
     "rationale": "Separates 'will need dialysis' from 'needs dialysis now', which is "
                  "the actual overnight decision.",
     "bloom": "apply"},
    {"topic": "Renal Replacement Therapy",
     "stem": "Mechanically, how does hemodialysis clear solute, and how is that "
             "different from hemofiltration?",
     "answer": "Hemodialysis removes solute by DIFFUSION across a semipermeable "
               "membrane, driven by a concentration gradient that is maintained by "
               "running blood and dialysate countercurrent. Water removal is passive and "
               "follows the solute. Hemofiltration is the other basic RRT method, using "
               "convection rather than diffusion.",
     "rationale": "Diffusion versus convection is why the two modalities clear different "
                  "size molecules and behave differently hemodynamically.",
     "bloom": "understand"},
    # ---- ICU nutrition (was: 1 fact) ----
    {"topic": "ICU Nutrition: Enteral and Parenteral",
     "stem": "Estimate daily calorie and protein requirements for a critically ill patient.",
     "answer": "kcal/day = 25 x weight in kg. Protein = 1.2 to 1.6 g/kg/day.",
     "rationale": "The arithmetic you need to write or check a tube-feed order.",
     "bloom": "apply"},
    {"topic": "ICU Nutrition: Enteral and Parenteral",
     "stem": "What are the ABSOLUTE contraindications to enteral tube feeding, and "
             "which conditions merely restrict it?",
     "answer": "Absolute: circulatory shock, intestinal ischemia, complete bowel "
               "obstruction, and ileus. Not absolute but full support is unwise: partial "
               "bowel obstruction, severe or unrelenting diarrhea, pancreatitis, and "
               "high-volume (over 500 mL/day) enterocutaneous fistula — limited feeding "
               "is often tolerated, and in pancreatitis feeds can go into the jejunum.",
     "rationale": "Feeding a shocked or ischemic gut is a genuine harm; the rest of the "
                  "list is routinely over-applied to withhold nutrition unnecessarily.",
     "bloom": "analyze"},
    {"topic": "ICU Nutrition: Enteral and Parenteral",
     "stem": "A tube-fed ICU patient develops diarrhea. How do you tell feeding-related "
             "diarrhea from C. difficile?",
     "answer": "Feeding-related diarrhea is osmotic — often from sorbitol in the formula "
               "— and is NOT accompanied by signs of systemic inflammation. Diarrhea with "
               "systemic inflammatory signs should not be written off as feed intolerance; "
               "consider antibiotic-associated colitis including C. difficile.",
     "rationale": "The default assumption is 'the feeds' and that is how C. diff gets "
                  "missed on a tube-fed patient.",
     "bloom": "analyze"},
    # ---- Vasopressor administration (mechanics, not drug choice) ----
    {"topic": "Vasoactive and Inotropic Drug Pharmacology",
     "stem": "How is a norepinephrine infusion started and titrated, and by what route?",
     "answer": "Always through a large central vein, because of its vasoconstrictor "
               "action. Start at 0.2 mcg/kg/min (roughly 10-20 mcg/min in a 70 kg adult) "
               "and titrate up to effect. Usual effective range 0.2 to 1.3 mcg/kg/min; "
               "refractory hypotension may need up to 5 mcg/kg/min.",
     "rationale": "Route and starting dose are the practical facts; the choice of "
                  "norepinephrine as first-line is covered by the sepsis guideline cards.",
     "bloom": "apply"},
    {"topic": "Vasoactive and Inotropic Drug Pharmacology",
     "stem": "When a vasopressor patient develops organ hypoperfusion, what is the "
             "interpretive trap?",
     "answer": "The main adverse effect of norepinephrine is vasoconstriction with organ "
               "hypoperfusion — but whenever a vasoconstrictor is needed to correct "
               "hypotension, it is often impossible to separate adverse DRUG effect from "
               "adverse DISEASE effect.",
     "rationale": "Guards against reflexively blaming the pressor and under-treating "
                  "shock, which is the more common error.",
     "bloom": "evaluate"},
    # ---- Stress ulcer prophylaxis ----
    {"topic": "Preventive Practices in the Critically Ill",
     "stem": "Who gets stress ulcer prophylaxis in the ICU?",
     "answer": "Any one of: mechanical ventilation beyond 48 hours; coagulopathy "
               "(platelets under 50,000, INR over 1.5, or PTT over 2x control); or a "
               "history of gastritis, peptic ulcer disease or prior upper GI bleed. Or "
               "two or more of: hypotension, severe sepsis, severe head injury, "
               "multisystem trauma, renal failure.",
     "rationale": "Prophylaxis is reflexively ordered for everyone; these are the actual "
                  "indications, and acid suppression is not free.",
     "bloom": "apply"},
    {"topic": "Preventive Practices in the Critically Ill",
     "stem": "What is the argument AGAINST routine gastric acid suppression in the ICU?",
     "answer": "Gastric erosions are near-universal within 24 hours of ICU admission but "
               "usually silent — significant bleeding occurs in under 5% of patients. "
               "Suppressing gastric acidity promotes microbial proliferation in the upper "
               "GI tract, and the gut is a major pathogen reservoir in sepsis, so acid "
               "suppression can cost more lives to pneumonia and sepsis than it saves "
               "from bleeding.",
     "rationale": "The trade-off behind 'why not just give everyone a PPI' — a question "
                  "that comes up on every ICU rotation.",
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
        kid = f"marino-icu-{i:02d}"
        if db.execute("SELECT 1 FROM kp_catalog WHERE id=? OR stem=?",
                      (kid, f["stem"])).fetchone():
            skipped += 1
            print(f"  skip  {f['stem'][:66]}")
            continue
        added += 1
        print(f"  add   [{f['topic'][:34]:<34}] {f['stem'][:52]}")
        if args.dry_run:
            continue
        db.execute(
            """INSERT INTO kp_catalog
                   (id, topic, domain, discipline, stem, answer, rationale, bloom,
                    source, confusable_with, tier, category, is_critical_care,
                    car_safe, added_at, times_seen, verified)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (kid, f["topic"], DOMAIN, "medicine", f["stem"], f["answer"],
             f["rationale"], f["bloom"], json.dumps([SOURCE]), "", 1, "topic",
             1, 0, now, 0, 1))
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
