import json, sys
sys.path.insert(0, 'data')
from build_kp_part6c import kps

disc = "anesthesia"
dom_regional = "Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)"
dom_pharm = "Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)"

# =====================================================================
# [11] Epidural anesthesia: pharmacology and dosing
# =====================================================================
topic11 = "Epidural anesthesia: pharmacology and dosing"

kps += [
  {"id":"epidural-anesthesia-pharmacology-dosing-d1","topic":topic11,"domain":dom_regional,"discipline":disc,
   "stem":"The principal pharmacodynamic change of aging relevant to anesthetic dosing is a reduced anesthetic requirement. How does this affect epidural anesthesia dosing?",
   "answer":"Older adult patients display a lower dose requirement for anesthetics including propofol, etomidate, opioids, benzodiazepines, and barbiturates; epidural local anesthetic requirements also decrease with age.",
   "rationale":"Aging reduces neuronal density, narrows intervertebral foramina (reducing drug escape), and decreases epidural fat, increasing the spread of a given epidural volume.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1490}],"confusable_with":""},

  {"id":"epidural-anesthesia-pharmacology-dosing-d2","topic":topic11,"domain":dom_regional,"discipline":disc,
   "stem":"Chloroprocaine has two unique roles in pediatric epidural anesthesia due to its rapid plasma clearance. What are they?",
   "answer":"(1) Continuous epidural infusion in neonates and very young infants and (2) repeat loading doses in patients where repeated doses of amino-amide local anesthetics would risk toxicity due to accumulation.",
   "rationale":"Chloroprocaine is an ester hydrolyzed rapidly by plasma cholinesterases; its rapid metabolism prevents systemic accumulation even with continuous infusions or frequent redosing.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":178}],"confusable_with":"bupivacaine in neonates"},

  {"id":"epidural-anesthesia-pharmacology-dosing-d3","topic":topic11,"domain":dom_regional,"discipline":disc,
   "stem":"When patients receive spinal or epidural anesthesia, what cardiovascular complication may occur during transport or recovery, and why?",
   "answer":"Patients may experience decreases in blood pressure during transport or recovery because the sympatholytic effects of major conduction blocks prevent compensatory reflex vasoconstriction.",
   "rationale":"The sympathetic blockade from neuraxial anesthesia persists after the block is placed; during transport when less external support (IV fluid, monitoring) is immediately available, hypotension may manifest.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":2098}],"confusable_with":""},

  {"id":"epidural-anesthesia-pharmacology-dosing-d4","topic":topic11,"domain":dom_regional,"discipline":disc,
   "stem":"When using isolated forearm technique and intense paralysis is needed, what minimum alveolar concentration of inhalation agent is recommended to prevent awareness?",
   "answer":"Administer at least 0.5-0.7 MAC of the inhalation agent; choose potent inhalation agents rather than TIVA if possible, and set an alarm for low anesthetic gas concentration.",
   "rationale":"At 0.5-0.7 MAC inhalation agents suppress explicit memory; TIVA without depth monitoring carries higher awareness risk; alarms ensure detection of inadvertent agent discontinuation.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":204}],"confusable_with":""},

  {"id":"epidural-anesthesia-pharmacology-dosing-d5","topic":topic11,"domain":dom_regional,"discipline":disc,
   "stem":"Benzodiazepines reduce the minimum alveolar concentration of volatile anesthetics by what percentage?",
   "answer":"Benzodiazepines reduce the MAC of volatile anesthetics by as much as 30%.",
   "rationale":"Benzodiazepines enhance GABAergic inhibition independently of volatile agents; their synergistic CNS depression means lower volatile concentrations are needed for equivalent anesthetic depth.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":284}],"confusable_with":""},

  {"id":"epidural-anesthesia-pharmacology-dosing-d6","topic":topic11,"domain":dom_regional,"discipline":disc,
   "stem":"Hyperbaric spinal anesthesia positioning allows anatomic and gravitational control of block distribution. How is a 'saddle block' achieved?",
   "answer":"A saddle block is achieved by keeping the patient sitting for 3-5 minutes following injection of hyperbaric solution, so that only the lower lumbar nerves and sacral roots are blocked.",
   "rationale":"Hyperbaric local anesthetic is denser than CSF and flows by gravity to the dependent perineal area when the patient remains sitting; redistributing upward requires supine position.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1582}],"confusable_with":"isobaric spinal"},

  {"id":"epidural-anesthesia-pharmacology-dosing-d7","topic":topic11,"domain":dom_regional,"discipline":disc,
   "stem":"Major contraindications to neuraxial anesthesia include what five categories?",
   "answer":"Lack of consent, coagulation abnormalities, severe hypovolemia, elevated intracranial pressure, and infection at the site of injection.",
   "rationale":"Each contraindication reflects a specific risk: consent (autonomy), coagulopathy (spinal hematoma), hypovolemia (hemodynamic collapse), elevated ICP (herniation), infection (meningitis/abscess).",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1541}],"confusable_with":""},
]

# =====================================================================
# [12] Epidural anesthesia: technique
# =====================================================================
topic12 = "Epidural anesthesia: technique"

kps += [
  {"id":"epidural-anesthesia-technique-d1","topic":topic12,"domain":dom_regional,"discipline":disc,
   "stem":"For epidural placement, the classic technique uses loss of resistance. To what structure does the needle pass through to reach the epidural space?",
   "answer":"The needle passes through the ligamentum flavum, and a sudden loss of resistance (to injection of air or saline) is encountered as it enters the epidural space.",
   "rationale":"The ligamentum flavum is a dense, elastic structure that resists injection; once breached, the negative-pressure epidural space allows free injection, providing tactile confirmation.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1541}],"confusable_with":""},

  {"id":"epidural-anesthesia-technique-d2","topic":topic12,"domain":dom_regional,"discipline":disc,
   "stem":"Real-time ultrasound guidance for epidural placement is described as particularly valuable in which patient population?",
   "answer":"Real-time ultrasound guidance is relatively easier in the pediatric population because of limited ossification of the vertebral processes allowing better visualization.",
   "rationale":"In adults, ossified vertebrae impede ultrasound penetration; in children, acoustic windows through incompletely ossified bone allow real-time visualization of the epidural space.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":333}],"confusable_with":""},

  {"id":"epidural-anesthesia-technique-d3","topic":topic12,"domain":dom_regional,"discipline":disc,
   "stem":"Neuraxial anesthesia performed in adults for perioperative anesthesia or analgesia is associated with an increased likelihood of what complication, and when does it typically begin?",
   "answer":"Neurological injury is increased with neuraxial anesthesia; symptoms typically begin within 3 days, with approximately two-thirds starting within the first 48 hours.",
   "rationale":"Epidural hematoma or abscess causes neural compression; early recognition within the critical 6-8 hour window for decompression determines functional outcome.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":335}],"confusable_with":""},

  {"id":"epidural-anesthesia-technique-d4","topic":topic12,"domain":dom_regional,"discipline":disc,
   "stem":"For a CSE technique, using a 25-gauge spinal needle does not increase headache risk compared with epidural alone, but is associated with what other consideration?",
   "answer":"Use of a 25-gauge spinal needle for CSE does not increase headache risk, but CSE technique compared with DPE or epidural is associated with increased opioid-based pruritus, increased uterine tachysystole, and greater incidence of fetal bradycardia.",
   "rationale":"Direct intrathecal opioid delivery in CSE produces greater pruritus than epidural-only routes; the intrathecal component may also cause rapid sympatholysis contributing to uterine and fetal effects.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":613}],"confusable_with":"DPE"},

  {"id":"epidural-anesthesia-technique-d5","topic":topic12,"domain":dom_regional,"discipline":disc,
   "stem":"Pre-existing neurological disease in the context of neuraxial anesthesia risk: what is the double-crush phenomenon?",
   "answer":"The double-crush phenomenon refers to increased susceptibility to nerve injury after neuraxial anesthesia in patients with preexisting central or peripheral neurologic diseases; two sub-threshold injuries may combine to cause clinical deficit.",
   "rationale":"A nerve already compromised by disease has reduced physiological reserve; a second insult from local anesthetic neurotoxicity or mechanical trauma can produce injury that neither alone would cause.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":320}],"confusable_with":""},

  {"id":"epidural-anesthesia-technique-d6","topic":topic12,"domain":dom_regional,"discipline":disc,
   "stem":"Hyperbaric bupivacaine for spinal anesthesia in cesarean delivery is typically injected, then the patient is positioned in lithotomy with left uterine displacement. How long after injection does this positioning occur?",
   "answer":"Three minutes after intrathecal injection of the hyperbaric solution, the patient is placed in lithotomy position with left uterine displacement.",
   "rationale":"A 3-minute sitting or semi-recumbent interval allows the hyperbaric solution to settle and the block to fix; early positioning prevents excessive cephalad spread.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1402}],"confusable_with":""},

  {"id":"epidural-anesthesia-technique-d7","topic":topic12,"domain":dom_regional,"discipline":disc,
   "stem":"Pre-procedure neuraxial ultrasonography by experienced practitioners offers what technical benefit?",
   "answer":"Neuraxial ultrasonography can identify skin-to-dura distance and reduce lumbar epidural block failure rate; it may also improve block efficacy.",
   "rationale":"Ultrasound pre-scanning identifies the interspinous gap, estimates depth to epidural space, and detects anatomical variants (scoliosis, calcified ligaments), improving first-pass success.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":333}],"confusable_with":""},
]

# =====================================================================
# [13] Epidural labor analgesia: technique and management
# =====================================================================
topic13 = "Epidural labor analgesia: technique and management"

kps += [
  {"id":"epidural-labor-analgesia-technique-d1","topic":topic13,"domain":dom_regional,"discipline":disc,
   "stem":"For epidural activation during the first stage of labor, initial injections may be given before or after catheter placement. What is the advantage of each timing?",
   "answer":"Administration through the needle can facilitate catheter placement (analgesia relaxes patient); administration through the catheter provides assurance that the catheter is functioning properly.",
   "rationale":"Testing catheter function before relying on it for high-stakes anesthesia (emergency cesarean) is critical; however, early needle injection can reduce patient movement during catheter advancement.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1397}],"confusable_with":""},

  {"id":"epidural-labor-analgesia-technique-d2","topic":topic13,"domain":dom_regional,"discipline":disc,
   "stem":"All opioids readily cross the placental barrier and can cause neonatal respiratory depression. Which opioid is preferred for labor analgesia and why?",
   "answer":"Fentanyl is preferred because it has a short duration of action and no active metabolites, making it less likely to cause significant neonatal depression compared with other opioids.",
   "rationale":"Fentanyl's context-sensitive half-life for typical labor doses is short; absence of active metabolites reduces cumulative neonatal exposure even with repeated maternal doses.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":609}],"confusable_with":"meperidine"},

  {"id":"epidural-labor-analgesia-technique-d3","topic":topic13,"domain":dom_regional,"discipline":disc,
   "stem":"A parturient in early labor with severe pain is requesting analgesia. Which technique provides the most rapid onset of pain relief?",
   "answer":"CSE analgesia -- intrathecal opioid and local anesthetic provide essentially immediate pain control; CSE especially benefits patients with severe pain early in labor.",
   "rationale":"Intrathecal drugs bypass the epidural membrane and act directly on spinal cord receptors; onset is within minutes, compared with 15-20 minutes for epidural-only techniques.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1400}],"confusable_with":"standard epidural"},

  {"id":"epidural-labor-analgesia-technique-d4","topic":topic13,"domain":dom_regional,"discipline":disc,
   "stem":"What is the FDA warning regarding neuraxial clonidine in obstetrics?",
   "answer":"The FDA has issued a black box warning regarding increased risk of hypotension and bradycardia with neuraxial clonidine in obstetrics.",
   "rationale":"Neuraxial clonidine causes central alpha-2-mediated sympatholysis; in pregnant patients who are hemodynamically sensitive, this can cause severe maternal hypotension with fetal compromise.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":610}],"confusable_with":""},

  {"id":"epidural-labor-analgesia-technique-d5","topic":topic13,"domain":dom_regional,"discipline":disc,
   "stem":"Chronic low back pain without neurological deficit: is it a contraindication to neuraxial anesthesia?",
   "answer":"Chronic low back pain without neurological deficit is NOT a contraindication to neuraxial anesthesia.",
   "rationale":"Low back pain alone without neural compromise does not increase the risk of neuraxial complications; the double-crush phenomenon applies to patients with neurological deficits or established nerve compromise.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":320}],"confusable_with":""},

  {"id":"epidural-labor-analgesia-technique-d6","topic":topic13,"domain":dom_regional,"discipline":disc,
   "stem":"An accidental intravascular injection of bupivacaine during labor epidural placement can cause severe local anesthetic systemic toxicity (LAST). What feature of bupivacaine makes its cardiac toxicity particularly dangerous?",
   "answer":"Bupivacaine binds cardiac sodium channels with high affinity and slow offset ('fast-in, slow-out' kinetics), making resuscitation from bupivacaine-induced cardiac arrest extremely difficult.",
   "rationale":"Bupivacaine's prolonged sodium channel binding prevents spontaneous cardiac recovery and reduces responsiveness to standard resuscitation drugs; this distinguishes it from less toxic LAs like lidocaine.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":610}],"confusable_with":"ropivacaine"},

  {"id":"epidural-labor-analgesia-technique-d7","topic":topic13,"domain":dom_regional,"discipline":disc,
   "stem":"The leading causes of pregnancy-related death in the US include several categories. What is the most common overall cause?",
   "answer":"Cardiovascular diseases (14%) are the leading cause of pregnancy-related death in the US, followed by infection/sepsis (13%) and cardiomyopathy (12%).",
   "rationale":"Anesthesiologists must be aware that hemorrhage, embolism, and hypertensive disorders -- traditional obstetric foci -- are now outranked by cardiovascular disease; preoperative cardiac evaluation is increasingly important.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1383}],"confusable_with":""},
]

print(f"Generated so far: {len(kps)} KPs")
print("OK")
