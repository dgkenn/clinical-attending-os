import json, sys
sys.path.insert(0, 'data')
from build_kp_part6b import kps

disc = "anesthesia"

# =====================================================================
# [8] Enhanced Recovery After Surgery (ERAS)
# =====================================================================
topic8 = "Enhanced Recovery After Surgery (ERAS)"
dom8 = "Pain medicine (acute perioperative pain, multimodal & opioid management, chronic pain syndromes, interventional techniques, opioid pharmacology & safety)"

kps += [
  {"id":"enhanced-recovery-after-surgery-eras-d1","topic":topic8,"domain":dom8,"discipline":disc,
   "stem":"What are ERAS programs also termed, and what is the key principle that ties them together?",
   "answer":"ERAS programs are also called enhanced recovery programs (ERPs) or fast-track surgery; they are coordinated, multidisciplinary perioperative care programs designed to reduce surgical stress and accelerate recovery.",
   "rationale":"By standardizing evidence-based pre-, intra-, and postoperative protocols across disciplines, ERAS reduces complications, length of stay, and hospitalization costs.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1813}],"confusable_with":""},

  {"id":"enhanced-recovery-after-surgery-eras-d2","topic":topic8,"domain":dom8,"discipline":disc,
   "stem":"In an ERAS protocol, why should nasogastric tubes be discouraged or used only briefly, even in gastrointestinal surgery?",
   "answer":"Nasogastric tubes should be discouraged or used only very briefly; the opioid-sparing effects of multimodal analgesia shorten postoperative ileus or may prevent it entirely.",
   "rationale":"Routine NGT use prolongs ileus by maintaining NPO status; removal encourages early oral intake, gut motility, and ambulation -- all key ERAS elements.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1813}],"confusable_with":""},

  {"id":"enhanced-recovery-after-surgery-eras-d3","topic":topic8,"domain":dom8,"discipline":disc,
   "stem":"In perioperative fluid management as part of ERAS, what is the principle regarding fluid balance?",
   "answer":"Both excessive and excessively restricted perioperative fluid therapy increases complications; goal-directed fluid management optimizing euvolemia is key to ERAS.",
   "rationale":"Fluid overload impairs gut healing and causes tissue edema; underfilling causes organ hypoperfusion; individualized, goal-directed therapy threaded through ERAS protocols optimizes outcomes.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1813}],"confusable_with":""},

  {"id":"enhanced-recovery-after-surgery-eras-d4","topic":topic8,"domain":dom8,"discipline":disc,
   "stem":"A patient's initial contact with an ERAS program ideally occurs at what time?",
   "answer":"The initial contact ideally occurs at the time of the preoperative evaluation visit.",
   "rationale":"Early enrollment allows ERAS education, optimization, prehabilitation, preoperative carbohydrate loading, and analgesia planning before the patient arrives for surgery.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":475}],"confusable_with":""},

  {"id":"enhanced-recovery-after-surgery-eras-d5","topic":topic8,"domain":dom8,"discipline":disc,
   "stem":"Multimodal analgesia is a cornerstone of ERAS. What does this approach typically combine to minimize opioid use?",
   "answer":"Multimodal analgesia combines interventional techniques (epidural, peripheral nerve blocks/catheters) with systemic pharmacology (NSAIDs, alpha-adrenergic agonists, NMDA antagonists, membrane stabilizers), minimizing opioid use.",
   "rationale":"Different analgesic classes act at different sites in the pain pathway; combining them allows lower doses of each, reducing side effects while maintaining efficacy.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":744}],"confusable_with":""},

  {"id":"enhanced-recovery-after-surgery-eras-d6","topic":topic8,"domain":dom8,"discipline":disc,
   "stem":"There is strong evidence that non-diabetic patients who drink carbohydrate-containing fluids up to 2 hours before induction of general anesthesia benefit how?",
   "answer":"Non-diabetic patients who drink carbohydrate-containing fluids up to 2 hours before induction experience less perioperative discomfort and metabolic stress compared with prolonged fasting.",
   "rationale":"Preoperative carbohydrate loading attenuates the surgical stress response, reduces postoperative insulin resistance, improves patient well-being, and is a core ERAS element.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":475}],"confusable_with":"standard NPO guidelines"},

  {"id":"enhanced-recovery-after-surgery-eras-d7","topic":topic8,"domain":dom8,"discipline":disc,
   "stem":"How does morphine accumulation pose a specific risk in patients with kidney failure, as relevant to opioid choice within ERAS protocols?",
   "answer":"Morphine metabolites (morphine-3-glucuronide and morphine-6-glucuronide) accumulate in kidney failure, causing narcosis and ventilatory depression.",
   "rationale":"Both morphine glucuronides are renally excreted; M6G is a potent opioid agonist that accumulates to toxic levels in renal insufficiency, making morphine a poor choice in this population.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":299}],"confusable_with":"fentanyl in renal failure"},
]

# =====================================================================
# [9] Enhanced recovery after cesarean (ERAC)
# =====================================================================
topic9 = "Enhanced recovery after cesarean (ERAC)"
dom9 = "Obstetric anesthesia (maternal physiology, labor analgesia, cesarean anesthesia, preeclampsia/eclampsia, obstetric hemorrhage, emergencies, fetal considerations)"

kps += [
  {"id":"enhanced-recovery-after-cesarean-erac-d1","topic":topic9,"domain":dom9,"discipline":disc,
   "stem":"Epidural analgesia provides superior postoperative respiratory outcomes compared with systemic opioid analgesia in non-cardiac surgery. What does this imply for ERAC protocols?",
   "answer":"Neuraxial analgesia (spinal/epidural) reduces opioid requirements and improves respiratory outcomes; ERAC leverages intrathecal opioids and multimodal non-opioid analgesia to support early ambulation.",
   "rationale":"Neuraxial techniques produce superior analgesia with less respiratory depression than IV opioids; combining with NSAIDs, acetaminophen, and regional blocks enables opioid-minimizing recovery.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":314}],"confusable_with":""},

  {"id":"enhanced-recovery-after-cesarean-erac-d2","topic":topic9,"domain":dom9,"discipline":disc,
   "stem":"In ERAC, why is early oral feeding and ambulation specifically important in the postoperative period?",
   "answer":"Early feeding maintains gut motility, reduces insulin resistance, and supports anabolism; early ambulation prevents DVT, reduces pulmonary complications, and shortens hospital stay.",
   "rationale":"The metabolic stress response to cesarean surgery causes protein catabolism and insulin resistance; early nutrition and mobility counteract these physiological changes and support recovery.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":475}],"confusable_with":""},

  {"id":"enhanced-recovery-after-cesarean-erac-d3","topic":topic9,"domain":dom9,"discipline":disc,
   "stem":"In ERAC, aspirin serves as an anticoagulant component. However, aspirin inhibits COX-1 uniquely among NSAIDs. How does its inhibition differ mechanistically?",
   "answer":"Aspirin irreversibly inhibits COX-1 by acetylating a serine residue in the enzyme, causing a near-1-week persistence of platelet inhibition (platelet lifespan duration).",
   "rationale":"Unlike reversible NSAID COX inhibition that lasts the drug's half-life, aspirin's covalent modification persists until new platelets are generated (7-10 days), relevant for bleeding risk assessment.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":313}],"confusable_with":"other NSAIDs"},

  {"id":"enhanced-recovery-after-cesarean-erac-d4","topic":topic9,"domain":dom9,"discipline":disc,
   "stem":"In the context of ERAC and opioid reduction, large-dose rapid IV opioid bolus (fentanyl, sufentanil, remifentanil, alfentanil) carries what specific risk?",
   "answer":"Rapid administration of large doses of these opioids can induce chest wall rigidity severe enough to make ventilation with bag and mask nearly impossible.",
   "rationale":"High-dose rapid opioid injection activates mu receptors on thoracic and abdominal musculature; glottic closure and truncal rigidity ('wooden chest') prevent effective ventilation.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":299}],"confusable_with":"laryngospasm"},

  {"id":"enhanced-recovery-after-cesarean-erac-d5","topic":topic9,"domain":dom9,"discipline":disc,
   "stem":"The ASA closed claims study highlights specific anesthetic risks during monitored anesthesia care (MAC). How is risk during MAC compared with general or regional anesthesia?",
   "answer":"The anesthetic risks associated with MAC are not necessarily different from those of general or regional anesthesia -- airway and cardiovascular complications can still occur.",
   "rationale":"MAC can progress to unintended deep sedation; the physiological monitoring requirements and vigilance needed are equivalent to other anesthetic techniques.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":247}],"confusable_with":""},

  {"id":"enhanced-recovery-after-cesarean-erac-d6","topic":topic9,"domain":dom9,"discipline":disc,
   "stem":"In ERAC, acetaminophen and ibuprofen are commonly used COX inhibitors. What is the maximum safe daily dose of acetaminophen in patients with liver disease?",
   "answer":"Maximum acetaminophen dose is 4g/day in healthy patients; 2-3g/day is safe in patients with liver disease.",
   "rationale":"Acetaminophen undergoes hepatic metabolism to a toxic metabolite (NAPQI) that is normally conjugated by glutathione; in liver disease, reduced glutathione reserve increases NAPQI accumulation and hepatotoxicity risk.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":164}],"confusable_with":""},

  {"id":"enhanced-recovery-after-cesarean-erac-d7","topic":topic9,"domain":dom9,"discipline":disc,
   "stem":"Prolonged dosing of opioids as part of pain management can produce what specific concern beyond tolerance?",
   "answer":"Prolonged opioid dosing can produce opioid-induced hyperalgesia -- paradoxical increased pain sensitivity with continued use.",
   "rationale":"Chronic opioid receptor activation triggers neuroplastic changes including central sensitization and descending facilitation, causing patients to become more sensitive to pain over time.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":299}],"confusable_with":"opioid tolerance"},
]

# =====================================================================
# [10] Epidural anesthesia for cesarean delivery
# =====================================================================
topic10 = "Epidural anesthesia for cesarean delivery"
dom10 = dom9

kps += [
  {"id":"epidural-anesthesia-cesarean-delivery-d1","topic":topic10,"domain":dom10,"discipline":disc,
   "stem":"For epidural anesthesia in cesarean delivery, what sensory level must be achieved and maintained?",
   "answer":"A T4 sensory level is required for cesarean delivery, as the peritoneum (innervated to T4) is manipulated; if the level recedes, additional local anesthetic is given in 5 mL increments.",
   "rationale":"Uterine and peritoneal manipulation sends afferent signals via T10-T4 nerve roots; inadequate block above T4 causes visceral pain during surgery.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1406}],"confusable_with":"T10 level for labor analgesia"},

  {"id":"epidural-anesthesia-cesarean-delivery-d2","topic":topic10,"domain":dom10,"discipline":disc,
   "stem":"When converting a labor epidural to cesarean anesthesia and block is patchy prior to delivery, what IV agents can supplement without causing excessive sedation?",
   "answer":"Patchy anesthesia prior to delivery can be treated with ketamine 10-20 mg IV combined with midazolam 1-2 mg, or 30% nitrous oxide; post-delivery IV opioids may also be added.",
   "rationale":"These agents supplement analgesia/sedation at sub-anesthetic doses; ketamine before delivery avoids excessive neonatal sedation, and nitrous oxide provides rapid-onset anxiolysis.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1406}],"confusable_with":""},

  {"id":"epidural-anesthesia-cesarean-delivery-d3","topic":topic10,"domain":dom10,"discipline":disc,
   "stem":"For anesthesia for emergency cesarean delivery, what distinction must be made before choosing the anesthetic technique?",
   "answer":"A distinction must be made between a true emergency requiring immediate delivery and one in which some delay is possible; communication with the obstetrician is essential to determine if the fetus, mother, or both are in immediate jeopardy.",
   "rationale":"True emergencies (cord prolapse with fetal bradycardia) require fastest-onset anesthesia (general or existing epidural top-up); less urgent cases allow time for spinal anesthesia.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1412}],"confusable_with":""},

  {"id":"epidural-anesthesia-cesarean-delivery-d4","topic":topic10,"domain":dom10,"discipline":disc,
   "stem":"A functioning labor epidural catheter provides an important contingency advantage. What specifically?",
   "answer":"The presence of a functioning epidural catheter makes it possible to avoid general anesthesia if urgent or emergency cesarean section becomes necessary.",
   "rationale":"GA for cesarean carries higher risk due to difficult airway (edema, obesity), aspiration, and neonatal depression; a pre-existing epidural allows rapid extension of block, avoiding these risks.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1394}],"confusable_with":""},

  {"id":"epidural-anesthesia-cesarean-delivery-d5","topic":topic10,"domain":dom10,"discipline":disc,
   "stem":"Compared with epidural anesthesia for cesarean delivery, what are three advantages of spinal anesthesia?",
   "answer":"Spinal anesthesia has more rapid and predictable onset, may produce a denser (more complete) block, and lacks the potential for serious systemic drug toxicity because a smaller local anesthetic dose is used.",
   "rationale":"Smaller intrathecal volumes achieve equivalent or better anesthesia than larger epidural volumes; systemic absorption is minimal, virtually eliminating the risk of local anesthetic toxicity.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1404}],"confusable_with":""},

  {"id":"epidural-anesthesia-cesarean-delivery-d6","topic":topic10,"domain":dom10,"discipline":disc,
   "stem":"The addition of fentanyl or sufentanil to intrathecal local anesthetic for cesarean delivery provides what benefit, and what doses are used?",
   "answer":"Adding fentanyl 12.5-25 mcg or sufentanil 5-7.5 mcg significantly potentiates the block; a T10 sensory level can be obtained with slightly larger amounts of local anesthetic when opioids are added.",
   "rationale":"Intrathecal opioids act on spinal cord mu-receptors to produce analgesia that is synergistic with local anesthetic, improving block quality and extending duration without additional systemic effects.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1402}],"confusable_with":""},

  {"id":"epidural-anesthesia-cesarean-delivery-d7","topic":topic10,"domain":dom10,"discipline":disc,
   "stem":"Hypotension after neuraxial block for cesarean delivery: what is the recommended treatment for moderate to profound hypotension?",
   "answer":"Moderate to profound hypotension should be treated with phenylephrine (preferred to maintain uteroplacental perfusion) and IV fluids; severe cases may require epinephrine 10-50 mcg or vasopressin 0.4-2.0 units IV.",
   "rationale":"Neuraxial sympathectomy reduces SVR; phenylephrine maintains perfusion pressure without increasing HR; epinephrine or vasopressin are reserved for refractory cases due to potential tachycardia or uterine vasospasm.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1400}],"confusable_with":""},
]

print(f"Generated so far: {len(kps)} KPs")
print("OK")
