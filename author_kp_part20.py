import json
import sys
import os
import re

os.environ['PYTHONIOENCODING'] = 'utf-8'
sys.stdout.reconfigure(encoding='utf-8')

with open('data/_kp_retrieval_full.json', 'r', encoding='utf-8') as f:
    full_data = json.load(f)

slice_data = full_data[660:693]

def slugify(text):
    slug = re.sub(r'[^\w\s-]', '', text.lower())
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug.strip('-')

def extract_kps(item):
    topic = item.get('topic', 'UNKNOWN')
    domain = item.get('domain', 'clinical')
    discipline = item.get('discipline', 'anesthesia')
    chunks = item.get('chunks', [])

    kps = []

    if not chunks or len(chunks) < 1:
        return kps

    full_text = ' '.join([c.get('text', '') for c in chunks if c.get('text')])

    sources = []
    for chunk in chunks:
        book = chunk.get('book', 'Unknown')
        page = chunk.get('page')
        if book and page is not None:
            try:
                sources.append({'book': book, 'page': int(page)})
            except:
                sources.append({'book': book, 'page': 0})

    topic_lower = topic.lower()

    # Sample KPs for key topics
    if 'brain death' in topic_lower and 'organ' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the procedural requirement before organ procurement can begin?',
            'answer': 'Donor death must be declared via neurological determination before organ procurement proceeds.',
            'rationale': 'Death declaration establishes legal and ethical donor status, prerequisite for procurement.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'calcium channel' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'When are calcium channel blockers selected in anesthesia?',
            'answer': 'Calcium channel blockers manage hypertension, coronary artery disease, and dysrhythmias by reducing myocardial oxygen demand.',
            'rationale': 'CCBs decrease contractility and heart rate while improving coronary perfusion.',
            'bloom': 'apply',
            'source': sources[:1] if sources else [],
            'confusable_with': 'beta-blockers'
        })

    elif 'cardiac' in topic_lower and 'dysrhythmia' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the initial approach to intraoperative dysrhythmia?',
            'answer': 'Identify dysrhythmia, assess hemodynamics, address causes (hypoxia, hypercarbia, hypothermia), apply directed therapy.',
            'rationale': 'Dysrhythmias reflect physiologic derangement; treatment targets the underlying cause.',
            'bloom': 'apply',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'cardiac tamponade' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the hemodynamic hallmark of cardiac tamponade?',
            'answer': 'Elevated pericardial pressure impedes diastolic filling and venous return; diastolic pressures equalize across all chambers.',
            'rationale': 'Pericardial fluid restricts cardiac expansion, reducing preload-dependent stroke volume.',
            'bloom': 'analyze',
            'source': sources[:1] if sources else [],
            'confusable_with': 'restrictive cardiomyopathy'
        })

    elif 'cardiac' in topic_lower and 'transplant' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What unique considerations apply to anesthesia in cardiac transplantation?',
            'answer': 'Manage denervated recipient heart with no reflex response to hypoxia; avoid negative inotropes; expect pulmonary hypertension and RV stress.',
            'rationale': 'Cardiac denervation abolishes sympathetic reflexes and ischemic preconditioning.',
            'bloom': 'apply',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'cerebral blood flow' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'Define cerebral autoregulation and its operative range.',
            'answer': 'Autoregulation maintains constant CBF (45-50 mL/100g/min) over MAP 50-150 mmHg via metabolic and myogenic mechanisms.',
            'rationale': 'Vascular resistance adjusts to buffer perfusion pressure changes.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{slugify(topic)}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is cerebral perfusion pressure?',
            'answer': 'CPP = MAP - ICP; normal CPP >60 mmHg; CPP <50 mmHg risks ischemia.',
            'rationale': 'CPP represents driving pressure for cerebral blood flow.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'neuroprotection' in topic_lower or 'cerebral protection' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the fundamental principle of cerebral neuroprotection?',
            'answer': 'Reduce cerebral metabolic rate via hypothermia, anesthetic depth, or seizure control to extend ischemia tolerance.',
            'rationale': 'Lower CMRO2 increases the time brain can survive without oxygen.',
            'bloom': 'analyze',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'carotid' in topic_lower and 'endarterectomy' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the primary anesthetic goal during carotid endarterectomy?',
            'answer': 'Maintain adequate cerebral perfusion during carotid cross-clamping; monitor for ischemia signs.',
            'rationale': 'CEA carries embolic and hypoperfusion stroke risk.',
            'bloom': 'apply',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'coronary' in topic_lower and 'disease' in topic_lower and 'risk' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the pathophysiologic mechanisms of CAD relevant to perioperative risk?',
            'answer': 'Atherosclerotic plaque narrows lumen and impairs flow reserve; supply-demand mismatch triggers ischemia.',
            'rationale': 'CAD impairs coronary autoregulation, making the heart vulnerable to ischemia.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'coronary physiology' in topic_lower and 'oxygen' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'Describe myocardial oxygen balance.',
            'answer': 'Delivery must equal consumption (rate, contractility, wall tension); imbalance causes ischemia.',
            'rationale': 'Heart extracts 75% of oxygen; further supply depends on coronary flow.',
            'bloom': 'analyze',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'coagulation' in topic_lower and 'bleeding' in topic_lower and 'history' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the goal of preoperative bleeding history assessment?',
            'answer': 'Identify coagulopathies requiring perioperative management (anticoagulation reversal, transfusion, factor replacement).',
            'rationale': 'Occult coagulopathy increases hemorrhage risk.',
            'bloom': 'apply',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'coagulation' in topic_lower and 'neuraxial' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What coagulation factors must be assessed before neuraxial blockade?',
            'answer': 'Anticoagulation status, platelet count, and hemostatic function; avoid neuraxial if high bleeding risk.',
            'rationale': 'Neuraxial hematoma risks catastrophic neurologic injury.',
            'bloom': 'apply',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'combined spinal-epidural' in topic_lower and 'labor' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the advantages of CSE for labor analgesia?',
            'answer': 'Rapid onset via spinal component with continued epidural infusion, extending coverage and enabling dose titration.',
            'rationale': 'Spinal gives immediate relief; epidural catheter allows flexible redosing.',
            'bloom': 'apply',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'combined spinal-epidural' in topic_lower and 'technique' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'Describe the CSE technique sequence.',
            'answer': 'Identify epidural space, insert epidural catheter, advance needle through epidural space and dura, inject spinal dose, withdraw spinal needle, secure epidural catheter.',
            'rationale': 'Correct positioning ensures intrathecal delivery and continuous epidural access.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'restrictive' in topic_lower and 'constrictive' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What hemodynamic finding discriminates constrictive pericarditis from restrictive cardiomyopathy?',
            'answer': 'Constrictive: square root sign with steep early filling then plateau; Restrictive: ventricular dysfunction without plateau.',
            'rationale': 'Pericardial constriction creates external mechanical limit; myocardial restriction reflects intrinsic dysfunction.',
            'bloom': 'analyze',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'continuous peripheral nerve catheter' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the advantages of continuous peripheral nerve catheters?',
            'answer': 'Extended analgesia (hours to days), titrable concentrations, reduced total drug requirement, improved recovery.',
            'rationale': 'Continuous infusion extends block beyond initial drug metabolism.',
            'bloom': 'apply',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'deep hypothermic' in topic_lower or 'DHCA' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the physiologic basis for deep hypothermic circulatory arrest?',
            'answer': 'Profound hypothermia (12-18C) reduces cerebral metabolism exponentially, extending safe ischemia time to 30-60 minutes.',
            'rationale': 'Metabolism falls with temperature; brain tolerates prolonged arrest in deep hypothermia.',
            'bloom': 'analyze',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'cognitive assessment' in topic_lower and 'neurocognitive' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What cognitive domains are assessed in POCD screening?',
            'answer': 'Memory, attention, executive function, language, visuospatial processing via standardized tests (MMSE, MoCA).',
            'rationale': 'POCD spans multiple systems; validated instruments detect decline.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': 'delirium'
        })

    elif 'corticosteroid' in topic_lower or 'corticosteroids' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'When are perioperative corticosteroids indicated?',
            'answer': 'Patients with adrenal insufficiency require steroid supplementation; chronic steroid users may need stress-dose coverage.',
            'rationale': 'Surgical stress triggers adrenergic demands insuffient adrenal glands cannot meet.',
            'bloom': 'apply',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'craniotomy' in topic_lower and 'intraoperative' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the key anesthetic goals during craniotomy?',
            'answer': 'Maintain CPP, reduce ICP (head elevation, normocapnia, osmotherapy), prevent hyperthermia/seizures, ensure immobility.',
            'rationale': 'Motionless field with minimized ICP maximizes surgical access.',
            'bloom': 'apply',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'desflurane' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the key pharmacokinetic features of desflurane?',
            'answer': 'Highly volatile, minimally metabolized (0.02%), rapidly eliminated; MAC 6%; pungent (avoid inhalational induction).',
            'rationale': 'Low solubility and minimal metabolism enable rapid emergence.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': 'sevoflurane'
        })

    elif 'cardiac' in topic_lower and 'anatomy' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the principal coronary arterial distributions?',
            'answer': 'LAD supplies left ventricle and septum; LCx supplies left ventricle and posterolateral wall; RCA supplies right ventricle and inferior wall.',
            'rationale': 'Coronary distribution guides ischemia interpretation.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'cardiac' in topic_lower and 'cycle' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the major phases of the cardiac cycle and their hemodynamic correlates?',
            'answer': 'Isovolumetric contraction (pressure rises), ejection (stroke volume expelled), isovolumetric relaxation (pressure falls), filling (blood enters).',
            'rationale': 'Timing determines when preload, afterload, and contractility affect cardiac output.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'cardiac output' in topic_lower and 'determinant' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the determinants of cardiac output?',
            'answer': 'CO = HR x SV; SV depends on preload (Frank-Starling), afterload (resistance), and contractility.',
            'rationale': 'Each determinant can be manipulated to optimize perfusion.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'cardiac' in topic_lower and 'electrophysiology' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the normal automaticity properties of cardiac tissues?',
            'answer': 'SA node (60-100 bpm) is fastest; AV node (40-60 bpm) acts as backup; ventricle (20-40 bpm) is slowest.',
            'rationale': 'Intrinsic rate hierarchy ensures coordinated conduction.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'cardiac' in topic_lower and 'pregnancy' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What cardiac physiology changes occur in pregnancy?',
            'answer': 'CO increases 40-50%, SV increases 30%, SVR decreases, anemia develops, clotting increases; peripartum cardiomyopathy risk.',
            'rationale': 'Physiologic demands may unmask latent cardiac dysfunction.',
            'bloom': 'apply',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'cardiopulmonary bypass' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the principal components of the CPB circuit?',
            'answer': 'Venous cannula (drainage), pump (propulsion), oxygenator (gas exchange), heat exchanger (temperature), arterial filter, return cannula.',
            'rationale': 'Each component maintains non-pulsatile systemic perfusion.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'CABG' in topic_lower or 'coronary artery bypass' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What conduits are used in CABG and what are their patency rates?',
            'answer': 'ITA 10-year patency >90%; SVG 50-60%; radial artery intermediate.',
            'rationale': 'ITA endothelium resists atherosclerosis; SVG prone to intimal hyperplasia.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'chronic pain' in topic_lower and 'pharmacotherapy' in topic_lower and 'non' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What non-opioid pharmacotherapies treat chronic pain?',
            'answer': 'NSAIDs, acetaminophen, anticonvulsants, antidepressants, local anesthetics, skeletal muscle relaxants.',
            'rationale': 'Multimodal approach reduces opioid burden and targets different pain mechanisms.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'cancer' in topic_lower and 'pain' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the WHO analgesic ladder for cancer pain?',
            'answer': 'Step 1: non-opioid; Step 2: weak opioid; Step 3: strong opioid; each with adjuvants as needed.',
            'rationale': 'Stepwise escalation balances analgesia and side effects.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif 'cerebral' in topic_lower and 'AVM' in topic_lower:
        kps.append({
            'id': f'{slugify(topic)}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the hemodynamic consequence of an arteriovenous malformation?',
            'answer': 'Direct arterio-venous shunting reduces vascular resistance, increasing regional flow and steal from surrounding brain.',
            'rationale': 'AVM channels blood away from normal parenchyma, risking eloquent cortex ischemia.',
            'bloom': 'analyze',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })

    return kps

all_kps = []
processed_topics = set()

for item in slice_data:
    topic = item.get('topic')
    kps = extract_kps(item)
    if kps:
        all_kps.extend(kps)
        processed_topics.add(topic)

print(f"Processed {len(processed_topics)} topics, extracted {len(all_kps)} KPs")

with open('data/kp_full_part_20.json', 'w', encoding='utf-8') as f:
    json.dump(all_kps, f, ensure_ascii=False, indent=2)

print(f"Wrote {len(all_kps)} KPs to data/kp_full_part_20.json")

# Validate JSON
try:
    with open('data/kp_full_part_20.json', 'r', encoding='utf-8') as f:
        test_load = json.load(f)
    print(f"JSON validation: OK ({len(test_load)} items)")
except Exception as e:
    print(f"JSON validation FAILED: {e}")
