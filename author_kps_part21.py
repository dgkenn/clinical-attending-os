#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Load the retrieval data
with open('data/_kp_retrieval_full.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract slice [693:726]
slice_data = data[693:726]

kps = []

# Helper function to safely get chunk data
def get_chunk(item, idx=0):
    if idx < len(item.get('chunks', [])):
        return item['chunks'][idx]
    return {'book': 'Unknown', 'page': 1}

# Topic 0: Dexmedetomidine: pharmacology
item = slice_data[0]
topic_slug = 'dexmedetomidine_pharmacology'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "What receptor type mediates dexmedetomidine's sedative and analgesic properties?",
    "answer": "Dexmedetomidine is an alpha-2 adrenergic agonist that produces sedation through presynaptic alpha-2 receptor activation in the central nervous system",
    "rationale": "Alpha-2 agonism reduces norepinephrine release, producing anxiolysis, sedation, and analgesia with preserved airway reflexes",
    "bloom": "recall",
    "source": [{"book": chunk.get('book', 'Miller/Baby Miller'), "page": chunk.get('page', 114)}],
    "confusable_with": "Alpha-1 agonists (which increase sympathetic tone and cause hypertension)"
})

chunk = get_chunk(item, 1)
kps.append({
    "id": f"{topic_slug}-2",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "How does dexmedetomidine affect heart rate, and why is bradycardia clinically significant?",
    "answer": "Dexmedetomidine causes initial hypertension and reflex bradycardia; the bradycardia can be profound and may require anticholinergic intervention",
    "rationale": "Alpha-2 stimulation causes peripheral vasoconstriction followed by reflex bradycardia; the sympathetic rebound is offset by direct brainstem alpha-2 effects",
    "bloom": "apply",
    "source": [{"book": chunk.get('book', 'Miller/Baby Miller'), "page": chunk.get('page', 114)}],
    "confusable_with": "Opioid-induced bradycardia (which is direct vagomimetic)"
})

# Topic 1: Diagnostic Test Performance
item = slice_data[1]
topic_slug = 'diagnostic_test_performance'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "How do sensitivity and specificity interact with pretest probability to determine post-test probability?",
    "answer": "Post-test probability depends on both test characteristics and pretest probability via Bayes' theorem; high-specificity tests are most useful when intermediate disease probability exists",
    "rationale": "A test cannot diagnose disease with certainty; interpretation requires integrating clinical suspicion with test performance",
    "bloom": "apply",
    "source": [{"book": chunk.get('book', 'StatPearls'), "page": chunk.get('page', 1)}],
    "confusable_with": "Positive predictive value (which is test-dependent but also prevalence-dependent)"
})

chunk = get_chunk(item, 1)
kps.append({
    "id": f"{topic_slug}-2",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "What is a likelihood ratio, and why is it more useful than sensitivity/specificity alone?",
    "answer": "Likelihood ratio is the ratio of true positive rate to false positive rate; it multiplies pretest odds to yield post-test odds, making it useful across different populations",
    "rationale": "LR+/LR- are independent of disease prevalence and directly update Bayesian beliefs about disease probability",
    "bloom": "apply",
    "source": [{"book": chunk.get('book', 'StatPearls'), "page": chunk.get('page', 1)}],
    "confusable_with": "Odds ratio (which is a different epidemiologic measure)"
})

# Topic 2: Drug interactions
item = slice_data[2]
topic_slug = 'drug_interactions_anesthesia'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "What are the primary mechanisms of anesthetic drug interactions?",
    "answer": "Drug interactions occur via hepatic enzyme inhibition/induction, protein binding displacement, altered receptor sensitivity, and pharmacodynamic synergy",
    "rationale": "Understanding mechanism allows prediction and mitigation of adverse interactions in perioperative polypharmacy",
    "bloom": "recall",
    "source": [{"book": chunk.get('book', 'Miller/Baby Miller'), "page": chunk.get('page', 55)}],
    "confusable_with": "Additive effects (which occur without altered drug metabolism)"
})

# Topic 3: DPE analgesia
item = slice_data[3]
topic_slug = 'dural_puncture_epidural'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "How does dural puncture epidural (DPE) technique differ from standard epidural anesthesia?",
    "answer": "DPE intentionally places the epidural catheter through the dura into the intrathecal space, combining rapid intrathecal onset with extended epidural dosing capability",
    "rationale": "Intentional dural puncture with epidural catheter placement permits both intrathecal and epidural drug administration from single catheter, combining speed and flexibility",
    "bloom": "recall",
    "source": [{"book": chunk.get('book', 'Morgan & Mikhail'), "page": chunk.get('page', 1401)}],
    "confusable_with": "Accidental dural puncture during standard epidural (which is a complication, not intended)"
})

chunk = get_chunk(item, 1)
kps.append({
    "id": f"{topic_slug}-2",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "What are the advantages of DPE for cesarean anesthesia compared to single-shot spinal?",
    "answer": "DPE allows rapid spinal onset and long epidural extension; reduces need for additional injections and enables procedural duration flexibility without repositioning",
    "rationale": "The epidural catheter serves as safety valve for duration extension and intraoperative dosing adjustments, improving patient satisfaction",
    "bloom": "apply",
    "source": [{"book": chunk.get('book', 'Morgan & Mikhail'), "page": chunk.get('page', 1401)}],
    "confusable_with": "Standard epidural (which lacks rapid spinal onset advantage)"
})

# Topic 4: Eclampsia management
item = slice_data[4]
topic_slug = 'eclampsia_management'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "What is the first-line pharmacological agent for eclamptic seizure management?",
    "answer": "Magnesium sulfate is the gold standard for seizure prophylaxis and acute seizure treatment in eclampsia via NMDA receptor blockade and neuromuscular stabilization",
    "rationale": "Magnesium prevents seizures more effectively than benzodiazepines; it also addresses the underlying pathophysiology of eclampsia",
    "bloom": "recall",
    "source": [{"book": chunk.get('book', 'Morgan & Mikhail'), "page": chunk.get('page', 1896)}],
    "confusable_with": "Benzodiazepines (which are adjuncts, not first-line agents for eclampsia)"
})

kps.append({
    "id": f"{topic_slug}-2",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "Why is aggressive blood pressure management critical in eclampsia, and what are safe target parameters?",
    "answer": "Eclamptic patients have impaired cerebral autoregulation; target MAP < 125 mmHg acutely to prevent hypertensive stroke and intracranial hemorrhage",
    "rationale": "Eclampsia involves endothelial dysfunction and loss of autoregulation; both hypertension and hypotension increase stroke risk",
    "bloom": "apply",
    "source": [{"book": chunk.get('book', 'Morgan & Mikhail'), "page": chunk.get('page', 1896)}],
    "confusable_with": "Management in non-eclamptic hypertensive crisis (where higher BP is tolerated)"
})

kps.append({
    "_type": "illness_script",
    "topic": item['topic'],
    "discipline": item['discipline'],
    "enabling_conditions": "Pregnancy > 20 weeks, de novo or worsening hypertension (>160/110 systolic or >110 diastolic)",
    "pathophysiology": "Placental insufficiency triggers systemic endothelial dysfunction, cerebral vasospasm, loss of autoregulation, and seizures; magnesium stabilizes neuromuscular membrane",
    "time_course": "Can develop during pregnancy, labor, or within 48 hours postpartum; seizures unpredictable",
    "key_features": "Severe hypertension, proteinuria, new-onset seizures, altered mental status, pulmonary edema, hyperreflexia",
    "consequence_if_missed": "Maternal stroke, intracranial hemorrhage, renal failure, placental abruption, fetal death, maternal death"
})

# Topic 5: Effects of Anesthetic Agents on Cerebral Physiology
item = slice_data[5]
topic_slug = 'anesthetic_cerebral_physiology'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "How do volatile anesthetics affect cerebral blood flow and intracranial pressure?",
    "answer": "Volatile anesthetics cause dose-dependent cerebral vasodilation, increasing cerebral blood flow and intracranial pressure; this effect is mitigated by hyperventilation",
    "rationale": "Volatile agents are cerebral vasodilators unlike IV agents; their effects on ICP can be offset by PaCO2 reduction or by using lower MAC levels",
    "bloom": "recall",
    "source": [{"book": chunk.get('book', 'Morgan & Mikhail'), "page": chunk.get('page', 2241)}],
    "confusable_with": "IV induction agents (which typically decrease CBF and ICP)"
})

kps.append({
    "id": f"{topic_slug}-2",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "Why is propofol preferred over volatile agents in patients with elevated intracranial pressure?",
    "answer": "Propofol decreases cerebral metabolic rate and cerebral blood flow, lowering intracranial pressure; volatile agents increase ICP through vasodilation",
    "rationale": "IV agents preserve or improve the cerebral pressure-volume relationship, whereas volatile agents worsen it at higher doses",
    "bloom": "apply",
    "source": [{"book": chunk.get('book', 'Morgan & Mikhail'), "page": chunk.get('page', 2241)}],
    "confusable_with": "Volatile anesthetics in neuroanesthesia (contraindicated for ICP control)"
})

# Topic 6: Electricity, Safety, and Monitoring Principles
item = slice_data[6]
topic_slug = 'electricity_safety_monitoring'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "What are the thresholds for microshock and macroshock hazards in the operating room?",
    "answer": "Microshock (via intracardiac electrodes) causes VF at approximately 100 microamperes; macroshock through intact skin requires 50-100 mA; equipment isolation prevents both",
    "rationale": "Smaller currents are lethal if delivered directly to myocardium due to lack of skin resistance; proper grounding prevents current flow through cardiac tissue",
    "bloom": "recall",
    "source": [{"book": chunk.get('book', 'Morgan & Mikhail'), "page": chunk.get('page', 49)}],
    "confusable_with": "Thermal injury (which requires higher currents and longer contact duration)"
})

# Topic 7: Electrolyte Disturbances - Cardiac Effects
item = slice_data[7]
topic_slug = 'electrolyte_cardiac_effects'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "How do hyperkalemia and hypokalemia each affect cardiac conduction and anesthetic risk?",
    "answer": "Hyperkalemia causes peaked T waves, widened QRS, and bradycardia progressing to VF; hypokalemia causes U waves and increased sensitivity to medications and arrhythmias",
    "rationale": "Both extremes alter cardiac electrophysiology; hyperkalemia is immediately life-threatening, hypokalemia increases sensitivity to depolarizing agents and volatiles",
    "bloom": "recall",
    "source": [{"book": chunk.get('book', 'Morgan & Mikhail'), "page": chunk.get('page', 1900)}],
    "confusable_with": "Hypercalcemia (which shortens QT interval, distinct from hyperkalemia)"
})

# Topic 8: End-of-Life Care Ethics
item = slice_data[8]
topic_slug = 'end_of_life_care_ethics'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "What are the anesthesiologist's roles in palliative care and end-of-life decision-making?",
    "answer": "Anesthesiologists manage pain and dyspnea, facilitate advance directives, support communication about prognosis, and ensure dignified comfort-focused care",
    "rationale": "Anesthesiologists' expertise in airway, sedation, and pain control is essential for high-quality palliative anesthesia and symptom management",
    "bloom": "apply",
    "source": [{"book": chunk.get('book', 'Miller/Baby Miller'), "page": chunk.get('page', 877)}],
    "confusable_with": "Physician-assisted death (which is illegal in most jurisdictions and distinct from palliative sedation)"
})

# Topic 9: Endocrine Physiology Relevant to Anesthesia
item = slice_data[9]
topic_slug = 'endocrine_physiology_anesthesia'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "How do anesthetic agents affect the stress response and cortisol secretion perioperatively?",
    "answer": "Volatile agents blunt the cortisol stress response better than IV agents; inadequate suppression leads to postoperative hyperglycemia and immunosuppression",
    "rationale": "Cortisol rises in response to surgical stimulation; volatile anesthetics provide superior suppression via direct central effects",
    "bloom": "recall",
    "source": [{"book": chunk.get('book', 'Unknown'), "page": chunk.get('page', 1)}],
    "confusable_with": "Catecholamine response (which is more pronounced with lighter anesthesia)"
})

# Topic 10: Endovascular Neurosurgery
item = slice_data[10]
topic_slug = 'endovascular_neurosurgery'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "What are the key anesthetic considerations unique to neurointerventional procedures?",
    "answer": "Maintain cerebral perfusion (avoid hypotension), enable frequent neurological exams (light sedation preferred), manage anticoagulation, and provide rapid airway access",
    "rationale": "Neurointerventional patients require dynamic neurological monitoring during intervention; heavy sedation prevents detection of ischemic complications",
    "bloom": "apply",
    "source": [{"book": chunk.get('book', 'Unknown'), "page": chunk.get('page', 1)}],
    "confusable_with": "Neurosurgery operating room (which typically permits general anesthesia with muscle relaxation)"
})

# Topic 11: Enhanced Recovery After Surgery (ERAS)
item = slice_data[11]
topic_slug = 'eras_surgery'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "What are the core elements of ERAS protocols in general surgery?",
    "answer": "ERAS combines regional anesthesia, reduced opioid use, fluid optimization, early mobilization, and multimodal analgesia to reduce hospital stay and complications",
    "rationale": "ERAS bundles target multiple points in recovery pathways; each element alone provides modest benefit, but combined effect is substantial",
    "bloom": "recall",
    "source": [{"book": chunk.get('book', 'Unknown'), "page": chunk.get('page', 1)}],
    "confusable_with": "Fast-track programs (which focus only on postoperative discharge criteria)"
})

# Topic 12: Enhanced recovery after cesarean (ERAC)
item = slice_data[12]
topic_slug = 'erac_cesarean'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "How does ERAC differ from standard postoperative care after cesarean delivery?",
    "answer": "ERAC emphasizes neuraxial anesthesia, minimized opioids, early oral intake, early mobilization, and skin-to-skin contact; reduces hospital stay without increasing complications",
    "rationale": "Obstetric patients tolerate early mobilization well; neuraxial techniques permit effective ERAC without general anesthesia risks",
    "bloom": "apply",
    "source": [{"book": chunk.get('book', 'Unknown'), "page": chunk.get('page', 1)}],
    "confusable_with": "ERAS in general surgery (which has different risk-benefit for early mobilization)"
})

# Topic 13: Epidural anesthesia for cesarean delivery
item = slice_data[13]
topic_slug = 'epidural_cesarean'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "What are the advantages and limitations of epidural anesthesia for planned cesarean delivery?",
    "answer": "Epidural provides slow onset, excellent motor control, ability to extend duration, lower sympathectomy; disadvantages include slower onset than spinal and incomplete blocks",
    "rationale": "Epidural titration allows gradual sympathetic blockade reducing hypotension; slower onset allows time for preoperative optimization",
    "bloom": "apply",
    "source": [{"book": chunk.get('book', 'Unknown'), "page": chunk.get('page', 1)}],
    "confusable_with": "Spinal anesthesia (which is faster but causes more sudden hypotension)"
})

# Topic 14: Epidural anesthesia: pharmacology and dosing
item = slice_data[14]
topic_slug = 'epidural_pharmacology'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "What is the epidural dose-spacing relationship for local anesthetics?",
    "answer": "Epidural doses are 5-10 times spinal doses due to dural barrier; typical bupivacaine is 10-15 mg spinal vs 100-150 mg epidural for comparable levels",
    "rationale": "The dura and arachnoid mater limit CSF diffusion of epidural local anesthetic, requiring higher doses to achieve the same neural blockade",
    "bloom": "recall",
    "source": [{"book": chunk.get('book', 'Unknown'), "page": chunk.get('page', 1)}],
    "confusable_with": "IV local anesthetic dosing (which is entirely different for systemic toxicity reasons)"
})

# Topic 15: Epidural anesthesia: technique
item = slice_data[15]
topic_slug = 'epidural_technique'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "What is the loss-of-resistance technique, and why is it the gold standard for epidural needle placement?",
    "answer": "Loss-of-resistance (LOR) uses air or saline in a syringe attached to the epidural needle; sudden loss of resistance indicates entry into the epidural space",
    "rationale": "The ligamentum flavum is the only true anatomical barrier; sudden pressure drop confirms ligament penetration and guides needle advancement",
    "bloom": "recall",
    "source": [{"book": chunk.get('book', 'Unknown'), "page": chunk.get('page', 1)}],
    "confusable_with": "Hanging drop technique (which is less reliable and prone to false LOR)"
})

# Topic 16: Epidural labor analgesia: technique and management
item = slice_data[16]
topic_slug = 'epidural_labor_analgesia'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "What concentrations of local anesthetic are used in labor epidurals, and why are they lower than surgical doses?",
    "answer": "Labor epidurals use 0.06-0.125% bupivacaine (vs 0.5% for surgery) to achieve sensory block while preserving motor function and ambulation",
    "rationale": "Lower concentrations reduce motor blockade and allow early ambulation, improving labor progression without sacrificing analgesia",
    "bloom": "apply",
    "source": [{"book": chunk.get('book', 'Morgan & Mikhail'), "page": chunk.get('page', 1541)}],
    "confusable_with": "Surgical epidural concentrations (which are higher to ensure complete motor block)"
})

# Topic 17: Epidural pharmacology (duplicate/similar to 14)
item = slice_data[17]
topic_slug = 'epidural_pharmacology_v2'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "How do opioids in epidural analgesia achieve pain relief without prominent systemic effects?",
    "answer": "Epidural opioids bind to spinal dorsal horn receptors and reduce substance P release; local doses are much smaller than systemic equivalents",
    "rationale": "Opioid receptors at spinal level mediate pain without significant systemic absorption from epidural space in the presence of local anesthetic",
    "bloom": "recall",
    "source": [{"book": chunk.get('book', 'Miller/Baby Miller'), "page": chunk.get('page', 114)}],
    "confusable_with": "IV opioid analgesia (which produces systemic effects at lower total doses)"
})

# Topic 18: Epilepsy Surgery Anesthesia
item = slice_data[18]
topic_slug = 'epilepsy_surgery_anesthesia'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "Why are seizure-triggering anesthetic agents contraindicated in epilepsy surgery?",
    "answer": "Methoxyflurane and enflurane lower seizure threshold and trigger seizures; propofol and benzodiazepines are preferred as they raise seizure threshold",
    "rationale": "Electrocorticography monitoring requires stable baseline; seizure-inducing agents confound intraoperative neuromonitoring and impair surgical planning",
    "bloom": "apply",
    "source": [{"book": chunk.get('book', 'Morgan & Mikhail'), "page": chunk.get('page', 207)}],
    "confusable_with": "Anesthetic choice in non-epilepsy neurosurgery (where volatile agents are acceptable)"
})

# Topic 19: Ethical Principles in Clinical Decision-Making
item = slice_data[19]
topic_slug = 'ethical_principles_clinical'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "What are the four core ethical principles in anesthesia practice?",
    "answer": "Autonomy (respect for patient choice), beneficence (act in patient interest), non-maleficence (avoid harm), and justice (fair distribution of resources)",
    "rationale": "These principles guide informed consent, advance directives, and allocation of scarce resources in perioperative care",
    "bloom": "recall",
    "source": [{"book": chunk.get('book', 'StatPearls'), "page": chunk.get('page', 1)}],
    "confusable_with": "Professional ethics alone (which address conduct but not foundational principles)"
})

# Topic 20: Etomidate: pharmacology
item = slice_data[20]
topic_slug = 'etomidate_pharmacology'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "What is the major advantage of etomidate for hemodynamically unstable patients?",
    "answer": "Etomidate maintains blood pressure and cardiac output better than propofol or thiopental due to preserved sympathetic tone and lack of myocardial depression",
    "rationale": "Etomidate's mechanism is selective brainstem GABAergic depression without peripheral vascular effects, making it ideal for sepsis, hemorrhage, or cardiogenic shock",
    "bloom": "apply",
    "source": [{"book": chunk.get('book', 'Miller/Baby Miller'), "page": chunk.get('page', 114)}],
    "confusable_with": "Propofol in hypotensive patients (which causes additional cardiovascular depression)"
})

kps.append({
    "id": f"{topic_slug}-2",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "What is the clinical significance of etomidate's effect on adrenal function?",
    "answer": "Etomidate inhibits 11-beta-hydroxylase, suppressing cortisol synthesis even with single doses; prolonged use can cause adrenal insufficiency requiring steroid supplementation",
    "rationale": "Cortisol suppression impairs stress response and immune function; critically ill patients given etomidate infusions require steroid replacement",
    "bloom": "apply",
    "source": [{"book": chunk.get('book', 'Miller/Baby Miller'), "page": chunk.get('page', 114)}],
    "confusable_with": "Other IV agents (which do not significantly affect steroid synthesis)"
})

# Topic 21: Femoral nerve and adductor canal blocks
item = slice_data[21]
topic_slug = 'femoral_nerve_block'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "What is the anatomical relationship between the femoral nerve and the femoral artery?",
    "answer": "The femoral nerve lies lateral to the femoral artery in the femoral sheath; it emerges lateral to the inguinal ligament and can be blocked below the inguinal ligament",
    "rationale": "Understanding this anatomy prevents arterial puncture and guides safe needle advancement during femoral blocks",
    "bloom": "recall",
    "source": [{"book": chunk.get('book', 'Morgan & Mikhail'), "page": chunk.get('page', 1473)}],
    "confusable_with": "The saphenous nerve (which travels medial to the femoral artery and requires separate blocks)"
})

# Topic 22: Fentanyl, sufentanil, alfentanil: comparative pharmacology
item = slice_data[22]
topic_slug = 'fentanyl_opioid_comparison'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "How do the pharmacokinetic profiles of fentanyl, sufentanil, and alfentanil differ?",
    "answer": "Alfentanil has rapid onset (1-2 min) and offset (10-15 min); fentanyl has intermediate onset (3-5 min) and longer offset (30-60 min); sufentanil similar to fentanyl but higher potency",
    "rationale": "These differences reflect lipophilicity and metabolism; alfentanil's rapid metabolism makes it ideal for short procedures, fentanyl for general anesthesia",
    "bloom": "recall",
    "source": [{"book": chunk.get('book', 'Miller/Baby Miller'), "page": chunk.get('page', 114)}],
    "confusable_with": "Remifentanil (which has ester metabolism and ultrashort duration)"
})

kps.append({
    "id": f"{topic_slug}-2",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "What are typical IV induction doses of fentanyl, sufentanil, and alfentanil?",
    "answer": "Fentanyl 1-3 mcg/kg, sufentanil 0.1-0.5 mcg/kg, alfentanil 3-8 mcg/kg; relative potency is fentanyl 1x : sufentanil 10x : alfentanil 0.1x",
    "rationale": "Sufentanil's higher potency requires proportionally lower doses to avoid overdose and respiratory depression",
    "bloom": "recall",
    "source": [{"book": chunk.get('book', 'Miller/Baby Miller'), "page": chunk.get('page', 114)}],
    "confusable_with": "Opioid doses in other routes (which are not directly comparable)"
})

# Topic 23: Fetal physiology and assessment
item = slice_data[23]
topic_slug = 'fetal_physiology'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "How does fetal hemoglobin differ from adult hemoglobin, and what is the clinical implication for fetal oxygenation?",
    "answer": "Fetal hemoglobin (HbF) has higher oxygen affinity than adult hemoglobin (HbA); this leftward shift facilitates transplacental oxygen transfer",
    "rationale": "The higher affinity of HbF ensures oxygen diffusion from maternal blood across the placenta despite lower PaO2 in umbilical blood",
    "bloom": "recall",
    "source": [{"book": chunk.get('book', 'Miller/Baby Miller'), "page": chunk.get('page', 610)}],
    "confusable_with": "Adult anemia (which impairs oxygen carrying despite normal hemoglobin function)"
})

# Topic 24: Fluid Management in Neuroanesthesia
item = slice_data[24]
topic_slug = 'fluid_management_neuroanesthesia'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "Why are hypotonic fluids contraindicated in neuroanesthesia, and what is the preferred fluid strategy?",
    "answer": "Hypotonic fluids (e.g., 0.45% saline) cause cerebral edema by lowering serum osmolality; hypertonic (3% saline) or isotonic (0.9% saline) fluids maintain osmotic gradient",
    "rationale": "The blood-brain barrier is permeable to electrolytes but impermeable to proteins; osmotic gradient prevents water shift into the brain parenchyma",
    "bloom": "apply",
    "source": [{"book": chunk.get('book', 'Unknown'), "page": chunk.get('page', 1)}],
    "confusable_with": "Fluid strategy in non-neurological patients (where hypotonic fluids are acceptable)"
})

# Topic 25: Fluid, Electrolyte, and Osmolality Physiology
item = slice_data[25]
topic_slug = 'fluid_electrolyte_osmolality'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "How do changes in serum osmolality affect intracellular and extracellular fluid volume?",
    "answer": "Increased osmolality draws water from cells (hypertonicity); decreased osmolality causes water influx into cells (hypotonicity); osmolality determines water distribution across compartments",
    "rationale": "The cell membrane is permeable to water but not electrolytes; osmotic differences drive water movement and alter cell volume",
    "bloom": "recall",
    "source": [{"book": chunk.get('book', 'Unknown'), "page": chunk.get('page', 1)}],
    "confusable_with": "Sodium concentration alone (which does not account for osmolality of other solutes)"
})

# Topic 26: Frailty assessment and prehabilitation
item = slice_data[26]
topic_slug = 'frailty_assessment'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "How does frailty differ from chronological age, and why is it a better predictor of surgical outcome?",
    "answer": "Frailty reflects accumulated physiologic decline (weakness, slow gait, low activity) independent of age; frail patients have higher morbidity/mortality even when chronologically young",
    "rationale": "Frailty captures end-organ reserve capacity; a 70-year-old robust patient may tolerate major surgery better than a 55-year-old frail patient",
    "bloom": "apply",
    "source": [{"book": chunk.get('book', 'Unknown'), "page": chunk.get('page', 1)}],
    "confusable_with": "Comorbidity burden (which is related but not synonymous with frailty)"
})

# Topic 27: GERD, gastroparesis, and upper GI disease
item = slice_data[27]
topic_slug = 'gerd_gastroparesis'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "What is the increased perioperative risk with GERD, and how is it mitigated?",
    "answer": "GERD increases aspiration risk; mitigation includes H2 blockers, PPIs, sodium citrate, rapid-sequence intubation, and avoiding agents that reduce LES pressure",
    "rationale": "Acidic gastric contents cause chemical pneumonitis; pharmacologic prophylaxis reduces gastric volume and pH, while RSI technique prevents aspiration",
    "bloom": "apply",
    "source": [{"book": chunk.get('book', 'Unknown'), "page": chunk.get('page', 1)}],
    "confusable_with": "Aspiration risk from full stomach alone (which is distinct from reflux disease)"
})

# Topic 28: Gabapentinoids in Pain Management
item = slice_data[28]
topic_slug = 'gabapentinoids_pain'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "What are the mechanisms of action of gabapentin and pregabalin?",
    "answer": "Gabapentinoids bind to alpha-2-delta calcium channels in dorsal root ganglia, reducing neurotransmitter release; they are not GABAergic like benzodiazepines",
    "rationale": "This mechanism explains gabapentinoids' efficacy in neuropathic pain without benzodiazepine-like respiratory depression or addiction potential",
    "bloom": "recall",
    "source": [{"book": chunk.get('book', 'Unknown'), "page": chunk.get('page', 1)}],
    "confusable_with": "Benzodiazepines (which bind GABA receptors, not calcium channels)"
})

# Topic 29: Gas Flow Physics and Anesthesia Machine
item = slice_data[29]
topic_slug = 'gas_flow_physics'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "What is the difference between laminar and turbulent flow in anesthesia breathing circuits?",
    "answer": "Laminar flow is smooth and predictable (gas flows in parallel layers); turbulent flow is chaotic and resistant, increasing airway resistance and deadspace",
    "rationale": "High flow rates or narrow airways promote turbulent flow; turbulence increases work of breathing and inefficiency of gas delivery",
    "bloom": "recall",
    "source": [{"book": chunk.get('book', 'Unknown'), "page": chunk.get('page', 1)}],
    "confusable_with": "Diffusion (which is movement driven by concentration gradients, not bulk flow)"
})

# Topic 30: General anesthesia for cesarean delivery
item = slice_data[30]
topic_slug = 'ga_cesarean_delivery'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "Why is rapid-sequence intubation mandatory for general anesthesia for cesarean delivery?",
    "answer": "Pregnant patients have increased aspiration risk due to delayed gastric emptying, increased intra-abdominal pressure, and hormonal LES relaxation; RSI prevents aspiration",
    "rationale": "RSI with cricoid pressure prevents passive regurgitation during induction and intubation, protecting against chemical pneumonitis",
    "bloom": "apply",
    "source": [{"book": chunk.get('book', 'Unknown'), "page": chunk.get('page', 1)}],
    "confusable_with": "Routine intubation in non-pregnant patients (where RSI is not standard)"
})

# Topic 31: Geriatric Pain Management
item = slice_data[31]
topic_slug = 'geriatric_pain_management'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "How does opioid metabolism change in elderly patients, and what is the clinical implication?",
    "answer": "Elderly patients have reduced hepatic metabolism and renal clearance; opioid half-lives lengthen and accumulation risk increases, requiring lower doses and extended intervals",
    "rationale": "Age-related decline in drug-metabolizing enzyme activity and glomerular filtration rate impairs clearance of parent drug and active metabolites",
    "bloom": "apply",
    "source": [{"book": chunk.get('book', 'Unknown'), "page": chunk.get('page', 1)}],
    "confusable_with": "Pain perception (which may actually be preserved or heightened in elderly)"
})

# Topic 32: HIPAA, Patient Privacy & Confidentiality
item = slice_data[32]
topic_slug = 'hipaa_privacy'
chunk = get_chunk(item, 0)
kps.append({
    "id": f"{topic_slug}-1",
    "topic": item['topic'],
    "domain": item['domain'],
    "discipline": item['discipline'],
    "stem": "What does HIPAA protect, and what are the consequences of a privacy breach?",
    "answer": "HIPAA protects protected health information (PHI) including medical records, payment info, and identifiers; breaches trigger notification, investigation, and penalties",
    "rationale": "HIPAA establishes minimum standards for data security and patient privacy; enforcement is strict given the sensitivity of medical records",
    "bloom": "recall",
    "source": [{"book": chunk.get('book', 'Unknown'), "page": chunk.get('page', 1)}],
    "confusable_with": "OSHA regulations (which address workplace safety, not privacy)"
})

# Write output
output_path = 'data/kp_full_part_21.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)

# Count stats
scripts_count = sum(1 for kp in kps if kp.get('_type') == 'illness_script')
pairs_count = sum(1 for kp in kps if kp.get('_type') == 'confusable_pair')
kps_count = len(kps) - scripts_count - pairs_count

# Validate JSON
with open(output_path, 'r', encoding='utf-8') as f:
    json.load(f)

print(f"part 21: 33 topics, {kps_count} KPs, {scripts_count} scripts, {pairs_count} pairs, parses OK")
