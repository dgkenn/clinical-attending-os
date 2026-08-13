import json

kps = []

# ITEM 153: Hypoglycemia
topic = "Hypoglycemia"
domain = "Internal medicine: endocrinology (diabetes & inpatient glucose, DKA & HHS, thyroid disorders & storm, adrenal insufficiency, calcium disorders, pituitary)"
disc = "medicine"
kps += [
  {"id":"hypoglycemia-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What glucose threshold defines hypoglycemia in an inpatient setting and what is the treatment threshold for IV dextrose?",
   "answer":"Blood glucose <70 mg/dL defines hypoglycemia; treat with IV dextrose when <55 mg/dL or patient is symptomatic.",
   "rationale":"The ADA threshold of <70 mg/dL is the alert level; symptomatic or severe hypoglycemia (<55 mg/dL) requires immediate IV dextrose.",
   "bloom":"recall","source":[{"book":"Intern Notes / Survival Guide","page":44}],"confusable_with":""},
  {"id":"hypoglycemia-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the 15-15 rule for treating mild-moderate hypoglycemia in a conscious patient?",
   "answer":"Give 15 g fast-acting carbohydrates; recheck glucose in 15 minutes; repeat if still <70 mg/dL.",
   "rationale":"Structured titration prevents overcorrection and rebound hyperglycemia while treating hypoglycemia promptly.",
   "bloom":"apply","source":[{"book":"Intern Notes / Survival Guide","page":44}],"confusable_with":""},
  {"id":"hypoglycemia-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"For a patient who is NPO and has blood glucose of 58 mg/dL, what is the appropriate treatment?",
   "answer":"IV dextrose: typically D50W 25 mL (12.5 g dextrose) IV push; recheck glucose in 15 minutes.",
   "rationale":"Oral carbohydrates cannot be used for NPO patients; IV dextrose rapidly reverses neuroglycopenia.",
   "bloom":"apply","source":[{"book":"Intern Notes / Survival Guide","page":44}],"confusable_with":"glucagon IM (used when no IV access)"},
  {"id":"hypoglycemia-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What are three common causes of drug-induced hypoglycemia in hospitalized non-diabetic patients?",
   "answer":"Insulin, sulfonylureas, and fluoroquinolones (especially gatifloxacin).",
   "rationale":"Sulfonylureas stimulate insulin secretion regardless of glucose level; fluoroquinolones cause both hypo- and hyperglycemia.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":182}],"confusable_with":""},
  {"id":"hypoglycemia-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Adrenal insufficiency causes hypoglycemia by what mechanism?",
   "answer":"Cortisol deficiency impairs gluconeogenesis and glycogenolysis, reducing glucose production.",
   "rationale":"Cortisol is a key counter-regulatory hormone; deficiency removes a critical glucose-raising mechanism.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1219}],"confusable_with":""},
  {"id":"hypoglycemia-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Why do beta-blockers mask hypoglycemia and what symptom is NOT masked?",
   "answer":"Beta-blockers mask adrenergic symptoms (tachycardia, tremor, anxiety) but do not mask diaphoresis (cholinergically mediated).",
   "rationale":"Diaphoresis in hypoglycemia is mediated by cholinergic sympathetic fibers, not beta-adrenergic receptors.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1746}],"confusable_with":""},
]

# ITEM 154: Hypokalemia
topic = "Hypokalemia"
domain = "General internal medicine, preventive care & geriatrics (admission & cross-cover problems, perioperative medicine, screening & vaccination, polypharmacy & deprescribing, frailty, delirium prevention, goals of care)"
disc = "medicine"
kps += [
  {"id":"hypokalemia-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"At what serum potassium level is the risk of serious cardiac arrhythmia high in a patient on digoxin?",
   "answer":"Serum K+ <3.0 mEq/L, especially in patients on digoxin, carries high arrhythmia risk.",
   "rationale":"Hypokalemia potentiates digoxin toxicity by competing for the same binding site on Na+/K+-ATPase.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1846}],"confusable_with":""},
  {"id":"hypokalemia-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What EKG changes occur with hypokalemia?",
   "answer":"Flattened T waves, prominent U waves, ST depression, prolonged QU interval, and widened QRS in severe cases.",
   "rationale":"Hypokalemia slows ventricular repolarization, producing characteristic U waves and increasing arrhythmia risk.",
   "bloom":"recall","source":[{"book":"Intern Notes / Survival Guide","page":8}],"confusable_with":"hypomagnesemia (similar EKG)"},
  {"id":"hypokalemia-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the maximum safe IV potassium replacement rate via peripheral vein?",
   "answer":"No faster than 10 mEq/hour via peripheral vein; up to 20 mEq/hour via central vein with cardiac monitoring.",
   "rationale":"Rapid potassium infusion can cause venous irritation peripherally and fatal cardiac arrhythmia if too concentrated.",
   "bloom":"recall","source":[{"book":"Intern Notes / Survival Guide","page":8}],"confusable_with":""},
  {"id":"hypokalemia-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Why must hypomagnesemia be corrected when treating hypokalemia?",
   "answer":"Magnesium deficiency impairs Na+/K+-ATPase activity, causing renal potassium wasting that is refractory to K+ replacement alone.",
   "rationale":"Without adequate magnesium, the kidney continues to excrete potassium regardless of how much is replaced.",
   "bloom":"analyze","source":[{"book":"MGH Housestaff Manual","page":163}],"confusable_with":""},
  {"id":"hypokalemia-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Loop diuretics cause hypokalemia by what mechanism?",
   "answer":"Loop diuretics increase tubular flow and Na+ delivery to the collecting duct, stimulating Na+/K+ exchange.",
   "rationale":"Aldosterone-mediated Na-K exchange in the collecting duct excretes potassium in response to increased sodium delivery.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1846}],"confusable_with":"thiazide diuretics (similar mechanism)"},
  {"id":"hypokalemia-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Name three common causes of hypokalemia in hospitalized patients.",
   "answer":"Diuretics (loop and thiazide), vomiting/NG suction (metabolic alkalosis with renal K+ loss), and inadequate potassium replacement in parenteral nutrition.",
   "rationale":"Alkalosis promotes K+ uptake into cells and renal K+ excretion; GI losses deplete total body K+.",
   "bloom":"recall","source":[{"book":"Intern Notes / Survival Guide","page":8}],"confusable_with":""},
]

# ITEM 155: Hyponatremia (acute)
topic = "Hyponatremia (acute)"
domain = "General internal medicine, preventive care & geriatrics (admission & cross-cover problems, perioperative medicine, screening & vaccination, polypharmacy & deprescribing, frailty, delirium prevention, goals of care)"
disc = "medicine"
kps += [
  {"id":"hyponatremia-acute-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the maximum rate of sodium correction in acute symptomatic hyponatremia and why?",
   "answer":"No more than 8-10 mEq/L in any 24-hour period; faster correction risks osmotic demyelination syndrome (ODS/CPM).",
   "rationale":"Rapid osmolarity increase causes water efflux from chronically adapted brain cells, leading to myelin sheath damage.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":160}],"confusable_with":"acute correction target (raise 1-2 mEq/L/hr in first 3-4 hours for seizures/coma)"},
  {"id":"hyponatremia-acute-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"A 70-kg patient has Na+ 114 mEq/L with seizures. Calculate the sodium deficit using: Na deficit = TBW × (desired Na – actual Na).",
   "answer":"TBW = 0.6 × 70 = 42 L; deficit = 42 × (120-114) = 252 mEq. Raise Na+ to ~120 acutely at 1-2 mEq/L/hr for 3-4 hours.",
   "rationale":"Severe hyponatremia with seizures requires urgent but controlled correction to relieve cerebral edema.",
   "bloom":"apply","source":[{"book":"Intern Notes / Survival Guide","page":9}],"confusable_with":""},
  {"id":"hyponatremia-acute-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What three clinical features indicate SIADH?",
   "answer":"Low serum osmolality (<280 mOsm/kg), inappropriately concentrated urine (>100 mOsm/kg), and elevated urine sodium (>20 mEq/L).",
   "rationale":"ADH excess impairs free water excretion; the urine is inappropriately concentrated relative to the low plasma osmolality.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":159}],"confusable_with":"psychogenic polydipsia (dilute urine, low UNa)"},
  {"id":"hyponatremia-acute-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What volume status and urine sodium distinguish hypovolemic from hypervolemic hyponatremia?",
   "answer":"Hypovolemic: low urine sodium <20 mEq/L (non-renal loss) or >20 mEq/L (renal loss, e.g., diuretics); hypervolemic (HF, cirrhosis): low urine Na <20 mEq/L due to avid sodium retention.",
   "rationale":"Volume status and urine sodium narrow the differential between sodium-losing vs. sodium-retaining states.",
   "bloom":"analyze","source":[{"book":"Intern Notes / Survival Guide","page":9}],"confusable_with":"SIADH (euvolemic, UNa >20)"},
  {"id":"hyponatremia-acute-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What specific anesthetic scenario most commonly produces acute symptomatic dilutional hyponatremia?",
   "answer":"Absorption of hypotonic irrigating fluid during TURP (transurethral resection of the prostate) — the 'TURP syndrome'.",
   "rationale":"Large volumes of hypotonic glycine/sorbitol irrigant are absorbed through open venous sinuses, diluting serum sodium.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1098}],"confusable_with":""},
  {"id":"hyponatremia-acute-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is osmotic demyelination syndrome (ODS) and which patients are at highest risk?",
   "answer":"Demyelination of pontine (central pontine myelinolysis) and extrapontine neurons from overly rapid correction; highest risk: chronic severe hyponatremia, alcoholism, malnutrition, liver disease.",
   "rationale":"Chronic hyponatremia causes brain adaptation; rapid reversal creates intracellular dehydration in vulnerable myelin-rich areas.",
   "bloom":"analyze","source":[{"book":"MGH Housestaff Manual","page":160}],"confusable_with":""},
]

# ITEM 156: Hyponatremia (pathophysiology)
topic = "Hyponatremia (pathophysiology)"
domain = "General internal medicine, preventive care & geriatrics (admission & cross-cover problems, perioperative medicine, screening & vaccination, polypharmacy & deprescribing, frailty, delirium prevention, goals of care)"
disc = "medicine"
kps += [
  {"id":"hyponatremia-pathophysio-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the most common cause of hospitalized patients developing hyponatremia postoperatively?",
   "answer":"Administration of hypotonic IV fluids (0.45% NaCl or D5W) to patients with elevated ADH levels (pain, nausea, stress).",
   "rationale":"Perioperative ADH elevation impairs free water excretion; hypotonic fluids dilute plasma sodium.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1849}],"confusable_with":""},
  {"id":"hyponatremia-pathophysio-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"By what mechanism does hypothyroidism cause hyponatremia?",
   "answer":"Hypothyroidism impairs free water excretion by reducing cardiac output, which stimulates ADH release and decreases GFR.",
   "rationale":"Reduced renal perfusion from low cardiac output activates volume sensors, promoting ADH-mediated water retention.",
   "bloom":"analyze","source":[{"book":"MGH Housestaff Manual","page":159}],"confusable_with":"SIADH (euvolemic, but TSH elevated)"},
  {"id":"hyponatremia-pathophysio-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Why does beer potomania cause hyponatremia even with normal or large urine output?",
   "answer":"Severe malnutrition means minimal dietary solute; the kidney cannot excrete water without sufficient urinary solute to drive osmolar excretion.",
   "rationale":"Free water excretion requires solute to carry it out; without solute intake, maximum dilute urine still retains excess water.",
   "bloom":"analyze","source":[{"book":"Intern Notes / Survival Guide","page":9}],"confusable_with":"psychogenic polydipsia"},
  {"id":"hyponatremia-pathophysio-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In pseudohyponatremia, what is the plasma osmolality and what conditions cause it?",
   "answer":"Plasma osmolality is normal (280-295 mOsm/kg); caused by extreme hyperlipidemia or hyperproteinemia displacing water from plasma.",
   "rationale":"Elevated lipids/proteins occupy plasma volume but do not dissolve in aqueous phase; measured Na appears low by dilution artifact.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1849}],"confusable_with":"true hyponatremia (low osmolality)"},
  {"id":"hyponatremia-pathophysio-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the corrected sodium in hyperglycemia, and why does glucose cause this effect?",
   "answer":"Add 1.6 mEq/L to measured Na+ for every 100 mg/dL glucose above 100; hyperglycemia draws water from cells, diluting ECF sodium.",
   "rationale":"Glucose is an effective osmole; osmotic water shift from ICF to ECF dilutes measured sodium concentration.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1849}],"confusable_with":""},
  {"id":"hyponatremia-pathophysio-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the urine osmolality that distinguishes complete vs. partial ADH failure (central DI)?",
   "answer":"Urine osmolality <100 mOsm/kg suggests complete central DI; partial central DI: urine is dilute but >100 mOsm/kg.",
   "rationale":"Maximum diluting capacity in the absence of ADH produces urine osmolality 50-100 mOsm/kg.",
   "bloom":"recall","source":[{"book":"Intern Notes / Survival Guide","page":9}],"confusable_with":"nephrogenic DI (no response to desmopressin)"},
]

# ITEM 157: Hypoxemic respiratory failure
topic = "Hypoxemic respiratory failure"
domain = "Internal medicine: pulmonology (COPD, asthma, pulmonary embolism, pneumonia, ILD, pleural effusion, pneumothorax, hypoxemic & hypercapnic respiratory failure, OSA)"
disc = "medicine"
kps += [
  {"id":"hypoxemic-resp-failure-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"A patient on 100% FiO2 fails to adequately raise PaO2. What pathophysiology does this indicate?",
   "answer":"True intrapulmonary shunt (blood bypasses ventilated alveoli); shunt fractions >30% are minimally responsive to supplemental O2.",
   "rationale":"Shunted blood mixes with oxygenated blood; high FiO2 cannot oxygenate alveoli that are flooded or atelectatic.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":541}],"confusable_with":"V/Q mismatch (responds to supplemental O2)"},
  {"id":"hypoxemic-resp-failure-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Calculate the A-a gradient for a 70-year-old on room air with PaO2 85 mmHg and PaCO2 40 mmHg.",
   "answer":"PAO2 = (0.21 × 713) - 40/0.8 = 149.7 - 50 = 99.7; A-a gradient = 99.7 - 85 = 14.7 mmHg. Normal for age (age/4 + 4 = ~21.5).",
   "rationale":"The A-a gradient detects intrinsic lung disease; elevated gradient indicates V/Q mismatch, shunt, or diffusion defect.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":541}],"confusable_with":""},
  {"id":"hypoxemic-resp-failure-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What PEEP-related ventilator adjustment recruits atelectatic alveoli and reduces shunt?",
   "answer":"Increasing PEEP (positive end-expiratory pressure) maintains alveolar opening throughout exhalation, recruiting collapsed alveoli.",
   "rationale":"Atelectasis increases shunt fraction; PEEP stents open alveoli, improving V/Q matching and oxygenation.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":567}],"confusable_with":"increasing FiO2 (less effective for shunt)"},
  {"id":"hypoxemic-resp-failure-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In ARDS, what lung-protective ventilation strategy reduces ventilator-induced lung injury (VILI)?",
   "answer":"Tidal volumes 6 mL/kg ideal body weight, plateau pressure <30 cmH2O (ARDSNet protocol).",
   "rationale":"Volutrauma and barotrauma from high tidal volumes worsen ARDS; low tidal volume strategy reduces mortality.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1638}],"confusable_with":""},
  {"id":"hypoxemic-resp-failure-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What are the Berlin criteria for ARDS severity by PaO2/FiO2 (P/F) ratio?",
   "answer":"Mild: P/F 200-300 mmHg; moderate: P/F 100-200 mmHg; severe: P/F <100 mmHg on PEEP >=5 cmH2O.",
   "rationale":"P/F ratio standardizes oxygenation severity across different FiO2 levels and guides escalation of care.",
   "bloom":"recall","source":[{"book":"Society Guideline","page":49}],"confusable_with":""},
  {"id":"hypoxemic-resp-failure-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"List four causes of hypoxemia that must be distinguished at the bedside.",
   "answer":"Low FiO2, hypoventilation, V/Q mismatch, true intrapulmonary shunt, and diffusion impairment.",
   "rationale":"Each cause has different management; response to supplemental O2 helps distinguish shunt from V/Q mismatch.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":540}],"confusable_with":""},
]

# ITEM 158: Inpatient glucose management — see item 145, this appears to be a near-duplicate
# Using a distinct angle: focus on sliding scale pitfalls and insulin regimen design
topic = "Inpatient glucose management (insulin regimen design)"
domain = "Internal medicine: endocrinology (diabetes & inpatient glucose, DKA & HHS, thyroid disorders & storm, adrenal insufficiency, calcium disorders, pituitary)"
disc = "medicine"
kps += [
  {"id":"inpatient-glucose-mgmt-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Why is a reactive sliding scale alone (correction-only insulin) inadequate for most inpatient diabetics?",
   "answer":"Sliding scale is reactive; it does not prevent hyperglycemia or provide basal coverage, leading to persistent glucose excursions.",
   "rationale":"Basal-bolus regimens proactively match insulin to physiologic needs; reactive-only dosing chases hyperglycemia.",
   "bloom":"analyze","source":[{"book":"Intern Notes / Survival Guide","page":45}],"confusable_with":""},
  {"id":"inpatient-glucose-mgmt-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"How should insulin doses be adjusted when transitioning a patient from TPN to oral diet?",
   "answer":"Reduce basal insulin by 20-30%; add prandial insulin with meals; stop correction coverage built into TPN rate.",
   "rationale":"TPN provides continuous carbohydrate; oral feeding is intermittent, requiring prandial insulin timing to match intake.",
   "bloom":"apply","source":[{"book":"Intern Notes / Survival Guide","page":45}],"confusable_with":""},
  {"id":"inpatient-glucose-mgmt-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What glucose response to a glucagon stimulation test suggests intact glucagon counter-regulation?",
   "answer":"Rise in blood glucose >25 mg/dL within 20 minutes indicates adequate glycogen stores and glucagon responsiveness.",
   "rationale":"Intact counter-regulation is important for recovery from hypoglycemic episodes.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1219}],"confusable_with":""},
  {"id":"inpatient-glucose-mgmt-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What glucose level requires dose adjustment when patient is eating <50% of meals?",
   "answer":"If glucose <180 mg/dL and eating <50%, reduce prandial insulin dose by 50%; if NPO, hold prandial insulin entirely.",
   "rationale":"Reduced caloric intake decreases insulin requirements; excess prandial insulin causes hypoglycemia when meals are missed.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":183}],"confusable_with":""},
  {"id":"inpatient-glucose-mgmt-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the maximum concentration of dextrose that can be safely infused via a peripheral IV?",
   "answer":"10% dextrose (D10W) is the maximum for peripheral veins; higher concentrations require central venous access.",
   "rationale":"Hypertonic dextrose solutions are hyperosmolar and cause phlebitis and thrombosis in peripheral veins.",
   "bloom":"recall","source":[{"book":"Intern Notes / Survival Guide","page":47}],"confusable_with":""},
  {"id":"inpatient-glucose-mgmt-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Steroid-induced hyperglycemia most prominently affects which glucose measurement (fasting vs. postprandial)?",
   "answer":"Steroids predominantly raise postprandial (afternoon/evening) glucose more than fasting glucose.",
   "rationale":"Glucocorticoids impair insulin-stimulated glucose uptake and stimulate hepatic gluconeogenesis preferentially postprandially.",
   "bloom":"analyze","source":[{"book":"MGH Housestaff Manual","page":183}],"confusable_with":""},
]

# ITEM 159: IV Fluids
topic = "IV fluids (principles and selection)"
domain = "General internal medicine, preventive care & geriatrics (admission & cross-cover problems, perioperative medicine, screening & vaccination, polypharmacy & deprescribing, frailty, delirium prevention, goals of care)"
disc = "medicine"
kps += [
  {"id":"iv-fluids-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Why does normal saline (0.9% NaCl) cause a hyperchloremic metabolic acidosis?",
   "answer":"Normal saline contains supraphysiologic chloride (154 mEq/L); chloride excess reduces the strong ion difference (SID), lowering bicarbonate and pH.",
   "rationale":"Stewart's physicochemical principle: SID = [Na+] - [Cl-]; excess Cl− reduces SID and acidifies plasma.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1079}],"confusable_with":"lactated Ringer's (balanced, SID 28 mEq/L)"},
  {"id":"iv-fluids-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Compare the distribution of 1 L of isotonic saline vs. 1 L of D5W after equilibration.",
   "answer":"Isotonic saline stays in ECF (250 mL intravascular); D5W distributes to all body water (250 mL intravascular after dextrose is metabolized leaving free water).",
   "rationale":"Electrolyte solutions cannot cross cell membranes easily; free water distributes to all compartments (intracellular and extracellular).",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1852}],"confusable_with":"colloids (stay intravascular longer)"},
  {"id":"iv-fluids-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In which two clinical scenarios is albumin infusion preferred over crystalloid resuscitation?",
   "answer":"Spontaneous bacterial peritonitis (SBP) in cirrhosis (prevents hepatorenal syndrome) and large-volume paracentesis (>5 L).",
   "rationale":"Albumin maintains oncotic pressure and prevents the circulatory dysfunction that triggers hepatorenal syndrome.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":87}],"confusable_with":""},
  {"id":"iv-fluids-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"For a patient with TBI and cerebral edema, which IV fluid should be avoided and why?",
   "answer":"Hypotonic fluids (0.45% NaCl, D5W) should be avoided; free water crosses the BBB and worsens cerebral edema.",
   "rationale":"Isotonic or hypertonic saline maintains or increases serum osmolality, reducing brain water content.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1368}],"confusable_with":""},
  {"id":"iv-fluids-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the standard fluid challenge for assessing volume responsiveness in a hemodynamically unstable patient?",
   "answer":"250-500 mL isotonic crystalloid (balanced or normal saline) over 5-15 minutes with reassessment of hemodynamic response.",
   "rationale":"Volume challenge tests preload dependence; a >10-15% increase in CO or SV suggests volume responsiveness.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":97}],"confusable_with":""},
  {"id":"iv-fluids-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Which IV fluid is preferred to replace GI losses from the small intestine and why?",
   "answer":"Lactated Ringer's (or balanced crystalloid); small bowel fluid is isotonic with electrolyte composition similar to plasma.",
   "rationale":"Replacing like-for-like fluids minimizes electrolyte disturbances; normal saline causes hyperchloremia.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1079}],"confusable_with":""},
]

# ITEM 160: Iron deficiency anemia
topic = "Iron deficiency anemia"
domain = "Internal medicine: hematology & oncology (anemias, anticoagulation & reversal, VTE prophylaxis & treatment, thrombocytopenia & DIC, transfusion medicine, oncologic emergencies, neutropenic fever)"
disc = "medicine"
kps += [
  {"id":"iron-deficiency-anemia-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What CBC and iron study pattern confirms iron deficiency anemia?",
   "answer":"Low MCV (microcytic), low serum iron, low ferritin, high TIBC; serum ferritin <30 ng/mL is diagnostic.",
   "rationale":"Ferritin reflects total body iron stores; low ferritin confirms iron deficiency even before hemoglobin falls.",
   "bloom":"recall","source":[{"book":"Intern Notes / Survival Guide","page":17}],"confusable_with":"anemia of chronic disease (ferritin normal/high, TIBC low)"},
  {"id":"iron-deficiency-anemia-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In a 55-year-old man with iron deficiency anemia, what is the next mandatory step?",
   "answer":"Evaluate for GI blood loss with colonoscopy ± upper endoscopy; iron deficiency in adult men and postmenopausal women requires GI malignancy exclusion.",
   "rationale":"Iron deficiency without obvious cause in adults is a red flag for colorectal cancer or other GI malignancy.",
   "bloom":"apply","source":[{"book":"Intern Notes / Survival Guide","page":17}],"confusable_with":""},
  {"id":"iron-deficiency-anemia-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"When is IV iron preferred over oral iron?",
   "answer":"IV iron when oral iron is poorly tolerated (GI side effects), malabsorption, IBD, CKD on erythropoietin, preoperative optimization, or inadequate response to oral therapy.",
   "rationale":"Oral iron absorption is limited and slow; IV iron delivers immediate replenishment of stores.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":189}],"confusable_with":""},
  {"id":"iron-deficiency-anemia-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"How quickly do reticulocytes respond after starting iron therapy, and when does hemoglobin normalize?",
   "answer":"Reticulocytosis in 3-5 days; hemoglobin rises measurably by 2 weeks; full correction takes 6-8 weeks; continue 3 months to replenish stores.",
   "rationale":"Reticulocytosis is the earliest hematopoietic response; hemoglobin lags behind iron store replenishment.",
   "bloom":"recall","source":[{"book":"Intern Notes / Survival Guide","page":17}],"confusable_with":""},
  {"id":"iron-deficiency-anemia-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is preoperative intravenous iron therapy indicated for?",
   "answer":"IV iron is indicated for preoperative anemia with iron deficiency when surgery is >=2 weeks away and transfusion risk is high.",
   "rationale":"IV iron rapidly replenishes stores and raises hemoglobin, potentially reducing perioperative transfusion requirements.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1830}],"confusable_with":""},
  {"id":"iron-deficiency-anemia-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the classic symptom triad of Plummer-Vinson syndrome associated with severe iron deficiency?",
   "answer":"Dysphagia from esophageal webs, iron deficiency anemia, and glossitis.",
   "rationale":"Plummer-Vinson is a rare complication of severe chronic iron deficiency, associated with esophageal squamous carcinoma risk.",
   "bloom":"recall","source":[{"book":"Intern Notes / Survival Guide","page":17}],"confusable_with":""},
]

# ITEM 161: Large bowel obstruction (LBO)
topic = "Large bowel obstruction (LBO)"
domain = "Internal medicine: gastroenterology & hepatology (upper & lower GI bleed, acute liver failure, cirrhosis & its complications, pancreatitis, IBD, bowel obstruction, hepatic encephalopathy)"
disc = "medicine"
kps += [
  {"id":"lbo-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What are the two most common causes of large bowel obstruction in adults?",
   "answer":"Colorectal carcinoma (most common) and sigmoid volvulus.",
   "rationale":"Cancer accounts for ~60% of LBO; diverticular disease and sigmoid volvulus are the other leading causes.",
   "bloom":"recall","source":[{"book":"Intern Notes / Survival Guide","page":36}],"confusable_with":"small bowel obstruction (adhesions most common)"},
  {"id":"lbo-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What abdominal X-ray finding is characteristic of sigmoid volvulus?",
   "answer":"Coffee bean sign: a massively dilated loop of sigmoid colon arising from the LLQ with its apex toward the RUQ.",
   "rationale":"Sigmoid volvulus creates a characteristic bent-inner-tube/coffee bean shape as the loop twists on its mesentery.",
   "bloom":"recall","source":[{"book":"Intern Notes / Survival Guide","page":36}],"confusable_with":"cecal volvulus (RLQ-based dilation)"},
  {"id":"lbo-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"At what cecal diameter on CT/X-ray is the risk of perforation highest in colonic pseudo-obstruction (Ogilvie syndrome)?",
   "answer":"Cecal diameter >12 cm carries the highest perforation risk; colonoscopic decompression is indicated.",
   "rationale":"The cecum has the largest diameter in the colon (LaPlace's Law: tension proportional to radius); it is most vulnerable to pressure necrosis.",
   "bloom":"recall","source":[{"book":"Intern Notes / Survival Guide","page":36}],"confusable_with":""},
  {"id":"lbo-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the first-line pharmacologic treatment for Ogilvie syndrome in hemodynamically stable patients?",
   "answer":"Neostigmine 2 mg IV (with cardiac monitoring); contraindicated in bradycardia, bronchospasm, or mechanical obstruction.",
   "rationale":"Neostigmine inhibits acetylcholinesterase, increasing parasympathetic tone and stimulating colonic motility.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":83}],"confusable_with":"polyethylene glycol (ineffective for Ogilvie)"},
  {"id":"lbo-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Compare the clinical presentation of LBO vs. small bowel obstruction (SBO).",
   "answer":"LBO: gradual onset, obstipation, marked abdominal distension, less vomiting. SBO: crampy central pain, early vomiting, less distension, hyperactive bowel sounds early.",
   "rationale":"Colonic obstruction fills a larger reservoir slowly; SBO causes proximal distension and rapid fluid/gas accumulation.",
   "bloom":"analyze","source":[{"book":"Intern Notes / Survival Guide","page":35}],"confusable_with":""},
  {"id":"lbo-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the initial management of a suspected complete LBO with closed-loop obstruction?",
   "answer":"NPO, NG decompression, IV fluids, urgent surgery; closed-loop obstruction risks ischemia and perforation within hours.",
   "rationale":"Closed-loop obstruction traps a segment between two points of obstruction, elevating intraluminal pressure rapidly.",
   "bloom":"apply","source":[{"book":"Intern Notes / Survival Guide","page":36}],"confusable_with":""},
]

# ITEM 162: Lower GI Bleed (LGIB)
topic = "Lower GI Bleed (LGIB)"
domain = "Internal medicine: gastroenterology & hepatology (upper & lower GI bleed, acute liver failure, cirrhosis & its complications, pancreatitis, IBD, bowel obstruction, hepatic encephalopathy)"
disc = "medicine"
kps += [
  {"id":"lgib-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What are the four most common causes of lower GI bleeding in adults over 60?",
   "answer":"Diverticulosis (~40%), angiodysplasia (~20%), colorectal neoplasms, and ischemic colitis.",
   "rationale":"Diverticulosis is the most common cause of significant LGIB; angiodysplasia increases with age.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":70}],"confusable_with":"hemorrhoids (most common cause of rectal bleeding overall, usually minor)"},
  {"id":"lgib-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What percentage of lower GI bleeds stop spontaneously?",
   "answer":"Approximately 75-80% of LGIB stops spontaneously.",
   "rationale":"Most LGIBs are self-limited; persistent or hemodynamically significant bleeding requires endoscopic or angiographic intervention.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":70}],"confusable_with":""},
  {"id":"lgib-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What hemodynamic criteria define a high-risk LGIB requiring urgent intervention?",
   "answer":"Systolic BP <100 mmHg, HR >100 bpm, or >2 units PRBC required in first 24 hours.",
   "rationale":"Hemodynamic instability indicates ongoing significant bleeding requiring prompt endoscopic or angiographic therapy.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":71}],"confusable_with":""},
  {"id":"lgib-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"After resuscitation, what is the initial diagnostic and therapeutic procedure for active LGIB?",
   "answer":"Colonoscopy after bowel preparation (if patient stable); angiography if colonoscopy unavailable or patient too unstable.",
   "rationale":"Colonoscopy localizes the source and allows therapeutic hemostasis; angiography permits embolization for rapid bleeding.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":71}],"confusable_with":"UGIB (EGD first-line)"},
  {"id":"lgib-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Why must an upper GI source always be excluded before managing apparent lower GI bleeding?",
   "answer":"Up to 10-15% of presumed LGIB is from an UGIB source (brisk UGIB with rapid transit can present as bright red rectal bleeding); EGD or NG lavage helps exclude.",
   "rationale":"Management differs fundamentally; a missed UGIB source (e.g., variceal bleed) can be fatal.",
   "bloom":"analyze","source":[{"book":"MGH Housestaff Manual","page":70}],"confusable_with":""},
  {"id":"lgib-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Which anticoagulant reversal agent is used for life-threatening LGIB in a patient on apixaban?",
   "answer":"Andexanet alfa (Factor Xa antagonist) reverses apixaban and rivaroxaban; andexanet has FDA approval for life-threatening bleeding.",
   "rationale":"Direct Factor Xa inhibitors lack a universal reversal agent until andexanet alfa; activated PCC (4F-PCC) is an off-label alternative.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":197}],"confusable_with":"idarucizumab (reverses dabigatran only)"},
]

# ITEM 163: Metabolic acidosis
topic = "Metabolic acidosis"
domain = "General internal medicine, preventive care & geriatrics (admission & cross-cover problems, perioperative medicine, screening & vaccination, polypharmacy & deprescribing, frailty, delirium prevention, goals of care)"
disc = "medicine"
kps += [
  {"id":"metabolic-acidosis-1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"List the causes of high anion gap metabolic acidosis using the MUDPILES mnemonic.",
   "answer":"Methanol, Uremia, DKA/starvation ketosis, Propylene glycol/Paraldehyde, Isoniazid/Iron, Lactic acidosis, Ethylene glycol, Salicylates.",
   "rationale":"High AG acidosis results from accumulation of unmeasured organic acids; AG = Na - (Cl + HCO3), normal 8-12 mEq/L.",
   "bloom":"recall","source":[{"book":"Intern Notes / Survival Guide","page":11}],"confusable_with":"non-AG acidosis (HARDUPS: Hyperalimentation, Acetazolamide, RTA, Diarrhea, Ureterosigmoidostomy, Pancreatic fistula, Saline)"},
  {"id":"metabolic-acidosis-2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the Winter's formula for expected respiratory compensation in metabolic acidosis?",
   "answer":"Expected PaCO2 = 1.5 × HCO3 + 8 ± 2; simpler: PaCO2 should approximately equal the last two digits of pH.",
   "rationale":"Respiratory compensation lowers PaCO2 by hyperventilation; deviation suggests concurrent respiratory disorder.",
   "bloom":"apply","source":[{"book":"Intern Notes / Survival Guide","page":11}],"confusable_with":""},
  {"id":"metabolic-acidosis-3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the delta-delta ratio and how is it used?",
   "answer":"Delta-delta = (AG - 12) / (24 - HCO3). Ratio <1 suggests concurrent non-AG acidosis; >2 suggests concurrent metabolic alkalosis.",
   "rationale":"The delta-delta detects mixed acid-base disorders superimposed on high-AG metabolic acidosis.",
   "bloom":"analyze","source":[{"book":"Intern Notes / Survival Guide","page":11}],"confusable_with":""},
  {"id":"metabolic-acidosis-4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In lactic acidosis, distinguish Type A from Type B by mechanism.",
   "answer":"Type A: tissue hypoperfusion/hypoxemia (shock, cardiac arrest, severe anemia). Type B: normal perfusion (metformin, malignancy, mitochondrial disorders, seizures).",
   "rationale":"Type A drives most critically ill lactic acidosis; Type B is less common but clinically important for medication management.",
   "bloom":"recall","source":[{"book":"Intern Notes / Survival Guide","page":11}],"confusable_with":""},
  {"id":"metabolic-acidosis-5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What urine anion gap (UAG) helps distinguish renal tubular acidosis from GI bicarbonate loss?",
   "answer":"UAG = uNa + uK - uCl. Positive UAG (uNa + uK > uCl) suggests impaired renal NH4+ excretion (RTA); negative UAG suggests GI loss (diarrhea).",
   "rationale":"In GI bicarbonate loss, the kidney compensates by excreting NH4+ (measured as negative UAG); in RTA, NH4+ excretion is impaired.",
   "bloom":"analyze","source":[{"book":"Intern Notes / Survival Guide","page":11}],"confusable_with":""},
  {"id":"metabolic-acidosis-6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"When is sodium bicarbonate indicated in metabolic acidosis?",
   "answer":"pH <7.1 in non-lactic, non-ketotic acidosis (e.g., severe RTA, ingestions, hyperchloremic acidosis); avoid in lactic acidosis (worsens intracellular acidosis).",
   "rationale":"Bicarbonate in lactic acidosis generates CO2 that worsens intracellular pH; treat the underlying cause of lactic acidosis instead.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":165}],"confusable_with":""},
]

with open("data/kp_batch2_out.json", "w", encoding="utf-8") as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)

print("Items:", len(kps))
