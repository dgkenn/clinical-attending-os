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
dis = 'medicine'

# ============================================================
# [53] Acute Cholecystitis & Choledocholithiasis
# ============================================================
t = 'Acute Cholecystitis & Choledocholithiasis'
kps += [
  {
    'id': 'acute-cholecystitis-choledocholithiasis-1',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'What is the typical pattern of LFT elevation in choledocholithiasis vs hepatocellular disease?',
    'answer': 'Choledocholithiasis: alkaline phosphatase, bilirubin, and GGT exceed AST/ALT elevations (cholestatic pattern). Normal LFTs help exclude choledocholithiasis; positive predictive value of elevated LFTs alone is poor.',
    'rationale': 'Common bile duct obstruction impairs biliary excretion preferentially; hepatocellular injury raises aminotransferases (AST/ALT) more than cholestatic markers.',
    'bloom': 'analyze',
    'source': [{'book': 'StatPearls', 'page': 4}],
    'confusable_with': 'Acute hepatitis — transaminase-dominant elevation; choledocholithiasis is cholestasis-dominant'
  },
  {
    'id': 'acute-cholecystitis-choledocholithiasis-2',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'What are the three serious complications of untreated choledocholithiasis?',
    'answer': 'Obstructive jaundice, pancreatitis (gallstone pancreatitis), and cholangitis (ascending biliary infection with Charcot triad: fever, jaundice, RUQ pain).',
    'rationale': 'Stones impacted at the ampulla of Vater obstruct the pancreatic duct (pancreatitis) and bile duct (jaundice); static bile becomes infected (cholangitis).',
    'bloom': 'recall',
    'source': [{'book': 'StatPearls', 'page': 2}],
    'confusable_with': 'Cholelithiasis (gallstones in GB) — most patients asymptomatic; only ~20% develop clinical events'
  },
  {
    'id': 'acute-cholecystitis-choledocholithiasis-3',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'What is the procedure of choice for removing CBD stones, and how is it performed?',
    'answer': 'ERCP with sphincterotomy: the papilla is cut with cautery to enlarge the ampulla of Vater, then stones are removed with snares/baskets or swept out with a balloon catheter.',
    'rationale': 'The endoscopic approach accesses the CBD via the duodenum without surgery; sphincterotomy relieves the obstructing anatomy to allow stone passage or extraction.',
    'bloom': 'recall',
    'source': [{'book': 'StatPearls', 'page': 5}],
    'confusable_with': 'Laparoscopic cholecystectomy — removes the gallbladder (source) but does not remove CBD stones'
  },
  {
    'id': 'acute-cholecystitis-choledocholithiasis-4',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'What is the approximate proportion of choledocholithiasis patients who remain asymptomatic, and what is the risk for those who refuse surgery?',
    'answer': 'Approximately 45% remain asymptomatic. Of those who refuse surgery, only 55% experience varying degrees of disease progression over follow-up.',
    'rationale': 'Not all CBD stones cause complications; risk stratification using clinical and biochemical predictors guides urgency of intervention.',
    'bloom': 'recall',
    'source': [{'book': 'StatPearls', 'page': 6}],
    'confusable_with': 'Cholelithiasis prognosis — similar asymptomatic proportion but lower complication risk than CBD stones'
  },
  {
    'id': 'acute-cholecystitis-choledocholithiasis-5',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'A patient with RUQ pain has normal liver tests. What does this effectively exclude?',
    'answer': 'Normal LFTs effectively exclude choledocholithiasis as the cause of biliary symptoms — normal levels rule against common bile duct stones.',
    'rationale': 'Even partial CBD obstruction produces detectable LFT abnormalities; completely normal LFTs make choledocholithiasis unlikely and shift diagnosis toward cystic duct obstruction (cholecystitis) or biliary colic.',
    'bloom': 'apply',
    'source': [{'book': 'StatPearls', 'page': 4}],
    'confusable_with': 'Acute cholecystitis — presents with abnormal LFTs only if secondary cholangitis; isolated cystic duct obstruction keeps LFTs near-normal'
  },
]

kps.append({
    '_type': 'illness_script',
    'topic': 'Acute Cholecystitis & Choledocholithiasis',
    'discipline': 'medicine',
    'enabling_conditions': 'Female sex, obesity, pregnancy, age >40 (cholesterol stones); hemolytic disorders, Crohn disease, ileal disease (pigment stones); rapid weight loss; prolonged fasting (biliary sludge)',
    'pathophysiology': 'Gallstones migrate to CBD via cystic duct; impaction at ampulla of Vater causes obstruction, biliary stasis, bacterial proliferation, and inflammation',
    'time_course': 'Biliary colic: 30 min-6 h, self-resolving; cholecystitis: >6 h with fever; cholangitis: rapid onset with sepsis features',
    'key_features': 'RUQ/epigastric pain (postprandial), Murphy sign (inspiratory arrest on RUQ palpation), jaundice, fever; Charcot triad = cholangitis; Reynolds pentad (+ shock + AMS) = suppurative cholangitis',
    'consequence_if_missed': 'Ascending cholangitis with gram-negative sepsis; gallstone pancreatitis; liver abscess; perforation with biliary peritonitis'
})

# ============================================================
# [54] Acute Respiratory Failure
# ============================================================
t = 'Acute Respiratory Failure'
kps += [
  {
    'id': 'acute-respiratory-failure-1',
    'topic': t, 'domain': dom_icu, 'discipline': dis,
    'stem': 'What are the key symptoms of respiratory distress (as distinct from dyspnea), and why must RR be measured directly?',
    'answer': 'Respiratory distress: tachypnea (RR>=20 — measure yourself, do not rely on charted values), cyanosis (SpO2 <80%), increased work of breathing (nasal flaring, retractions, grunting, tripoding, diaphoresis), and obstruction (wheezing, stridor).',
    'rationale': 'Respiratory rate is the earliest and most sensitive sign of deterioration but is systematically under-measured and inaccurately charted in hospitals.',
    'bloom': 'recall',
    'source': [{'book': 'MGH Housestaff Manual', 'page': 46}],
    'confusable_with': 'Dyspnea alone — subjective sensation; distress requires objective signs of increased work of breathing'
  },
  {
    'id': 'acute-respiratory-failure-2',
    'topic': t, 'domain': dom_icu, 'discipline': dis,
    'stem': 'What SpO2 targets are recommended for patients at risk of hypercapnic respiratory failure (COPD, OHS, neuromuscular)?',
    'answer': 'Target SpO2 88-92% (resulting in PaO2 50-70 mmHg) to avoid hypoxic drive suppression and CO2 retention; avoid high-flow O2 in these patients.',
    'rationale': 'Patients with chronic hypercapnia rely partly on hypoxic drive; excessive O2 suppresses ventilatory drive, worsens CO2 retention, and causes V/Q mismatch.',
    'bloom': 'apply',
    'source': [{'book': 'MGH Housestaff Manual', 'page': 48}],
    'confusable_with': 'SpO2 target 91-96% for general critical illness — higher target acceptable in non-hypercapnic patients'
  },
  {
    'id': 'acute-respiratory-failure-3',
    'topic': t, 'domain': dom_icu, 'discipline': dis,
    'stem': 'ARDS lung-protective ventilation: what are the two key pressure and volume parameters?',
    'answer': 'Tidal volume <=6 mL/kg predicted body weight AND plateau pressure <30 cmH2O; higher PEEP is also used. These limits prevent volutrauma and barotrauma.',
    'rationale': 'In ARDS, non-aerated regions collapse while aerated regions are small; high tidal volumes overdistend compliant regions causing ventilator-induced lung injury.',
    'bloom': 'recall',
    'source': [{'book': 'Miller/Baby Miller', 'page': 766}],
    'confusable_with': 'Standard ICU ventilation — tidal volumes of 8-10 mL/kg were historical standard; now known to worsen ARDS'
  },
  {
    'id': 'acute-respiratory-failure-4',
    'topic': t, 'domain': dom_icu, 'discipline': dis,
    'stem': 'Auto-PEEP (dynamic hyperinflation) in a ventilated patient: how is it detected and what are the hemodynamic consequences?',
    'answer': 'Detected by end-expiratory hold (auto-PEEP = end-expiratory pressure minus set PEEP) with flow >0 at end expiration. Causes: decreased venous return (hypotension), alveolar overdistention (volutrauma/barotrauma), and increased work to trigger the ventilator.',
    'rationale': 'Incomplete exhalation traps gas, raising intrinsic PEEP; the resulting increased intrathoracic pressure impedes venous return and cardiac output.',
    'bloom': 'analyze',
    'source': [{'book': 'MGH Housestaff Manual', 'page': 58}],
    'confusable_with': 'Tension pneumothorax — also causes hypotension with elevated airway pressures; distinguished by tracheal deviation and unilateral breath sounds'
  },
  {
    'id': 'acute-respiratory-failure-5',
    'topic': t, 'domain': dom_icu, 'discipline': dis,
    'stem': 'Venovenous ECMO is used for what type of respiratory failure, and what cardiac function does it require?',
    'answer': 'VV-ECMO manages hypoxemic respiratory failure (e.g., severe ARDS); it replaces pulmonary function only and requires intact native cardiac output to distribute oxygenated blood.',
    'rationale': 'VV circuit oxygenates and removes CO2 from venous blood before returning it to the venous system; the patient\'s heart must still pump oxygenated blood to tissues.',
    'bloom': 'recall',
    'source': [{'book': 'MGH Housestaff Manual', 'page': 61}],
    'confusable_with': 'VA-ECMO — replaces both heart and lungs; used in cardiogenic shock where cardiac output is insufficient'
  },
]

kps.append({
    '_type': 'confusable_pair',
    'topic_a': 'Venovenous ECMO (VV-ECMO)',
    'topic_b': 'Venoarterial ECMO (VA-ECMO)',
    'discriminator': 'VV-ECMO: replaces lungs only (hypoxemic resp failure) — needs intact cardiac output. VA-ECMO: replaces heart + lungs (cardiogenic shock) — arterial reinfusion bypasses heart'
})

print('Batch 6 KPs:', len(kps))
with open('data/_kp_part2_batch6.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print('Written.')
