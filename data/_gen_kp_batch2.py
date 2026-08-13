import json

kps = []

def kp(id_, topic, domain, discipline, stem, answer, rationale, bloom, book, page, confusable=""):
    return {"id": id_, "topic": topic, "domain": domain, "discipline": discipline,
            "stem": stem, "answer": answer, "rationale": rationale,
            "bloom": bloom, "source": [{"book": book, "page": page}],
            "confusable_with": confusable}

def script(topic, discipline, ec, patho, tc, kf, consequence):
    return {"_type": "illness_script", "topic": topic, "discipline": discipline,
            "enabling_conditions": ec, "pathophysiology": patho,
            "time_course": tc, "key_features": kf, "consequence_if_missed": consequence}

def pair(a, b, discriminator):
    return {"_type": "confusable_pair", "topic_a": a, "topic_b": b, "discriminator": discriminator}

with open('data/_kp_retrieval_full.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
sliced = data[33:66]
D = lambda idx: sliced[idx]["domain"]
DI = lambda idx: sliced[idx]["discipline"]
T = lambda idx: sliced[idx]["topic"]

# ── 5: Guillain-Barre Syndrome ──────────────────────────────────────
top = T(5); dom = D(5); dis = DI(5)
kps += [
    kp("gbs-1", top, dom, dis,
       "What is the most common global cause of nonpoliovirus-associated acute flaccid paralysis?",
       "Guillain-Barre syndrome (GBS) is the most common global cause of nonpoliovirus acute flaccid paralysis",
       "Molecular mimicry after infection triggers immune attack on peripheral nerve myelin, disrupting saltatory conduction.",
       "recall", "StatPearls: StatPearls   Guillain Barre Syndrome (", 1),
    kp("gbs-2", top, dom, dis,
       "A patient develops ascending weakness with absent deep tendon reflexes 2 weeks after a GI illness; what is the most likely diagnosis?",
       "Guillain-Barre syndrome: acute immune-mediated polyradiculoneuropathy presenting with ascending weakness and areflexia",
       "Preceding infection (Campylobacter, CMV, EBV) triggers autoimmune demyelination of nerve roots and peripheral nerves.",
       "recall", "StatPearls: StatPearls   Guillain Barre Syndrome (", 2),
    kp("gbs-3", top, dom, dis,
       "What are the three critical organ systems to monitor in GBS for life-threatening complications?",
       "Respiratory (FVC decline, risk of ventilatory failure), cardiac (arrhythmias), and autonomic (hemodynamic instability)",
       "Ascending paralysis can reach respiratory muscles; dysautonomia causes dangerous BP swings and arrhythmias.",
       "apply", "StatPearls: StatPearls   Guillain Barre Syndrome (", 2),
    kp("gbs-4", top, dom, dis,
       "How does pure sensory neuropathy without muscle weakness differ from GBS on exam?",
       "Absent/diminished reflexes without muscle weakness plus numbness/paresthesias (pain, temperature, proprioception loss); peak within 4 weeks",
       "GBS typically causes both motor and sensory involvement; pure sensory variants spare motor fibers but share reflex loss.",
       "analyze", "StatPearls: StatPearls   Guillain Barre Syndrome (", 7),
    kp("gbs-5", top, dom, dis,
       "What two disease-modifying treatments are used for GBS?",
       "IVIG (intravenous immunoglobulin) and plasmapheresis (plasma exchange) are the two evidence-based treatments",
       "Both modalities reduce circulating autoantibodies; IVIG neutralizes them; plasmapheresis removes them directly.",
       "recall", "StatPearls: StatPearls   Guillain Barre Syndrome (", 2),
]
kps.append(script(top, dis,
    "Recent infection (Campylobacter jejuni, CMV, EBV, Mycoplasma, COVID-19); prior vaccination (rare)",
    "Molecular mimicry triggers autoimmune demyelination of nerve roots/peripheral nerves; axonal variants (AMAN/AMSAN) directly damage axons",
    "Ascending weakness/areflexia over days to ~4 weeks; plateau; then slow recovery over weeks to months",
    "Ascending flaccid paralysis, areflexia, albuminocytologic dissociation on CSF (high protein, normal WBC), autonomic instability",
    "Respiratory failure requiring intubation if FVC not monitored; cardiovascular collapse from dysautonomia"))

# ── 6: Headache: Primary Disorders ─────────────────────────────────
top = T(6); dom = D(6); dis = DI(6)
kps += [
    kp("headache-primary-1", top, dom, dis,
       "What mnemonic is used to screen for secondary causes of headache requiring further workup?",
       "SNOOP4: Systemic symptoms, Neurological signs, Onset sudden, Older than 50, Position-dependent, Prior pattern change, Papilledema/pregnancy",
       "Secondary headache red flags indicate structural, vascular, or infectious etiology requiring imaging/LP before treating as primary disorder.",
       "recall", "StatPearls: StatPearls   Headache  Primary Disorde", 7),
    kp("headache-primary-2", top, dom, dis,
       "When headache with red flags requires urgent workup, what imaging is first-line for excluding acute intracranial hemorrhage?",
       "Noncontrast CT of the head is first-line to exclude acute intracranial hemorrhage or mass effect",
       "CT is rapid and highly sensitive for fresh blood (hyperdense); LP follows if CT is negative but SAH is still suspected.",
       "recall", "StatPearls: StatPearls   Headache  Primary Disorde", 8),
    kp("headache-primary-3", top, dom, dis,
       "What is the primary treatment for medication-overuse headache (rebound headache)?",
       "Discontinuing the overused analgesic medication is the primary treatment for medication-overuse headache",
       "Chronic analgesic/triptan overuse sensitizes central pain pathways; withdrawal initially worsens headache before improvement.",
       "apply", "StatPearls: StatPearls   Headache  Primary Disorde", 13),
    kp("headache-primary-4", top, dom, dis,
       "Hypnic headache occurs exclusively during sleep and typically begins after what age?",
       "Hypnic headache typically begins after age 50 and occurs only during sleep, waking the patient",
       "Hypnic headache is a rare primary disorder of sleep-wake regulation, possibly linked to REM sleep disturbances.",
       "recall", "StatPearls: StatPearls   Headache  Primary Disorde", 13),
    kp("headache-primary-5", top, dom, dis,
       "What is the risk of chronic daily headache in patients who overuse abortive therapies?",
       "Medication overuse leads to chronification and conversion to chronic headaches that are intractable and difficult to treat",
       "Repeated analgesic exposure induces central sensitization and reduces the headache threshold.",
       "apply", "StatPearls: StatPearls   Headache  Primary Disorde", 14),
]

# ── 7: Heat-Related Illness (chunks mostly off-topic — 3 KPs max) ───
top = T(7); dom = D(7); dis = DI(7)
# chunks are Infectious Disease / Adrenal / Thyroid topics — minimal usable content
kps += [
    kp("heat-illness-1", top, dom, dis,
       "A patient presents with confusion, hyperthermia, and anhidrosis after outdoor exertion; what is the critical differentiation from heat exhaustion?",
       "Classic heat stroke: core temp >40C with CNS dysfunction (confusion, coma); heat exhaustion preserves mentation",
       "In heat stroke, thermoregulation fails completely; anhidrosis reflects hypothalamic dysfunction. Heat exhaustion retains thermoregulation.",
       "analyze", "MGH Housestaff Manual", 185),
    kp("heat-illness-2", top, dom, dis,
       "What endocrine emergency can mimic heat-related illness with fever, tachycardia, and hemodynamic instability?",
       "Adrenal crisis (acute adrenal insufficiency) can present with fever, hypotension, and shock mimicking heat stroke",
       "Adrenal insufficiency causes glucocorticoid and mineralocorticoid deficiency; stress triggers decompensation with vascular collapse.",
       "analyze", "MGH Housestaff Manual", 185),
    kp("heat-illness-3", top, dom, dis,
       "What thyroid emergency causes hyperthermia, tachycardia, and altered mental status that must be distinguished from heat stroke?",
       "Thyroid storm: hyperthermia, tachycardia/AF, altered mental status; triggered by physiologic stress in uncontrolled hyperthyroidism",
       "Excess thyroid hormone dramatically raises metabolic rate; if TSH is undetectable and T4 elevated, thyroid storm must be considered.",
       "analyze", "MGH Housestaff Manual", 189),
]

# ── 8: Hemodynamic Monitoring ──────────────────────────────────────
top = T(8); dom = D(8); dis = DI(8)
kps += [
    kp("hemodynamic-monitoring-1", top, dom, dis,
       "What pressure does the pulmonary artery catheter measure when the balloon is inflated in the wedge position?",
       "Pulmonary capillary wedge pressure (PCWP), which approximates left atrial pressure and left ventricular end-diastolic pressure",
       "Balloon occludes forward flow; the distal port equilibrates with downstream pulmonary venous/LA pressure.",
       "recall", "Miller/Baby Miller", 397),
    kp("hemodynamic-monitoring-2", top, dom, dis,
       "What does a decrease in systolic BP >10 mmHg with positive-pressure ventilation (systolic pressure variation >10 mmHg) indicate?",
       "The patient is fluid-responsive: cardiac output is likely to increase with an IV fluid bolus",
       "Positive-pressure breath reduces venous return; if CO is preload-dependent (hypovolemic), SBP drops >10 mmHg with each breath.",
       "analyze", "Miller/Baby Miller", 393),
    kp("hemodynamic-monitoring-3", top, dom, dis,
       "What are clinical signs of hypovolemia on physical exam?",
       "Decreased skin turgor, thready pulse, dry mucous membranes, tachycardia, orthostasis, decreased urine output",
       "Reduced intravascular volume activates the sympathetic nervous system; skin vasoconstricts and heart rate rises.",
       "recall", "Stanford CA-1", 46),
    kp("hemodynamic-monitoring-4", top, dom, dis,
       "What laboratory finding in hypovolemia reflects prerenal physiology?",
       "Urine Na <10 mEq/L, urine osmolality >1.010, rising hematocrit, contraction alkalosis then metabolic acidosis",
       "Kidneys avidly retain Na and water in prerenal state; urine Na reflects tubular sodium reabsorption.",
       "recall", "Stanford CA-1", 46),
    kp("hemodynamic-monitoring-5", top, dom, dis,
       "What less-invasive alternative uses the Doppler effect to estimate cardiac output via the descending aorta?",
       "Esophageal Doppler measures blood flow velocity in the descending aorta to estimate cardiac output",
       "Doppler shift in reflected ultrasound frequency is proportional to blood flow velocity; CO is calculated from aortic cross-sectional area.",
       "recall", "Miller/Baby Miller", 398),
    kp("hemodynamic-monitoring-6", top, dom, dis,
       "In heart failure with preserved EF (HFpEF), what is the primary pharmacologic treatment?",
       "Diuretics to prevent volume overload; treat comorbidities (DM, HTN, AF); SGLT2 inhibitors are the only agents shown to reduce CV death in HFpEF",
       "HFpEF results from impaired relaxation; SGLT2i reduce preload, inflammation, and cardiac fibrosis.",
       "apply", "MGH Housestaff Manual", 27),
]

# ── 9 & 10: HAP/VAP (duplicate topics — write once, reference both) ─
top = T(9); dom = D(9); dis = DI(9)
kps += [
    kp("hapvap-1", top, dom, dis,
       "How is HAP distinguished from VAP by timing definition?",
       "HAP: pneumonia >=48h after hospital admission without intubation; VAP: pneumonia >=48h after endotracheal intubation",
       "Endotracheal tube bypasses upper airway defenses and allows direct bacterial aspiration into the lower respiratory tract.",
       "recall", "MGH Housestaff Manual", 117),
    kp("hapvap-2", top, dom, dis,
       "What are the three diagnostic criteria for HAP/VAP on clinical assessment?",
       "New/progressive infiltrates on CXR plus >=2 of: fever, leukocytosis, purulent tracheal secretions",
       "No gold-standard exists for HAP/VAP; >50% of clinical diagnoses are false-positive on postmortem studies.",
       "recall", "Marino ICU Book", 552),
    kp("hapvap-3", top, dom, dis,
       "VAP affects what proportion of mechanically ventilated ICU patients?",
       "VAP affects approximately 5-15% of mechanically ventilated individuals",
       "Prolonged intubation, sedation, aspiration, and supine positioning all increase VAP risk.",
       "recall", "StatPearls: StatPearls   Shock  Classification & P", 7),
    kp("hapvap-4", top, dom, dis,
       "What bundle of VAP prevention measures is recommended?",
       "Head-of-bed elevation 30-45 degrees, oral care with chlorhexidine, daily spontaneous breathing trials, early mobilization, avoid unnecessary reintubation",
       "Most VAP arises from oropharyngeal aspiration; bundle measures reduce colonization and aspiration risk.",
       "apply", "Curated Units", 0),
    kp("hapvap-5", top, dom, dis,
       "What BAL bacterial threshold is used to diagnose VAP microbiologically?",
       "BAL with threshold >=10^4-10^5 CFU/mL is used as the microbiologic threshold for VAP",
       "Lower thresholds include normal oropharyngeal flora; high CFU/mL indicates true lower respiratory infection.",
       "recall", "Curated Units", 0),
    kp("hapvap-6", top, dom, dis,
       "What is the most common infection acquired in the ICU?",
       "Pneumonia (HAP/VAP) is the most common infection acquired in the ICU",
       "Mechanical ventilation, immunosuppression, and aspiration risk converge in critically ill patients to make pneumonia highly prevalent.",
       "recall", "Marino ICU Book", 552),
]

print(f"Batch2 items: {len(kps)}")
with open('data/_kp_batch2.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("OK")
