import json

kps = []
dom_onc = 'Internal medicine: on-call & cross-cover (approach to the acutely changing ward patient)'
dom_icu = 'Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)'
dom_em = 'Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)'
dom_endo = 'Internal medicine: endocrinology (diabetes & inpatient glucose, DKA & HHS, thyroid disorders & storm, adrenal insufficiency, calcium disorders, pituitary)'
dis = 'medicine'

# ============================================================
# [46] Approach to Suspected DVT and Limb Swelling
# ============================================================
t = 'Approach to Suspected DVT and Limb Swelling'
kps += [
  {
    'id': 'approach-to-dvt-1',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'What are the classic clinical signs of DVT and their prevalence?',
    'answer': 'Pain (50%), swelling (70%), limb edema (may be unilateral or bilateral if pelvic veins involved), red/hot skin with dilated veins. Homans sign has no sensitivity or specificity.',
    'rationale': 'DVT obstructs venous return, causing distal stasis, inflammation, and edema; pelvic extension causes bilateral signs.',
    'bloom': 'recall',
    'source': [{'book': 'StatPearls', 'page': 5}],
    'confusable_with': 'Cellulitis — also warm/red/swollen but lacks dilated veins and DVT risk factors'
  },
  {
    'id': 'approach-to-dvt-2',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'What is phlegmasia alba dolens and what does it progress to?',
    'answer': 'Phlegmasia alba dolens is massive iliofemoral DVT causing edema and pain; it can progress to phlegmasia cerulea dolens (venous gangrene with cyanosis and limb ischemia).',
    'rationale': 'Complete iliofemoral occlusion prevents venous and eventually arterial flow; tissue ischemia and gangrene result without urgent thrombus removal.',
    'bloom': 'recall',
    'source': [{'book': 'MGH Housestaff Manual', 'page': 54}],
    'confusable_with': 'Arterial occlusion (acute limb ischemia) — also causes limb ischemia but from arterial, not venous, cause'
  },
  {
    'id': 'approach-to-dvt-3',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'The HIT antibody cycle involves IgG, heparin, and PF4. What does this cycle ultimately cause clinically?',
    'answer': 'IgG binds heparin-PF4 complexes and activates platelets via Fc receptor, releasing more PF4 and thrombin — creating a severely hypercoagulable state causing thrombosis despite thrombocytopenia.',
    'rationale': 'The cycle amplifies platelet activation and thrombin generation; stopping heparin is essential but a non-heparin anticoagulant must be started immediately.',
    'bloom': 'analyze',
    'source': [{'book': 'StatPearls', 'page': 3}],
    'confusable_with': 'ITP — also causes thrombocytopenia but via different mechanism and without hypercoagulability'
  },
  {
    'id': 'approach-to-dvt-4',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'In a patient at significantly increased bleeding risk with VTE risk, what VTE prophylaxis strategy is used?',
    'answer': 'Mechanical prophylaxis alone (compression stockings, pneumatic compression devices) until bleeding risk decreases, then pharmacologic anticoagulation is added.',
    'rationale': 'Pharmacologic anticoagulation in high-bleeding-risk patients risks catastrophic hemorrhage; mechanical methods reduce venous stasis without coagulopathy.',
    'bloom': 'apply',
    'source': [{'book': 'Morgan & Mikhail', 'page': 1299}],
    'confusable_with': 'Low-dose LMWH in normal-bleed-risk patients — both prevent DVT but drug is contraindicated in high-bleed-risk'
  },
]

# ============================================================
# [47] Approach to Thrombocytopenia
# ============================================================
t = 'Approach to Thrombocytopenia'
kps += [
  {
    'id': 'approach-to-thrombocytopenia-1',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'A patient develops thrombocytopenia 5-10 days after starting heparin and is found to have new arterial thrombosis. What is the diagnosis?',
    'answer': 'Heparin-Induced Thrombocytopenia (HIT) — an immune-mediated disorder where IgG antibodies against heparin-PF4 complexes paradoxically cause thrombocytopenia AND thrombosis.',
    'rationale': 'The platelet count typically drops 5-10 days post-heparin exposure; the hypercoagulable state can cause arterial and venous thromboses despite low platelet counts.',
    'bloom': 'apply',
    'source': [{'book': 'StatPearls', 'page': 1}],
    'confusable_with': 'ITP — immune thrombocytopenia but without thrombosis; HITT (HIT with thrombosis) is a subset'
  },
  {
    'id': 'approach-to-thrombocytopenia-2',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'What platelet threshold is commonly used before major nonneuraxial surgery, and what higher threshold is required for brain or posterior eye surgery?',
    'answer': '>50 x10^9/L for major nonneuraxial surgery; >100 x10^9/L for surgery on the brain or posterior eye, based on expert opinion.',
    'rationale': 'Brain and posterior ocular surgery have catastrophic consequences from even small hemorrhages; higher platelet counts are required to maintain intraoperative hemostasis.',
    'bloom': 'recall',
    'source': [{'book': 'Miller/Baby Miller', 'page': 232}],
    'confusable_with': 'Platelet transfusion trigger 10x10^9/L — threshold for prophylactic transfusion in hematology, not surgical'
  },
  {
    'id': 'approach-to-thrombocytopenia-3',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'A thoracentesis is planned in a patient with thrombocytopenia. At what platelet count is reversal considered, and is there absolute contraindication data?',
    'answer': 'Consider reversing thrombocytopenia at platelets <50k before thoracentesis, but there is no data supporting an absolute contraindication threshold.',
    'rationale': 'Clinical practice suggests platelets <50k increases bleeding risk, but procedure-specific data are limited; individual risk-benefit assessment is required.',
    'bloom': 'apply',
    'source': [{'book': 'MGH Housestaff Manual', 'page': 261}],
    'confusable_with': 'INR >1.5 for thoracentesis — also a relative contraindication worth addressing'
  },
  {
    'id': 'approach-to-thrombocytopenia-4',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'Blood products are bacterially contaminated more commonly in which product: platelets or PRBCs?',
    'answer': 'Platelets: bacterial contamination positive cultures 1:2000 (vs 1:7000 for PRBCs), making bacterial sepsis from platelet transfusion a leading cause of transfusion-related mortality.',
    'rationale': 'Platelets are stored at room temperature (~22°C) rather than refrigerated, which allows bacterial proliferation — in contrast to PRBCs stored at 4°C.',
    'bloom': 'recall',
    'source': [{'book': 'Morgan & Mikhail', 'page': 1967}],
    'confusable_with': 'TRALI — more common with FFP and platelets vs PRBCs but due to antibodies, not bacteria'
  },
]

kps.append({
    '_type': 'illness_script',
    'topic': 'Approach to Thrombocytopenia',
    'discipline': 'medicine',
    'enabling_conditions': 'Heparin exposure (HIT); autoimmune conditions (ITP); bone marrow suppression (drug/chemo/malignancy); DIC (sepsis, trauma); hypersplenism',
    'pathophysiology': 'Three mechanisms: decreased production (marrow failure), increased destruction (immune/consumptive), sequestration (splenomegaly)',
    'time_course': 'HIT: 5-10 days after heparin start; ITP: days-weeks; DIC: hours-days after trigger; drug-induced: variable',
    'key_features': 'Count + trend, bleeding signs (petechiae, purpura, mucosal), thrombosis (paradoxical in HIT), fever/organomegaly, medication timeline',
    'consequence_if_missed': 'HIT: catastrophic arterial/venous thrombosis if heparin continued; DIC: multiorgan failure; severe thrombocytopenia: intracranial hemorrhage'
})

# ============================================================
# [48] Approach to Uncontrolled Pain
# ============================================================
t = 'Approach to Uncontrolled Pain'
kps += [
  {
    'id': 'approach-to-uncontrolled-pain-1',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'In elderly patients with uncontrolled pain, what specific benefit do regional/neuraxial techniques offer over general anesthesia?',
    'answer': 'Regional techniques are opioid-sparing, potentially avoiding opioid-induced delirium and respiratory depression; they also reduce adverse effects of general anesthesia in older patients.',
    'rationale': 'Elderly patients have decreased renal/hepatic clearance and heightened opioid sensitivity; regional analgesia provides targeted pain control without systemic CNS depression.',
    'bloom': 'apply',
    'source': [{'book': 'Miller/Baby Miller', 'page': 679}],
    'confusable_with': 'Opioid dose adjustment alone — useful but does not eliminate opioid risks in elderly'
  },
  {
    'id': 'approach-to-uncontrolled-pain-2',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'A patient on opioids reports uncontrolled pain and is constipated. What class of treatment is uniquely appropriate for opioid-induced side effects?',
    'answer': 'Peripherally-acting mu-opioid receptor antagonists (e.g., methylnaltrexone) reverse opioid-induced constipation without reversing central analgesia.',
    'rationale': 'These agents do not cross the blood-brain barrier, selectively blocking peripheral opioid receptors in the gut responsible for reduced motility.',
    'bloom': 'apply',
    'source': [{'book': 'MGH Housestaff Manual', 'page': 169}],
    'confusable_with': 'Naloxone — reverses both analgesia and constipation by acting centrally and peripherally'
  },
  {
    'id': 'approach-to-uncontrolled-pain-3',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'End-of-life pain management: what is the fundamental goal, and does changing to CMO status require DNR/DNI?',
    'answer': 'Goal is to enhance comfort and optimize symptom management. Comfort Measures Only (CMO) does NOT require changing code status; code status reflects patient goals, not medical state.',
    'rationale': 'EOL is a medical state defined by prognosis; code status is a separate decision reflecting patient values — a patient can be CMO and full code if they choose.',
    'bloom': 'recall',
    'source': [{'book': 'MGH Housestaff Manual', 'page': 169}],
    'confusable_with': 'DNR = comfort care — incorrect; CMO and code status are independent decisions'
  },
  {
    'id': 'approach-to-uncontrolled-pain-4',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'For patients with pheochromocytoma and paraganglioma requiring surgery, what special epidural considerations apply?',
    'answer': 'Premedicate to reduce anxiety, avoid epinephrine in the epidural test dose, and use low-concentration local anesthetics to avoid sympathectomy-induced hemodynamic lability.',
    'rationale': 'Epinephrine test dose can trigger catecholamine release from the tumor; extensive sympathectomy from dense epidural block worsens hemodynamic instability.',
    'bloom': 'apply',
    'source': [{'book': 'Miller/Baby Miller', 'page': 552}],
    'confusable_with': 'Standard epidural technique — requires modification for catecholamine-secreting tumors'
  },
]

# ============================================================
# [49] Approach to the Fall
# ============================================================
t = 'Approach to the Fall'
kps += [
  {
    'id': 'approach-to-the-fall-1',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'An on-call nurse reports a patient fall. What aspects of history and exam are most important in the immediate assessment?',
    'answer': 'Assess for injury (head, spine, fracture); determine mechanism (trip vs syncope vs sudden collapse — the last two suggest cardiac/neurologic cause); vital signs, neuro exam, orthostasis, medications (especially sedatives, antihypertensives, opioids).',
    'rationale': 'Falls from syncope or cardiac arrhythmia require urgent cardiac workup; traumatic injuries require imaging; polypharmacy is the most common modifiable cause in hospitalized patients.',
    'bloom': 'apply',
    'source': [{'book': 'Miller/Baby Miller', 'page': 222}],
    'confusable_with': 'Fall from trip (mechanical) — lowest acuity; syncope or seizure as cause requires urgent workup'
  },
  {
    'id': 'approach-to-the-fall-2',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'Anesthetic management after hip fracture from a fall should facilitate what recovery goal?',
    'answer': 'Anesthetic management and postoperative analgesia should facilitate an accelerated, enhanced recovery program with early mobilization; regional techniques (nerve blocks) support this by minimizing opioids.',
    'rationale': 'Early mobilization after hip fracture reduces VTE, pneumonia, deconditioning, and delirium; opioid-sparing regional analgesia enables faster physiotherapy engagement.',
    'bloom': 'apply',
    'source': [{'book': 'Morgan & Mikhail', 'page': 1313}],
    'confusable_with': 'Complete bed rest post-fracture — now contraindicated; ERAS protocols mandate early mobilization'
  },
  {
    'id': 'approach-to-the-fall-3',
    'topic': t, 'domain': dom_onc, 'discipline': dis,
    'stem': 'In the preoperative evaluation for a fall-related surgical procedure, what should guide evidence-based decision-making when formal guidelines are lacking?',
    'answer': 'Substantial clinical judgment is required; many clinical practice guidelines provide expert-opinion-based advice without clinical trial evidence — apply guidelines to the individual patient context.',
    'rationale': 'Perioperative medicine guidelines often extrapolate from non-surgical populations; individual comorbidities, frailty, and functional status must modify guideline-based decisions.',
    'bloom': 'analyze',
    'source': [{'book': 'Miller/Baby Miller', 'page': 222}],
    'confusable_with': 'Rigid guideline application — may be inappropriate for complex geriatric fall patients'
  },
]

print('Batch 4 KPs:', len(kps))
with open('data/_kp_part2_batch4.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print('Written.')
