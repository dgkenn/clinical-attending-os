import json

kps = []

# TOPIC 8: Gas Analysis & Anesthetic Agent Monitoring
kps += [
  {"id":"gasanalysis-1","topic":"Gas Analysis & Anesthetic Agent Monitoring","domain":"Anesthesia monitoring & equipment (anesthesia machine & circuits, ventilators, capnography & gas analysis, pulse oximetry, depth of anesthesia, neuromuscular monitoring, alarms & safety checks)","discipline":"anesthesia",
   "stem":"Volatile anesthetics are measured by what primary physical method in modern anesthetic machines?",
   "answer":"Infrared absorption spectroscopy (primary method for measuring anesthetic gas concentrations)",
   "rationale":"Volatile agents absorb infrared light at specific wavelengths proportional to concentration, enabling continuous accurate monitoring.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":197}],"confusable_with":"Mass spectrometry (accurate but not standard real-time at every machine)"},
  {"id":"gasanalysis-2","topic":"Gas Analysis & Anesthetic Agent Monitoring","domain":"Anesthesia monitoring & equipment (anesthesia machine & circuits, ventilators, capnography & gas analysis, pulse oximetry, depth of anesthesia, neuromuscular monitoring, alarms & safety checks)","discipline":"anesthesia",
   "stem":"Desflurane degraded by desiccated CO2 absorbent containing sodium or potassium hydroxide produces what toxic byproduct?",
   "answer":"Carbon monoxide at potentially clinically important levels (from desflurane + desiccated CO2 absorbent)",
   "rationale":"Volatile agent degradation by alkali in desiccated absorbent generates CO, which binds haemoglobin reducing oxygen-carrying capacity.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":268}],"confusable_with":"Compound A (sevoflurane degradation product, renal concern)"},
  {"id":"gasanalysis-3","topic":"Gas Analysis & Anesthetic Agent Monitoring","domain":"Anesthesia monitoring & equipment (anesthesia machine & circuits, ventilators, capnography & gas analysis, pulse oximetry, depth of anesthesia, neuromuscular monitoring, alarms & safety checks)","discipline":"anesthesia",
   "stem":"What minimum alveolar concentration of volatile agent reduces the risk of intraoperative awareness?",
   "answer":"At least 0.5-0.7 MAC of inhaled agent; choosing potent inhalation agents over TIVA reduces awareness risk",
   "rationale":"Adequate MAC ensures amnesia and unconsciousness; TIVA carries higher awareness risk if drug delivery fails without a MAC monitor.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":204}],"confusable_with":"Any propofol dose guaranteeing unconsciousness (TIVA lacks exhaled gas monitoring)"},
  {"id":"gasanalysis-4","topic":"Gas Analysis & Anesthetic Agent Monitoring","domain":"Anesthesia monitoring & equipment (anesthesia machine & circuits, ventilators, capnography & gas analysis, pulse oximetry, depth of anesthesia, neuromuscular monitoring, alarms & safety checks)","discipline":"anesthesia",
   "stem":"Carbon monoxide diffusing capacity (DLCO) is reduced in what category of lung disease?",
   "answer":"Reduced DLCO is typical of restrictive or interstitial lung disease (reduced alveolar surface for gas exchange)",
   "rationale":"Interstitial fibrosis reduces alveolar-capillary membrane area and diffusion capacity, lowering DLCO independent of airway obstruction.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":876}],"confusable_with":"Obstructive disease (FEV1/FVC reduced but DLCO may be normal or increased)"},
  {"id":"gasanalysis-5","topic":"Gas Analysis & Anesthetic Agent Monitoring","domain":"Anesthesia monitoring & equipment (anesthesia machine & circuits, ventilators, capnography & gas analysis, pulse oximetry, depth of anesthesia, neuromuscular monitoring, alarms & safety checks)","discipline":"anesthesia",
   "stem":"What is the isolated forearm technique used to monitor during anesthesia?",
   "answer":"Isolated forearm technique detects consciousness/awareness by allowing the patient to respond with a hand squeeze while paralyzed",
   "rationale":"Tourniquet on one arm before NMB injection preserves neuromuscular function in that limb, enabling volitional movement as an awareness signal.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":204}],"confusable_with":"BIS monitoring (electroencephalographic awareness monitor)"},
]

# TOPIC 9: Glucose management in pediatrics
kps += [
  {"id":"pedglucose-1","topic":"Glucose management in pediatrics","domain":"Pediatric anesthesia (neonatal physiology, congenital heart, pediatric airway, fluid/glucose management, regional in children)","discipline":"anesthesia",
   "stem":"What metabolic emergency must be avoided in anesthetic management of neonates and premature infants?",
   "answer":"Hypoglycemia must be avoided in neonates; glucose monitoring and dextrose-containing fluids are required",
   "rationale":"Neonates have limited glycogen stores and high metabolic demands; prolonged fasting or glucose-free IV fluids rapidly produce hypoglycemia.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":655}],"confusable_with":"Hyperglycemia as the primary concern in neonates (hypoglycemia is the acute risk)"},
  {"id":"pedglucose-2","topic":"Glucose management in pediatrics","domain":"Pediatric anesthesia (neonatal physiology, congenital heart, pediatric airway, fluid/glucose management, regional in children)","discipline":"anesthesia",
   "stem":"In a DKA patient, what three hormone/counter-regulatory axes drive hyperglycemia pathogenesis?",
   "answer":"Insulin deficiency plus elevated glucagon, catecholamines (stress hormones) drive DKA pathophysiology",
   "rationale":"Insulin deficiency removes glucose uptake while glucagon and catecholamines promote gluconeogenesis and lipolysis, fueling ketogenesis.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":184}],"confusable_with":"Cortisol as the dominant driver (it contributes but glucagon/catecholamines are primary)"},
  {"id":"pedglucose-3","topic":"Glucose management in pediatrics","domain":"Pediatric anesthesia (neonatal physiology, congenital heart, pediatric airway, fluid/glucose management, regional in children)","discipline":"anesthesia",
   "stem":"What ADA screening age and interval is recommended for type 2 diabetes in asymptomatic adults?",
   "answer":"Begin screening at age 35 years, repeat every 3 years if normal; every 1 year if pre-diabetes",
   "rationale":"Earlier detection allows lifestyle modification or pharmacotherapy to delay progression to overt type 2 diabetes.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":181}],"confusable_with":"Screening all adults from age 18 regardless of risk (current ADA recommendation is age 35)"},
  {"id":"pedglucose-4","topic":"Glucose management in pediatrics","domain":"Pediatric anesthesia (neonatal physiology, congenital heart, pediatric airway, fluid/glucose management, regional in children)","discipline":"anesthesia",
   "stem":"In the 4-2-1 rule, what is the maintenance fluid rate per hour for the first 10 kg of body weight?",
   "answer":"4 mL/kg/h for the first 10 kg (40 mL/h for a 10 kg child)",
   "rationale":"The Holliday-Segar 4-2-1 formula provides caloric and fluid requirements proportional to metabolic rate at each weight tier.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Hemorrhagic Shock Classification & Management","page":9}],"confusable_with":"2 mL/kg/h for first 10 kg (that is the rate for 10-20 kg tier)"},
]

# TOPIC 10: Glycemic Management in the ICU
kps += [
  {"id":"icuglucose-1","topic":"Glycemic Management in the ICU","domain":"Anesthesia critical care (shock & resuscitation, sepsis, ARDS & mechanical ventilation, hemodynamic monitoring, AKI, sedation/delirium, nutrition, end-of-life)","discipline":"anesthesia",
   "stem":"In ICU patients, intensive insulin therapy targeting glucose 80-110 mg/dL carries what serious risk compared with conventional targets?",
   "answer":"Significantly increased risk of hypoglycemia (glucose <40 mg/dL) with intensive insulin therapy in ICU patients",
   "rationale":"Tight glucose targets require frequent dosing adjustments; critical illness causes unpredictable insulin sensitivity fluctuations, raising severe hypoglycemia risk.",
   "bloom":"apply","source":[{"book":"Society Guideline: Guideline   KDIGO 2012 AKI","page":47}],"confusable_with":"Intensive insulin therapy being universally beneficial after NICE-SUGAR trial"},
  {"id":"icuglucose-2","topic":"Glycemic Management in the ICU","domain":"Anesthesia critical care (shock & resuscitation, sepsis, ARDS & mechanical ventilation, hemodynamic monitoring, AKI, sedation/delirium, nutrition, end-of-life)","discipline":"anesthesia",
   "stem":"What are the two sepsis pathophysiology features that cause relative hypovolemia in the ICU?",
   "answer":"Systemic blood pooling and fluid transudation into tissues causing relative hypovolemia in sepsis",
   "rationale":"Cytokine-mediated vasodilation pools blood peripherally while capillary leak shifts fluid extravascularly, both reducing effective circulating volume.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2126}],"confusable_with":"Absolute volume depletion from hemorrhage (different mechanism in sepsis)"},
  {"id":"icuglucose-3","topic":"Glycemic Management in the ICU","domain":"Anesthesia critical care (shock & resuscitation, sepsis, ARDS & mechanical ventilation, hemodynamic monitoring, AKI, sedation/delirium, nutrition, end-of-life)","discipline":"anesthesia",
   "stem":"What drug interaction must be avoided when correcting potassium deficiency with potassium chloride to prevent exacerbating metabolic alkalosis?",
   "answer":"Potassium chloride is the preferred salt when metabolic alkalosis is present because it provides chloride to correct the alkalosis",
   "rationale":"Metabolic alkalosis is often a chloride-responsive state; replacing K+ as KCl simultaneously corrects the chloride deficit sustaining the alkalosis.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1882}],"confusable_with":"Potassium phosphate or potassium bicarbonate which would worsen alkalosis"},
  {"id":"icuglucose-4","topic":"Glycemic Management in the ICU","domain":"Anesthesia critical care (shock & resuscitation, sepsis, ARDS & mechanical ventilation, hemodynamic monitoring, AKI, sedation/delirium, nutrition, end-of-life)","discipline":"anesthesia",
   "stem":"Beta-agonists can be used to acutely lower plasma potassium by what mechanism?",
   "answer":"Beta-agonists promote cellular uptake of potassium; useful in acute hyperkalemia associated with massive transfusion",
   "rationale":"Beta-2 receptor activation stimulates Na/K-ATPase, driving potassium intracellularly; low-dose epinephrine can rapidly lower plasma K+.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1887}],"confusable_with":"Calcium gluconate (stabilizes membrane, does not shift potassium)"},
]

print(f"Batch C: {len(kps)} entries")
with open('C:/Users/Dean/anesthesia_attending/data/kp_batch6c_out.json','w',encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("OK")
