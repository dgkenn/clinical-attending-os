
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/_kp_redeepen.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

kps = []
DOM_GI = ('Internal medicine: gastroenterology & hepatology (upper & lower GI bleed, acute liver failure, '
          'cirrhosis & its complications, pancreatitis, IBD, bowel obstruction, hepatic encephalopathy)')
DOM_HEME = ('Internal medicine: hematology & oncology (anemias, anticoagulation & reversal, VTE prophylaxis & '
            'treatment, thrombocytopenia & DIC, transfusion medicine, oncologic emergencies, neutropenic fever)')
DOM_NEPH = 'Internal medicine: nephrology, fluids & electrolytes'
DIS = 'medicine'

# ── [140] Hepatocellular Carcinoma ────────────────────────────────────────────
T = 'Hepatocellular Carcinoma (HCC)'
kps += [
  {'id':'hcc-d1','topic':T,'domain':DOM_GI,'discipline':DIS,
   'stem':'NAFLD/MASLD is a growing cause of HCC; what percentage of HCC occurs in the absence of background cirrhosis in NAFLD patients?',
   'answer':'13% of NAFLD-associated HCC occurs without cirrhosis; HCC incidence in the US expected to increase 122% by 2030 due to obesity/diabetes',
   'rationale':'NAFLD-driven HCC can bypass cirrhosis, highlighting the need for surveillance even in non-cirrhotic at-risk patients.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Hepatocellular Carcinoma (HCC)','page':3}],'confusable_with':'HBV-associated HCC (also arises without cirrhosis but via viral genome integration)'},
  {'id':'hcc-d2','topic':T,'domain':DOM_GI,'discipline':DIS,
   'stem':'How does HBV drive hepatocellular carcinogenesis, and what specific genomic locus is a primary target?',
   'answer':'HBV integrates its genome into host DNA, primarily at the telomerase reverse transcriptase (TERT) promoter, driving oncogenesis',
   'rationale':'TERT promoter mutation caused by HBV integration confers replicative immortality to hepatocytes, the first step in malignant transformation.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Hepatocellular Carcinoma (HCC)','page':2}],'confusable_with':'HCV-associated HCC (occurs through cirrhosis/chronic inflammation, not direct genomic integration)'},
  {'id':'hcc-d3','topic':T,'domain':DOM_GI,'discipline':DIS,
   'stem':'Alpha-fetoprotein (AFP) in HCC: does its level correlate with tumour size or vascular invasion?',
   'answer':'No; AFP levels do not correlate with tumour size or vascular invasion; about 40% of HCC patients have elevated AFP',
   'rationale':'AFP sensitivity is limited; absence of AFP elevation does not exclude HCC, and false positives occur in cirrhosis and pregnancy.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Hepatocellular Carcinoma (HCC)','page':5}],'confusable_with':''},
  {'id':'hcc-d4','topic':T,'domain':DOM_GI,'discipline':DIS,
   'stem':'What are the Milan criteria for liver transplantation in HCC, and what survival rates do they confer?',
   'answer':'Milan criteria: single tumour <=5cm or <=3 tumours each <=3cm, no vascular invasion; associated with 60-80% 5-year survival and <15% post-transplant recurrence',
   'rationale':'Milan criteria define the threshold at which transplant is curative rather than palliative; exceeding them dramatically increases recurrence.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Hepatocellular Carcinoma (HCC)','page':8}],'confusable_with':'UCSF criteria (slightly expanded; less universally accepted)'},
  {'id':'hcc-d5','topic':T,'domain':DOM_GI,'discipline':DIS,
   'stem':'What is the first-line systemic treatment for advanced HCC, and what is the second-line FDA-approved option?',
   'answer':'First-line: sorafenib (multikinase inhibitor); second-line: regorafenib (also a multikinase inhibitor) for sorafenib-intolerant or progressed patients',
   'rationale':'Regorafenib demonstrated OS benefit in patients who progressed on sorafenib; regorafenib has less palmar-plantar erythrodysesthesia than sorafenib.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Hepatocellular Carcinoma (HCC)','page':8}],'confusable_with':'lenvatinib (alternative first-line), atezolizumab+bevacizumab (now preferred first-line in many guidelines)'},
  {'id':'hcc-d6','topic':T,'domain':DOM_GI,'discipline':DIS,
   'stem':'Intraperitoneal bleeding is a life-threatening complication of HCC; what is the emergent management?',
   'answer':'Emergent angiography with embolisation for haemoperitoneum from ruptured HCC',
   'rationale':'HCC tumours are highly vascular; rupture causes rapid haemoperitoneum requiring immediate haemostatic intervention before definitive oncological management.',
   'bloom':'apply','source':[{'book':'StatPearls: StatPearls   Hepatocellular Carcinoma (HCC)','page':9}],'confusable_with':''},
  {'id':'hcc-d7','topic':T,'domain':DOM_GI,'discipline':DIS,
   'stem':'HCC shares risk factor overlap with ESLD. In decompensated cirrhosis, when should acute portal vein thrombosis (PVT) be anticoagulated?',
   'answer':'Anticoagulate acute PVT with LMWH (unless high bleeding risk); transition to DOAC or warfarin once stable; continue at least 6 months',
   'rationale':'Anticoagulation of acute PVT can re-canalise the portal vein and prevent extension to mesenteric veins; bleeding risk must be weighed against thrombosis risk.',
   'bloom':'apply','source':[{'book':'MGH Housestaff Manual','page':93}],'confusable_with':''},
]
kps.append({'_type':'illness_script','topic':T,'discipline':DIS,
  'enabling_conditions':'Cirrhosis (HBV, HCV, alcohol, NAFLD), aflatoxin exposure, haemochromatosis, alpha-1-antitrypsin deficiency',
  'pathophysiology':'Oncogenic drivers include viral genome integration (HBV), chronic inflammation/fibrosis (HCV/alcohol/NAFLD), and metabolic injury',
  'time_course':'Develops over years of chronic liver disease; aggressive once symptomatic',
  'key_features':'RUQ pain/mass, weight loss, AFP elevation, arterial enhancement with washout on triphasic CT/MRI (LI-RADS 5)',
  'consequence_if_missed':'Tumour growth beyond Milan criteria (transplant window lost), vascular invasion, distant metastases'})

# ── [141] Hepatorenal Syndrome ────────────────────────────────────────────────
T = 'Hepatorenal Syndrome (HRS)'
kps += [
  {'id':'hrs-d1','topic':T,'domain':DOM_GI,'discipline':DIS,
   'stem':'What is the core pathophysiological sequence that leads to renal vasoconstriction in hepatorenal syndrome?',
   'answer':'Portal hypertension -> NO/prostaglandin-mediated splanchnic vasodilation -> reduced effective arterial blood volume -> RAAS/ADH/SNS activation -> renal vasoconstriction',
   'rationale':'The kidneys in HRS are structurally normal but functionally ischemic due to systemic haemodynamic derangement; normal kidneys transplanted into HRS patients recover function.',
   'bloom':'recall','source':[{'book':'MGH Housestaff Manual','page':97}],'confusable_with':'ATN (structural tubular damage; FENa >2%, muddy casts)'},
  {'id':'hrs-d2','topic':T,'domain':DOM_GI,'discipline':DIS,
   'stem':'HRS-AKI (formerly HRS type 1) requires what diagnostic criteria for confirmation?',
   'answer':'Advanced hepatic failure with portal hypertension (ascites); exclusion of other AKI causes; no improvement after 48h of diuretic withdrawal and volume expansion with albumin',
   'rationale':'HRS is a diagnosis of exclusion requiring volume challenge to rule out hypovolaemic AKI before initiating vasoconstrictors.',
   'bloom':'recall','source':[{'book':'MGH Housestaff Manual','page':97}],'confusable_with':'pre-renal AKI (responds to volume), CKD on cirrhosis'},
  {'id':'hrs-d3','topic':T,'domain':DOM_GI,'discipline':DIS,
   'stem':'What is the evidence-based treatment regimen for HRS-AKI, and what adverse effects must be monitored?',
   'answer':'Vasoconstrictor (terlipressin or norepinephrine) plus albumin; monitor for ischaemic and respiratory adverse effects',
   'rationale':'Vasoconstrictors reverse splanchnic vasodilation; albumin expands effective circulating volume; combination improves renal function and bridges to transplant.',
   'bloom':'apply','source':[{'book':'StatPearls: StatPearls   Hepatorenal Syndrome (HRS)','page':2}],'confusable_with':''},
  {'id':'hrs-d4','topic':T,'domain':DOM_GI,'discipline':DIS,
   'stem':'What is the median transplant-free survival after vasopressor initiation for HRS, based on a recent cohort study?',
   'answer':'Median transplant-free survival was 28 days; median overall survival from vasopressor initiation was only 48 days; 33.8% died during hospitalisation',
   'rationale':'HRS carries very poor prognosis without liver transplantation; these data support early transplant evaluation and goals-of-care conversations.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Hepatorenal Syndrome (HRS)','page':9}],'confusable_with':''},
  {'id':'hrs-d5','topic':T,'domain':DOM_GI,'discipline':DIS,
   'stem':'In patients with refractory ascites, what procedure can transiently reduce abdominal distension and restore haemodynamic stability?',
   'answer':'Abdominal paracentesis can transiently reduce abdominal distension and restore haemodynamic stability; TIPS is used for refractory cases',
   'rationale':'Large-volume paracentesis with albumin infusion (8 g/L removed) reduces intra-abdominal pressure and improves splanchnic perfusion acutely.',
   'bloom':'apply','source':[{'book':'Miller/Baby Miller','page':533}],'confusable_with':''},
  {'id':'hrs-d6','topic':T,'domain':DOM_GI,'discipline':DIS,
   'stem':'HRS staging (KDIGO-based) classifies AKI by creatinine rise: what creatinine change defines Stage 1A vs Stage 1B?',
   'answer':'Stage 1A: creatinine increase >=0.3 mg/dL to <1.5 mg/dL; Stage 1B: >=1.5 mg/dL to twice the baseline creatinine',
   'rationale':'Granular staging enables risk stratification and earlier intervention in HRS-AKI before full renal failure develops.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Hepatorenal Syndrome (HRS)','page':6}],'confusable_with':''},
  {'id':'hrs-d7','topic':T,'domain':DOM_GI,'discipline':DIS,
   'stem':'When managing a patient with decompensated cirrhosis and oliguria, what is the foundational management principle for AKI?',
   'answer':'Optimise haemodynamics and avoid nephrotoxins: correct volume status, hold diuretics if hypovolaemic, stop NSAIDs/ACEi/ARBs, avoid contrast; empiric diuretics in oliguria have no benefit',
   'rationale':'Many AKI episodes in cirrhosis are prerenal or drug-induced and respond to haemodynamic optimisation before vasoconstrictors are needed.',
   'bloom':'apply','source':[{'book':'MGH Housestaff Manual','page':100}],'confusable_with':''},
]
kps.append({'_type':'illness_script','topic':T,'discipline':DIS,
  'enabling_conditions':'Advanced cirrhosis with portal hypertension, ascites, SBP, large-volume paracentesis without albumin, GI bleed',
  'pathophysiology':'Splanchnic vasodilation reduces effective circulating volume -> RAAS/SNS activation -> renal vasoconstriction; kidneys structurally normal',
  'time_course':'HRS-AKI: rapid progression (days); HRS-CKD: slower (weeks-months)',
  'key_features':'Rising creatinine in cirrhotic patient, no structural kidney disease, no improvement after albumin challenge, FENa <0.1%',
  'consequence_if_missed':'Irreversible renal failure, need for RRT, death without liver transplantation'})

# ── [142] Hypercalcemia ───────────────────────────────────────────────────────
T = 'Hypercalcemia: Causes and Management'
kps += [
  {'id':'hypercalcemia-d1','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'What formula corrects total serum calcium for hypoalbuminemia, and why is this correction necessary?',
   'answer':'Corrected Ca = measured Ca (mg/dL) + [4.0 - serum albumin (g/dL)] x 0.8; low albumin causes falsely low total calcium while ionised calcium is normal',
   'rationale':'About 40% of circulating calcium is albumin-bound; hypoalbuminaemia reduces total calcium without affecting ionised (physiologically active) calcium.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Hypercalcemia  Causes and Management','page':2}],'confusable_with':''},
  {'id':'hypercalcemia-d2','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'Hypercalcemia symptoms can be remembered by what mnemonic, and what do each refer to?',
   'answer':'"Bones, Groans, Moans and Psychic Tones": bones (bone pain, fractures), groans (GI: N/V, constipation, pancreatitis), moans (polyuria, nephrolithiasis), psychic tones (confusion, depression, fatigue)',
   'rationale':'This mnemonic organises the multi-system manifestations of hypercalcaemia across skeletal, GI, renal, and neuropsychiatric systems.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Hypercalcemia  Causes and Management','page':4}],'confusable_with':''},
  {'id':'hypercalcemia-d3','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'If PTH is elevated (or inappropriately unsuppressed) in hypercalcemia, what are the three main differential diagnoses?',
   'answer':'Primary hyperparathyroidism, tertiary hyperparathyroidism, and familial hypocalciuric hypercalcaemia (FHH)',
   'rationale':'PTH-mediated hypercalcaemia requires distinguishing sporadic primary HPT (most common) from FHH (benign, no surgical indication) and tertiary HPT (CKD setting).',
   'bloom':'analyze','source':[{'book':'StatPearls: StatPearls   Hypercalcemia','page':5}],'confusable_with':'PTHrP-mediated HHM (PTH suppressed, not elevated)'},
  {'id':'hypercalcemia-d4','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'Humoral hypercalcemia of malignancy (HHM) is mediated by which peptide, and which tumours most commonly produce it?',
   'answer':'PTHrP (parathyroid hormone-related protein); produced by squamous cell carcinomas, renal cell carcinoma, bladder, breast cancer',
   'rationale':'PTHrP mimics PTH actions on bone and kidney, raising calcium while suppressing true PTH; PTHrP measurement distinguishes HHM from primary HPT.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Hypercalcemia  Causes and Management','page':5}],'confusable_with':'osteolytic bone metastases (local cytokine release, PTHrP often negative)'},
  {'id':'hypercalcemia-d5','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'Granulomatous diseases and lymphoma cause hypercalcemia by what mechanism?',
   'answer':'Extrarenal conversion of 25-hydroxyvitamin D to 1,25-dihydroxyvitamin D by activated macrophages, bypassing renal regulation',
   'rationale':'Activated macrophages in granulomata (sarcoid, TB, Wegeners) have constitutive 1-alpha-hydroxylase activity independent of PTH suppression.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Hypercalcemia  Causes and Management','page':3}],'confusable_with':'vitamin D intoxication (exogenous, 25-OHD very elevated; 1,25 may be normal)'},
  {'id':'hypercalcemia-d6','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'An anaesthetist reviewing a patient with hypercalcemia preoperatively should consider which two electrolyte checks due to associated dysregulation?',
   'answer':'Check serum K+ and Mg2+ (hypercalcaemia is associated with dysregulation of these electrolytes); acidosis should be avoided (reduces Ca2+-albumin binding)',
   'rationale':'Concurrent electrolyte abnormalities in hypercalcaemia increase cardiac arrhythmia risk and must be corrected before elective surgery.',
   'bloom':'apply','source':[{'book':'Stanford CA-1','page':60}],'confusable_with':''},
  {'id':'hypercalcemia-d7','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'Cancer-related hypercalcemia often occurs in what disease stage, and what is its prognosis?',
   'answer':'Occurs in later stages of malignancy; poses a bleak prognosis with multiple ER visits, frequent hospitalisations, and limited survival',
   'rationale':'HHM signals advanced cancer with significant tumour burden; treatment is palliative (IV fluids, bisphosphonates) rather than curative.',
   'bloom':'apply','source':[{'book':'StatPearls: StatPearls   Hypercalcemia  Causes and Management','page':7}],'confusable_with':''},
]

# ── [143] Hypercapnic Respiratory Failure ─────────────────────────────────────
T = 'Hypercapnic Respiratory Failure'
DOM_PULM = ('Internal medicine: pulmonology (COPD, asthma, pulmonary embolism, pneumonia, ILD, pleural effusion, '
            'pneumothorax, hypoxemic & hypercapnic respiratory failure, OSA)')
kps += [
  {'id':'hypercapnic-resp-failure-d1','topic':T,'domain':DOM_PULM,'discipline':DIS,
   'stem':'What two broad mechanisms cause hypercapnic respiratory failure?',
   'answer':'Hypoventilation (e.g., drug intoxication, neuromuscular weakness, obesity hypoventilation) or increased dead space ventilation (e.g., COPD, severe asthma)',
   'rationale':'PaCO2 = VCO2 / (VA); hypercapnia arises when alveolar ventilation is inadequate either from reduced drive/effort or from wasted ventilation.',
   'bloom':'recall','source':[{'book':'Miller/Baby Miller','page':767}],'confusable_with':'hypoxemic respiratory failure (V/Q mismatch or shunt; normal or low PaCO2)'},
  {'id':'hypercapnic-resp-failure-d2','topic':T,'domain':DOM_PULM,'discipline':DIS,
   'stem':'In acute hypercapnic respiratory failure, what non-invasive respiratory support modality is recommended, and what does it include?',
   'answer':'Non-invasive positive-pressure ventilation (NIPPV), encompassing CPAP and BiPAP; improves health-related quality of life and reduces intubation in acute COPD exacerbation',
   'rationale':'NIPPV augments alveolar ventilation, reduces work of breathing, and avoids complications of mechanical ventilation when used appropriately.',
   'bloom':'recall','source':[{'book':'Society Guideline: Guideline   GOLD 2024 COPD Full Report','page':120}],'confusable_with':'HFNC (beneficial for hypoxaemic failure; less evidence in hypercapnic failure)'},
  {'id':'hypercapnic-resp-failure-d3','topic':T,'domain':DOM_PULM,'discipline':DIS,
   'stem':'What supplemental oxygen SpO2 target is appropriate for a patient at risk for hypercapnic respiratory failure, and why?',
   'answer':'SpO2 88-92% in patients at risk for hypercapnia; higher targets risk suppressing hypoxic drive and worsening hypercapnia (Haldane effect)',
   'rationale':'Excessive oxygen in chronic CO2 retainers worsens hypercapnia through Haldane effect (CO2 displacement from hemoglobin) and reduced hypoxic pulmonary vasoconstriction.',
   'bloom':'apply','source':[{'book':'MGH Housestaff Manual','page':48}],'confusable_with':'standard target SpO2 91-96% (for patients without hypercapnia risk)'},
  {'id':'hypercapnic-resp-failure-d4','topic':T,'domain':DOM_PULM,'discipline':DIS,
   'stem':'Serious pressure-related complications of NIPPV include which three conditions?',
   'answer':'Pneumothorax, pneumocephalus, and pneumomediastinum (especially with SARS-CoV-2 pneumonia)',
   'rationale':'High NIPPV pressures can cause barotrauma; the risk is amplified with underlying lung disease causing air trapping or fragile alveoli.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Noninvasive Ventilation (NIV)','page':8}],'confusable_with':''},
  {'id':'hypercapnic-resp-failure-d5','topic':T,'domain':DOM_PULM,'discipline':DIS,
   'stem':'COPD increases the risk of respiratory failure and ICU admission; what is the range of reported invasive mechanical ventilation use in hospitalised COPD patients?',
   'answer':'Wide variation: 2.3% to 33% of hospitalised COPD patients require invasive mechanical ventilation',
   'rationale':'Wide variation reflects heterogeneity in COPD severity, available NIV infrastructure, and institutional practices; NIV reduces intubation rates.',
   'bloom':'recall','source':[{'book':'Society Guideline: Guideline   GOLD 2024 COPD Full Report','page':145}],'confusable_with':''},
  {'id':'hypercapnic-resp-failure-d6','topic':T,'domain':DOM_PULM,'discipline':DIS,
   'stem':'In a patient with hypercapnic respiratory failure from drug overdose, what specific intervention addresses the cause while providing respiratory support?',
   'answer':'Specific reversal agent (naloxone for opioids, flumazenil for benzodiazepines) alongside respiratory support; do not rely on reversal alone if prolonged hypercapnia has occurred',
   'rationale':'Drug-induced hypoventilation is a correctable cause; reversal must be coupled with ventilatory support until the drug effect fully resolves.',
   'bloom':'apply','source':[{'book':'Miller/Baby Miller','page':767}],'confusable_with':''},
  {'id':'hypercapnic-resp-failure-d7','topic':T,'domain':DOM_PULM,'discipline':DIS,
   'stem':'Normalising PaCO2 to 40 mmHg in a chronic hypercapnic COPD patient on a ventilator has what adverse consequence?',
   'answer':'Creates the equivalent of a respiratory alkalosis (overcorrection), causing cerebral vasoconstriction and alkalosis-related complications; oxygen must also be carefully controlled',
   'rationale':'Chronic CO2 retainers have renal bicarbonate compensation; rapid CO2 normalisation creates metabolic alkalosis and suppresses respiratory drive.',
   'bloom':'analyze','source':[{'book':'Morgan & Mikhail','page':1925}],'confusable_with':''},
]
kps.append({'_type':'confusable_pair',
  'topic_a':'Hypercapnic respiratory failure','topic_b':'Hypoxemic respiratory failure',
  'discriminator':'Hypercapnic: elevated PaCO2, due to inadequate alveolar ventilation (hypoventilation or dead space); treat with NIV/ventilation. Hypoxemic: low PaO2 with normal or low PaCO2, due to V/Q mismatch or shunt; treat with supplemental O2 or PEEP'})

print(f'Batch 3 KPs: {len(kps)}')
with open('data/_part4_batch3.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print('Batch 3 written OK')
