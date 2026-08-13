import json

with open('C:/Users/Dean/anesthesia_attending/data/_kps_batch1.json', 'r', encoding='utf-8') as f:
    kps = json.load(f)

# ============================================================
# [9] Enhanced recovery after cesarean (ERAC)
# Chunks: mostly about LAST, neuraxial complications, epidural pharmacology, opioid basics
# Limited direct ERAC content - use what is available
# ============================================================
t = "Enhanced recovery after cesarean (ERAC)"
dom = "Obstetric anesthesia (maternal physiology, labor analgesia, cesarean anesthesia, preeclampsia/eclampsia, obstetric hemorrhage, emergencies, fetal considerations)"
disc = "anesthesia"
s = "erac"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the management sequence for venous air embolism (VAE) detected intraoperatively?",
 "answer":"Stop cause (halt insufflation, occlude open veins, flood field with saline) -> Trendelenburg left-side-down position -> CPR/ACLS for circulatory collapse",
 "rationale":"Left-side-down Trendelenburg keeps air in the apex of the right ventricle away from the pulmonary outflow, allowing blood to fill around it; CPR may dislodge the air bolus.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":850}],"confusable_with":""},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the mechanism and treatment of local anesthetic systemic toxicity (LAST)?",
 "answer":"Local anesthetics block sodium channels throughout the body (brain, heart); treatment: lipid emulsion (20% intralipid), benzodiazepines for seizures, CPR if cardiac arrest",
 "rationale":"Lipid emulsion acts as a lipid sink sequestering lipophilic local anesthetic away from cardiac sodium channels, rapidly reversing cardiovascular toxicity.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":850}],"confusable_with":"High spinal (no seizures, sympathectomy predominates)"},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"In neuraxial anesthesia for cesarean, which regional technique provides a more rapid, predictable onset and denser block?",
 "answer":"Spinal anesthesia provides more rapid, predictable onset and denser block than epidural; epidural allows better ongoing control of sensory level",
 "rationale":"The smaller intrathecal dose ensures the drug acts on nerve roots directly in CSF without systemic absorption risk, producing more reliable block quality.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1404}],"confusable_with":"Epidural (slower onset but adjustable level)"},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"What spinal opioid advantage does spinal anesthesia for cesarean delivery offer postoperatively?",
 "answer":"Spinal anesthesia allows use of spinal opioids for postoperative pain relief (e.g., intrathecal morphine for 24-hour analgesia)",
 "rationale":"Intrathecal morphine provides prolonged postoperative analgesia at very low doses (0.1-0.2 mg), reducing systemic opioid requirement after cesarean.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1404}],"confusable_with":"Epidural opioids (separate catheter technique)"},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the most common complication of neuraxial blockade for labor analgesia and what are the prophylactic measures?",
 "answer":"Hypotension (decrease in SBP >20%) is the most common complication, occurring in approximately 14% of cases; prophylactic measures include left uterine displacement and IV hydration",
 "rationale":"Sympathetic blockade reduces SVR; aortocaval compression by the gravid uterus compounds hypotension; left uterine displacement opens the vena cava.",
 "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":615}],"confusable_with":""},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"In comparison to CSE technique, what specific adverse events are more common with CSE but less common with DPE?",
 "answer":"CSE has increased opioid-based pruritus, increased risk of uterine tachysystole, and greater incidence of fetal bradycardia after block placement compared to DPE",
 "rationale":"Intrathecal opioids in CSE cause more systemic mu-receptor activation; rapid onset CSE analgesia may reflexively increase uterine tone causing fetal bradycardia.",
 "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":613}],"confusable_with":"DPE (fewer one-sided blocks, fewer catheter failures)"},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What pre-anesthesia step is essential before any cesarean delivery regardless of regional technique chosen?",
 "answer":"Administration of a nonparticulate antacid within 30 minutes of anticipated surgery; must be prepared to administer general anesthetic at any time during the procedure",
 "rationale":"All parturients are considered to have a full stomach; nonparticulate antacid (sodium citrate) neutralizes gastric pH without risk of aspiration injury if particulate antacid is aspirated.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1404}],"confusable_with":""},
]

# ============================================================
# [10] Epidural anesthesia for cesarean delivery
# ============================================================
t = "Epidural anesthesia for cesarean delivery"
dom = "Obstetric anesthesia (maternal physiology, labor analgesia, cesarean anesthesia, preeclampsia/eclampsia, obstetric hemorrhage, emergencies, fetal considerations)"
disc = "anesthesia"
s = "epidural-cesarean"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What sensory level is required for epidural anesthesia for cesarean delivery, and how is patchy anesthesia treated before delivery?",
 "answer":"T4 sensory level required; patchy anesthesia before delivery treated with IV ketamine 10-20 mg + midazolam 1-2 mg or 30% nitrous oxide",
 "rationale":"T4 level blocks thoracic visceral afferents from the uterus; patchy block is supplemented with IV agents to avoid GA before delivery.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1406}],"confusable_with":""},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"For emergency cesarean, what agents provide rapid onset when dosed through an existing epidural catheter?",
 "answer":"Alkalinized lidocaine or 3% chloroprocaine provides rapid-onset epidural anesthesia; alkalinizing agents increase the un-ionized fraction for faster nerve penetration",
 "rationale":"Adding bicarbonate raises local anesthetic pH, increasing the un-ionized fraction that crosses nerve sheaths, shortening onset from >20 min to <5 min.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1402}],"confusable_with":"Bupivacaine (slower onset, not ideal for emergency)"},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"What are the absolute contraindications to regional anesthesia for cesarean delivery?",
 "answer":"Patient refusal, infection at injection site, coagulopathy, marked hypovolemia, and true allergy to local anesthetics",
 "rationale":"These contraindications reflect situations where regional block is dangerous (bleeding into epidural space with coagulopathy, hemodynamic collapse with sympathectomy in hypovolemia).",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1393}],"confusable_with":"Relative contraindications (sepsis, prior back surgery)"},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"What are the indications for emergency (crash) cesarean section requiring immediate general anesthesia?",
 "answer":"Massive bleeding (placenta previa/accreta, abruption, uterine rupture), umbilical cord prolapse, severe fetal distress requiring immediate delivery",
 "rationale":"When immediate delivery is required for maternal or fetal survival, general anesthesia (RSI) is faster than establishing new neuraxial block.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1412}],"confusable_with":"Urgent cesarean (some delay possible, neuraxial preferred)"},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"After delivery during cesarean, what supplemental analgesia can be added if a functioning epidural is in place?",
 "answer":"After delivery, intravenous opioid supplementation may be used, provided excessive sedation and loss of consciousness are avoided",
 "rationale":"Post-delivery, fetal considerations no longer limit maternal opioid dosing; systemic opioids can supplement regional block without risk to the neonate.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1406}],"confusable_with":""},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the advantage of continuous epidural anesthesia over single-shot spinal for cesarean delivery?",
 "answer":"Continuous epidural allows better ongoing control of sensory level; spinal has faster, more predictable onset and denser block but fixed duration",
 "rationale":"Epidural catheter allows supplemental dosing if block recedes or surgery is prolonged; spinal cannot be redosed once in place without second injection.",
 "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1404}],"confusable_with":""},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the test dose before epidural activation and what does a positive result indicate?",
 "answer":"3 mL test dose of local anesthetic with epinephrine 1:200,000; intravascular placement: tachycardia from epinephrine; subarachnoid placement: rapid dense block",
 "rationale":"Epinephrine causes tachycardia within 30-60 seconds if injected intravascularly; inadvertent subarachnoid injection produces rapid spinal anesthesia.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1397}],"confusable_with":""},
]

kps.append({"_type":"confusable_pair","topic_a":"Emergency (crash) cesarean - general anesthesia","topic_b":"Urgent cesarean - neuraxial preferred",
 "discriminator":"True crash = immediate delivery required for survival (cord prolapse, severe fetal distress, massive hemorrhage): GA with RSI; Urgent = some delay possible: extend existing epidural or place spinal"})

# ============================================================
# [11] Epidural anesthesia: pharmacology and dosing
# Chunks are mostly off-topic (MAC, aging pharmacology). Use what's relevant.
# ============================================================
t = "Epidural anesthesia: pharmacology and dosing"
dom = "Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)"
disc = "anesthesia"
s = "epidural-pharma"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What effect do opioids and benzodiazepines coadministered during epidural anesthesia have on blood pressure?",
 "answer":"Combination of opioids and benzodiazepines markedly reduces arterial blood pressure and peripheral vascular resistance synergistically",
 "rationale":"Both drug classes depress cardiovascular function; their combination produces more hypotension than either alone, particularly relevant during cardiac surgery.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":284}],"confusable_with":""},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"Benzodiazepines reduce the MAC of volatile anesthetics by what percentage?",
 "answer":"Benzodiazepines reduce the minimum alveolar concentration of volatile anesthetics by as much as 30%",
 "rationale":"Benzodiazepines potentiate GABA-A inhibition, providing synergistic sedation that reduces the volatile agent requirement to prevent movement.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":284}],"confusable_with":""},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"In elderly patients, what pharmacodynamic change most affects epidural and neuraxial dosing?",
 "answer":"Reduced anesthetic requirement (reduced MAC for volatile agents; lower dose requirements for propofol, etomidate, opioids, benzodiazepines, and barbiturates)",
 "rationale":"Age-related reduction in neural density, reduced protein binding, and decreased CNS receptor density all contribute to enhanced drug sensitivity.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1490}],"confusable_with":""},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"How does chloroprocaine's pharmacokinetics make it uniquely useful in epidural anesthesia for neonates and infants?",
 "answer":"Rapid plasma clearance of chloroprocaine allows its use as continuous epidural infusion in neonates/young infants without stepwise blood concentration buildup from repeat loading doses",
 "rationale":"Chloroprocaine is an ester hydrolyzed rapidly by plasma cholinesterase; its short half-life prevents toxic accumulation in patients receiving repeat epidural doses.",
 "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":178}],"confusable_with":"Lidocaine (amino-amide, slower clearance)"},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the MAC-awake value for volatile agents and what does it represent?",
 "answer":"MAC-awake is approximately 0.4 MAC for volatile agents; the concentration preventing response to verbal/tactile stimulation in 50% of subjects (prevents recall at lower levels)",
 "rationale":"MAC-awake is substantially below MAC (immobility threshold); awareness monitoring (BIS, SedLine) targets suppression above MAC-awake.",
 "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":114}],"confusable_with":"MAC (immobility endpoint, not awareness endpoint)"},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"Why do intraoperative hyperventilation and volatile/opioid agents cause postoperative apnea?",
 "answer":"Intraoperative hyperventilation commonly causes postoperative apnea; volatile agents and opioids raise the apneic threshold (PaCO2 required to drive breathing), creating apnea when normocarbia returns",
 "rationale":"The apneic threshold is the PaCO2 below which breathing ceases; if hyperventilation lowers PaCO2 below the raised threshold, apnea persists until PaCO2 rises.",
 "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":352}],"confusable_with":""},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"For patients with epidural or spinal anesthesia during transport and recovery, what cardiovascular complication must be anticipated?",
 "answer":"Decreases in blood pressure during transport or recovery; sympatholytic effects of major conduction blocks prevent compensatory reflex vasoconstriction when patients are moved or sit up",
 "rationale":"Neuraxial sympathetic blockade inhibits peripheral vasoconstriction; positional changes reduce venous return without compensatory response, causing orthostatic hypotension.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":2098}],"confusable_with":""},
]

# ============================================================
# [12] Epidural anesthesia: technique
# ============================================================
t = "Epidural anesthesia: technique"
dom = "Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)"
disc = "anesthesia"
s = "epidural-technique"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What technique identifies entry into the epidural space during Tuohy needle placement?",
 "answer":"Sudden loss of resistance (to injection of air or saline) as the needle passes through the ligamentum flavum and enters the epidural space",
 "rationale":"The ligamentum flavum provides resistance to injection; the epidural space lacks resistance, producing the characteristic sudden loss of resistance.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1541}],"confusable_with":"Loss of resistance for subarachnoid (needle continues to freely flowing CSF)"},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"How can ultrasound guidance improve epidural placement success?",
 "answer":"Neuraxial ultrasonography improves block efficacy by identifying skin-to-dura distance and reducing lumbar epidural block failure rate; useful for real-time guidance especially in pediatric patients (less ossification)",
 "rationale":"Ultrasound identifies landmarks non-invasively; real-time guidance is more challenging in adults due to ossification but can visualize catheter tip and drug spread.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":333}],"confusable_with":""},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"What neurological complication risk is higher with epidural anesthesia compared to spinal anesthesia?",
 "answer":"Epidural (including CSE) anesthesia is associated with a more frequent rate of nerve injury compared with spinal anesthesia; neuraxial anesthesia in adults for perioperative use has higher neurological complication risk than in obstetric, pediatric, or chronic pain settings",
 "rationale":"The epidural catheter passes through more tissue, increasing mechanical nerve injury risk; direct spinal cord injury risk from epidural needle is higher than with pencil-point spinal needle.",
 "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":335}],"confusable_with":""},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the natural history of PDPH and when does the epidural blood patch become necessary?",
 "answer":"PDPH typically begins within 3 days (two-thirds within 48 hours); spontaneous resolution in 7 days for most; minority persist at 6 months; epidural blood patch is definitive therapy with 90% initial improvement",
 "rationale":"Conservative measures (supine position, hydration, caffeine) suffice for most; blood patch indicated for severe or persistent headache that limits function.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":336}],"confusable_with":"Migraine headache (position-independent)"},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"Why should neuraxial anesthesia be considered carefully in patients with preexisting spinal stenosis or neurologic disease?",
 "answer":"Spinal stenosis is associated with increased nerve injury risk after neuraxial techniques; preexisting neurologic disease increases susceptibility to injury after neuraxial anesthesia (double-crush phenomenon)",
 "rationale":"Compressed or diseased nerves are more vulnerable to additional ischemic or mechanical injury from needle placement, local anesthetic neurotoxicity, or pressure from catheter.",
 "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":320}],"confusable_with":"Chronic low back pain (not a contraindication without neurologic deficit)"},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"When placing a thoracic epidural, what anatomic feature limits the approach options compared to lumbar epidural?",
 "answer":"Thoracic epidural is technically more difficult; the spinous processes angle steeply downward, so paramedian approach is often preferred; a segmental band of anesthesia at injected levels leaves above and below unblocked",
 "rationale":"Thoracic spinous process angulation narrows the midline window; the paramedian approach bypasses this limitation and can achieve a segmental thoracic block.",
 "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1583}],"confusable_with":"Lumbar epidural (wider interspinous space, midline approach easier)"},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What are the neurological warning signs that must immediately halt any neuraxial procedure?",
 "answer":"Radicular pain or paresthesia occurring during any neuraxial procedure should warn the practitioner to stop and reposition the needle/catheter",
 "rationale":"Paresthesia indicates contact with or injection into a nerve root; continuing risks direct neural trauma or intraneural injection causing permanent damage.",
 "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":335}],"confusable_with":""},
]

# ============================================================
# [13] Epidural labor analgesia: technique and management
# ============================================================
t = "Epidural labor analgesia: technique and management"
dom = "Obstetric anesthesia (maternal physiology, labor analgesia, cesarean anesthesia, preeclampsia/eclampsia, obstetric hemorrhage, emergencies, fetal considerations)"
disc = "anesthesia"
s = "epidural-labor"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What sequence is suggested for epidural activation for first-stage labor analgesia?",
 "answer":"1. Test dose (3 mL LA + epinephrine 1:200,000) for intravascular/subarachnoid placement; 2. Fractionate LA doses with opioids; 3. Confirm adequate analgesia before leaving patient",
 "rationale":"Test dose identifies misplaced catheter before large drug volumes are injected; fractionated dosing minimizes the dose given if catheter is misplaced.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1397}],"confusable_with":""},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What are the major contraindications to neuraxial anesthesia for labor?",
 "answer":"Lack of consent, coagulation abnormalities, severe hypovolemia, elevated intracranial pressure, infection at the site of injection",
 "rationale":"Coagulopathy risks epidural hematoma; severe hypovolemia will worsen with sympathectomy; elevated ICP risks brainstem herniation if CSF is accessed.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1541}],"confusable_with":""},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the risk of double-crush neurologic injury in patients with preexisting peripheral neurologic disease undergoing neuraxial anesthesia?",
 "answer":"Preexisting neurological disease (peripheral neuropathy, spinal stenosis) increases susceptibility to injury after neuraxial anesthesia; the double-crush phenomenon means compromised nerves are more vulnerable to additional insult",
 "rationale":"A nerve already compressed or diseased has reduced reserve for additional ischemia, chemical, or mechanical injury from needle, catheter, or local anesthetic.",
 "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":320}],"confusable_with":""},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"In comparison of labor analgesia techniques, what are the advantages of DPE over CSE?",
 "answer":"DPE has fewer one-sided blocks, fewer catheter failures, and compared with CSE, lower risk of opioid-based pruritus, uterine tachysystole, and fetal bradycardia",
 "rationale":"DPE's intentional dural puncture allows epidural drugs to more reliably reach the intrathecal space while avoiding the high-dose intrathecal opioid bolus of CSE.",
 "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":613}],"confusable_with":""},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"What percentage of maternal deaths are anesthesia-related according to US CDC data?",
 "answer":"Only 0.4% of maternal deaths were anesthesia-related; leading causes are cardiovascular diseases, infection/sepsis, cardiomyopathy, hemorrhage, embolism, stroke",
 "rationale":"Modern obstetric anesthesia practices have dramatically reduced anesthesia-attributable maternal mortality; non-anesthetic causes now dominate.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1383}],"confusable_with":""},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What saddle block technique can be achieved with hyperbaric spinal anesthesia and how is it produced?",
 "answer":"Keep patient sitting for 3-5 minutes after hyperbaric injection so only lower lumbar and sacral nerves are blocked (saddle distribution for perineal anesthesia)",
 "rationale":"Hyperbaric solution is denser than CSF and settles under gravity to the most dependent nerve roots in the sitting patient.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1582}],"confusable_with":"Full spinal (patient moved supine immediately, solution spreads cephalad)"},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What are the potential benefits of epidural analgesia for labor over systemic opioid analgesia regarding respiratory outcomes?",
 "answer":"Epidural analgesia is superior to systemic opioid analgesia for pain control and improves respiratory outcomes in adults undergoing surgery; in obstetrics it avoids neonatal opioid-induced respiratory depression",
 "rationale":"Systemic opioids cross the placenta and cause neonatal respiratory depression; epidural/neuraxial analgesia achieves equivalent or superior pain control without systemic drug transfer.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":314}],"confusable_with":""},
]

print(f"KPs so far: {len(kps)}")

with open('C:/Users/Dean/anesthesia_attending/data/_kps_batch2.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Batch 2 saved OK")
