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
# [55] Adrenal Crisis
# ============================================================
t = 'Adrenal Crisis'
kps += [
  {
    'id': 'adrenal-crisis-1',
    'topic': t, 'domain': dom_endo, 'discipline': dis,
    'stem': 'What two perioperative triggers can precipitate acute adrenal insufficiency (Addisonian crisis)?',
    'answer': 'Failure to provide adequate glucocorticoid coverage in steroid-dependent patients during periods of stress (infection, trauma, surgery), and etomidate infusion which suppresses adrenal steroidogenesis.',
    'rationale': 'The HPA axis is suppressed by exogenous steroids and cannot mount the stress response; etomidate irreversibly inhibits 11-beta-hydroxylase for up to 24-48 hours.',
    'bloom': 'recall',
    'source': [{'book': 'Morgan & Mikhail', 'page': 1236}],
    'confusable_with': 'Septic shock — both cause refractory hypotension; adrenal crisis responds to hydrocortisone'
  },
  {
    'id': 'adrenal-crisis-2',
    'topic': t, 'domain': dom_endo, 'discipline': dis,
    'stem': 'A patient on chronic steroids develops fever, hypotension, and AMS perioperatively. What finding excludes malignant hyperthermia from the differential?',
    'answer': 'Absence of major metabolic acidosis and no exposure to a known triggering agent (volatile anesthetic or succinylcholine) effectively excludes MH; decreasing hypertension now replaced by relative hypotension is more consistent with Addisonian crisis.',
    'rationale': 'MH produces a hypermetabolic state with marked metabolic acidosis and rising EtCO2 in response to triggering agents; Addisonian crisis is a mineralocorticoid/glucocorticoid deficiency state.',
    'bloom': 'analyze',
    'source': [{'book': 'Morgan & Mikhail', 'page': 2122}],
    'confusable_with': 'Sepsis — also causes fever and hypotension; Addisonian crisis requires steroid history and responds to hydrocortisone'
  },
  {
    'id': 'adrenal-crisis-3',
    'topic': t, 'domain': dom_endo, 'discipline': dis,
    'stem': 'If hydrocortisone is unavailable during an adrenal crisis, what is the preferred alternative parenteral glucocorticoid?',
    'answer': 'Prednisolone is the preferred alternative parenteral glucocorticoid when hydrocortisone is unavailable.',
    'rationale': 'Prednisolone has significant glucocorticoid activity and can be administered parenterally; dexamethasone lacks mineralocorticoid activity but is also usable if others unavailable.',
    'bloom': 'recall',
    'source': [{'book': 'StatPearls', 'page': 10}],
    'confusable_with': 'Dexamethasone — no mineralocorticoid activity; adequate for glucocorticoid replacement but not full Addisonian crisis coverage'
  },
  {
    'id': 'adrenal-crisis-4',
    'topic': t, 'domain': dom_endo, 'discipline': dis,
    'stem': 'In patients with Cushing syndrome from exogenous glucocorticoids, why is adrenal crisis a specific perioperative concern?',
    'answer': 'Exogenous glucocorticoids suppress the HPA axis; the adrenal glands may not respond to perioperative stress, requiring supplemental "stress dose" corticosteroids during surgery.',
    'rationale': 'Chronic exogenous steroid use causes adrenocortical atrophy via negative feedback; sudden stress without supplementation leads to relative or absolute adrenal insufficiency.',
    'bloom': 'apply',
    'source': [{'book': 'Morgan & Mikhail', 'page': 1236}],
    'confusable_with': 'Endogenous Cushing (adrenal adenoma) — these patients have functional adrenal tissue and are not at risk for crisis'
  },
]

kps.append({
    '_type': 'illness_script',
    'topic': 'Adrenal Crisis',
    'discipline': 'medicine',
    'enabling_conditions': 'Chronic exogenous steroid use (most common); primary adrenal insufficiency (Addison disease); etomidate administration; bilateral adrenal hemorrhage; pituitary apoplexy',
    'pathophysiology': 'Deficiency of cortisol and (in primary AI) aldosterone; loss of glucocorticoid support causes vasodilation, cytokine upregulation, hypoglycemia; mineralocorticoid loss causes hyponatremia and hyperkalemia',
    'time_course': 'Hours-days after stress trigger; acute crisis in minutes-hours if precipitated by surgery/trauma without coverage',
    'key_features': 'Hypotension refractory to vasopressors, fever, abdominal pain, AMS, hyponatremia, hyperkalemia, hypoglycemia; history of steroid use or adrenal disease',
    'consequence_if_missed': 'Death from refractory vasodilatory shock; easily treated with IV hydrocortisone 100mg bolus'
})

# ============================================================
# [56] Advanced Cardiac Life Support (ACLS): Shockable Rhythms
# ============================================================
t = 'Advanced Cardiac Life Support (ACLS): Shockable Rhythms'
kps += [
  {
    'id': 'acls-shockable-1',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'What is the preferred defibrillator type and shock strategy for VF/VT?',
    'answer': 'Biphasic defibrillator is preferred over monophasic; single shock (not stacked/sequential) is preferred — deliver one shock then immediately resume CPR.',
    'rationale': 'Biphasic waveforms deliver equivalent energy with less myocardial damage; sequential shocks delay CPR and do not improve defibrillation success versus single shocks.',
    'bloom': 'recall',
    'source': [{'book': 'Miller/Baby Miller', 'page': 843}],
    'confusable_with': 'Historical monophasic "stacked shocks" — no longer recommended'
  },
  {
    'id': 'acls-shockable-2',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'If VF/VT persists after at least one CPR-defibrillation cycle, what antiarrhythmic drug is considered?',
    'answer': 'Amiodarone (or lidocaine as an alternative) for shock-refractory VF/VT. A study showed lidocaine had favorable results vs placebo for OHCA, but amiodarone did not show consistent benefit.',
    'rationale': 'Amiodarone blocks Na, K, Ca channels and beta-adrenergic receptors; it prolongs action potential duration to reduce re-entrant VF.',
    'bloom': 'apply',
    'source': [{'book': 'Miller/Baby Miller', 'page': 844}],
    'confusable_with': 'Magnesium — first-line for torsades de pointes (polymorphic VT with prolonged QT); not standard for monomorphic VT/VF'
  },
  {
    'id': 'acls-shockable-3',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'Why was vasopressin removed from the 2015 ACLS shockable rhythm algorithm?',
    'answer': 'Vasopressin showed no advantage over epinephrine alone or in combination; its removal simplified the protocol without outcome benefit.',
    'rationale': 'RCTs failed to demonstrate improved ROSC or survival with vasopressin; epinephrine remains the sole recommended vasopressor.',
    'bloom': 'recall',
    'source': [{'book': 'Miller/Baby Miller', 'page': 844}],
    'confusable_with': 'Vasopressin in septic shock — still an adjunct to norepinephrine; role differs from cardiac arrest'
  },
  {
    'id': 'acls-shockable-4',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'In the perioperative setting, what are the major causes of cardiovascular collapse that overlap with VF/VT (shockable rhythms)?',
    'answer': 'Major perioperative cardiovascular collapse causes include the 8 Hs and 8 Ts: hypoxia, hypovolemia, acidosis, electrolyte disorders, hypothermia, toxins (anaphylaxis), tension pneumothorax, thrombosis (coronary/PE), malignant hyperthermia, QT prolongation, hypervagal response.',
    'rationale': 'Perioperative VF/VT often has a correctable underlying cause; treating only the rhythm without addressing the cause leads to recurrence.',
    'bloom': 'apply',
    'source': [{'book': 'Miller/Baby Miller', 'page': 843}],
    'confusable_with': 'Primary VF (e.g., acute MI) — idiopathic; no perioperative trigger'
  },
  {
    'id': 'acls-shockable-5',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'Levothyroxine appears in the Marino ICU Book index as a treatment for what cardiac arrest condition?',
    'answer': 'Levothyroxine can be considered as an adjunct in cardiac arrest management (particularly in the context of hypothyroid-related arrest) and is also listed for treatment of ventricular tachycardia in selected cases.',
    'rationale': 'Thyroid hormone affects cardiac contractility and rhythm via nuclear receptor-mediated effects on ion channel expression; severe hypothyroidism can cause VT and refractory cardiac arrest.',
    'bloom': 'recall',
    'source': [{'book': 'Marino ICU Book', 'page': 776}],
    'confusable_with': 'Standard ACLS drugs — epinephrine and amiodarone are first-line; levothyroxine is adjunct in specific scenarios'
  },
]

# ============================================================
# [57] Airway Management in Emergencies
# ============================================================
t = 'Airway Management in Emergencies'
kps += [
  {
    'id': 'airway-management-emergencies-1',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'In bariatric patients requiring emergency airway management, why does desaturation occur more rapidly and what positioning is critical?',
    'answer': 'Obese patients desaturate more rapidly due to compromised airway mechanics, increased metabolic demand and O2 consumption, and underlying conditions contributing to hypoxia. Patient positioning (ramping/head elevation) is crucial before any attempt.',
    'rationale': 'Functional residual capacity is significantly reduced in obesity; this shortens apnea safe time. Ramping opens the airway by aligning the external auditory canal with the sternal notch.',
    'bloom': 'apply',
    'source': [{'book': 'StatPearls', 'page': 7}],
    'confusable_with': 'Standard supine positioning in obese patients — reduces FRC further and worsens desaturation'
  },
  {
    'id': 'airway-management-emergencies-2',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'What manual airway management maneuvers are used when advanced airway equipment is unavailable or has malfunctioned?',
    'answer': 'Head-tilt-chin-lift (avoid in trauma) or jaw-thrust maneuver (preferred in trauma with suspected C-spine injury); oropharyngeal and nasopharyngeal airways as adjuncts.',
    'rationale': 'Jaw-thrust displaces the mandible forward without cervical extension, relieving soft-tissue obstruction while minimizing C-spine movement.',
    'bloom': 'recall',
    'source': [{'book': 'StatPearls', 'page': 4}],
    'confusable_with': 'Head-tilt in trauma — contraindicated if C-spine injury is possible; use jaw-thrust instead'
  },
  {
    'id': 'airway-management-emergencies-3',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'An angioedema patient has airway compromise. What is the management algorithm based on etiology?',
    'answer': 'Allergic/histaminergic angioedema: epinephrine, antihistamines, steroids, emergent intubation. Hereditary angioedema (HAE): C1 inhibitor replacement, icatibant, or FFP — epinephrine/steroids/antihistamines are less effective.',
    'rationale': 'HAE is bradykinin-mediated (not histamine), so antihistamines and steroids do not reliably work; specific HAE therapies target bradykinin or kallikrein pathways.',
    'bloom': 'analyze',
    'source': [{'book': 'Morgan & Mikhail', 'page': 2036}],
    'confusable_with': 'Allergic angioedema — histamine-mediated, responds to epinephrine/steroids/antihistamines'
  },
  {
    'id': 'airway-management-emergencies-4',
    'topic': t, 'domain': dom_em, 'discipline': dis,
    'stem': 'In prehospital emergency airway management, what environmental factor can impair laryngoscopy equipment function?',
    'answer': 'Extreme temperatures can cause laryngoscopy equipment malfunction; backup methods (video laryngoscopy, BVM) must be immediately available.',
    'rationale': 'Electronic video laryngoscopes and fiber-optic bundles are temperature-sensitive; cold causes fogging and battery failure, heat degrades optics.',
    'bloom': 'recall',
    'source': [{'book': 'StatPearls', 'page': 5}],
    'confusable_with': 'Equipment failure in OR — highly unlikely in controlled setting; prehospital environment requires redundancy'
  },
]

print('Batch 7 KPs:', len(kps))
with open('data/_kp_part2_batch7.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print('Written.')
