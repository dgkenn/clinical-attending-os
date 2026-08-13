"""Author KPs for topics 111-121 (slice items 12-22)."""
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

kps = []

# ── 111: CKD: Complications — Cardiovascular and Metabolic ───────────────────
T = "CKD: Complications — Cardiovascular and Metabolic"
DOM = "Internal medicine: nephrology, fluids & electrolytes"
DISC = "medicine"

kps += [
  {"id":"ckd-cv-metabolic-d1","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Finerenone is a non-steroidal mineralocorticoid receptor antagonist used in CKD + type 2 diabetes. What are its two primary demonstrated benefits?",
   "answer":"Finerenone reduces chronic kidney disease outcomes (progression) and reduces cardiovascular events in patients with CKD and type 2 diabetes.",
   "rationale":"Mineralocorticoid receptor overactivation drives fibrosis in the kidney and vessels; finerenone selectively blocks this without the sex-hormone side effects of spironolactone.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":191}],
   "confusable_with":"spironolactone (steroidal, more side effects)"},

  {"id":"ckd-cv-metabolic-d2","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"In CKD patients with type 2 diabetes, which GLP-1 receptor agonists do NOT require dose adjustment for kidney function?",
   "answer":"Liraglutide, semaglutide (injectable), and dulaglutide provide cardiovascular benefit and do not require dose adjustment in CKD.",
   "rationale":"These GLP-1 RAs are metabolically cleared (not renally excreted unchanged) and demonstrated cardiovascular outcome benefits in dedicated CKD/diabetes trials, making them preferred agents.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":107}],
   "confusable_with":"exenatide (renally cleared, requires dose adjustment)"},

  {"id":"ckd-cv-metabolic-d3","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What metabolic acidosis treatment is recommended for CKD patients with pH <7.2 based on the BICAR-ICU trial?",
   "answer":"IV sodium bicarbonate targeting pH >7.3 reduces need for RRT initiation; a subset with AKIN stages 2-3 showed improved 28-day mortality — but treatment begins AFTER addressing the underlying cause.",
   "rationale":"Metabolic acidosis in CKD accelerates catabolism, worsens bone disease, and impairs cardiac function; bicarbonate supplementation is a treatment target in both CKD and critical illness.",
   "bloom":"apply",
   "source":[{"book":"MGH Housestaff Manual","page":106}],
   "confusable_with":"DKA management (bicarbonate NOT given even in acidosis)"},

  {"id":"ckd-cv-metabolic-d4","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"A patient with alcoholic ketoacidosis has an anion-gap metabolic acidosis. What is the treatment sequence and what specific nutritional supplement is essential?",
   "answer":"Volume restoration and thiamine supplementation are essential first; potassium repletion; euglycemia must be achieved before considering bicarbonate (which is not first-line).",
   "rationale":"Thiamine is required for glucose metabolism; giving dextrose without thiamine precipitates Wernicke's encephalopathy; euglycemia closes the anion gap without bicarbonate.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Metabolic Acidosis  Approach and Anion Gap","page":11}],
   "confusable_with":"DKA (also treated without bicarbonate typically)"},

  {"id":"ckd-cv-metabolic-d5","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Low-protein diets in CKD constrict what anatomical structure to reduce intraglomerular pressure?",
   "answer":"Low-protein intake constricts the glomerular afferent arterioles, lowering intraglomerular pressure and reducing hyperfiltration.",
   "rationale":"Dietary amino acids (especially those from animal protein) stimulate afferent arteriolar dilation as part of tubuloglomerular feedback; reducing protein intake decreases this stimulus.",
   "bloom":"analyze",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":94}],
   "confusable_with":""},

  {"id":"ckd-cv-metabolic-d6","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What team-based care components does KDIGO 2024 recommend for patients approaching kidney failure?",
   "answer":"Multidisciplinary team including dietary counseling, medication management, education about KRT modalities, transplant options, dialysis access surgery planning, and ethical/psychological/social care.",
   "rationale":"CKD preparation for kidney replacement therapy (KRT) requires early, coordinated, patient-centered planning to optimize outcomes and ensure informed decision-making about modality choice.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":146}],
   "confusable_with":""},

  {"id":"ckd-cv-metabolic-d7","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What cardiovascular risk does PCSK9 inhibitor evolocumab provide in CKD patients with and without diabetes?",
   "answer":"Evolocumab (PCSK9 inhibitor) provides cardiovascular safety and efficacy in CKD patients regardless of diabetes status; it does not increase the risk of new-onset diabetes.",
   "rationale":"PCSK9 inhibitors lower LDL-C by upregulating hepatic LDL receptor expression; the cardiovascular benefit is maintained and glycaemic neutrality confirmed in the FOURIER trial subanalysis.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":194}],
   "confusable_with":"statins (slight increase in new-onset diabetes risk)"},
]

# ── 112: CKD: Definition, Staging, and Progression ───────────────────────────
T = "CKD: Definition, Staging, and Progression"
DOM = "Internal medicine: nephrology, fluids & electrolytes"
DISC = "medicine"

kps += [
  {"id":"ckd-staging-d1","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"How is CKD defined, and what minimum duration of abnormality is required?",
   "answer":"CKD is defined as abnormalities of kidney structure or function present for a minimum of 3 months with implications for health; classified by Cause, GFR category (G1-G5), and Albuminuria category (A1-A3) — the CGA system.",
   "rationale":"The 3-month criterion distinguishes CKD from acute kidney injury; the CGA classification captures causative diagnosis and both functional (GFR) and structural (albuminuria) dimensions for prognosis.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":22}],
   "confusable_with":"AKI (acute, <3 months)"},

  {"id":"ckd-staging-d2","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"The 2021 CKD-EPI equation removed race. What is the current standard definition of CKD by GFR and albuminuria thresholds?",
   "answer":"GFR <60 mL/min OR kidney damage (albuminuria ≥30 mg/day) for ≥3 months; 2021 CKD-EPI equation used for GFR estimation (race omitted).",
   "rationale":"Two parallel pathways define CKD: reduced filtration function (eGFR-based) or evidence of structural damage (albuminuria); either alone for ≥3 months meets the diagnostic threshold.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":102}],
   "confusable_with":""},

  {"id":"ckd-staging-d3","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"On repeat testing of albuminuria, what change is considered to exceed expected biological variability and warrant formal evaluation?",
   "answer":"A doubling of albuminuria or more (≥100% increase) exceeds the expected variability (95% CI ~50% on repeat testing) and warrants evaluation if replicated.",
   "rationale":"Single albuminuria measurements have high intraindividual variability due to hydration, exercise, and infection; only sustained large increases represent true disease progression.",
   "bloom":"apply",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":83}],
   "confusable_with":""},

  {"id":"ckd-staging-d4","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What are the most highly evaluated clinical endpoints in CKD epidemiological studies that drive prognosis?",
   "answer":"All-cause mortality, cardiovascular mortality, kidney failure (requiring KRT), and AKI episodes — assessed in the CKD Prognosis Consortium across large multinational studies.",
   "rationale":"Both lower eGFR and higher albuminuria independently and additively increase risk of all these outcomes; the CGA classification was developed to capture these risk dimensions.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":29}],
   "confusable_with":""},

  {"id":"ckd-staging-d5","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"KDIGO 2024 guidance notes that integration of a simple CKD algorithm into primary care, cardiology, and endocrinology practice could achieve what important goal?",
   "answer":"Significantly improve early identification and treatment of CKD — most CKD is silent and detectable only with laboratory testing (eGFR + ACR).",
   "rationale":"The majority of CKD patients are undiagnosed; early detection in high-risk populations (diabetes, hypertension) enables timely initiation of nephroprotective therapy before significant loss of function.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":24}],
   "confusable_with":""},

  {"id":"ckd-staging-d6","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What three standardized educational topics are considered essential for patients with CKD approaching kidney failure?",
   "answer":"(1) Knowledge about CKD; (2) knowledge about treatment to slow progression and complications; (3) knowledge about kidney failure management options including KRT modalities.",
   "rationale":"Informed patients make better decisions about dialysis modality, transplant evaluation, and conservative management; early education reduces emergency dialysis starts and improves outcomes.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":148}],
   "confusable_with":""},

  {"id":"ckd-staging-d7","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Serum creatinine as a GFR surrogate has a critical limitation in dynamic states. What does a rise in creatinine by >1 mg/dL per day imply about GFR?",
   "answer":"One must assume GFR <10 mL/min when creatinine rises >1 mg/dL/day, because creatinine approximates GFR only at steady state — acute creatinine rise underestimates true GFR loss.",
   "rationale":"In AKI, creatinine accumulates because GFR has fallen abruptly; the measured creatinine at any given moment reflects a lagged average GFR, not the current GFR, making GFR estimation unreliable.",
   "bloom":"analyze",
   "source":[{"book":"MGH Housestaff Manual","page":99}],
   "confusable_with":""},
]

# ── 113: CKD: Etiology and Workup ─────────────────────────────────────────────
T = "CKD: Etiology and Workup"
DOM = "Internal medicine: nephrology, fluids & electrolytes"
DISC = "medicine"

kps += [
  {"id":"ckd-etiology-d1","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What are the most common causes of chronic kidney disease in the United States?",
   "answer":"Hypertensive nephrosclerosis, diabetic nephropathy, chronic glomerulonephritis, and polycystic kidney disease — in decreasing order of frequency.",
   "rationale":"Diabetes and hypertension together account for >70% of new ESRD cases; targeting modifiable risk factors in these conditions is the most impactful intervention for CKD prevention.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1107}],
   "confusable_with":""},

  {"id":"ckd-etiology-d2","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What drugs elevate serum creatinine without changing GFR, and why does this matter for CKD workup?",
   "answer":"Trimethoprim (in Bactrim), H2 blockers (cimetidine), and dronedarone impair tubular creatinine secretion, raising serum Cr without reducing GFR — BUN remains stable in these cases.",
   "rationale":"Recognizing drug-induced creatinine elevation prevents inappropriate CKD labeling and workup; the stable BUN distinguishes this from true GFR impairment where BUN also rises.",
   "bloom":"apply",
   "source":[{"book":"MGH Housestaff Manual","page":99}],
   "confusable_with":"true AKI"},

  {"id":"ckd-etiology-d3","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"The cause of CKD should be classified as part of the CGA system. What two markers are used to detect kidney damage even before GFR falls below 60?",
   "answer":"Decreased GFR and increased albuminuria (or other markers of kidney damage including hematuria, imaging abnormalities, or pathological changes on biopsy) are both detection markers.",
   "rationale":"Albuminuria reflects glomerular basement membrane damage and occurs early in diabetic nephropathy before eGFR declines; identifying it early enables nephroprotective treatment initiation.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":54}],
   "confusable_with":""},

  {"id":"ckd-etiology-d4","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"In CKD etiology workup, why is a high protein diet (>1.3 g/kg/day) specifically contraindicated in patients at risk of progression?",
   "answer":"High protein intake increases intraglomerular pressure via afferent arteriolar dilation and increases uremic toxin generation, accelerating CKD progression.",
   "rationale":"Dietary protein load is directly sensed by the kidney; the resulting hyperfiltration and increased uremic toxin burden are two independent mechanisms of nephron loss.",
   "bloom":"analyze",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":93}],
   "confusable_with":""},

  {"id":"ckd-etiology-d5","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"BUN out of proportion to creatinine (BUN:Cr >20) suggests which category of azotemia and what common causes?",
   "answer":"Prerenal azotemia (or upper GI bleeding causing urea absorption) — common causes include volume depletion, heart failure, hepatorenal syndrome, or high-protein diet/catabolic state.",
   "rationale":"In prerenal states, tubular urea reabsorption increases as tubular flow slows; creatinine is not reabsorbed, so the BUN:Cr ratio rises disproportionately.",
   "bloom":"apply",
   "source":[{"book":"MGH Housestaff Manual","page":99}],
   "confusable_with":"intrinsic renal azotemia (BUN:Cr ~10-15)"},

  {"id":"ckd-etiology-d6","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Obesity is linked to CKD progression. What mechanism connects adiposity to glomerular injury?",
   "answer":"Obesity-related CKD involves glomerular hyperfiltration from increased metabolic demand, adipokine-mediated inflammation, insulin resistance, and hypertension — all driving glomerulosclerosis.",
   "rationale":"Obese kidneys undergo compensatory hyperfiltration to meet excess metabolic needs; sustained glomerular hypertension causes focal segmental glomerulosclerosis (FSGS) even without diabetes.",
   "bloom":"analyze",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":189}],
   "confusable_with":""},

  {"id":"ckd-etiology-d7","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What acid-base consequence of severe CKD must be treated, and what subset of ICU patients in the BICAR-ICU trial derived the greatest mortality benefit from IV bicarbonate?",
   "answer":"Chronic metabolic acidosis; ICU patients with AKIN stages 2-3 (severe AKI) had improved 28-day mortality with IV bicarbonate targeting pH >7.3.",
   "rationale":"Severe acidosis impairs myocardial function, hepatic drug metabolism, and immune response; correcting acidosis in AKI patients prevents RRT initiation and reduces mortality in the most severe cases.",
   "bloom":"apply",
   "source":[{"book":"MGH Housestaff Manual","page":106}],
   "confusable_with":""},
]

# ── 114: COPD: Diagnosis and Classification ────────────────────────────────────
T = "COPD: Diagnosis and Classification"
DOM = "Internal medicine: pulmonology (COPD, asthma, pulmonary embolism, pneumonia, ILD, pleural effusion, pneumothorax, hypoxemic & hypercapnic respiratory failure, OSA)"
DISC = "medicine"

kps += [
  {"id":"copd-diagnosis-d1","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"How is COPD currently defined and what distinguishes it from asthma on spirometry?",
   "answer":"COPD is characterized by airflow limitation that is NOT fully reversible (post-bronchodilator FEV1/FVC <0.70); strongly associated with cigarette smoking; asthma has reversible obstruction.",
   "rationale":"The GOLD definition requires persistent post-bronchodilator obstruction; in contrast, asthma's airflow limitation improves ≥12% and ≥200 mL with bronchodilator, distinguishing the two entities.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":869}],
   "confusable_with":"asthma (reversible), cardiac dyspnea"},

  {"id":"copd-diagnosis-d2","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Wheezing with exercise is one symptom that may prompt COPD vs. asthma evaluation. What COPD-related pulmonary symptom requires supplemental oxygen when PaO2 falls below what threshold?",
   "answer":"Supplemental oxygen is indicated when PaO2 <60 mmHg (8 kPa) or SpO2 <90% in adults, children, and infants (>1 month) breathing room air.",
   "rationale":"Chronic hypoxemia causes secondary pulmonary hypertension and cor pulmonale; long-term oxygen therapy (LTOT) is the only pharmacological treatment proven to improve survival in COPD with resting hypoxemia.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":2166}],
   "confusable_with":""},

  {"id":"copd-diagnosis-d3","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"COPD is the most common pulmonary disorder in adult anesthetic practice. What is its principal demographic association?",
   "answer":"COPD strongly associates with cigarette smoking and has a male predominance; prevalence increases with age.",
   "rationale":"Cigarette smoke causes both emphysematous airspace destruction (via elastase/anti-elastase imbalance) and chronic bronchitis (via mucus gland hyperplasia); the combined defect creates irreversible obstruction.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":869}],
   "confusable_with":""},

  {"id":"copd-diagnosis-d4","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Alpha-1 antitrypsin deficiency causes a specific COPD subtype. What treatment is available for severe AAT deficiency-associated emphysema?",
   "answer":"Alpha-1 proteinase inhibitor (augmentation therapy) — demonstrated long-term efficacy and safety in the RAPID-OLE extension trial for patients with severe AAT deficiency emphysema.",
   "rationale":"AAT deficiency causes panacinar emphysema predominantly in the lower lobes from unopposed neutrophil elastase activity; replacement therapy reduces the rate of lung density decline.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   GOLD 2024 COPD Full Report","page":189}],
   "confusable_with":""},

  {"id":"copd-diagnosis-d5","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"An anesthesiologist is managing an intubated COPD patient with suspected bronchospasm during anesthesia. What clinical monitors indicate worsening obstruction?",
   "answer":"Sudden acute rise in peak inspiratory pressures, changes in end-tidal CO2 waveform (prolonged expiratory phase, rising plateau), and decreasing oxygen saturation indicate worsening obstruction.",
   "rationale":"Bronchospasm under anesthesia increases dynamic lung resistance, elevating peak airway pressures; ETCO2 waveform develops a shark-fin shape with sloped alveolar plateau reflecting delayed gas mixing.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Asthma  Chronic Management","page":3}],
   "confusable_with":"pneumothorax (also raises peak pressures but has other features)"},

  {"id":"copd-diagnosis-d6","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What is the prevention strategy that has most conclusively been shown to reduce COPD-related perioperative complications?",
   "answer":"Smoking cessation before surgery, optimization of bronchodilators, treatment of respiratory infections, and physical conditioning; patients with FEV1 <50% predicted require particularly careful pre-operative assessment.",
   "rationale":"Smoking cessation reduces airway reactivity and secretion production; the benefits on mucociliary clearance begin within days-weeks, reducing post-operative pulmonary complications.",
   "bloom":"apply",
   "source":[{"book":"Miller/Baby Miller","page":784}],
   "confusable_with":""},

  {"id":"copd-diagnosis-d7","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Should COPD diagnosis be based on a single spirometry test? What does evidence suggest?",
   "answer":"Evidence suggests COPD diagnosis should NOT be based on a single spirometry test alone — confirmatory testing, clinical context, and repeat spirometry are recommended to avoid over- or under-diagnosis.",
   "rationale":"A single post-bronchodilator FEV1/FVC <0.70 has variable sensitivity depending on age and technique; older patients may have physiological age-related FEV1 decline misclassified as COPD.",
   "bloom":"analyze",
   "source":[{"book":"Society Guideline: Guideline   GOLD 2024 COPD Full Report","page":165}],
   "confusable_with":""},
]

kps.append({"_type":"illness_script","topic":T,"discipline":DISC,
  "enabling_conditions":"Smoking (primary), occupational dust/fumes, alpha-1 antitrypsin deficiency, biomass fuel exposure, recurrent childhood respiratory infections",
  "pathophysiology":"Airway inflammation → mucus hypersecretion (chronic bronchitis) + emphysematous airspace destruction → irreversible airflow limitation + air trapping",
  "time_course":"Insidious over decades; exacerbations are acute precipitated events",
  "key_features":"Chronic productive cough, dyspnea, post-bronchodilator FEV1/FVC <0.70, hyperinflation on CXR, barrel chest",
  "consequence_if_missed":"Delayed diagnosis means missed opportunity for smoking cessation and early bronchodilator therapy; unrecognized severe disease increases perioperative risk"})

# ── 115: COPD: Stable Management ─────────────────────────────────────────────
T = "COPD: Stable Management"
DOM = "Internal medicine: pulmonology (COPD, asthma, pulmonary embolism, pneumonia, ILD, pleural effusion, pneumothorax, hypoxemic & hypercapnic respiratory failure, OSA)"
DISC = "medicine"

kps += [
  {"id":"copd-stable-mgmt-d1","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"A patient with stable severe COPD has persistent dyspnea at rest. What pharmacological option addresses dyspnea palliatively in advanced COPD?",
   "answer":"Opioids (morphine) are used for symptom management in advanced COPD; the Canadian Thoracic Society guideline specifically addresses managing dyspnea in advanced COPD patients.",
   "rationale":"Low-dose systemic opioids reduce the sensation of dyspnea via central mu-receptor mechanisms; this is the most evidence-based pharmacological dyspnea palliation in advanced COPD.",
   "bloom":"apply",
   "source":[{"book":"Society Guideline: Guideline   GOLD 2024 COPD Full Report","page":178}],
   "confusable_with":"high-dose opioids (contraindicated for respiratory depression risk)"},

  {"id":"copd-stable-mgmt-d2","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Home non-invasive positive pressure ventilation (NIPPV) in stable severe COPD: what does meta-analysis show about clinical outcomes?",
   "answer":"Home NIPPV is associated with improved clinical outcomes (reduced hospitalization, improved survival) in patients with severe chronic hypercapnia from COPD.",
   "rationale":"Nocturnal NIPPV reduces the work of breathing during sleep, allowing respiratory muscles to rest and reducing daytime hypercapnia through improved overnight gas exchange.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   GOLD 2024 COPD Full Report","page":177}],
   "confusable_with":"CPAP (used for OSA, not COPD hypercapnia)"},

  {"id":"copd-stable-mgmt-d3","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Muscle wasting (sarcopenia) in COPD contributes to higher morbidity and mortality. What is the mechanism and implication for management?",
   "answer":"Muscle loss in COPD results from systemic inflammation, inactivity, hypoxia, and glucocorticoid use; sarcopenia independently increases morbidity and mortality, making exercise rehabilitation essential.",
   "rationale":"Skeletal muscle dysfunction limits exercise tolerance and respiratory muscle strength; COPD patients with lower limb muscle weakness have worse prognosis independent of FEV1.",
   "bloom":"analyze",
   "source":[{"book":"Society Guideline: Guideline   GOLD 2024 COPD Full Report","page":164}],
   "confusable_with":""},

  {"id":"copd-stable-mgmt-d4","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"A COPD patient's reported exacerbation may not be a true COPD exacerbation. What alternative diagnoses should be excluded?",
   "answer":"Acute heart failure (NT-proBNP), pneumonia, pulmonary embolism, pneumothorax, and respiratory infections unrelated to COPD — these are common 'mimics' of COPD exacerbation.",
   "rationale":"Misattributing dyspnea to COPD exacerbation delays treatment of treatable conditions; NT-proBNP and chest imaging are useful in the initial assessment of acute breathlessness in COPD.",
   "bloom":"apply",
   "source":[{"book":"Society Guideline: Guideline   GOLD 2024 COPD Full Report","page":198}],
   "confusable_with":""},

  {"id":"copd-stable-mgmt-d5","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Theophylline has been used in COPD management. What residual evidence supports its use in stable COPD patients?",
   "answer":"Evidence shows theophylline treatment has value (improves FEV1 and exercise tolerance) in patients handicapped by chronic obstructive lung disease, though it is now a second-line option due to narrow therapeutic index.",
   "rationale":"Theophylline inhibits phosphodiesterase and antagonizes adenosine, providing modest bronchodilation and possible anti-inflammatory effects; toxicity (arrhythmias, seizures) limits its use.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   GOLD 2024 COPD Full Report","page":183}],
   "confusable_with":""},

  {"id":"copd-stable-mgmt-d6","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Pulmonary complications after abdominal surgery cost an average of what additional amount per episode and what patient factor most increases this risk?",
   "answer":"Postoperative pulmonary complications (PPCs) add an average of $25,000+ per episode; COPD (and OSA) most significantly increases this risk.",
   "rationale":"PPCs prolong ICU and hospital stays, requiring additional ventilatory support, antibiotics, and physiotherapy; COPD patients have severely reduced respiratory reserve that decompensates under surgical stress.",
   "bloom":"recall",
   "source":[{"book":"Miller/Baby Miller","page":784}],
   "confusable_with":""},

  {"id":"copd-stable-mgmt-d7","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What VTE prophylaxis principle is relevant in hospitalized stable COPD patients?",
   "answer":"VTE prophylaxis (pharmacological and/or mechanical) should be used in hospitalized COPD patients as they have elevated DVT/PE risk due to immobility, inflammation, and polycythemia.",
   "rationale":"Hospitalized COPD patients are immobile with systemic inflammation, polycythemia, and often dehydration — all VTE risk factors; PE can precipitate acute-on-chronic respiratory failure.",
   "bloom":"apply",
   "source":[{"book":"Society Guideline: Guideline   GOLD 2024 COPD Full Report","page":202}],
   "confusable_with":""},
]

# ── 116: Cardiac Imaging Interpretation ──────────────────────────────────────
T = "Cardiac Imaging Interpretation"
DOM = "Internal medicine: cardiology (ACS, stable & unstable angina, heart failure, brady/tachyarrhythmias, valvular disease, hypertension & emergencies, lipids, syncope)"
DISC = "medicine"

kps += [
  {"id":"cardiac-imaging-d1","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What does an E/A ratio >2 on mitral inflow Doppler indicate about left ventricular diastolic function?",
   "answer":"E/A >2 indicates restrictive filling pattern — rapid passive LV filling (high E) because the stiff ventricle has elevated filling pressure; atrial contraction contributes minimally (low A).",
   "rationale":"In severe diastolic dysfunction, elevated LA pressure accelerates early diastolic LV filling; the stiff ventricle is already near its pressure-volume limit, so atrial systole contributes little additional volume.",
   "bloom":"analyze",
   "source":[{"book":"Curated Units","page":0}],
   "confusable_with":"impaired relaxation (E/A <1, opposite pattern)"},

  {"id":"cardiac-imaging-d2","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What diastolic dysfunction pattern does an E/A ratio <1 represent?",
   "answer":"E/A <1 (reversal) indicates impaired relaxation — slow early diastolic filling (low E) with preserved atrial contribution (high A); the earliest pattern of diastolic dysfunction.",
   "rationale":"Impaired relaxation occurs when the LV cannot relax quickly enough in early diastole; the LA must contract more forcefully to achieve adequate filling, elevating the A velocity relative to E.",
   "bloom":"recall",
   "source":[{"book":"Curated Units","page":0}],
   "confusable_with":"restrictive filling (E/A >2, opposite)"},

  {"id":"cardiac-imaging-d3","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"On point-of-care ultrasound, a 'D-shaped' LV in the parasternal short-axis view indicates what pathological process?",
   "answer":"D-shaped LV indicates right ventricular pressure or volume overload — the RV is dilated and its pressure flattens the interventricular septum, distorting the normally circular LV cross-section.",
   "rationale":"The RV and LV share the interventricular septum; when RV pressure exceeds LV pressure (as in pulmonary embolism, RV failure, or pulmonary hypertension), septal bowing toward the LV creates the D-sign.",
   "bloom":"apply",
   "source":[{"book":"Miller/Baby Miller","page":411}],
   "confusable_with":"constrictive pericarditis (which also affects septal motion)"},

  {"id":"cardiac-imaging-d4","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What does the presence of strain imaging (global longitudinal strain, GLS) abnormality on echocardiography suggest when standard LVEF is preserved?",
   "answer":"Strain imaging abnormalities may suggest an underlying infiltrative cardiomyopathy (e.g., amyloidosis) even when LVEF appears preserved; GLS is more sensitive than EF for subclinical systolic dysfunction.",
   "rationale":"Amyloid infiltration causes subendocardial dysfunction detectable by strain before EF falls; the pattern of relative apical sparing of GLS is highly specific for cardiac amyloidosis.",
   "bloom":"analyze",
   "source":[{"book":"Society Guideline: Guideline   ACC AHA 2023 Atrial Fibrillation","page":23}],
   "confusable_with":"hypertensive cardiomyopathy"},

  {"id":"cardiac-imaging-d5","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"On chest X-ray, approximately what minimum volume of pleural fluid is required before it becomes visible?",
   "answer":"Pleural effusions are visible on CXR when >200 mL of fluid is present (blunting of costophrenic angle); smaller effusions require ultrasound for detection.",
   "rationale":"The costophrenic angle requires approximately 200 mL of fluid to be blunted on PA CXR; lateral views can detect as little as 75-100 mL; ultrasound detects even smaller collections.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":261}],
   "confusable_with":""},

  {"id":"cardiac-imaging-d6","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Holter monitoring showing no ischemic episodes has what predictive value for perioperative cardiac complications?",
   "answer":"An excellent negative predictive value for postoperative cardiac complications — absence of ischemic episodes on Holter monitoring effectively excludes significant ischemic burden.",
   "rationale":"Ischemia on ambulatory ECG monitoring reflects the degree of fixed and dynamic coronary obstruction; its absence suggests adequate coronary reserve under the modest daily exertional demands monitored.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":645}],
   "confusable_with":"exercise stress testing (limited by baseline ST changes or inability to exercise)"},

  {"id":"cardiac-imaging-d7","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"In POCUS assessment for pleural effusion, where should the probe be placed and in what position for optimal detection in a semi-recumbent patient?",
   "answer":"Probe in the midaxillary line with indicator toward the patient's head; may need more posterior positioning (between patient and bed) to visualize smaller effusions.",
   "rationale":"Pleural fluid gravitates posteriorly and basally; the midaxillary or posterior axillary line approach with appropriate probe orientation maximizes acoustic window to the dependent pleural space.",
   "bloom":"apply",
   "source":[{"book":"Miller/Baby Miller","page":417}],
   "confusable_with":""},
]

# ── 117: Cardiac Rehabilitation and Secondary Prevention ─────────────────────
T = "Cardiac Rehabilitation and Secondary Prevention"
DOM = "Internal medicine: cardiology (ACS, stable & unstable angina, heart failure, brady/tachyarrhythmias, valvular disease, hypertension & emergencies, lipids, syncope)"
DISC = "medicine"

kps += [
  {"id":"cardiac-rehab-d1","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What patient populations are recommended for cardiac rehabilitation?",
   "answer":"Individuals with ischemic heart disease (stable or post-ACS), congestive heart failure, and those recovering from myocardial infarction or cardiac procedures (including surgery).",
   "rationale":"Cardiac rehabilitation reduces cardiovascular mortality, recurrent events, and hospitalizations via structured exercise, risk factor modification, education, and psychosocial support.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Cardiac Rehabilitation and Secondary Prevention","page":2}],
   "confusable_with":""},

  {"id":"cardiac-rehab-d2","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What are the key components of cardiac rehabilitation beyond exercise training?",
   "answer":"Managing medical conditions and cardiovascular risk factors, optimizing nutrition, promoting smoking cessation, reducing psychosocial stress, and medication adherence.",
   "rationale":"Multidimensional rehabilitation addresses the entire cardiovascular risk profile; exercise alone is insufficient — smoking, hypertension, dyslipidemia, and psychological factors all independently drive recurrent events.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Cardiac Rehabilitation and Secondary Prevention","page":5}],
   "confusable_with":""},

  {"id":"cardiac-rehab-d3","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What equipment is typically available in the early post-discharge phase of cardiac rehabilitation (approximately week 1)?",
   "answer":"Exercise bicycles, treadmills, strength equipment, and telemetry monitoring; facilities typically structured for supervised exercise lasting about 2 weeks in this early phase.",
   "rationale":"Early phase-2 cardiac rehabilitation requires continuous ECG telemetry because exercise-induced arrhythmias and ischemia are most likely in the early post-event/post-procedural period.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Cardiac Rehabilitation and Secondary Prevention","page":4}],
   "confusable_with":""},

  {"id":"cardiac-rehab-d4","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Prehabilitation programs for surgical patients focus on what specific goals before planned cardiac surgery?",
   "answer":"Improved physical fitness, dietary interventions to counteract catabolism and support anabolism with exercise, antistress interventions to foster resilience, and smoking cessation.",
   "rationale":"Pre-operative physical conditioning (prehabilitation) improves cardiorespiratory reserve and speeds post-operative recovery; nutritional optimization reduces the catabolic effects of surgery.",
   "bloom":"recall",
   "source":[{"book":"Miller/Baby Miller","page":241}],
   "confusable_with":""},

  {"id":"cardiac-rehab-d5","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Cardiac rehabilitation for patients with congenital heart disease remains limited by what evidence gap?",
   "answer":"Research on cardiac rehabilitation for congenital heart disease remains limited, particularly lacking randomized clinical trials in both adult and pediatric populations to establish specific guidelines.",
   "rationale":"Congenital heart disease has diverse anatomies and physiologies that make generalization from acquired heart disease rehabilitation data problematic; bespoke rehabilitation protocols require disease-specific evidence.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Cardiac Rehabilitation and Secondary Prevention","page":6}],
   "confusable_with":""},

  {"id":"cardiac-rehab-d6","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"A high cervical spinal cord injury patient requires cardiac monitoring. What specific cardiac complication may require atropine or permanent pacing?",
   "answer":"Bradycardia from high cervical injury (disrupting sympathetic innervation C3-T5) can be severe enough to cause cardiac arrest; atropine or permanent pacing may be required.",
   "rationale":"High cervical cord injuries disrupt the entire sympathetic cardioaccelerator fibers (T1-T4), leaving unopposed vagal parasympathetic control and causing refractory bradycardia.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Acute Spinal Cord Injury & Syndromes","page":13}],
   "confusable_with":""},

  {"id":"cardiac-rehab-d7","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Cardiac rehabilitation is described as a 'complex, interprofessional intervention.' What specific level of evidence (LOE) framework do guidelines use to rate supporting evidence quality?",
   "answer":"ACC/AHA guidelines use Level of Evidence (LOE) that rates quality based on type, quantity, and consistency of evidence from clinical trials — ranging from LOE A (multiple RCTs) to LOE C (expert opinion).",
   "rationale":"Structured evidence grading enables clinicians to understand whether a recommendation rests on robust RCT data or weaker observational/expert opinion, guiding the strength of clinical application.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   ACC AHA 2022 Heart Failure","page":8}],
   "confusable_with":""},
]

# ── 118: Coagulation Abnormalities in Liver Disease ──────────────────────────
T = "Coagulation Abnormalities in Liver Disease"
DOM = "Internal medicine: gastroenterology & hepatology (upper & lower GI bleed, acute liver failure, cirrhosis & its complications, pancreatitis, IBD, bowel obstruction, hepatic encephalopathy)"
DISC = "medicine"

kps += [
  {"id":"coag-liver-d1","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Why does a prolonged PT/INR in liver disease NOT reliably indicate a bleeding tendency?",
   "answer":"The INR was designed to monitor warfarin, not liver function; in liver disease, anticoagulant factors (protein C, antithrombin, TFPI) are ALSO reduced, potentially balancing the procoagulant factor deficiency — patients may be hypercoagulable despite elevated INR.",
   "rationale":"Liver disease impairs synthesis of both procoagulant and anticoagulant factors equally; INR reflects only procoagulants (factors II, V, VII, X) measured in the PT assay, missing the anticoagulant balance.",
   "bloom":"analyze",
   "source":[{"book":"Morgan & Mikhail","page":1171},{"book":"Morgan & Mikhail","page":1185}],
   "confusable_with":"warfarin anticoagulation (where INR accurately predicts bleeding)"},

  {"id":"coag-liver-d2","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Only what percentage of normal factor activity is required for normal coagulation, and what does this mean for interpreting PT prolongation?",
   "answer":"Only 20-30% of normal factor activity is required for normal coagulation; PT prolongation in liver disease therefore usually reflects SEVERE liver disease or vitamin K deficiency.",
   "rationale":"The procoagulant reserve is large; PT prolongs only when factor levels fall below the 20-30% threshold, which occurs relatively late in the course of liver synthetic failure.",
   "bloom":"analyze",
   "source":[{"book":"Morgan & Mikhail","page":1171}],
   "confusable_with":""},

  {"id":"coag-liver-d3","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What is the optimal method to assess global coagulation status in a patient with liver disease?",
   "answer":"Thromboelastography (TEG), rotational thromboelastometry (ROTEM), and Sonoclot viscoelastic coagulation testing — these demonstrate the global state of the coagulation system including both clot formation and fibrinolysis.",
   "rationale":"Viscoelastic tests capture the full coagulation process (clot initiation, amplification, and fibrinolysis) in whole blood, detecting the true hemostatic balance that INR/PT misrepresents in liver disease.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1185}],
   "confusable_with":"PT/INR alone (inadequate for liver disease)"},

  {"id":"coag-liver-d4","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"How can platelet dysfunction in liver disease be partially compensated despite low platelet counts?",
   "answer":"Elevated von Willebrand factor (vWF) in liver disease may result in activated platelets allowing normal or increased coagulation despite much lower platelet counts.",
   "rationale":"Reduced ADAMTS13 activity in liver disease increases vWF multimer size, enhancing platelet adhesion; this partially compensates for thrombocytopenia by increasing platelet recruitment to injury sites.",
   "bloom":"analyze",
   "source":[{"book":"Morgan & Mikhail","page":1185}],
   "confusable_with":""},

  {"id":"coag-liver-d5","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"During liver transplantation, what coagulation complication may develop specifically during the anhepatic phase that requires specific treatment?",
   "answer":"Primary fibrinolysis (not DIC) can occur during the anhepatic phase — detected by viscoelastic coagulation analysis; treated with epsilon-aminocaproic acid or tranexamic acid (antifibrinolytics).",
   "rationale":"Without the functioning liver to clear tPA and other fibrinolytic activators, unopposed plasmin activation dissolves clots; antifibrinolytics are used selectively when confirmed by POC viscoelastic testing.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1213}],
   "confusable_with":"DIC (which has both thrombosis and fibrinolysis)"},

  {"id":"coag-liver-d6","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What is the PT/INR threshold that indicates severe hepatic synthetic dysfunction, and what is its significance for emergency surgery?",
   "answer":"Persistent INR ≥1.5 following vitamin K administration indicates true hepatic synthetic failure; emergency surgery in this setting carries very high risk due to uncompensatable coagulopathy.",
   "rationale":"Vitamin K administration corrects coagulopathy caused by deficiency but not by hepatocellular failure; an INR ≥1.5 persisting after vitamin K confirms factor synthesis impairment.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1189}],
   "confusable_with":"warfarin-induced coagulopathy (correctable with vitamin K)"},

  {"id":"coag-liver-d7","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Primary fibrinolysis is occasionally encountered in which non-transplant surgical conditions?",
   "answer":"Primary fibrinolysis occurs in severe liver disease, during the anhepatic phase of liver transplantation, and occasionally in patients with carcinoma of the prostate.",
   "rationale":"Prostate cancer releases high levels of urokinase-type plasminogen activator (uPA), causing primary fibrinolysis; this is distinct from DIC and requires antifibrinolytic therapy rather than heparin.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1178}],
   "confusable_with":"DIC (consumptive)"},
]

kps.append({"_type":"illness_script","topic":T,"discipline":DISC,
  "enabling_conditions":"Cirrhosis (any etiology), acute liver failure, liver transplantation, hepatic malignancy",
  "pathophysiology":"Reduced synthesis of procoagulant AND anticoagulant factors simultaneously; thrombocytopenia from portal hypertension (splenomegaly); vWF elevation partially compensates; fibrinolysis may dominate in anhepatic phase",
  "time_course":"Chronic in cirrhosis; acute in ALF or transplantation",
  "key_features":"Prolonged PT/INR (does not equal bleeding risk), low platelets, abnormal viscoelastic testing; risk of both bleeding AND thrombosis",
  "consequence_if_missed":"Uncontrolled variceal or surgical bleeding; paradoxical portal vein thrombosis if anticoagulants withheld inappropriately"})

# ── 119: Colonic Angiodysplasia & Vascular Lesions ───────────────────────────
T = "Colonic Angiodysplasia & Vascular Lesions"
DOM = "Internal medicine: gastroenterology & hepatology (upper & lower GI bleed, acute liver failure, cirrhosis & its complications, pancreatitis, IBD, bowel obstruction, hepatic encephalopathy)"
DISC = "medicine"

kps += [
  {"id":"colonic-angiodysplasia-d1","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What are the anatomical location, typical patient demographics, and classic associations of colonic angiodysplasia?",
   "answer":"Angiodysplasia: small submucosal vascular malformations with right colon predominance; associated with advanced age, aortic stenosis, and renal failure (uremic toxins damage vessels).",
   "rationale":"Right colonic predominance may reflect high intraluminal pressure and mechanical stress on the thinner cecal wall; the Heyde syndrome (AS + angiodysplasia bleeding) involves acquired von Willebrand factor deficiency from AS-related shear stress.",
   "bloom":"recall",
   "source":[{"book":"Curated Units","page":0}],
   "confusable_with":"diverticular bleeding (left colon predominance)"},

  {"id":"colonic-angiodysplasia-d2","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"How does colonic angiodysplasia present clinically and what diagnostic modalities are used?",
   "answer":"Presents with chronic occult GI bleeding causing iron-deficiency anemia, or intermittent visible bleeding; diagnosed by colonoscopy (spider-web/cherry-red lesions) or capsule endoscopy for small bowel involvement.",
   "rationale":"Angiodysplastic lesions are often small and intermittent in bleeding, making them easily missed on colonoscopy without careful mucosal inspection; capsule endoscopy detects small bowel lesions beyond colonoscope reach.",
   "bloom":"recall",
   "source":[{"book":"Curated Units","page":0}],
   "confusable_with":"hemorrhoids (more distal, bright red coating stool)"},

  {"id":"colonic-angiodysplasia-d3","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What endoscopic treatment is used for bleeding angiodysplasia?",
   "answer":"Argon plasma coagulation (APC) is the primary endoscopic hemostasis technique for angiodysplasia; other options include bipolar electrocoagulation and heater probe.",
   "rationale":"APC delivers non-contact electrocoagulation via ionized argon gas, enabling treatment of flat or recessed lesions with controlled depth of thermal injury appropriate for thin-walled right colon.",
   "bloom":"recall",
   "source":[{"book":"Curated Units","page":0}],
   "confusable_with":""},

  {"id":"colonic-angiodysplasia-d4","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"In upper GI bleeding, what less common causes beyond peptic ulcer disease must be considered?",
   "answer":"Angiodysplasia, erosive esophagitis, Mallory-Weiss tear, gastric tumor, and aortoenteric fistula are less common upper GI causes alongside the dominant peptic ulcer disease.",
   "rationale":"Aortoenteric fistula is life-threatening and must be excluded in patients with prior aortic surgery; Mallory-Weiss tears follow vomiting episodes; each requires specific endoscopic or surgical management.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":2157}],
   "confusable_with":""},

  {"id":"colonic-angiodysplasia-d5","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"When a patient presents with melena (without hematemesis), what BUN:Creatinine ratio supports an upper GI bleeding source?",
   "answer":"BUN:Cr >30 has a positive LR of 7.5 for upper GI bleeding; a ratio >35 has 100% specificity.",
   "rationale":"Digestion of blood in the upper GI tract generates urea (elevating BUN) while creatinine is unaffected; the BUN:Cr ratio is a non-endoscopic indicator of upper GI bleeding location.",
   "bloom":"apply",
   "source":[{"book":"MGH Housestaff Manual","page":70}],
   "confusable_with":"prerenal azotemia (also high BUN:Cr but no GI bleed)"},

  {"id":"colonic-angiodysplasia-d6","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"In large bowel obstruction, what neoplastic cause is especially important to recognize as it may present as the first sign of colorectal carcinoma?",
   "answer":"Left-sided colorectal carcinoma — LBO from obstructing left colon cancer is often the first clinical presentation; emergency surgery may be required.",
   "rationale":"Left colon cancers grow intraluminally in the narrower sigmoid/descending colon and cause obstruction at smaller sizes than right-sided cancers (which present with anemia/weight loss).",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Large Bowel Obstruction (LBO)","page":2}],
   "confusable_with":"sigmoid volvulus"},
]

# ── 120: Complicated Parapneumonic Effusion and Empyema ───────────────────────
T = "Complicated Parapneumonic Effusion and Empyema"
DOM = "Internal medicine: pulmonology (COPD, asthma, pulmonary embolism, pneumonia, ILD, pleural effusion, pneumothorax, hypoxemic & hypercapnic respiratory failure, OSA)"
DISC = "medicine"

kps += [
  {"id":"parapneumonic-empyema-d1","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What fluid characteristics distinguish a complicated parapneumonic effusion from an uncomplicated one?",
   "answer":"Complicated: pH <7.0, glucose <60 mg/dL, high LDH, with risk of progression to empyema; Uncomplicated: pH 7.0-7.2, glucose >60 mg/dL — typically resolves with antibiotics alone.",
   "rationale":"Low pH reflects bacterial metabolism and lactate production; hypoglycosis results from bacterial glucose consumption; together they indicate an effusion at high risk of organizing into empyema if not drained.",
   "bloom":"apply",
   "source":[{"book":"Curated Units","page":0}],
   "confusable_with":"transudative effusion (pH >7.3, glucose normal)"},

  {"id":"parapneumonic-empyema-d2","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Light's criteria classify pleural effusions. What three measurements distinguish an exudate?",
   "answer":"Effusion protein/serum protein >0.5 OR effusion LDH/serum LDH >0.6 OR effusion LDH >200 (or >2/3 upper limit normal serum LDH) — meeting ANY criterion = exudate.",
   "rationale":"Light's criteria have >97% sensitivity for exudate identification; parapneumonic effusions are exudates with WBC >1,000 (complicated >100,000 with gram stain positivity = empyema).",
   "bloom":"recall",
   "source":[{"book":"Intern Notes / Survival Guide","page":83}],
   "confusable_with":"transudate (none of Light's criteria met)"},

  {"id":"parapneumonic-empyema-d3","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"A pleural effusion WBC >100,000 with positive gram stain of pleural fluid establishes what diagnosis?",
   "answer":"Empyema — established by >100,000 WBC AND positive gram stain or culture; requires drainage (chest tube) and prolonged antibiotics.",
   "rationale":"Empyema represents frank pus in the pleural space; once organized (fibrinopurulent or organizing stage), tube drainage alone is insufficient and surgical decortication or intrapleural fibrinolytics are needed.",
   "bloom":"recall",
   "source":[{"book":"Intern Notes / Survival Guide","page":83}],
   "confusable_with":"complicated parapneumonic effusion (sterile, different threshold)"},

  {"id":"parapneumonic-empyema-d4","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What are the indications for therapeutic thoracentesis beyond parapneumonic effusion and empyema?",
   "answer":"Large effusions causing respiratory compromise or symptoms (dyspnea), hemothorax, empyema, and complicated parapneumonic effusion all warrant therapeutic drainage.",
   "rationale":"Thoracentesis for therapeutic relief of respiratory compromise removes mechanical compression of lung parenchyma; for infected effusions it removes the bacterial reservoir driving ongoing infection.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":261}],
   "confusable_with":""},

  {"id":"parapneumonic-empyema-d5","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"A bronchopleural fistula (BPF) can occur after pneumonectomy. What anesthetic challenge does an existing BPF create?",
   "answer":"BPF creates communication between the bronchus and pleural space; the diseased lung must be frequently suctioned during procedures; one-lung ventilation is required to prevent contamination of the healthy lung.",
   "rationale":"Positive pressure ventilation through a BPF causes preferential air leak through the fistula rather than alveolar ventilation; aspiration of infected pleural fluid into the contralateral lung is a lethal complication.",
   "bloom":"analyze",
   "source":[{"book":"Morgan & Mikhail","page":918}],
   "confusable_with":""},

  {"id":"parapneumonic-empyema-d6","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What coagulation parameters require consideration before performing therapeutic thoracentesis?",
   "answer":"Consider reversing coagulopathy (INR >1.5, recent LMWH) or thrombocytopenia (platelets <50k) before thoracentesis — though there are no absolute contraindications.",
   "rationale":"Thoracentesis carries bleeding risk into the pleural space or chest wall; coagulation correction reduces hematoma and hemothorax risk, particularly in anticoagulated or thrombocytopenic patients.",
   "bloom":"apply",
   "source":[{"book":"MGH Housestaff Manual","page":261}],
   "confusable_with":""},

  {"id":"parapneumonic-empyema-d7","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Community-acquired pneumonia complicated by a parapneumonic effusion occurs in what proportion of hospitalized CAP patients?",
   "answer":"20-40% of hospitalized CAP patients develop parapneumonic effusions.",
   "rationale":"Parapneumonic effusions result from pleural inflammation adjacent to pneumonic consolidation; uncomplicated ones resolve with antibiotics, but a minority progress to complicated or empyematous stage requiring drainage.",
   "bloom":"recall",
   "source":[{"book":"Curated Units","page":0}],
   "confusable_with":""},
]

kps.append({"_type":"illness_script","topic":T,"discipline":DISC,
  "enabling_conditions":"Bacterial pneumonia (CAP or HAP), aspiration, lung abscess, thoracic surgery, esophageal rupture",
  "pathophysiology":"Bacterial invasion of pleural space → inflammatory exudate (parapneumonic) → bacterial proliferation → empyema; pH/glucose fall as bacteria metabolize glucose/generate lactate",
  "time_course":"Uncomplicated resolves in days; complicated progresses to empyema over days-weeks if untreated",
  "key_features":"Fever persisting despite antibiotics, pleural pain, decreased breath sounds; pH <7.0, glucose <60, +culture = empyema",
  "consequence_if_missed":"Organized empyema requiring surgery (decortication); sepsis; lung entrapment"})

# ── 121: Crohn's Disease: Diagnosis & Classification ─────────────────────────
T = "Crohn's Disease: Diagnosis & Classification"
DOM = "Internal medicine: gastroenterology & hepatology (upper & lower GI bleed, acute liver failure, cirrhosis & its complications, pancreatitis, IBD, bowel obstruction, hepatic encephalopathy)"
DISC = "medicine"

kps += [
  {"id":"crohns-diagnosis-d1","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"P-ANCA and ASCA are serological markers used in IBD. Which disease is more associated with each, and what is their diagnostic utility?",
   "answer":"P-ANCA: more associated with ulcerative colitis; ASCA: found in both Crohn's and UC but MORE prevalent in Crohn's disease; testing both helps distinguish UC from Crohn's but is not definitive.",
   "rationale":"P-ANCA in UC reflects autoimmune colonic inflammation; ASCA antibodies target Saccharomyces cerevisiae cell wall antigens and appear more commonly in Crohn's; dual testing increases diagnostic specificity.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Ulcerative Colitis  Diagnosis & Classification","page":4}],
   "confusable_with":""},

  {"id":"crohns-diagnosis-d2","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What distinguishes Crohn's disease from ulcerative colitis in terms of the extent and depth of bowel involvement?",
   "answer":"Crohn's involves any part of the GI tract from mouth to anus with skip lesions and transmural (full-thickness) inflammation; UC is limited to the colon with continuous mucosal/submucosal inflammation.",
   "rationale":"Transmural involvement in Crohn's causes fistulas, abscesses, and strictures; skip lesions reflect patchy inflammation unlike UC's continuous mucosal pattern progressing proximally from rectum.",
   "bloom":"analyze",
   "source":[{"book":"StatPearls: StatPearls   Ulcerative Colitis  Diagnosis & Classification","page":4}],
   "confusable_with":"ulcerative colitis (continuous, mucosal only)"},

  {"id":"crohns-diagnosis-d3","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"A first-degree relative of a patient with ulcerative colitis has what elevated risk of developing IBD?",
   "answer":"A four-fold higher risk of developing ulcerative colitis; UC also has higher incidence in Jewish populations than other ethnicities.",
   "rationale":"Genetic susceptibility to UC involves NOD2 and other immune-regulatory genes; first-degree relatives share ~50% of genetic variants, conferring substantially increased risk.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Ulcerative Colitis  Diagnosis & Classification","page":2}],
   "confusable_with":""},

  {"id":"crohns-diagnosis-d4","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"How does the severity of ulcerative colitis grade bleeding episodes and what constitutes 'severe' disease?",
   "answer":"Mild: <4 rectal bleeding episodes/day; Moderate: >4/day; Severe: >4/day PLUS systemic features of illness (fever, tachycardia, anemia) combined with hypoalbuminemia.",
   "rationale":"Severe UC (Truelove-Witts criteria) indicates colonic inflammation sufficient to cause systemic toxicity; these patients require hospital admission, IV steroids, and consideration for colectomy or rescue biologics.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Ulcerative Colitis  Diagnosis & Classification","page":6}],
   "confusable_with":""},

  {"id":"crohns-diagnosis-d5","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Appendectomy before age 20 has opposite associations with UC and Crohn's disease. What are they?",
   "answer":"Appendectomy before age 20 is associated with DECREASED incidence of UC, but INCREASED incidence of Crohn's disease.",
   "rationale":"The appendix contains lymphoid tissue that may modulate intestinal immune tolerance; its removal before adulthood alters gut immunity in disease-specific ways — protecting against UC but potentially increasing Crohn's risk.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Ulcerative Colitis  Diagnosis & Classification","page":2}],
   "confusable_with":""},

  {"id":"crohns-diagnosis-d6","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Microbiologic studies are included in the initial IBD evaluation. Why is this essential before diagnosing idiopathic IBD?",
   "answer":"Infectious causes (bacterial, parasitic) can produce clinical findings indistinguishable from idiopathic UC; microbiologic studies for infection must be negative before attributing findings to IBD.",
   "rationale":"Clostridium difficile, Campylobacter, Shigella, and Entamoeba histolytica all cause bloody diarrhea with colitis that mimics IBD; treating IBD with immunosuppressants in the presence of infection is dangerous.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Ulcerative Colitis  Diagnosis & Classification","page":4}],
   "confusable_with":"infectious colitis"},

  {"id":"crohns-diagnosis-d7","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What is the first-line treatment for mild-to-moderate ulcerative colitis and what remission rate does it achieve?",
   "answer":"First-line treatment is sulfasalazine and 5-aminosalicylates (oral ± rectal), achieving remission in approximately 50% of patients.",
   "rationale":"5-ASA agents work locally on colonic mucosa to reduce inflammation; rectal preparations are particularly effective for proctitis; failure to achieve remission leads to escalation to glucocorticoids or biologics.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Ulcerative Colitis  Diagnosis & Classification","page":5}],
   "confusable_with":""},
]

kps.append({"_type":"confusable_pair","topic_a":"Crohn's Disease","topic_b":"Ulcerative Colitis",
  "discriminator":"Crohn's: any GI segment, skip lesions, transmural, fistulas/abscesses, ASCA more prevalent, appendectomy increases risk; UC: colon only, continuous, mucosal, P-ANCA more prevalent, appendectomy before 20 reduces risk"})

print(f"Topics 111-121 complete: {len(kps)} KP objects")
with open('data/_kps_part3b.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Saved to data/_kps_part3b.json")
