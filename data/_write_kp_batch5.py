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
# [50] ACLS & Cardiac Arrest
# ============================================================
t = 'ACLS & Cardiac Arrest'
kps += [
  {
    'id': 'acls-cardiac-arrest-1',
    'topic': t, 'domain': dom_icu, 'discipline': dis,
    'stem': 'What change was made to resuscitation sequencing in the 2010 AHA guidelines, and what is the rationale?',
    'answer': 'Sequence changed from ABC (airway-breathing-compression) to CAB (compression first). Chest compressions maintain coronary and cerebral perfusion — delay increases ischemia; most cardiac arrest patients have sufficient residual O2 for 2-3 minutes.',
    'rationale': 'Time to first compression is the strongest predictor of ROSC; pausing for airway before compressions wastes critical time during VF/VT.',
    'bloom': 'recall',
    'source': [{'book': 'Morgan & Mikhail', 'page': 2056}],
    'confusable_with': 'Respiratory arrest algorithm — airway IS the first priority when the primary problem is apnea not cardiac'
  },
  {
    'id': 'acls-cardiac-arrest-2',
    'topic': t, 'domain': dom_icu, 'discipline': dis,
    'stem': 'What EtCO2 value after 20 minutes in an intubated cardiac arrest patient suggests low likelihood of ROSC?',
    'answer': 'EtCO2 persistently <10 mmHg after 20 minutes in an intubated patient predicts low likelihood of ROSC and may inform decision to cease resuscitation. This does NOT apply to non-intubated patients.',
    'rationale': 'EtCO2 reflects pulmonary blood flow and thus cardiac output during CPR; persistently low values indicate inadequate perfusion despite resuscitation.',
    'bloom': 'apply',
    'source': [{'book': 'Morgan & Mikhail', 'page': 2057}],
    'confusable_with': 'EtCO2 during CPR as quality marker — high EtCO2 indicates good compressions; low suggests inadequate technique OR futility'
  },
  {
    'id': 'acls-cardiac-arrest-3',
    'topic': t, 'domain': dom_icu, 'discipline': dis,
    'stem': 'Vasopressin was removed from ACLS guidelines in 2015. Why?',
    'answer': 'Vasopressin offered no advantage over epinephrine alone or in combination; its removal simplified the algorithm without evidence of harm or benefit from inclusion.',
    'rationale': 'Multiple RCTs failed to show improved ROSC or survival with vasopressin; epinephrine remains the sole recommended vasopressor in cardiac arrest.',
    'bloom': 'recall',
    'source': [{'book': 'Miller/Baby Miller', 'page': 844}],
    'confusable_with': 'Vasopressin in septic shock — still has a role as adjunct to norepinephrine'
  },
  {
    'id': 'acls-cardiac-arrest-4',
    'topic': t, 'domain': dom_icu, 'discipline': dis,
    'stem': 'During CPR, what rate and depth of chest compressions are recommended, and why must the sternum fully recoil?',
    'answer': 'Rate >=100/min; depth 1.5-2 inches (4-5 cm); full recoil between compressions is required to allow venous return and ventricular filling.',
    'rationale': 'Incomplete recoil prevents ventricular preload recovery; adequate depth generates sufficient coronary and cerebral perfusion pressure.',
    'bloom': 'recall',
    'source': [{'book': 'Marino ICU Book', 'page': 208}],
    'confusable_with': 'AHA 2020 update: depth 2-2.4 inches (5-6 cm) for adults — avoid >2.4 inches (rib fractures)'
  },
  {
    'id': 'acls-cardiac-arrest-5',
    'topic': t, 'domain': dom_icu, 'discipline': dis,
    'stem': 'ACLS drugs are associated with ROSC but not with what two more clinically meaningful outcomes?',
    'answer': 'ACLS drugs are associated with ROSC but NOT with improved survival to hospital discharge or improved neurologic recovery.',
    'rationale': 'Epinephrine and other vasopressors may restart the heart but cause post-resuscitation myocardial dysfunction and vasoconstriction that limits neurologically intact survival.',
    'bloom': 'analyze',
    'source': [{'book': 'Miller/Baby Miller', 'page': 844}],
    'confusable_with': 'High-quality CPR — strongly associated with both ROSC AND neurologically intact survival'
  },
]

# ============================================================
# [51] ACLS: Non-Shockable Rhythms (PEA & Asystole)
# ============================================================
t = 'ACLS: Non-Shockable Rhythms (PEA & Asystole)'
kps += [
  {
    'id': 'acls-nonshockable-1',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'List the 8 Hs and 8 Ts for reversible causes of cardiac arrest (PEA/asystole).',
    'answer': '8 Hs: Hypoxia, Hypovolemia, Hydrogen ion (acidosis), Hypo/Hyperkalemia, Hypothermia, Hypoglycemia, plus two perioperative additions (Malignant hyperthermia, QT prolongation). 8 Ts: Toxins/anaphylaxis, Tension pneumothorax, Thrombosis (coronary), Thrombus (pulmonary), plus Hypervagal response, Pulmonary hypertension.',
    'rationale': 'PEA/asystole are non-shockable; survival depends entirely on identifying and correcting a reversible cause — defibrillation provides no benefit.',
    'bloom': 'recall',
    'source': [{'book': 'Miller/Baby Miller', 'page': 843}],
    'confusable_with': 'VF/VT (shockable) — defibrillation is first-line; H&T still apply but shock is concurrent'
  },
  {
    'id': 'acls-nonshockable-2',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'What is the cornerstone of ACLS delivery for non-shockable rhythms?',
    'answer': 'High-quality chest compressions — the cornerstone of neurologically intact survival. Performed at correct rate and depth with complete recoil and minimal interruptions.',
    'rationale': 'Compressions maintain cardiac output and coronary perfusion pressure; even brief pauses reduce aortic diastolic pressure and cerebral flow dramatically.',
    'bloom': 'recall',
    'source': [{'book': 'StatPearls', 'page': 2}],
    'confusable_with': 'Epinephrine administration — improves ROSC rate but compressions remain the single most important intervention'
  },
  {
    'id': 'acls-nonshockable-3',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'How can respiratory arrest be mistaken for cardiac arrest, and why is this distinction critical?',
    'answer': 'Respiratory arrest patients may present with agonal gasps mistaken for breathing; if unrecognized, airway/ventilation management is delayed and rapid progression to cardiac arrest occurs.',
    'rationale': 'Agonal breathing is a brainstem reflex not effective ventilation; without immediate airway management, hypoxic cardiac arrest follows within minutes.',
    'bloom': 'apply',
    'source': [{'book': 'StatPearls', 'page': 7}],
    'confusable_with': 'Seizure activity — also presents with abnormal movements that can mimic agonal gasps'
  },
  {
    'id': 'acls-nonshockable-4',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'What post-cardiac arrest care does ischemia-reperfusion injury require?',
    'answer': 'Comprehensive post-cardiac arrest care: hemodynamic support, mechanical ventilation (lung-protective), temperature management, treatment of underlying causes and seizures, infection monitoring.',
    'rationale': 'Ischemia-reperfusion after ROSC affects multiple organ systems; without systematic management, secondary organ failure and neurological death occur.',
    'bloom': 'apply',
    'source': [{'book': 'StatPearls', 'page': 10}],
    'confusable_with': 'Resuscitation endpoints only — ROSC is the beginning of post-arrest care, not the end'
  },
]

# ============================================================
# [52] Acute Abdomen: Differential Diagnosis & Initial Approach
# ============================================================
t = 'Acute Abdomen: Differential Diagnosis & Initial Approach'
kps += [
  {
    'id': 'acute-abdomen-1',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'What is the first priority when evaluating a patient with acute abdominal pain?',
    'answer': 'Immediately assess for and exclude life-threatening causes: bowel obstruction, perforation, mesenteric ischemia, pancreatitis, MI, DKA, and elevated ICP. Vital signs and stability assessment come first.',
    'rationale': 'Several causes of acute abdomen require emergency surgery or intervention within hours; delayed diagnosis increases mortality exponentially.',
    'bloom': 'apply',
    'source': [{'book': 'MGH Housestaff Manual', 'page': 75}],
    'confusable_with': 'Pain management before diagnosis — controversial; adequate analgesia does not impair exam accuracy'
  },
  {
    'id': 'acute-abdomen-2',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'In critically ill patients, which four intraabdominal infections can develop de novo without antecedent surgery?',
    'answer': 'Perforated ulcer, diverticulitis, appendicitis, and acalculous cholecystitis can all develop in critically ill patients whether or not they are recovering from a surgical procedure.',
    'rationale': 'Critical illness impairs mucosal perfusion and immunity; ischemic cholecystitis and stress ulcer perforation are particular risks in ICU patients.',
    'bloom': 'recall',
    'source': [{'book': 'Morgan & Mikhail', 'page': 2152}],
    'confusable_with': 'Post-surgical abdominal complications — anastomotic leak, wound infection; these are similar presentations but require different management'
  },
  {
    'id': 'acute-abdomen-3',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'When is abdominal ultrasound preferred over CT for imaging in children with suspected acute abdomen?',
    'answer': 'Abdominal ultrasound is preferred when imaging is needed but findings are unclear — particularly to avoid radiation in children; CT is reserved for equivocal US or high clinical concern.',
    'rationale': 'Pediatric patients are more radiosensitive; ultrasound identifies free fluid, appendiceal dilation, and intussusception without ionizing radiation.',
    'bloom': 'apply',
    'source': [{'book': 'StatPearls', 'page': 11}],
    'confusable_with': 'Plain abdominal XR — adequate only for suspected obstruction or perforation (free air); misses most diagnoses'
  },
  {
    'id': 'acute-abdomen-4',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'What adrenal emergency can mimic acute abdomen and must be excluded in patients on chronic corticosteroids?',
    'answer': 'Adrenal (Addisonian) crisis — can present with abdominal pain, nausea, vomiting, hypotension, and fever, mimicking an acute abdomen.',
    'rationale': 'Glucocorticoid deficiency causes prostaglandin-mediated smooth muscle spasm and hypotension; in steroid-dependent patients, surgical stress triggers adrenal crisis.',
    'bloom': 'analyze',
    'source': [{'book': 'StatPearls', 'page': 10}],
    'confusable_with': 'Surgical acute abdomen — adrenal crisis requires steroids not surgery; differentiate by hemodynamics and steroid history'
  },
]

kps.append({
    '_type': 'illness_script',
    'topic': 'Acute Abdomen: Differential Diagnosis & Initial Approach',
    'discipline': 'medicine',
    'enabling_conditions': 'Any age; prior abdominal surgery (adhesion SBO); gallstones; diverticular disease; PUD; atherosclerosis (mesenteric ischemia); critical illness (acalculous cholecystitis)',
    'pathophysiology': 'Visceral (crampy, poorly localized) or parietal (sharp, well-localized, peritoneal signs) pain; ischemia and perforation cause peritonitis via bacterial translocation or chemical irritation',
    'time_course': 'Perforation/ischemia: acute onset minutes-hours; obstruction: progressive over hours; appendicitis: hours with migration RLQ',
    'key_features': 'Pain character/location/radiation/migration; peritoneal signs (guarding, rigidity, rebound); bowel sounds; fever; hemodynamic instability',
    'consequence_if_missed': 'Perforation with septic shock; intestinal infarction with 80%+ mortality; missed ectopic pregnancy with hemorrhage'
})

print('Batch 5 KPs:', len(kps))
with open('data/_kp_part2_batch5.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print('Written.')
