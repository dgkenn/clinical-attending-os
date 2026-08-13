import json, sys
sys.path.insert(0, 'data')
from build_kp_part6h import kps

disc = "anesthesia"
dom_basic = "Anesthesia: basic & clinical sciences (relevant anatomy, respiratory/cardiac/renal/neuro physiology, pharmacokinetics/dynamics principles, physics of gases & flow, statistics)"
dom_obs = "Obstetric anesthesia (maternal physiology, labor analgesia, cesarean anesthesia, preeclampsia/eclampsia, obstetric hemorrhage, emergencies, fetal considerations)"
dom_pharm = "Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)"
dom_pain = "Pain medicine (acute perioperative pain, multimodal & opioid management, chronic pain syndromes, interventional techniques, opioid pharmacology & safety)"
dom_ethics = "Patient safety, ethics, professionalism & quality (closed-claims lessons, never events, root-cause analysis, informed consent, communication, handoffs, wellness)"
dom_regional = "Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)"

# =====================================================================
# [26] Gas Flow Physics and Anesthesia Machine
# =====================================================================
topic26 = "Gas Flow Physics and Anesthesia Machine"

kps += [
  {"id":"gas-flow-physics-anesthesia-machine-d1","topic":topic26,"domain":dom_basic,"discipline":disc,
   "stem":"Electronic flowmeters in modern anesthesia machines measure gas flow differently from traditional Thorpe tubes. What is the measurement principle?",
   "answer":"Electronic flowmeters measure gas flow based on the amount of pressure drop caused by a flow restrictor; each gas (oxygen, nitrous oxide, air) has a separate electronic flow measurement device.",
   "rationale":"Pressure drop across a fixed restriction is proportional to flow rate (Hagen-Poiseuille law for laminar flow); electronic transducers convert this pressure difference to a digital flow readout.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":102}],"confusable_with":"variable-area flowmeter (Thorpe tube)"},

  {"id":"gas-flow-physics-anesthesia-machine-d2","topic":topic26,"domain":dom_basic,"discipline":disc,
   "stem":"What is the function of the oxygen analyzer in the breathing circuit and what alarm threshold is required?",
   "answer":"The oxygen analyzer monitors inspired oxygen concentration and must alarm within 30 seconds when FiO2 drops below a set limit that cannot be adjusted to less than 18%.",
   "rationale":"This galvanic cell sensor is the final safeguard against delivering a hypoxic mixture; upstream failures (pin index, proportional valve) can go undetected without this independent check.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":266}],"confusable_with":""},

  {"id":"gas-flow-physics-anesthesia-machine-d3","topic":topic26,"domain":dom_basic,"discipline":disc,
   "stem":"Sevoflurane forms compound A in CO2 absorbent (particularly alkali such as barium hydroxide lime or soda lime), but NOT in calcium hydroxide. What is the guideline to prevent rebreathing of compound A?",
   "answer":"Guidelines recommend keeping fresh gas flows >2 L/min to prevent REBREATHING of compound A (not to prevent its formation); compound A itself does not form with calcium hydroxide absorbent.",
   "rationale":"Low-flow techniques allow compound A to accumulate in the circuit from rebreathing; higher flows dilute and flush compound A; the clinical relevance in humans (nephrotoxicity) is controversial.",
   "bloom":"apply","source":[{"book":"Stanford CA-1","page":20}],"confusable_with":"isoflurane CO formation"},

  {"id":"gas-flow-physics-anesthesia-machine-d4","topic":topic26,"domain":dom_basic,"discipline":disc,
   "stem":"MAC-awake (MAC-Aware) for volatile agents is approximately what fraction of MAC, and what does it represent clinically?",
   "answer":"MAC-awake is approximately 0.4 MAC for volatile agents (0.6 MAC for nitrous oxide); it is the concentration preventing response to verbal/tactile stimulation in 50% of patients.",
   "rationale":"At 1.0 MAC patients are immobile to noxious stimuli; at lower concentrations they may still respond to voice; MAC-awake defines the threshold below which explicit awareness is likely.",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":23}],"confusable_with":"MAC-BAR"},

  {"id":"gas-flow-physics-anesthesia-machine-d5","topic":topic26,"domain":dom_basic,"discipline":disc,
   "stem":"Neonates and infants have a proportionately greater total body water content than adults. What percentage is it in neonates vs adults?",
   "answer":"Neonates have total water content of approximately 70-75% of body weight; adults have approximately 50-60%.",
   "rationale":"Higher total body water in neonates creates a larger volume of distribution for water-soluble drugs, requiring higher weight-based loading doses; this is the pharmacokinetic basis for allometric dosing.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1454}],"confusable_with":""},

  {"id":"gas-flow-physics-anesthesia-machine-d6","topic":topic26,"domain":dom_basic,"discipline":disc,
   "stem":"The blood:gas partition coefficient of nitrous oxide is 0.47. What does this mean for its uptake kinetics compared with agents with higher blood:gas coefficients?",
   "answer":"A blood:gas coefficient of 0.47 means nitrous oxide is relatively insoluble in blood; at steady state 1 mL of blood contains only 0.47x as much N2O as 1 mL of alveolar gas, resulting in rapid equilibration and fast onset/offset.",
   "rationale":"Less soluble agents equilibrate more quickly between alveolar and blood phases; minimal blood binding means alveolar concentration rises quickly to match inspired concentration.",
   "bloom":"analyze","source":[{"book":"Stanford CA-1","page":19}],"confusable_with":"halothane (high blood:gas coefficient)"},

  {"id":"gas-flow-physics-anesthesia-machine-d7","topic":topic26,"domain":dom_basic,"discipline":disc,
   "stem":"In infants, the greater minute ventilation-to-FRC ratio speeds inhalation induction. How does MAC for halogenated agents in infants compare with neonates and adults?",
   "answer":"MAC for halogenated agents is GREATER in infants than in neonates and adults; sevoflurane is an exception -- no increase in MAC can be demonstrated between neonates and infants.",
   "rationale":"Higher MAC in infants reflects immature CNS neurodevelopment and increased metabolic activity; the rapid inhalation induction speeds delivery of these higher concentrations to the CNS.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1443}],"confusable_with":""},
]

# =====================================================================
# [27] General anesthesia for cesarean delivery
# =====================================================================
topic27 = "General anesthesia for cesarean delivery"

kps += [
  {"id":"general-anesthesia-cesarean-delivery-d1","topic":topic27,"domain":dom_obs,"discipline":disc,
   "stem":"In the suggested technique for general anesthesia for cesarean section, what are the induction agents of choice and their doses?",
   "answer":"Rapid-sequence induction: propofol 2 mg/kg or ketamine 1-2 mg/kg with succinylcholine 1.5 mg/kg; ketamine is used instead of propofol in hypovolemic patients.",
   "rationale":"Propofol provides smooth hemodynamic induction in stable patients; ketamine's sympathomimetic effect maintains cardiac output in hemorrhagic or hemodynamically compromised patients.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1411}],"confusable_with":""},

  {"id":"general-anesthesia-cesarean-delivery-d2","topic":topic27,"domain":dom_obs,"discipline":disc,
   "stem":"General anesthesia for vaginal delivery is avoided except for what specific circumstance?",
   "answer":"General anesthesia for vaginal delivery is avoided except for a true emergency because of the increased risk of aspiration in the pregnant patient.",
   "rationale":"Pregnancy causes reduced LES tone, increased intragastric pressure, and delayed gastric emptying; combined with difficult airway risk from edema and obesity, GA carries substantially higher aspiration risk.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1402}],"confusable_with":""},

  {"id":"general-anesthesia-cesarean-delivery-d3","topic":topic27,"domain":dom_obs,"discipline":disc,
   "stem":"The step-by-step technique for GA for cesarean includes denitrogenation before induction. How long should preoxygenation last?",
   "answer":"Denitrogenation is accomplished with 100% oxygen for 3-5 minutes while monitors are applied; alternatively, 4 maximal breaths over 30 seconds is an accepted rapid alternative.",
   "rationale":"Pregnancy reduces FRC and increases O2 consumption; preoxygenation replaces nitrogen in the FRC with oxygen, extending the apneic safe period during rapid-sequence induction.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1411}],"confusable_with":""},

  {"id":"general-anesthesia-cesarean-delivery-d4","topic":topic27,"domain":dom_obs,"discipline":disc,
   "stem":"Indications for emergency cesarean delivery requiring immediate delivery (crash C-section) include what specific obstetric emergencies?",
   "answer":"Massive bleeding (placenta previa/accreta, abruption, uterine rupture), umbilical cord prolapse, and severe fetal distress are indications for emergency cesarean.",
   "rationale":"Each of these can cause rapid fetal demise or maternal hemorrhage; the time-critical nature dictates that anesthetic technique selection prioritizes speed of onset.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1412}],"confusable_with":""},

  {"id":"general-anesthesia-cesarean-delivery-d5","topic":topic27,"domain":dom_obs,"discipline":disc,
   "stem":"The combination of decreased FRC and increased oxygen consumption in pregnancy promotes what dangerous condition during anesthesia?",
   "answer":"The combination of decreased FRC and increased oxygen consumption promotes rapid arterial desaturation during periods of apnea; this is why preoxygenation is critical before induction.",
   "rationale":"FRC represents the oxygen reservoir in the lungs; decreased reserve plus increased consumption means the pregnant patient exhausts her oxygen stores 2-3 times faster than a non-pregnant adult.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1359}],"confusable_with":""},

  {"id":"general-anesthesia-cesarean-delivery-d6","topic":topic27,"domain":dom_obs,"discipline":disc,
   "stem":"During active postpartum hemorrhage from placenta previa, what specific hemostatic consideration applies to the lower uterine segment?",
   "answer":"The placental implantation site in the lower uterine segment often does not contract as well as the rest of the uterus after delivery, so bleeding can continue post-delivery.",
   "rationale":"Lower uterine segment has proportionally less myometrium and poor contractile response to oxytocin; this anatomical feature predicts persistent hemorrhage requiring additional uterotonics, intrauterine balloon, or hysterectomy.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1416}],"confusable_with":""},

  {"id":"general-anesthesia-cesarean-delivery-d7","topic":topic27,"domain":dom_obs,"discipline":disc,
   "stem":"Anesthesia-related closed claims in obstetrics often involve delays in care for emergency cesarean delivery. What are the documented contributing factors?",
   "answer":"Payments involved delays in care, miscommunication about urgency level, concerns about difficult intubation or high spinal block, and lapses in documentation or record keeping.",
   "rationale":"Closed claims data demonstrate that communication failures and cognitive biases (anchoring on less urgent classification) are more common causes than pure technical failures in obstetric anesthesia adverse events.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1387}],"confusable_with":""},
]

print(f"Generated so far: {len(kps)} KPs")
print("OK")
