import json

kps = []
dom_onc = 'Internal medicine: on-call & cross-cover (approach to the acutely changing ward patient)'
dom_icu = 'Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)'
dom_em = 'Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)'
dom_endo = 'Internal medicine: endocrinology (diabetes & inpatient glucose, DKA & HHS, thyroid disorders & storm, adrenal insufficiency, calcium disorders, pituitary)'
dom_neuro = 'Internal medicine: neurology (ischemic & hemorrhagic stroke, seizures & status epilepticus, altered mental status & delirium, headache, neuromuscular weakness, spinal cord syndromes)'
dom_geri = 'General internal medicine, preventive care & geriatrics (admission & cross-cover problems, perioperative medicine, screening & vaccination, polypharmacy & deprescribing, frailty, delirium prevention, goals of care)'
dom_id = 'Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)'
dom_pulm = 'Internal medicine: pulmonology (COPD, asthma, pulmonary embolism, pneumonia, ILD, pleural effusion, pneumothorax, hypoxemic & hypercapnic respiratory failure, OSA)'
dom_rheum = 'Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)'
dis = 'medicine'

# ============================================================
# [58] Altered Mental Status (AMS): Approach & Differential
# ============================================================
t = 'Altered Mental Status (AMS): Approach & Differential'
kps += [
  {
    'id': 'ams-approach-1',
    'topic': t, 'domain': dom_neuro, 'discipline': dis,
    'stem': 'What toxic alcohol causes AMS with blurry vision, dilated pupils, papilledema, and an elevated osmolar gap with HAGMA?',
    'answer': 'Methanol — metabolized to formic acid; presents with AMS, blurry vision ("snowfield"), dilated pupils, papilledema. Coexistence of HAGMA with elevated osmolar gap (>10 mOsm/kg) is highly suggestive of toxic alcohol.',
    'rationale': 'Formic acid inhibits cytochrome oxidase causing optic nerve toxicity and systemic acidosis; the intact methanol creates an osmolar gap before metabolism.',
    'bloom': 'apply',
    'source': [{'book': 'StatPearls', 'page': 8}],
    'confusable_with': 'Ethylene glycol — also causes HAGMA + osmolar gap but targets kidneys (oxalate crystals), not optic nerve'
  },
  {
    'id': 'ams-approach-2',
    'topic': t, 'domain': dom_neuro, 'discipline': dis,
    'stem': 'What formula calculates serum osmolality, and what is the normal osmolar gap?',
    'answer': 'Calculated osmolality = 2x(Na+K) + (glucose/18) + (BUN/2.8) + (ethanol/4.6). Normal osmolar gap <10 mOsm/kg; elevation >10 suggests exogenous osmoles (methanol, ethylene glycol, isopropanol).',
    'rationale': 'Measured osmolality (freezing point depression) minus calculated value reveals unmeasured osmotically active substances not accounted for in the formula.',
    'bloom': 'apply',
    'source': [{'book': 'StatPearls', 'page': 8}],
    'confusable_with': 'Anion gap calculation — different formula; osmolar gap focuses on unmeasured osmoles, not unmeasured anions'
  },
  {
    'id': 'ams-approach-3',
    'topic': t, 'domain': dom_neuro, 'discipline': dis,
    'stem': 'Hypercalcemia presents with what neurological manifestations?',
    'answer': 'Hypercalcemia causes syncope, arrhythmias, and altered mental status (among other systemic effects).',
    'rationale': 'Hypercalcemia depresses neuronal excitability (membrane stabilization effect) and impairs synaptic transmission, causing confusion, lethargy, and in severe cases coma.',
    'bloom': 'recall',
    'source': [{'book': 'StatPearls', 'page': 7}],
    'confusable_with': 'Hyponatremia-related AMS — also causes confusion but via different mechanism (cerebral edema); both present similarly'
  },
  {
    'id': 'ams-approach-4',
    'topic': t, 'domain': dom_neuro, 'discipline': dis,
    'stem': 'In evaluating AMS in a hyponatremic patient, what clinical detail distinguishes acute from chronic hyponatremia?',
    'answer': 'Acute hyponatremia (<48 hours): seizures and severe neurological symptoms are common and potentially life-threatening. Chronic hyponatremia (>48 hours): brain has adapted; correction must be slow (<8-10 mEq/L per day) to avoid osmotic demyelination.',
    'rationale': 'Chronic hyponatremia causes cells to extrude organic osmolytes (adaptation); rapid correction creates an osmotic gradient drawing water out of brain cells, causing osmotic demyelination syndrome.',
    'bloom': 'analyze',
    'source': [{'book': 'Intern Notes / Survival Guide', 'page': 17}],
    'confusable_with': 'Acute hyponatremia correction speed — can correct faster (up to 1-2 mEq/L/h) in symptomatic acute cases'
  },
  {
    'id': 'ams-approach-5',
    'topic': t, 'domain': dom_neuro, 'discipline': dis,
    'stem': 'In a postoperative patient with prolonged somnolence, what does a pertinent review focus on to solve the diagnostic dilemma?',
    'answer': 'Review medical and surgical history, history of drug ingestions, physical examination, laboratory results, and perioperative anesthetic management including all drugs given.',
    'rationale': 'Postoperative AMS has a broad differential (residual anesthetics, metabolic, structural, drug interactions); systematic review narrows the cause efficiently.',
    'bloom': 'apply',
    'source': [{'book': 'Morgan & Mikhail', 'page': 351}],
    'confusable_with': 'MH presenting as AMS — unusual; more typically presents with hyperthermia and rigidity, not somnolence'
  },
]

# ============================================================
# [59] Altered mental status & acute delirium on the wards
# ============================================================
t = 'Altered mental status & acute delirium on the wards'
kps += [
  {
    'id': 'delirium-wards-1',
    'topic': t, 'domain': dom_geri, 'discipline': dis,
    'stem': 'What are the three subtypes of delirium and which carries the worst prognosis?',
    'answer': 'Hyperactive (agitated), hypoactive (quiet, easily missed), and mixed. Hypoactive delirium carries the worst prognosis — frequently undetected and associated with higher mortality.',
    'rationale': 'Hypoactive delirium resembles sedation or depression; without formal screening (CAM), it goes unrecognized and untreated, leading to prolonged delirium and complications.',
    'bloom': 'recall',
    'source': [{'book': 'Miller/Baby Miller', 'page': 682}],
    'confusable_with': 'Emergence delirium — occurs earlier (pre-PACU or at PACU arrival) vs postoperative delirium which develops in PACU or later'
  },
  {
    'id': 'delirium-wards-2',
    'topic': t, 'domain': dom_geri, 'discipline': dis,
    'stem': 'What validated tool is used to diagnose delirium formally in the hospital setting?',
    'answer': 'The Confusion Assessment Method (CAM); also the Riker Sedation Agitation Scale for ICU patients. CAM requires acute onset + fluctuating course + inattention PLUS either disorganized thinking or altered consciousness.',
    'rationale': 'Clinical impression alone misses hypoactive delirium in >70% of cases; CAM provides sensitivity ~94% and specificity ~89% in trained raters.',
    'bloom': 'recall',
    'source': [{'book': 'Miller/Baby Miller', 'page': 682}],
    'confusable_with': 'Mini-Mental State Examination (MMSE) — assesses cognition but not specifically delirium diagnosis'
  },
  {
    'id': 'delirium-wards-3',
    'topic': t, 'domain': dom_geri, 'discipline': dis,
    'stem': 'In a ventilated ARDS patient with rising peak airway pressures and new arterial hypotension, what must be immediately excluded?',
    'answer': 'Tension pneumothorax — high intrathoracic pressure impedes venous return causing hypotension; suspect when peak airway pressure rises along with hemodynamic collapse, especially if concurrent with PEEP increase.',
    'rationale': 'PEEP and overdistended lungs can both rupture alveoli; in ventilated patients, the high pressure can prevent lung from re-expanding after air leak.',
    'bloom': 'apply',
    'source': [{'book': 'Miller/Baby Miller', 'page': 380}],
    'confusable_with': 'Auto-PEEP — also raises airway pressure and causes hypotension via venous return impairment, but without unilateral breath sound change'
  },
  {
    'id': 'delirium-wards-4',
    'topic': t, 'domain': dom_geri, 'discipline': dis,
    'stem': 'TRALI (transfusion-related acute lung injury) presents how, and what is its leading cause among transfusion mortalities?',
    'answer': 'TRALI: dyspnea, hypoxemia, hypotension, fever, and pulmonary edema 4-6 hours after transfusion of plasma-containing products (platelets/FFP > pRBCs); 5-10% mortality. It is the leading cause of transfusion-related mortality.',
    'rationale': 'Donor antibodies react with recipient leukocyte antigens, activating neutrophils and damaging pulmonary endothelium; management is supportive (O2, mechanical ventilation).',
    'bloom': 'recall',
    'source': [{'book': 'Stanford CA-1', 'page': 52}],
    'confusable_with': 'TACO (transfusion-associated circulatory overload) — also causes pulmonary edema but is cardiogenic; responds to diuretics; BNP elevated'
  },
]

kps.append({
    '_type': 'confusable_pair',
    'topic_a': 'TRALI',
    'topic_b': 'TACO (transfusion-associated circulatory overload)',
    'discriminator': 'TRALI: non-cardiogenic pulmonary edema 4-6h post-transfusion; donor Ab to recipient leukocytes; normal CVP/BNP; treat supportively. TACO: cardiogenic pulmonary edema; elevated BNP/CVP; responds to diuretics'
})

# ============================================================
# [60] Anaphylaxis
# ============================================================
t = 'Anaphylaxis'
kps += [
  {
    'id': 'anaphylaxis-1',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'More than 90% of intraoperative allergic reactions occur within what time frame, and what makes identification of the causative agent difficult?',
    'answer': 'More than 90% occur within 3 minutes of drug administration; identification is difficult because multiple drugs are given simultaneously early in anesthesia (antibiotics, NMBAs, induction agents).',
    'rationale': 'Temporal proximity to multiple concurrent drug exposures means cause-effect cannot be attributed without specific allergy testing post-event.',
    'bloom': 'recall',
    'source': [{'book': 'Stanford CA-1', 'page': 78}],
    'confusable_with': 'Delayed reactions (hours later) — possible but far less common; more typical of latex or contrast media'
  },
  {
    'id': 'anaphylaxis-2',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'What is the mortality rate of intraoperative anaphylaxis, and what is the most common cause?',
    'answer': 'Mortality approximately 3.4%. NMBAs are a prominent cause (account for a large fraction of anesthetic allergic reactions); rocuronium and succinylcholine are most common.',
    'rationale': 'NMBAs are typically the first drug given after induction and have the most potent IgE-mediated reaction potential; cross-reactivity between NMBAs exists.',
    'bloom': 'recall',
    'source': [{'book': 'Stanford CA-1', 'page': 78}],
    'confusable_with': 'Antibiotic anaphylaxis — often given immediately after NMBA; distinguishing requires timing and allergy testing'
  },
  {
    'id': 'anaphylaxis-3',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'In children undergoing surgery with a history of latex allergy risk factors, what is the preferred scheduling approach?',
    'answer': 'Schedule the patient as the first case of the day in a latex-free environment; remove latex gloves and replace tops of multi-dose vials (contain latex). Risk factors: healthcare workers, children with spina bifida, urogenital abnormalities, food allergies (tropical fruits, chestnuts).',
    'rationale': 'First-case latex-free OR minimizes aerosolized latex from prior cases; latex proteins persist in OR air for hours after latex glove use.',
    'bloom': 'apply',
    'source': [{'book': 'Stanford CA-1', 'page': 79}],
    'confusable_with': 'Latex-safe (not latex-free) environment — incomplete; latex-free is required for high-risk patients'
  },
  {
    'id': 'anaphylaxis-4',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'What dose of epinephrine is safe to administer during anesthesia with halothane, and what is the limit with non-sensitizing agents?',
    'answer': 'Halothane sensitizes the heart to epinephrine arrhythmias: limit to 1.5 mcg/kg. With non-sensitizing agents (desflurane, isoflurane, sevoflurane): up to 4.5 mcg/kg is safe.',
    'rationale': 'Halothane increases myocardial automaticity and sensitizes the myocardium to catecholamines; newer volatile agents have minimal sensitizing effect.',
    'bloom': 'recall',
    'source': [{'book': 'Morgan & Mikhail', 'page': 265}],
    'confusable_with': 'Anaphylaxis epinephrine dosing — 0.3-0.5 mg IM (300-500 mcg) for anaphylaxis, separate from local infiltration limits'
  },
]

print('Batch 8 KPs:', len(kps))
with open('data/_kp_part2_batch8.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print('Written.')
