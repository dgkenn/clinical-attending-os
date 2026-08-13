import json

kps = []

# ITEM 140: Electrolyte disorders
topic = "Electrolyte disorders"
domain = "General internal medicine, preventive care & geriatrics (admission & cross-cover problems, perioperative medicine, screening & vaccination, polypharmacy & deprescribing, frailty, delirium prevention, goals of care)"
disc = "medicine"
kps += [
  {"id":"electrolyte-disorders-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"A patient has a serum K+ of 6.5 mEq/L. What is the immediate treatment priority?",
   "answer":"Hyperkalemia >6 mEq/L should always be corrected; treat with glucose, insulin, and diuresis.",
   "rationale":"Lethal arrhythmias can occur at K+ above 6 mEq/L, so immediate correction is mandatory.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1846}],"confusable_with":""},
  {"id":"electrolyte-disorders-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the first-line treatment for symptomatic hypercalcemia?",
   "answer":"Rehydration followed by brisk diuresis (urinary output 200-300 mL/h) using IV saline plus a loop diuretic.",
   "rationale":"Volume expansion increases calcium excretion; loop diuretics further accelerate renal calcium clearance.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1846}],"confusable_with":"bisphosphonates (second-line)"},
  {"id":"electrolyte-disorders-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What IV formulation and dose treats symptomatic hypocalcemia emergently?",
   "answer":"IV calcium chloride 3-5 mL of 10% solution, or calcium gluconate 10-20 mL of 10% solution.",
   "rationale":"Symptomatic hypocalcemia is a medical emergency requiring immediate ionized calcium restoration.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1846}],"confusable_with":"calcium gluconate vs. calcium chloride dosing"},
  {"id":"electrolyte-disorders-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Why must a loop diuretic not be given before adequate hydration in hypercalcemia treatment?",
   "answer":"Premature diuretic therapy before rehydration aggravates hypercalcemia by exacerbating volume depletion.",
   "rationale":"Volume depletion increases proximal tubular calcium reabsorption, worsening hypercalcemia.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1890}],"confusable_with":""},
  {"id":"electrolyte-disorders-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Severe hypermagnesemia can lead to what two life-threatening complications?",
   "answer":"Respiratory arrest and cardiac arrest.",
   "rationale":"Magnesium inhibits neuromuscular transmission and cardiac conduction at high serum levels.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1846}],"confusable_with":""},
  {"id":"electrolyte-disorders-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In malignant hyperthermia (MH), which electrolyte is treated with glucose and insulin, and why is IV calcium not indicated?",
   "answer":"Hyperkalemia in MH is treated with glucose and insulin; IV calcium salts have no useful role in MH treatment.",
   "rationale":"Massive rhabdomyolysis releases intracellular potassium; glucose/insulin shift K+ back intracellularly.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1991}],"confusable_with":""},
  {"id":"electrolyte-disorders-7","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Isolated hypomagnesemia discovered preoperatively: what should be done?",
   "answer":"Isolated hypomagnesemia should be corrected before elective procedures because of its arrhythmia risk.",
   "rationale":"Magnesium is a cofactor for Na/K-ATPase; deficiency predisposes to cardiac dysrhythmias.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1846}],"confusable_with":""},
  {"id":"electrolyte-disorders-8","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Name two electrolyte/acid-base disturbances that potentiate neuromuscular blockade.",
   "answer":"Respiratory acidosis and electrolyte disturbances such as hypocalcemia potentiate neuromuscular blockade.",
   "rationale":"Acid-base and electrolyte changes alter acetylcholine receptor sensitivity at the neuromuscular junction.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":366}],"confusable_with":""},
]

# ITEM 141: Falls & fall prevention
topic = "Falls & fall prevention in hospitalized older adults"
domain = "General internal medicine, preventive care & geriatrics (admission & cross-cover problems, perioperative medicine, screening & vaccination, polypharmacy & deprescribing, frailty, delirium prevention, goals of care)"
disc = "medicine"
kps += [
  {"id":"falls-fall-prevention-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What framework is widely used for the comprehensive geriatric assessment (CGA)?",
   "answer":"The 'Geriatric 5Ms': mind, mobility, medications, matters most, and multicomplexity.",
   "rationale":"The 5Ms systematically captures medical and psychosocial domains driving functional limitations.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":170}],"confusable_with":""},
  {"id":"falls-fall-prevention-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the greatest postoperative concern after lower extremity arthroplasty?",
   "answer":"Patient falls are the greatest postoperative concern; comprehensive fall prevention programs are required.",
   "rationale":"Regional anesthesia may transiently impair protective reflexes; early mobilization is prioritized after arthroplasty.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1313}],"confusable_with":""},
  {"id":"falls-fall-prevention-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Why are older adults at greater risk for spinal cord injury from falls than younger patients?",
   "answer":"Older adults have decreased mobility and flexibility, greater spondylosis/osteophytes, and decreased spinal canal space to accommodate cord edema.",
   "rationale":"Age-related degenerative changes narrow the spinal canal and increase susceptibility to cord injury from low-energy falls.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1341}],"confusable_with":""},
  {"id":"falls-fall-prevention-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"The incidence of spinal injury from falls in older adults is now approaching which mechanism in younger patients?",
   "answer":"Spinal cord injury from motor vehicle accidents in younger patients.",
   "rationale":"Falls have become the dominant mechanism of spinal injury in older adults due to demographic shifts.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1341}],"confusable_with":""},
  {"id":"falls-fall-prevention-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Which society has developed guidelines for prevention and treatment of postoperative delirium in older adults?",
   "answer":"The American Geriatrics Society (AGS).",
   "rationale":"Postoperative delirium and falls share overlapping risk factors; AGS guidelines address both in older surgical patients.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1504}],"confusable_with":""},
  {"id":"falls-fall-prevention-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What sources beyond the current medication list should be reviewed during medication reconciliation in older inpatients?",
   "answer":"Prior notes, discharge summaries, SNF paperwork; pharmacy dispense history; and ask about OTC meds, herbals, CBD/THC.",
   "rationale":"Undocumented medications and supplements are frequent contributors to drug interactions and fall risk.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":171}],"confusable_with":""},
]

# ITEM 142: GERD & Esophageal Disorders
topic = "GERD & Esophageal Disorders"
domain = "Internal medicine: gastroenterology & hepatology (upper & lower GI bleed, acute liver failure, cirrhosis & its complications, pancreatitis, IBD, bowel obstruction, hepatic encephalopathy)"
disc = "medicine"
kps += [
  {"id":"gerd-esophageal-disorders-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What are the surgical indications for treating gastroesophageal reflux disease?",
   "answer":"Surgery when esophagitis is refractory to medical management or results in complications: stricture, recurrent pulmonary aspiration, or Barrett esophagus.",
   "rationale":"PPIs control acid but do not prevent aspiration or structural complications requiring antireflux operations.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":928}],"confusable_with":""},
  {"id":"gerd-esophageal-disorders-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Which two esophageal motility disorders most commonly require surgical management?",
   "answer":"Achalasia and systemic sclerosis (scleroderma).",
   "rationale":"Achalasia occurs as an isolated finding; scleroderma is part of a generalized collagen-vascular disorder.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":928}],"confusable_with":"Zenker diverticulum (cricopharyngeal dysfunction)"},
  {"id":"gerd-esophageal-disorders-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Cricopharyngeal muscle dysfunction often results in which structural esophageal complication?",
   "answer":"Zenker diverticulum.",
   "rationale":"Impaired cricopharyngeal relaxation increases hypopharyngeal pressure, forcing mucosa to herniate posteriorly.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":928}],"confusable_with":"achalasia"},
  {"id":"gerd-esophageal-disorders-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"How does metoclopramide improve GERD symptoms?",
   "answer":"Metoclopramide increases lower esophageal sphincter tone, speeds gastric emptying, and lowers gastric fluid volume by enhancing acetylcholine effects on intestinal smooth muscle.",
   "rationale":"Its prokinetic action does not require vagal innervation but is abolished by anticholinergic agents.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":446}],"confusable_with":"PPIs (suppress acid but do not increase LES tone)"},
  {"id":"gerd-esophageal-disorders-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What three GI manifestations result from autonomic neuropathy in diabetics?",
   "answer":"Diarrhea, delayed gastric emptying, and esophageal motility disorders.",
   "rationale":"Vagal neuropathy impairs coordinated peristalsis and lower esophageal sphincter function.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1746}],"confusable_with":""},
  {"id":"gerd-esophageal-disorders-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In gastroparesis diagnosis, what retention findings on gastric scintigraphy confirm delayed emptying?",
   "answer":">10% retention at 4 hours and/or >60% retention at 2 hours with a radiolabeled egg meal.",
   "rationale":"Standardized scintigraphy thresholds define delayed gastric emptying.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":80}],"confusable_with":"wireless motility capsule (alternative)"},
]

# ITEM 143: Gastrointestinal bleeding
topic = "Gastrointestinal bleeding"
domain = "General internal medicine, preventive care & geriatrics (admission & cross-cover problems, perioperative medicine, screening & vaccination, polypharmacy & deprescribing, frailty, delirium prevention, goals of care)"
disc = "medicine"
kps += [
  {"id":"gastrointestinal-bleeding-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"GI bleeding from stress ulceration is common in ICU patients not receiving what?",
   "answer":"Stress ulcer prophylaxis.",
   "rationale":"Splanchnic hypoperfusion and acid exposure cause mucosal erosions; prophylaxis reduces clinically significant bleeding.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":984}],"confusable_with":""},
  {"id":"gastrointestinal-bleeding-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In cirrhotic patients who develop GI bleeding, what metabolic complication is precipitated by absorbed nitrogen from digested blood?",
   "answer":"Hepatic encephalopathy, precipitated by ammonia from blood protein breakdown in the GI tract.",
   "rationale":"Gut bacteria convert blood proteins to ammonia, which is not cleared by the failing liver.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1193}],"confusable_with":""},
  {"id":"gastrointestinal-bleeding-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Name the four major portosystemic collateral sites that develop in portal hypertension.",
   "answer":"Gastroesophageal, hemorrhoidal, periumbilical (caput medusae), and retroperitoneal.",
   "rationale":"Portal hypertension redirects blood through tributaries draining into the systemic circulation.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1193}],"confusable_with":""},
  {"id":"gastrointestinal-bleeding-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is hepatorenal syndrome, and what commonly precipitates it?",
   "answer":"Functional renal defect in cirrhosis with progressive oliguria, avid sodium retention, azotemia, intractable ascites, and high mortality; precipitated by GI bleeding, aggressive diuresis, sepsis, or major surgery.",
   "rationale":"Splanchnic vasodilation reduces effective circulating volume, triggering renal vasoconstriction without structural renal disease.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1184}],"confusable_with":"acute tubular necrosis (structural vs functional)"},
  {"id":"gastrointestinal-bleeding-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What BUN/Cr ratio is suggestive of an upper GI bleed source?",
   "answer":"BUN/Cr ratio >30 is suggestive of UGIB (LR 7.5); ratio >35 has near 100% specificity.",
   "rationale":"Upper GI blood is digested and absorbed, raising BUN without affecting creatinine.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":70}],"confusable_with":""},
  {"id":"gastrointestinal-bleeding-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Supine hypotension in acute GI bleeding indicates approximately what percentage of intravascular volume loss?",
   "answer":"Supine hypotension indicates approximately 40% intravascular volume loss.",
   "rationale":"Orthostatics detect 15% loss; supine hypotension does not occur until 40% loss because compensatory mechanisms are overwhelmed.",
   "bloom":"apply","source":[{"book":"Intern Notes / Survival Guide","page":13}],"confusable_with":"orthostatic hypotension (15% loss)"},
]

# ITEM 144: Glycemic Targets & Monitoring
topic = "Glycemic Targets & Monitoring"
domain = "Internal medicine: endocrinology (diabetes & inpatient glucose, DKA & HHS, thyroid disorders & storm, adrenal insufficiency, calcium disorders, pituitary)"
disc = "medicine"
kps += [
  {"id":"glycemic-targets-monitoring-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In critically ill patients, what is the ADA target blood glucose range for insulin therapy?",
   "answer":"Initiate insulin for persistent hyperglycemia >180 mg/dL; then target 140-180 mg/dL.",
   "rationale":"Tighter 80-110 targets increased hypoglycemia and mortality in multicenter RCTs after initial single-center benefit.",
   "bloom":"recall","source":[{"book":"Society Guideline","page":46}],"confusable_with":"80-110 mg/dL target (harmful in multicenter RCTs)"},
  {"id":"glycemic-targets-monitoring-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Why is urine glucose testing unreliable for monitoring glycemic control in patients on SGLT2 inhibitors?",
   "answer":"SGLT2 inhibitors increase urinary glucose excretion regardless of blood glucose, making urine testing falsely elevated.",
   "rationale":"SGLT2 is the primary pathway for renal glucose reabsorption; inhibition causes glucosuria at all blood glucose levels.",
   "bloom":"analyze","source":[{"book":"StatPearls: StatPearls   Glycemic Targets & Monitoring","page":15}],"confusable_with":""},
  {"id":"glycemic-targets-monitoring-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Empagliflozin should be withheld for at least how long before major surgery?",
   "answer":"At least 3 days before major surgery or procedures associated with prolonged fasting.",
   "rationale":"Continued SGLT2 use perioperatively increases risk of euglycemic DKA during fasting/stress states.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Glycemic Targets & Monitoring","page":10}],"confusable_with":""},
  {"id":"glycemic-targets-monitoring-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"When dapagliflozin and digoxin are co-administered, what monitoring is required?",
   "answer":"Therapeutic drug monitoring of digoxin is required; dapagliflozin increases digoxin Cmax by 36% and AUC by 20%.",
   "rationale":"Digoxin has a narrow therapeutic index; SGLT2-mediated increases in exposure raise toxicity risk.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Glycemic Targets & Monitoring","page":15}],"confusable_with":""},
  {"id":"glycemic-targets-monitoring-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"A patient on canagliflozin is also prescribed rifampin. What adjustment may be needed?",
   "answer":"Increasing the canagliflozin dose may be considered; rifampin (a UGT inducer) reduces canagliflozin AUC.",
   "rationale":"UGT enzymes metabolize canagliflozin; induction accelerates clearance and may diminish glycemic effectiveness.",
   "bloom":"analyze","source":[{"book":"StatPearls: StatPearls   Glycemic Targets & Monitoring","page":15}],"confusable_with":""},
  {"id":"glycemic-targets-monitoring-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Before initiating canagliflozin or ertugliflozin, what risk factors for lower-limb amputation must be assessed?",
   "answer":"Peripheral vascular disease, history of amputation, neuropathy, elevated HbA1c at baseline, and diabetic foot ulcers.",
   "rationale":"These SGLT2 inhibitors carry FDA warning for increased lower-limb amputation risk in patients with existing vascular complications.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Glycemic Targets & Monitoring","page":16}],"confusable_with":""},
]

# ITEM 145: Glycemic management in hospitalized patients
topic = "Glycemic management in hospitalized patients"
domain = "General internal medicine, preventive care & geriatrics (admission & cross-cover problems, perioperative medicine, screening & vaccination, polypharmacy & deprescribing, frailty, delirium prevention, goals of care)"
disc = "medicine"
kps += [
  {"id":"glycemic-mgmt-hosp-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What are the inpatient glycemic targets for a non-ICU floor patient?",
   "answer":"Fasting 100-140 mg/dL, random <180 mg/dL.",
   "rationale":"These targets balance hyperglycemia harm against the higher inpatient hypoglycemia risk.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":183}],"confusable_with":"ICU target (140-180 mg/dL)"},
  {"id":"glycemic-mgmt-hosp-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"When should an insulin drip be used in the ICU, and what overlap rule applies when transitioning to SC insulin?",
   "answer":"Use insulin drip if BG >180 x2 and anticipated ICU stay >3 days; always overlap with SC insulin 2-3 hours before stopping the drip.",
   "rationale":"Subcutaneous overlap prevents rebound hyperglycemia from the delay in onset after IV discontinuation.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":183}],"confusable_with":""},
  {"id":"glycemic-mgmt-hosp-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the standard weight-based starting dose for SC insulin in hospitalized patients?",
   "answer":"0.4 units/kg/day: half as long-acting basal, the other half split into 3 prandial doses with meals.",
   "rationale":"Weight-based dosing provides a reasonable starting point; inpatient doses are typically 80% of home doses.",
   "bloom":"recall","source":[{"book":"Intern Notes / Survival Guide","page":45}],"confusable_with":""},
  {"id":"glycemic-mgmt-hosp-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"For a Type 1 diabetic who is NPO, what insulin rule applies?",
   "answer":"Type 1 diabetics ALWAYS need basal insulin even when NPO; discontinue bolus insulin but continue basal.",
   "rationale":"Type 1 DM has no endogenous insulin; withholding basal entirely causes DKA even without oral intake.",
   "bloom":"apply","source":[{"book":"Intern Notes / Survival Guide","page":45}],"confusable_with":"Type 2 DM NPO management"},
  {"id":"glycemic-mgmt-hosp-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What KDIGO glycemic target is suggested in critically ill patients?",
   "answer":"KDIGO 2012 suggests insulin therapy targeting plasma glucose 110-149 mg/dL in critically ill patients.",
   "rationale":"Stress hyperglycemia worsens renal tubular injury; KDIGO targets are slightly tighter than ADA's 140-180 mg/dL.",
   "bloom":"recall","source":[{"book":"Society Guideline: Guideline   KDIGO 2012 AKI","page":46}],"confusable_with":"ADA ICU target (140-180 mg/dL)"},
  {"id":"glycemic-mgmt-hosp-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Which classes of oral antidiabetic agents should be held during hospitalization?",
   "answer":"Hold oral agents and GLP-1 agonists; SGLT2 inhibitors may be continued with stable renal function but carry increased euglycemic DKA risk.",
   "rationale":"Oral agents risk aspiration, lactic acidosis, hemodynamic instability; SGLT2 inhibitors risk euglycemic DKA in fasting ill patients.",
   "bloom":"apply","source":[{"book":"Intern Notes / Survival Guide","page":45}],"confusable_with":""},
]

# ITEM 146: Goals of care
topic = "Goals of care, advance directives & serious illness communication"
domain = "General internal medicine, preventive care & geriatrics (admission & cross-cover problems, perioperative medicine, screening & vaccination, polypharmacy & deprescribing, frailty, delirium prevention, goals of care)"
disc = "medicine"
kps += [
  {"id":"goals-of-care-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the 'surprise question' trigger for initiating a serious illness conversation?",
   "answer":"'Would I be surprised if this patient died in the next year?' - if no, initiate a serious illness conversation.",
   "rationale":"The surprise question reliably identifies patients with limited prognosis for whom goals-of-care discussions are warranted.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":166}],"confusable_with":""},
  {"id":"goals-of-care-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is a time-limited trial in serious illness care?",
   "answer":"An agreement to use certain medical therapies over a defined period to see if the patient improves or deteriorates according to agreed-on clinical outcomes.",
   "rationale":"Time-limited trials address prognostic uncertainty and allow families to evaluate treatment before committing indefinitely.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":873}],"confusable_with":"comfort measures only (irreversible commitment)"},
  {"id":"goals-of-care-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Palliative care consultations fall into which two broad categories?",
   "answer":"Goals-of-care consults and symptom management consults.",
   "rationale":"Goals-of-care consults align treatment with patient values; symptom management consults address pain, dyspnea, and distressing symptoms.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":866}],"confusable_with":"hospice (end-of-life only) vs. palliative care (any stage)"},
  {"id":"goals-of-care-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What average cost reduction per patient has been demonstrated with palliative care consult services?",
   "answer":"An average decrease of $15,000 per patient with similar duration of survival.",
   "rationale":"Palliative care aligns care with patient preferences, reducing unwanted interventions and resource utilization.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":864}],"confusable_with":""},
  {"id":"goals-of-care-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the current policy stance on automatically suspending DNR orders during surgery?",
   "answer":"Policies automatically suspending DNR orders are inappropriate; the patient's goals and advance directives should guide perioperative resuscitation decisions.",
   "rationale":"Patients retain the right to limit resuscitation in the OR; blanket suspension violates patient autonomy.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":876}],"confusable_with":""},
  {"id":"goals-of-care-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In sepsis guidelines, what is the rationale for early goals-of-care discussions?",
   "answer":"To determine which treatments are acceptable and which are not desired; advance care planning improves concordance between treatment and patient values.",
   "rationale":"Sepsis carries high multi-organ failure and mortality risk; early conversations prevent unwanted aggressive interventions.",
   "bloom":"analyze","source":[{"book":"Society Guideline","page":49}],"confusable_with":""},
]

# ITEM 147: HFrEF
topic = "Heart Failure with Reduced Ejection Fraction (HFrEF)"
domain = "Internal medicine: cardiology (ACS, stable & unstable angina, heart failure, brady/tachyarrhythmias, valvular disease, hypertension & emergencies, lipids, syncope)"
disc = "medicine"
kps.append({"_type":"illness_script","topic":topic,"discipline":disc,
  "enabling_conditions":"Ischemic cardiomyopathy, dilated cardiomyopathy, prior MI, hypertension, valvular disease",
  "pathophysiology":"Reduced LVEF impairs cardiac output; neurohormonal activation (RAAS, sympathetic) causes maladaptive remodeling",
  "time_course":"Chronic progressive; acute decompensation episodic",
  "key_features":"Dyspnea, orthopnea, edema, elevated BNP, LVEF <=40% on echo",
  "consequence_if_missed":"Progressive pump failure, sudden cardiac death from arrhythmia"})
kps += [
  {"id":"hfref-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What biomarker distinguishes heart failure from other causes of dyspnea?",
   "answer":"BNP (brain natriuretic peptide); elevation is associated with impaired ventricular function.",
   "rationale":"BNP is released from myocardium under wall stress; elevation correlates with ventricular dysfunction severity.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":659}],"confusable_with":"troponin (myocyte necrosis) vs BNP (wall stress)"},
  {"id":"hfref-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"At what serum digoxin concentration does the risk of death increase significantly in HF patients?",
   "answer":"Serum digoxin concentration >=1.2 ng/mL is associated with significantly higher mortality.",
   "rationale":"Digoxin has a narrow therapeutic index; concentrations above 1.2 ng/mL increase arrhythmia and mortality risk.",
   "bloom":"recall","source":[{"book":"Society Guideline: Guideline   ACC AHA 2022 Heart Failure","page":55}],"confusable_with":""},
  {"id":"hfref-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What digoxin dose should be used initially in patients >70 years or with impaired renal function?",
   "answer":"Low doses of 0.125 mg daily or every other day should be used initially.",
   "rationale":"Digoxin is renally cleared; reduced clearance in the elderly and CKD increases toxicity risk.",
   "bloom":"apply","source":[{"book":"Society Guideline: Guideline   ACC AHA 2022 Heart Failure","page":55}],"confusable_with":""},
  {"id":"hfref-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"For patients with HFmrEF (LVEF 41-49%), what treatment approach is recommended?",
   "answer":"It may be reasonable to treat lower-end HFmrEF with GDMT used for HFrEF; repeat LVEF evaluation is needed.",
   "rationale":"No prospective RCTs exist for HFmrEF; post-hoc analyses suggest lower-end HFmrEF responds like HFrEF.",
   "bloom":"analyze","source":[{"book":"Society Guideline: Guideline   ACC AHA 2022 Heart Failure","page":64}],"confusable_with":"HFpEF (LVEF >=50%)"},
  {"id":"hfref-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What did a meta-analysis of 4 ARB trials in HFpEF (n=7694) show regarding mortality?",
   "answer":"ARBs showed no benefit on cardiovascular mortality (HR 1.02), all-cause mortality (HR 1.02), or HF hospitalization (HR 0.92) in HFpEF.",
   "rationale":"RAAS blockade reduces mortality in HFrEF but does not translate to preserved-EF HF.",
   "bloom":"analyze","source":[{"book":"Society Guideline: Guideline   ACC AHA 2022 Heart Failure","page":68}],"confusable_with":"ARBs in HFrEF (beneficial)"},
  {"id":"hfref-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"At what stage of HF should palliative care be integrated?",
   "answer":"Across all stages of HF, starting early in the course of illness.",
   "rationale":"Palliative care addresses symptom burden, communication, and advance planning throughout the disease trajectory.",
   "bloom":"recall","source":[{"book":"Society Guideline: Guideline   ACC AHA 2022 Heart Failure","page":103}],"confusable_with":""},
]

# ITEM 148: Hemoptysis
topic = "Hemoptysis: Evaluation and Management"
domain = "Internal medicine: pulmonology (COPD, asthma, pulmonary embolism, pneumonia, ILD, pleural effusion, pneumothorax, hypoxemic & hypercapnic respiratory failure, OSA)"
disc = "medicine"
kps += [
  {"id":"hemoptysis-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What clinical findings warrant chest radiography in a patient with airway disease and hemoptysis?",
   "answer":"Hemoptysis, weight loss, clubbing, inspiratory crackles, significant hypoxemia, or moderate-severe airflow obstruction.",
   "rationale":"These findings suggest structural or parenchymal lung disease requiring imaging to identify the bleeding source.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Angioedema  classification & management","page":10}],"confusable_with":""},
  {"id":"hemoptysis-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In a non-smoking patient with irreversible airflow obstruction and hemoptysis, which genetic cause of emphysema should be ruled out?",
   "answer":"Homozygous alpha-1 antitrypsin deficiency.",
   "rationale":"Alpha-1 antitrypsin deficiency causes early-onset panacinar emphysema with bronchiectasis that can produce hemoptysis.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Angioedema  classification & management","page":10}],"confusable_with":""},
  {"id":"hemoptysis-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In a patient with moderate-severe asthma, elevated serum IgE, and hemoptysis, which specific pulmonary syndrome should be considered?",
   "answer":"Allergic bronchopulmonary aspergillosis (ABPA).",
   "rationale":"ABPA causes eosinophilic bronchiectasis that can produce hemoptysis; elevated IgE and anti-Aspergillus antibodies are diagnostic markers.",
   "bloom":"analyze","source":[{"book":"StatPearls: StatPearls   Angioedema  classification & management","page":10}],"confusable_with":"eosinophilic granulomatosis with polyangiitis"},
  {"id":"hemoptysis-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Thoracic neuroendocrine tumors span a spectrum from which well-differentiated to high-grade type?",
   "answer":"From well-differentiated typical carcinoids to high-grade large cell neuroendocrine carcinomas.",
   "rationale":"Carcinoid tumors are an important endobronchial cause of hemoptysis; spectrum understanding guides prognosis.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Carcinoid Tumors & Neuroendocrine Tumors (NETs)","page":1}],"confusable_with":"small cell lung cancer"},
]

# ITEM 149: Hepatic Encephalopathy
topic = "Hepatic Encephalopathy"
domain = "Internal medicine: gastroenterology & hepatology (upper & lower GI bleed, acute liver failure, cirrhosis & its complications, pancreatitis, IBD, bowel obstruction, hepatic encephalopathy)"
disc = "medicine"
kps.append({"_type":"illness_script","topic":topic,"discipline":disc,
  "enabling_conditions":"Cirrhosis, portal hypertension, acute liver failure; precipitants: GI bleeding, infection, high protein intake, hypokalemia, constipation, hepatotoxic medications",
  "pathophysiology":"Accumulation of neurotoxins (ammonia, short-chain fatty acids) from impaired hepatic clearance; elevated ICP in acute liver failure",
  "time_course":"Episodic in cirrhosis; continuous or rapidly progressive in acute liver failure",
  "key_features":"Mental status alterations, asterixis, hyperreflexia or inverted plantar reflex, symmetric high-voltage slow-wave EEG activity",
  "consequence_if_missed":"Progression to coma; cerebral edema and herniation in acute liver failure"})
kps += [
  {"id":"hepatic-encephalopathy-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What characteristic EEG pattern is associated with hepatic encephalopathy?",
   "answer":"Symmetric high-voltage, slow-wave EEG activity.",
   "rationale":"Ammonia and neurotoxins impair neuronal metabolism, producing generalized slow-wave activity.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1200}],"confusable_with":"triphasic waves vs generalized slowing"},
  {"id":"hepatic-encephalopathy-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Name four precipitants of hepatic encephalopathy in cirrhotic patients.",
   "answer":"GI bleeding, increased dietary protein intake, hypokalemic alkalosis (from vomiting or diuresis), infections, worsening liver function, and hepatotoxic drugs.",
   "rationale":"Each factor either increases ammonia load or impairs neuronal function; correcting precipitants is first-line management.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1184}],"confusable_with":""},
  {"id":"hepatic-encephalopathy-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"TIPS reduces portal hypertension but increases the risk of what complication?",
   "answer":"Hepatic encephalopathy increases after TIPS, because portal blood bypasses hepatic detoxification.",
   "rationale":"Gut-derived ammonia and other toxins reach the systemic circulation via the shunt without hepatic clearance.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1194}],"confusable_with":""},
  {"id":"hepatic-encephalopathy-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is currently the most common cause of cirrhosis in the United States?",
   "answer":"Nonalcoholic steatohepatitis (NASH), accompanying the rise in morbid obesity, has overtaken chronic alcohol abuse.",
   "rationale":"Metabolic syndrome-driven hepatic steatosis and inflammation is now the leading cause of cirrhosis in the US.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1191}],"confusable_with":""},
  {"id":"hepatic-encephalopathy-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In patients with significant liver disease, which two volatile anesthetics preserve hepatic blood flow?",
   "answer":"Isoflurane and sevoflurane preserve hepatic blood flow and oxygen delivery.",
   "rationale":"Halothane reduces hepatic blood flow more than isoflurane/sevoflurane and carries hepatotoxicity risk.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1183}],"confusable_with":"halothane (hepatotoxic)"},
  {"id":"hepatic-encephalopathy-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What happens to succinylcholine duration in severe liver disease?",
   "answer":"Duration may be prolonged due to reduced pseudocholinesterase, though rarely of clinical consequence.",
   "rationale":"Pseudocholinesterase is synthesized by the liver; severe disease reduces production and slows succinylcholine metabolism.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1201}],"confusable_with":""},
]

# ITEM 150: Hypercalcemia
topic = "Hypercalcemia"
domain = "Internal medicine: endocrinology (diabetes & inpatient glucose, DKA & HHS, thyroid disorders & storm, adrenal insufficiency, calcium disorders, pituitary)"
disc = "medicine"
kps.append({"_type":"illness_script","topic":topic,"discipline":disc,
  "enabling_conditions":"Primary hyperparathyroidism, malignancy (PTHrP), sarcoidosis, vitamin D toxicity, Paget disease, thiazide diuretics, milk-alkali syndrome",
  "pathophysiology":"Excess calcium impairs neuromuscular transmission, cardiac conduction, and renal tubular function",
  "time_course":"Subacute to chronic; hypercalcemia of malignancy often acutely severe",
  "key_features":"Bones, stones, groans, moans; shortened QT on ECG; serum calcium >10.5 mg/dL",
  "consequence_if_missed":"Cardiac arrhythmias, renal failure, pancreatitis, altered mental status, death"})
kps += [
  {"id":"hypercalcemia-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What calcium level goal should be achieved before elective surgery for hyperparathyroidism-related hypercalcemia?",
   "answer":"Hydration with normal saline and furosemide diuresis should decrease serum calcium to <14 mg/dL (3.5 mmol/L) before proceeding.",
   "rationale":"Calcium >14 mg/dL increases arrhythmia risk and impairs neuromuscular function perioperatively.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1232}],"confusable_with":""},
  {"id":"hypercalcemia-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In hypercalcemia of malignancy refractory to IV saline and loop diuretics, what additional agents are used?",
   "answer":"IV bisphosphonates (pamidronate or etidronate); if insufficient: plicamycin, glucocorticoids, calcitonin, or dialysis.",
   "rationale":"Malignancy hypercalcemia is often PTHrP-driven and requires osteoclast inhibition beyond fluid therapy.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1232}],"confusable_with":""},
  {"id":"hypercalcemia-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Why should hypoventilation be avoided in a patient with hypercalcemia?",
   "answer":"Hypoventilation causes respiratory acidosis, which increases ionized calcium and worsens hypercalcemia.",
   "rationale":"Acidosis shifts calcium off albumin, increasing ionized (biologically active) calcium.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1232}],"confusable_with":""},
  {"id":"hypercalcemia-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"During the anhepatic phase of liver transplant, why is periodic calcium chloride given?",
   "answer":"Large citrate load from blood products is not metabolized, causing hypocalcemia and myocardial depression; 1 g CaCl2 given guided by ionized calcium.",
   "rationale":"Citrate chelates ionized calcium; without hepatic metabolism, severe hypocalcemia develops during massive transfusion.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1212}],"confusable_with":""},
  {"id":"hypercalcemia-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What cancer-associated mechanism causes hypercalcemia without bone metastases?",
   "answer":"Ectopic secretion of PTHrP (parathyroid hormone-related protein) by tumor cells causes humoral hypercalcemia of malignancy.",
   "rationale":"PTHrP binds PTH receptors, increasing bone resorption and renal calcium reabsorption without bony involvement.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1889}],"confusable_with":"primary hyperparathyroidism (elevated PTH, not PTHrP)"},
]
kps.append({"_type":"confusable_pair","topic_a":"Primary hyperparathyroidism","topic_b":"Humoral hypercalcemia of malignancy",
  "discriminator":"Both cause elevated ionized Ca2+; PTH is elevated in primary hyperparathyroidism and suppressed in malignancy where PTHrP is the driver"})

# ITEM 151: HHS
topic = "Hyperosmolar Hyperglycemic State (HHS)"
domain = "Internal medicine: endocrinology (diabetes & inpatient glucose, DKA & HHS, thyroid disorders & storm, adrenal insufficiency, calcium disorders, pituitary)"
disc = "medicine"
kps.append({"_type":"illness_script","topic":topic,"discipline":disc,
  "enabling_conditions":"Type 2 diabetes, older patients with renal/cardiac comorbidities; triggers: infection, medication non-adherence, steroids, antipsychotics",
  "pathophysiology":"Residual insulin prevents ketosis but cannot lower glucose; severe hyperglycemia causes osmotic diuresis and profound dehydration",
  "time_course":"Days to weeks of gradual worsening",
  "key_features":"Glucose >600 mg/dL, serum osmolality >320 mOsm/kg, minimal ketonemia, pH >7.30, HCO3- >15 mEq/L, altered mental status",
  "consequence_if_missed":"Mortality 15-20%; cerebral edema or osmotic demyelination if corrected too rapidly"})
kps += [
  {"id":"hhs-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the calculated serum osmolality formula and the diagnostic threshold for HHS?",
   "answer":"Osmolality = 2[Na] + glucose/18 + BUN/2.8; diagnosis requires osmolality >320 mOsm/kg.",
   "rationale":"Calculated osmolality reflects the combined osmotic load; >320 indicates severe hyperosmolarity.",
   "bloom":"apply","source":[{"book":"Curated Units","page":0}],"confusable_with":"DKA (osmolality elevated but pH <7.30)"},
  {"id":"hhs-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Why does HHS not typically feature significant ketoacidosis?",
   "answer":"Enough residual insulin is present to prevent ketone body formation, but insufficient to lower glucose.",
   "rationale":"Type 2 DM retains partial insulin secretion that blunts lipolysis and ketogenesis while osmotic diuresis progresses.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1219}],"confusable_with":"DKA (near-zero insulin leads to ketosis)"},
  {"id":"hhs-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the safe rate of glucose reduction in HHS and why is faster correction dangerous?",
   "answer":"Target 25-50 mg/dL/hour; faster reduction risks osmotic cerebral edema and stroke.",
   "rationale":"Neurons adapt to hyperosmolarity by generating idiogenic osmoles; rapid osmolality drop causes water influx into brain cells.",
   "bloom":"analyze","source":[{"book":"Curated Units","page":0}],"confusable_with":"DKA (can correct glucose somewhat faster)"},
  {"id":"hhs-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the mortality rate of treated HHS compared to DKA?",
   "answer":"HHS mortality is 15-20% even with treatment, substantially higher than DKA mortality of 0.2-2.5%.",
   "rationale":"HHS occurs in older patients with more comorbidities; dehydration and precipitating illness drive higher mortality.",
   "bloom":"recall","source":[{"book":"Curated Units","page":0}],"confusable_with":""},
  {"id":"hhs-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Net water movement between compartments follows what principle in the setting of HHS?",
   "answer":"Net water movement occurs from the relatively hypoosmolar compartment to the relatively hyperosmolar compartment.",
   "rationale":"Osmotic equilibrium is maintained across cell membranes; hyperglycemia draws water from cells into the ECF.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1851}],"confusable_with":""},
]
kps.append({"_type":"confusable_pair","topic_a":"Hyperosmolar Hyperglycemic State (HHS)","topic_b":"Diabetic Ketoacidosis (DKA)",
  "discriminator":"HHS: glucose >600, osmolality >320, pH >7.30, minimal ketones, Type 2 DM, high mortality 15-20%. DKA: glucose 250-600, pH <7.30, ketonemia, often Type 1 DM, mortality 0.2-2.5%"})

# ITEM 152: Hypertension
topic = "Hypertension: Diagnosis and Chronic Management"
domain = "Internal medicine: cardiology (ACS, stable & unstable angina, heart failure, brady/tachyarrhythmias, valvular disease, hypertension & emergencies, lipids, syncope)"
disc = "medicine"
kps += [
  {"id":"hypertension-diag-mgmt-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What standard medical therapy is indicated for intractable heart failure before transplantation?",
   "answer":"ACE inhibitors (or ARBs), beta-blockers (usually carvedilol), diuretics, vasodilators; many receive ICD/cardiac pacing.",
   "rationale":"GDMT reduces neurohormonal activation and improves survival even in end-stage HF.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":765}],"confusable_with":""},
  {"id":"hypertension-diag-mgmt-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the perioperative recommendation regarding ACE inhibitors and ARBs?",
   "answer":"Holding ACE inhibitors and ARBs perioperatively may be considered because continuation is associated with increased intraoperative hypotension.",
   "rationale":"RAAS blockade blunts compensatory vasoconstriction during anesthetic vasodilation and blood loss.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":486}],"confusable_with":"beta-blockers (should be continued perioperatively)"},
  {"id":"hypertension-diag-mgmt-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Abrupt discontinuation of beta-blockers for 24-48 hours triggers what syndrome?",
   "answer":"Beta-blocker withdrawal syndrome: rebound hypertension, tachycardia, and angina, caused by upregulation of beta-adrenergic receptors.",
   "rationale":"Chronic beta-blockade causes receptor upregulation; sudden discontinuation creates a hyperadrenergic state.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":399}],"confusable_with":""},
  {"id":"hypertension-diag-mgmt-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Chronic hypertension alters cerebral autoregulation - what is the clinical implication for anesthesia?",
   "answer":"Chronic hypertension shifts the cerebral autoregulation curve rightward; 'normal' blood pressures may cause cerebral ischemia in these patients.",
   "rationale":"The lower limit of autoregulation is elevated; patients are less tolerant of intraoperative hypotension.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":351}],"confusable_with":""},
]

with open("data/kp_batch1_out.json", "w", encoding="utf-8") as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)

print("Items:", len(kps))
