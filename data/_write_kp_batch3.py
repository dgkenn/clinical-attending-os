import json

kps = []
dom_onc = 'Internal medicine: on-call & cross-cover (approach to the acutely changing ward patient)'
dom_icu = 'Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)'
dom_em = 'Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)'
dom_endo = 'Internal medicine: endocrinology (diabetes & inpatient glucose, DKA & HHS, thyroid disorders & storm, adrenal insufficiency, calcium disorders, pituitary)'
dis = 'medicine'

# ============================================================
# [42] Approach to Nausea and Vomiting
# ============================================================
t = 'Approach to Nausea and Vomiting'
kps += [
  {
    'id': 'approach-to-nausea-vomiting-1',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'A ward patient develops acute nausea and vomiting. What life-threatening causes must be excluded first?',
    'answer': 'First exclude: bowel obstruction, bowel perforation, mesenteric ischemia, pancreatitis, MI, DKA, and elevated intracranial pressure.',
    'rationale': 'These diagnoses require urgent intervention; missing them while treating nausea symptomatically leads to catastrophic delays.',
    'bloom': 'apply',
    'source': [{'book': 'MGH Housestaff Manual', 'page': 75}],
    'confusable_with': 'Gastroenteritis — benign but diagnosis of exclusion'
  },
  {
    'id': 'approach-to-nausea-vomiting-2',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'Without prophylactic intervention, roughly what fraction of patients undergoing inhalational anesthesia develop PONV?',
    'answer': 'Approximately one-third (range 10-80%) develop PONV without prophylaxis; consequences include delayed PACU discharge, unanticipated admission, aspiration risk, and significant discomfort.',
    'rationale': 'Volatile anesthetic agents directly stimulate the chemoreceptor trigger zone and increase vagal tone via gut motility changes.',
    'bloom': 'recall',
    'source': [{'book': 'Miller/Baby Miller', 'page': 734}],
    'confusable_with': 'Regional anesthesia PONV rate — substantially lower'
  },
  {
    'id': 'approach-to-nausea-vomiting-3',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'Nausea, vomiting, and paroxysmal hypertension with diaphoresis point to what endocrine cause?',
    'answer': 'Pheochromocytoma or paraganglioma — hormonally active tumors producing catecholamines; classic triad is paroxysmal headache, tachycardia, and diaphoresis.',
    'rationale': 'Catecholamine surges cause sympathetic hyperactivity including GI motility disturbances, explaining nausea and vomiting as part of the paroxysmal syndrome.',
    'bloom': 'analyze',
    'source': [{'book': 'Miller/Baby Miller', 'page': 551}],
    'confusable_with': 'Carcinoid syndrome — also causes episodic flushing and GI symptoms but via serotonin/vasoactive peptides'
  },
  {
    'id': 'approach-to-nausea-vomiting-4',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'Spinal anesthesia for outpatient lower-extremity surgery reduces PONV. What is the mechanism?',
    'answer': 'Spinal anesthesia avoids volatile agents and opioids (both emetic), eliminating the two most potent causes of PONV; the tradeoff is possible prolonged motor block delaying discharge.',
    'rationale': 'Volatile agents and opioids both stimulate the vomiting center and CTZ via separate pathways; avoiding both dramatically reduces PONV incidence.',
    'bloom': 'analyze',
    'source': [{'book': 'Miller/Baby Miller', 'page': 699}],
    'confusable_with': 'Total spinal complication — rare but catastrophic hemodynamic event requiring airway management'
  },
]

# ============================================================
# [43] Approach to Oliguria and Low Urine Output
# ============================================================
t = 'Approach to Oliguria and Low Urine Output'
kps += [
  {
    'id': 'approach-to-oliguria-1',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'What is the AKI definition of oliguria used in organ dysfunction assessment?',
    'answer': 'Oliguria as an AKI criterion: urine output <0.5 mL/kg/h for at least 2 hours.',
    'rationale': 'This threshold reflects inadequate renal perfusion or tubular dysfunction; below this rate the kidneys cannot clear nitrogenous wastes effectively.',
    'bloom': 'recall',
    'source': [{'book': 'Morgan & Mikhail', 'page': 2147}],
    'confusable_with': 'Anuria (<100 mL/24h) — typically indicates complete obstruction or bilateral renal failure'
  },
  {
    'id': 'approach-to-oliguria-2',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'Acute kidney failure is classified as prerenal, renal, and postrenal. What does the initial therapeutic approach depend on?',
    'answer': 'Initial therapy varies by cause: prerenal requires volume resuscitation; intrinsic (renal) requires removing the offending agent and supportive care; postrenal requires relief of obstruction.',
    'rationale': 'Prerenal AKI is functional and rapidly reversible with fluid; intrinsic AKI reflects structural tubular injury; postrenal AKI requires mechanical decompression.',
    'bloom': 'apply',
    'source': [{'book': 'Morgan & Mikhail', 'page': 1106}],
    'confusable_with': 'Intrinsic renal AKI (ATN) treated with fluids — fluid loading in ATN does not improve GFR and may cause harm'
  },
  {
    'id': 'approach-to-oliguria-3',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'Does mannitol or furosemide given to convert oliguric to nonoliguric AKI improve outcomes?',
    'answer': 'No — there is no clinical evidence that mannitol provides kidney protection or that converting oliguric to nonoliguric AKI lessens severity or mortality compared with volume correction.',
    'rationale': 'Loop diuretics increase urine output without restoring GFR; conversion from oliguric to nonoliguric is a marker of less severe injury, not the result of diuretic therapy.',
    'bloom': 'recall',
    'source': [{'book': 'Morgan & Mikhail', 'page': 1079}],
    'confusable_with': 'Volume resuscitation — correction of hypovolemia does improve prerenal AKI'
  },
  {
    'id': 'approach-to-oliguria-4',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'In the KDIGO framework, what does oliguria measure and why is it considered a poor measure of kidney function?',
    'answer': 'Oliguria measures urine flow rate, which is a poor measure of kidney function; it is an indirect and insensitive proxy for GFR.',
    'rationale': 'Urine output can be maintained through tubular processing even with severely reduced filtration; conversely, high urine output does not exclude AKI.',
    'bloom': 'analyze',
    'source': [{'book': 'Society Guideline: Guideline   KDIGO 2012 AKI', 'page': 38}],
    'confusable_with': 'Serum creatinine — also lags behind true GFR changes but is a better AKI marker than urine output alone'
  },
]

# ============================================================
# [44] Approach to Palpitations
# ============================================================
t = 'Approach to Palpitations'
kps += [
  {
    'id': 'approach-to-palpitations-1',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'A patient reports palpitations. What are the most dangerous potential complications of atrial fibrillation that must be screened for?',
    'answer': 'Thromboembolism/stroke, new-onset or worsening heart failure, acute MI, hemodynamic instability/cardiogenic shock, sudden death (Wolff-Parkinson-White), and tachycardia-induced cardiomyopathy.',
    'rationale': 'AF causes stasis in the left atrial appendage promoting clot, impairs atrial kick reducing cardiac output, and rapid ventricular rates cause demand ischemia and cardiomyopathy.',
    'bloom': 'recall',
    'source': [{'book': 'StatPearls', 'page': 7}],
    'confusable_with': 'PACs/PVCs — benign palpitations without thromboembolic risk'
  },
  {
    'id': 'approach-to-palpitations-2',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'Palpitations, paroxysmal hypertension, headache, and diaphoresis in a ward patient. What endocrine emergency should be considered?',
    'answer': 'Pheochromocytoma or paraganglioma — catecholamine-secreting tumors with the classic triad of paroxysmal headache, tachycardia, and diaphoresis.',
    'rationale': 'Pheochromocytoma releases bursts of catecholamines causing episodic sympathetic activation; diagnosis requires plasma/urine metanephrines.',
    'bloom': 'apply',
    'source': [{'book': 'StatPearls', 'page': 17}],
    'confusable_with': 'Panic disorder — clinically similar but metanephrine levels are normal'
  },
  {
    'id': 'approach-to-palpitations-3',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'Palpitations, syncope, and chest pain in a patient with known sarcoidosis suggest what cardiac complication requiring urgent evaluation?',
    'answer': 'Cardiac sarcoidosis causing arrhythmias or conduction defects; early recognition is essential to prevent irreversible organ damage.',
    'rationale': 'Sarcoid granulomas infiltrate the conduction system and myocardium, causing VT, heart block, and sudden death.',
    'bloom': 'apply',
    'source': [{'book': 'StatPearls', 'page': 6}],
    'confusable_with': 'Pulmonary sarcoidosis palpitations — usually less life-threatening'
  },
  {
    'id': 'approach-to-palpitations-4',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'When evaluating chest pain with palpitations, how does the ACC/AHA 2021 guideline suggest selecting between CCTA and functional stress testing?',
    'answer': 'Best test depends on clinical question, symptom acuity, baseline CVD risk/known CAD history, and patient-specific contraindications; CCTA is favored for anatomic characterization, stress testing for functional assessment.',
    'rationale': 'CCTA identifies obstructive CAD anatomically; functional testing demonstrates ischemia under stress — the choice depends on pre-test probability and clinical context.',
    'bloom': 'analyze',
    'source': [{'book': 'MGH Housestaff Manual', 'page': 22}],
    'confusable_with': 'ECG alone — insufficient to exclude ACS in intermediate-risk palpitations'
  },
]

# ============================================================
# [45] Approach to Supratherapeutic INR and Bleeding
# ============================================================
t = 'Approach to Supratherapeutic INR and Bleeding'
kps += [
  {
    'id': 'approach-to-supratherapeutic-inr-1',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'Which coagulation factors depend on vitamin K and are produced by the liver (and thus reflect hepatic synthetic function)?',
    'answer': 'All coagulation factors except factor VIII and von Willebrand factor are produced by the liver; vitamin K is required for synthesis of factors II (prothrombin), VII, IX, and X.',
    'rationale': 'Warfarin inhibits vitamin K epoxide reductase, reducing carboxylation of factors II, VII, IX, X; PT/INR is dominated by factor VII (shortest half-life).',
    'bloom': 'recall',
    'source': [{'book': 'Morgan & Mikhail', 'page': 1155}],
    'confusable_with': 'Factor VIII deficiency (hemophilia A) — not vitamin K dependent, not liver-synthesized'
  },
  {
    'id': 'approach-to-supratherapeutic-inr-2',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'What INR threshold must be reached before a neuraxial catheter can be removed in a patient on warfarin?',
    'answer': 'Neuraxial catheters should be removed when INR is 1.5 or lower; a neuraxial block should not be placed unless INR is normal.',
    'rationale': 'Epidural hematoma risk rises sharply at INR >1.5; maintaining INR ≤1.5 at removal minimizes bleeding into the epidural space.',
    'bloom': 'recall',
    'source': [{'book': 'Morgan & Mikhail', 'page': 1299}],
    'confusable_with': 'INR <2.0 threshold used for other procedures — neuraxial has stricter requirement'
  },
  {
    'id': 'approach-to-supratherapeutic-inr-3',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'A patient on warfarin with AF and life-threatening bleeding. What is the recommended reversal strategy per ACC/AHA 2023?',
    'answer': '4-factor prothrombin complex concentrate (4F-PCC) PLUS IV vitamin K is recommended over FFP + vitamin K for rapid INR correction in life-threatening bleeding.',
    'rationale': '4F-PCC contains concentrated factors II, VII, IX, X and achieves faster and more complete INR reversal than FFP; vitamin K provides sustained normalization.',
    'bloom': 'apply',
    'source': [{'book': 'Society Guideline: Guideline   ACC AHA 2023 Atrial Fibrillation', 'page': 45}],
    'confusable_with': 'FFP alone — slower, requires large volumes, risk of volume overload'
  },
  {
    'id': 'approach-to-supratherapeutic-inr-4',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'For most patients on warfarin or DOAC undergoing an invasive procedure, is bridging anticoagulation recommended?',
    'answer': 'Temporary cessation of anticoagulation WITHOUT bridging is recommended for most AF patients (excluding recent stroke/TIA or mechanical valve) undergoing invasive procedures.',
    'rationale': 'Bridging increases bleeding without reducing thromboembolic risk in most AF patients; the risk of periprocedural bleeding from heparin outweighs its thromboembolic protection.',
    'bloom': 'apply',
    'source': [{'book': 'Society Guideline: Guideline   ACC AHA 2023 Atrial Fibrillation', 'page': 50}],
    'confusable_with': 'Mechanical heart valve — bridging IS indicated due to very high thromboembolic risk'
  },
]

print('Batch 3 KPs:', len(kps))
with open('data/_kp_part2_batch3.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print('Written.')
