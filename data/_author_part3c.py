"""Author KPs for topics 122-131 (slice items 23-32)."""
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

kps = []

# ── 122: Dementia: recognition, evaluation & inpatient management ─────────────
T = "Dementia: recognition, evaluation & inpatient management"
DOM = "General internal medicine, preventive care & geriatrics (admission & cross-cover problems, perioperative medicine, screening & vaccination, polypharmacy & deprescribing, frailty, delirium prevention, goals of care)"
DISC = "medicine"

kps += [
  {"id":"dementia-inpatient-d1","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What three key elements are required for clinical diagnosis of Charles Bonnet syndrome (complex visual hallucinations) in a patient without cognitive decline?",
   "answer":"(1) Presence of complex visual hallucinations, (2) documented visual impairment, and (3) absence of psychiatric or cognitive disease.",
   "rationale":"Charles Bonnet syndrome occurs in visually impaired patients whose brain generates hallucinations to compensate for reduced visual input; patients retain insight and are not psychotic.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Approach to Anaphylaxis","page":5}],
   "confusable_with":"delirium (has cognitive changes), psychosis (no insight)"},

  {"id":"dementia-inpatient-d2","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"How does delirium differ from dementia in terms of onset, attention, and consciousness?",
   "answer":"Delirium: acute onset (hours-days), fluctuating course, inattention is cardinal feature, altered level of consciousness; Dementia: insidious onset over months-years, stable (not fluctuating), attention relatively preserved until late.",
   "rationale":"The CAM (Confusion Assessment Method) requires acute onset + inattention + either disorganized thinking or altered consciousness for delirium diagnosis; dementia lacks these acute/fluctuating features.",
   "bloom":"analyze",
   "source":[{"book":"StatPearls","page":1}],
   "confusable_with":"delirium superimposed on dementia (both present)"},

  {"id":"dementia-inpatient-d3","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"In the elderly, benzodiazepines should be used with what caution and what alternative is preferred?",
   "answer":"Benzodiazepines should be used with caution due to their tendency to cause and/or worsen delirium in elderly patients; if given, doses should be significantly reduced. Non-pharmacological strategies or low-dose antipsychotics are preferred for delirium.",
   "rationale":"The elderly have reduced benzodiazepine metabolism, increased sensitivity to CNS depressants, and altered GABAergic neurotransmission; benzodiazepines paradoxically worsen agitation and perpetuate delirium.",
   "bloom":"apply",
   "source":[{"book":"Miller/Baby Miller","page":674}],
   "confusable_with":"alcohol withdrawal delirium (where benzodiazepines are indicated)"},

  {"id":"dementia-inpatient-d4","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Emergence agitation in adult patients under anesthesia: what is its incidence and key distinguishing feature from delirium?",
   "answer":"Emergence agitation in adults occurs in only 3-5% (much lower than in children 2-4 years where it is most frequent); it typically resolves quickly and is followed by uneventful recovery, unlike sustained delirium.",
   "rationale":"Emergence agitation is a transient state of motor excitement during awakening from anesthesia; it resolves as anesthetic concentrations fall, unlike postoperative delirium which persists for days.",
   "bloom":"recall",
   "source":[{"book":"Miller/Baby Miller","page":736}],
   "confusable_with":"postoperative delirium (more sustained)"},

  {"id":"dementia-inpatient-d5","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"In preoperative evaluation of a patient with dementia, what critical assessment elements guide anesthesia planning?",
   "answer":"Assess cognitive baseline, medication reconciliation (especially anticholinergics/benzodiazepines), frailty assessment, goals of care discussion, and risk of postoperative delirium and POCD.",
   "rationale":"Dementia patients have reduced cognitive reserve, making them highly vulnerable to postoperative delirium; minimizing neurotoxic medications, regional techniques, and early mobilization are priority interventions.",
   "bloom":"apply",
   "source":[{"book":"Miller/Baby Miller","page":219}],
   "confusable_with":""},

  {"id":"dementia-inpatient-d6","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Prehabilitation in patients with dementia planning elective surgery focuses on which specific goals?",
   "answer":"Improved physical fitness, dietary/nutritional optimization, antistress interventions for resilience and self-efficacy, and cessation of harmful substances.",
   "rationale":"Prehabilitation improves cardiorespiratory reserve and nutritional status before surgery, which in dementia patients is particularly important given their baseline frailty and reduced physiological reserve.",
   "bloom":"recall",
   "source":[{"book":"Miller/Baby Miller","page":241}],
   "confusable_with":""},

  {"id":"dementia-inpatient-d7","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"For a patient with implanted cardiac devices (PPM/ICD) who has dementia and presents for surgery, what critical perioperative considerations must be addressed?",
   "answer":"Device type (PPM, ICD, CRT), programming, dependency status, magnet effects, electrosurgery interference risk, and post-operative ICD reprogramming must all be assessed pre-operatively.",
   "rationale":"Dementia patients may not be able to report symptoms or pacemaker dependency; electrosurgery can inhibit pacemakers or trigger inappropriate ICD shocks; device reprogramming ensures appropriate perioperative function.",
   "bloom":"apply",
   "source":[{"book":"Stanford CA-1","page":88}],
   "confusable_with":""},
]

# ── 123: Diabetic Kidney Disease ─────────────────────────────────────────────
T = "Diabetic Kidney Disease"
DOM = "Internal medicine: nephrology, fluids & electrolytes"
DISC = "medicine"

kps += [
  {"id":"diabetic-kidney-d1","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What is the sequential pattern of kidney involvement in type 1 diabetes and by what age does evidence of kidney disease typically appear?",
   "answer":"Diabetic kidney dysfunction manifests first by proteinuria and later by elevated serum creatinine; most type 1 diabetics have evidence of kidney disease by 30 years of age.",
   "rationale":"Chronic hyperglycemia causes glycosylation of basement membrane proteins, mesangial expansion, and glomerulosclerosis; microalbuminuria precedes macroalbuminuria and GFR decline by years.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1221}],
   "confusable_with":""},

  {"id":"diabetic-kidney-d2","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"In surgical patients on insulin infusion, what intraoperative glucose target is recommended and what electrolyte supplement is important to add to IV fluids?",
   "answer":"Target intraoperative glucose 85-180 mg/dL; add ~20 mEq KCl to each liter of maintenance fluid because insulin drives potassium intracellularly causing hypokalemia.",
   "rationale":"Insulin activates Na-K-ATPase, shifting potassium intracellularly; without potassium supplementation, insulin infusion in diabetic patients can cause dangerous hypokalemia during surgery.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1223}],
   "confusable_with":""},

  {"id":"diabetic-kidney-d3","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Diabetic patients have impaired renal prostaglandin-mediated vasodilation. What drug class is particularly dangerous in such patients and what injury does it cause?",
   "answer":"NSAIDs — they block renal prostaglandins needed for afferent arteriolar vasodilation in states of reduced renal perfusion, causing hemodynamically-mediated AKI in patients with diabetic nephropathy.",
   "rationale":"Diabetic nephropathy reduces GFR reserve; in volume depletion or low cardiac output states, renal prostaglandins maintain afferent arteriolar tone — NSAIDs remove this protective mechanism.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":315}],
   "confusable_with":"contrast nephropathy"},

  {"id":"diabetic-kidney-d4","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"During the oliguric phase of intrinsic AKI in a diabetic patient, what typically follows and what volume monitoring challenges arise?",
   "answer":"Oliguria typically lasts ~2 weeks then is followed by a diuretic phase with progressive increase in urinary output, which is usually absent in nonoliguric kidney failure; large urinary outputs during this phase risk volume depletion.",
   "rationale":"The diuretic phase represents tubular recovery before concentrating ability returns; the large volume of dilute urine can cause severe hypovolemia and electrolyte losses if not replaced appropriately.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1107}],
   "confusable_with":""},

  {"id":"diabetic-kidney-d5","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Poorly controlled diabetes is associated with what preoperative hemoglobin A1c threshold that increases surgical complications?",
   "answer":"Abnormally elevated HbA1c identifies patients with poor long-term glucose control who are more likely to have hyperglycemia on the day of surgery and face increased complications, adverse outcomes, and costs.",
   "rationale":"HbA1c reflects average glycemia over 3 months; poor control means persistent perioperative hyperglycemia impairing wound healing, increasing infection risk, and worsening outcomes from end-organ complications.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1220}],
   "confusable_with":""},

  {"id":"diabetic-kidney-d6","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Hyperphosphatemia in CKD and diabetic kidney disease is treated with what class of agents?",
   "answer":"Phosphate-binding antacids such as aluminum hydroxide or aluminum carbonate are used to treat hyperphosphatemia; calcium-based binders are also used.",
   "rationale":"Dialysis is insufficient to remove the daily phosphate burden from diet; oral phosphate binders prevent intestinal absorption of dietary phosphate, lowering serum phosphate to reduce vascular calcification risk.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1895}],
   "confusable_with":""},

  {"id":"diabetic-kidney-d7","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What are the four major categories of chronic kidney disease etiology (not acute) and which are most common in the general population?",
   "answer":"Hypertensive nephrosclerosis, diabetic nephropathy (most common causes), chronic glomerulonephritis, and polycystic kidney disease.",
   "rationale":"Diabetes and hypertension together account for approximately 70% of ESRD in the US; understanding etiology guides selection of nephroprotective therapy (RAAS inhibition for both).",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1107}],
   "confusable_with":""},
]

# ── 124: Diabetic Macrovascular Complications & CV Risk Reduction ─────────────
T = "Diabetic Macrovascular Complications & CV Risk Reduction"
DOM = "Internal medicine: endocrinology (diabetes & inpatient glucose, DKA & HHS, thyroid disorders & storm, adrenal insufficiency, calcium disorders, pituitary)"
DISC = "medicine"

kps += [
  {"id":"dm-macrovascular-d1","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What combined prevalence of total diabetes and impaired fasting glucose exists in adults over age 20 in the US, and what three major complications from diabetes does this population face?",
   "answer":"Combined prevalence ~14.4%; diabetes is the leading cause of blindness, ESRD, and nontraumatic amputations; type 2 accounts for >90% with 70-80% chance of premature death.",
   "rationale":"Macrovascular (atherosclerosis) and microvascular (retinopathy, nephropathy, neuropathy) complications from chronic hyperglycemia explain these endpoints; CV risk reduction is the primary mortality target.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   JNC7 2003 Hypertension Full Report","page":52}],
   "confusable_with":""},

  {"id":"dm-macrovascular-d2","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"The three major life-threatening acute complications of diabetes and its treatment are what?",
   "answer":"Diabetic ketoacidosis (DKA), hyperosmolar nonketotic coma (HHS), and hypoglycemia — in addition to sepsis and other acute medical problems worsened by diabetes.",
   "rationale":"Each represents a distinct emergency: DKA from insulin deficiency + ketogenesis; HHS from profound hyperglycemia without ketosis; hypoglycemia from excessive insulin relative to carbohydrate intake or renal impairment.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1218}],
   "confusable_with":""},

  {"id":"dm-macrovascular-d3","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"ACEI added to conventional therapy in diabetic patients reduces combined MI, stroke, and CVD death by approximately what percentage, and by how much does it reduce stroke alone?",
   "answer":"ACEI added to conventional therapy reduces combined MI/stroke/CVD death by ~25% and stroke by ~33% compared to placebo plus conventional therapy.",
   "rationale":"ACE inhibitors provide both hemodynamic (BP lowering) and non-hemodynamic (reduction in angiotensin II-mediated vascular inflammation) cardioprotection in diabetic patients.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   JNC7 2003 Hypertension Full Report","page":53}],
   "confusable_with":""},

  {"id":"dm-macrovascular-d4","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What are the diagnostic criteria for diabetes mellitus and what glycemic thresholds define each criterion?",
   "answer":"Classic symptoms + random glucose ≥200 mg/dL; or fasting plasma glucose ≥126 mg/dL; or 2-hour glucose ≥200 mg/dL on OGTT; or HbA1c ≥6.5%.",
   "rationale":"Each diagnostic criterion reflects the glycemic threshold associated with risk of microvascular complications (particularly retinopathy); all thresholds should be confirmed on a separate day unless clearly symptomatic.",
   "bloom":"recall",
   "source":[{"book":"Miller/Baby Miller","page":546}],
   "confusable_with":"prediabetes (impaired fasting glucose 100-125, HbA1c 5.7-6.4%)"},

  {"id":"dm-macrovascular-d5","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"In patients with diabetes-related macrovascular disease, what perioperative pharmacological intervention using alpha-2 agonists reduces myocardial contractility requirements?",
   "answer":"Alpha-2 agonists (e.g., dexmedetomidine, clonidine) reduce the requirement for volatile anesthetic agents (decrease MAC values), reduce postoperative pain intensity, decrease opioid consumption, and reduce PONV.",
   "rationale":"Alpha-2 agonists act centrally to reduce sympathetic outflow and provide sedation and analgesia; their sympatholytic properties are particularly beneficial in diabetic patients with autonomic neuropathy and fragile cardiovascular control.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1826}],
   "confusable_with":""},

  {"id":"dm-macrovascular-d6","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What is the primary pharmacodynamic change in elderly diabetic patients that affects anesthetic dosing?",
   "answer":"Reduced anesthetic requirement — lower MAC for volatile agents; reduced dose requirements for propofol, etomidate, opioids, benzodiazepines, and barbiturates due to reduced pharmacodynamic sensitivity.",
   "rationale":"Age-related CNS changes (reduced receptor density, altered neurotransmitter balance, decreased neuronal reserve) lower the drug concentrations needed for anesthetic effect; overdose causes prolonged emergence.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1490}],
   "confusable_with":""},

  {"id":"dm-macrovascular-d7","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"The main categories of cardiovascular diagnoses in surgical patients with pre-existing cardiovascular disease are what, and how does this affect perioperative risk assessment?",
   "answer":"Arrhythmias, stroke, and thromboembolism are most common; the prevalence of cardiovascular disease in surgical patients drives the necessity for structured cardiac risk assessment and optimization.",
   "rationale":"Pre-existing cardiovascular disease multiplies perioperative morbidity; ACC/AHA guidelines mandate systematic evaluation using cardiac risk indices and functional capacity assessment.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":618}],
   "confusable_with":""},
]

# ── 125: Diabetic Microvascular Complications ─────────────────────────────────
T = "Diabetic Microvascular Complications"
DOM = "Internal medicine: endocrinology (diabetes & inpatient glucose, DKA & HHS, thyroid disorders & storm, adrenal insufficiency, calcium disorders, pituitary)"
DISC = "medicine"

kps += [
  {"id":"dm-microvascular-d1","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Both ACEIs and ARBs are recommended by the ADA for which specific diabetic microvascular complication, and what outcome do they delay?",
   "answer":"Recommended for type 2 diabetics with CKD — both ACEIs and ARBs delay deterioration in GFR and worsening of albuminuria (i.e., slow progression of diabetic nephropathy).",
   "rationale":"Angiotensin blockade reduces intraglomerular pressure by dilating the efferent arteriole, lowering the driving force for protein filtration and mesangial expansion.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   JNC7 2003 Hypertension Full Report","page":53}],
   "confusable_with":""},

  {"id":"dm-microvascular-d2","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Diabetes is the leading cause of blindness, ESRD, and nontraumatic amputations. What autonomic neuropathy finding should be specifically assessed before anesthesia in a diabetic patient?",
   "answer":"Lack of sweating and abnormal heart rate variability during voluntary deep breathing (normal HRV >10 beats/min) indicate significant autonomic neuropathy requiring modified hemodynamic management.",
   "rationale":"Autonomic neuropathy causes intraoperative hemodynamic instability (orthostatic hypotension, gastroparesis, silent ischemia); pre-operative detection allows prophylactic vasopressor and aggressive monitoring strategy.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1221}],
   "confusable_with":""},

  {"id":"dm-microvascular-d3","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Classic symptoms of hyperglycemia include polyuria, polydipsia, weight loss, and blurred vision. What does blurred vision reflect at a microvascular level?",
   "answer":"Blurred vision reflects osmotic swelling of the lens from high intralens glucose and sorbitol accumulation, causing reversible refractive changes; sustained hyperglycemia causes retinal vascular damage (retinopathy).",
   "rationale":"Aldose reductase converts excess glucose to sorbitol in lens and retinal pericytes; sorbitol accumulation causes osmotic damage — reversible early (refractive error) but progressing to pericyte loss and retinopathy.",
   "bloom":"analyze",
   "source":[{"book":"Miller/Baby Miller","page":546}],
   "confusable_with":""},

  {"id":"dm-microvascular-d4","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"NSAIDs are particularly dangerous in patients with diabetic nephropathy. For what other specific CKD conditions are they similarly hazardous?",
   "answer":"NSAIDs are dangerous in patients with hypovolemia, heart failure, cirrhosis, and hypercalcemia — conditions where renal prostaglandins are needed for vasodilation to maintain GFR.",
   "rationale":"All these states represent reduced effective circulating volume; the kidney compensates by releasing prostaglandins to vasodilate the afferent arteriole — NSAIDs remove this compensatory mechanism.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":315}],
   "confusable_with":""},

  {"id":"dm-microvascular-d5","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Perioperative morbidity in diabetic patients increases significantly with poor glycemic control. What specific complication risk is elevated?",
   "answer":"Wound infections, delayed healing, cardiovascular events, acute kidney injury, and increased length of stay — all elevated in diabetic patients with poor preoperative glycemic control (elevated HbA1c).",
   "rationale":"Hyperglycemia impairs neutrophil function, complement activation, and collagen synthesis; perioperative hyperglycemia independently worsens surgical outcomes even in previously well-controlled diabetics.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1220}],
   "confusable_with":""},

  {"id":"dm-microvascular-d6","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Rapid intravenous potassium replacement (>8 mEq/h) for hypokalemia in a diabetic patient requires what specific precautions?",
   "answer":"Peripheral IV replacement should not exceed 8 mEq/h; more rapid replacement (10-20 mEq/h) requires central venous administration and close ECG monitoring.",
   "rationale":"Potassium is irritating to peripheral veins and causes phlebitis at higher concentrations; rapid central infusion risks causing cardiac arrhythmias that require continuous ECG monitoring.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1882}],
   "confusable_with":""},
]

# ── 126: Diabetic ketoacidosis & hyperosmolar hyperglycemic state ─────────────
T = "Diabetic ketoacidosis & hyperosmolar hyperglycemic state"
DOM = "General internal medicine, preventive care & geriatrics (admission & cross-cover problems, perioperative medicine, screening & vaccination, polypharmacy & deprescribing, frailty, delirium prevention, goals of care)"
DISC = "medicine"

kps += [
  {"id":"dka-hhs-d1","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What is the correct sequence of treatment for diabetic ketoacidosis?",
   "answer":"First: replace the fluid deficit from hyperglycemic osmotic diuresis; then add insulin; then replace potassium, phosphate, and magnesium.",
   "rationale":"Fluid replacement is paramount first because insulin drives potassium intracellularly — starting insulin before potassium repletion causes dangerous hypokalemia; fluid also lowers glucose before insulin is needed.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1931}],
   "confusable_with":"HHS (same fluid priority but different insulin urgency)"},

  {"id":"dka-hhs-d2","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What alternative bicarbonate buffers have been proposed for DKA but remain clinically unproven?",
   "answer":"Carbicarb and tromethamine (THAM) are alternative buffers that do not produce CO2 (unlike bicarbonate), making them theoretically preferable, but they remain unproven in clinical DKA trials.",
   "rationale":"Sodium bicarbonate generates CO2 when neutralizing acid; CO2 can cross the blood-brain barrier and paradoxically worsen CNS acidosis while peripheral pH improves — this theoretical concern motivates investigation of CO2-free buffers.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1931}],
   "confusable_with":""},

  {"id":"dka-hhs-d3","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"DKA is one of three life-threatening acute diabetic complications. What distinguishes DKA from HHS biochemically?",
   "answer":"DKA: relative/absolute insulin deficiency causes ketoacidosis (anion-gap metabolic acidosis, ketones); HHS: sufficient insulin to prevent ketosis but profound hyperglycemia (often >600 mg/dL) and hyperosmolality without significant acidosis.",
   "rationale":"In type 2 diabetes (typical HHS), enough residual insulin prevents lipolysis/ketogenesis but cannot prevent hyperglycemia; the profound dehydration from osmotic diuresis drives hyperosmolality.",
   "bloom":"analyze",
   "source":[{"book":"Morgan & Mikhail","page":1218}],
   "confusable_with":"alcoholic ketoacidosis (ketosis without significant hyperglycemia)"},

  {"id":"dka-hhs-d4","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"DKA can be a complication of total parenteral nutrition (TPN). What metabolic complications are associated with TPN excess glucose administration?",
   "answer":"Overfeeding with excess glucose causes DKA, hyperosmolar coma, excessive CO2 production, hypoglycemia (interruption), and metabolic acidosis.",
   "rationale":"TPN-related DKA occurs when exogenous glucose overwhelms insulin secretory capacity; excessive CO2 production from carbohydrate oxidation worsens respiratory failure in ventilator-dependent patients.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":2001}],
   "confusable_with":""},

  {"id":"dka-hhs-d5","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Adrenal crisis must be distinguished from DKA and HHS in the differential diagnosis of metabolic emergencies. What endocrine conditions are included in the differential for patients presenting in apparent adrenal crisis?",
   "answer":"Thyrotoxicosis, DKA, HHS, myxedema coma, and pituitary adenoma are all included in the endocrine differential for a patient presenting with features of adrenal crisis.",
   "rationale":"All these conditions can present with hemodynamic instability, altered mental status, and metabolic derangements; each requires specific management; adrenal crisis must be recognized quickly because mortality is high without hydrocortisone.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Adrenal Crisis","page":10}],
   "confusable_with":"septic shock, cardiogenic shock"},

  {"id":"dka-hhs-d6","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Severe lactic acidosis can mimic DKA biochemically (anion-gap metabolic acidosis). What underlying condition most commonly causes lactic acidosis?",
   "answer":"Severe tissue hypoxia from hypoxemia, hypoperfusion (ischemia), or inability to use oxygen (e.g., cyanide poisoning) causes lactic acidosis via anaerobic metabolism.",
   "rationale":"Anaerobic glycolysis produces lactic acid as the terminal product when mitochondrial oxidative phosphorylation fails; lactic acidosis with anion gap can mimic DKA but lacks ketones.",
   "bloom":"analyze",
   "source":[{"book":"Morgan & Mikhail","page":1928}],
   "confusable_with":"DKA (ketones present in DKA, absent in pure lactic acidosis)"},

  {"id":"dka-hhs-d7","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Mineralocorticoid replacement after adrenal crisis taper: when is it considered unnecessary?",
   "answer":"Mineralocorticoid replacement is unnecessary if glucocorticoid doses exceed 50 mg (e.g., hydrocortisone >50 mg/day has sufficient mineralocorticoid activity); individual assessment with endocrinology is required.",
   "rationale":"Hydrocortisone at high doses (~50 mg) provides sufficient mineralocorticoid effect via non-selective glucocorticoid receptor activity to maintain sodium balance; fludrocortisone is added only at lower physiological replacement doses.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Adrenal Crisis","page":10}],
   "confusable_with":""},
]

kps.append({"_type":"illness_script","topic":T,"discipline":DISC,
  "enabling_conditions":"DKA: type 1 DM (most common), type 2 with stressor (infection, ischemia, missed insulin); HHS: type 2 DM + dehydration",
  "pathophysiology":"DKA: insulin deficiency → unchecked lipolysis → ketogenesis → anion-gap acidosis + osmotic diuresis; HHS: residual insulin prevents ketosis but not hyperglycemia → profound dehydration + hyperosmolality",
  "time_course":"DKA: hours-days; HHS: days-weeks of worsening hyperglycemia",
  "key_features":"DKA: Kussmaul breathing, fruity breath, ketones; HHS: profound dehydration, glucose >600, osmolality >320, minimal ketones",
  "consequence_if_missed":"Cerebral edema (DKA treatment complication in children); circulatory collapse; death without prompt fluid and electrolyte replacement"})

kps.append({"_type":"confusable_pair","topic_a":"DKA","topic_b":"HHS",
  "discriminator":"DKA: anion-gap acidosis, ketonemia, younger/T1DM; HHS: no significant ketosis/acidosis, profound hyperglycemia >600, hyperosmolality >320, older/T2DM"})

# ── 127: Dialysis: Hemodialysis Principles and Access ─────────────────────────
T = "Dialysis: Hemodialysis Principles and Access"
DOM = "Internal medicine: nephrology, fluids & electrolytes"
DISC = "medicine"

kps += [
  {"id":"hemodialysis-d1","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What are the two fundamental transport mechanisms in hemodialysis and peritoneal dialysis?",
   "answer":"Diffusion: concentration gradient drives small molecules (urea, creatinine) across a selectively permeable membrane; Convection (ultrafiltration): hydrostatic pressure forces medium-weight molecules and plasma water across the membrane.",
   "rationale":"Diffusion clears small solutes (urea, potassium) efficiently but not middle molecules; convection (as in hemofiltration) removes middle molecules and excess fluid; modern hemodialysis combines both.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":103}],
   "confusable_with":"peritoneal dialysis (uses peritoneum as membrane, primarily diffusion + osmotic ultrafiltration)"},

  {"id":"hemodialysis-d2","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What is the preferred order of arteriovenous access creation for hemodialysis fistulas?",
   "answer":"Radiocephalic fistula (wrist) is preferred first; then brachiocephalic; then transposed brachiobasilic; then loop arteriovenous graft — most distal access preserved for future central access.",
   "rationale":"Distal-first access preserves proximal vessels for future access when distal sites fail; arteriovenous fistulas (AVF) are preferred over grafts due to lower infection and thrombosis rates.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Dialysis  CRRT in the ICU","page":4}],
   "confusable_with":""},

  {"id":"hemodialysis-d3","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"At what GFR threshold should vascular access planning begin for patients likely to need hemodialysis?",
   "answer":"Access planning should begin when GFR falls below 30 mL/min (CKD G4), or at initial assessment if there is imminent need for maintenance dialysis.",
   "rationale":"AVF maturation requires 6-12 weeks minimum; early creation ensures access is functional when dialysis is needed, avoiding temporary central venous catheter use with its infection and thrombosis risks.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Dialysis  Hemodialysis Principles and Access","page":3}],
   "confusable_with":""},

  {"id":"hemodialysis-d4","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"An arteriovenous fistula is surgically created by what procedure?",
   "answer":"An arteriotomy is made, the artery is flushed with heparinized saline, and an anastomosis connects the artery directly to the adjacent vein, allowing arterial flow to mature the vein for cannulation.",
   "rationale":"Arterial flow through the vein causes turbulence-mediated wall thickening and dilation over weeks; the matured vein develops a thick wall suitable for repeated large-bore needle cannulation.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Dialysis  Hemodialysis Principles and Access","page":4}],
   "confusable_with":"AV graft (prosthetic material, no maturation needed)"},

  {"id":"hemodialysis-d5","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What should be assessed by palpation when examining an arteriovenous fistula?",
   "answer":"Place fingertips lightly over the fistula to detect pulsation (arterial component) and thrill (turbulent flow at the anastomosis indicating patency); loss of thrill suggests stenosis or thrombosis.",
   "rationale":"A patent AVF produces a continuous bruit (auscultation) and thrill (palpation) from turbulent arteriovenous flow; diminished or absent thrill is an early sign of outflow stenosis requiring urgent evaluation.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Dialysis  Hemodialysis Principles and Access","page":8}],
   "confusable_with":""},

  {"id":"hemodialysis-d6","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Intraoperative continuous venovenous hemodialysis (CVVHD) during liver transplantation serves what specific purpose?",
   "answer":"CVVHD provides real-time volume and electrolyte management (closely managing serum sodium and potassium) in patients with marginal or absent kidney function during the transplantation.",
   "rationale":"Liver transplantation requires massive fluid shifts; CVVHD allows precise management of the electrolyte derangements (hyperkalemia, acidosis) that would otherwise be fatal in anuric patients.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1206}],
   "confusable_with":""},

  {"id":"hemodialysis-d7","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Cisatracurium is the neuromuscular blocking agent of choice for patients on dialysis. Why?",
   "answer":"Cisatracurium is eliminated by Hofmann degradation (temperature and pH-dependent spontaneous degradation) independent of renal excretion, so its duration is not prolonged in renal failure.",
   "rationale":"Other NMBDs (e.g., vecuronium, pancuronium) have significant renal elimination; their active metabolites accumulate in renal failure causing prolonged neuromuscular blockade and delayed recovery.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1149}],
   "confusable_with":"pancuronium (prolonged by renal failure)"},
]

# ── 128: Disseminated intravascular coagulation (DIC) ─────────────────────────
T = "Disseminated intravascular coagulation (DIC)"
DOM = "Internal medicine: hematology & oncology (anemias, anticoagulation & reversal, VTE prophylaxis & treatment, thrombocytopenia & DIC, transfusion medicine, oncologic emergencies, neutropenic fever)"
DISC = "medicine"

kps += [
  {"id":"dic-d1","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What is the pathophysiological mechanism of DIC in obstetric complications such as placental abruption?",
   "answer":"Release of tissue thromboplastins from placental separation precipitates DIC; activation of circulating plasminogen (fibrinolysis) occurs simultaneously, causing both consumptive coagulopathy and fibrinolysis.",
   "rationale":"Placental tissue factor activates the extrinsic coagulation cascade systemically; simultaneously, plasminogen activators from damaged tissues lyse forming clots, depleting fibrinogen and platelets.",
   "bloom":"analyze",
   "source":[{"book":"Morgan & Mikhail","page":1416}],
   "confusable_with":"primary fibrinolysis (no thrombotic component)"},

  {"id":"dic-d2","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"DIC is a complication of TURP syndrome. What are all the conditions in the differential diagnosis of hypotension following TURP?",
   "answer":"Hemorrhage, TURP syndrome (dilutional hyponatremia), bladder perforation, myocardial infarction or ischemia, septicemia, and DIC.",
   "rationale":"TURP involves absorption of hypotonic irrigation fluid, blood loss, and risk of bacteremia; DIC can develop from bacterial endotoxin release or from irrigation fluid absorption-related coagulopathy.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1149}],
   "confusable_with":""},

  {"id":"dic-d3","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"In what conditions does laboratory evidence of DIC commonly appear but is rarely associated with clinical bleeding?",
   "answer":"Laboratory DIC (elevated D-dimers, low fibrinogen, prolonged PT) is often present in critical illness (e.g., sepsis, malignancy) but rarely causes clinical bleeding in these subclinical/compensated states.",
   "rationale":"Compensated DIC occurs when factor synthesis matches consumption; laboratory evidence reflects ongoing low-grade thrombin generation without clinical hemorrhage unless additional stressors (surgery, infection) tip the balance.",
   "bloom":"analyze",
   "source":[{"book":"Morgan & Mikhail","page":2154}],
   "confusable_with":""},

  {"id":"dic-d4","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"DIC is a known complication of sepsis, hypothermia, and bowel perforation. What is the underlying mechanism linking these conditions to DIC?",
   "answer":"Each releases tissue factor (endotoxin in sepsis, gut bacteria in perforation, cell damage in hypothermia) or causes endothelial activation that initiates the coagulation cascade systemically.",
   "rationale":"Tissue factor exposure and endothelial damage activate thrombin generation; in sepsis, bacterial endotoxin and cytokines (TNF-alpha, IL-1) cause diffuse endothelial TF expression and PAI-1-mediated fibrinolysis shutdown.",
   "bloom":"analyze",
   "source":[{"book":"Morgan & Mikhail","page":1129}],
   "confusable_with":""},

  {"id":"dic-d5","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"How does plasmin relate to DIC and what are two endogenous and one exogenous plasminogen activator?",
   "answer":"Plasmin degrades fibrin, fibrinogen, and other coagulation factors; endogenous activators: tPA (tissue plasminogen activator) and urokinase (urine); exogenous: streptokinase (bacterial).",
   "rationale":"DIC involves simultaneous activation of both coagulation (thrombin) and fibrinolysis (plasmin); the balance between these determines whether the patient bleeds (fibrinolytic predominance) or clots (coagulation predominance).",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1177}],
   "confusable_with":""},

  {"id":"dic-d6","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Malignant hyperthermia (MH) can present with laboratory features resembling DIC. What lab abnormalities characterize MH?",
   "answer":"MH produces mixed metabolic and respiratory acidosis, marked base deficit, hyperkalemia, hypermagnesemia, reduced mixed-venous oxygen saturation; ionized calcium may initially increase then decrease; DIC-like coagulopathy can develop late.",
   "rationale":"MH causes massive mitochondrial uncoupling and ATP consumption; the resulting cellular acidosis, muscle necrosis, and organ failure can progress to consumptive coagulopathy in untreated severe episodes.",
   "bloom":"analyze",
   "source":[{"book":"Morgan & Mikhail","page":1988}],
   "confusable_with":"DIC from other causes"},

  {"id":"dic-d7","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"In obstetric DIC following active bleeding or hemodynamic instability, what is the definitive surgical management?",
   "answer":"Immediate cesarean section under general anesthesia is required for active bleeding or hemodynamic instability; two large-bore IV catheters and intravascular volume resuscitation are essential.",
   "rationale":"Delivery of the fetus and placenta removes the source of tissue thromboplastin driving DIC; general anesthesia is chosen over regional because coagulopathy makes neuraxial blockade hazardous.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1416}],
   "confusable_with":""},
]

kps.append({"_type":"illness_script","topic":T,"discipline":DISC,
  "enabling_conditions":"Sepsis (gram-negative endotoxin), obstetric emergencies (abruption, amniotic fluid embolism), massive trauma, malignancy (especially AML-M3), severe burns, snake envenomation",
  "pathophysiology":"Systemic tissue factor exposure → disseminated thrombin generation → microvascular thrombosis + consumption of platelets and clotting factors → secondary fibrinolysis",
  "time_course":"Acute (sepsis, trauma, obstetric): hours; Chronic (malignancy): weeks to months",
  "key_features":"Thrombocytopenia, prolonged PT/aPTT, low fibrinogen, elevated D-dimers/FDPs, microangiopathic hemolysis (schistocytes); bleeding and thrombosis can coexist",
  "consequence_if_missed":"Multi-organ failure from microvascular thrombi; uncontrolled hemorrhage from factor consumption; death"})

# ── 129: Drug Dosing in Renal Impairment ──────────────────────────────────────
T = "Drug Dosing in Renal Impairment"
DOM = "Internal medicine: nephrology, fluids & electrolytes"
DISC = "medicine"

kps += [
  {"id":"drug-renal-d1","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Which neuromuscular blocking drugs require significant dose reduction or avoidance in severe renal failure and why?",
   "answer":"d-Tubocurarine (curare): 40-60% renally excreted — increasingly prolonged with reduced kidney function; pancuronium: 40% renal + 10% biliary — prolonged in renal failure. Cisatracurium is preferred.",
   "rationale":"NMBDs dependent on renal excretion accumulate in renal failure, causing prolonged neuromuscular blockade beyond the surgical period; Hofmann-degraded agents (cisatracurium, atracurium) avoid this.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1105},{"book":"Morgan & Mikhail","page":347}],
   "confusable_with":"cisatracurium (Hofmann elimination, safe in renal failure)"},

  {"id":"drug-renal-d2","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Which opioids are specifically contraindicated in elderly patients with renal impairment and why?",
   "answer":"Meperidine and morphine — meperidine metabolizes to normeperidine (renally excreted, causes seizures); morphine metabolizes to morphine-6-glucuronide and morphine-3-glucuronide (active, renally excreted, cause prolonged CNS depression).",
   "rationale":"Accumulation of active renally-cleared opioid metabolites causes unpredictable CNS toxicity; fentanyl and hydromorphone are preferred in renal impairment as their metabolites are inactive or minimally toxic.",
   "bloom":"apply",
   "source":[{"book":"Miller/Baby Miller","page":675}],
   "confusable_with":"fentanyl (inactive metabolites, safe in renal failure)"},

  {"id":"drug-renal-d3","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"For aminoglycosides in patients with normal and stable kidney function, what dosing strategy limits nephrotoxicity?",
   "answer":"Once-daily (extended-interval) dosing of aminoglycosides is recommended when feasible — favored by pharmacokinetic/pharmacodynamic properties (concentration-dependent killing, post-antibiotic effect).",
   "rationale":"High peak concentrations with extended low troughs optimize bacterial killing (concentration-dependent) while minimizing renal cortical accumulation (which occurs preferentially during sustained high trough levels).",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2012 AKI","page":65}],
   "confusable_with":"time-dependent antibiotics (beta-lactams) which require continuous infusion"},

  {"id":"drug-renal-d4","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"For once-daily aminoglycoside dosing, what Cmin level should be achieved at 12, 18, or 24 hours after the dose?",
   "answer":"Cmin should be below the limits of detection of the assay (<1 mcg/mL) at these time intervals; levels should be checked at least once or weekly during prolonged courses.",
   "rationale":"A low or undetectable trough ensures there is sufficient time for cortical aminoglycoside concentration to fall, preventing proximal tubular accumulation and nephrotoxicity.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2012 AKI","page":66}],
   "confusable_with":""},

  {"id":"drug-renal-d5","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Direct thrombin inhibitors (DTIs) have no reversal agents — how should their anticoagulant effect be managed acutely?",
   "answer":"DTIs have no direct reversal agents; their relatively short half-lives mean time and supportive medical care are often sufficient; for DOACs, novel reversal agents are available.",
   "rationale":"Argatroban and bivalirudin (DTIs) are cleared hepatically with short half-lives; stopping the infusion and time allows effect to dissipate; however argatroban also significantly elevates INR, complicating warfarin transition.",
   "bloom":"apply",
   "source":[{"book":"Miller/Baby Miller","page":458}],
   "confusable_with":"warfarin (reversed with vitamin K or PCC)"},

  {"id":"drug-renal-d6","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"The HAS-BLED score flags abnormal renal function as a bleeding risk factor for anticoagulation. What CrCl threshold defines 'abnormal renal function' in this score?",
   "answer":"CrCl <50 mL/min is the threshold for 'abnormal renal function' in the HAS-BLED bleeding risk score.",
   "rationale":"Renally-cleared anticoagulants (direct oral anticoagulants like rivaroxaban, dabigatran, apixaban) accumulate in moderate-severe renal impairment, increasing bleeding risk; dose adjustment or avoidance is needed below CrCl 50.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":14}],
   "confusable_with":""},

  {"id":"drug-renal-d7","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Argatroban has the greatest effect on INR among DTIs. Why does this complicate management?",
   "answer":"Argatroban significantly prolongs the INR independently of its anticoagulant effect; this complicates the transition to long-term warfarin anticoagulation as the INR will overestimate warfarin's true effect while argatroban is present.",
   "rationale":"The INR uses PT which measures thrombin generation; argatroban directly inhibits thrombin, prolonging PT/INR without reflecting vitamin K-dependent factor levels; warfarin's true INR is uninterpretable until argatroban clears.",
   "bloom":"analyze",
   "source":[{"book":"Miller/Baby Miller","page":454}],
   "confusable_with":"bivalirudin (shorter half-life, less INR interference)"},
]

# ── 130: Drug-Induced Liver Injury (DILI) ─────────────────────────────────────
T = "Drug-Induced Liver Injury (DILI)"
DOM = "Internal medicine: gastroenterology & hepatology (upper & lower GI bleed, acute liver failure, cirrhosis & its complications, pancreatitis, IBD, bowel obstruction, hepatic encephalopathy)"
DISC = "medicine"

kps += [
  {"id":"dili-d1","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What are the causes of postoperative hepatic dysfunction that must be included in the differential diagnosis?",
   "answer":"Viral hepatitis, impaired hepatic perfusion, preexisting liver disease, hepatocyte hypoxia, sepsis, hemolysis, benign postoperative intrahepatic cholestasis, and drug-induced hepatitis.",
   "rationale":"Post-anesthetic jaundice most commonly results from hemolysis or benign cholestasis; drug hepatitis (especially halothane, though now rare) must be considered after all common causes are excluded.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":263}],
   "confusable_with":""},

  {"id":"dili-d2","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Halothane hepatitis is considered extremely rare. What key exposure history suggests DILI from a volatile anesthetic?",
   "answer":"Prior exposure to halothane (or other halogenated agents) in a patient with unexplained post-operative hepatitis — especially with a shorter latency on re-exposure.",
   "rationale":"Halothane hepatitis (type II hypersensitivity) involves immune-mediated destruction of trifluoroacetylated protein adducts on hepatocyte membranes; sensitization from prior exposure accelerates injury on re-exposure.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":263}],
   "confusable_with":"viral hepatitis"},

  {"id":"dili-d3","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"In acute liver failure (ALF) evaluation, what laboratory parameters assess hepatic synthetic function and what threshold defines significant dysfunction?",
   "answer":"INR, albumin, and PT assess synthetic function; ALT/AST measure hepatocellular damage; INR ≥1.5 with encephalopathy defines ALF; bilirubin, alkaline phosphatase, GGT, LDH assess cholestasis and hepatocellular injury.",
   "rationale":"Synthetic function (INR, albumin) falls later than transaminase elevation but carries prognostic weight; the King's College Criteria for transplant listing is based on INR and bilirubin trajectories.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Acute Liver Failure (ALF)","page":7}],
   "confusable_with":""},

  {"id":"dili-d4","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What are the features of the initial presentation of acute liver injury that should prompt urgent investigation?",
   "answer":"Fatigue, lethargy, anorexia, nausea/vomiting, RUQ pain, pruritis, ± jaundice → ascites, confusion (progressing to coma in ALF); initial diagnostics include CBC, CMP, PT/INR, fibrinogen, LDH, lactate, ABG, arterial ammonia.",
   "rationale":"The progression from liver injury to ALF is characterized by worsening synthetic failure and encephalopathy; arterial ammonia correlates with cerebral edema risk and is required for grading encephalopathy severity.",
   "bloom":"apply",
   "source":[{"book":"MGH Housestaff Manual","page":89}],
   "confusable_with":""},

  {"id":"dili-d5","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"The differential diagnosis of DILI includes which chronic liver diseases that must be excluded?",
   "answer":"Alcoholic liver disease, alpha-1 antitrypsin deficiency, autoimmune liver disease, viral hepatitis A through E, and NAFLD/MASLD all appear in the DILI differential.",
   "rationale":"DILI is a diagnosis of exclusion; common chronic conditions (viral hepatitis, autoimmune, metabolic) must be excluded by serology, metabolic workup, and biopsy if needed before attributing injury to a drug.",
   "bloom":"recall",
   "source":[{"book":"StatPearls","page":5}],
   "confusable_with":""},

  {"id":"dili-d6","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"In alcohol-related liver disease, how does the AST:ALT ratio help distinguish it from other DILI?",
   "answer":"In alcoholic hepatitis, AST:ALT ratio >2:1 (typically >2) is characteristic; in most other forms of hepatitis (viral, DILI), ALT usually exceeds AST.",
   "rationale":"Alcohol depletes pyridoxal phosphate (required for ALT synthesis more than AST) and directly injures mitochondria (releasing mitochondrial AST); the result is disproportionate AST elevation.",
   "bloom":"analyze",
   "source":[{"book":"MGH Housestaff Manual","page":91}],
   "confusable_with":""},

  {"id":"dili-d7","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Safe storage and packaging of acetaminophen is addressed in public health guidelines. What unintentional route of acetaminophen DILI occurs most commonly in children and adults respectively?",
   "answer":"Children: accidental toxic ingestion (inadequate safe storage); Adults: unintentional overdose from multiple products containing acetaminophen simultaneously (e.g., cold medicines + prescription opioid-acetaminophen combinations).",
   "rationale":"Acetaminophen DILI (from NAPQI accumulation when glutathione depleted) is the leading cause of ALF in the US; in adults, therapeutic misadventure from unknowingly combining acetaminophen-containing products is more common than intentional overdose.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Acute Liver Failure (ALF)","page":18}],
   "confusable_with":""},
]

kps.append({"_type":"illness_script","topic":T,"discipline":DISC,
  "enabling_conditions":"Acetaminophen overdose (most common in West), idiosyncratic reactions (antibiotics, NSAIDs, statins, herbal supplements), immune-mediated (halothane, nitrofurantoin)",
  "pathophysiology":"Intrinsic DILI: dose-dependent hepatocellular necrosis (acetaminophen via NAPQI glutathione depletion); Idiosyncratic DILI: immune or metabolic hypersensitivity, unpredictable, dose-independent",
  "time_course":"Intrinsic: hours-days; Idiosyncratic: weeks to months after drug initiation",
  "key_features":"Elevated transaminases ± cholestasis; fever, rash, eosinophilia in immune-mediated; drug rechallenge typically reproduces injury faster",
  "consequence_if_missed":"Acute liver failure with coagulopathy and encephalopathy; need for emergency liver transplant evaluation"})

# ── 131: Esophageal Variceal Bleeding ─────────────────────────────────────────
T = "Esophageal Variceal Bleeding"
DOM = "Internal medicine: gastroenterology & hepatology (upper & lower GI bleed, acute liver failure, cirrhosis & its complications, pancreatitis, IBD, bowel obstruction, hepatic encephalopathy)"
DISC = "medicine"

kps += [
  {"id":"esoph-variceal-d1","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"A patient with cirrhosis presents with hematemesis. What is the classification of compensated vs. decompensated cirrhosis, and why is variceal bleeding a decompensating event?",
   "answer":"Compensated: no ascites, encephalopathy, jaundice, or GI bleeding (may have non-bleeding varices); Decompensated: ascites, hepatic encephalopathy, jaundice, SBP, hepatopulmonary syndrome, or variceal bleeding. Variceal bleeding defines decompensation.",
   "rationale":"Portal hypertension-driven variceal formation is a structural consequence of cirrhotic fibrosis; the first bleed dramatically worsens prognosis (30-50% 6-week mortality without treatment), marking the transition to decompensated disease.",
   "bloom":"analyze",
   "source":[{"book":"MGH Housestaff Manual","page":93}],
   "confusable_with":""},

  {"id":"esoph-variceal-d2","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What is the pathophysiology of hepatic encephalopathy in the context of variceal bleeding, and why does bleeding specifically worsen HE?",
   "answer":"HE pathophysiology: elevated ammonia → neurotoxic effects + abnormal neurotransmission (GABA-like, glutaminergic). Variceal bleeding worsens HE because digestion of blood dramatically increases ammonia generation from the GI tract.",
   "rationale":"Each gram of hemoglobin yields ~3 mmol of ammonia during bacterial degradation in the colon; massive upper GI blood load thus transiently floods the portal circulation with ammonia, overwhelming hepatic detoxification.",
   "bloom":"analyze",
   "source":[{"book":"MGH Housestaff Manual","page":95}],
   "confusable_with":""},

  {"id":"esoph-variceal-d3","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Patients undergoing TIPS (transjugular intrahepatic portosystemic shunt) are at risk for what two anesthetic complications related to their underlying disease?",
   "answer":"Frequently hypovolemic with profound ascites AND at risk of esophageal variceal bleeding and aspiration.",
   "rationale":"TIPS reduces portal hypertension by creating a direct portosystemic shunt; pre-procedure patients are often in advanced liver failure with ascites causing poor functional residual capacity and variceal bleeding risk.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1535}],
   "confusable_with":""},

  {"id":"esoph-variceal-d4","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"Why should hypotensive anesthesia be specifically avoided in patients with variceal disease undergoing liver transplantation?",
   "answer":"Hypotensive anesthesia should be avoided because reduced hepatic perfusion pressure worsens hepatic ischemia and liver function in an already compromised liver.",
   "rationale":"The cirrhotic liver has reduced hepatic arterial buffer response and impaired autoregulation; deliberate hypotension dramatically reduces hepatic blood flow, potentially precipitating acute-on-chronic liver failure.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1203}],
   "confusable_with":""},

  {"id":"esoph-variceal-d5","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What is the role of non-selective beta-blockers in secondary prophylaxis of esophageal variceal bleeding?",
   "answer":"Non-selective beta-blockers combined with endoscopic variceal ligation (EVL) or cyanoacrylate injection are first-line therapy for secondary prophylaxis to prevent rebleeding in patients who survive GOV1 hemorrhage.",
   "rationale":"Non-selective beta-blockers (propranolol, nadolol) reduce portal pressure via two mechanisms: reduced cardiac output (beta-1 blockade) and splanchnic vasoconstriction (beta-2 blockade increasing mesenteric resistance).",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Lower GI Bleed  Evaluation & Management","page":9}],
   "confusable_with":"cardioselective beta-blockers (block only beta-1, inadequate splanchnic effect)"},

  {"id":"esoph-variceal-d6","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"What clinical signs specifically related to cirrhosis and portal hypertension should be assessed at initial evaluation of a GI bleed?",
   "answer":"Elevated jugular venous pulse (right-sided HF from portal-pulmonary hypertension), pleural effusion (hepatohydrothorax), spider angiomata, caput medusae, splenomegaly, ascites, palmar erythema.",
   "rationale":"These physical signs confirm portal hypertension and guide risk stratification; hepatohydrothorax indicates severe portal hypertension with ascitic fluid tracking into the pleural space through diaphragmatic defects.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Lower GI Bleed  Evaluation & Management","page":4}],
   "confusable_with":""},

  {"id":"esoph-variceal-d7","topic":T,"domain":DOM,"discipline":DISC,
   "stem":"A TEE probe is sometimes needed intraoperatively. Why should it be used with caution or avoided in patients with known esophageal variceal disease?",
   "answer":"TEE probe placement carries risk of variceal rupture, perforation, and massive hemorrhage in patients with esophageal varices; the risk-benefit must be carefully weighed before insertion.",
   "rationale":"Varices are thin-walled dilated venous channels subject to pressure from the esophageal probe; even mild mechanical trauma during insertion can precipitate life-threatening hemorrhage.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1203}],
   "confusable_with":""},
]

kps.append({"_type":"illness_script","topic":T,"discipline":DISC,
  "enabling_conditions":"Cirrhosis from any cause (alcohol, viral, metabolic), non-cirrhotic portal hypertension (portal vein thrombosis, schistosomiasis)",
  "pathophysiology":"Portal hypertension → portosystemic collateral formation → esophageal varices → rupture from increased wall tension (Laplace: pressure × radius / wall thickness)",
  "time_course":"Acute hemorrhage; 30-50% 6-week mortality without treatment",
  "key_features":"Hematemesis, hematochezia if brisk; stigmata of cirrhosis; confirmed on upper endoscopy",
  "consequence_if_missed":"Exsanguination; hepatic encephalopathy from blood-derived ammonia; hepatorenal syndrome from hemodynamic insult"})

print(f"Topics 122-131 complete: {len(kps)} KP objects")
with open('data/_kps_part3c.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Saved to data/_kps_part3c.json")
