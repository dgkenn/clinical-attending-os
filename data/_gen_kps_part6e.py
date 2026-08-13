import json

with open('C:/Users/Dean/anesthesia_attending/data/_kps_batch4.json', 'r', encoding='utf-8') as f:
    kps = json.load(f)

# ============================================================
# [21] Fluid Management in Neuroanesthesia
# ============================================================
t = "Fluid Management in Neuroanesthesia"
dom = "Neuroanesthesia (intracranial pressure & cerebral physiology, craniotomy, awake craniotomy, spine surgery, neuromonitoring, TBI, aneurysm)"
disc = "anesthesia"
s = "neuro-fluid"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the definition of intracranial hypertension and what are its major causes?",
 "answer":"Intracranial hypertension: sustained ICP above 15 mmHg; caused by expanding tissue or fluid mass, depressed skull fracture, cerebral edema, or obstructive hydrocephalus",
 "rationale":"Monro-Kellie doctrine: the skull is a rigid compartment; any volume increase in one component (brain, blood, CSF) must be compensated by reduction in others or ICP rises.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":967}],"confusable_with":""},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What type of cerebral edema responds to corticosteroids and what type does not?",
 "answer":"Vasogenic edema (especially tumor-associated) responds to dexamethasone; vasogenic edema from trauma does NOT respond to corticosteroids",
 "rationale":"Dexamethasone reduces blood-brain barrier permeability in vasogenic edema from tumors; traumatic edema involves different mechanisms (cytotoxic and ionic) unresponsive to steroids.",
 "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":968}],"confusable_with":"Cytotoxic edema (intracellular, does not respond to steroids)"},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"Why should sedative or opioid premedication be avoided in patients with suspected intracranial hypertension?",
 "answer":"Sedative/opioid premedication should be avoided when ICP elevation is suspected because hypercapnia secondary to respiratory depression increases ICP",
 "rationale":"Opioid-induced hypoventilation raises PaCO2, which is a potent cerebral vasodilator causing further ICP increase in an already hypertensive intracranial compartment.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":970}],"confusable_with":""},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"What intraoperative monitors are standard for most craniotomies?",
 "answer":"Standard for craniotomy: direct intraarterial pressure monitoring AND bladder catheterization; rapid blood pressure changes occur during anesthetic procedures requiring beat-to-beat monitoring",
 "rationale":"Intraarterial monitoring allows immediate detection of BP changes that affect CPP; urine output guides fluid management and reflects hemodynamic status.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":970}],"confusable_with":""},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"After spinal cord transection, when is succinylcholine safe and when is it contraindicated?",
 "answer":"Succinylcholine can be used safely in the FIRST 24 hours after spinal cord injury; should NOT be used thereafter because of life-threatening hyperkalemia risk",
 "rationale":"Denervation causes upregulation of extrajunctional acetylcholine receptors; succinylcholine causes massive potassium efflux from these receptors, causing cardiac arrest.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1013}],"confusable_with":"Other NMBAs (non-depolarizing agents safe throughout)"},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the concern with high-dose mannitol for kidney protection in high-risk patients?",
 "answer":"High-dose mannitol can be NEPHROTOXIC; there is no clinical evidence that mannitol provides kidney protection beyond what is achieved by correcting hypovolemia and preserving renal perfusion",
 "rationale":"Mannitol increases tubular osmolarity and can cause tubular obstruction at high doses; its osmotic diuresis may cause hypovolemia worsening renal perfusion.",
 "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1079}],"confusable_with":"Mannitol for ICP reduction (appropriate use, different from renal protection)"},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"In spinal shock following high cervical spinal cord injury, what anesthetic modifications address hemodynamic instability?",
 "answer":"Spinal shock causes hypotension and bradycardia; IV fluid bolus, ketamine for anesthesia induction (minimal BP reduction), and vasopressors as required; direct arterial pressure monitoring essential",
 "rationale":"High spinal cord injury disrupts sympathetic outflow; ketamine's cardiovascular stimulation (sympathomimetic effect) helps maintain BP, unlike propofol which worsens hypotension.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1013}],"confusable_with":""},
]

# ============================================================
# [22] Fluid, Electrolyte, and Osmolality Physiology
# ============================================================
t = "Fluid, Electrolyte, and Osmolality Physiology"
dom = "Critical care & ICU medicine (sepsis/shock, mechanical ventilation, AKI, electrolytes, hemodynamics, vasopressors, end-organ support)"
disc = "anesthesia"
s = "fluid-electrolyte"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What determines osmotic pressure in body compartments, and what are the dominant determinants in ICF vs. ECF?",
 "answer":"Osmotic pressure depends on the NUMBER of nondiffusible solute particles (not mass); potassium is the most important determinant of intracellular osmotic pressure; sodium is the most important determinant of extracellular osmotic pressure",
 "rationale":"Average kinetic energy of particles is similar regardless of mass; effective osmoles are those that cannot cross cell membranes to equilibrate.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1845}],"confusable_with":""},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What governs fluid exchange between the intracellular and interstitial compartments?",
 "answer":"Fluid exchange between intracellular and interstitial spaces is governed by osmotic forces created by differences in nondiffusible solute concentrations",
 "rationale":"Unlike the vascular compartment (where oncotic pressure and hydrostatic pressure both matter), the cell membrane is a pure osmotic barrier; only osmolality differences drive water movement.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1845}],"confusable_with":"Capillary fluid exchange (Starling forces: oncotic + hydrostatic)"},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"At what serum sodium level do serious manifestations of hyponatremia generally become apparent?",
 "answer":"Serious manifestations of hyponatremia are generally associated with low plasma sodium levels (specific threshold below normal range); the clinical context matters as much as absolute level",
 "rationale":"Acute hyponatremia at moderately low levels causes cerebral edema and seizures; chronic adaptation means very low levels may be tolerated; rate of change matters critically.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1845}],"confusable_with":""},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"How is the sodium deficit calculated for correction of symptomatic hyponatremia with hypertonic saline?",
 "answer":"Na deficit (mEq) = Normal TBW x (Desired P[Na] - Current P[Na]); divide deficit by 513 (concentration of 3% NaCl in mEq/L) to get volume of hypertonic saline needed",
 "rationale":"This formula quantifies the sodium needed to raise plasma sodium to a target level; the 513 denominator reflects the high sodium concentration (513 mEq/L) in 3% NaCl.",
 "bloom":"apply","source":[{"book":"Marino ICU Book","page":442}],"confusable_with":""},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"In patients with liver failure, what mechanisms cause the fluid and electrolyte derangements including ascites?",
 "answer":"Portal hypertension (increased hydrostatic pressure causing transudation) + hypoalbuminemia (decreased oncotic pressure) + lymphatic seepage + impaired renin-angiotensin activation contribute to ascites and edema",
 "rationale":"Each mechanism independently promotes fluid transudation into the peritoneal and interstitial space; combined, they create massive fluid redistribution.",
 "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1199}],"confusable_with":""},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"Primary adrenal insufficiency causes what specific electrolyte abnormalities, and why does this differ from secondary/tertiary adrenal insufficiency?",
 "answer":"Primary adrenal insufficiency causes mineralocorticoid deficiency (direct cortex destruction) leading to hyponatremia and hyperkalemia; secondary/tertiary AI spares the adrenal cortex (aldosterone preserved via renin-angiotensin) so electrolyte disturbances are less severe",
 "rationale":"Aldosterone is regulated by the renin-angiotensin system, not ACTH; secondary/tertiary AI only reduces cortisol (ACTH-dependent), preserving aldosterone and thus sodium/potassium balance.",
 "bloom":"analyze","source":[{"book":"StatPearls: StatPearls   Adrenal Crisis","page":7}],"confusable_with":"Secondary adrenal insufficiency (pure glucocorticoid deficiency)"},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"In oliguria following cardiovascular surgery, what initial assessment distinguishes prerenal from other causes?",
 "answer":"Brisk diuresis in response to an IV fluid challenge suggests acute decrease in intravascular volume (prerenal); lack of response suggests intrinsic renal failure or outflow obstruction",
 "rationale":"Prerenal oliguria responds to volume restoration by improving renal perfusion; intrinsic AKI tubular damage does not improve with volume alone.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":528}],"confusable_with":""},
]

# ============================================================
# [23] Frailty assessment and prehabilitation
# ============================================================
t = "Frailty assessment and prehabilitation"
dom = "Perioperative medicine (preoperative assessment, risk stratification, premedication, ERAS, fluid management, temperature, positioning, post-op care)"
disc = "anesthesia"
s = "frailty-prehab"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What are the four goals of prehabilitation programs before surgery?",
 "answer":"(1) Improved physical fitness; (2) dietary interventions to counteract catabolism and support anabolism with exercise; (3) antistress interventions for resilience; (4) cessation of adverse health habits (alcohol, smoking)",
 "rationale":"Prehabilitation optimizes physiologic reserve before surgical stress; patients with improved fitness tolerate perioperative stress better and recover faster.",
 "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":241}],"confusable_with":"Rehabilitation (postoperative; prehabilitation is preoperative)"},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What are the clinical components of the frailty phenotype identified in the operational frailty score?",
 "answer":"Frailty phenotype: slow gait speed, decreased functional status, weak grip strength; assessed with 6-minute walk test and frailty scoring tools",
 "rationale":"Physical frailty reflects reduced physiologic reserve; these measures predict postoperative morbidity, mortality, and functional decline better than age alone.",
 "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":787}],"confusable_with":"Sarcopenia (muscle mass only; frailty is broader multidomain construct)"},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the Mini-Cog test used for in the preoperative frailty assessment?",
 "answer":"Mini-Cog: 3-item recall + clock draw test used for cognitive assessment in preoperative frailty evaluation; identifies cognitive impairment that predicts postoperative delirium",
 "rationale":"Cognitive frailty is a component of overall frailty; preoperative cognitive impairment is a major independent risk factor for postoperative delirium and POCD.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1494}],"confusable_with":"MMSE (longer, not typically used as perioperative screen)"},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"In the preoperative frailty assessment, what malnutrition screening tools and interventions are recommended?",
 "answer":"PONS, MST, MUST scores for malnutrition screening; preoperative immunonutrition (IMN) and oral nutrition supplementation (ONS) for at least 1 week; IV iron/epoetin alfa for anemia; early postoperative feeding",
 "rationale":"Preoperative nutritional optimization improves immune function, wound healing, and muscle anabolism; anemia correction reduces perioperative transfusion requirements.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":787}],"confusable_with":""},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"What specific opioids should be avoided in elderly and frail patients due to active metabolite accumulation?",
 "answer":"Avoid meperidine (normeperidine -> anticholinergic delirium, seizures) and morphine (morphine-6-glucuronide -> narcosis) in elderly/renal impairment; fentanyl and remifentanil preferred",
 "rationale":"Fentanyl has no active metabolites and remifentanil is organ-independently cleared; older frail patients have reduced renal clearance making metabolite accumulation clinically significant.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":675}],"confusable_with":""},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What preoperative cardiac evaluation algorithm is recommended for elderly frail patients undergoing noncardiac surgery?",
 "answer":"Perform preoperative cardiac evaluation according to the ACC/AHA algorithm for noncardiac surgery; also document functional status and history of falls, assess nutritional status",
 "rationale":"Frail elderly patients have higher baseline cardiovascular risk and worse outcomes from both cardiac events and deconditioning; structured evaluation guides risk reduction strategies.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1492}],"confusable_with":""},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"Why are postoperative pulmonary complications (PPCs) particularly important to prevent in frail patients and how much do they cost?",
 "answer":"PPCs are dangerous and costly: significant complications (pneumonia, pleural effusion, reintubation, prolonged intubation) add an average of $25,000+ per episode; frail patients have higher baseline PPC risk from functional limitations",
 "rationale":"Frailty is associated with sarcopenia, poor respiratory reserve, and impaired cough reflex; prevention of PPCs requires preoperative screening and targeted intervention.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":784}],"confusable_with":""},
]

print(f"KPs so far: {len(kps)}")

with open('C:/Users/Dean/anesthesia_attending/data/_kps_batch5.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Batch 5 saved OK")
