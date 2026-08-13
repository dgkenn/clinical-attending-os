import json, sys
sys.path.insert(0, 'data')
from build_kp_part6d import kps

disc = "anesthesia"
dom_regional = "Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)"
dom_pharm = "Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)"
dom_neuro = "Neuroanesthesia (intracranial pressure & cerebral physiology, craniotomy, awake craniotomy, spine surgery, neuromonitoring, TBI, aneurysm)"
dom_ethics = "Patient safety, ethics, professionalism & quality (closed-claims lessons, never events, root-cause analysis, informed consent, communication, handoffs, wellness)"
dom_basic = "Anesthesia: basic & clinical sciences (relevant anatomy, respiratory/cardiac/renal/neuro physiology, pharmacokinetics/dynamics principles, physics of gases & flow, statistics)"

# =====================================================================
# [14] Epidural pharmacology
# =====================================================================
topic14 = "Epidural pharmacology"

kps += [
  {"id":"epidural-pharmacology-d1","topic":topic14,"domain":dom_regional,"discipline":disc,
   "stem":"In a patient receiving epidural anesthesia, residual NMB at emergence from anesthesia is common. What is the standard of care for detection and reversal?",
   "answer":"Monitoring neuromuscular blockade with train-of-four and pharmacological reversal are standard of care for patients who received NMBAs.",
   "rationale":"Residual NMB impairs airway reflexes and ventilation; objective TOF monitoring detects incomplete recovery that clinical signs (head lift, hand grip) alone miss.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":344}],"confusable_with":""},

  {"id":"epidural-pharmacology-d2","topic":topic14,"domain":dom_regional,"discipline":disc,
   "stem":"In epidural opioid pharmacology, morphine provides long-lasting analgesia (4-6 hours) during the first stage of labor. What is the main limitation of epidural morphine used alone?",
   "answer":"The onset of analgesia is slow (45-60 minutes), doses sufficient for reliable analgesia have a high incidence of side effects, and onset may be insufficient for active labor pain.",
   "rationale":"Morphine's hydrophilicity limits its rate of penetration through dural and neural membranes; combining with fentanyl provides faster onset via the more lipophilic component.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1392}],"confusable_with":""},

  {"id":"epidural-pharmacology-d3","topic":topic14,"domain":dom_regional,"discipline":disc,
   "stem":"The combination of epidural morphine 0.1-0.25 mg with fentanyl 12.5 mcg or sufentanil 5 mcg achieves what clinical benefit over each drug alone?",
   "answer":"The combination results in more rapid onset of analgesia (within 5 minutes) by leveraging the fast-onset lipophilic opioid while prolonging duration with the hydrophilic morphine.",
   "rationale":"Fentanyl/sufentanil penetrate neural tissue rapidly for quick onset; morphine provides sustained spinal receptor occupancy for duration; the combination is synergistic.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1392}],"confusable_with":""},

  {"id":"epidural-pharmacology-d4","topic":topic14,"domain":dom_regional,"discipline":disc,
   "stem":"Combination of opioids and benzodiazepines can produce a dangerous synergistic interaction on the cardiovascular system. What is it?",
   "answer":"Co-administration of opioids and benzodiazepines markedly reduces arterial blood pressure and peripheral vascular resistance; this synergistic interaction is commonly observed in cardiac surgery patients.",
   "rationale":"Both drug classes independently reduce sympathetic tone and myocardial contractility; their combination produces disproportionate vasodilation and cardiac depression -- potentially catastrophic in patients with limited cardiac reserve.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":284}],"confusable_with":""},

  {"id":"epidural-pharmacology-d5","topic":topic14,"domain":dom_regional,"discipline":disc,
   "stem":"Benzodiazepines have minimal left-ventricular depressant effects EXCEPT in what circumstance?",
   "answer":"Benzodiazepines cause myocardial depression and arterial hypotension when co-administered with opioids (synergistic interaction).",
   "rationale":"Benzodiazepine-only cardiovascular depression is modest due to compensatory sympathetic activation; co-induction with opioids removes this sympathetic compensation, unmasking combined hypotension.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":283}],"confusable_with":""},

  {"id":"epidural-pharmacology-d6","topic":topic14,"domain":dom_regional,"discipline":disc,
   "stem":"Diazepam has an unusual pharmacokinetic feature that can cause a secondary plasma peak. What is it?",
   "answer":"Enterohepatic circulation produces a secondary peak in diazepam plasma concentration 6 to 12 hours following administration.",
   "rationale":"Diazepam and its active metabolites are excreted in bile, undergo intestinal hydrolysis, and are reabsorbed, causing a second rise in plasma levels that can produce renewed sedation.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":283}],"confusable_with":""},

  {"id":"epidural-pharmacology-d7","topic":topic14,"domain":dom_regional,"discipline":disc,
   "stem":"Long-acting sedatives such as benzodiazepines given preoperatively can cause what specific postoperative complication?",
   "answer":"Long-acting benzodiazepines can delay awakening from anesthesia and interfere with postoperative recovery.",
   "rationale":"Benzodiazepines redistribute but do not eliminate rapidly; residual drug causes prolonged sedation, respiratory depression, and delayed discharge -- flumazenil can reverse but has a shorter duration than most benzodiazepines.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":352}],"confusable_with":""},
]

# =====================================================================
# [15] Epilepsy Surgery Anesthesia
# =====================================================================
topic15 = "Epilepsy Surgery Anesthesia"

kps += [
  {"id":"epilepsy-surgery-anesthesia-d1","topic":topic15,"domain":dom_neuro,"discipline":disc,
   "stem":"Awake craniotomy has become the norm for epilepsy surgery. What two conditions make it ideal for this indication?",
   "answer":"Awake craniotomy allows intraoperative EEG recording to identify seizure foci and enables real-time neurological testing to preserve eloquent cortex during resection.",
   "rationale":"Conscious patients can perform language, motor, or cognitive tasks; the neurosurgeon maps functional areas and resects only epileptogenic tissue outside these areas.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1006}],"confusable_with":""},

  {"id":"epilepsy-surgery-anesthesia-d2","topic":topic15,"domain":dom_neuro,"discipline":disc,
   "stem":"Dexmedetomidine does not suppress spikes from seizure foci on EEG. What are the evoked potential monitoring implications of dexmedetomidine at usual infusion doses?",
   "answer":"Evoked potentials monitored during spine surgery are not suppressed at usual infusion doses (<0.6 mcg/kg/h), making dexmedetomidine compatible with intraoperative neurophysiological monitoring.",
   "rationale":"Dexmedetomidine's alpha-2 mechanism does not depress cortical generation of evoked potentials at clinical doses, unlike volatile agents which degrade SSEP and MEP signals.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":146}],"confusable_with":"propofol for monitoring"},

  {"id":"epilepsy-surgery-anesthesia-d3","topic":topic15,"domain":dom_neuro,"discipline":disc,
   "stem":"Stereotaxis in epilepsy surgery allows targeting deep brain structures. What other movement disorder and pain conditions can stereotaxis treat?",
   "answer":"Stereotaxis can be employed in treating involuntary movement disorders (e.g., Parkinson's disease via deep brain stimulation), intractable pain, and epilepsy.",
   "rationale":"Stereotactic frames provide 3D coordinate systems for millimeter-precision targeting; this accuracy enables DBS electrode placement or lesioning in deep structures like the thalamus or globus pallidus.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":977}],"confusable_with":""},

  {"id":"epilepsy-surgery-anesthesia-d4","topic":topic15,"domain":dom_neuro,"discipline":disc,
   "stem":"Patients who have experienced intraoperative awareness events should receive what follow-up care?",
   "answer":"Close follow-up and involvement of mental health experts to avoid the traumatic stress associated with intraoperative awareness; patients should be managed with empathy and offered psychological support.",
   "rationale":"Intraoperative awareness with recall is a significant psychological trauma; PTSD, anxiety disorders, and sleep disturbances are common sequelae that require formal psychological intervention.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":207}],"confusable_with":""},

  {"id":"epilepsy-surgery-anesthesia-d5","topic":topic15,"domain":dom_neuro,"discipline":disc,
   "stem":"For patients with intracranial mass lesions presenting with headache, visual disturbances, or seizures, what preoperative medication should be continued until the time of surgery?",
   "answer":"Corticosteroids and anticonvulsant therapy should be continued until the time of surgery; anticonvulsant blood concentrations may be measured if seizures are not well controlled.",
   "rationale":"Perioperative discontinuation of anticonvulsants risks breakthrough seizures; corticosteroids reduce vasogenic edema around brain tumors and must be maintained to prevent herniation.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":970}],"confusable_with":""},

  {"id":"epilepsy-surgery-anesthesia-d6","topic":topic15,"domain":dom_neuro,"discipline":disc,
   "stem":"Patients undergoing regional anesthesia with propofol sedation who may recall perioperative events: what communication should occur preoperatively?",
   "answer":"Patients should be made aware that they might recall perioperative events during regional anesthesia with propofol sedation; clarification of technique is important for informed consent.",
   "rationale":"Expectations management reduces psychological harm if awareness occurs; patients who are prepared for possible recall show less distress than those surprised by it.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":207}],"confusable_with":""},

  {"id":"epilepsy-surgery-anesthesia-d7","topic":topic15,"domain":dom_neuro,"discipline":disc,
   "stem":"Patients with Parkinson's disease may receive dopamine agonists as monotherapy or combination therapy. What is a rare serious side effect associated with dopamine agonist use?",
   "answer":"Pulmonary, cardiac, and retroperitoneal fibrosis; pleural effusion and thickening; and Raynaud syndrome are rare but serious side effects associated with some dopamine agonists.",
   "rationale":"Ergot-derived dopamine agonists (bromocriptine, cabergoline) have serotonergic and vasoconstrictive effects that can cause fibrotic reactions in multiple organs, requiring preoperative assessment.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1006}],"confusable_with":""},
]

# =====================================================================
# [16] Ethical Principles in Clinical Decision-Making
# (Chunks are primarily about AKI -- use what is relevant)
# =====================================================================
topic16 = "Ethical Principles in Clinical Decision-Making"

kps += [
  {"id":"ethical-principles-clinical-decision-making-d1","topic":topic16,"domain":dom_ethics,"discipline":disc,
   "stem":"When an anesthesiologist disagrees with the planned surgical or anesthetic approach, what is the ethical and professional obligation?",
   "answer":"The anesthesiologist should respond by voicing concerns and should not proceed until a safe anesthetic and surgical plan have been agreed upon.",
   "rationale":"Patient safety obligations require the anesthesiologist to advocate for the patient even when this creates interpersonal conflict; proceeding with a plan felt to be unsafe violates professional duty.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":57}],"confusable_with":""},

  {"id":"ethical-principles-clinical-decision-making-d2","topic":topic16,"domain":dom_ethics,"discipline":disc,
   "stem":"In goals-of-care discussions for critically ill patients with sepsis, what should the discussion take into account beyond acute illness prognosis?",
   "answer":"Goals-of-care discussions should take into consideration chronic medical conditions in addition to acute sepsis, as these affect overall prognosis and quality of life.",
   "rationale":"A patient's underlying trajectory (metastatic cancer, end-stage organ failure) fundamentally alters the risk-benefit analysis of aggressive ICU interventions; values and chronic prognosis must be integrated.",
   "bloom":"apply","source":[{"book":"Society Guideline","page":50}],"confusable_with":""},

  {"id":"ethical-principles-clinical-decision-making-d3","topic":topic16,"domain":dom_ethics,"discipline":disc,
   "stem":"Treating patients with dignity, respecting privacy and confidentiality, and listening to patient needs are listed as principles of good clinical practice in what context?",
   "answer":"These are principles of good record keeping and clinical practice during remote patient consultations, applicable to all clinical interactions including telemedicine.",
   "rationale":"The ethical principles of beneficence, non-maleficence, autonomy, and justice underlie these practical guidelines, ensuring patient-centered care regardless of care delivery format.",
   "bloom":"apply","source":[{"book":"Society Guideline: Guideline   GOLD 2024 COPD Full Report","page":147}],"confusable_with":""},

  {"id":"ethical-principles-clinical-decision-making-d4","topic":topic16,"domain":dom_ethics,"discipline":disc,
   "stem":"AKI occurs in up to what percentage of ICU admissions, and what is the ethical implication of this prevalence?",
   "answer":"AKI occurs in up to 30% of ICU admissions; its high prevalence means intensive care providers must proactively screen for, prevent, and treat it as a standard of care obligation.",
   "rationale":"High-frequency conditions with preventable contributors (nephrotoxin avoidance, contrast avoidance, optimization of hemodynamics) create ethical obligations for systematic prevention rather than reactive treatment.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Acute kidney injury","page":2}],"confusable_with":""},

  {"id":"ethical-principles-clinical-decision-making-d5","topic":topic16,"domain":dom_ethics,"discipline":disc,
   "stem":"In clinical decision-making for AKI, what is the ethical relevance of differentiating prerenal, intrinsic renal, and postrenal causes?",
   "answer":"Differentiating AKI etiology guides appropriate treatment strategy and avoids harmful interventions; applying the wrong treatment (e.g., IV fluids in obstructive AKI) can worsen outcomes.",
   "rationale":"Ethical clinical decision-making requires accurate diagnosis; appropriate use of diagnostic tools (urine electrolytes, imaging, biopsy) enables targeted treatment and avoids iatrogenic harm.",
   "bloom":"analyze","source":[{"book":"StatPearls: StatPearls   Acute kidney injury","page":1}],"confusable_with":""},

  {"id":"ethical-principles-clinical-decision-making-d6","topic":topic16,"domain":dom_ethics,"discipline":disc,
   "stem":"ACE inhibitors and ARBs are co-contributors to AKI. What is the ethical implication when reviewing medications for a hospitalized patient?",
   "answer":"All patients presenting with AKI warrant a comprehensive medication review; ACE inhibitors and ARBs are often co-contributors and should be held or adjusted, representing a duty-to-act principle.",
   "rationale":"Failure to identify and modify nephrotoxic medications violates the duty of non-maleficence; systematic medication reconciliation is both ethically required and standard perioperative care.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Acute kidney injury","page":6}],"confusable_with":""},

  {"id":"ethical-principles-clinical-decision-making-d7","topic":topic16,"domain":dom_ethics,"discipline":disc,
   "stem":"Informed consent for HIV testing must include what three elements per Florida statutes, as an example of patient-centered ethical obligations?",
   "answer":"Explanation of confidentiality, mandatory reporting implications, and opportunity for anonymous testing must be included in informed consent for HIV testing.",
   "rationale":"These requirements reflect core ethical principles: autonomy (informed choice), beneficence (appropriate testing), and justice (protecting against discrimination) applied to a sensitive clinical test.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   HIV  Antiretroviral Therapy (ART)","page":6}],"confusable_with":""},
]

print(f"Generated so far: {len(kps)} KPs")
print("OK")
