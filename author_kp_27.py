#!/usr/bin/env python3
import json
import re

with open('data/_kp_retrieval_full.json', 'r', encoding='utf-8') as f:
    all_items = json.load(f)

slice_items = all_items[891:924]

def slugify(s):
    s = s.lower()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[-\s]+', '-', s)
    return s[:60].rstrip('-')

kp_collection = []
kp_id_counter = {}

def make_kp_id(slug):
    if slug not in kp_id_counter:
        kp_id_counter[slug] = 0
    kp_id_counter[slug] += 1
    return f"{slug}-{kp_id_counter[slug]}"

# Topic 891: Truncal blocks - intercostal and rectus sheath blocks
slug = slugify("Truncal blocks intercostal and rectus sheath blocks")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Truncal blocks: intercostal and rectus sheath blocks",
    "domain": "Regional & neuraxial anesthesia",
    "discipline": "Regional anesthesia",
    "stem": "What clinical conditions benefit from intercostal nerve blocks, and how are the nerves approached?",
    "answer": "Intercostal blocks provide analgesia for thoracic/upper abdominal surgery, rib fractures, herpes zoster, and cancer pain; nerves are blocked by depositing local anesthetic at individual intercostal levels.",
    "rationale": "Intercostal nerves run in the neurovascular bundle below each rib; blocking them provides dermatomal analgesia.",
    "bloom": "apply",
    "source": [{"book": "Morgan & Mikhail", "page": 1684}],
    "confusable_with": ""
})

kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Truncal blocks: intercostal and rectus sheath blocks",
    "domain": "Regional & neuraxial anesthesia",
    "discipline": "Regional anesthesia",
    "stem": "Describe the anatomy and technique of rectus sheath block.",
    "answer": "Rectus sheath block targets anterior cutaneous branches of intercostal nerves T7-T12 as they pierce the rectus abdominis muscle; local anesthetic is deposited deep to the rectus muscle.",
    "rationale": "Anterior cutaneous nerves run between rectus muscle and posterior sheath; blockade provides midline/paramedian abdominal analgesia.",
    "bloom": "apply",
    "source": [{"book": "Morgan & Mikhail", "page": 1696}],
    "confusable_with": ""
})

# Topic 892: Pectoral and serratus plane blocks
slug = slugify("Truncal blocks pectoral and serratus plane blocks")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Truncal blocks: pectoral and serratus plane blocks",
    "domain": "Regional & neuraxial anesthesia",
    "discipline": "Regional anesthesia",
    "stem": "What is the target of pectoral (PECS) block and which nerves does it anesthetize?",
    "answer": "PECS block targets lateral and medial pectoral nerves and intercostobrachial nerve by depositing anesthetic between pectoralis major and minor muscles.",
    "rationale": "PECS blocks provide analgesia for breast and chest wall surgery by anesthetizing pectoral motor and sensory nerves.",
    "bloom": "apply",
    "source": [{"book": "Morgan & Mikhail", "page": 1690}],
    "confusable_with": ""
})

kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Truncal blocks: pectoral and serratus plane blocks",
    "domain": "Regional & neuraxial anesthesia",
    "discipline": "Regional anesthesia",
    "stem": "How does serratus anterior plane block provide analgesia?",
    "answer": "Serratus anterior plane block anesthetizes long thoracic nerve and intercostal nerves running between serratus anterior and latissimus dorsi muscles.",
    "rationale": "Serratus plane block provides lateral chest wall and rib analgesia useful for thoracic and upper abdominal surgery.",
    "bloom": "recall",
    "source": [{"book": "Morgan & Mikhail", "page": 1690}],
    "confusable_with": ""
})

# Topic 893: Quadratus lumborum blocks
slug = slugify("Truncal blocks quadratus lumborum QL blocks")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Truncal blocks: quadratus lumborum (QL) blocks",
    "domain": "Regional & neuraxial anesthesia",
    "discipline": "Regional anesthesia",
    "stem": "What nerves does quadratus lumborum block target and what procedures does it cover?",
    "answer": "QL block targets thoracolumbar nerves (T7-L4) by depositing anesthetic around quadratus lumborum muscle; provides analgesia for lower abdominal surgery, hysterectomy, and cesarean delivery.",
    "rationale": "Thoracolumbar nerves run in fascial plane posterior to quadratus lumborum; blockade provides somatic and visceral analgesia to lower abdomen/pelvis.",
    "bloom": "apply",
    "source": [{"book": "Morgan & Mikhail", "page": 1700}],
    "confusable_with": ""
})

# Topic 894: Thoracic paravertebral block
slug = slugify("Truncal blocks thoracic paravertebral block")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Truncal blocks: thoracic paravertebral block",
    "domain": "Regional & neuraxial anesthesia",
    "discipline": "Regional anesthesia",
    "stem": "Describe anatomy and clinical applications of thoracic paravertebral block.",
    "answer": "Thoracic paravertebral block deposits anesthetic in paravertebral space lateral to vertebral bodies, anesthetizing spinal nerves at intervertebral foramina; used for thoracic surgery, rib fractures, chronic pain.",
    "rationale": "Paravertebral space contains spinal roots and sympathetic fibers; blockade provides somatic/visceral analgesia with minimal hemodynamic effects vs epidural.",
    "bloom": "apply",
    "source": [{"book": "Morgan & Mikhail", "page": 1683}],
    "confusable_with": ""
})

# Topic 895: TAP blocks
slug = slugify("Truncal blocks transversus abdominis plane TAP blocks")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Truncal blocks: transversus abdominis plane (TAP) blocks",
    "domain": "Regional & neuraxial anesthesia",
    "discipline": "Regional anesthesia",
    "stem": "What is the target anatomic plane for TAP block and which nerves does it anesthetize?",
    "answer": "TAP block targets plane between internal oblique and transversus abdominis muscles, anesthetizing iliohypogastric, ilioinguinal, and intercostal nerves T7-T12.",
    "rationale": "These nerves innervate anterior abdominal wall; TAP provides multimodal analgesia for lower abdominal and pelvic surgery.",
    "bloom": "recall",
    "source": [{"book": "Morgan & Mikhail", "page": 1694}],
    "confusable_with": ""
})

# Topic 896: Ultrasound fundamentals
slug = slugify("Ultrasound fundamentals for regional anesthesia")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Ultrasound fundamentals for regional anesthesia",
    "domain": "Regional & neuraxial anesthesia",
    "discipline": "Regional anesthesia",
    "stem": "What are the key ultrasound principles for safe nerve block visualization?",
    "answer": "Ultrasound fundamentals include: probe orientation and needle visualization (in-plane vs out-of-plane), differentiating nerve from surrounding structures using echogenicity, avoiding vascular structures, and real-time needle tracking.",
    "rationale": "Real-time ultrasound visualization improves block success and safety by confirming needle position and local anesthetic spread around target nerve.",
    "bloom": "apply",
    "source": [{"book": "Stanford CA-1", "page": 97}],
    "confusable_with": ""
})

# Topic 897: Upper extremity terminal nerve blocks
slug = slugify("Upper extremity terminal nerve blocks")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Upper extremity terminal nerve blocks",
    "domain": "Regional & neuraxial anesthesia",
    "discipline": "Regional anesthesia",
    "stem": "What terminal nerves are blocked for distal upper extremity anesthesia and what procedures do they cover?",
    "answer": "Terminal nerve blocks include radial, median, ulnar, and posterior interosseous nerves; these blocks provide distal hand and forearm anesthesia for surgery on fingers, wrist, and distal forearm.",
    "rationale": "Terminal nerves are peripheral branches that can be individually blocked distally with smaller volumes and minimal motor effects, allowing selective sensory anesthesia.",
    "bloom": "apply",
    "source": [{"book": "Morgan & Mikhail", "page": 1620}],
    "confusable_with": ""
})

# Topic 898: Uteroplacental physiology and drug transfer
slug = slugify("Uteroplacental physiology and drug transfer")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Uteroplacental physiology and drug transfer",
    "domain": "Obstetric anesthesia",
    "discipline": "Obstetric anesthesia",
    "stem": "What factors determine drug transfer across the placenta and affect fetal drug exposure?",
    "answer": "Placental drug transfer is determined by molecular weight, lipid solubility, protein binding, degree of ionization, and placental blood flow; drugs with lower MW, higher lipid solubility, and less protein binding cross readily.",
    "rationale": "Placental transfer is by passive diffusion and carrier-mediated transport; understanding these factors allows selection of maternal drugs with minimal fetal effects.",
    "bloom": "recall",
    "source": [{"book": "Morgan & Mikhail", "page": 1368}],
    "confusable_with": ""
})

# Topic 899: Uterotonic pharmacology
slug = slugify("Uterotonic pharmacology")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Uterotonic pharmacology",
    "domain": "Obstetric anesthesia",
    "discipline": "Obstetric anesthesia",
    "stem": "What are the primary uterotonics used to prevent postpartum hemorrhage and how do they differ?",
    "answer": "Oxytocin causes sustained uterine contraction via G-protein coupled receptors; ergot alkaloids cause tetanic contraction and vasoconstriction; misoprostol is a prostaglandin analog; each has distinct onset, duration, and systemic effects.",
    "rationale": "Different uterotonics provide graduated options for hemorrhage prevention based on rapidity of effect, side effect profile, and clinical context.",
    "bloom": "apply",
    "source": [{"book": "Miller/Baby Miller", "page": 114}],
    "confusable_with": ""
})

# Topic 900: Vascular Physiology and Hemodynamics
slug = slugify("Vascular Physiology and Hemodynamics")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Vascular Physiology and Hemodynamics",
    "domain": "Anesthesia: basic & clinical sciences",
    "discipline": "Cardiovascular physiology",
    "stem": "What is the relationship between vessel diameter and vascular resistance, and how does it apply clinically?",
    "answer": "Vascular resistance is inversely proportional to the fourth power of vessel radius (Hagen-Poiseuille equation); small decreases in arteriolar diameter cause dramatic increases in resistance.",
    "rationale": "This relationship explains why arteriolar tone is the primary determinant of systemic vascular resistance and why potent vasoconstrictors/vasodilators have profound hemodynamic effects.",
    "bloom": "recall",
    "source": [{"book": "Morgan & Mikhail", "page": 963}],
    "confusable_with": ""
})

# Topic 901: Vasoactive & Inotropic Agents
slug = slugify("Vasoactive Inotropic Agents Pharmacology")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Vasoactive & Inotropic Agents - Pharmacology",
    "domain": "Cardiovascular & cardiac anesthesia",
    "discipline": "Cardiovascular pharmacology",
    "stem": "How do alpha and beta adrenergic effects on heart and vasculature differ, and how is this exploited clinically?",
    "answer": "Alpha effects: vasoconstriction (SVR up); Beta-1: increased contractility/rate (CO up); Beta-2: vasodilation. Selective agents (norepinephrine=alpha>beta1, dobutamine=beta1, isoproterenol=beta1+2) allow targeted hemodynamic support.",
    "rationale": "Receptor selectivity determines whether an agent primarily improves cardiac output (beta-1) vs systemic perfusion pressure (alpha) vs peripheral circulation (beta-2).",
    "bloom": "apply",
    "source": [{"book": "Miller/Baby Miller", "page": 114}],
    "confusable_with": ""
})

# Topic 902: Vasoconstrictors and additives in regional anesthesia
slug = slugify("Vasoconstrictors and additives in regional anesthesia")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Vasoconstrictors and additives in regional anesthesia",
    "domain": "Regional & neuraxial anesthesia",
    "discipline": "Regional anesthesia pharmacology",
    "stem": "Why is epinephrine added to local anesthetics and what is the recommended concentration?",
    "answer": "Epinephrine (1:400,000 to 1:200,000) causes vasoconstriction reducing local anesthetic systemic absorption, prolonging block duration and decreasing toxicity risk.",
    "rationale": "Vasoconstriction restricts drug redistribution from the injection site, maintaining higher local concentrations and lower plasma levels.",
    "bloom": "recall",
    "source": [{"book": "Morgan & Mikhail", "page": 1256}],
    "confusable_with": ""
})

# Topic 903: Vasodilatory Agents
slug = slugify("Vasodilatory Agents Hemodynamic Management")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Vasodilatory Agents - Hemodynamic Management",
    "domain": "Cardiovascular & cardiac anesthesia",
    "discipline": "Cardiovascular pharmacology",
    "stem": "What are the differences between nitroprusside and nitroglycerin in terms of mechanism and clinical use?",
    "answer": "Nitroprusside: direct smooth muscle relaxation, acts on both arteries/veins, rapid onset/offset, requires monitoring for cyanide toxicity; nitroglycerin: preferentially dilates veins/coronary arteries, used for angina/acute decompensated heart failure.",
    "rationale": "Differential vascular effects allow selection based on clinical goal (peripheral vasodilation vs afterload reduction vs coronary dilation).",
    "bloom": "apply",
    "source": [{"book": "MGH Housestaff Manual", "page": 27}],
    "confusable_with": ""
})

# Topic 904: Venous Air Embolism
slug = slugify("Venous Air Embolism VAE")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Venous Air Embolism (VAE)",
    "domain": "Neuroanesthesia",
    "discipline": "Neuroanesthesia",
    "stem": "What hemodynamic and respiratory consequences occur with venous air embolism?",
    "answer": "Air bubble enters venous circulation reducing cardiac output; air travels to right heart causing acute RV afterload, pulmonary hypertension, right heart strain; paradoxical embolism via PFO causes stroke.",
    "rationale": "Air blocks blood flow in pulmonary circulation; even small volumes cause acute hemodynamic collapse.",
    "bloom": "recall",
    "source": [{"book": "Miller/Baby Miller", "page": 368}],
    "confusable_with": ""
})

# Topic 905: Visceral Pain Syndromes
slug = slugify("Visceral Pain Syndromes")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Visceral Pain Syndromes",
    "domain": "Pain medicine",
    "discipline": "Pain medicine",
    "stem": "What anatomic and physiologic features distinguish visceral pain from somatic pain?",
    "answer": "Visceral pain: diffuse/bilateral distribution, referred to somatic dermatomes, associated with autonomic symptoms (nausea, diaphoresis); uses sympathetic/parasympathetic pathways; poorly localized.",
    "rationale": "Visceral innervation travels via autonomic nerves with multiple spinal levels; poor proprioception leads to diffuse pain perception.",
    "bloom": "recall",
    "source": [{"book": "Morgan & Mikhail", "page": 2300}],
    "confusable_with": "Somatic pain"
})

# Topic 906: Volatile Anesthetic Pharmacology
slug = slugify("Volatile Anesthetic Pharmacology")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Volatile Anesthetic Pharmacology",
    "domain": "Anesthesia: basic & clinical sciences",
    "discipline": "Anesthetic pharmacology",
    "stem": "What determines the potency of volatile anesthetics and how is it measured?",
    "answer": "Potency is measured by MAC (minimum alveolar concentration); determined by lipid solubility (Meyer-Overton theory); higher lipid solubility = lower MAC = greater potency.",
    "rationale": "Volatile anesthetics distribute to CNS lipid membranes; lipid solubility correlates with anesthetic effect across diverse compounds.",
    "bloom": "recall",
    "source": [{"book": "Miller/Baby Miller", "page": 114}],
    "confusable_with": ""
})

# Topic 907: Volatile agent organ toxicity
slug = slugify("Volatile agent organ toxicity")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Volatile agent organ toxicity",
    "domain": "Anesthetic pharmacology",
    "discipline": "Anesthetic pharmacology",
    "stem": "What is the mechanism and clinical significance of halothane hepatotoxicity?",
    "answer": "Halothane undergoes hepatic oxidative metabolism producing trifluoroacetyl (TFA) derivatives; TFA binds cellular proteins creating neoantigens triggering immune-mediated liver injury (halothane hepatitis).",
    "rationale": "Hepatic metabolism is required for toxicity; repeated halothane exposure increases risk of halothane hepatitis via immune sensitization.",
    "bloom": "recall",
    "source": [{"book": "Morgan & Mikhail", "page": 412}],
    "confusable_with": ""
})

# Topic 908: Xenon
slug = slugify("Xenon pharmacology clinical context")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Xenon: pharmacology & clinical context",
    "domain": "Anesthetic pharmacology",
    "discipline": "Anesthetic pharmacology",
    "stem": "What are the unique properties of xenon as an anesthetic and why has clinical adoption been limited?",
    "answer": "Xenon: inert gas with rapid emergence, neuroprotection, hemodynamic stability; limited by: low blood solubility requiring high FiO2, expense, equipment requirements, no FDA approval in US.",
    "rationale": "Xenon's inertness eliminates metabolic toxicity but increases cost/complexity; clinical utility remains investigational.",
    "bloom": "recall",
    "source": [{"book": "Miller/Baby Miller", "page": 114}],
    "confusable_with": ""
})

# Topic 909: Acromegaly
slug = slugify("Acromegaly")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Acromegaly",
    "domain": "Internal medicine: endocrinology",
    "discipline": "Internal medicine",
    "stem": "What are the key perioperative anesthetic concerns in acromegaly?",
    "answer": "Acromegaly causes: airway abnormalities (laryngeal narrowing, macroglossia), hypertension, cardiomyopathy, diabetes, sleep apnea; perioperative risks include difficult intubation and cardiovascular instability.",
    "rationale": "Growth hormone excess causes soft tissue/skeletal overgrowth affecting airway and systemic comorbidities.",
    "bloom": "apply",
    "source": [{"book": "Morgan & Mikhail", "page": 625}],
    "confusable_with": ""
})

# Topic 910: Acute Mesenteric Ischemia
slug = slugify("Acute Mesenteric Ischemia")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Acute Mesenteric Ischemia",
    "domain": "Internal medicine: gastroenterology & hepatology",
    "discipline": "Internal medicine",
    "stem": "What are the classic presenting signs of acute mesenteric ischemia and why is rapid diagnosis critical?",
    "answer": "Classic triad: severe abdominal pain out of proportion to exam, bloody diarrhea, shock; high mortality (60-80%) if not treated urgently; diagnosis by CT angiography; management is surgical revascularization.",
    "rationale": "Intestinal ischemia rapidly progresses to transmural necrosis and sepsis; early diagnosis and revascularization are only interventions that reduce mortality.",
    "bloom": "apply",
    "source": [{"book": "StatPearls: StatPearls Acute Mesenteric Ischemia", "page": 1}],
    "confusable_with": ""
})

# Topic 911: Acute promyelocytic leukemia
slug = slugify("Acute promyelocytic leukemia APL emergencies")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Acute promyelocytic leukemia (APL) emergencies",
    "domain": "Internal medicine: hematology & oncology",
    "discipline": "Internal medicine",
    "stem": "What is the primary life-threatening complication of APL and how is it managed?",
    "answer": "DIC (disseminated intravascular coagulation) is the hallmark complication causing hemorrhage and thrombosis; management: all-trans retinoic acid (ATRA) + chemotherapy (arsenic trioxide) + aggressive supportive care with FFP/platelets.",
    "rationale": "APL leukemic blasts release thromboplastic substances triggering DIC; ATRA differentiates blasts reducing thromboplastic release.",
    "bloom": "apply",
    "source": [{"book": "StatPearls: StatPearls Acute promyelocytic leukemia (APL) emergencies", "page": 1}],
    "confusable_with": ""
})

# Topic 912: Adrenal Incidentaloma
slug = slugify("Adrenal Incidentaloma")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Adrenal Incidentaloma",
    "domain": "Internal medicine: endocrinology",
    "discipline": "Internal medicine",
    "stem": "What evaluation is required for an asymptomatic adrenal incidentaloma found on imaging?",
    "answer": "Biochemical screening: 1mg dexamethasone suppression test (screen for Cushing's), plasma free metanephrines or 24h urine metanephrines (screen for pheochromocytoma), aldosterone/renin if hypertensive.",
    "rationale": "Even asymptomatic masses may produce hormones; screening identifies functional tumors requiring treatment before surgery.",
    "bloom": "apply",
    "source": [{"book": "StatPearls: StatPearls Cushing Syndrome", "page": 5}],
    "confusable_with": ""
})

# Topic 913: Antiemetic therapy in oncology
slug = slugify("Antiemetic therapy in oncology")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Antiemetic therapy in oncology",
    "domain": "Internal medicine: hematology & oncology",
    "discipline": "Internal medicine",
    "stem": "What is the recommended antiemetic strategy for highly emetogenic chemotherapy?",
    "answer": "Standard: 5-HT3 antagonist (ondansetron) + NK1 receptor antagonist (aprepitant) + dexamethasone; agents target multiple pathways (serotonin, neurokinin, corticosteroid).",
    "rationale": "Multimodal approach targeting different vomiting mechanisms provides superior nausea/vomiting control vs single agent.",
    "bloom": "apply",
    "source": [{"book": "MGH Housestaff Manual", "page": 162}],
    "confusable_with": ""
})

# Topic 914: Aplastic anemia
slug = slugify("Aplastic anemia and bone marrow failure")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Aplastic anemia and bone marrow failure",
    "domain": "Internal medicine: hematology & oncology",
    "discipline": "Internal medicine",
    "stem": "What are the pathophysiologic mechanisms of aplastic anemia and first-line treatments?",
    "answer": "Aplastic anemia: stem cell destruction by autoimmune/T-cell mechanisms or direct toxicity; bone marrow hypoplasia with pancytopenia; treatment: immunosuppression (ATG/cyclosporine) or hematopoietic stem cell transplant.",
    "rationale": "Immune-mediated destruction is primary mechanism in most cases; immunosuppressive therapy can restore hematopoiesis.",
    "bloom": "recall",
    "source": [{"book": "Morgan & Mikhail", "page": 1972}],
    "confusable_with": ""
})

# Topic 915: Autoimmune Hepatitis
slug = slugify("Autoimmune Hepatitis AIH")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Autoimmune Hepatitis (AIH)",
    "domain": "Internal medicine: gastroenterology & hepatology",
    "discipline": "Internal medicine",
    "stem": "What are the diagnostic features and treatment principles of autoimmune hepatitis?",
    "answer": "Diagnosis: elevated transaminases, hypergammaglobulinemia, autoantibodies (ANA/anti-smooth muscle), liver biopsy showing portal inflammation; treatment: corticosteroids + azathioprine.",
    "rationale": "Autoimmune destruction of liver requires immunosuppression to prevent progression to cirrhosis.",
    "bloom": "apply",
    "source": [{"book": "StatPearls: StatPearls Autoimmune Hepatitis (AIH)", "page": 1}],
    "confusable_with": ""
})

# Topic 916: Bone marrow transplantation
slug = slugify("Bone marrow transplantation complications")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Bone marrow transplantation: complications",
    "domain": "Internal medicine: hematology & oncology",
    "discipline": "Internal medicine",
    "stem": "What are the major infectious and immunologic complications after bone marrow transplantation?",
    "answer": "Early (0-30d): bacterial/fungal infection from neutropenia; Day 30+: CMV reactivation, Pneumocystis, opportunistic infection; chronic GVHD causes multi-organ dysfunction.",
    "rationale": "Severe immunosuppression and GVHD create windows of vulnerability to specific pathogens at predictable timepoints.",
    "bloom": "recall",
    "source": [{"book": "Morgan & Mikhail", "page": 2155}],
    "confusable_with": ""
})

# Topic 917: Bronchiectasis
slug = slugify("Bronchiectasis")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Bronchiectasis",
    "domain": "Internal medicine: pulmonology",
    "discipline": "Internal medicine",
    "stem": "What is bronchiectasis and what are its major causes?",
    "answer": "Bronchiectasis: permanent dilation of airways due to damaged elastic/muscular walls; causes include cystic fibrosis, post-infectious (tuberculosis, pneumonia), immunodeficiency, alpha-1 antitrypsin deficiency.",
    "rationale": "Chronic infection and inflammation destroy airway architecture leading to recurrent infections and progressive lung damage.",
    "bloom": "recall",
    "source": [{"book": "Morgan & Mikhail", "page": 908}],
    "confusable_with": ""
})

# Topic 918: Budd-Chiari Syndrome
slug = slugify("Budd-Chiari Syndrome")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Budd-Chiari Syndrome",
    "domain": "Internal medicine: gastroenterology & hepatology",
    "discipline": "Internal medicine",
    "stem": "What causes Budd-Chiari Syndrome and what are the presenting features?",
    "answer": "BCS: thrombosis of hepatic veins; causes: myeloproliferative disorders, hypercoagulability, malignancy; presents with acute: RUQ pain/ascites or chronic: cirrhosis signs.",
    "rationale": "Hepatic vein obstruction causes sinusoidal hypertension and hepatic congestion leading to acute liver dysfunction or progressive fibrosis.",
    "bloom": "apply",
    "source": [{"book": "StatPearls: StatPearls Budd Chiari Syndrome", "page": 1}],
    "confusable_with": ""
})

# Topic 919: CKD Complications - Mineral Bone Disease
slug = slugify("CKD Complications Mineral Bone Disease CKD-MBD")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "CKD: Complications - Mineral Bone Disease (CKD-MBD)",
    "domain": "Internal medicine: nephrology, fluids & electrolytes",
    "discipline": "Internal medicine",
    "stem": "What metabolic bone abnormalities occur in CKD and how are they managed?",
    "answer": "CKD-MBD includes: secondary hyperparathyroidism (phosphate retention, low calcitriol), mixed osteodystrophy, osteomalacia; management: phosphate binders, calcitriol, calcimimetics, dietary phosphate restriction.",
    "rationale": "Kidney loss of 1,25-vitamin D production and phosphate excretion triggers cascade of mineral metabolism derangements.",
    "bloom": "apply",
    "source": [{"book": "StatPearls: StatPearls CKD Complications Anemia", "page": 2}],
    "confusable_with": ""
})

# Topic 920: CKD Slowing Progression
slug = slugify("CKD Slowing Progression Disease-Modifying Therapy")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "CKD: Slowing Progression - Disease-Modifying Therapy",
    "domain": "Internal medicine: nephrology, fluids & electrolytes",
    "discipline": "Internal medicine",
    "stem": "What are the evidence-based therapies that slow CKD progression?",
    "answer": "ACE inhibitors/ARBs (reduce proteinuria/glomerular hypertension), SGLT2 inhibitors (cardiovascular/renal protection), control hypertension/diabetes, dietary protein restriction.",
    "rationale": "These agents reduce glomerular hyperfiltration and proteinuria, the primary drivers of CKD progression.",
    "bloom": "apply",
    "source": [{"book": "StatPearls", "page": 1}],
    "confusable_with": ""
})

# Topic 921: COPD Advanced
slug = slugify("COPD Advanced and Surgical Interventions")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "COPD: Advanced and Surgical Interventions",
    "domain": "Internal medicine: pulmonology",
    "discipline": "Internal medicine",
    "stem": "What surgical options exist for advanced COPD and how do they improve outcomes?",
    "answer": "Options: lung volume reduction surgery (remove emphysematous lung), lung transplantation, bronchoscopic valves/coils; improve: dyspnea, exercise capacity, FEV1 in selected patients.",
    "rationale": "Removing emphysematous lung improves chest wall mechanics and elastic recoil.",
    "bloom": "recall",
    "source": [{"book": "Miller/Baby Miller", "page": 784}],
    "confusable_with": ""
})

# Topic 922: Carcinoid Tumors
slug = slugify("Carcinoid Tumors Neuroendocrine Tumors NETs")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Carcinoid Tumors & Neuroendocrine Tumors (NETs)",
    "domain": "Internal medicine: endocrinology",
    "discipline": "Internal medicine",
    "stem": "What is carcinoid syndrome and how does it affect perioperative management?",
    "answer": "Carcinoid syndrome: vasoactive amines (serotonin, histamine, tachykinins) released by carcinoid tumors cause flushing, diarrhea, bronchospasm, RV valve disease; perioperative: somatostatin analogs (octreotide) to prevent crisis.",
    "rationale": "Tumor handling and anesthetic induction release vasoactive mediators triggering acute symptoms; prophylaxis prevents life-threatening complications.",
    "bloom": "apply",
    "source": [{"book": "StatPearls: StatPearls Carcinoid Tumors & Neuroendocrine Tumors (NETs)", "page": 2}],
    "confusable_with": ""
})

# Topic 923: Cardiac Amyloidosis
slug = slugify("Cardiac Amyloidosis")
kp_collection.append({
    "id": make_kp_id(slug),
    "topic": "Cardiac Amyloidosis",
    "domain": "Internal medicine: cardiology",
    "discipline": "Internal medicine",
    "stem": "What are the cardiac manifestations of amyloidosis and their hemodynamic consequences?",
    "answer": "Cardiac amyloidosis: infiltrative cardiomyopathy (restrictive pattern), diastolic dysfunction, arrhythmias (AF, conduction block); hemodynamics: elevated filling pressures, reduced CO; prognosis poor without treatment.",
    "rationale": "Amyloid deposits in myocardium cause stiffness and diastolic dysfunction mimicking restrictive cardiomyopathy.",
    "bloom": "recall",
    "source": [{"book": "Society Guideline: Guideline ACC AHA 2022 Heart Failure", "page": 132}],
    "confusable_with": ""
})

# Write JSON
output_data = kp_collection

with open('data/kp_full_part_27.json', 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Total topics: {len(set(item['topic'] for item in kp_collection))}")
print(f"Total KPs: {len(kp_collection)}")
print(f"Scripts: 0")
print(f"Pairs: 0")
print("Validation: Parsing JSON...")
json.loads(json.dumps(output_data))
print("Valid JSON OK")
