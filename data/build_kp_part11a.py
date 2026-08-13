
import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

output = []

# ============================================================
# ITEM 363: CKD: Slowing Progression — Disease-Modifying Therapy
# ============================================================
topic = "CKD: Slowing Progression — Disease-Modifying Therapy"
domain = "Internal medicine: nephrology, fluids & electrolytes"
discipline = "medicine"

kps = [
  {"id":"ckd-slowing-progression-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"A patient with CKD G3-G5 asks about dietary protein. What protein intake does KDIGO 2024 suggest?",
   "answer":"Maintain 0.8 g/kg body weight/day; avoid high protein >1.3 g/kg/day in those at risk of progression.",
   "rationale":"High protein intake increases glomerular hyperfiltration and accelerates CKD progression.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":93}],
   "confusable_with":""},

  {"id":"ckd-slowing-progression-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Which agent from the FIGARO-DKD and FIDELIO-DKD trials reduces CKD outcomes in type 2 diabetes?",
   "answer":"Finerenone, a non-steroidal mineralocorticoid receptor antagonist, reduces CKD progression and cardiovascular events in T2DM-associated CKD.",
   "rationale":"Finerenone selectively blocks mineralocorticoid receptors in the kidney and heart, reducing proteinuria and fibrosis without the hyperkalemia risk of steroidal MRAs.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":191}],
   "confusable_with":"spironolactone (steroidal MRA with greater hyperkalemia risk)"},

  {"id":"ckd-slowing-progression-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Early identification and referral to specialist kidney care services is emphasized because it has potential to do what?",
   "answer":"Early specialist referral can reverse, delay, or prevent CKD progression; referral thresholds depend on local wait times and must be adjusted for high-risk individuals.",
   "rationale":"CKD progression is modifiable with timely nephroprotective interventions; delays lead to preventable ESRD.",
   "bloom":"apply",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":140}],
   "confusable_with":""},

  {"id":"ckd-slowing-progression-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What is the current evidence base for the frequency of CKD screening in high-risk populations such as diabetes?",
   "answer":"There are no evidence-based recommendations for optimal screening frequency in at-risk populations; annual screening is standard practice in diabetes.",
   "rationale":"Early identification enables earlier intervention potentially slowing progression, even without a defined optimal interval.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":24}],
   "confusable_with":""},

  {"id":"ckd-slowing-progression-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"For which CKD stage does KDIGO recommend using validated risk equations incorporating regression or machine learning to identify high-risk individuals?",
   "answer":"For CKD G3 patients at intermediate risk, validated progression risk models should identify high-risk patients for early intervention.",
   "rationale":"Risk stratification guides intensity of monitoring and timing of interventions such as nephrology referral and treatment intensification.",
   "bloom":"apply",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":88}],
   "confusable_with":""},

  {"id":"ckd-slowing-progression-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"KDIGO recommends that laboratories automatically report validated risk equation results for which CKD stages?",
   "answer":"Laboratories should automatically report validated CKD progression risk equation results for CKD G3-G5 patients when required variables are available.",
   "rationale":"Automated reporting improves clinical workflow, decision-making, and patient understanding without additional clinician effort.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":86}],
   "confusable_with":""},

  {"id":"ckd-slowing-progression-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"A simple CKD detection algorithm shared across primary care, cardiology, and endocrinology would provide what benefit?",
   "answer":"Cross-specialty use of a simple CKD detection algorithm could significantly improve early identification and treatment of CKD given its comorbidity with cardiovascular disease and diabetes.",
   "rationale":"CKD is commonly undiagnosed at the interface of diabetes and cardiovascular care; cross-specialty screening expands early detection.",
   "bloom":"analyze",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":24}],
   "confusable_with":""},

  {"id":"ckd-slowing-progression-d8","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What is a recognized potential harm of early CKD detection that KDIGO acknowledges?",
   "answer":"Early CKD detection may cause anxiety in some patients, particularly if there is no immediately actionable intervention; psychological harm from labeling must be weighed against benefit.",
   "rationale":"Population screening programs must consider both benefits (early intervention) and harms (labeling anxiety, overdiagnosis of non-progressive disease).",
   "bloom":"analyze",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":55}],
   "confusable_with":""},
]
output.extend(kps)

# ============================================================
# ITEM 364: COPD: Advanced and Surgical Interventions
# ============================================================
topic = "COPD: Advanced and Surgical Interventions"
domain = "Internal medicine: pulmonology (COPD, asthma, pulmonary embolism, pneumonia, ILD, pleural effusion, pneumothorax, hypoxemic & hypercapnic respiratory failure, OSA)"
discipline = "medicine"

kps = [
  {"id":"copd-advanced-surgical-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What is the average additional cost per episode of postoperative pulmonary complications in COPD patients?",
   "answer":"Postoperative pulmonary complications add an average of $25,000+ per episode to healthcare costs.",
   "rationale":"PPCs substantially increase length of stay and resource use, making prevention a key perioperative goal.",
   "bloom":"recall",
   "source":[{"book":"Miller/Baby Miller","page":784}],
   "confusable_with":""},

  {"id":"copd-advanced-surgical-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Which surgical populations most consistently show benefit from prehabilitation in high-risk pulmonary patients?",
   "answer":"Colorectal, esophageal, prostate, and some orthopedic surgery patients may benefit from prehabilitation; evidence remains heterogeneous across other populations.",
   "rationale":"Prehabilitation enhances cardiopulmonary reserve and functional capacity, improving postoperative recovery in high-demand surgeries.",
   "bloom":"apply",
   "source":[{"book":"Miller/Baby Miller","page":785}],
   "confusable_with":""},

  {"id":"copd-advanced-surgical-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What bronchoscopic intervention in severe emphysema uses heat to create local fibrosis and reduce hyperinflated segments?",
   "answer":"Bronchoscopic thermal vapor ablation (BTVA), studied in the STEP-UP trial, uses segmental thermal vapor delivery to reduce lung volumes in heterogeneous emphysema.",
   "rationale":"Vapor ablation creates inflammatory fibrosis in targeted emphysematous segments, reducing hyperinflation and improving respiratory mechanics.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   GOLD 2024 COPD Full Report","page":196}],
   "confusable_with":"endobronchial valve placement (different bronchoscopic technique requiring collateral ventilation assessment)"},

  {"id":"copd-advanced-surgical-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"A patient with advanced pulmonary disease is being evaluated for lung transplant. What does a higher GAP score indicate?",
   "answer":"A higher GAP score indicates worse mortality prognosis in ILD/IPF; it is particularly valuable when evaluating patients for lung transplant referrals.",
   "rationale":"The GAP index (Gender, Age, Physiology) integrates clinical variables to predict 1-, 2-, and 3-year mortality, guiding transplant timing.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Idiopathic Pulmonary Fibrosis","page":9}],
   "confusable_with":"BODE index (COPD-specific mortality score incorporating BMI, obstruction, dyspnea, exercise)"},

  {"id":"copd-advanced-surgical-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Home noninvasive positive pressure ventilation (NPPV) in COPD patients was associated with what outcomes in a 2020 JAMA meta-analysis?",
   "answer":"Home NPPV in COPD was associated with improved clinical outcomes including reduced hospitalizations and improved survival in a 2020 JAMA systematic review and meta-analysis.",
   "rationale":"Long-term NPPV reduces hypercapnia and work of breathing in advanced COPD with daytime hypercapnia, improving outcomes beyond bronchodilators.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   GOLD 2024 COPD Full Report","page":177}],
   "confusable_with":"CPAP (used for OSA; not indicated for hypercapnic COPD)"},

  {"id":"copd-advanced-surgical-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Bullectomy in emphysema has what cardiovascular effect at rest and during exercise?",
   "answer":"Bullectomy has documented acute and chronic effects on cardiovascular function at rest and during exercise by decompressing adjacent functional lung and improving venous return.",
   "rationale":"Large bullae compress functional parenchyma and the right heart; resection allows lung re-expansion and improves hemodynamics.",
   "bloom":"analyze",
   "source":[{"book":"Society Guideline: Guideline   GOLD 2024 COPD Full Report","page":194}],
   "confusable_with":"lung volume reduction surgery (LVRS, distinct; addresses diffuse emphysema not bullae)"},

  {"id":"copd-advanced-surgical-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What does the Canadian Thoracic Society guideline specifically address regarding advanced COPD management?",
   "answer":"The Canadian Thoracic Society provides a clinical practice guideline for managing dyspnea in advanced COPD, emphasizing symptom-focused pharmacological and non-pharmacological palliative strategies.",
   "rationale":"Advanced COPD dyspnea is refractory to bronchodilators; palliative low-dose opioids and non-pharmacological strategies (fans, positioning) improve quality of life.",
   "bloom":"apply",
   "source":[{"book":"Society Guideline: Guideline   GOLD 2024 COPD Full Report","page":178}],
   "confusable_with":""},
]
output.extend(kps)

# ============================================================
# ITEM 365: Carcinoid Tumors & Neuroendocrine Tumors (NETs)
# ============================================================
topic = "Carcinoid Tumors & Neuroendocrine Tumors (NETs)"
domain = "Internal medicine: endocrinology (diabetes & inpatient glucose, DKA & HHS, thyroid disorders & storm, adrenal insufficiency, calcium disorders, pituitary)"
discipline = "medicine"

kps = [
  {"id":"carcinoid-nets-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What is the estimated incidence of carcinoid syndrome in pulmonary NETs, and what anatomical prerequisite is typically required?",
   "answer":"Carcinoid syndrome occurs in 2-12% of pulmonary NETs and typically arises only when liver metastases are present.",
   "rationale":"The liver metabolizes vasoactive mediators; hepatic metastases allow serotonin/histamine to bypass first-pass hepatic metabolism and enter systemic circulation.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Carcinoid Tumors & Neuroendocrine Tumors (NETs)","page":4}],
   "confusable_with":"primary GI NETs (carcinoid syndrome more common even without liver mets due to portal bypass)"},

  {"id":"carcinoid-nets-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Which IHC markers confirm pulmonary NET diagnosis but cannot differentiate typical from atypical carcinoid?",
   "answer":"Chromogranin A, synaptophysin, and CD56 confirm pulmonary NET; none can differentiate typical from atypical carcinoids (requires mitotic count and necrosis assessment).",
   "rationale":"Typical and atypical carcinoids differ in mitotic rate and presence of necrosis on histology, not IHC marker profile.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Carcinoid Tumors & Neuroendocrine Tumors (NETs)","page":6}],
   "confusable_with":"small cell lung cancer (high-grade neuroendocrine; also positive for these markers)"},

  {"id":"carcinoid-nets-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Which bioactive mediators released by carcinoid tumors cause flushing, diarrhea, wheezing, and right-sided valvular disease?",
   "answer":"Serotonin, histamine, chromogranin, and somatostatin; serotonin is primarily responsible for right-sided valvular disease (tricuspid, pulmonic) and diarrhea.",
   "rationale":"Serotonin induces fibrous plaques on right-sided valves; the lungs inactivate serotonin before left-sided exposure, sparing mitral/aortic valves.",
   "bloom":"analyze",
   "source":[{"book":"StatPearls: StatPearls   Carcinoid Tumors & Neuroendocrine Tumors (NETs)","page":4}],
   "confusable_with":"mastocytosis (flushing/diarrhea via histamine, no valvular disease)"},

  {"id":"carcinoid-nets-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"NCCN recommends what surveillance imaging protocol for pulmonary NETs post-resection?",
   "answer":"Close radiological surveillance with chest CT with IV contrast and multiphasic abdominal CT; independent pulmonary NET trial data are rare due to disease rarity.",
   "rationale":"Pulmonary NETs can metastasize late; surveillance imaging detects recurrence to enable salvage therapy.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Carcinoid Tumors & Neuroendocrine Tumors (NETs)","page":13}],
   "confusable_with":""},

  {"id":"carcinoid-nets-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What nuclear medicine scan uses radiolabeled octreotide to image NETs, and why does it work?",
   "answer":"Indium-111-labeled octreotide scintigraphy (OctreoScan) increases sensitivity for diagnosis, staging, and recurrence surveillance; NETs overexpress somatostatin receptors that bind octreotide.",
   "rationale":"Somatostatin receptor scintigraphy provides functional imaging of primary and metastatic NET lesions not detectable on anatomic CT.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Carcinoid Tumors & Neuroendocrine Tumors (NETs)","page":8}],
   "confusable_with":"Ga-68 DOTATATE PET/CT (more modern, higher resolution alternative)"},

  {"id":"carcinoid-nets-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What is the therapy of choice for thymic NETs and why are formal guidelines limited?",
   "answer":"Complete surgical resection with negative margins is the treatment of choice; guidelines are unavailable due to disease rarity and absence of prospective trials.",
   "rationale":"Thymic NETs are rare tumors; evidence derives mainly from case reports and series, making formal guideline development impractical.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Carcinoid Tumors & Neuroendocrine Tumors (NETs)","page":11}],
   "confusable_with":"thymoma (different cell of origin; treated differently)"},

  {"id":"carcinoid-nets-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What mTOR-directed agent is used in metastatic NETs, and at what stage does chemotherapy form the backbone of treatment?",
   "answer":"mTOR inhibitors (e.g., everolimus) are used for metastatic NETs; chemotherapy forms the backbone of stage IV metastatic NET treatment despite limited efficacy data.",
   "rationale":"The PI3K/mTOR pathway is dysregulated in NETs; everolimus reduces tumor cell proliferation by inhibiting this pathway.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Carcinoid Tumors & Neuroendocrine Tumors (NETs)","page":13}],
   "confusable_with":"somatostatin analogues (octreotide/lanreotide; different mechanism for symptom control and antiproliferation)"},
]
output.extend(kps)

script = {"_type":"illness_script","topic":topic,"discipline":discipline,
  "enabling_conditions":"Middle-aged adults; more common in women and non-Hispanic whites; hereditary syndromes (MEN1); rising incidence due to improved detection",
  "pathophysiology":"Neuroendocrine cell overproduction of vasoactive mediators (serotonin, histamine, chromogranin); hepatic metastases allow systemic mediator escape bypassing first-pass metabolism",
  "time_course":"Often indolent; pulmonary NETs may be discovered incidentally; carcinoid syndrome usually late (requires liver mets)",
  "key_features":"Flushing, diarrhea, wheezing, right-sided valvular disease; Chromogranin A/synaptophysin positive on IHC; somatostatin receptor imaging positive",
  "consequence_if_missed":"Carcinoid crisis during surgery (life-threatening vasoactive mediator surge); progressive right heart failure from valvular disease; delayed diagnosis with advanced metastatic disease"}
output.append(script)

# ============================================================
# ITEM 366: Cardiac Amyloidosis
# ============================================================
topic = "Cardiac Amyloidosis"
domain = "Internal medicine: cardiology (ACS, stable & unstable angina, heart failure, brady/tachyarrhythmias, valvular disease, hypertension & emergencies, lipids, syncope)"
discipline = "medicine"

kps = [
  {"id":"cardiac-amyloidosis-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What are the two main types of cardiac amyloidosis defined by their deposited protein?",
   "answer":"AL amyloidosis (monoclonal immunoglobulin light chains) and ATTR-CM (transthyretin amyloidosis, either wild-type or from pathogenic TTR gene variants).",
   "rationale":"Protein type determines prognosis and treatment: AL requires plasma cell-directed therapy; ATTR is treated with tafamidis or other TTR stabilizers.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   ACC AHA 2022 Heart Failure","page":69}],
   "confusable_with":"AL has worse prognosis; ATTR-CM has specific FDA-approved therapy (tafamidis)"},

  {"id":"cardiac-amyloidosis-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Why are ARNi, ACEi, ARB, and beta-blockers often poorly tolerated in ATTR-CM with EF ≤40%?",
   "answer":"Vasodilating agents exacerbate hypotension from amyloid-associated autonomic dysfunction; beta-blockers worsen HF because ATTR-CM patients rely on heart rate to maintain cardiac output due to fixed stroke volume.",
   "rationale":"Amyloid infiltration causes restrictive physiology with fixed stroke volume; rate reduction or vasodilation can precipitate hemodynamic collapse.",
   "bloom":"analyze",
   "source":[{"book":"Society Guideline: Guideline   ACC AHA 2022 Heart Failure","page":70}],
   "confusable_with":"HFrEF from other causes (standard GDMT well tolerated and mortality-reducing)"},

  {"id":"cardiac-amyloidosis-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What characteristic echocardiographic strain pattern suggests cardiac amyloidosis over other causes of LVH?",
   "answer":"Relative apical sparing on global longitudinal strain imaging is highly specific for cardiac amyloidosis; overall GLS is reduced with preserved apical strain.",
   "rationale":"Amyloid deposits preferentially affect basal and mid segments, sparing the apex, creating a distinctive bull's eye pattern on GLS maps.",
   "bloom":"apply",
   "source":[{"book":"Society Guideline: Guideline   ACC AHA 2023 Atrial Fibrillation","page":23}],
   "confusable_with":"hypertrophic cardiomyopathy (LVH but different GLS pattern; no apical sparing)"},

  {"id":"cardiac-amyloidosis-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Cardiac amyloidosis is pathophysiologically classified as what type of cardiomyopathy?",
   "answer":"Cardiac amyloidosis is a restrictive cardiomyopathy from extracellular myocardial protein deposition causing diastolic dysfunction and elevated filling pressures.",
   "rationale":"Misfolded protein fibrils displace and stiffen normal myocardium, impairing ventricular relaxation while systolic function may be preserved until late.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   ACC AHA 2022 Heart Failure","page":69}],
   "confusable_with":"cardiac sarcoidosis (granulomatous infiltration; also restrictive physiology but different treatment)"},

  {"id":"cardiac-amyloidosis-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Early detection of cardiac amyloidosis is important for what specific treatment decision?",
   "answer":"Early detection allows initiation of disease-specific therapy (tafamidis for ATTR-CM; chemotherapy/stem cell transplant for AL) before severe myocardial infiltration.",
   "rationale":"Disease-modifying therapies are more effective early; late-stage amyloidosis has limited response to treatment.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Cardiac Amyloidosis","page":2}],
   "confusable_with":""},

  {"id":"cardiac-amyloidosis-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What does family history assessment add to the workup of a new HF presentation?",
   "answer":"Family history identifies possible inherited cardiomyopathy (including familial ATTR amyloidosis or genetic DCM); conditions requiring disease-specific therapy like amyloid heart disease need targeted evaluation.",
   "rationale":"Genetic cardiomyopathies require specific testing (TTR gene sequencing for familial ATTR) and family member screening.",
   "bloom":"apply",
   "source":[{"book":"Society Guideline: Guideline   ACC AHA 2022 Heart Failure","page":18}],
   "confusable_with":""},

  {"id":"cardiac-amyloidosis-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Hereditary renal amyloidosis (e.g., fibrinogen A alpha-chain type) can benefit from what transplant strategy, with what limitation?",
   "answer":"Combined liver and renal transplantation benefits hereditary renal amyloidosis; liver transplant stops amyloidogenic protein production but does not affect ocular or cardiac manifestations.",
   "rationale":"The mutant amyloidogenic protein is produced in the liver; liver replacement halts new deposition, stabilizing renal disease but not already-affected non-hepatic organs.",
   "bloom":"analyze",
   "source":[{"book":"StatPearls","page":8}],
   "confusable_with":"ATTR-CM (tafamidis preferred for cardiac ATTR; transplant reserved for select cases)"},
]
output.extend(kps)

script2 = {"_type":"illness_script","topic":topic,"discipline":discipline,
  "enabling_conditions":"Age >60 (wild-type ATTR in older men); AL in plasma cell dyscrasias; hereditary ATTR from Val30Met or other TTR variants; carpal tunnel syndrome, biceps tendon rupture as early clues",
  "pathophysiology":"Misfolded protein fibrils deposit in myocardial extracellular space causing restrictive cardiomyopathy; autonomic neuropathy common; ECG shows low voltage despite thick walls",
  "time_course":"Insidious; median survival without therapy ~2-4 years for AL; wild-type ATTR slower (5+ years); tafamidis shown to reduce mortality in ATTR",
  "key_features":"Restrictive cardiomyopathy, LVH without HTN history, low ECG voltage, apical sparing GLS, bilateral CTS, neuropathy, intolerance of standard HF meds",
  "consequence_if_missed":"Progressive refractory HF; fatal arrhythmias; missed window for tafamidis or chemotherapy; ATTR-CM increasingly identified as cause of HFpEF"}
output.append(script2)

# ============================================================
# ITEM 367: Cardiovascular Risk in Systemic and Inflammatory Diseases
# ============================================================
topic = "Cardiovascular Risk in Systemic and Inflammatory Diseases"
domain = "Internal medicine: cardiology (ACS, stable & unstable angina, heart failure, brady/tachyarrhythmias, valvular disease, hypertension & emergencies, lipids, syncope)"
discipline = "medicine"

kps = [
  {"id":"cv-risk-inflammatory-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Which conditions are recognized as ASCVD risk-enhancing factors warranting intensified statin therapy in borderline-risk patients?",
   "answer":"CKD, chronic inflammatory diseases (RA, psoriasis, lupus), HIV, South Asian ethnicity, metabolic syndrome, and premature menopause (<40y) are ASCVD risk-enhancing factors.",
   "rationale":"Chronic inflammation accelerates atherosclerosis through endothelial dysfunction, plaque instability, and dyslipidemia independent of traditional Framingham risk factors.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":218}],
   "confusable_with":"high-risk primary prevention (requires statin without additional risk enhancers)"},

  {"id":"cv-risk-inflammatory-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Hyperglycemia contributes to cardiovascular risk through which specific mechanisms?",
   "answer":"Hyperglycemia causes decreased immune function, increased oxidative stress, endothelial dysfunction, procoagulant state, inflammatory cytokines, and fluid/electrolyte shifts.",
   "rationale":"Advanced glycation end-products and reactive oxygen species from hyperglycemia accelerate atherosclerosis and microvascular disease.",
   "bloom":"analyze",
   "source":[{"book":"Miller/Baby Miller","page":547}],
   "confusable_with":""},

  {"id":"cv-risk-inflammatory-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Which systemic conditions commonly produce marked diastolic dysfunction seen on Doppler echocardiography?",
   "answer":"Systemic hypertension and coronary artery disease are common causes of marked diastolic dysfunction.",
   "rationale":"Chronic pressure overload and ischemia cause myocardial hypertrophy and fibrosis, impairing diastolic relaxation and raising filling pressures.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1499}],
   "confusable_with":"restrictive cardiomyopathy (infiltrative disease; different pathology)"},

  {"id":"cv-risk-inflammatory-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"A patient with HIV on lopinavir-ritonavir needs a statin. What dose modification applies to rosuvastatin?",
   "answer":"Rosuvastatin levels increase 5- to 7-fold with lopinavir-ritonavir; start at a low dose (5-10 mg) to avoid myopathy.",
   "rationale":"Protease inhibitors inhibit OATP1B1/OATP1B3 transporters, dramatically increasing statin plasma exposure and rhabdomyolysis risk.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Osteoporosis  screening, diagnosis & treatment","page":20}],
   "confusable_with":"atorvastatin-PI interaction (doubles atorvastatin; less extreme than rosuvastatin)"},

  {"id":"cv-risk-inflammatory-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"In older adults, which cardiovascular diseases most prominently drive morbidity, mortality, and cost?",
   "answer":"Heart failure, stroke, arrhythmias, hypertension, and frailty are the leading cardiovascular contributors to morbidity, mortality, and increased cost of care in older adults.",
   "rationale":"Age-related arterial stiffening, reduced cardiac reserve, and lifelong atherosclerotic exposure converge to make cardiovascular disease the dominant geriatric killer.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1499}],
   "confusable_with":""},

  {"id":"cv-risk-inflammatory-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Patients with carotid stenosis have greatly increased risk of what other vascular disease?",
   "answer":"Patients with carotid stenosis almost universally have coexisting coronary artery disease and peripheral arterial disease; atherosclerosis is a systemic disease.",
   "rationale":"Shared risk factors (hypertension, hyperlipidemia, diabetes, smoking) produce concurrent atherosclerosis in multiple vascular beds.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":960}],
   "confusable_with":""},

  {"id":"cv-risk-inflammatory-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Low socioeconomic status is associated with what respiratory and cardiovascular risks?",
   "answer":"Low SES is consistently associated with airflow obstruction, COPD, and likely higher cardiovascular risk through greater environmental exposures and reduced healthcare access.",
   "rationale":"Social determinants drive both inflammatory burden and access to preventive care, amplifying cardiovascular risk in low-SES populations.",
   "bloom":"analyze",
   "source":[{"book":"Society Guideline: Guideline   GOLD 2024 COPD Full Report","page":27}],
   "confusable_with":""},
]
output.extend(kps)

# ============================================================
# ITEM 368: Chemotherapy toxicities and monitoring (HIPEC/CRS-focused chunks)
# ============================================================
topic = "Chemotherapy toxicities and monitoring"
domain = "Internal medicine: hematology & oncology (anemias, anticoagulation & reversal, VTE prophylaxis & treatment, thrombocytopenia & DIC, transfusion medicine, oncologic emergencies, neutropenic fever)"
discipline = "medicine"

kps = [
  {"id":"chemo-toxicities-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"In epithelioid peritoneal mesothelioma, what peritoneal cancer index cutoff is associated with optimal CRS-HIPEC candidacy and what survival is achievable?",
   "answer":"Peritoneal cancer index <17 with epithelioid histology and unicavitary disease is associated with 5-year survival rates of 50-60% after CRS-HIPEC.",
   "rationale":"Higher PCI correlates with incomplete cytoreduction, which dramatically worsens outcomes; CC-0/CC-1 completeness drives survival benefit.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Chemotherapy toxicities and monitoring","page":6}],
   "confusable_with":"colorectal peritoneal carcinomatosis (PCI cutoff typically <20 for optimal candidate)"},

  {"id":"chemo-toxicities-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What hemostatic techniques are used intraoperatively during CRS-HIPEC to control bleeding on large peritonectomy surfaces?",
   "answer":"Argon beam coagulation provides superficial tissue destruction for hemostasis on raw peritonectomy surfaces; careful tissue plane dissection minimizes blood loss.",
   "rationale":"Extensive peritonectomy creates large raw surfaces requiring reliable hemostasis to prevent transfusion requirements and coagulopathy.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Chemotherapy toxicities and monitoring","page":11}],
   "confusable_with":""},

  {"id":"chemo-toxicities-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What prehabilitation targets are most critical before CRS-HIPEC?",
   "answer":"Nutritional optimization (poor nutrition worsens outcomes) and functional capacity enhancement are key modifiable prehabilitation targets before CRS-HIPEC.",
   "rationale":"CRS-HIPEC is a major cytoreductive procedure with high morbidity; preoperative nutritional and functional status significantly influence postoperative recovery.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Chemotherapy toxicities and monitoring","page":8}],
   "confusable_with":""},

  {"id":"chemo-toxicities-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Left upper quadrant peritonectomy during CRS addresses which structures, and when is splenectomy required?",
   "answer":"Left upper quadrant peritonectomy addresses the left hemidiaphragm, splenic hilum, and greater curvature of the stomach; splenectomy is required when tumor involves the splenic hilum or capsule.",
   "rationale":"The left upper quadrant is a common site of peritoneal implants in GI/gynecologic cancers; complete resection there often requires en bloc splenectomy.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Chemotherapy toxicities and monitoring","page":10}],
   "confusable_with":""},

  {"id":"chemo-toxicities-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What apparatus components are required to perform HIPEC after cytoreduction?",
   "answer":"HIPEC requires temperature probes (extracorporeal circuit and peritoneal cavity), a roller pump, a cytotoxic agent reservoir, a heat exchanger, and a computer-regulated system with a timer.",
   "rationale":"Precise temperature control (41-43 degrees C) is critical; hyperthermia enhances cytotoxic drug penetration through increased cell membrane permeability and heat-induced protein denaturation.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Chemotherapy toxicities and monitoring","page":7}],
   "confusable_with":""},

  {"id":"chemo-toxicities-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What multidisciplinary team is essential for CRS-HIPEC patient management?",
   "answer":"Pathologists, radiologists, oncologists, anesthesiologists, nurses, and pharmacists are essential interprofessional team members for comprehensive CRS-HIPEC care.",
   "rationale":"Complex oncologic surgery requires coordinated expertise from patient selection through perioperative management and long-term surveillance.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Chemotherapy toxicities and monitoring","page":14}],
   "confusable_with":""},

  {"id":"chemo-toxicities-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Peritoneal surface malignancies arise through what route, and what histological transformation increases tumor spread?",
   "answer":"Peritoneal malignancies arise primarily from the peritoneum or through direct spread from GI and gynecologic malignancies; epithelial-to-mesenchymal transition increases cell motility and resistance to anoikis.",
   "rationale":"EMT allows cancer cells to detach from primary tumors, survive in the peritoneal fluid, and implant on mesothelial surfaces.",
   "bloom":"analyze",
   "source":[{"book":"StatPearls: StatPearls   Chemotherapy toxicities and monitoring","page":5}],
   "confusable_with":""},
]
output.extend(kps)

# ============================================================
# ITEM 369: Chronic Pancreatitis
# ============================================================
topic = "Chronic Pancreatitis"
domain = "Internal medicine: gastroenterology & hepatology (upper & lower GI bleed, acute liver failure, cirrhosis & its complications, pancreatitis, IBD, bowel obstruction, hepatic encephalopathy)"
discipline = "medicine"

kps = [
  {"id":"chronic-pancreatitis-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What proportion of chronic heavy drinkers develop pancreatitis, and what are the leading etiologies by sex?",
   "answer":"Fewer than 5% of chronic heavy drinkers develop pancreatitis; gallstones are #1 in females, alcohol #1 in males, hypertriglyceridemia (TG>1000) is #3.",
   "rationale":"Additional cofactors (genetic, dietary, environmental) beyond alcohol are required for acinar cell damage to exceed repair mechanisms.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Acute Pancreatitis","page":4}],
   "confusable_with":""},

  {"id":"chronic-pancreatitis-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Which genetic mutations are associated with early-onset or recurrent pancreatitis and when should genetic testing be considered?",
   "answer":"PRSS1 (hereditary pancreatitis), CFTR (cystic fibrosis), and alpha-1 antitrypsin deficiency; consider testing in patients <30 with recurrent or idiopathic pancreatitis plus positive family history.",
   "rationale":"These variants impair protective mechanisms against premature trypsinogen activation or alter ductal secretion, predisposing to repeated acinar injury.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Acute Pancreatitis","page":5}],
   "confusable_with":"autoimmune pancreatitis (responds to steroids; IgG4 elevation; different pathogenesis)"},

  {"id":"chronic-pancreatitis-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What triglyceride level should raise suspicion for hypertriglyceridemia-induced pancreatitis?",
   "answer":"Suspect hypertriglyceridemia-induced pancreatitis when triglycerides exceed 1000 mg/dL; it is the third most common cause (~10%) after gallstones and alcohol.",
   "rationale":"Massive hypertriglyceridemia generates toxic free fatty acids via pancreatic lipase hydrolysis, causing acinar cell membrane disruption.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":85}],
   "confusable_with":""},

  {"id":"chronic-pancreatitis-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What is the incidence of post-ERCP pancreatitis and what prophylactic medication reduces this risk?",
   "answer":"Post-ERCP pancreatitis occurs in approximately 4.5% of procedures; rectal NSAIDs (indomethacin or diclofenac) reduce this risk.",
   "rationale":"Rectal NSAIDs inhibit phospholipase A2 and prostaglandin-mediated inflammation triggered by ERCP-related pancreatic duct manipulation.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":85}],
   "confusable_with":""},

  {"id":"chronic-pancreatitis-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What oxidative and nonoxidative pathways mediate alcohol-induced acinar cell injury?",
   "answer":"Oxidative: acetaldehyde accumulation and NAD redox disruption; nonoxidative: fatty acid ethyl ester formation in mitochondria, triggering premature zymogen activation.",
   "rationale":"Both pathways converge on acinar cell injury, but additional susceptibility factors determine which individuals develop pancreatitis.",
   "bloom":"analyze",
   "source":[{"book":"StatPearls: StatPearls   Acute Pancreatitis","page":4}],
   "confusable_with":""},

  {"id":"chronic-pancreatitis-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Chronic pancreatitis is listed in which differential diagnoses in the MGH manual?",
   "answer":"Chronic pancreatitis appears in the differential for chronic abdominal pain and for causes of dyspepsia (along with biliary disease, gastric cancer, celiac, IBD, and drug-induced).",
   "rationale":"Chronic pancreatitis produces persistent visceral pain, malabsorption, and exocrine/endocrine insufficiency that overlap with multiple GI disorders.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":72}],
   "confusable_with":"IBS (functional; no structural pathology)"},

  {"id":"chronic-pancreatitis-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What mechanism explains neuropathic pain in chronic pancreatitis as distinct from acute nociceptive pain?",
   "answer":"Neuropathic pain in chronic pancreatitis results from injury to peripheral or central neural structures, producing central sensitization; it is largely independent of ongoing acute inflammation.",
   "rationale":"Pancreatic neural remodeling (perineural inflammation, neuroplasticity) drives chronic pain that persists even after pain triggers are removed.",
   "bloom":"analyze",
   "source":[{"book":"Morgan & Mikhail","page":1708}],
   "confusable_with":"nociceptive visceral pain (responds better to analgesics; less central sensitization)"},
]
output.extend(kps)

# ============================================================
# ITEM 370: Colorectal Cancer Screening & Surveillance
# ============================================================
topic = "Colorectal Cancer Screening & Surveillance"
domain = "Internal medicine: gastroenterology & hepatology (upper & lower GI bleed, acute liver failure, cirrhosis & its complications, pancreatitis, IBD, bowel obstruction, hepatic encephalopathy)"
discipline = "medicine"

kps = [
  {"id":"crc-screening-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"At what age do ACS and ACG recommend beginning CRC screening for average-risk individuals, and how does USPSTF differ?",
   "answer":"ACS and ACG recommend starting at age 45; USPSTF recommends starting at age 50.",
   "rationale":"ACS and ACG lowered the age to 45 based on rising CRC incidence in younger adults and modeling showing mortality benefit.",
   "bloom":"recall",
   "source":[{"book":"Intern Notes / Survival Guide","page":40}],
   "confusable_with":"USPSTF age 50 vs ACS/ACG age 45"},

  {"id":"crc-screening-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"How does FIT compare to guaiac FOBT in sensitivity and specificity for CRC screening?",
   "answer":"FIT has sensitivity 79% and specificity 94%, both higher than guaiac FOBT; results reported in micrograms of hemoglobin per gram of feces.",
   "rationale":"FIT uses antibodies specific to human hemoglobin, eliminating dietary restrictions and improving specificity compared to guaiac-based testing.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Colorectal Cancer Screening & Surveillance","page":4}],
   "confusable_with":"guaiac FOBT (lower sensitivity/specificity; requires dietary restriction)"},

  {"id":"crc-screening-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What post-treatment CRC surveillance protocol is recommended for CEA, CT, and colonoscopy?",
   "answer":"CEA every 6 months for 3 years; CT at 1 and 2 years; colonoscopy at 1 and 3 years after curative CRC resection.",
   "rationale":"CEA elevation precedes clinical/radiological recurrence by weeks to months, enabling early detection of resectable recurrences.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Colorectal Cancer Screening & Surveillance","page":5}],
   "confusable_with":""},

  {"id":"crc-screening-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What proportions of CRC cases are attributable to hereditary syndromes vs IBD?",
   "answer":"Hereditary syndromes (HNPCC/Lynch, FAP) account for 5-10% of CRC; chronic IBD accounts for approximately 1% of CRC cases.",
   "rationale":"Lynch syndrome (mismatch repair deficiency) and FAP (APC mutation) are the most common hereditary CRC syndromes requiring enhanced surveillance.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Colorectal Cancer Screening & Surveillance","page":5}],
   "confusable_with":""},

  {"id":"crc-screening-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What is the current role of barium enema in CRC screening?",
   "answer":"Barium enemas were historically the preferred radiologic screening modality for CRC but are now infrequently used in current clinical practice.",
   "rationale":"CT colonography and colonoscopy have superior sensitivity and specificity, replacing barium enema for CRC screening.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Colorectal Cancer Screening & Surveillance","page":7}],
   "confusable_with":"CT colonography/virtual colonoscopy (different modality with better performance)"},

  {"id":"crc-screening-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"After detection of a suspicious lesion by flexible sigmoidoscopy, what is the recommended next step?",
   "answer":"A follow-up colonoscopy is typically recommended for biopsy confirmation and treatment after a suspicious lesion is found on flexible sigmoidoscopy.",
   "rationale":"Flexible sigmoidoscopy covers only the distal colon; full colonoscopy detects synchronous proximal lesions and enables therapeutic polypectomy.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Colorectal Cancer Screening & Surveillance","page":7}],
   "confusable_with":""},

  {"id":"crc-screening-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Under what circumstances is CRC screening inadvisable despite guidelines recommending it?",
   "answer":"Screening may be inadvisable in terminal illness, severe comorbidities limiting life expectancy, or patient refusal; individuals have the right to decline screening.",
   "rationale":"In patients with limited life expectancy, procedural risks and costs of screening exceed the potential survival benefit.",
   "bloom":"analyze",
   "source":[{"book":"StatPearls: StatPearls   Colorectal Cancer Screening & Surveillance","page":6}],
   "confusable_with":""},
]
output.extend(kps)

# Save partial output
with open('data/kp_redeep_part11a_partial.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Part A done: {len(output)} items written to partial file")
