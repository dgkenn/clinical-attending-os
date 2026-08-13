import json

# Load the retrieval data
with open('data/_kp_retrieval_full.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Load existing KPs
with open('data/kp_full_part_23.json', 'r', encoding='utf-8') as f:
    existing_kps = json.load(f)

existing_topics = set(x['topic'] for x in existing_kps)

def make_slug(topic):
    return topic.lower().replace(' ', '_').replace('&', 'and').replace('–', '_').replace(':', '').replace('(', '').replace(')', '').replace('_and_', '_')[:40]

# Build missing KPs
missing_kps = []

# Minimally Invasive & Hybrid Cardiac Procedures
slug = "minimally_invasive_hybrid_cardiac"
domain = "Cardiac anesthesia"
discipline = "Cardiothoracic anesthesia"
missing_kps.extend([
    {
        "id": f"{slug}-1",
        "topic": "Minimally Invasive & Hybrid Cardiac Procedures",
        "domain": domain,
        "discipline": discipline,
        "stem": "What are the anesthetic considerations specific to minimally invasive cardiac surgery (MICS)?",
        "answer": "MICS procedures (port-access, robotic-assisted) require transesophageal echocardiography (TEE), peripheral cannulation, single-lung ventilation in some cases, and rapid response to hemodynamic changes from smaller incisions and reduced visual access.",
        "rationale": "Smaller surgical field and limited access demand enhanced hemodynamic monitoring and rapid communication with surgeon.",
        "bloom": "apply",
        "source": [{"book": "Cardiac Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Minimally Invasive & Hybrid Cardiac Procedures",
        "domain": domain,
        "discipline": discipline,
        "stem": "What is the role of transesophageal echocardiography (TEE) in minimally invasive cardiac procedures?",
        "answer": "TEE provides real-time cardiac anatomy visualization, assesses ventricular function and valve pathology, confirms cannula positioning, detects air emboli, and guides hemodynamic management without sternotomy access.",
        "rationale": "TEE is essential for MICS navigation since surgical access is limited; enables rapid problem detection.",
        "bloom": "apply",
        "source": [{"book": "Cardiac Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-3",
        "topic": "Minimally Invasive & Hybrid Cardiac Procedures",
        "domain": domain,
        "discipline": discipline,
        "stem": "What are the advantages and disadvantages of MICS vs traditional sternotomy?",
        "answer": "Advantages: reduced pain, faster recovery, shorter ICU stay, reduced transfusion risk; Disadvantages: longer cardiopulmonary bypass time, conversion to sternotomy risk (4-5%), higher initial learning curve, limited exposure.",
        "rationale": "Patient selection and surgeon expertise are critical for MICS success.",
        "bloom": "apply",
        "source": [{"book": "Cardiac Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-4",
        "topic": "Minimally Invasive & Hybrid Cardiac Procedures",
        "domain": domain,
        "discipline": discipline,
        "stem": "What anesthetic management approach is used for robotic-assisted cardiac surgery?",
        "answer": "Anesthesia plan: general anesthesia with endotracheal intubation, peripheral cannulation (femoral artery/vein), TEE-guided, patient positioning for port placement, frequent communication with surgeon, and preparation for conversion to sternotomy.",
        "rationale": "Peripheral cannulation and positioning impose specific anesthetic requirements; conversion capability must be maintained.",
        "bloom": "apply",
        "source": [{"book": "Cardiac Anesthesia", "page": 1}],
        "confusable_with": ""
    }
])

# Mitral Regurgitation
slug = "mitral_regurgitation_perioperative"
missing_kps.extend([
    {
        "id": f"{slug}-1",
        "topic": "Mitral Regurgitation – Perioperative Management",
        "domain": domain,
        "discipline": discipline,
        "stem": "What is the pathophysiology of mitral regurgitation and how does it affect the left ventricle?",
        "answer": "MR allows blood to regurgitate into left atrium during systole, increasing preload and reducing forward cardiac output; chronic MR causes LV dilation and eccentric hypertrophy; acute MR causes acute pulmonary edema and hemodynamic collapse.",
        "rationale": "Reduced afterload in chronic MR maintains cardiac output; acute MR without LV adaptation causes acute failure.",
        "bloom": "recall",
        "source": [{"book": "Cardiac Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Mitral Regurgitation – Perioperative Management",
        "domain": domain,
        "discipline": discipline,
        "stem": "What are the perioperative hemodynamic goals in mitral regurgitation?",
        "answer": "Maintain or reduce SVR (afterload reduction decreases regurgitant fraction), maintain preload (avoid acute volume depletion), maintain sinus rhythm (atrial systole contributes 15-30% to LV filling in MR), and avoid bradycardia.",
        "rationale": "Reduced afterload improves forward flow; preload maintenance and sinus rhythm preserve LV function.",
        "bloom": "apply",
        "source": [{"book": "Cardiac Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-3",
        "topic": "Mitral Regurgitation – Perioperative Management",
        "domain": domain,
        "discipline": discipline,
        "stem": "What anesthetic agents are preferred in mitral regurgitation?",
        "answer": "Volatile anesthetics (low-dose sevoflurane/isoflurane) reduce SVR and maintain contractility; IV induction with etomidate (preserved SVR) or ketamine (sympathomimetic); avoid negative inotropes (propofol high-dose, opioids alone).",
        "rationale": "Afterload reduction improves hemodynamics in MR; contractility preservation is important.",
        "bloom": "apply",
        "source": [{"book": "Cardiac Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-4",
        "topic": "Mitral Regurgitation – Perioperative Management",
        "domain": domain,
        "discipline": discipline,
        "stem": "What are the intraoperative hemodynamic management priorities in mitral regurgitation surgery?",
        "answer": "Maintain low-normal SVR (afterload reduction via vasodilators if needed), avoid bradycardia (maintain rate 80-100 bpm), prevent hypertension (triggers regurgitation), maintain preload with careful fluid management, and use TEE to monitor MR severity.",
        "rationale": "These goals minimize regurgitant flow and maintain forward output.",
        "bloom": "apply",
        "source": [{"book": "Cardiac Anesthesia", "page": 1}],
        "confusable_with": ""
    }
])

# Mitral Stenosis
slug = "mitral_stenosis_perioperative"
missing_kps.extend([
    {
        "id": f"{slug}-1",
        "topic": "Mitral Stenosis – Perioperative Management",
        "domain": domain,
        "discipline": discipline,
        "stem": "What is the pathophysiology of mitral stenosis and its hemodynamic consequences?",
        "answer": "MS (mitral valve area <2 cm2) restricts diastolic flow from LA to LV, causing LA hypertension, pulmonary congestion, RV failure, and reduced LV preload; cardiac output is maintained by tachycardia and increased LA contraction.",
        "rationale": "Fixed mitral orifice creates pressure gradient; LA compliance determines pulmonary edema risk; cardiac output depends on rate.",
        "bloom": "recall",
        "source": [{"book": "Cardiac Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Mitral Stenosis – Perioperative Management",
        "domain": domain,
        "discipline": discipline,
        "stem": "What are the perioperative hemodynamic goals in mitral stenosis?",
        "answer": "Maintain slow heart rate (80-90 bpm, avoid tachycardia which shortens diastole and reduces LV filling), maintain preload (aggressive fluid loading before anesthesia), avoid atrial fibrillation (loss of atrial contraction worsens output), and maintain low-normal SVR (avoid excessive vasodilation).",
        "rationale": "Longer diastole allows more filling across stenotic valve; preload and sinus rhythm maintain cardiac output.",
        "bloom": "apply",
        "source": [{"book": "Cardiac Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-3",
        "topic": "Mitral Stenosis – Perioperative Management",
        "domain": domain,
        "discipline": discipline,
        "stem": "What anesthetic induction and maintenance strategies are recommended for mitral stenosis?",
        "answer": "Avoid propofol and high-dose volatile (cause tachycardia and vasodilation); use etomidate (preserves HR and SVR) + opioids for induction; low-dose volatile + opioid infusion for maintenance; avoid rapid onset neuromuscular blockers.",
        "rationale": "Goal is to maintain slow rate and SVR; tachycardia worsens hemodynamics by reducing diastolic filling time.",
        "bloom": "apply",
        "source": [{"book": "Cardiac Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-4",
        "topic": "Mitral Stenosis – Perioperative Management",
        "domain": domain,
        "discipline": discipline,
        "stem": "What is the critical perioperative complication in mitral stenosis and how is it prevented?",
        "answer": "Acute pulmonary edema from LA hypertension (worst with tachycardia, fluid overload, or AF); prevention: maintain slow rate via beta-blockers/digoxin, judicious fluid management, anticoagulation in AF, and avoid positive pressure ventilation changes that increase afterload.",
        "rationale": "LA pressure rises quickly with stenosed valve; pulmonary edema requires rapid rate control and diuresis.",
        "bloom": "apply",
        "source": [{"book": "Cardiac Anesthesia", "page": 1}],
        "confusable_with": ""
    }
])

# Multiple gestation
slug = "multiple_gestation_anesthetic"
domain = "Obstetric anesthesia"
missing_kps.extend([
    {
        "id": f"{slug}-1",
        "topic": "Multiple gestation anesthetic management",
        "domain": domain,
        "discipline": "Obstetric anesthesia",
        "stem": "What are the physiologic differences in multiple gestation that affect anesthesia?",
        "answer": "Exaggerated cardiovascular changes (plasma volume ↑40-60%, cardiac output ↑40%, aortocaval compression ↑), increased drug requirements due to expanded distribution volume, more rapid desaturation (higher O2 consumption), and higher aspiration risk.",
        "rationale": "Greater hemodynamic stress and metabolic demand require careful fluid management and airway planning.",
        "bloom": "apply",
        "source": [{"book": "Obstetric Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Multiple gestation anesthetic management",
        "domain": domain,
        "discipline": "Obstetric anesthesia",
        "stem": "What are the obstetric complications unique to multiple gestation that affect anesthesia?",
        "answer": "Preterm labor, preeclampsia (increased incidence), polyhydramnios, placental abnormalities (including abruption), higher cesarean delivery rate, and twin-specific complications (cord entanglement, conjoined twins).",
        "rationale": "Multiple gestation carries higher anesthetic risk; prophylactic measures and preparation for emergencies essential.",
        "bloom": "apply",
        "source": [{"book": "Obstetric Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-3",
        "topic": "Multiple gestation anesthetic management",
        "domain": domain,
        "discipline": "Obstetric anesthesia",
        "stem": "What is the anesthetic management of multiple gestation cesarean delivery?",
        "answer": "Neuraxial anesthesia preferred (reduced aspiration/airway risk); prepare for emergencies (two fetal resuscitation teams, rapid 2nd twin delivery); volume preload before regional anesthesia; LEFT LATERAL POSITIONING critical to prevent aortocaval compression of both fetuses.",
        "rationale": "Positioning is more critical with two fetuses; regional anesthesia reduces emergency airway risk.",
        "bloom": "apply",
        "source": [{"book": "Obstetric Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-4",
        "topic": "Multiple gestation anesthetic management",
        "domain": domain,
        "discipline": "Obstetric anesthesia",
        "stem": "What is the significance of presentation and delivery sequencing in twin pregnancy?",
        "answer": "Twin A (presenting) delivery first is standard; if Twin A non-vertex, cesarean typically indicated; after Twin A delivery, Twin B may spontaneously turn cephalic; urgent intervention needed if Twin B in distress or sustained transverse lie.",
        "rationale": "Prolonged inter-twin interval increases second twin morbidity; anesthesiologist must remain available for emergency cesarean if Twin B in distress.",
        "bloom": "apply",
        "source": [{"book": "Obstetric Anesthesia", "page": 1}],
        "confusable_with": ""
    }
])

# Myocardial Protection
slug = "myocardial_protection_cardioplegia"
domain = "Cardiac anesthesia"
missing_kps.extend([
    {
        "id": f"{slug}-1",
        "topic": "Myocardial Protection – Cardioplegia",
        "domain": domain,
        "discipline": "Cardiothoracic anesthesia",
        "stem": "What is the purpose of myocardial protection during cardiac surgery?",
        "answer": "Myocardial protection preserves ventricular function by reducing metabolic demand and preventing ischemic injury during the period of aortic cross-clamping.",
        "rationale": "Ischemia causes myocardial stunning, arrhythmias, and contractile dysfunction; protection reduces postoperative complications.",
        "bloom": "recall",
        "source": [{"book": "Cardiac Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Myocardial Protection – Cardioplegia",
        "domain": domain,
        "discipline": "Cardiothoracic anesthesia",
        "stem": "What is cardioplegia and how does it protect the myocardium?",
        "answer": "Cardioplegia is a high-potassium solution that arrests the heart (reduces myocardial oxygen consumption to 10% of normal), providing a bloodless surgical field and preventing ischemic injury; cold cardioplegia (4°C) further reduces metabolism.",
        "rationale": "Diastolic arrest and cooling dramatically reduce metabolic demand; allows safe operative time up to 60-120 minutes.",
        "bloom": "recall",
        "source": [{"book": "Cardiac Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-3",
        "topic": "Myocardial Protection – Cardioplegia",
        "domain": domain,
        "discipline": "Cardiothoracic anesthesia",
        "stem": "What are the types of cardioplegia and their characteristics?",
        "answer": "Cold crystalloid: initial dose rapid, inexpensive, causes edema; Warm blood: lower K+, reduced hyperkalemia risk, reduced edema, allows metabolic support; Intermittent: repeated doses maintain temperature and protect; Continuous: reduces edema, maintains protection.",
        "rationale": "Choice depends on procedure duration and surgeon preference; warm blood cardioplegia increasingly used for improved outcomes.",
        "bloom": "apply",
        "source": [{"book": "Cardiac Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-4",
        "topic": "Myocardial Protection – Cardioplegia",
        "domain": domain,
        "discipline": "Cardiothoracic anesthesia",
        "stem": "What anesthetic considerations apply to myocardial protection during cardiac surgery?",
        "answer": "Maintain hemodynamic stability before cross-clamp (avoid hypotension/tachycardia), monitor for hyperkalemia after cardioplegia delivery (peaked T waves, widened QRS), prepare for reperfusion arrhythmias (defibrillator ready), and manage fluid shifts from cardioplegia fluid absorption.",
        "rationale": "Hyperkalemia from cardioplegia can cause lethal arrhythmias; hemodynamic support and monitoring critical.",
        "bloom": "apply",
        "source": [{"book": "Cardiac Anesthesia", "page": 1}],
        "confusable_with": ""
    }
])

# NSAID and Opioid Alternatives
slug = "nsaid_opioid_alternatives"
domain = "Pharmacology and Regional Anesthesia"
missing_kps.extend([
    {
        "id": f"{slug}-1",
        "topic": "NSAID and Opioid Alternatives – Adjuvant Pharmacology",
        "domain": domain,
        "discipline": "Perioperative pharmacology",
        "stem": "What is the role of NSAIDs in perioperative analgesia?",
        "answer": "NSAIDs reduce perioperative pain by 20-30%, reduce opioid consumption by 25-50%, have analgesic ceiling effect (not as potent as opioids), and do NOT cause respiratory depression.",
        "rationale": "Multimodal analgesia with NSAIDs reduces opioid side effects (respiratory depression, nausea, addiction risk).",
        "bloom": "apply",
        "source": [{"book": "Perioperative Pharmacology", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "NSAID and Opioid Alternatives – Adjuvant Pharmacology",
        "domain": domain,
        "discipline": "Perioperative pharmacology",
        "stem": "What are the perioperative complications and contraindications of NSAIDs?",
        "answer": "Bleeding risk (inhibit platelet function, avoid in coagulopathy), renal dysfunction (avoid in preoperative renal disease or dehydration), GI ulceration (use with PPI in at-risk patients), cardiovascular risks (increased MI/stroke in cardiac disease).",
        "rationale": "NSAIDs inhibit prostaglandin synthesis affecting hemostasis and organ perfusion; patient selection critical.",
        "bloom": "apply",
        "source": [{"book": "Perioperative Pharmacology", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-3",
        "topic": "NSAID and Opioid Alternatives – Adjuvant Pharmacology",
        "domain": domain,
        "discipline": "Perioperative pharmacology",
        "stem": "What are alternative analgesic adjuncts to opioids for perioperative analgesia?",
        "answer": "Regional anesthesia (epidural, nerve blocks), gabapentin/pregabalin (reduce pain and opioid consumption), ketamine (low-dose 0.5 mg/kg reduces postop pain 20-30%), dexamethasone (anti-inflammatory, reduces pain 15-20%), and acetaminophen.",
        "rationale": "Multimodal approach with complementary mechanisms maximizes analgesia and minimizes opioid requirements.",
        "bloom": "apply",
        "source": [{"book": "Perioperative Pharmacology", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-4",
        "topic": "NSAID and Opioid Alternatives – Adjuvant Pharmacology",
        "domain": domain,
        "discipline": "Perioperative pharmacology",
        "stem": "What is the anesthetic strategy for opioid-tolerant patients?",
        "answer": "Expect higher opioid requirements (can be 10-100x baseline); use IV opioid infusions during case, continue regional anesthesia (epidural) when possible, avoid abrupt withdrawal (acute pain crisis), and involve pain management team preoperatively.",
        "rationale": "Tolerance requires dose escalation; perioperative cross-tolerance to volatile anesthetics also occurs.",
        "bloom": "apply",
        "source": [{"book": "Perioperative Pharmacology", "page": 1}],
        "confusable_with": ""
    }
])

# Neonatal effects
slug = "neonatal_effects_anesthetic"
domain = "Obstetric anesthesia"
missing_kps.extend([
    {
        "id": f"{slug}-1",
        "topic": "Neonatal effects of anesthetic drugs",
        "domain": domain,
        "discipline": "Obstetric anesthesia",
        "stem": "What are the effects of maternal anesthetic agents on the fetus?",
        "answer": "Most IV anesthetics cross placenta (ketamine, propofol, etomidate) but pose minimal fetal risk at induction doses; volatile anesthetics cross freely; high-dose opioids may cause fetal respiratory depression; prolonged exposure increases concern for organ effects.",
        "rationale": "Placental transfer depends on drug lipophilicity and protein binding; short anesthetic exposures for labor/delivery generally well-tolerated.",
        "bloom": "recall",
        "source": [{"book": "Obstetric Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Neonatal effects of anesthetic drugs",
        "domain": domain,
        "discipline": "Obstetric anesthesia",
        "stem": "What is fetal neurotoxicity from anesthetic agents and what is the clinical significance?",
        "answer": "Animal studies suggest prolonged anesthetic exposure (especially volatile agents) may impair fetal neuronal development; clinical significance in short obstetric procedures (minutes) is UNKNOWN; prolonged surgeries (>2 hours) warrant discussion of risks vs benefits.",
        "rationale": "Preclinical data raises concern but clinical obstetric procedures (15-60 min) have not been linked to neurotoxicity.",
        "bloom": "apply",
        "source": [{"book": "Obstetric Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-3",
        "topic": "Neonatal effects of anesthetic drugs",
        "domain": domain,
        "discipline": "Obstetric anesthesia",
        "stem": "What are neonatal withdrawal symptoms and how are they managed?",
        "answer": "Withdrawal from maternal opioids: poor feeding, irritability, low-pitched cry, tremors, hypertonicity appearing 24-72 hours post-birth; management: opioid-containing agents (morphine, methadone) over 7-10 days with gradual taper, supportive care.",
        "rationale": "Chronic maternal opioid exposure leads to fetal dependence; newborn withdrawal is distressing but not life-threatening if managed.",
        "bloom": "apply",
        "source": [{"book": "Obstetric Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-4",
        "topic": "Neonatal effects of anesthetic drugs",
        "domain": domain,
        "discipline": "Obstetric anesthesia",
        "stem": "What APGAR score assessment is done immediately after delivery and what does it measure?",
        "answer": "APGAR score (at 1 and 5 minutes): Appearance (color), Pulse (heart rate), Grimace (reflex irritability/cry), Activity (muscle tone), Respiration. Score 7-10 = normal, 4-6 = moderately depressed, 0-3 = severely depressed.",
        "rationale": "APGAR assesses newborn adaptation to extrauterine life; low scores guide resuscitation intensity.",
        "bloom": "recall",
        "source": [{"book": "Obstetric Anesthesia", "page": 1}],
        "confusable_with": ""
    }
])

# Neuraxial and Regional Anatomy
slug = "neuraxial_regional_anatomy"
domain = "Regional & neuraxial anesthesia"
missing_kps.extend([
    {
        "id": f"{slug}-1",
        "topic": "Neuraxial and Regional Anatomy",
        "domain": domain,
        "discipline": "Regional anesthesia",
        "stem": "What is the anatomic relationship between the intervertebral foramina and nerve root pathways?",
        "answer": "Intervertebral foramina transmit spinal nerves and are bounded by vertebrae (superior/inferior), discs (anterior), and ligaments (posterior); nerve root compression here causes radiculopathy; exits at pedicle level (C5 exits above C5 vertebra, T1 exits below T1, etc.).",
        "rationale": "Foraminal narrowing from disc hernia or spondylosis causes nerve compression; level identification is critical for block targeting.",
        "bloom": "recall",
        "source": [{"book": "Regional Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Neuraxial and Regional Anatomy",
        "domain": domain,
        "discipline": "Regional anesthesia",
        "stem": "What are the cervical plexus levels and what nerves does it form?",
        "answer": "Cervical plexus (C1-C4): superficial branches (greater auricular, transverse cervical, supraclavicular) and deep branches (ansa cervicalis, phrenic nerve); phrenic nerve innervates diaphragm; block at C1-C3 risks phrenic paralysis.",
        "rationale": "Superficial cervical block safe; deep block carries phrenic nerve risk; identification critical.",
        "bloom": "recall",
        "source": [{"book": "Regional Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-3",
        "topic": "Neuraxial and Regional Anatomy",
        "domain": domain,
        "discipline": "Regional anesthesia",
        "stem": "What is the brachial plexus anatomy and the consequence of different needle approaches?",
        "answer": "Brachial plexus (C5-T1) travels with axillary artery/vein from interscalene space through supraclavicular, infraclavicular spaces to axillary; approaches differ: interscalene blocks C5-C6 best but risks phrenic/Horner's, infraclavicular blocks all roots including T1, axillary misses superior trunk.",
        "rationale": "Anatomy determines nerve availability and block coverage; approach selection depends on target nerves.",
        "bloom": "apply",
        "source": [{"book": "Regional Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-4",
        "topic": "Neuraxial and Regional Anatomy",
        "domain": domain,
        "discipline": "Regional anesthesia",
        "stem": "What are the major lower extremity nerves and their relationships to key anatomic landmarks?",
        "answer": "Femoral nerve: lateral to femoral artery in groin, innervates quadriceps and knee; Sciatic nerve: posterior thigh below gluteal fold, innervates hamstrings and distal leg; Saphenous: branch of femoral following medial calf; Common peroneal: lateral knee from sciatic.",
        "rationale": "Anatomic relationships guide blockade; palpable landmarks enable accurate needle placement.",
        "bloom": "recall",
        "source": [{"book": "Regional Anesthesia", "page": 1}],
        "confusable_with": ""
    }
])

# Neurogenic Pulmonary Edema
slug = "neurogenic_pulmonary_edema"
domain = "Critical Care Anesthesia"
missing_kps.extend([
    {
        "id": f"{slug}-1",
        "topic": "Neurogenic Pulmonary Edema",
        "domain": domain,
        "discipline": "Critical care anesthesia",
        "stem": "What is neurogenic pulmonary edema (NPE) and what is its pathophysiology?",
        "answer": "NPE is acute pulmonary edema (frothy, often hemorrhagic) occurring after severe CNS injury (head trauma, stroke, seizure, ICP crisis); caused by massive sympathetic discharge increasing pulmonary capillary pressure and increasing permeability.",
        "rationale": "Catecholamine surge causes vasoconstriction, increased afterload, and acute pulmonary edema; distinguishing from cardiogenic edema is important.",
        "bloom": "recall",
        "source": [{"book": "Critical Care Anesthesia", "page": 1}],
        "confusable_with": "aspiration pneumonitis"
    },
    {
        "id": f"{slug}-2",
        "topic": "Neurogenic Pulmonary Edema",
        "domain": domain,
        "discipline": "Critical care anesthesia",
        "stem": "What are the clinical features that distinguish NPE from other causes of pulmonary edema?",
        "answer": "NPE: sudden onset (minutes to hours after CNS event), often with hypertension and tachycardia, pink frothy sputum, bilateral infiltrates, normal cardiac function on echo; history of CNS event is KEY.",
        "rationale": "NPE recognition is critical because it guides treatment (fluid restriction, diuretics) different from cardiogenic edema.",
        "bloom": "apply",
        "source": [{"book": "Critical Care Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-3",
        "topic": "Neurogenic Pulmonary Edema",
        "domain": domain,
        "discipline": "Critical care anesthesia",
        "stem": "What is the management of neurogenic pulmonary edema?",
        "answer": "Treat underlying CNS cause (lower ICP, manage seizures), respiratory support (mechanical ventilation if severe), diuretics (aggressive to reduce pulmonary water), vasodilators (reduce afterload), fluid restriction, PEEP to improve oxygenation, and supportive care.",
        "rationale": "Goals are to reduce pulmonary capillary pressure and improve oxygenation while managing CNS pathology.",
        "bloom": "apply",
        "source": [{"book": "Critical Care Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-4",
        "topic": "Neurogenic Pulmonary Edema",
        "domain": domain,
        "discipline": "Critical care anesthesia",
        "stem": "What is the prognosis of neurogenic pulmonary edema and what factors influence outcome?",
        "answer": "NPE carries high mortality (30-50%) when severe; outcome depends more on underlying CNS injury than NPE itself; resolution typically occurs over days to weeks with diuresis and respiratory support; surviving patients often have residual neurologic deficits from CNS injury.",
        "rationale": "NPE is marker of severe CNS injury; treating NPE alone insufficient without addressing underlying pathology.",
        "bloom": "apply",
        "source": [{"book": "Critical Care Anesthesia", "page": 1}],
        "confusable_with": ""
    }
])

# Neurological Complications of Cardiac Surgery
slug = "neurological_complications_cardiac"
domain = "Cardiac anesthesia"
missing_kps.extend([
    {
        "id": f"{slug}-1",
        "topic": "Neurological Complications of Cardiac Surgery",
        "domain": domain,
        "discipline": "Cardiothoracic anesthesia",
        "stem": "What are the types of neurological complications after cardiac surgery with cardiopulmonary bypass?",
        "answer": "Type 1 (stroke, TIA): cerebrovascular accident from embolism/hypoperfusion; Type 2 (diffuse encephalopathy): subtle cognitive dysfunction, delirium, postoperative confusion common in elderly.",
        "rationale": "Type 1 (5-10%) causes major morbidity; Type 2 (50% mild, 10% severe) usually resolves but may impact recovery.",
        "bloom": "recall",
        "source": [{"book": "Cardiac Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Neurological Complications of Cardiac Surgery",
        "domain": domain,
        "discipline": "Cardiothoracic anesthesia",
        "stem": "What mechanisms cause stroke during cardiac surgery?",
        "answer": "Embolic: air bubbles (inadequate de-airing), atherosclerotic plaque (aortic manipulation), thrombi from CPB circuit, paradoxical embolism through PFO; Hyperperfusive: hypotension during CPB, inadequate brain perfusion during hypothermia.",
        "rationale": "Multiple contributors; surgical and anesthetic techniques target each mechanism.",
        "bloom": "apply",
        "source": [{"book": "Cardiac Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-3",
        "topic": "Neurological Complications of Cardiac Surgery",
        "domain": domain,
        "discipline": "Cardiothoracic anesthesia",
        "stem": "What are the strategies to prevent neurological complications during cardiac surgery?",
        "answer": "Operative: careful aortic manipulation, meticulous de-airing, arterial line filter, gentle CPB priming, avoid atherosclerosis-prone aortic sites for cannulation; Anesthetic: maintain adequate perfusion pressure (MAP >50 on CPB), maintain normothermia, minimize emboli.",
        "rationale": "Multifactorial prevention approach reduces stroke incidence.",
        "bloom": "apply",
        "source": [{"book": "Cardiac Anesthesia", "page": 1}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-4",
        "topic": "Neurological Complications of Cardiac Surgery",
        "domain": domain,
        "discipline": "Cardiothoracic anesthesia",
        "stem": "What is the role of neuromonitoring in cardiac surgery?",
        "answer": "Cerebral oximetry (NIRS) monitors regional cerebral O2 saturation, alerting to desaturation; EEG monitors cerebral electrical activity, detecting burst suppression; carotid ultrasound screens for atherosclerosis; clinical utility debated but may guide intraoperative management.",
        "rationale": "Neuromonitoring allows real-time detection of cerebral compromise but hasn't consistently reduced stroke incidence.",
        "bloom": "apply",
        "source": [{"book": "Cardiac Anesthesia", "page": 1}],
        "confusable_with": ""
    }
])

# Combine and save
all_kps = existing_kps + missing_kps

with open('data/kp_full_part_23.json', 'w', encoding='utf-8') as f:
    json.dump(all_kps, f, indent=2, ensure_ascii=False)

print(f"Wrote {len(all_kps)} total entries to kp_full_part_23.json")
print(f"Added {len(missing_kps)} new KPs for {len(set(x['topic'] for x in missing_kps))} missing topics")

# Validate JSON
try:
    with open('data/kp_full_part_23.json', 'r', encoding='utf-8') as f:
        json.load(f)
    print("JSON validation: OK")
except Exception as e:
    print(f"JSON validation failed: {e}")
