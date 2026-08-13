import json

kps = []

# ── TOPIC 5: Acetaminophen (Paracetamol) Toxicity ────────────────────────────
# Chunks: Morgan & Mikhail p.1757 (APAP pharmacology), p.2160 (overdose mgmt),
# StatPearls p.1/3/4 (mislabeled as CCl4 toxicity but contain APAP context),
# StatPearls Hepatic Encephalopathy p.5 (APAP as cause of ALF)
kps += [
  {
    "id": "apap-tox-1",
    "topic": "Acetaminophen (Paracetamol) Toxicity",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "What is the recommended maximum daily adult dose of acetaminophen, and what condition potentiates its hepatotoxicity?",
    "answer": "Max 3000 mg/day; potentiated by isoniazid, zidovudine, barbiturates, and alcohol",
    "rationale": "Hepatic CYP2E1 inducers (alcohol, isoniazid, barbiturates) increase NAPQI production from APAP metabolism, depleting glutathione and causing centrilobular hepatic necrosis.",
    "bloom": "recall",
    "source": [{"book": "Morgan & Mikhail", "page": 1757}],
    "confusable_with": "4000 mg/day (previously recommended but now reduced to 3000 mg/day for adults)"
  },
  {
    "id": "apap-tox-2",
    "topic": "Acetaminophen (Paracetamol) Toxicity",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "Acetaminophen causes hepatotoxicity at high doses. What is its mechanism of action at therapeutic doses?",
    "answer": "Inhibits prostaglandin synthesis (central); lacks significant anti-inflammatory activity unlike NSAIDs",
    "rationale": "APAP acts centrally on prostaglandin synthesis pathways, producing analgesia and antipyresis without meaningful peripheral COX inhibition or platelet effects.",
    "bloom": "recall",
    "source": [{"book": "Morgan & Mikhail", "page": 1757}],
    "confusable_with": "NSAIDs (peripheral COX inhibitors with anti-inflammatory activity and platelet inhibition)"
  },
  {
    "id": "apap-tox-3",
    "topic": "Acetaminophen (Paracetamol) Toxicity",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "An obtunded patient with unknown ingestion arrives. What three empiric IV treatments should be given while workup proceeds?",
    "answer": "Naloxone (up to 2 mg), dextrose 50% (50 mL), thiamine (100 mg) IV — to treat opioid overdose, hypoglycemia, Wernicke-Korsakoff",
    "rationale": "These reversible or treatable causes of altered consciousness require rapid empiric treatment; dextrose can be omitted if glucose is measured as normal.",
    "bloom": "apply",
    "source": [{"book": "Morgan & Mikhail", "page": 2160}],
    "confusable_with": "flumazenil first (flumazenil risks seizures in benzodiazepine-dependent patients; not routine)"
  },
  {
    "id": "apap-tox-4",
    "topic": "Acetaminophen (Paracetamol) Toxicity",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "Acetaminophen toxicity is a leading cause of acute liver failure. What defines acute liver failure?",
    "answer": "Severe acute liver injury with INR >=1.5 and altered mental status in a patient without preexisting liver disease",
    "rationale": "ALF from APAP toxicity occurs via NAPQI-mediated centrilobular necrosis impairing synthetic function; coagulopathy (elevated INR) and encephalopathy mark decompensation.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Hepatic Encephalopathy", "page": 5}],
    "confusable_with": "acute-on-chronic liver failure (occurs in patients WITH preexisting liver disease)"
  },
  {
    "id": "apap-tox-5",
    "topic": "Acetaminophen (Paracetamol) Toxicity",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "When an overdose patient has concurrent opioid and benzodiazepine ingestion with respiratory depression, what should be done before giving naloxone?",
    "answer": "Intubate first to secure the airway",
    "rationale": "Naloxone rapidly reverses opioid sedation but not benzodiazepine effects; the patient may become combative or protect their airway inadequately, necessitating prior airway control.",
    "bloom": "apply",
    "source": [{"book": "Morgan & Mikhail", "page": 2160}],
    "confusable_with": "naloxone first (risks abrupt arousal with uncontrolled airway if benzos also on board)"
  },
  {
    "_type": "illness_script",
    "topic": "Acetaminophen (Paracetamol) Toxicity",
    "discipline": "medicine",
    "enabling_conditions": "Intentional overdose (single acute ingestion >150 mg/kg), chronic supratherapeutic use, alcohol use, CYP2E1 inducers",
    "pathophysiology": "Excess NAPQI (toxic metabolite) depletes hepatic glutathione, binds covalently to hepatocyte proteins causing centrilobular necrosis",
    "time_course": "Phase 1 (0-24h): nausea/vomiting; Phase 2 (24-72h): RUQ pain, transaminase rise; Phase 3 (72-96h): peak hepatotoxicity, possible ALF; Phase 4: recovery or death",
    "key_features": "Transaminase elevation (may be >10,000), coagulopathy, encephalopathy in ALF; serum APAP level on Rumack-Matthew nomogram guides N-acetylcysteine therapy",
    "consequence_if_missed": "Fulminant hepatic failure, cerebral edema, death without liver transplant"
  }
]

# ── TOPIC 6: Acute Kidney Injury (AKI) in ICU ───────────────────────────────
kps += [
  {
    "id": "aki-icu-1",
    "topic": "Acute Kidney Injury (AKI) in ICU",
    "domain": "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)",
    "discipline": "medicine",
    "stem": "What are the KDIGO diagnostic criteria for AKI? (any of three findings qualifies)",
    "answer": "Serum Cr rise >=0.3 mg/dL within 48h; OR Cr >=1.5x baseline within 7 days; OR urine output <0.5 mL/kg/h for >=6 hours",
    "rationale": "KDIGO 2012 criteria are the most widely used; AKI is common in the ICU (up to 30% of admissions) and may manifest as oliguria alone before Cr rises.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Acute kidney injury", "page": 2}],
    "confusable_with": "RIFLE criteria (older; KDIGO is now preferred and more sensitive)"
  },
  {
    "id": "aki-icu-2",
    "topic": "Acute Kidney Injury (AKI) in ICU",
    "domain": "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)",
    "discipline": "medicine",
    "stem": "Which drugs cause prerenal AKI by reducing intraglomerular pressure via efferent arteriolar vasodilation?",
    "answer": "ACE inhibitors and angiotensin receptor blockers (ARBs)",
    "rationale": "ACEi/ARBs block angiotensin II-mediated efferent vasoconstriction; in states of low renal perfusion (HF, hypovolemia), GFR is maintained by this mechanism — blockade causes filtration failure.",
    "bloom": "apply",
    "source": [{"book": "StatPearls: StatPearls   Acute kidney injury", "page": 3}],
    "confusable_with": "NSAIDs (cause prerenal AKI by afferent arteriolar vasoconstriction, not efferent)"
  },
  {
    "id": "aki-icu-3",
    "topic": "Acute Kidney Injury (AKI) in ICU",
    "domain": "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)",
    "discipline": "medicine",
    "stem": "Sepsis can cause AKI and ATN independent of what commonly assumed mechanism?",
    "answer": "Independent of blood pressure or renal blood flow reduction — sepsis causes direct tubular injury via endothelial dysfunction, inflammation, and oxidative stress",
    "rationale": "JASN 2011 data showed sepsis-induced ATN involves microvascular and inflammatory injury even without frank hypotension, changing the simple ischemia model.",
    "bloom": "analyze",
    "source": [{"book": "MGH Housestaff Manual", "page": 99}],
    "confusable_with": "purely ischemic ATN (septic AKI has additional direct inflammatory pathways)"
  },
  {
    "id": "aki-icu-4",
    "topic": "Acute Kidney Injury (AKI) in ICU",
    "domain": "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)",
    "discipline": "medicine",
    "stem": "What is the mnemonic for emergent dialysis indications in AKI?",
    "answer": "AEIOU: Acidemia (refractory), Electrolytes (hyperkalemia, hypercalcemia), Intoxication (methanol, ethylene glycol, lithium, salicylates), Overload (volume), Uremia (pericarditis, encephalopathy, bleeding)",
    "rationale": "Emergent dialysis is indicated for life-threatening complications of AKI that cannot be managed medically; these AEIOU criteria provide the actionable threshold.",
    "bloom": "recall",
    "source": [{"book": "Intern Notes / Survival Guide", "page": 43}],
    "confusable_with": "absolute Cr or BUN threshold (no single number triggers dialysis; clinical indications guide timing)"
  },
  {
    "id": "aki-icu-5",
    "topic": "Acute Kidney Injury (AKI) in ICU",
    "domain": "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)",
    "discipline": "medicine",
    "stem": "Why does serum creatinine poorly estimate GFR in acute kidney injury compared to chronic kidney disease?",
    "answer": "Cr approximates GFR only at steady state; in AKI, Cr is still rising and does not reflect current GFR — if Cr rises >1 mg/dL/day, assume GFR <10",
    "rationale": "In AKI, renal function is changing rapidly; creatinine lags behind actual GFR changes, causing dangerous underestimation of injury severity during acute phase.",
    "bloom": "analyze",
    "source": [{"book": "MGH Housestaff Manual", "page": 99}],
    "confusable_with": "eGFR formulas (CKD-EPI/MDRD — designed for steady-state CKD, not AKI)"
  },
  {
    "id": "aki-icu-6",
    "topic": "Acute Kidney Injury (AKI) in ICU",
    "domain": "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)",
    "discipline": "medicine",
    "stem": "In hepatorenal syndrome (HRS), what is the initial pharmacologic treatment combination?",
    "answer": "Terlipressin (1 mg IV q6h, escalate to 2 mg q6h if no response at 48-72h) PLUS albumin (20-40 g/day)",
    "rationale": "Terlipressin is a vasopressin analogue that raises MAP and renal perfusion; albumin increases effective arterial blood volume through oncotic and non-oncotic mechanisms, enhancing response.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Hepatorenal Syndrome (HRS)", "page": 8}],
    "confusable_with": "IV fluids alone (volume expansion without vasoconstrictors insufficient in HRS; terlipressin + albumin is the standard)"
  },
  {
    "_type": "illness_script",
    "topic": "Acute Kidney Injury (AKI) in ICU",
    "discipline": "medicine",
    "enabling_conditions": "Sepsis, hypovolemia, nephrotoxins (contrast, aminoglycosides, NSAIDs), cardiac failure, hepatorenal syndrome, rhabdomyolysis",
    "pathophysiology": "Prerenal (reduced perfusion), intrinsic (tubular/glomerular/interstitial injury), or postrenal (obstruction); sepsis-AKI involves endothelial dysfunction beyond pure ischemia",
    "time_course": "Hours to days; oliguria may precede Cr rise; serial monitoring required",
    "key_features": "Rising Cr/BUN, oliguria, electrolyte disturbances (hyperkalemia, acidemia), volume overload",
    "consequence_if_missed": "Severe hyperkalemia causing fatal arrhythmia; refractory metabolic acidosis; uremic pericarditis/encephalopathy"
  }
]

# ── TOPIC 7: Acute Kidney Injury — Electrolyte & Acid-Base ──────────────────
kps += [
  {
    "id": "aki-elec-1",
    "topic": "Acute Kidney Injury — Electrolyte & Acid-Base",
    "domain": "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)",
    "discipline": "medicine",
    "stem": "What anion gap calculation adjustment is critical to avoid missing elevated AG metabolic acidosis in hypoalbuminemic patients?",
    "answer": "Correct anion gap for albumin: corrected AG = measured AG + 2.5 x (4 - albumin [g/dL])",
    "rationale": "Albumin carries negative charge contributing to the normal anion gap; hypoalbuminemia lowers the normal AG, masking a true AGMA if uncorrected.",
    "bloom": "apply",
    "source": [{"book": "StatPearls: StatPearls   Metabolic Acidosis  Approach and Anion Gap", "page": 10}],
    "confusable_with": "unadjusted AG (will miss AGMA in hypoalbuminemic ICU patients)"
  },
  {
    "id": "aki-elec-2",
    "topic": "Acute Kidney Injury — Electrolyte & Acid-Base",
    "domain": "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)",
    "discipline": "medicine",
    "stem": "When the corrected anion gap is elevated, what additional calculation evaluates for concurrent mixed acid-base disorders?",
    "answer": "Delta gap (delta-delta): assess whether the AG rise equals the HCO3 fall (if AG rise > HCO3 fall, concurrent metabolic alkalosis; if AG rise < HCO3 fall, concurrent NAGMA)",
    "rationale": "The delta gap unmasks mixed disorders hidden behind an obvious AGMA by comparing the expected vs. actual HCO3 change.",
    "bloom": "analyze",
    "source": [{"book": "StatPearls: StatPearls   Metabolic Acidosis  Approach and Anion Gap", "page": 10}],
    "confusable_with": "stopping at calculating the anion gap (insufficient for complex ICU mixed disorders)"
  },
  {
    "id": "aki-elec-3",
    "topic": "Acute Kidney Injury — Electrolyte & Acid-Base",
    "domain": "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)",
    "discipline": "medicine",
    "stem": "What potassium replacement constraint applies to peripheral intravenous infusions, and why?",
    "answer": "Do not exceed 8 mEq/h peripherally; >10-20 mEq/h requires central venous access and continuous ECG monitoring",
    "rationale": "Potassium is irritative to peripheral veins at high concentrations and rapid infusion risks cardiac arrhythmias; central access and ECG monitoring are required for aggressive repletion.",
    "bloom": "recall",
    "source": [{"book": "Morgan & Mikhail", "page": 1882}],
    "confusable_with": "IV KCl always acceptable at high rates peripherally (incorrect; exceeding 8 mEq/h peripherally risks phlebitis and cardiac arrhythmia)"
  },
  {
    "id": "aki-elec-4",
    "topic": "Acute Kidney Injury — Electrolyte & Acid-Base",
    "domain": "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)",
    "discipline": "medicine",
    "stem": "In AKI-associated hyperkalemia, why should dextrose-containing IV fluids be avoided for potassium replacement or resuscitation?",
    "answer": "Dextrose causes hyperglycemia leading to secondary insulin release that drives K+ into cells and can worsen existing hypokalemia; in hyperkalemia states it is also counterproductive",
    "rationale": "Insulin-mediated transcellular K+ shift is the desired mechanism for acutely lowering K+ in hyperkalemia (insulin + dextrose), but dextrose alone worsens hypokalemia by triggering this shift.",
    "bloom": "apply",
    "source": [{"book": "Morgan & Mikhail", "page": 1882}],
    "confusable_with": "using dextrose for potassium replacement (contraindicated; will worsen hypokalemia)"
  },
  {
    "id": "aki-elec-5",
    "topic": "Acute Kidney Injury — Electrolyte & Acid-Base",
    "domain": "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)",
    "discipline": "medicine",
    "stem": "Which sequential ECG changes mark progressive hyperkalemia from early to terminal?",
    "answer": "Peaked T waves (shortened QT) -> QRS widening, PR prolongation, P wave loss, R-wave loss, ST depression -> sine wave pattern -> VF/asystole",
    "rationale": "Progressive hyperkalemia depolarizes myocardial membranes, first enhancing then impairing excitability and conduction, culminating in fatal arrhythmia if uncorrected.",
    "bloom": "recall",
    "source": [{"book": "Morgan & Mikhail", "page": 1886}],
    "confusable_with": "hypokalemia ECG changes (U waves, flat T waves, prolonged QU — opposite direction)"
  }
]

# ── TOPIC 8: Acute Pancreatitis & GI Emergencies in ICU ─────────────────────
kps += [
  {
    "id": "acute-panc-1",
    "topic": "Acute Pancreatitis & GI Emergencies in ICU",
    "domain": "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)",
    "discipline": "medicine",
    "stem": "What physical signs indicate hemorrhagic pancreatitis with retroperitoneal or peritoneal bleeding?",
    "answer": "Cullen sign (periumbilical ecchymosis) and Grey-Turner sign (flank ecchymosis)",
    "rationale": "Retroperitoneal and peritoneal blood tracking along fascial planes produces these classic surface discolorations, indicating severe necrotizing hemorrhagic pancreatitis.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Acute Pancreatitis", "page": 9}],
    "confusable_with": "Rovsing sign, psoas sign (appendicitis, not pancreatitis)"
  },
  {
    "id": "acute-panc-2",
    "topic": "Acute Pancreatitis & GI Emergencies in ICU",
    "domain": "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)",
    "discipline": "medicine",
    "stem": "When is CT with IV contrast indicated in acute pancreatitis, and what does it evaluate?",
    "answer": "Not routinely required; indicated when diagnosis is uncertain or patient fails to improve after 48-72 hours — evaluates pancreatic necrosis, pseudocyst, infection",
    "rationale": "Early CT is unnecessary in typical presentations; delayed CT (after 48-72h) is most accurate for necrosis detection and guides intervention decisions.",
    "bloom": "apply",
    "source": [{"book": "StatPearls: StatPearls   Acute Pancreatitis", "page": 11}],
    "confusable_with": "CT always required at presentation (overuse exposes patients to contrast/radiation without benefit if diagnosis is clear)"
  },
  {
    "id": "acute-panc-3",
    "topic": "Acute Pancreatitis & GI Emergencies in ICU",
    "domain": "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)",
    "discipline": "medicine",
    "stem": "What is the CTSI scoring system range and interpretation for acute pancreatitis severity?",
    "answer": "0-10: 0-2 mild, 4-6 moderate, 8-10 severe; based on CT Balthazar grade plus degree of pancreatic necrosis",
    "rationale": "CTSI (CT Severity Index) combines morphologic CT findings with necrosis extent to predict complications and mortality in acute pancreatitis.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Acute Pancreatitis", "page": 16}],
    "confusable_with": "Ranson criteria (clinical scoring, not CT-based)"
  },
  {
    "id": "acute-panc-4",
    "topic": "Acute Pancreatitis & GI Emergencies in ICU",
    "domain": "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)",
    "discipline": "medicine",
    "stem": "Following a single episode of alcohol-related pancreatitis, what is the approximate recurrence rate and risk of progression to chronic pancreatitis?",
    "answer": "Recurrence ~24%; chronic pancreatitis progression ~16% — both reduced by sustained alcohol abstinence",
    "rationale": "Continued alcohol use drives recurrent inflammation leading to permanent exocrine and endocrine dysfunction; abstinence is the most important prognostic intervention.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Acute Pancreatitis", "page": 16}],
    "confusable_with": "gallstone pancreatitis recurrence pattern (cholecystectomy eliminates recurrence; alcohol pancreatitis requires behavioral intervention)"
  },
  {
    "id": "acute-panc-5",
    "topic": "Acute Pancreatitis & GI Emergencies in ICU",
    "domain": "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)",
    "discipline": "medicine",
    "stem": "What chest radiograph finding suggests severe acute pancreatitis with systemic involvement?",
    "answer": "Pleural effusions or bilateral infiltrates (ARDS pattern)",
    "rationale": "Severe pancreatitis triggers systemic inflammatory response syndrome that can cause ARDS (bilateral infiltrates) and pleural effusions from diaphragmatic inflammation.",
    "bloom": "apply",
    "source": [{"book": "StatPearls: StatPearls   Acute Pancreatitis", "page": 11}],
    "confusable_with": "lobar consolidation (suggests pneumonia as alternative diagnosis, not pancreatitis complication)"
  },
  {
    "_type": "illness_script",
    "topic": "Acute Pancreatitis & GI Emergencies in ICU",
    "discipline": "medicine",
    "enabling_conditions": "Gallstones (most common), alcohol (second most common), hypertriglyceridemia, ERCP, drugs",
    "pathophysiology": "Premature intrapancreatic trypsinogen activation causes autodigestion; cytokine release drives SIRS; severe cases progress to necrotizing pancreatitis with infected necrosis",
    "time_course": "Acute onset epigastric pain radiating to back; peaks within hours; systemic complications develop over days",
    "key_features": "Severe epigastric pain, nausea/vomiting, elevated lipase/amylase, hypovolemia; Cullen/Grey-Turner signs in hemorrhagic disease",
    "consequence_if_missed": "Infected pancreatic necrosis, sepsis, ARDS, multiorgan failure, death"
  }
]

# ── TOPIC 9: Acute Spinal Cord Injury & Syndromes ───────────────────────────
kps += [
  {
    "id": "spinal-cord-1",
    "topic": "Acute Spinal Cord Injury & Syndromes",
    "domain": "Internal medicine: neurology (ischemic & hemorrhagic stroke, seizures & status epilepticus, altered mental status & delirium, headache, neuromuscular weakness, spinal cord syndromes)",
    "discipline": "medicine",
    "stem": "Anterior cord syndrome presents with what sensory and motor pattern?",
    "answer": "Bilateral motor paralysis + loss of pain/temperature (spinothalamic), with PRESERVED proprioception, vibration, and fine touch (dorsal columns intact)",
    "rationale": "The anterior spinal artery supplies the anterior two-thirds of the spinal cord (corticospinal tracts and spinothalamic tracts); dorsal columns supplied by posterior spinal arteries are spared.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Acute Spinal Cord Injury & Syndromes", "page": 2}],
    "confusable_with": "Brown-Sequard syndrome (ipsilateral motor + dorsal column loss, contralateral spinothalamic loss from hemisection)"
  },
  {
    "id": "spinal-cord-2",
    "topic": "Acute Spinal Cord Injury & Syndromes",
    "domain": "Internal medicine: neurology (ischemic & hemorrhagic stroke, seizures & status epilepticus, altered mental status & delirium, headache, neuromuscular weakness, spinal cord syndromes)",
    "discipline": "medicine",
    "stem": "What is the most common cause of anterior spinal artery syndrome?",
    "answer": "Aortic surgery",
    "rationale": "Interruption of radiculomedullary arteries (particularly the artery of Adamkiewicz at T9-L2) during aortic cross-clamping deprives the anterior spinal artery of its major blood supply.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Acute Spinal Cord Injury & Syndromes", "page": 3}],
    "confusable_with": "atherosclerotic embolism (second most common but less frequent than aortic surgery)"
  },
  {
    "id": "spinal-cord-3",
    "topic": "Acute Spinal Cord Injury & Syndromes",
    "domain": "Internal medicine: neurology (ischemic & hemorrhagic stroke, seizures & status epilepticus, altered mental status & delirium, headache, neuromuscular weakness, spinal cord syndromes)",
    "discipline": "medicine",
    "stem": "What intraoperative protocol is used to reduce anterior spinal artery syndrome risk during aortic surgery?",
    "answer": "Increase MAP (raise blood pressure) to improve anterior spinal artery flow; place lumbar drain to reduce cerebrospinal fluid pressure and improve spinal cord perfusion pressure",
    "rationale": "Spinal cord perfusion pressure = MAP minus CSF pressure; lumbar drainage reduces the CSF pressure component while vasopressors increase MAP, protecting cord perfusion.",
    "bloom": "apply",
    "source": [{"book": "StatPearls: StatPearls   Acute Spinal Cord Injury & Syndromes", "page": 11}],
    "confusable_with": "hypothermia alone (adjunct, not the primary mechanism of cord protection during aortic surgery)"
  },
  {
    "id": "spinal-cord-4",
    "topic": "Acute Spinal Cord Injury & Syndromes",
    "domain": "Internal medicine: neurology (ischemic & hemorrhagic stroke, seizures & status epilepticus, altered mental status & delirium, headache, neuromuscular weakness, spinal cord syndromes)",
    "discipline": "medicine",
    "stem": "Why are lateral horn structures particularly relevant to autonomic dysfunction in spinal cord injury?",
    "answer": "Lateral horns (T1-L2) contain preganglionic sympathetic neurons; injuries above T1 disrupt all sympathetic outflow causing neurogenic shock",
    "rationale": "If spinal cord ischemia does not involve T1-L2 lateral horns, autonomic symptoms may be absent; injuries above this level impair sympathetic vasomotor control causing hypotension and bradycardia.",
    "bloom": "analyze",
    "source": [{"book": "StatPearls: StatPearls   Acute Spinal Cord Injury & Syndromes", "page": 3}],
    "confusable_with": "purely sensorimotor deficit (autonomic dysfunction is common in high cervical lesions)"
  },
  {
    "id": "spinal-cord-5",
    "topic": "Acute Spinal Cord Injury & Syndromes",
    "domain": "Internal medicine: neurology (ischemic & hemorrhagic stroke, seizures & status epilepticus, altered mental status & delirium, headache, neuromuscular weakness, spinal cord syndromes)",
    "discipline": "medicine",
    "stem": "What is the gold standard imaging modality for confirming anterior spinal cord syndrome?",
    "answer": "MRI",
    "rationale": "MRI directly visualizes spinal cord infarction, edema, and vascular anatomy, confirming the anatomical level and extent of cord damage; no acute treatment exists but MRI guides prognosis.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Acute Spinal Cord Injury & Syndromes", "page": 15}],
    "confusable_with": "CT myelography (adequate for bony anatomy, inferior to MRI for cord parenchyma)"
  },
  {
    "_type": "illness_script",
    "topic": "Acute Spinal Cord Injury & Syndromes",
    "discipline": "medicine",
    "enabling_conditions": "Aortic surgery, aortic atherosclerosis/dissection, spinal trauma, percutaneous spinal procedures, hypotension, sickle cell disease",
    "pathophysiology": "Occlusion or hypoperfusion of the anterior spinal artery causes infarction of the anterior 2/3 of cord (motor tracts + spinothalamic tracts); dorsal columns spared",
    "time_course": "Acute onset: sudden back pain at level of injury followed within minutes to hours by bilateral motor deficit and sensory loss",
    "key_features": "Bilateral flaccid then spastic paraparesis; loss of pain/temperature; preserved proprioception; MRI confirms cord infarct",
    "consequence_if_missed": "Most patients remain functionally incapacitated; respiratory failure in high cervical lesions; delayed neurogenic bladder and pressure ulcers"
  }
]

# ── TOPIC 10: Angioedema ──────────────────────────────────────────────────────
kps += [
  {
    "id": "angioedema-1",
    "topic": "Angioedema",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "How does angioedema differ from urticaria in its pathophysiology and location?",
    "answer": "Urticaria: IgE-mediated, superficial skin (wheals with pruritus); Angioedema: deep non-pitting edema of subcutaneous tissue from vasodilation and increased permeability — can involve pharynx/larynx",
    "rationale": "Angioedema involves deeper subcutaneous and submucosal tissues; when it involves the upper airway it causes life-threatening obstruction requiring immediate airway management.",
    "bloom": "apply",
    "source": [{"book": "Morgan & Mikhail", "page": 2035}],
    "confusable_with": "urticaria (superficial skin, pruritic, does not cause airway obstruction)"
  },
  {
    "id": "angioedema-2",
    "topic": "Angioedema",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "What mediator in anaphylaxis causes vasodilation, increased vascular permeability, and smooth muscle contraction, contributing to angioedema?",
    "answer": "Bradykinin (cleaved from kininogen by BK-A) — increases vascular permeability and vasodilation; also histamine from mast cell degranulation",
    "rationale": "Bradykinin-mediated angioedema (as in ACE inhibitor angioedema and hereditary angioedema) is histamine-independent and does not respond to antihistamines or epinephrine reliably.",
    "bloom": "recall",
    "source": [{"book": "Morgan & Mikhail", "page": 2037}],
    "confusable_with": "histamine-mediated angioedema (responds to antihistamines; bradykinin-mediated does not)"
  },
  {
    "id": "angioedema-3",
    "topic": "Angioedema",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "What treatment is indicated for hereditary angioedema (HAE) acute attacks that is distinct from allergic angioedema?",
    "answer": "C1 inhibitor replacement protein (C1INHRP); fresh frozen plasma (FFP) as alternative",
    "rationale": "HAE is caused by C1 inhibitor deficiency leading to bradykinin excess; replacing C1 inhibitor halts the kinin cascade; epinephrine and antihistamines are largely ineffective.",
    "bloom": "apply",
    "source": [{"book": "Morgan & Mikhail", "page": 2036}],
    "confusable_with": "epinephrine (first line for IgE/histamine-mediated allergic angioedema; ineffective for bradykinin-mediated HAE)"
  },
  {
    "id": "angioedema-4",
    "topic": "Angioedema",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "ACE inhibitors cause angioedema via what mechanism, and how is this distinguished from allergic angioedema?",
    "answer": "ACE inhibitor blocks bradykinin degradation, causing bradykinin accumulation; this is non-IgE mediated, non-pruritic, and does not respond to antihistamines/steroids",
    "rationale": "ACE inhibitors inhibit kininase II (same as ACE), which normally degrades bradykinin; accumulation causes bradykinin-mediated vasodilation and permeability increase in susceptible patients.",
    "bloom": "analyze",
    "source": [{"book": "Morgan & Mikhail", "page": 660}],
    "confusable_with": "drug allergy (different mechanism; ACEi angioedema is pharmacologic, not immunologic)"
  },
  {
    "id": "angioedema-5",
    "topic": "Angioedema",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "In anaphylaxis with angioedema involving the pharynx/larynx, what are the immediate airway management priorities in order?",
    "answer": "Epinephrine IM immediately; prepare for intubation (may be difficult due to edema); surgical airway (cricothyrotomy) if intubation fails",
    "rationale": "Laryngeal/pharyngeal angioedema rapidly progresses; epinephrine is the first-line vasopressor and bronchodilator; edema may make intubation impossible, requiring surgical airway.",
    "bloom": "apply",
    "source": [{"book": "Morgan & Mikhail", "page": 2036}],
    "confusable_with": "antihistamines first (too slow; epinephrine is the life-saving immediate intervention)"
  },
  {
    "_type": "illness_script",
    "topic": "Angioedema",
    "discipline": "medicine",
    "enabling_conditions": "ACE inhibitor use, hereditary C1 inhibitor deficiency, IgE-mediated allergy (foods, drugs, latex), NSAIDs",
    "pathophysiology": "Histamine or bradykinin-mediated marked vasodilation and increased permeability of submucosal blood vessels; deep non-pitting edema develops",
    "time_course": "Can develop within minutes (allergic) to hours (bradykinin-mediated); laryngeal involvement causes rapid airway obstruction",
    "key_features": "Non-pitting swelling of face/lips/tongue/throat; absent pruritus (bradykinin-mediated); may coexist with urticaria (allergic)",
    "consequence_if_missed": "Complete upper airway obstruction, asphyxiation, and death if laryngeal edema not recognized and managed"
  }
]

print(f"Batch 2: {len(kps)} entries")
with open("C:/Users/Dean/anesthesia_attending/data/_kp_batch2.json", "w", encoding="utf-8") as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Written to _kp_batch2.json")
