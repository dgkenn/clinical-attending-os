import json, sys
sys.path.insert(0, 'data')
from build_kp_part6f import kps

disc = "anesthesia"
dom_obs = "Obstetric anesthesia (maternal physiology, labor analgesia, cesarean anesthesia, preeclampsia/eclampsia, obstetric hemorrhage, emergencies, fetal considerations)"
dom_neuro = "Neuroanesthesia (intracranial pressure & cerebral physiology, craniotomy, awake craniotomy, spine surgery, neuromonitoring, TBI, aneurysm)"
dom_basic = "Anesthesia: basic & clinical sciences (relevant anatomy, respiratory/cardiac/renal/neuro physiology, pharmacokinetics/dynamics principles, physics of gases & flow, statistics)"
dom_preop = "Preoperative evaluation & perioperative medicine (risk stratification, cardiac/pulmonary/endocrine optimization, NPO & aspiration risk, chronic medication management, frailty, consent)"
dom_pain = "Pain medicine (acute perioperative pain, multimodal & opioid management, chronic pain syndromes, interventional techniques, opioid pharmacology & safety)"
dom_pharm = "Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)"
dom_regional = "Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)"

# =====================================================================
# [20] Fetal physiology and assessment
# =====================================================================
topic20 = "Fetal physiology and assessment"

kps += [
  {"id":"fetal-physiology-assessment-d1","topic":topic20,"domain":dom_obs,"discipline":disc,
   "stem":"The neonatal myocardium differs fundamentally from the adult. What is the key implication for calcium-dependent contractility in neonates?",
   "answer":"The neonatal myocardium depends heavily on the concentration of free ionized calcium for contractility; transfusion of blood products to neonates may cause hypocalcemia and depressed cardiac function.",
   "rationale":"Immature sarcoplasmic reticulum with disorganized T-tubules cannot store and release calcium efficiently; neonates rely on extracellular calcium, making them vulnerable to the citrate chelation in stored blood.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":639}],"confusable_with":"adult cardiac calcium handling"},

  {"id":"fetal-physiology-assessment-d2","topic":topic20,"domain":dom_obs,"discipline":disc,
   "stem":"Maternal physiology during pregnancy leads to poor oxygen reserve and rapid desaturation. What two respiratory changes cause this?",
   "answer":"Decreased FRC (from elevated diaphragm reducing expiratory reserve volume) and increased oxygen consumption (from increased metabolic rate) together reduce oxygen reserve and accelerate desaturation during apnea.",
   "rationale":"The combination means pregnant patients have less oxygen stored in the lungs and consume it faster; this is why preoxygenation before any apneic period is critical.",
   "bloom":"apply","source":[{"book":"Stanford CA-1","page":100}],"confusable_with":""},

  {"id":"fetal-physiology-assessment-d3","topic":topic20,"domain":dom_obs,"discipline":disc,
   "stem":"Aortocaval compression occurs in late pregnancy. How is it prevented and why is left uterine displacement specifically recommended?",
   "answer":"Left uterine displacement (manual or with a wedge) is recommended to relieve pressure of the gravid uterus on the inferior vena cava and aorta, preventing supine hypotensive syndrome.",
   "rationale":"The gravid uterus compresses the IVC in supine position, reducing venous return, cardiac output, and uteroplacental perfusion; left displacement shifts the uterus off the IVC.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":935}],"confusable_with":""},

  {"id":"fetal-physiology-assessment-d4","topic":topic20,"domain":dom_obs,"discipline":disc,
   "stem":"Maternal cardiovascular changes in pregnancy include increased cardiac output. What is the approximate increase in cardiac output?",
   "answer":"Cardiac output increases approximately 40-50% during pregnancy, primarily through increased stroke volume early on and then increased heart rate.",
   "rationale":"The increase in blood volume (approximately 40-50%) and decreased SVR from placental arteriovenous shunting drive the cardiac output increase, which must be considered in perioperative hemodynamic management.",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":100}],"confusable_with":""},

  {"id":"fetal-physiology-assessment-d5","topic":topic20,"domain":dom_obs,"discipline":disc,
   "stem":"Respiratory alkalosis occurs during pregnancy due to increased minute ventilation. How is this compensated?",
   "answer":"Pregnancy-induced respiratory alkalosis (from increased tidal volume and RR) is compensated by renal bicarbonate excretion, resulting in a lower serum bicarbonate level than non-pregnant women.",
   "rationale":"Compensatory metabolic acidosis maintains pH near normal; importantly, the reduced bicarbonate buffer reserve makes pregnant patients less able to compensate for acute acidemia.",
   "bloom":"analyze","source":[{"book":"Stanford CA-1","page":100}],"confusable_with":""},

  {"id":"fetal-physiology-assessment-d6","topic":topic20,"domain":dom_obs,"discipline":disc,
   "stem":"The FDA has issued a black box warning for which neuraxial adjunct in obstetrics, and what are the specific concerns?",
   "answer":"Neuraxial clonidine carries a black box warning in obstetrics for increased risk of hypotension and bradycardia.",
   "rationale":"Clonidine's central alpha-2 agonism causes sympatholysis; in the hemodynamically sensitive parturient, this can produce severe hypotension compromising uteroplacental perfusion.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":610}],"confusable_with":"epidural opioids"},

  {"id":"fetal-physiology-assessment-d7","topic":topic20,"domain":dom_obs,"discipline":disc,
   "stem":"When providing anesthesia for nonobstetric surgery during pregnancy, what two specific drug-related concerns must be addressed?",
   "answer":"(1) Avoidance of teratogenic drugs and (2) avoidance of intrauterine fetal hypoxia and prevention of preterm labor.",
   "rationale":"Certain drugs (nitrous oxide, benzodiazepines in first trimester) have teratogenic potential; any anesthetic-related hypotension or hypoxemia can compromise uteroplacental oxygen delivery to the fetus.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":601}],"confusable_with":""},
]

# =====================================================================
# [21] Fluid Management in Neuroanesthesia
# =====================================================================
topic21 = "Fluid Management in Neuroanesthesia"

kps += [
  {"id":"fluid-management-neuroanesthesia-d1","topic":topic21,"domain":dom_neuro,"discipline":disc,
   "stem":"Intracranial hypertension is defined as a sustained ICP above what value?",
   "answer":"Intracranial hypertension is defined as a sustained ICP above 15 mmHg.",
   "rationale":"Normal ICP is 5-15 mmHg; sustained elevation reduces cerebral perfusion pressure (CPP = MAP - ICP) and can cause herniation if untreated.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":967}],"confusable_with":""},

  {"id":"fluid-management-neuroanesthesia-d2","topic":topic21,"domain":dom_neuro,"discipline":disc,
   "stem":"In the neuroanesthesia setting, sedative or opioid premedication should be avoided when what condition is suspected?",
   "answer":"Sedative or opioid premedication is best avoided when intracranial hypertension is suspected; hypercapnia secondary to respiratory depression increases ICP.",
   "rationale":"Opioids and sedatives can cause hypoventilation, raising PaCO2; hypercapnia is a potent cerebral vasodilator that increases CBF and ICP -- dangerous in the already-elevated ICP patient.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":970}],"confusable_with":""},

  {"id":"fluid-management-neuroanesthesia-d3","topic":topic21,"domain":dom_neuro,"discipline":disc,
   "stem":"Vasogenic cerebral edema (from tumor) often responds to what specific medical treatment?",
   "answer":"Vasogenic edema associated with tumors often responds to corticosteroids.",
   "rationale":"Blood-brain barrier disruption allows plasma proteins to leak into brain interstitium; steroids reduce vessel wall permeability by multiple mechanisms, decreasing protein-driven osmotic edema.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":968}],"confusable_with":"cytotoxic edema"},

  {"id":"fluid-management-neuroanesthesia-d4","topic":topic21,"domain":dom_neuro,"discipline":disc,
   "stem":"Water intoxication can cause a specific type of cerebral edema. What is the mechanism?",
   "answer":"Acute decreases in serum osmolality (water intoxication) cause intracellular movement of water into brain cells, resulting in cerebral edema.",
   "rationale":"The brain is enclosed in the skull; when plasma osmolality falls rapidly, osmotic gradients drive water into cells; the rigid calvarium prevents volume compensation, increasing ICP.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":968}],"confusable_with":"vasogenic edema"},

  {"id":"fluid-management-neuroanesthesia-d5","topic":topic21,"domain":dom_neuro,"discipline":disc,
   "stem":"In patients with spinal cord injury and spinal shock, what hemodynamic pattern is expected and what is the initial fluid approach?",
   "answer":"Spinal shock causes hypotension and bradycardia; an IV fluid bolus and use of vasopressors (ketamine for induction may help prevent further BP decrease) are the initial approach.",
   "rationale":"Loss of sympathetic tone from high cord injury causes peripheral vasodilation and relative bradycardia; fluid loading increases preload and vasopressors restore tone until the injury stabilizes.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1013}],"confusable_with":"neurogenic shock vs hemorrhagic shock"},

  {"id":"fluid-management-neuroanesthesia-d6","topic":topic21,"domain":dom_neuro,"discipline":disc,
   "stem":"In direct arterial pressure monitoring for neurosurgical patients, what are two specific indications mentioned?",
   "answer":"Direct arterial pressure monitoring is used for patients with intracranial hypertension (for precise CPP management) and high cervical cord injury (for detecting hemodynamic instability).",
   "rationale":"CPP management requires real-time BP data; beat-to-beat arterial pressure allows rapid identification and treatment of hypotension that would otherwise compromise perfusion pressure.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":970}],"confusable_with":""},

  {"id":"fluid-management-neuroanesthesia-d7","topic":topic21,"domain":dom_neuro,"discipline":disc,
   "stem":"Elevated ICP in the context of neuraxial anesthesia is listed as a major contraindication. Why is ICP elevation specifically relevant to epidural/spinal placement?",
   "answer":"Elevated ICP is a contraindication to neuraxial anesthesia because dural puncture can cause acute CSF pressure changes, potentially precipitating brain herniation.",
   "rationale":"In the setting of elevated ICP, loss of CSF through a dural hole can rapidly reduce spinal CSF pressure, creating a pressure gradient that drives herniation of the cerebellar tonsils or temporal lobe.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1541}],"confusable_with":""},
]

# =====================================================================
# [22] Fluid, Electrolyte, and Osmolality Physiology
# =====================================================================
topic22 = "Fluid, Electrolyte, and Osmolality Physiology"

kps += [
  {"id":"fluid-electrolyte-osmolality-physiology-d1","topic":topic22,"domain":dom_basic,"discipline":disc,
   "stem":"When using hypertonic saline for rapid correction of symptomatic hyponatremia, how is the volume of 3% NaCl calculated?",
   "answer":"Na+ deficit (mEq) = Normal TBW x (Desired P[Na+] - Current P[Na+]); divide by 513 (Na concentration in 3% NaCl in mEq/L) to get volume in liters.",
   "rationale":"Controlled correction targeting 2 mEq/L per hour x desired hours prevents osmotic demyelination; the calculation ensures the appropriate volume of hypertonic saline is infused.",
   "bloom":"apply","source":[{"book":"Marino ICU Book","page":442}],"confusable_with":""},

  {"id":"fluid-electrolyte-osmolality-physiology-d2","topic":topic22,"domain":dom_basic,"discipline":disc,
   "stem":"Ringer's lactate has a higher strong ion difference (SID) than normal saline. What is the clinical consequence with large-volume infusions?",
   "answer":"Ringer's lactate (SID 27) and Plasma-Lyte (SID 50) have alkalinizing effects from lactate/acetate metabolism to bicarbonate, which can be a concern with large-volume accumulation.",
   "rationale":"High-SID solutions generate bicarbonate as anion buffers are metabolized; normal saline has SID=0 and causes hyperchloremic metabolic acidosis -- balanced crystalloids cause less acidosis but may cause mild alkalemia.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":463}],"confusable_with":"normal saline acidosis"},

  {"id":"fluid-electrolyte-osmolality-physiology-d3","topic":topic22,"domain":dom_basic,"discipline":disc,
   "stem":"Osmotic pressure is dependent on what property of solute particles, and why does particle mass not affect osmotic pressure?",
   "answer":"Osmotic pressure depends only on the NUMBER of nondiffusible solute particles, not their mass; this is because the average kinetic energy of particles in solution is similar regardless of mass.",
   "rationale":"Each dissolved particle exerts the same osmotic effect whether it is a small ion or a large protein molecule; this is why sodium (small) dominates ECF osmolality despite lower molecular weight than albumin.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1845}],"confusable_with":"oncotic pressure"},

  {"id":"fluid-electrolyte-osmolality-physiology-d4","topic":topic22,"domain":dom_basic,"discipline":disc,
   "stem":"Mannitol is sometimes administered for renal protection in high-risk patients. What does clinical evidence show about this practice?",
   "answer":"There is no clinical evidence that mannitol provides kidney protection, lessens the severity of AKI, or reduces morbidity/mortality compared with correction of hypovolemia alone.",
   "rationale":"Mannitol's osmotic diuresis was thought to flush tubular debris and reduce cast formation; controlled studies fail to show benefit over simple volume repletion in preventing contrast or ischemic nephropathy.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1079}],"confusable_with":"furosemide for AKI"},

  {"id":"fluid-electrolyte-osmolality-physiology-d5","topic":topic22,"domain":dom_basic,"discipline":disc,
   "stem":"Portal hypertension in cirrhosis causes ascites through what three primary mechanisms?",
   "answer":"(1) Increased portal hydrostatic pressure driving intestinal fluid transudation; (2) hypoalbuminemia decreasing plasma oncotic pressure; (3) seepage of protein-rich lymph from an overloaded hepatic lymphatic system.",
   "rationale":"All three mechanisms reduce the Starling forces that retain fluid in vascular spaces; together they produce massive ascites that is difficult to manage without correcting the underlying cirrhosis.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1199}],"confusable_with":""},

  {"id":"fluid-electrolyte-osmolality-physiology-d6","topic":topic22,"domain":dom_basic,"discipline":disc,
   "stem":"In prerenal AKI, what urinary findings support the diagnosis?",
   "answer":"Urine sodium <10 mEq/L, urine osmolality >450 mOsm/kg, urine specific gravity >1.010, and BUN:Cr ratio >10:1 support prerenal AKI.",
   "rationale":"A healthy kidney conserving sodium in response to volume depletion produces concentrated urine with low sodium; these findings distinguish prerenal from intrinsic renal causes where tubular conservation is impaired.",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":46}],"confusable_with":"ATN"},

  {"id":"fluid-electrolyte-osmolality-physiology-d7","topic":topic22,"domain":dom_basic,"discipline":disc,
   "stem":"Primary adrenal insufficiency causes electrolyte disturbances through mineralocorticoid deficiency. What are the expected electrolyte abnormalities?",
   "answer":"Mineralocorticoid deficiency in primary adrenal insufficiency causes hyponatremia and hyperkalemia from impaired renal sodium retention and potassium excretion.",
   "rationale":"Aldosterone promotes renal sodium reabsorption and potassium secretion; without it, sodium is wasted and potassium accumulates, creating dangerous electrolyte imbalances.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Adrenal Crisis","page":7}],"confusable_with":"secondary adrenal insufficiency"},
]

print(f"Generated so far: {len(kps)} KPs")
print("OK")
