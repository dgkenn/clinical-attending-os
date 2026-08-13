import json

kps = []

# ── TOPIC 29: Chest Trauma ───────────────────────────────────────────────────
# Chunks are largely off-topic (laryngospasm, VTE, bronchiectasis, causes of hypoxemia).
# Writing KPs from the most relevant fragments.
kps += [
  {
    "id": "chest-trauma-1",
    "topic": "Chest Trauma",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "What are the causes of hypoxemia that should be considered after chest trauma, organized by mechanism?",
    "answer": "V/Q mismatch (contusion, hemothorax, pneumothorax); shunt (atelectasis, contusion); dead space (tension pneumothorax); decreased FiO2 rare; also hypoventilation from pain or chest wall instability",
    "rationale": "Chest trauma causes multiple simultaneous mechanisms of hypoxemia; pulmonary contusion, pneumothorax, and hemothorax all reduce V/Q ratio; tension pneumothorax creates dead space and obstructive shock.",
    "bloom": "analyze",
    "source": [{"book": "Stanford CA-1", "page": 54}],
    "confusable_with": "a single mechanism explaining all chest-trauma hypoxemia (multiple simultaneous mechanisms are the rule)"
  },
  {
    "id": "chest-trauma-2",
    "topic": "Chest Trauma",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "In a trauma patient on positive-pressure ventilation with rising peak pressure, PEEP increase, and new hypotension, what is the emergent diagnosis and treatment?",
    "answer": "Tension pneumothorax; immediate needle decompression (2nd ICS MCL) followed by chest tube thoracostomy",
    "rationale": "PPV forces air through a pleural tear; rising intrathoracic pressure collapses the lung and compresses mediastinum, obstructing venous return causing obstructive shock.",
    "bloom": "apply",
    "source": [{"book": "Miller/Baby Miller", "page": 380}],
    "confusable_with": "bronchospasm (raises peak pressure without hemodynamic compromise and without plateau pressure rise)"
  },
  {
    "id": "chest-trauma-3",
    "topic": "Chest Trauma",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "What are the critical early assessments for trauma patients emphasized for anesthesiologists in the emergency department?",
    "answer": "Adequacy of airway, vascular access, hemodynamic tolerance of anesthesia, prevention of hypothermia, blood bank access, avoidance of crystalloids and vasopressors until hemorrhage is controlled",
    "rationale": "Permissive hypotension (targeting MAP rather than normal BP) until hemorrhage is surgically controlled reduces dilutional coagulopathy; hypothermia impairs coagulation; early anesthesiologist involvement improves outcomes.",
    "bloom": "apply",
    "source": [{"book": "Morgan & Mikhail", "page": 1333}],
    "confusable_with": "aggressive crystalloid resuscitation pre-operatively (excessive crystalloids worsen dilutional coagulopathy and coagulopathic bleeding)"
  },
  {
    "id": "chest-trauma-4",
    "topic": "Chest Trauma",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "What is negative pressure pulmonary edema (NPPE) and what causes it in the context of laryngospasm?",
    "answer": "NPPE occurs when forceful inspiratory effort against an obstructed upper airway (laryngospasm, severe stridor) generates extreme negative intrathoracic pressure, drawing fluid into alveoli",
    "rationale": "The strongly negative intrathoracic pressure increases left ventricular afterload and reduces left atrial pressure, pulling fluid from pulmonary capillaries into alveoli — a form of non-cardiogenic pulmonary edema.",
    "bloom": "analyze",
    "source": [{"book": "Stanford CA-1", "page": 73}],
    "confusable_with": "cardiogenic pulmonary edema (NPPE is mechanical/hydrostatic from negative pressure, not cardiac failure; resolves with airway opening)"
  }
]

# ── TOPIC 30: Coagulopathy & Hematologic Emergencies in ICU ─────────────────
kps += [
  {
    "id": "coagulopathy-icu-1",
    "topic": "Coagulopathy & Hematologic Emergencies in ICU",
    "domain": "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)",
    "discipline": "medicine",
    "stem": "The PROPPR trial established the optimal blood product transfusion ratio in massive hemorrhage. What ratio was found to reduce mortality?",
    "answer": "1:1:1 ratio of plasma:platelets:packed red blood cells (compared to 1:1:2)",
    "rationale": "Balanced resuscitation (1:1:1 ratio) provides hemostatic components proportionate to red cells, reducing dilutional coagulopathy and improving survival in massive hemorrhage (JAMA 2015;313:471).",
    "bloom": "recall",
    "source": [{"book": "Morgan & Mikhail", "page": 1353}],
    "confusable_with": "1:1:2 ratio (older approach prioritizing RBC over plasma/platelets; inferior in PROPPR trial)"
  },
  {
    "id": "coagulopathy-icu-2",
    "topic": "Coagulopathy & Hematologic Emergencies in ICU",
    "domain": "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)",
    "discipline": "medicine",
    "stem": "In the non-bleeding patient, at what platelet count threshold is prophylactic platelet transfusion recommended?",
    "answer": "Platelet count <10,000/uL in non-bleeding patients; <50,000/uL for active bleeding or surgical procedures; <100,000/uL for intracranial hemorrhage or neurosurgery",
    "rationale": "Risk-stratified platelet transfusion thresholds balance transfusion risks against bleeding risk; neurosurgery and intracranial hemorrhage require higher counts due to critical consequences of bleeding.",
    "bloom": "recall",
    "source": [{"book": "Miller/Baby Miller", "page": 446}],
    "confusable_with": "transfusing platelets at 50,000 for all patients regardless of bleeding (unnecessary transfusion in stable non-bleeding patients)"
  },
  {
    "id": "coagulopathy-icu-3",
    "topic": "Coagulopathy & Hematologic Emergencies in ICU",
    "domain": "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)",
    "discipline": "medicine",
    "stem": "Antifibrinolytic therapy is generally contraindicated in DIC. Why?",
    "answer": "DIC involves simultaneous activation of both coagulation and fibrinolysis; blocking fibrinolysis in DIC risks catastrophic thrombotic complications from unopposed fibrin deposition",
    "rationale": "In DIC, fibrinolysis is a compensatory mechanism to clear widespread microthrombi; inhibiting it with antifibrinolytics (TXA, aminocaproic acid) can cause end-organ ischemia and is generally contraindicated.",
    "bloom": "analyze",
    "source": [{"book": "Miller/Baby Miller", "page": 446}],
    "confusable_with": "antifibrinolytics beneficial in all coagulopathy (only appropriate in isolated hyperfibrinolysis, NOT in DIC)"
  },
  {
    "id": "coagulopathy-icu-4",
    "topic": "Coagulopathy & Hematologic Emergencies in ICU",
    "domain": "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)",
    "discipline": "medicine",
    "stem": "What is transfusion-associated circulatory overload (TACO), and what patient factors predispose to it?",
    "answer": "TACO is pulmonary edema from volume overload during transfusion; risk factors include pre-existing cardiac dysfunction, renal insufficiency, hypoalbuminemia, and rapid infusion rate",
    "rationale": "Transfusion adds osmotically and hydrostatically active fluid; patients with impaired cardiac or renal compensation for added volume cannot handle this without developing flash pulmonary edema.",
    "bloom": "apply",
    "source": [{"book": "Morgan & Mikhail", "page": 1353}],
    "confusable_with": "TRALI (transfusion-related acute lung injury — non-cardiogenic, within 6h, antibody-mediated; TACO is cardiogenic, elevated BNP)"
  },
  {
    "id": "coagulopathy-icu-5",
    "topic": "Coagulopathy & Hematologic Emergencies in ICU",
    "domain": "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)",
    "discipline": "medicine",
    "stem": "In heparin use during DIC, what conditions have the highest thrombotic risk that might justify anticoagulation despite active coagulopathy?",
    "answer": "Conditions with highest thrombotic risk such as promyelocytic leukemia-associated DIC (APL) or purpura fulminans",
    "rationale": "Most DIC is managed supportively with factor/platelet replacement; heparin is reserved for DIC dominated by thrombosis (APL-DIC, purpura fulminans) where clotting is the primary life threat, not bleeding.",
    "bloom": "analyze",
    "source": [{"book": "Miller/Baby Miller", "page": 446}],
    "confusable_with": "heparin for all DIC (contraindicated in hemorrhagic DIC; only for specific thrombotic-predominant subtypes)"
  }
]

# ── TOPIC 31: Corticosteroid complications & steroid-sparing strategies ───────
# Chunks largely off-topic (fat embolism, CMV endotheliitis, adrenal crisis, pituitary apoplexy).
# Write KPs from relevant fragments only.
kps += [
  {
    "id": "steroid-complication-1",
    "topic": "Corticosteroid complications & steroid-sparing strategies",
    "domain": "Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)",
    "discipline": "medicine",
    "stem": "What are the 'sick day rules' for patients on chronic glucocorticoids who develop an acute illness?",
    "answer": "Double or triple the daily oral glucocorticoid dose during acute illness; for fever >38C, double the dose; cannot take oral medications: use parenteral equivalent and seek emergency care",
    "rationale": "Chronic glucocorticoid use suppresses the HPA axis; physiologic stress normally triggers cortisol surge to 3-5x baseline; patients on chronic steroids cannot mount this response and require supplementation.",
    "bloom": "apply",
    "source": [{"book": "StatPearls: StatPearls   Adrenal Crisis", "page": 12}],
    "confusable_with": "stopping steroids during illness (dangerous; may precipitate adrenal crisis)"
  },
  {
    "id": "steroid-complication-2",
    "topic": "Corticosteroid complications & steroid-sparing strategies",
    "domain": "Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)",
    "discipline": "medicine",
    "stem": "More than what percentage of patients who develop adrenal crisis do NOT have a prior diagnosis of adrenal insufficiency?",
    "answer": "More than 50% — clinician familiarity with stress-dose steroids is essential even without established diagnosis",
    "rationale": "Undiagnosed or secondary adrenal insufficiency (from exogenous steroid use, pituitary disease) frequently presents as adrenal crisis during physiologic stress; high clinical suspicion is required.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Adrenal Crisis", "page": 12}],
    "confusable_with": "adrenal crisis only occurring in known Addison disease (secondary and undiagnosed adrenal insufficiency are equally at risk)"
  },
  {
    "id": "steroid-complication-3",
    "topic": "Corticosteroid complications & steroid-sparing strategies",
    "domain": "Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)",
    "discipline": "medicine",
    "stem": "Pituitary apoplexy is a rare but life-threatening emergency requiring rapid initiation of what specific treatment to prevent adrenal crisis?",
    "answer": "Immediate corticosteroid therapy (hydrocortisone) to prevent/treat adrenal crisis from sudden loss of ACTH drive to the adrenal glands",
    "rationale": "Pituitary apoplexy (hemorrhage or infarction of pituitary adenoma) destroys ACTH-secreting cells, causing acute secondary adrenal insufficiency; without cortisol replacement, patients develop refractory hypotension.",
    "bloom": "apply",
    "source": [{"book": "StatPearls: StatPearls   Pituitary Apoplexy", "page": 1}],
    "confusable_with": "surgical decompression first (steroids must be given before or concurrently with surgical decisions to prevent death from adrenal crisis)"
  },
  {
    "id": "steroid-complication-4",
    "topic": "Corticosteroid complications & steroid-sparing strategies",
    "domain": "Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)",
    "discipline": "medicine",
    "stem": "Steroid-induced ocular hypertension is a complication of long-term topical corticosteroid use. Why does this complicate management of CMV corneal endotheliitis?",
    "answer": "CMV endotheliitis requires antiviral therapy; topical corticosteroids used to suppress inflammation worsen IOP; regular IOP monitoring and anti-glaucoma therapy are required concurrently",
    "rationale": "The competing needs of immune suppression (to reduce corneal edema) versus avoidance of steroid-induced IOP elevation require careful monitoring and often dual therapy.",
    "bloom": "analyze",
    "source": [{"book": "StatPearls: StatPearls   Bone marrow transplantation  complications", "page": 29}],
    "confusable_with": "stopping steroids to protect IOP (may worsen corneal graft rejection; requires balance with anti-glaucoma treatment)"
  }
]

# ── TOPIC 32: Digoxin Toxicity ────────────────────────────────────────────────
kps += [
  {
    "id": "digoxin-tox-1",
    "topic": "Digoxin Toxicity",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "What serum potassium level is desirable in patients taking digoxin to prevent toxicity from hypokalemia?",
    "answer": "Potassium >4.0 mEq/L in patients on digoxin; hypokalemia potentiates digoxin toxicity",
    "rationale": "Digoxin inhibits Na/K-ATPase; hypokalemia reduces competition at the pump binding site, increasing digoxin binding and toxicity; maintaining K+ >4 mEq/L reduces this risk.",
    "bloom": "recall",
    "source": [{"book": "Morgan & Mikhail", "page": 1882}],
    "confusable_with": "K+ >3.5 mEq/L being sufficient for digoxin patients (higher threshold >4.0 mEq/L applies specifically to digoxin users)"
  },
  {
    "id": "digoxin-tox-2",
    "topic": "Digoxin Toxicity",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "What is the danger of administering calcium salts to patients taking digoxin, even for hyperkalemia treatment?",
    "answer": "Calcium potentiates digoxin toxicity; theoretical risk of stone heart (irreversible non-contractile diastolic arrest); however clinical studies have NOT confirmed significant risk in practice",
    "rationale": "Digoxin impairs Ca extrusion via Na/K-ATPase; additional calcium further elevates intracellular Ca; the theoretical 'stone heart' has not been reliably demonstrated clinically, but caution remains.",
    "bloom": "analyze",
    "source": [{"book": "Morgan & Mikhail", "page": 1886}],
    "confusable_with": "calcium absolutely contraindicated in digoxin toxicity (the concern is theoretical; use calcium when hyperkalemia is life-threatening, with monitoring)"
  },
  {
    "id": "digoxin-tox-3",
    "topic": "Digoxin Toxicity",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "Hypomagnesemia potentiates digoxin toxicity by what mechanism, and what other electrolyte disturbance does hypomagnesemia commonly cause?",
    "answer": "Hypomagnesemia potentiates digoxin-associated arrhythmias; it also causes hypokalemia (via renal K+ wasting) which further increases digoxin toxicity — dual electrolyte correction required",
    "rationale": "Mg is a cofactor for Na/K-ATPase (same target as digoxin); Mg deficiency impairs renal K+ retention causing hypokalemia; both electrolyte deficiencies synergistically increase digoxin toxicity risk.",
    "bloom": "analyze",
    "source": [{"book": "Morgan & Mikhail", "page": 1899}],
    "confusable_with": "correcting K+ alone (hypomagnesemia will continue to waste K+ renally, making K+ repletion refractory until Mg is corrected)"
  },
  {
    "id": "digoxin-tox-4",
    "topic": "Digoxin Toxicity",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "What mechanisms promote abnormal cardiac impulse formation (triggered activity) and are particularly associated with digoxin toxicity?",
    "answer": "Delayed after-depolarizations (phase 3-4) reaching threshold potential, causing extrasystoles or sustained tachyarrhythmias; digoxin increases intracellular Ca promoting this mechanism",
    "rationale": "Digoxin impairs Na/K-ATPase, raising intracellular Na which increases intracellular Ca via Na/Ca exchanger; elevated Ca causes delayed after-depolarizations promoting ventricular arrhythmias.",
    "bloom": "analyze",
    "source": [{"book": "Morgan & Mikhail", "page": 607}],
    "confusable_with": "early after-depolarizations (typical of QT-prolonging drugs; digoxin primarily causes delayed after-depolarizations)"
  },
  {
    "id": "digoxin-tox-5",
    "topic": "Digoxin Toxicity",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "Hyperkalemia >6 mEq/L from any cause requires treatment due to lethal cardiac risk. What ECG progression leads to ventricular fibrillation?",
    "answer": "Peaked T waves (short QT) -> QRS widening, PR prolongation -> P wave loss -> sine wave pattern -> ventricular fibrillation/asystole",
    "rationale": "Progressive hyperkalemia depolarizes the resting membrane potential; conduction slows and automaticity fails; the sine wave pattern represents near-terminal loss of normal ventricular depolarization.",
    "bloom": "recall",
    "source": [{"book": "Morgan & Mikhail", "page": 1886}],
    "confusable_with": "LBBB pattern (fixed morphology; hyperkalemia ECG changes are dynamic and progress with rising K+)"
  },
  {
    "_type": "illness_script",
    "topic": "Digoxin Toxicity",
    "discipline": "medicine",
    "enabling_conditions": "Renal impairment (decreased clearance), hypokalemia, hypomagnesemia, hypothyroidism, drug interactions (amiodarone, verapamil double digoxin levels)",
    "pathophysiology": "Na/K-ATPase inhibition increases intracellular Na and Ca; AV nodal block (therapeutic); delayed after-depolarizations cause triggered arrhythmias; narrow therapeutic index",
    "time_course": "Chronic toxicity more common than acute; symptoms develop insidiously with declining renal function or electrolyte disturbance",
    "key_features": "Non-specific: nausea/vomiting, visual disturbances (xanthopsia); cardiac: bradyarrhythmias, heart block, ventricular ectopy, atrial tachycardia with AV block (classic), bidirectional VT",
    "consequence_if_missed": "Life-threatening arrhythmias; treatment: digoxin antibody fragments (Digibind/DigiFab) for severe toxicity"
  }
]

print(f"Batch 7: {len(kps)} entries")
with open("C:/Users/Dean/anesthesia_attending/data/_kp_batch7.json", "w", encoding="utf-8") as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Written to _kp_batch7.json")
