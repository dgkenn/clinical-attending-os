import json, sys
sys.stdout.reconfigure(encoding='utf-8')

kps = []
DI = "anesthesia"

# ── 24: Upper extremity surgery and brachial plexus blocks ───────────────────
T = "Upper extremity surgery and brachial plexus blocks"
D = "Subspecialty & out-of-OR anesthesia (ENT/shared airway, ophthalmology, orthopedics, transplant, vascular, ambulatory/office, non-operating-room anesthesia, robotic, laser)"
kps += [
  {"id":"ue-bpb-1","topic":T,"domain":D,"discipline":DI,
   "stem":"For shoulder procedures, a brachial plexus block with or without a perineural catheter is ideally suited. What are the alternative 'shoulder block' options for distal shoulder analgesia?",
   "answer":"Superior trunk or supraclavicular block combined with suprascapular and axillary nerve blocks (the shoulder block).",
   "rationale":"These distal targets spare the phrenic nerve while providing adequate shoulder analgesia, useful when hemidiaphragmatic paralysis is contraindicated.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1314}],"confusable_with":"Interscalene block (invariably blocks phrenic nerve)"},
  {"id":"ue-bpb-2","topic":T,"domain":D,"discipline":DI,
   "stem":"Intravenous regional anesthesia (Bier block) provides intense but limited anesthesia. What nerves emerge from the brachial plexus proximal to the axillary injection and are therefore spared?",
   "answer":"The musculocutaneous nerve (lateral forearm sensation); it exits the plexus proximal to the axillary level and requires independent block.",
   "rationale":"Local anesthetic deposited in the axillary sheath does not spread proximal enough to anesthetize the musculocutaneous nerve, which leaves the cord before the axilla.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1609}],"confusable_with":""},
  {"id":"ue-bpb-3","topic":T,"domain":D,"discipline":DI,
   "stem":"Patients undergoing peripheral nerve blocks should be monitored with what minimum monitors during the block procedure?",
   "answer":"Pulse oximetry, noninvasive blood pressure, and ECG; end-tidal CO2 and FiO2 measurement should also be available.",
   "rationale":"Local anesthetic systemic toxicity can cause rapid cardiovascular and CNS collapse; monitoring allows early detection and prompt intervention.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1613}],"confusable_with":""},
  {"id":"ue-bpb-4","topic":T,"domain":D,"discipline":DI,
   "stem":"Transcranial motor evoked potentials (Tc-MEPs) require the patient to bite down during monitoring; what injury risk does this create and how is it mitigated?",
   "answer":"Bite injuries to the tongue, lips, and teeth; mitigated by placing bite blocks before Tc-MEP monitoring.",
   "rationale":"Tc-MEPs generate whole-body motor contractions including jaw; without protection, the force of masseter contraction can cause severe oral injury.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":370}],"confusable_with":""},
  {"id":"ue-bpb-5","topic":T,"domain":D,"discipline":DI,
   "stem":"Infraclavicular perineural infusion has been shown to provide analgesia superior to what two other brachial plexus infusion sites?",
   "answer":"Superior to both supraclavicular and axillary perineural infusions for postoperative analgesia.",
   "rationale":"The infraclavicular position of the catheter, posterior to the axillary artery near the cords, provides consistent spread to all three cords of the brachial plexus.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1632}],"confusable_with":""}
]

# ── 25: Urine Output Monitoring ───────────────────────────────────────────────
T = "Urine Output Monitoring"
D = "Anesthesia critical care (shock & resuscitation, sepsis, ARDS & mechanical ventilation, hemodynamic monitoring, AKI, sedation/delirium, nutrition, end-of-life)"
kps += [
  {"id":"urine-output-1","topic":T,"domain":D,"discipline":DI,
   "stem":"Urinary output is described as an imperfect reflection of what four clinical parameters?",
   "answer":"Kidney perfusion, kidney function, renal status, cardiovascular status, and fluid volume status.",
   "rationale":"Urine output can be maintained by non-renal mechanisms (ADH, aldosterone) despite inadequate renal perfusion; noninvasive cardiac monitors provide more reliable assessment.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":213}],"confusable_with":""},
  {"id":"urine-output-2","topic":T,"domain":D,"discipline":DI,
   "stem":"When oliguria develops intraoperatively, what four questions should be systematically answered before treating?",
   "answer":"(1) Is there a problem with the catheter/drainage system? (2) Are hemodynamics compatible with adequate renal function? (3) Could the decrease relate to surgical manipulations? (4) How can the catheter be evaluated?",
   "rationale":"Systematic evaluation prevents unnecessary fluid or drug administration for catheter malfunction masquerading as oliguria.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1086}],"confusable_with":""},
  {"id":"urine-output-3","topic":T,"domain":D,"discipline":DI,
   "stem":"Bladder temperature monitoring via a urinary catheter provides what type of core temperature measurement?",
   "answer":"A measure of core body temperature (correlates well with pulmonary artery temperature at steady state).",
   "rationale":"The bladder is a core compartment; urine temperature reflects mixed venous blood temperature at equilibrium, making it a reliable core temperature site.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":722}],"confusable_with":"Peripheral temperature (extremity; reflects core-to-peripheral gradient)"},
  {"id":"urine-output-4","topic":T,"domain":D,"discipline":DI,
   "stem":"Once anesthesia is induced for major cardiac surgery, what monitoring device is inserted and why?",
   "answer":"An indwelling urinary catheter is inserted to monitor urine output as a surrogate for renal perfusion and adequacy of cardiac output during the procedure.",
   "rationale":"Real-time urine output during bypass and weaning provides a sensitive but non-specific indicator of global organ perfusion adequacy.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":722}],"confusable_with":""},
  {"id":"urine-output-5","topic":T,"domain":D,"discipline":DI,
   "stem":"In the PACU, blood pressure, heart rate, and respiratory rate should be measured at minimum how frequently during routine recovery?",
   "answer":"At least every 5 minutes.",
   "rationale":"Rapid physiologic changes occur in the immediate postoperative period; frequent vital sign measurement ensures early detection of respiratory or hemodynamic compromise.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2100}],"confusable_with":""}
]

# ── 26: Vaporizers: Design, Function & Safety ─────────────────────────────────
T = "Vaporizers: Design, Function & Safety"
D = "Anesthesia equipment (anesthesia machine, vaporizers, ventilators, monitoring, circuits, scavenging, checkout)"
kps += [
  {"id":"vaporizer-1","topic":T,"domain":D,"discipline":DI,
   "stem":"Equipment-related adverse anesthetic outcomes are rarely due to device malfunction; they are more commonly due to what?",
   "answer":"Misuse of anesthesia gas delivery systems; operator lack of familiarity and failure to verify machine function account for most equipment-related closed claims.",
   "rationale":"Human factors (unfamiliarity, failure to check) cause 3x more equipment-related adverse outcomes than actual device malfunction, highlighting the importance of preanesthesia checkout.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":88}],"confusable_with":""},
  {"id":"vaporizer-2","topic":T,"domain":D,"discipline":DI,
   "stem":"The Tec 6 desflurane vaporizer uses a specialized heated sump design. Why does desflurane require a fundamentally different vaporizer design from other volatile agents?",
   "answer":"Desflurane has a very high vapor pressure (boiling point near room temperature at ~23 degrees C); a conventional variable-bypass vaporizer cannot control its vaporization accurately.",
   "rationale":"Standard vaporizers depend on a vapor pressure that is stable at room temperature; desflurane would deliver unpredictable high concentrations without active heating and pressurization.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":262}],"confusable_with":"Sevoflurane (standard Tec 7 variable-bypass vaporizer)"},
  {"id":"vaporizer-3","topic":T,"domain":D,"discipline":DI,
   "stem":"Modern anesthesia machines use what types of flow sensors for measuring gas flow (rather than traditional Thorpe tubes)?",
   "answer":"Hot-wire anemometers, differential pressure transducers, or mass flow sensors; all depend on electrical power to display gas flow.",
   "rationale":"Electronic flow measurement allows integration with ventilator control systems and provides more accurate low-flow measurement than mechanical rotameters.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":258}],"confusable_with":"Rotameter/Thorpe tube (mechanical, not electrical)"},
  {"id":"vaporizer-4","topic":T,"domain":D,"discipline":DI,
   "stem":"During the anesthesia machine checkout, what piped gas supply pressure should be verified as the minimum threshold?",
   "answer":"50 psig for piped gas pressures.",
   "rationale":"Inadequate pipeline pressure compromises the oxygen flush and fresh gas flow delivery; the checkout confirms adequate supply before patient care.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":274}],"confusable_with":"Cylinder pressure (E-cylinder O2 full = 2000 psig; working pressure different)"},
  {"id":"vaporizer-5","topic":T,"domain":D,"discipline":DI,
   "stem":"Safety interlock technology in modern operating rooms is designed to address what primary safety gap?",
   "answer":"Design improvements and systematic examination of system faults are far more effective at promoting safety than creating policies; interlocks enforce correct behavior automatically.",
   "rationale":"Human reliance on policies and memory is prone to failure under stress; physical interlocks (e.g., agent-specific filler connectors, vaporizer interlock preventing multiple agents simultaneously) eliminate entire classes of error.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":59}],"confusable_with":""}
]

print(f"Topics 24-26 drafted: {len(kps)} KPs")
