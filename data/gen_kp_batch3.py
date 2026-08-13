import json

kps = []

# ITEM 164: NSTEMI / Unstable Angina
topic = "NSTEMI and Unstable Angina"
domain = "Internal medicine: cardiology (ACS, stable & unstable angina, heart failure, brady/tachyarrhythmias, valvular disease, hypertension & emergencies, lipids, syncope)"
disc = "medicine"
kps += [
  {"id":"nstemi-unstable-angina-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the HEART score and what threshold drives early invasive strategy?",
   "answer":"HEART score: History, ECG, Age, Risk factors, Troponin (each 0-2 points). Score >=4 is high risk; score 0-3 is low risk allowing early discharge.",
   "rationale":"HEART score stratifies 6-week MACE risk; high scores warrant invasive strategy within 24 hours.",
   "bloom":"apply","source":[{"book":"StatPearls","page":1}],"confusable_with":"TIMI score (similar but less validated in ED)"},
  {"id":"nstemi-unstable-angina-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What distinguishes NSTEMI from unstable angina in the biomarker era?",
   "answer":"NSTEMI: elevated troponin indicating myocyte necrosis. Unstable angina: no troponin elevation despite symptoms; no myocyte injury.",
   "rationale":"Troponin elevation is the defining biochemical criterion separating the two; both may have ST depression or T-wave changes.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2137}],"confusable_with":"STEMI (ST elevation with complete occlusion)"},
  {"id":"nstemi-unstable-angina-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the recommended timing for PCI in NSTEMI with high-risk features (persistent ischemia, hemodynamic instability)?",
   "answer":"Immediate invasive strategy (within 2 hours) — analogous to STEMI management.",
   "rationale":"Very high-risk NSTEMI (ongoing ischemia, hemodynamic instability, severe arrhythmia) mandates urgent revascularization.",
   "bloom":"recall","source":[{"book":"StatPearls","page":3}],"confusable_with":"routine NSTEMI (<24 hours)"},
  {"id":"nstemi-unstable-angina-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Name four high-risk features in NSTEMI that mandate early invasive strategy within 24 hours.",
   "answer":"Troponin rise/fall, dynamic ST/T changes, GRACE score >140, and TIMI risk score >=3.",
   "rationale":"These markers indicate significant plaque instability and adverse short-term outcomes without revascularization.",
   "bloom":"recall","source":[{"book":"StatPearls","page":3}],"confusable_with":""},
  {"id":"nstemi-unstable-angina-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What perioperative timeframe is associated with the highest risk of reinfarction for elective surgery after NSTEMI?",
   "answer":"Within 30 days of NSTEMI; after DES placement, delay elective surgery minimum 12 months (6 months with newer-generation DES per ACC/AHA).",
   "rationale":"Stent thrombosis risk is highest in the first months; DAPT interruption for surgery increases this risk.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":621}],"confusable_with":"bare-metal stent (delay 30 days)"},
  {"id":"nstemi-unstable-angina-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What ECG change in the absence of ST elevation is most specific for NSTEMI?",
   "answer":"New horizontal or downsloping ST depression >=0.5 mm in >=2 contiguous leads, or deep symmetric T-wave inversions.",
   "rationale":"These ECG changes indicate subendocardial ischemia (vs. transmural injury in STEMI).",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2137}],"confusable_with":"Wellens pattern (critical LAD stenosis, T-wave inversions V1-V4)"},
]

# ITEM 165: Neutropenic fever
topic = "Neutropenic fever"
domain = "Internal medicine: hematology & oncology (anemias, anticoagulation & reversal, VTE prophylaxis & treatment, thrombocytopenia & DIC, transfusion medicine, oncologic emergencies, neutropenic fever)"
disc = "medicine"
kps += [
  {"id":"neutropenic-fever-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Define neutropenic fever by ANC and temperature criteria.",
   "answer":"ANC <500 cells/mm3 (or <1000 with expected fall to <500 in 48 hours) with single oral temperature >38.3°C or sustained >38.0°C for >1 hour.",
   "rationale":"Specific thresholds prevent both over- and under-treatment; ANC <500 defines profound immunosuppression.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":202}],"confusable_with":""},
  {"id":"neutropenic-fever-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What empiric antibiotic coverage is required at presentation of neutropenic fever?",
   "answer":"Anti-pseudomonal beta-lactam monotherapy: piperacillin-tazobactam, cefepime, meropenem, or imipenem-cilastatin IV within 60 minutes.",
   "rationale":"Pseudomonas and enteric gram-negatives are rapidly fatal in neutropenic patients; broad coverage is mandatory.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":202}],"confusable_with":""},
  {"id":"neutropenic-fever-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What MASCC score threshold separates high-risk from low-risk neutropenic fever?",
   "answer":"MASCC score >=21 = low risk (consider oral step-down or outpatient management); <21 = high risk (inpatient IV antibiotics).",
   "rationale":"MASCC score accounts for comorbidities, symptom burden, and solid vs. hematologic malignancy to stratify risk.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":202}],"confusable_with":""},
  {"id":"neutropenic-fever-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"When should vancomycin be added empirically to broad-spectrum coverage in neutropenic fever?",
   "answer":"Add vancomycin for suspected MRSA, catheter-related infection, hypotension, mucositis, prior MRSA colonization, or gram-positive bacteremia pending susceptibilities.",
   "rationale":"Routine vancomycin addition is not recommended due to resistance risk; it is reserved for high-risk gram-positive scenarios.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":202}],"confusable_with":""},
  {"id":"neutropenic-fever-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"For persistent fever after 4 days of antibiotics with no identified source in neutropenic patients, what should be added?",
   "answer":"Empiric antifungal coverage (echinocandin or liposomal amphotericin B) for suspected invasive fungal infection.",
   "rationale":"Candida and mold (Aspergillus) superinfection occurs after prolonged neutropenia and broad-spectrum antibiotics.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":202}],"confusable_with":"fluconazole (inadequate for mold coverage)"},
  {"id":"neutropenic-fever-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Name two signs suggesting invasive pulmonary aspergillosis in a persistently febrile neutropenic patient.",
   "answer":"CT chest showing halo sign (ground-glass opacity surrounding a nodule) or air crescent sign; elevated serum or BAL galactomannan.",
   "rationale":"These CT and serum markers are relatively specific for invasive Aspergillus; prompt antifungal escalation is required.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":202}],"confusable_with":""},
]

# ITEM 166: Palliative care and symptom management
topic = "Palliative care & symptom management"
domain = "General internal medicine, preventive care & geriatrics (admission & cross-cover problems, perioperative medicine, screening & vaccination, polypharmacy & deprescribing, frailty, delirium prevention, goals of care)"
disc = "medicine"
kps += [
  {"id":"palliative-care-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the WHO analgesic ladder for pain management?",
   "answer":"Step 1: Non-opioids (NSAID/acetaminophen). Step 2: Mild opioid ± non-opioid (codeine, tramadol). Step 3: Strong opioid ± non-opioid (morphine, oxycodone, fentanyl).",
   "rationale":"Stepwise escalation ensures adequate pain control while minimizing side effects; step 2 may be omitted for severe pain.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":866}],"confusable_with":""},
  {"id":"palliative-care-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is equianalgesic dosing and why is it required when rotating opioids?",
   "answer":"Equianalgesic dosing uses standardized dose conversions to maintain analgesia when switching opioids; incomplete cross-tolerance requires reducing the new opioid dose by 25-50%.",
   "rationale":"Different opioids have different receptor binding profiles; tolerance to one does not fully transfer to another.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":870}],"confusable_with":""},
  {"id":"palliative-care-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is terminal sedation (palliative sedation) and what are its ethical justifications?",
   "answer":"Sedation to unconsciousness for refractory suffering at end of life; justified by the doctrine of double effect and proportionality.",
   "rationale":"Intent is symptom relief, not hastening death; requires careful documentation of refractory symptoms and consent.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":873}],"confusable_with":"physician-assisted dying (intent is death)"},
  {"id":"palliative-care-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"For dyspnea management in the dying patient, what is the first-line pharmacologic agent?",
   "answer":"Low-dose opioids (morphine 2-4 mg IV/SC q4h) reduce the sensation of dyspnea via central opioid and opioid-sensitive receptors.",
   "rationale":"Opioids are the most evidence-based treatment for refractory dyspnea; they do not hasten death at appropriate doses.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":871}],"confusable_with":"benzodiazepines (second-line for dyspnea anxiety)"},
  {"id":"palliative-care-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the evidence basis for withholding vs. withdrawing life-sustaining treatment?",
   "answer":"Ethically and legally equivalent: withdrawing treatment already started is morally equivalent to not starting it.",
   "rationale":"Established bioethics principle; the deciding factor is the patient's current values and medical futility, not the timing.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":875}],"confusable_with":""},
  {"id":"palliative-care-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What antiemetic is first-line for opioid-induced nausea and vomiting?",
   "answer":"Ondansetron (5-HT3 antagonist) or haloperidol (D2 antagonist) are commonly used first-line; metoclopramide for delayed gastric emptying-related nausea.",
   "rationale":"Opioid-induced nausea is partly mediated through dopaminergic and serotonergic pathways in the chemoreceptor trigger zone.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":870}],"confusable_with":""},
]

# ITEM 167: Peptic ulcer disease (PUD) — bleeding
topic = "Peptic ulcer disease (PUD) — bleeding"
domain = "Internal medicine: gastroenterology & hepatology (upper & lower GI bleed, acute liver failure, cirrhosis & its complications, pancreatitis, IBD, bowel obstruction, hepatic encephalopathy)"
disc = "medicine"
kps += [
  {"id":"pud-bleeding-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the most common cause of upper GI bleeding requiring hospitalization?",
   "answer":"Peptic ulcer disease (duodenal and gastric ulcers) accounts for ~50% of UGIB requiring admission.",
   "rationale":"Acid-peptic erosion of arterial vessels in ulcer bases (visible vessel sign) is responsible for major hemorrhage.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":69}],"confusable_with":"esophageal varices (second most common in cirrhotics)"},
  {"id":"pud-bleeding-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What Forrest classification identifies peptic ulcers at highest rebleeding risk requiring endoscopic hemostasis?",
   "answer":"Forrest Ia (spurting vessel) and Ib (oozing vessel) — active bleeding. Forrest IIa (visible non-bleeding vessel) — 50% rebleed risk.",
   "rationale":"Endoscopic classification guides intervention; low-risk stigmata (clean ulcer base) can be managed without endoscopic therapy.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":69}],"confusable_with":""},
  {"id":"pud-bleeding-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What pre-endoscopy infusion is given for presumed UGIB from peptic ulcer?",
   "answer":"IV PPI bolus followed by continuous infusion (e.g., pantoprazole 80 mg IV bolus then 8 mg/hour) before and after endoscopy.",
   "rationale":"High-dose PPI raises gastric pH >6, which is necessary for platelet aggregation and clot stability in the ulcer base.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":69}],"confusable_with":""},
  {"id":"pud-bleeding-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Why must H. pylori be tested and treated in peptic ulcer bleeding?",
   "answer":"H. pylori eradication dramatically reduces ulcer recurrence and rebleeding; 70-80% of duodenal ulcers are H. pylori-associated.",
   "rationale":"Treating the underlying H. pylori infection reduces 1-year rebleeding risk from ~30% to <5%.",
   "bloom":"analyze","source":[{"book":"MGH Housestaff Manual","page":68}],"confusable_with":""},
  {"id":"pud-bleeding-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Approximately what percentage of UGIB patients have no hematemesis or melena initially?",
   "answer":"Up to 15-20% of significant UGIB presents without hematemesis or melena; hematochezia from brisk UGIB is possible.",
   "rationale":"Brisk UGIB can transit rapidly and appear as hematochezia; normal initial BM does not exclude UGIB.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":69}],"confusable_with":""},
  {"id":"pud-bleeding-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the role of NGT lavage in evaluation of UGIB?",
   "answer":"NGT lavage has limited sensitivity (negative lavage does not exclude UGIB); may localize bleeding as proximal to ligament of Treitz if grossly bloody.",
   "rationale":"NGT lavage is neither sensitive nor specific; it may clear blood for better endoscopic visualization.",
   "bloom":"analyze","source":[{"book":"MGH Housestaff Manual","page":69}],"confusable_with":""},
]

# ITEM 168: Polypharmacy and medication reconciliation
topic = "Polypharmacy and medication reconciliation"
domain = "General internal medicine, preventive care & geriatrics (admission & cross-cover problems, perioperative medicine, screening & vaccination, polypharmacy & deprescribing, frailty, delirium prevention, goals of care)"
disc = "medicine"
kps += [
  {"id":"polypharmacy-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the Beer's Criteria and for whom is it designed?",
   "answer":"The American Geriatrics Society Beer's Criteria identifies potentially inappropriate medications in adults >=65 years; lists drugs to avoid or use cautiously.",
   "rationale":"Older adults have altered pharmacokinetics/dynamics; Beer's Criteria guides deprescribing to reduce ADR risk.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":170}],"confusable_with":"START/STOPP criteria (European equivalent)"},
  {"id":"polypharmacy-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Name four Beer's Criteria drug classes that increase fall risk in older adults.",
   "answer":"Benzodiazepines, anticholinergics, alpha-blockers (orthostasis), and sedating antihistamines.",
   "rationale":"These agents impair gait, coordination, alertness, and blood pressure regulation, directly increasing fall risk.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":170}],"confusable_with":""},
  {"id":"polypharmacy-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the definition of polypharmacy and at what medication count does adverse drug reaction risk increase substantially?",
   "answer":"Polypharmacy typically defined as >=5 regular medications; risk of ADRs increases substantially at >=10 medications (major polypharmacy).",
   "rationale":"Each additional medication adds potential interactions and adverse effects; risk is not linear.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":170}],"confusable_with":""},
  {"id":"polypharmacy-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Prescribing cascade: give one clinical example.",
   "answer":"Metoclopramide → parkinsonism → levodopa prescribed → worsening nausea → further prokinetic added.",
   "rationale":"Side effects of one drug are misdiagnosed as a new condition and treated with additional drugs, compounding toxicity.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":171}],"confusable_with":""},
  {"id":"polypharmacy-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What framework guides systematic deprescribing in hospitalized older adults?",
   "answer":"STOPPFrail criteria, the Screening Tool for Older Persons' Prescriptions in Frail adults, guides deprescribing.",
   "rationale":"Frail patients have limited life expectancy; preventive medications with long time-to-benefit are appropriate targets.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":171}],"confusable_with":"Beer's Criteria (avoidance) vs STOPPFrail (deprescribing)"},
  {"id":"polypharmacy-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Which commonly prescribed medications must not be abruptly stopped at hospital discharge due to withdrawal risk?",
   "answer":"Beta-blockers (rebound hypertension, angina), benzodiazepines (seizures), SSRIs (discontinuation syndrome), clonidine (hypertensive crisis), and corticosteroids (adrenal insufficiency).",
   "rationale":"Medications that suppress physiologic systems cause rebound phenomena on abrupt discontinuation.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":171}],"confusable_with":""},
]

# ITEM 169: Postoperative complications (fever, ileus, urinary retention)
topic = "Postoperative complications (fever, ileus, urinary retention)"
domain = "General internal medicine, preventive care & geriatrics (admission & cross-cover problems, perioperative medicine, screening & vaccination, polypharmacy & deprescribing, frailty, delirium prevention, goals of care)"
disc = "medicine"
kps += [
  {"id":"postop-complications-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the '5 W's' mnemonic for postoperative fever and their timeline?",
   "answer":"Wind (atelectasis/pneumonia, POD 1-2), Water (UTI, POD 3-5), Wound (infection, POD 5-7), Walking (DVT/PE, any time), Wonder drugs (drug fever, any time).",
   "rationale":"Fever within hours of surgery suggests physiologic stress or atelectasis; later fevers suggest infection.",
   "bloom":"recall","source":[{"book":"Intern Notes / Survival Guide","page":55}],"confusable_with":""},
  {"id":"postop-complications-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is postoperative ileus and how is it distinguished from small bowel obstruction?",
   "answer":"Ileus: diffuse absent bowel sounds, dilated loops throughout on X-ray, no mechanical point of obstruction, usually resolves with conservative management. SBO: hyperactive bowel sounds early, air-fluid levels, transition point on CT.",
   "rationale":"Distinguishing ileus from mechanical SBO is critical; ileus is managed conservatively while SBO may require surgery.",
   "bloom":"analyze","source":[{"book":"Intern Notes / Survival Guide","page":55}],"confusable_with":""},
  {"id":"postop-complications-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the most effective pharmacologic agent for preventing postoperative nausea and vomiting (PONV)?",
   "answer":"Ondansetron 4 mg IV at end of surgery is the most evidence-based PONV prophylaxis; combination with dexamethasone reduces risk further.",
   "rationale":"5-HT3 antagonists block serotonin in the CTZ and GI tract; combination therapy targets multiple PONV pathways.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1033}],"confusable_with":""},
  {"id":"postop-complications-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What are the primary risk factors for postoperative urinary retention (POUR)?",
   "answer":"Male sex, age >50, BPH, spinal/regional anesthesia, pelvic/anorectal surgery, and opioid use.",
   "rationale":"Bladder atony from surgery, opioids, and regional anesthetic effects impairs detrusor contraction.",
   "bloom":"recall","source":[{"book":"Intern Notes / Survival Guide","page":55}],"confusable_with":""},
  {"id":"postop-complications-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the threshold bladder volume for intervention in postoperative urinary retention?",
   "answer":"Bladder volume >500 mL on bedside ultrasound with inability to void warrants urinary catheterization.",
   "rationale":"Prolonged overdistension damages the detrusor, causing long-term dysfunction; prompt decompression preserves function.",
   "bloom":"recall","source":[{"book":"Intern Notes / Survival Guide","page":55}],"confusable_with":""},
  {"id":"postop-complications-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What early intervention reduces incidence of postoperative ileus after abdominal surgery?",
   "answer":"Early oral feeding and ambulation (enhanced recovery after surgery, ERAS); minimize opioids (use multimodal analgesia).",
   "rationale":"Gut stimulation by oral intake and ambulation restores peristalsis; opioids suppress GI motility via mu-opioid receptors.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1033}],"confusable_with":""},
]

# ITEM 170: Pulmonary embolism (PE) risk stratification
topic = "Pulmonary embolism: risk stratification"
domain = "Internal medicine: hematology & oncology (anemias, anticoagulation & reversal, VTE prophylaxis & treatment, thrombocytopenia & DIC, transfusion medicine, oncologic emergencies, neutropenic fever)"
disc = "medicine"
kps += [
  {"id":"pe-risk-stratification-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Name the three components of Virchow's triad.",
   "answer":"Venous stasis, endothelial injury, and hypercoagulability.",
   "rationale":"Virchow's triad identifies the fundamental mechanisms of thrombosis underlying DVT and PE.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":877}],"confusable_with":""},
  {"id":"pe-risk-stratification-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the Wells criteria score that makes PE likely?",
   "answer":"Wells score >4 makes PE likely; clinical signs of DVT (3 pts), PE the most likely diagnosis (3 pts), HR >100 (1.5 pts), immobilization/surgery (1.5 pts), prior VTE (1.5 pts), hemoptysis (1 pt), malignancy (1 pt).",
   "rationale":"Wells score guides the D-dimer threshold and whether to proceed directly to CTPA.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":877}],"confusable_with":"PERC rule (to rule out PE without D-dimer)"},
  {"id":"pe-risk-stratification-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What sPESI score >0 findings identify high-risk PE?",
   "answer":"Any of: age >80, cancer, chronic cardiopulmonary disease, HR >=110 bpm, SBP <100 mmHg, SaO2 <90% — each scores 1 point; any positive = high risk.",
   "rationale":"sPESI identifies PE patients with 30-day mortality risk >10% who need more intensive management.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":96}],"confusable_with":""},
  {"id":"pe-risk-stratification-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What markers of RV dysfunction elevate PE risk beyond submassive to massive?",
   "answer":"Echocardiographic RV dilation/dysfunction, elevated troponin, or BNP elevation; hemodynamic instability (SBP <90) defines massive PE.",
   "rationale":"RV failure from acute pressure overload is the primary mechanism of death in PE; biomarkers quantify RV strain.",
   "bloom":"analyze","source":[{"book":"MGH Housestaff Manual","page":96}],"confusable_with":""},
  {"id":"pe-risk-stratification-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In postoperative patients, what is the earliest time mechanical thromboprophylaxis should begin?",
   "answer":"Intermittent pneumatic compression (IPC) should begin immediately upon OR arrival or postoperatively when pharmacologic prophylaxis is not yet safe.",
   "rationale":"IPC reduces DVT by augmenting venous return and reducing stasis; no bleeding risk, unlike pharmacologic agents.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":879}],"confusable_with":""},
  {"id":"pe-risk-stratification-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Why does IPC (intermittent pneumatic compression) decrease DVT in the pelvis less than in the legs?",
   "answer":"IPC only compresses the legs; pelvic veins are not directly compressed, so pelvic DVT risk reduction requires pharmacologic prophylaxis.",
   "rationale":"Pelvic DVT is a significant source of PE after pelvic surgery; pharmacologic prophylaxis is critical in high-risk procedures.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":879}],"confusable_with":""},
]

# ITEM 171: Pulmonary embolism: treatment
topic = "Pulmonary Embolism: Treatment"
domain = "Internal medicine: pulmonology (COPD, asthma, pulmonary embolism, pneumonia, ILD, pleural effusion, pneumothorax, hypoxemic & hypercapnic respiratory failure, OSA)"
disc = "medicine"
kps += [
  {"id":"pe-treatment-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the first-line anticoagulant for acute PE in a hemodynamically stable patient without renal failure?",
   "answer":"Direct oral anticoagulants (apixaban or rivaroxaban) are first-line for non-massive PE; apixaban 10 mg BID x 7 days then 5 mg BID.",
   "rationale":"DOAC trials (EINSTEIN, AMPLIFY) showed non-inferiority to LMWH/warfarin with lower major bleeding.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":879}],"confusable_with":"warfarin (needs bridging, slower onset)"},
  {"id":"pe-treatment-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the minimum duration of anticoagulation for unprovoked PE?",
   "answer":"Minimum 3 months; indefinite anticoagulation is recommended for unprovoked or recurrent PE unless bleeding risk is prohibitive.",
   "rationale":"Unprovoked PE carries 30% recurrence rate in 5 years; extended anticoagulation substantially reduces recurrence.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":97}],"confusable_with":"provoked PE (3 months, then reassess)"},
  {"id":"pe-treatment-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the indication for systemic thrombolysis in PE?",
   "answer":"Massive PE with hemodynamic instability (SBP <90 mmHg despite resuscitation) and no absolute contraindications; tPA 100 mg IV over 2 hours.",
   "rationale":"Thrombolysis rapidly dissolves clot and restores RV function; reserved for hemodynamic instability due to bleeding risk.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":97}],"confusable_with":"submassive PE (consider CDT or surgical embolectomy)"},
  {"id":"pe-treatment-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"During emergency pulmonary embolectomy, why do patients tolerate positive-pressure ventilation poorly?",
   "answer":"The obstructed pulmonary vasculature causes fixed high PVR; positive-pressure ventilation reduces venous return and further decreases RV output.",
   "rationale":"RV is dependent on preload and sensitive to afterload; PPV increases intrathoracic pressure, dropping venous return and CO.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":880}],"confusable_with":""},
  {"id":"pe-treatment-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"When is an IVC filter indicated for PE?",
   "answer":"Absolute contraindication to anticoagulation (recent surgery, active hemorrhage) or recurrent VTE despite adequate anticoagulation.",
   "rationale":"IVC filters trap emboli but do not treat PE; anticoagulation remains the primary long-term therapy when possible.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":879}],"confusable_with":""},
  {"id":"pe-treatment-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is catheter-directed thrombolysis (CDT) and for which PE category is it considered?",
   "answer":"CDT delivers low-dose thrombolytic directly into the clot via pulmonary artery catheter; considered for submassive PE with RV dysfunction and high systemic thrombolysis bleeding risk.",
   "rationale":"CDT reduces thrombolytic dose and systemic bleeding risk while achieving local clot dissolution.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":97}],"confusable_with":"systemic thrombolysis (massive PE only)"},
]

# ITEM 172: Pulmonary embolism: diagnosis and treatment (hematology domain)
topic = "Pulmonary embolism: diagnosis and treatment"
domain = "Internal medicine: hematology & oncology (anemias, anticoagulation & reversal, VTE prophylaxis & treatment, thrombocytopenia & DIC, transfusion medicine, oncologic emergencies, neutropenic fever)"
disc = "medicine"
kps += [
  {"id":"pe-dx-treatment-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the sensitivity and specificity of D-dimer for PE, and when should it be ordered?",
   "answer":"D-dimer: sensitivity ~95-97%, specificity ~40-50%. Use only in low-to-intermediate pre-test probability; high probability requires CTPA directly.",
   "rationale":"D-dimer has a high negative predictive value but is non-specific; elevated D-dimer requires imaging confirmation.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":95}],"confusable_with":""},
  {"id":"pe-dx-treatment-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What EKG finding is classically associated with acute PE but has low sensitivity?",
   "answer":"S1Q3T3 pattern (S wave in I, Q wave in III, inverted T in III); sinus tachycardia is the most common actual finding.",
   "rationale":"S1Q3T3 reflects acute RV strain but occurs in <20% of PE; new right bundle branch block or sinus tachycardia are more common.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":95}],"confusable_with":""},
  {"id":"pe-dx-treatment-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the gold standard imaging for acute PE diagnosis?",
   "answer":"CT pulmonary angiography (CTPA) with sensitivity ~96% and specificity ~97%.",
   "rationale":"CTPA directly visualizes clot in pulmonary arteries and rules in or out PE with high accuracy.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":95}],"confusable_with":"V/Q scan (alternative in renal failure, contrast allergy, pregnancy)"},
  {"id":"pe-dx-treatment-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"How is amniotic fluid embolism distinguished from PE at presentation?",
   "answer":"AFE: acute respiratory failure + cardiovascular collapse + DIC ± altered mental status/seizures; lacks clot on CTPA. PE: hypoxemia, RV strain, clot on CTPA, without DIC.",
   "rationale":"AFE triggers complement and coagulation cascades with DIC; PE does not primarily cause DIC.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1424}],"confusable_with":""},
  {"id":"pe-dx-treatment-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In fat embolism syndrome (FES) following orthopedic trauma, what is the classic timing of onset?",
   "answer":"1-3 days after the precipitating fracture (especially long bone or pelvis).",
   "rationale":"Fat emboli travel via venous circulation; lung inflammation and systemic petechiae develop over 24-72 hours.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1298}],"confusable_with":"PE (earlier onset, no petechiae)"},
  {"id":"pe-dx-treatment-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the role of heparin in PE treatment and why is unfractionated heparin preferred in some scenarios?",
   "answer":"UFH preferred when thrombolysis is planned (short half-life, easily reversed), in renal failure (LMWH accumulates), and when rapid anticoagulation titration is needed.",
   "rationale":"UFH is renally independent, reversible with protamine, and its activity can be rapidly adjusted.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":97}],"confusable_with":"LMWH (preferred for most stable PE)"},
]

# ITEM 173: Respiratory acid-base disorders
topic = "Respiratory acid-base disorders"
domain = "Internal medicine: pulmonology (COPD, asthma, pulmonary embolism, pneumonia, ILD, pleural effusion, pneumothorax, hypoxemic & hypercapnic respiratory failure, OSA)"
disc = "medicine"
kps += [
  {"id":"resp-acid-base-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What renal compensation occurs in chronic respiratory acidosis and what is the expected HCO3- rise?",
   "answer":"Renal bicarbonate retention: HCO3- rises 3.5 mEq/L per 10 mmHg rise in PaCO2 (chronic) vs. 1 mEq/L per 10 mmHg (acute).",
   "rationale":"Chronic retention of CO2 drives renal H+ secretion and HCO3- generation over 3-5 days.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1860}],"confusable_with":"acute respiratory acidosis (less compensation)"},
  {"id":"resp-acid-base-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In a patient with COPD and chronic hypercapnia (PaCO2 60, pH 7.38), what will happen if you correct PaCO2 to 40 rapidly?",
   "answer":"Post-hypercapnic metabolic alkalosis: renal HCO3- will not normalize quickly; acute drop in PaCO2 leaves retained bicarbonate, causing alkalemia.",
   "rationale":"Renal HCO3- correction lags behind respiratory correction by days; rapid normalization of PaCO2 unmasks metabolic alkalosis.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1860}],"confusable_with":""},
  {"id":"resp-acid-base-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What expected PaCO2 confirms adequate respiratory compensation in metabolic alkalosis?",
   "answer":"Expected PaCO2 = 0.7 × HCO3- + 21 ± 2 (Winters' equivalent for alkalosis).",
   "rationale":"Respiratory compensation for metabolic alkalosis is limited because hypoventilation raises PaCO2 but risks hypoxemia.",
   "bloom":"apply","source":[{"book":"Intern Notes / Survival Guide","page":12}],"confusable_with":""},
  {"id":"resp-acid-base-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"A patient on mechanical ventilation has pH 7.52, PaCO2 28, HCO3- 22. What is the diagnosis?",
   "answer":"Primary acute respiratory alkalosis (low PaCO2, elevated pH); HCO3- expected = 24 - 2×(40-28)/10 = 24-2.4 ≈ 21.6. Consistent with acute respiratory alkalosis.",
   "rationale":"Common in mechanically ventilated patients if minute ventilation is too high; can cause cerebral vasoconstriction.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1860}],"confusable_with":""},
  {"id":"resp-acid-base-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What are two common causes of mixed metabolic alkalosis and respiratory acidosis?",
   "answer":"COPD exacerbation with vomiting, or diuretic use in a COPD patient retaining CO2.",
   "rationale":"Metabolic alkalosis (hypokalemia + diuretics/vomiting) occurs concurrently with respiratory acidosis in COPD.",
   "bloom":"analyze","source":[{"book":"Intern Notes / Survival Guide","page":12}],"confusable_with":""},
  {"id":"resp-acid-base-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What effect does permissive hypercapnia have on oxyhemoglobin dissociation (and is this beneficial or harmful)?",
   "answer":"Hypercapnia shifts the OHD curve rightward (Bohr effect), reducing O2 affinity and improving O2 delivery to tissues — generally beneficial in ARDS management.",
   "rationale":"Lower pH reduces hemoglobin's O2 affinity; tissue oxygenation is maintained even with reduced SaO2.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1638}],"confusable_with":""},
]

# ITEM 174: STEMI
topic = "STEMI: Diagnosis and Acute Management"
domain = "Internal medicine: cardiology (ACS, stable & unstable angina, heart failure, brady/tachyarrhythmias, valvular disease, hypertension & emergencies, lipids, syncope)"
disc = "medicine"
kps += [
  {"id":"stemi-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the maximum acceptable door-to-balloon time for primary PCI in STEMI?",
   "answer":"Door-to-balloon time should be <=90 minutes; fibrinolysis should be given within 30 minutes if PCI is not available within 120 minutes.",
   "rationale":"Myocardium salvaged is directly proportional to time to reperfusion; guideline-mandated times reduce infarct size and mortality.",
   "bloom":"recall","source":[{"book":"StatPearls","page":1}],"confusable_with":"NSTEMI (no similar time target)"},
  {"id":"stemi-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What ECG criteria define STEMI requiring immediate reperfusion?",
   "answer":"New ST elevation >=1 mm in >=2 contiguous limb leads or >=2 mm in >=2 contiguous precordial leads; new LBBB with concordant ST changes.",
   "rationale":"ST elevation indicates complete coronary occlusion with transmural ischemia; immediate reperfusion halts ongoing necrosis.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2137}],"confusable_with":"LV aneurysm (persistent ST elevation, no acute troponin rise)"},
  {"id":"stemi-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the prehospital triage strategy for suspected STEMI when transfer time to PCI-capable center is <120 minutes?",
   "answer":"Bypass non-PCI hospitals and transport directly to PCI center; administer aspirin, heparin, and P2Y12 inhibitor en route.",
   "rationale":"Direct transfer avoids delays from secondary inter-hospital transfer and maximizes benefit of primary PCI.",
   "bloom":"recall","source":[{"book":"StatPearls","page":1}],"confusable_with":""},
  {"id":"stemi-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What absolute contraindications exist for thrombolysis in STEMI?",
   "answer":"Prior intracranial hemorrhage, known intracranial neoplasm, ischemic stroke in past 3 months, active internal bleeding, suspected aortic dissection, significant head trauma <3 months.",
   "rationale":"Contraindications reflect hemorrhagic risk from systemic fibrinolysis that outweighs reperfusion benefit.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":37}],"confusable_with":""},
  {"id":"stemi-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In perioperative STEMI, what makes diagnosis difficult and what is the primary diagnostic tool?",
   "answer":"Perioperative ECG changes may be obscured by baseline abnormalities; troponin serial measurements are the primary diagnostic tool.",
   "rationale":"Regional and general anesthetics mask pain symptoms; ECG monitoring is limited; troponin elevation confirms myocardial injury.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":2137}],"confusable_with":""},
  {"id":"stemi-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the mortality rate of acute MI overall, and how much has in-hospital mortality been reduced with contemporary PCI?",
   "answer":"Overall mortality ~25%; with contemporary interventional cardiology, in-hospital mortality reduced to <10%.",
   "rationale":"Primary PCI dramatically reduces infarct size and mechanical complications; pharmacologic therapy further lowers mortality.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2137}],"confusable_with":""},
]

with open("data/kp_batch3_out.json", "w", encoding="utf-8") as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)

print("Items:", len(kps))
