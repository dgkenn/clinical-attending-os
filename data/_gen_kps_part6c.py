import json

with open('C:/Users/Dean/anesthesia_attending/data/_kps_batch2.json', 'r', encoding='utf-8') as f:
    kps = json.load(f)

# ============================================================
# [14] Epidural pharmacology
# Chunks mostly off-topic - use available pharmacology chunks
# ============================================================
t = "Epidural pharmacology"
dom = "Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)"
disc = "anesthesia"
s = "epidural-pharm2"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the role of epidural morphine in labor analgesia and why is it rarely used alone?",
 "answer":"Epidural morphine 0.1-0.25 mg provides 4-6 hours analgesia for first-stage labor but onset is slow (45-60 min) and higher doses cause significant side effects; usually combined with fentanyl for faster onset",
 "rationale":"Morphine is highly hydrophilic; slow epidural onset requires combination with lipophilic opioids like fentanyl for rapid initial analgesia.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1392}],"confusable_with":"Fentanyl alone (fast onset but short duration)"},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What epidural opioid combination is used to achieve rapid onset (5 min) of labor analgesia?",
 "answer":"Morphine 0.1-0.25 mg combined with fentanyl 12.5 mcg (or sufentanil 5 mcg) provides rapid-onset analgesia within 5 minutes",
 "rationale":"Lipophilic fentanyl/sufentanil penetrates the dura rapidly for quick onset; hydrophilic morphine provides sustained duration covering the first stage.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1392}],"confusable_with":""},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"In preventing intraoperative awareness, what minimum MAC of inhalation agent should be administered during TIVA when a potent inhalational agent is not available?",
 "answer":"Administer at least 0.5-0.7 MAC of the inhalation agent; if hemodynamic compromise limits this, consider benzodiazepines or scopolamine for amnesia",
 "rationale":"0.5 MAC provides reasonable but not guaranteed amnesia; below this level recall risk increases substantially, especially with neuromuscular blockade masking movement.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":204}],"confusable_with":""},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"Why does cimetidine (an H2 blocker) affect the hepatic metabolism of co-administered drugs?",
 "answer":"Cimetidine reduces liver blood flow, thereby limiting hepatic drug metabolism for drugs with high hepatic extraction ratios",
 "rationale":"Cimetidine inhibits cytochrome P450 and reduces hepatic blood flow; drugs cleared primarily by hepatic blood flow (high extraction) will have prolonged effects.",
 "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":352}],"confusable_with":""},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"What bupivacaine and ropivacaine property makes them the most commonly used local anesthetics for labor epidural analgesia?",
 "answer":"Bupivacaine and ropivacaine are the most commonly used local anesthetics for labor analgesia; both are extremely safe when appropriately dosed for epidural or intrathecal administration",
 "rationale":"These long-acting amides provide sustained labor analgesia; ropivacaine has less cardiac toxicity than bupivacaine with similar clinical potency.",
 "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":610}],"confusable_with":"Lidocaine (shorter duration, not suitable for sustained labor analgesia)"},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What warning has the FDA issued regarding epidural clonidine use in obstetrics?",
 "answer":"FDA 'black box' warning: increased risk of hypotension and bradycardia with neuraxial clonidine in obstetrics; use with caution",
 "rationale":"Clonidine as an alpha-2 agonist potentiates epidural local anesthetic and opioid effects but causes hemodynamic instability that may compromise uteroplacental blood flow.",
 "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":610}],"confusable_with":"Dexmedetomidine (not used neuraxially in obstetrics)"},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the clinical significance of the enterohepatic circulation of diazepam?",
 "answer":"Enterohepatic circulation produces a secondary peak in diazepam plasma concentration 6-12 hours following administration",
 "rationale":"Diazepam excreted in bile is reabsorbed from the intestine, creating a second plasma concentration peak that can cause re-sedation hours after apparent recovery.",
 "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":283}],"confusable_with":"Midazolam (no enterohepatic recirculation, no secondary peak)"},
]

# ============================================================
# [15] Epilepsy Surgery Anesthesia
# ============================================================
t = "Epilepsy Surgery Anesthesia"
dom = "Neuroanesthesia (intracranial pressure & cerebral physiology, craniotomy, awake craniotomy, spine surgery, neuromonitoring, TBI, aneurysm)"
disc = "anesthesia"
s = "epilepsy-surgery"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What anesthetic technique is the norm for epilepsy surgery and why?",
 "answer":"Awake craniotomy is the norm for epilepsy surgery (and DBS); allows real-time cortical mapping for language, motor, and sensory function to guide safe resection",
 "rationale":"Intraoperative patient cooperation during electrocortical stimulation identifies eloquent cortex adjacent to the epileptogenic zone, minimizing neurologic deficits.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1006}],"confusable_with":"General anesthesia with neuromonitoring"},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What agent is used for ECT and epilepsy surgery EEG activation, and what is its EEG effect?",
 "answer":"Etomidate can facilitate longer motor seizure activity in ECT and may activate seizure foci (excitatory EEG spikes) - useful for epileptogenic focus mapping",
 "rationale":"Etomidate's excitatory EEG property paradoxically makes it useful when seizure activity needs to be provoked or prolonged for therapeutic or diagnostic purposes.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":144}],"confusable_with":"Propofol (anticonvulsant, would suppress seizure focus)"},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"Stereotactic surgery for epilepsy may involve what procedures, and what anesthetic approach is used?",
 "answer":"Stereotaxis is used to treat epilepsy; techniques include lesioning (thalamotomy), deep brain stimulation, and stereotactic radiosurgery; awake or general anesthesia depending on the specific procedure",
 "rationale":"Stereotactic targeting requires precise frame placement; DBS targeting often uses microelectrode recording during awake surgery.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":977}],"confusable_with":""},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"In patients with intracranial mass lesions presenting with seizures, what is the initial non-anesthetic treatment and anesthetic consideration?",
 "answer":"Initial treatment: dexamethasone to decrease cerebral edema; continue anticonvulsants until time of surgery; sedative/opioid premedication avoided if ICP elevated",
 "rationale":"Dexamethasone reduces vasogenic edema around tumors; anticonvulsants must be continued perioperatively; sedation may cause hypercapnia raising ICP.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1001}],"confusable_with":""},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"What EEG-based depth of anesthesia consideration is relevant when using BIS monitoring during TIVA?",
 "answer":"BIS index ideally 40-60 for general anesthesia; SedLine PSI ideally 25-50; both use processed EEG; set alarm for low anesthetic gas concentration when using TIVA",
 "rationale":"Processed EEG monitoring detects inadequate anesthetic depth before awareness occurs; alarms on gas concentration analyzers provide backup if TIVA delivery fails.",
 "bloom":"apply","source":[{"book":"Stanford CA-1","page":24}],"confusable_with":""},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What special anesthetic modification is needed in patients with cervical spine instability presenting for cranial/neurological procedures?",
 "answer":"Awake fiberoptic intubation or video laryngoscopy to avoid neck extension/flexion that could cause cord injury; direct arterial pressure monitoring is helpful as hypotension compounds cord ischemia",
 "rationale":"Unstable cervical spine is vulnerable to cord compression with neck manipulation during laryngoscopy; controlled awake technique avoids extension.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1013}],"confusable_with":""},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the significance of increasingly managing patients with regional anesthesia and propofol sedation (MAC) for surgical procedures?",
 "answer":"Patients under regional + propofol MAC may recall perioperative events; they should be informed that recall of events is possible and does not constitute awareness under general anesthesia",
 "rationale":"MAC/conscious sedation maintains patient responsiveness; recall of events is expected and does not represent a general anesthesia awareness event; clarification prevents psychological harm.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":207}],"confusable_with":"Awareness under GA (different medicolegal and psychological implications)"},
]

# ============================================================
# [16] Ethical Principles in Clinical Decision-Making
# ============================================================
t = "Ethical Principles in Clinical Decision-Making"
dom = "Patient safety, ethics, professionalism & quality (closed-claims lessons, never events, root-cause analysis, informed consent, communication, handoffs, wellness)"
disc = "anesthesia"
s = "clinical-ethics"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"In crew resource management (CRM), how should a less experienced clinician respond when they disagree with a management plan?",
 "answer":"Voice concerns about management and do not proceed until a safe anesthetic and surgical plan have been agreed upon",
 "rationale":"Psychological safety and hierarchical barriers are CRM failure points; every team member has a duty to speak up and a culture must exist where this is expected.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":57}],"confusable_with":""},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What does HIPAA-compliant care require regarding sensitive discussions in the PACU setting?",
 "answer":"PACU design should include individually enclosed patient bays for infection control and privacy; sensitive discussions between patient, family, and care team involve confidential issues",
 "rationale":"HIPAA requires protection of PHI; open-ward PACU designs risk inadvertent disclosure of sensitive diagnoses, medications, or prognoses to neighboring patients.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":2096}],"confusable_with":""},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"What patient rights principles apply to HIV testing in a healthcare setting under Florida law as an example of medical ethics?",
 "answer":"Patient must be notified of planned HIV test and has the right to refuse (documented in chart); informed consent must include confidentiality, mandatory reporting, and opportunity for anonymous testing",
 "rationale":"Patient autonomy requires informed consent for testing; confidentiality duties protect against stigma; mandatory reporting serves public health interests.",
 "bloom":"apply","source":[{"book":"StatPearls: StatPearls   HIV  Antiretroviral Therapy (ART)","page":6}],"confusable_with":""},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"What are the three pillars of the good medical record keeping and clinical practice principles in remote patient consultations?",
 "answer":"Treat patients with dignity; respect privacy and confidentiality; listen to patient needs and act in their best interest",
 "rationale":"These principles apply equally to in-person and remote consultations; remote care requires additional vigilance for privacy breaches via technology.",
 "bloom":"recall","source":[{"book":"Society Guideline: Guideline   GOLD 2024 COPD Full Report","page":147}],"confusable_with":""},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the ethical tension when a patient in septic shock has significantly impaired quality of life from underlying chronic illness?",
 "answer":"Goals of care discussion must balance beneficence (treating sepsis) with autonomy (patient's values about QoL and acceptable interventions); palliative care may be appropriate when sepsis is end-stage manifestation",
 "rationale":"Aggressive treatment prolongs life but may extend suffering; patient values about QoL, functional status, and acceptable interventions must guide decisions.",
 "bloom":"analyze","source":[{"book":"Society Guideline","page":49}],"confusable_with":""},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the ethical basis for advance care planning in patients with severe chronic illness who develop acute illness?",
 "answer":"Advance care planning establishes patient-directed goals of care in advance of incapacity; legally and ethically binding; guides treatment decisions when patient cannot make decisions",
 "rationale":"Advance directives respect autonomy prospectively; when patients lose decision-making capacity, prior expressed wishes guide the healthcare team.",
 "bloom":"apply","source":[{"book":"Society Guideline","page":49}],"confusable_with":""},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is 'decision making' in the context of crew resource management, and what does it involve?",
 "answer":"Decision making: ability to use logic and sound judgment based on available information; less experienced clinicians should seek advice from experienced colleagues when appropriate",
 "rationale":"Structured decision-making processes that include consultation reduce errors; CRM teaches recognition of cognitive limitations and appropriate help-seeking.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":57}],"confusable_with":""},
]

# ============================================================
# [17] Etomidate: pharmacology
# Chunks mostly off-topic (benzodiazepines, aging, TIVA) but have etomidate-specific content
# ============================================================
t = "Etomidate: pharmacology"
dom = "Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)"
disc = "anesthesia"
s = "etomidate-pharm"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What are etomidate's effects on the CNS and why is it favored in hemodynamically unstable patients?",
 "answer":"Etomidate reduces CMRO2 and is a potent direct cerebral vasoconstrictor reducing CBF and ICP; it has minimal cardiovascular depressant effects preserving hemodynamic stability",
 "rationale":"Etomidate's cardiovascular stability makes it the induction agent of choice when hypotension would be dangerous (hypovolemia, cardiac dysfunction, aortic stenosis).",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":144}],"confusable_with":"Propofol (causes significant hypotension)"},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What endocrine side effect of etomidate is particularly concerning in septic patients?",
 "answer":"Etomidate inhibits adrenocortical synthesis (11-beta-hydroxylase), causing cortisol suppression; use in septic patients is controversial - risk-benefit must be assessed, with alternatives (ketamine) considered",
 "rationale":"Septic patients have baseline HPA axis dysfunction; additional etomidate-induced cortisol suppression may worsen stress response and potentially increase mortality.",
 "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":145}],"confusable_with":"Etomidate in non-septic patients (less clinically significant)"},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"How does etomidate's EEG profile differ from thiopental, and when is this exploited clinically?",
 "answer":"Etomidate causes excitatory EEG spikes more frequently than thiopental and may activate seizure foci; this is exploited in ECT to facilitate longer motor seizure duration",
 "rationale":"Etomidate's pro-excitatory EEG property contrasts with thiopental's burst suppression; in ECT, longer seizures correlate with better therapeutic outcomes.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":144}],"confusable_with":"Propofol (anticonvulsant, suppresses seizures)"},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"In elderly patients, how does etomidate's pharmacokinetics change and what dose adjustment is required?",
 "answer":"Initial volume of distribution for etomidate significantly decreases with aging; lower doses required to achieve the same EEG endpoint compared with young patients",
 "rationale":"Reduced Vd in elderly means less drug needed to achieve a given plasma concentration; pharmacodynamic sensitivity also increases with age.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1507}],"confusable_with":""},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the etomidate induction dose for cardiac surgery and why does it have advantages in patients with cardiovascular risk?",
 "answer":"Etomidate cardiac induction provides stable hemodynamics with minimal cardiac depression and preserved CPP; described as having a 'characteristic' of decreased CMRO2 and cerebral vasoconstriction",
 "rationale":"Etomidate is the only IV induction agent that does not significantly lower blood pressure, making it valuable in cardiac, vascular, or any surgery where hemodynamic stability is paramount.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":145}],"confusable_with":"Ketamine (cardiovascular stimulation rather than stability)"},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"Why might patients with kidney disease show increased sensitivity to barbiturates despite normal pharmacokinetics?",
 "answer":"Patients with kidney disease often exhibit increased sensitivity to barbiturates even with normal pharmacokinetic profiles; possible mechanisms include decreased protein binding, greater brain penetration from BBB disruption, or synergy with retained toxins",
 "rationale":"Uremic toxins may augment CNS sensitivity to sedatives; reduced albumin binding in hypoalbuminemia increases free drug fraction.",
 "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1102}],"confusable_with":""},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the preferred IV induction agent in patients with active elevated ICP who also have hemodynamic instability?",
 "answer":"Etomidate is preferred for elevated ICP plus hemodynamic instability because it reduces CMRO2, CBF, and ICP while maintaining cardiovascular stability; ketamine avoided (raises ICP)",
 "rationale":"Propofol would lower blood pressure worsening CPP; ketamine raises ICP; etomidate is the agent that reduces ICP without cardiovascular depression.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":144}],"confusable_with":"Propofol (reduces ICP but also blood pressure)"},
]

kps.append({"_type":"confusable_pair","topic_a":"Etomidate","topic_b":"Propofol",
 "discriminator":"Both reduce CMRO2/CBF/ICP; propofol causes significant hypotension (useful antiemetic, anticonvulsant); etomidate preserves hemodynamics but causes adrenocortical suppression and myoclonus"})

print(f"KPs so far: {len(kps)}")

with open('C:/Users/Dean/anesthesia_attending/data/_kps_batch3.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Batch 3 saved OK")
