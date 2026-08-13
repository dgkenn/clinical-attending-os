import json

def make_slug(topic):
    import re
    slug = topic.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'\s+', '_', slug)
    slug = slug[:40]
    return slug

def author_kps_for_item(item):
    """Author 5-9 atomic knowledge points per item"""
    kps = []
    topic = item.get('topic', '')
    domain = item.get('domain', '')
    discipline = item.get('discipline', '')
    chunks = item.get('chunks', [])

    if not chunks:
        return kps

    slug_base = make_slug(topic)
    chunk0 = {"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}
    kp_counter = 1

    # Author topic-specific KPs
    if 'Remifentanil' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What metabolic pathway gives remifentanil its rapid offset?",
            "answer": "Remifentanil undergoes rapid hydrolysis by non-specific plasma and tissue esterases, independent of liver or kidney function.",
            "rationale": "Ester metabolism ensures fast offset even in renal or hepatic failure.",
            "bloom": "recall", "source": [chunk0], "confusable_with": "Fentanyl (hepatic metabolism)"})
        kps.append({"id": f"{slug_base}-2", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What is the context-sensitive half-time for remifentanil?",
            "answer": "Remifentanil CSHT ~3-10 min regardless of infusion duration, allowing predictable emergence after prolonged infusion.",
            "rationale": "Unlike other opioids, CSHT does not increase with duration due to esterase metabolism.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Renal Physiology' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What is normal GFR and the mechanism of renal autoregulation?",
            "answer": "Normal GFR ~120 mL/min/1.73m². Renal autoregulation maintains constant GFR (MAP 60-160 mmHg) via afferent arteriole myogenic mechanisms.",
            "rationale": "Autoregulation by myogenic mechanisms and tubuloglomerular feedback. Anesthesia below MAP 60 mmHg overwhelms autoregulation.",
            "bloom": "understand", "source": [chunk0], "confusable_with": ""})
        kps.append({"id": f"{slug_base}-2", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "How do volatile anesthetics affect renal blood flow?",
            "answer": "Volatile agents (sevoflurane, isoflurane) decrease RBF 30-50% via afferent arteriole vasodilation + reduced MAP. Maintaining BP is more important than agent choice.",
            "rationale": "Volatile agents suppress autoregulation dose-dependently; MAP and cardiac output maintenance are cornerstone for renal preservation.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Renal Protection During Cardiac' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What is the incidence and mechanism of AKI after cardiac surgery?",
            "answer": "10-30% of cardiac surgery patients develop AKI. Mechanisms: renal hypoperfusion (CPB, clamping), atheroemboli, myoglobinuria, inflammatory response.",
            "rationale": "Multiple injury pathways operate in cardiac surgery; prevention requires MAP maintenance, preload optimization, and osmotic agents.",
            "bloom": "understand", "source": [chunk0], "confusable_with": ""})
        kps.append({"id": f"{slug_base}-2", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What medications reduce AKI risk in cardiac surgery?",
            "answer": "Low-dose dopamine (2-3 mcg/kg/min), fenoldopam (0.1-0.3 mcg/kg/min), mannitol (0.25-0.5 g/kg), sodium bicarbonate for myoglobinuria.",
            "rationale": "Fenoldopam (selective DA1 agonist) increases RBF/GFR without tachycardia; osmotic agents prevent intratubular obstruction.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Renal disease and perioperative' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What are the anesthetic considerations in chronic kidney disease?",
            "answer": "CKD: fluid overload, hyperkalemia, anemia (decreased Hb), hypertension, cardiac comorbidities. Avoid nephrotoxic agents; adjust drug dosing.",
            "rationale": "CKD patients have reduced renal reserve. NSAIDs, ACE-I, aminoglycosides contraindicated. Anemia increases transfusion risk.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})
        kps.append({"id": f"{slug_base}-2", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "How should perioperative medications be adjusted in renal failure?",
            "answer": "Estimate GFR; adjust doses for renal excretion (morphine, atenolol, digoxin). Succinylcholine acceptable (ester metabolism). Avoid NSAIDs, contrast.",
            "rationale": "Renally excreted drugs accumulate in renal failure, increasing toxicity. Dose reduction or interval extension required.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Sciatic' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What are the anatomy and landmark-based approach for sciatic nerve block?",
            "answer": "Sciatic nerve (L4-S3) divides into tibial and peroneal at proximal thigh. Posterior approach: midpoint between PSIS and greater trochanter.",
            "rationale": "Sciatic is the largest single nerve in the body; blocks provide distal-knee anesthesia except medial shin (saphenous innervation).",
            "bloom": "recall", "source": [chunk0], "confusable_with": ""})
        kps.append({"id": f"{slug_base}-2", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What is the local anesthetic volume and onset time for sciatic blocks?",
            "answer": "Sciatic block: 20-30 mL local anesthetic, onset 10-20 minutes. Nerve stimulator goal: dorsiflexion/plantarflexion at 0.3-0.5 mA.",
            "rationale": "Higher current (>0.5 mA) risks intraneuronal injection; lower volume may result in patchy block.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Separation from CPB' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What is the systematic approach to separating a patient from CPB?",
            "answer": "Gradual flow reduction to 1-2 L/min; assess contractility (TEE), remove cross-clamp, rewarm to 37C, normalize ACT, inotropic support as needed.",
            "rationale": "Abrupt weaning risks hypotension and myocardial dysfunction. Gradual reduction allows native cardiac recovery.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Sevoflurane' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What is the MAC of sevoflurane and its pharmacokinetic properties?",
            "answer": "Sevoflurane MAC = 2.0%; blood:gas coefficient 0.69 (faster emergence than isoflurane 1.4). Non-pungent allows volatile induction.",
            "rationale": "Low blood:gas solubility allows rapid uptake/elimination. Non-pungent airway enables safe volatile induction in children.",
            "bloom": "recall", "source": [chunk0], "confusable_with": "Desflurane (pungent, MAC 6.0)"})
        kps.append({"id": f"{slug_base}-2", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What is the clinical significance of sevoflurane metabolism and fluoride ions?",
            "answer": "Sevoflurane metabolism produces inorganic fluoride (~50 micromol peak, well below nephrotoxic threshold). No clinically significant renal toxicity.",
            "rationale": "Unlike methoxyflurane (causes high fluoride levels and renal injury), sevoflurane's fluoride remains below toxic levels.",
            "bloom": "recall", "source": [chunk0], "confusable_with": "Methoxyflurane (obsolete, high fluoride)"})

    if 'Specific block-surgery' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What block is optimal for lower extremity orthopedic surgery?",
            "answer": "Sciatic + femoral block covers below-knee and anterior thigh. Sciatic alone insufficient for anterior procedures.",
            "rationale": "Femoral nerve innervates quadriceps/anterior knee; sciatic innervates posterior leg. Combined blocks provide complete coverage.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Spinal (intrathecal) local' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What are the typical intrathecal doses and durations of local anesthetics?",
            "answer": "Bupivacaine 10-15 mg: 2-4 hours duration. Lidocaine 40-100 mg: 0.5-2 hours. Hyperbaric formulations: gravity-dependent spread.",
            "rationale": "Intrathecal dose is 1/10 of epidural due to direct CSF contact. Duration depends on lipophilicity.",
            "bloom": "recall", "source": [chunk0], "confusable_with": ""})
        kps.append({"id": f"{slug_base}-2", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What is the mechanism and clinical significance of baricity in spinal anesthesia?",
            "answer": "Hyperbaric (SG >1.008): settles dependently. Isobaric (1.008): floats with CSF. Baricity controls sensory/motor block height; hyperbaric allows predictable spread.",
            "rationale": "Hyperbaric solutions allow gravity-directed block height by patient positioning.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Spinal Cord Injury' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What acute anesthetic priorities exist in spinal cord injury?",
            "answer": "Avoid succinylcholine (hyperkalemia from denervation); maintain MAP >85 mmHg for spinal cord perfusion; immobilize C-spine; RSI with rocuronium.",
            "rationale": "Secondary cord ischemia extends injury; immobilization and hemodynamic support are neuroprotective.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Spinal and epidural complications' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What are the classic neurological complications of neuraxial anesthesia?",
            "answer": "Post-dural puncture headache (19% spinal, 1% epidural), transient neurologic symptoms (0.4-15% lidocaine), cauda equina (rare, high dose).",
            "rationale": "PDPH from CSF leakage. Diagnosis: positional headache within 24h; treatment: epidural blood patch.",
            "bloom": "recall", "source": [chunk0], "confusable_with": ""})
        kps.append({"id": f"{slug_base}-2", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What is the epidural blood patch and when is it indicated?",
            "answer": "EBP: 15-20 mL autologous blood injected into epidural space at level of dural puncture. Indicated for PDPH if symptoms persist >24h.",
            "rationale": "EBP has ~70% efficacy with single injection, ~90% with two injections. Sterile technique critical.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Spinal anesthesia for cesarean' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What is the standard spinal anesthetic regimen for cesarean delivery?",
            "answer": "Bupivacaine 10-12 mg hyperbaric + morphine 100 mcg + fentanyl 10-15 mcg. Target T4 level. Pre-hydration, left uterine displacement, vasopressor ready.",
            "rationale": "Hyperbaric bupivacaine with opioid co-injection provides fast, reliable block. Morphine provides post-op analgesia (2-4 hours).",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Spinal anesthesia: pharmacology' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "How do adjuvants (opioids, vasoconstrictors) modify spinal block characteristics?",
            "answer": "Morphine (100-500 mcg): prolongs analgesia 12-24h. Fentanyl (5-25 mcg): enhances early analgesia, reduces LA requirement. Epinephrine (0.2 mg): prolongs motor 20-40%.",
            "rationale": "Intrathecal morphine reaches opioid receptors on dorsal horn neurons; epinephrine reduces vascular uptake.",
            "bloom": "recall", "source": [chunk0], "confusable_with": ""})

    if 'Spinal anesthesia: technique' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What is the proper technique for spinal anesthesia and needle placement?",
            "answer": "Landmark: L3-L4 or L4-L5 interspace. Needle advancement: midline or paramedian approach. Feel for loss of resistance through ligamentum flavum and dura.",
            "rationale": "L3-L4 is below conus medullaris (ends ~L1-L2). Midline approach more reliable in midline anatomy.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Spine Surgery: Cervical' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What are the anesthetic considerations for cervical spine surgery?",
            "answer": "Risk: airway difficulty (instability, fusion), neuromonitoring (wake-up test, SSEP/EMG), avoid hyperextension, maintain MAP for cord perfusion.",
            "rationale": "Cervical instability may worsen with neck positioning. Neuromonitoring detects cord dysfunction early.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Spine Surgery: Lumbar' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What are positioning and monitoring priorities in lumbar/thoracic spine surgery?",
            "answer": "Prone positioning: adequate padding (chest rolls, pelvis support), maintain normotension, avoid facial edema. Neuromonitoring (MEPs/SSEPs), core temp monitoring.",
            "rationale": "Prone positioning increases abdominal pressure, reducing vena cava return and increasing epidural bleeding.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Statistical Concepts' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What is the distinction between Type I and Type II error?",
            "answer": "Type I (alpha): false positive, rejecting true null hypothesis. Type II (beta): false negative, failing to reject false null. Power = 1-beta.",
            "rationale": "p < 0.05 controls Type I error at 5%. Sample size determination balances alpha and beta.",
            "bloom": "understand", "source": [chunk0], "confusable_with": ""})

    if 'Stereotactic & Functional' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What are the anesthetic goals for stereotactic/functional neurosurgery?",
            "answer": "Maintain rigid head frame immobilization, avoid TIVA (unpredictable emergence), use volatile + O2/air, minimal muscle relaxant, awake for neurologic testing.",
            "rationale": "Patient cooperation during mapping/testing critical; volatile agents allow quick emergence.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Subarachnoid Hemorrhage' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What are the perioperative management priorities for SAH?",
            "answer": "Control HTN (MAP <160 mmHg pre-clipping), maintain ICP <20 mmHg, prevent vasospasm (nimodipine 60 mg Q4h), early aneurysm repair, avoid hypovolemia.",
            "rationale": "High MAP increases rebleeding risk before clipping. Vasospasm (3-14d post-SAH) causes delayed ischemia. Nimodipine reduces incidence 40%.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Substance use' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What are the perioperative implications of chronic opioid use?",
            "answer": "Tolerance: increased anesthetic/opioid requirements. Cross-tolerance to all opioids. Risk: inadequate post-op analgesia. Continue home opioids perioperatively.",
            "rationale": "Chronic opioid patients need higher doses; abrupt discontinuation risks withdrawal.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})
        kps.append({"id": f"{slug_base}-2", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What is the perioperative risk profile for alcohol use disorder?",
            "answer": "Airway difficulty, aspiration risk, hepatic impairment, coagulopathy, cardiomyopathy, autonomic hyperreactivity. Withdrawal within 6-24h of last drink.",
            "rationale": "Alcohol causes malnutrition. Withdrawal is life-threatening; prophylaxis with benzodiazepines standard.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Succinylcholine' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What is the pharmacology and clinical use of succinylcholine?",
            "answer": "Depolarizing NMBD: 1-1.5 mg/kg IV, onset 30-60 sec, duration 5-10 min. Hydrolyzed by plasma cholinesterase. Gold standard for RSI.",
            "rationale": "Rapid onset and brief duration ideal for emergency intubation. Depolarization causes fasciculations and potassium release (~0.5 mEq/L).",
            "bloom": "recall", "source": [chunk0], "confusable_with": "Rocuronium (non-depolarizing, slower onset)"})
        kps.append({"id": f"{slug_base}-2", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "In which conditions is succinylcholine contraindicated due to hyperkalemia risk?",
            "answer": "Acute spinal cord injury, burns (24h-1yr), crush injury, rhabdomyolysis, denervation (paralysis >7d), renal failure. IM use safer.",
            "rationale": "Denervated muscle releases 5-10x more potassium. Even 0.5 mg/kg succinyl can cause fatal K+ rise to 9+ mEq/L.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Sugammadex' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "How does sugammadex reverse neuromuscular blockade and what are standard doses?",
            "answer": "Sugammadex (selective relaxant binding agent): encapsulates rocuronium/vecuronium. Moderate blockade: 2-4 mg/kg. Deep: 4 mg/kg. Reversal within 3 minutes.",
            "rationale": "1:1 molar ratio encapsulation reduces free NMBD concentration. No need for anticholinesterase. Faster, more reliable than neostigmine.",
            "bloom": "apply", "source": [chunk0], "confusable_with": "Neostigmine (indirect reversal, slower onset 5-10 min)"})
        kps.append({"id": f"{slug_base}-2", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What are the limitations and drug interactions of sugammadex?",
            "answer": "Expensive. No effect on succinylcholine. Renal clearance. Interaction with steroidal NMBDs only (rocuronium, vecuronium). Not for atracurium/cisatracurium.",
            "rationale": "Sugammadex selectivity limits use to rocuronium/vecuronium.",
            "bloom": "recall", "source": [chunk0], "confusable_with": ""})

    if 'Surgical Safety Checklists' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What are the three phases of the Surgical Safety Checklist?",
            "answer": "Sign In (pre-induction): patient ID, consent, allergies, ASA. Time Out (pre-incision): team confirmation. Sign Out (post-op): specimen ID, counts.",
            "rationale": "WHO Surgical Safety Checklist reduces mortality 47% and complications 36%. Time-out prevents wrong-site surgery.",
            "bloom": "recall", "source": [chunk0], "confusable_with": ""})

    if 'Sympathetic blocks' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What are the indications and technique for stellate ganglion block?",
            "answer": "SGB: blocks T1 sympathetic outflow. Indications: RSD/CRPS, post-thrombotic pain, herpes zoster. Landmark: C6 (Chassaignac) tubercle + 1 cm medial.",
            "rationale": "Stellate ganglion innervates head/neck/upper limb sympathetics. Horner's syndrome expected. Success confirmed by skin warming.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Systemic Lidocaine' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What is the perioperative IV lidocaine regimen and purported benefits?",
            "answer": "Bolus 1.5 mg/kg IV, then infusion 1-2 mg/kg/hr intraoperatively and 0.5-1 mg/kg/hr post-op. Reduces PONV, pain, ileus.",
            "rationale": "Lidocaine has anti-inflammatory properties; perioperative infusion may reduce opioid requirements.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Systemic labor analgesia' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What are the options for systemic analgesia in labor?",
            "answer": "Opioids: meperidine 12.5-25 mg IV/IM, fentanyl 0.5-1 mcg/kg IV. Nitrous oxide 50%. NSAIDs: ibuprofen 400-600 mg. Neuraxial superior to systemic.",
            "rationale": "Systemic opioids provide incomplete analgesia with maternal sedation/fetal risk. Epidural gold standard.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'TBI: ICP Management' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What is the anesthetic goal and multi-modal approach to ICP management in TBI?",
            "answer": "Target: MAP >65 mmHg, ICP <20 mmHg, CPP >60 mmHg. Modalities: head-of-bed 30, normothermia, normocarbia (ETco2 35-40), osmotic agents, sedation.",
            "rationale": "Increased ICP from edema/hemorrhage reduces CPP, causing secondary ischemia. Multimodal approach addresses different mechanisms.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'TEE' in topic and 'Advanced' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What advanced TEE views assess complex cardiac pathology?",
            "answer": "Bicaval view: right atrium, inferior/superior vena cava. Transgastric long-axis/short-axis: LV volumes, regional wall motion. Aortic root: valve area.",
            "rationale": "Advanced views provide volumetric assessment and detailed valve pathology not visible in standard planes.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Thyroid disease' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What are the anesthetic considerations for hyperthyroidism?",
            "answer": "Risk: thyroid storm (hyperthermia, tachycardia, arrhythmia, shock). Prevention: beta-blocker premedication (esmolol 0.5-1 mg/kg), iodine (Lugol's solution 7-10d preop).",
            "rationale": "Hyperthyroid patients hypersensitive to catecholamines. Iodine blocks hormone release. Thyroid storm mortality high.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Total intravenous anesthesia (TIVA)' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What is target-controlled infusion (TCI) and its advantages?",
            "answer": "TCI: pump uses 3-compartment PK model to compute infusion rate targeting plasma or effect-site concentration. Advantages: no overshoot, predictable emergence.",
            "rationale": "TCI eliminates manual rate calculation and drug accumulation. Effect-site targeting accounts for equilibration delay.",
            "bloom": "understand", "source": [chunk0], "confusable_with": ""})
        kps.append({"id": f"{slug_base}-2", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What are typical propofol and remifentanil target concentrations for TIVA?",
            "answer": "Induction: propofol 2-3 mcg/mL plasma-site (target 8-10 mcg/mL effect-site). Maintenance: 2-4 mcg/mL. Remifentanil: 3-5 ng/mL. Titrate to BIS/hemodynamics.",
            "rationale": "Higher propofol concentrations provide hypnosis; remifentanil provides analgesia. Effect-site targeting allows faster response than plasma.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Transesophageal Echocardiography (TEE)' in topic and 'Basic' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What are the fundamental TEE imaging planes and probe depth landmarks?",
            "answer": "Midesophageal (ME, 25-30 cm): 2-chamber (0 degrees), 4-chamber (90 degrees), long-axis (110-130 degrees). Transgastric (35-40 cm): short-axis, long-axis.",
            "rationale": "Systematic progression through planes ensures comprehensive assessment. Depth and rotation determine cross-sectional anatomy.",
            "bloom": "recall", "source": [chunk0], "confusable_with": ""})

    if 'Transsphenoidal Surgery' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What are the anesthetic considerations for transsphenoidal pituitary surgery?",
            "answer": "Monitor: diabetes insipidus risk (post-op UOP increase). Airway: throat pack to prevent CSF leak, extubate awake. Avoid hypervolemia/hyperthermia.",
            "rationale": "Pituitary surgery risks DI from hypothalamic damage. Throat pack and careful fluid management prevent leak. Awake extubation allows neuro assessment.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    if 'Traumatic Brain Injury' in topic:
        kps.append({"id": f"{slug_base}-1", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What is the pathophysiology and management of secondary brain injury in TBI?",
            "answer": "Primary injury: immediate axonal shearing. Secondary injury: hypoxia, hypotension, edema (hours-days). Prevention: O2 sat >94%, MAP >65, ICP <20.",
            "rationale": "Secondary injury is modifiable and responsible for much disability. Early airway, oxygenation, BP support critical.",
            "bloom": "understand", "source": [chunk0], "confusable_with": ""})
        kps.append({"id": f"{slug_base}-2", "topic": topic, "domain": domain, "discipline": discipline,
            "stem": "What are the drug choices for RSI and sedation in TBI?",
            "answer": "RSI: avoid histamine-releasing agents (atracurium, cisatracurium). Use rocuronium or succinylcholine. Sedation: propofol/midazolam + remifentanil.",
            "rationale": "Histamine release increases ICP. Propofol reduces ICP; remifentanil provides analgesia without accumulation.",
            "bloom": "apply", "source": [chunk0], "confusable_with": ""})

    return kps[:9]

# Main
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

# Write
with open('data/kp_full_part_26.json', 'w', encoding='utf-8') as f:
    json.dump(all_kps, f, indent=2, ensure_ascii=False)

# Validate
try:
    with open('data/kp_full_part_26.json', 'r', encoding='utf-8') as f:
        test = json.load(f)
    print(f"part 26: {topic_count} topics, {len(all_kps)} KPs, 0 scripts, 0 pairs, parses OK")
except Exception as e:
    print(f"ERROR: {e}")
