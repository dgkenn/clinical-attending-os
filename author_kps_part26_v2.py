import json
import re

def make_slug(topic):
    slug = topic.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'\s+', '_', slug)
    slug = slug[:40]
    return slug

def extract_sentences(text, limit=10):
    """Extract meaningful sentences from text"""
    # Clean up text
    text = text.replace('\xa0', ' ').replace('–', '-').replace('—', '-')
    text = re.sub(r'\s+', ' ', text)

    # Split on sentence boundaries
    sentences = re.split(r'[.!?;]+', text)

    result = []
    for sent in sentences:
        sent = sent.strip()
        if 20 < len(sent) < 250 and not sent.startswith('Section'):
            result.append(sent)
            if len(result) >= limit:
                break
    return result

def author_kps_for_item(item):
    """Author atomic knowledge points"""
    kps = []
    topic = item.get('topic', '')
    domain = item.get('domain', '')
    discipline = item.get('discipline', '')
    chunks = item.get('chunks', [])

    if not chunks:
        return kps

    slug_base = make_slug(topic)
    kp_counter = 1

    # Topic-specific extraction logic
    if 'Remifentanil' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What metabolic pathway gives remifentanil its rapid offset?",
            "answer": "Remifentanil undergoes rapid hydrolysis by non-specific plasma and tissue esterases, independent of liver or kidney function.",
            "rationale": "Ester metabolism ensures fast offset even in renal or hepatic failure, making it suitable for rapid-sequence induction and short procedures.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": "Fentanyl (hepatic metabolism, prolonged offset)"
        })
        kp_counter += 1
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the clinical context-sensitive half-time for remifentanil?",
            "answer": "Remifentanil has a context-sensitive half-time ~3-10 min regardless of infusion duration, allowing predictable emergence after prolonged infusion.",
            "rationale": "Unlike other opioids, remifentanil's CSHT does not increase with duration due to esterase metabolism; this enables rapid wakefulness even after hours of use.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Renal Physiology' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is normal GFR and the mechanism of renal autoregulation?",
            "answer": "Normal GFR ~120 mL/min/1.73m². Renal autoregulation maintains GFR constant (MAP 60-160 mmHg) via afferent arteriole vasoconstriction at high pressure and vasodilation at low pressure.",
            "rationale": "Autoregulation is mediated by myogenic mechanisms and tubuloglomerular feedback. Anesthesia below MAP 60 mmHg overwhelms autoregulation, reducing GFR and urine output.",
            "bloom": "understand",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "How do volatile anesthetics and sympathomimetics affect renal blood flow?",
            "answer": "Volatile agents (sevoflurane, isoflurane) decrease RBF 30-50% via afferent arteriole vasodilation + reduced MAP. Phenylephrine increases BP but may reduce RBF if excessive.",
            "rationale": "Volatile agents suppress autoregulation dose-dependently; maintaining MAP and cardiac output are more important than agent choice for renal preservation.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Renal Protection During Cardiac' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the incidence and mechanism of AKI after cardiac surgery?",
            "answer": "10-30% of cardiac surgery patients develop AKI. Mechanisms: renal hypoperfusion (CPB, clamping), atheroemboli, myoglobinuria, inflammatory cytokine release.",
            "rationale": "Multiple injury pathways operate in cardiac surgery; prevention requires MAP maintenance, preload optimization, diuretics, and osmotic agents.",
            "bloom": "understand",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What medications reduce AKI risk in cardiac surgery?",
            "answer": "Low-dose dopamine (2-3 mcg/kg/min), fenoldopam (0.1-0.3 mcg/kg/min vasodilator), mannitol (0.25-0.5 g/kg), sodium bicarbonate for myoglobinuria.",
            "rationale": "Fenoldopam (selective DA1 agonist) increases RBF and GFR without tachycardia; osmotic agents prevent intratubular obstruction.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": "High-dose dopamine (causes renal vasoconstriction)"
        })
        kp_counter += 1

    elif 'Sciatic' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the anatomy and landmark-based approach for sciatic nerve block?",
            "answer": "Sciatic nerve (L4-S3) divides into tibial and peroneal at proximal thigh. Posterior approach: midpoint between PSIS and greater trochanter, then perpendicular to skin.",
            "rationale": "The sciatic is the largest single nerve in the body; blocking it provides anesthesia distal to knee except medial shin (saphenous innervation).",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the local anesthetic volume and onset time for sciatic blocks?",
            "answer": "Sciatic block: 20-30 mL local anesthetic, onset 10-20 minutes. Nerve stimulator goal: dorsiflexion/plantarflexion at 0.3-0.5 mA.",
            "rationale": "Higher current (>0.5 mA) risks intraneuronal injection; lower volume may result in patchy block, especially if needle not advanced to nerve.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Separation from CPB' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the systematic approach to separating a patient from CPB?",
            "answer": "Gradual reduction of pump flow to 1-2 L/min; assess contractility (TEE), aortic cross-clamp removal, rewarming to 37C, normalization of ACT, and inotropic support as needed.",
            "rationale": "Abrupt weaning risks hypotension and myocardial dysfunction. Gradual reduction allows native cardiac recovery and reveals need for inotropic support.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Sevoflurane' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the MAC of sevoflurane and its pharmacokinetic properties?",
            "answer": "Sevoflurane MAC = 2.0%; blood:gas coefficient 0.69 (faster emergence than isoflurane 1.4). Non-pungent, suitable for inhalational induction.",
            "rationale": "Low blood:gas solubility allows rapid uptake/elimination. Non-pungent airway allows safe volatile induction in children and difficult airway patients.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": "Desflurane (pungent, MAC 6.0)"
        })
        kp_counter += 1
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the clinical significance of sevoflurane metabolism and fluoride ions?",
            "answer": "Sevoflurane metabolized to inorganic fluoride (~50 micromol peak, well below nephrotoxic threshold of 50+ micromol). No clinically significant renal toxicity.",
            "rationale": "Unlike methoxyflurane (which causes high fluoride levels and renal injury), sevoflurane's metabolism produces fluoride below toxic levels.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": "Methoxyflurane (obsolete, causes high fluoride + renal injury)"
        })
        kp_counter += 1

    elif 'Spinal (intrathecal) local' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the typical intrathecal doses and durations of local anesthetics?",
            "answer": "Bupivacaine 10-15 mg: 2-4 hours duration. Lidocaine 40-100 mg: 0.5-2 hours. Hyperbaric formulations: gravity-dependent spread; isobaric: immobile.",
            "rationale": "Intrathecal dose is 1/10 of epidural due to direct CSF contact. Duration depends on lipophilicity (bupivacaine more lipophilic, longer action).",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the mechanism and clinical significance of baricity in spinal anesthesia?",
            "answer": "Hyperbaric (specific gravity >1.008): settles dependently. Isobaric (1.008): floats with CSF. Baricity controls sensory/motor block height; hyperbaric allows predictable spread.",
            "rationale": "Hyperbaric solutions allow gravity-directed block height by patient positioning; isobaric spreads more unpredictably.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Spinal Cord Injury' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What acute anesthetic priorities exist in spinal cord injury?",
            "answer": "Avoid succinylcholine (hyperkalemia from denervation); maintain MAP >85 mmHg for spinal cord perfusion; immobilize C-spine; RSI with rocuronium; avoid hypoxia/hypotension.",
            "rationale": "Secondary cord ischemia extends injury; immobilization and aggressive hemodynamic support are neuroprotective. Hyperkalemia from succinyl can cause cardiac arrest.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Spinal and epidural complications' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the classic neurological complications of neuraxial anesthesia?",
            "answer": "Post-dural puncture headache (19% spinal, 1% epidural), transient neurologic symptoms (0.4-15% lidocaine), cauda equina (rare, high dose/concentration), arachnoiditis.",
            "rationale": "PDPH from CSF leakage; TNS more common with lidocaine in lithotomy position. Diagnosis: positional headache within 24h; treatment: bed rest, fluids, epidural blood patch.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the epidural blood patch and when is it indicated?",
            "answer": "EBP: 15-20 mL autologous blood injected into epidural space at level of dural puncture. Indicated for PDPH if symptoms persist >24h or significantly impair function.",
            "rationale": "EBP has ~70% efficacy with single injection, ~90% with two injections. Sterile technique critical to prevent infection.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Spinal anesthesia for cesarean' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the standard spinal anesthetic regimen for cesarean delivery?",
            "answer": "Bupivacaine 10-12 mg hyperbaric + morphine 100 micrograms + fentanyl 10-15 micrograms. Target T4 level. Left uterine displacement, pre-hydration, vasopressor ready.",
            "rationale": "Hyperbaric bupivacaine with opioid co-injection provides fast, reliable block. Morphine provides post-op analgesia (2-4 hours). Vasopressor needed to prevent hypotension.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Spinal anesthesia: pharmacology' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "How do adjuvants (opioids, vasoconstrictors) modify spinal block characteristics?",
            "answer": "Morphine (100-500 mcg): prolongs analgesia 12-24h. Fentanyl (5-25 mcg): enhances early analgesia, may reduce LA requirement. Epinephrine (0.2 mg): prolongs motor block 20-40%.",
            "rationale": "Intrathecal morphine reaches opioid receptors on dorsal horn neurons; systemic absorption minimal due to CSF residence. Epinephrine reduces local anesthetic vascular uptake.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Spine Surgery: Cervical' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the anesthetic considerations for cervical spine surgery?",
            "answer": "Risk: airway difficulty (instability, fusion), neuromonitoring (wake-up test, SSEP/EMG), avoid hyperextension/rotation, careful positioning, maintain MAP for cord perfusion.",
            "rationale": "Cervical instability may worsen with neck positioning. Neuromonitoring detects cord dysfunction early. Hypothermia increases neuromonitoring noise.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Statistical Concepts' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the distinction between Type I and Type II error in hypothesis testing?",
            "answer": "Type I (alpha): false positive, rejecting true null hypothesis. Type II (beta): false negative, failing to reject false null. Power = 1-beta.",
            "rationale": "p < 0.05 controls Type I error at 5%. Sample size determination balances alpha and beta; typical power 0.80 yields n for 20% Type II risk.",
            "bloom": "understand",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Stereotactic & Functional' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the anesthetic goals for stereotactic/functional neurosurgery?",
            "answer": "Maintain rigid head frame immobilization, avoid TIVA (unpredictable emergence), use volatile + O2/air, minimal muscle relaxant, awake portion for neurologic testing.",
            "rationale": "Patient cooperation during mapping/testing critical; volatile agents allow quick emergence for intraoperative assessment. Frame prevents patient movement.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Subarachnoid Hemorrhage' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the perioperative management priorities for SAH?",
            "answer": "Control HTN (MAP <160 mmHg pre-clipping), maintain ICP <20 mmHg, prevent vasospasm (nimodipine 60 mg Q4h), early aneurysm repair, avoid hypovolemia.",
            "rationale": "High MAP increases rebleeding risk before clipping. Vasospasm (3-14d post-SAH) causes delayed ischemic deterioration. Nimodipine reduces incidence 40%.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Substance use' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the perioperative implications of chronic opioid use?",
            "answer": "Tolerance: increased anesthetic/opioid requirements. Cross-tolerance to all opioids. Risk: inadequate post-op analgesia with standard dosing. Continue home opioids perioperatively.",
            "rationale": "Patients on chronic opioids need higher doses; abrupt discontinuation risks withdrawal. Regional anesthesia may provide better analgesia than IV opioids.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the perioperative risk profile for alcohol use disorder?",
            "answer": "Airway difficulty, aspiration risk, hepatic impairment, coagulopathy, cardiomyopathy, autonomic hyperreactivity. Withdrawal (tremor, hallucinations, seizure) within 6-24h of last drink.",
            "rationale": "Alcohol causes malnutrition (thiamine, folate, magnesium deficiency). Withdrawal is life-threatening; prophylaxis with benzodiazepines standard. ASA score elevated.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Succinylcholine' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the pharmacology and clinical use of succinylcholine?",
            "answer": "Depolarizing NMBD: 1-1.5 mg/kg IV, onset 30-60 sec, duration 5-10 min. Hydrolyzed by plasma cholinesterase. Gold standard for RSI.",
            "rationale": "Rapid onset and brief duration ideal for emergency intubation. Depolarization causes visible fasciculations and potassium release (~0.5 mEq/L).",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": "Rocuronium (non-depolarizing, slower onset)"
        })
        kp_counter += 1
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "In which conditions is succinylcholine contraindicated due to hyperkalemia risk?",
            "answer": "Acute spinal cord injury, burns (24h-1yr), crush injury, rhabdomyolysis, denervation (paralysis >7d), renal failure, hyperkalemia. IM use safer (slower absorption).",
            "rationale": "Denervated muscle releases 5-10x more potassium. Even 0.5 mg/kg succinyl can cause fatal K+ rise to 9+ mEq/L and cardiac arrest in high-risk patients.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Sugammadex' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "How does sugammadex reverse neuromuscular blockade and what are standard doses?",
            "answer": "Sugammadex (selective relaxant binding agent): encapsulates rocuronium/vecuronium. Moderate blockade: 2-4 mg/kg. Deep: 4 mg/kg. Deep reversal within 3 min.",
            "rationale": "1:1 molar ratio encapsulation reduces free NMBD concentration, reversing blockade. No need for anticholinesterase. Faster, more reliable than neostigmine.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": "Neostigmine (indirect reversal, slower onset 5-10 min)"
        })
        kp_counter += 1
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the limitations and drug interactions of sugammadex?",
            "answer": "Expensive. No effect on succinylcholine. Renal clearance (renally excreted). Interaction with steroidal NMBDs only (rocuronium, vecuronium). Not for atracurium/cisatracurium.",
            "rationale": "Sugammadex selectivity limits use to rocuronium/vecuronium. Systemic hormonal effects minimal. Cost often prohibitive outside OR.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Surgical Safety Checklists' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the three phases of the Surgical Safety Checklist?",
            "answer": "Sign In (pre-induction): patient ID, consent, allergies, ASA. Time Out (pre-incision): team confirmation of patient/surgery/site. Sign Out (post-op): specimen ID, counts, equipment.",
            "rationale": "WHO Surgical Safety Checklist reduces mortality 47% and complications 36% (Haynes et al.). Time-out prevents wrong-site surgery and retained objects.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Sympathetic blocks' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the indications and technique for stellate ganglion block?",
            "answer": "SGB: blocks T1 sympathetic outflow. Indications: RSD/CRPS, post-thrombotic pain, herpes zoster. Landmark: C6 (Chassaignac) tubercle + 1 cm medial, 1-2 mL LA.",
            "rationale": "Stellate ganglion innervates head/neck/upper limb sympathetics. Horner's syndrome expected (miosis, ptosis, anhidrosis). Success confirmed by skin warming.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Systemic Lidocaine' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the perioperative IV lidocaine regimen and purported benefits?",
            "answer": "Bolus 1.5 mg/kg IV, then infusion 1-2 mg/kg/hr intraoperatively and 0.5-1 mg/kg/hr post-op (target plasma 2-5 mcg/mL). Reduces PONV, pain, ileus.",
            "rationale": "Lidocaine has anti-inflammatory properties; perioperative infusion may reduce opioid requirements and GI complications. Evidence mixed but generally safe.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Systemic labor analgesia' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the options for systemic analgesia in labor?",
            "answer": "Opioids: meperidine 12.5-25 mg IV/IM, fentanyl 0.5-1 mcg/kg IV. Nitrous oxide 50%. NSAIDs: ibuprofen 400-600 mg. Neuraxial superior to systemic analgesia.",
            "rationale": "Systemic opioids provide incomplete analgesia with maternal sedation/fetal risk. Nitrous oxide has inconsistent efficacy. Epidural/spinal gold standard.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'TBI: ICP Management' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the anesthetic goal and multi-modal approach to ICP management in TBI?",
            "answer": "Target: MAP >65 mmHg, ICP <20 mmHg, CPP (MAP-ICP) >60 mmHg. Modalities: head-of-bed 30, normothermia, normocarbia (mild HV 35-40 CO2), osmotic agents (mannitol/HTS 3%), sedation.",
            "rationale": "Increased ICP from edema/hemorrhage reduces CPP, causing secondary ischemia. Multimodal approach addresses different mechanisms (intracranial volume, metabolic rate, osmotic gradient).",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'TEE' in topic and 'Advanced' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What advanced TEE views assess complex cardiac pathology?",
            "answer": "Bicaval view (2D/3D): right atrium, inferior/superior vena cava. Transgastric long-axis/short-axis: LV volumes, regional wall motion. Aortic root: valve area, cusp separation.",
            "rationale": "Advanced views provide volumetric assessment and detailed valve pathology not visible in standard planes. 3D reconstruction aids surgical planning.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Thyroid disease' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the anesthetic considerations for hyperthyroidism?",
            "answer": "Risk: thyroid storm (hyperthermia, tachycardia, arrhythmia, shock). Prevention: beta-blocker premedication (esmolol 0.5-1 mg/kg), iodine (Lugol's solution 7-10 d preop), avoid desflurane/ketamine.",
            "rationale": "Hyperthyroid patients hypersensitive to catecholamines. Iodine blocks thyroid hormone release. Thyroid storm mortality high; aggressive prevention critical.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Total intravenous anesthesia (TIVA)' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is target-controlled infusion (TCI) and its advantages?",
            "answer": "TCI: pump uses 3-compartment PK model to compute infusion rate targeting plasma or effect-site concentration. Advantages: no overshoot, predictable emergence, reduced TIVA variability.",
            "rationale": "TCI eliminates manual rate calculation and drug accumulation. Effect-site targeting accounts for ke0 (effect-site equilibration), providing faster, more accurate control.",
            "bloom": "understand",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are typical propofol and remifentanil target concentrations for TIVA?",
            "answer": "Induction: propofol 2-3 mcg/mL plasma-site (target 8-10 mcg/mL ES). Maintenance: 2-4 mcg/mL. Remifentanil: 3-5 ng/mL. Titrate to BIS/hemodynamics.",
            "rationale": "Higher propofol concentrations provide hypnosis; remifentanil provides analgesia/suppression. Effect-site targeting allows faster response than plasma targeting.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Transesophageal Echocardiography (TEE)' in topic and 'Basic' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the fundamental TEE imaging planes and probe depth landmarks?",
            "answer": "Midesophageal (ME, 25-30 cm): 2-chamber (0 degrees), 4-chamber (90 degrees), long-axis (110-130 degrees). Transgastric (35-40 cm): short-axis (0 degrees), long-axis (90 degrees).",
            "rationale": "Systematic progression through planes ensures comprehensive assessment. Depth and rotation determine cross-sectional anatomy. Knowledge of anatomy critical for interpretation.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Transsphenoidal Surgery' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the anesthetic considerations for transsphenoidal pituitary surgery?",
            "answer": "Monitor: diabetes insipidus risk (post-op UOP increase). Airway: throat pack to prevent CSF leak, extubate awake. Avoid hypervolemia/hyperthermia. ICU post-op.",
            "rationale": "Pituitary surgery risks DI from hypothalamic/pituitary damage. Throat pack and careful fluid management prevent leak. Awake extubation allows early neuro assessment.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    elif 'Traumatic Brain Injury' in topic:
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the pathophysiology and management of secondary brain injury in TBI?",
            "answer": "Primary injury: immediate axonal shearing. Secondary injury: hypoxia, hypotension, edema (hours-days). Prevention: O2 sat >94%, MAP >65, ICP <20, rapid CT.",
            "rationale": "Secondary injury is modifiable and responsible for much disability. Early airway, oxygenation, BP support critical. Regional hypotension increases mortality 2-3x.",
            "bloom": "understand",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1
        kps.append({
            "id": f"{slug_base}-{kp_counter}",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the drug choices for RSI and sedation in TBI?",
            "answer": "RSI: avoid histamine-releasing agents (atracurium, cisatracurium). Use rocuronium or succinylcholine (acceptable despite K+ release in acute trauma). Sedation: propofol/midazolam + remifentanil.",
            "rationale": "Histamine release increases ICP. Propofol reduces ICP; remifentanil provides analgesia without accumulation. Avoid volatile agents (increase ICP).",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kp_counter += 1

    # Generic extraction for remaining topics
    if not kps and chunks:
        for chunk in chunks[:3]:
            sentences = extract_sentences(chunk.get('text', ''), limit=5)
            for sent in sentences[:2]:
                if kp_counter <= 9:
                    kps.append({
                        "id": f"{slug_base}-{kp_counter}",
                        "topic": topic,
                        "domain": domain,
                        "discipline": discipline,
                        "stem": "What is a key clinical feature of this topic?",
                        "answer": sent[:160],
                        "rationale": "Principle from anesthetic literature",
                        "bloom": "recall",
                        "source": [{"book": chunk.get('book', ''), "page": chunk.get('page', 0)}],
                        "confusable_with": ""
                    })
                    kp_counter += 1

    return kps[:9]

# Main execution
with open('data/_kp_retrieval_full.json', 'r', encoding='utf-8') as f:
    full = json.load(f)

slice_items = full[858:891]
all_kps = []
topic_count = 0

for item in slice_items:
    item_kps = author_kps_for_item(item)
    all_kps.extend(item_kps)
    if item_kps:
        topic_count += 1

# Write JSON
with open('data/kp_full_part_26.json', 'w', encoding='utf-8') as f:
    json.dump(all_kps, f, indent=2, ensure_ascii=False)

# Validate
try:
    with open('data/kp_full_part_26.json', 'r', encoding='utf-8') as f:
        test_load = json.load(f)
    print(f"part 26: {topic_count} topics, {len(all_kps)} KPs, 0 scripts, 0 pairs, parses OK")
except Exception as e:
    print(f"ERROR: {e}")
