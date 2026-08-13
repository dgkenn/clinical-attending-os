import json, sys
sys.stdout.reconfigure(encoding='utf-8')

kps = []

# ── Topic 20: Succinylcholine pharmacology ───────────────────────────────────
# Chunks: pediatric MAC, MH, N2O, induction agents for asthma
kps += [
  {"id":"succinylcholine-pharmacology-1","topic":"Succinylcholine: pharmacology","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"Pediatric patients have a greater minute ventilation-to-FRC ratio than adults. What pharmacokinetic consequence does this have for inhaled anesthetic induction?",
   "answer":"The higher MV-to-FRC ratio in children causes a more rapid rise in alveolar anesthetic concentration, combined with greater brain blood flow, speeding inhalation induction compared to adults.",
   "rationale":"FRC is the buffer diluting inhaled anesthetic; a smaller FRC means faster equilibration; higher cardiac output to the brain further speeds CNS drug delivery.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1443}],"confusable_with":""},
  {"id":"succinylcholine-pharmacology-2","topic":"Succinylcholine: pharmacology","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"Which inhalation agent does NOT trigger malignant hyperthermia, making it the safest choice for MH-susceptible patients?",
   "answer":"Nitrous oxide does not trigger malignant hyperthermia; all potent halogenated volatile agents (sevoflurane, desflurane, isoflurane, halothane) are triggers. Succinylcholine is also a trigger.",
   "rationale":"MH susceptibility is caused by ryanodine receptor mutations leading to uncontrolled sarcoplasmic calcium release; halogenated agents and succinylcholine open these channels; N2O and non-depolarizing NMBs are safe.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":257}],"confusable_with":"Nitrous oxide MH safety (often confused with volatile agents; N2O is safe)"},
  {"id":"succinylcholine-pharmacology-3","topic":"Succinylcholine: pharmacology","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"Temperature must be closely monitored in pediatric patients because of their greater risk for two specific temperature-related complications. What are they?",
   "answer":"Pediatric patients have greater risk for malignant hyperthermia (particularly with volatile agents + succinylcholine) and greater susceptibility for intraoperative hypothermia or hyperthermia.",
   "rationale":"Higher surface-area-to-body-mass ratio makes children prone to heat loss; immature thermoregulatory mechanisms increase hypothermia risk; MH risk is also higher in pediatric patients.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1443}],"confusable_with":""},
  {"id":"succinylcholine-pharmacology-4","topic":"Succinylcholine: pharmacology","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"MAC for halogenated anesthetic agents is greater in pediatric patients compared to adults. How does MAC change across age?",
   "answer":"MAC is higher in infants and children than in adults; MAC decreases with increasing age, being highest in neonates/infants and progressively lower in older children and adults.",
   "rationale":"Developmentally, immature CNS may have different receptor densities or anesthetic sensitivities; MAC peaks in infancy and declines progressively throughout life.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1443}],"confusable_with":""},
  {"id":"succinylcholine-pharmacology-5","topic":"Succinylcholine: pharmacology","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"For a patient with asthma requiring intubation, what induction agents can produce bronchodilation?",
   "answer":"Propofol, ketamine, and sevoflurane can produce bronchodilation; ketamine is particularly useful in hemodynamically unstable asthmatic patients; sevoflurane provides the smoothest inhalation induction.",
   "rationale":"Ketamine releases catecholamines causing bronchial smooth muscle relaxation; propofol and sevoflurane blunt airway reactivity; avoiding histamine-releasing drugs (morphine, atracurium) reduces bronchospasm risk.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":867}],"confusable_with":"Succinylcholine bronchospasm risk (succinylcholine can trigger bronchospasm via histamine; rocuronium preferred in asthmatics)"}
]

# ── Topic 21: Sugammadex cyclodextrin reversal ───────────────────────────────
kps += [
  {"id":"sugammadex-reversal-1","topic":"Sugammadex: cyclodextrin reversal","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"Sugammadex is a cyclodextrin that reverses neuromuscular blockade. Which class of NMBAs does it reverse, and which class does it NOT reverse?",
   "answer":"Sugammadex reverses aminosteroid NMBAs (rocuronium, vecuronium); it does NOT reverse benzylisoquinoline NMBAs (cisatracurium, atracurium).",
   "rationale":"Sugammadex encapsulates steroidal NMBAs via hydrophobic inclusion; its chemical cavity does not accommodate the different molecular structure of benzylisoquinoline relaxants.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":368}],"confusable_with":"Neostigmine (acetylcholinesterase inhibitor that reverses all non-depolarizing NMBAs but requires anticholinergic co-administration)"},
  {"id":"sugammadex-reversal-2","topic":"Sugammadex: cyclodextrin reversal","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"After sugammadex reversal of rocuronium, re-dosing the same or a different aminosteroid NMBA is potentially impaired. Why?",
   "answer":"Following sugammadex reversal, subsequent neuromuscular blockade with steroidal (aminosteroid) NMBAs may be impaired because free sugammadex encapsulates newly administered rocuronium or vecuronium.",
   "rationale":"Sugammadex remains in circulation and binds available steroidal NMBA molecules; if re-paralysis is needed, benzylisoquinoline agents (cisatracurium) must be used.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":368}],"confusable_with":"Cysteine reversal (reverses gantacurium and fumarate NMBAs; different mechanism)"},
  {"id":"sugammadex-reversal-3","topic":"Sugammadex: cyclodextrin reversal","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"To assess return of pharyngeal muscle function (important for swallowing and airway protection), what neuromuscular monitoring site is used?",
   "answer":"To assess pharyngeal muscle function, monitor the corrugator supercilii (or adductor pollicis at rest); pharyngeal muscles are more sensitive than adductor pollicis, so the adductor pollicis serves as a conservative indicator.",
   "rationale":"Recovery at adductor pollicis precedes pharyngeal recovery; waiting for full adductor pollicis recovery ensures pharyngeal protection is restored, reducing aspiration risk.",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":39}],"confusable_with":"Corrugator supercilii (monitors deep blockade / diaphragm; used to guide intraoperative relaxation, not extubation)"},
  {"id":"sugammadex-reversal-4","topic":"Sugammadex: cyclodextrin reversal","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"What is the mechanism by which sugammadex reverses neuromuscular blockade?",
   "answer":"Sugammadex (modified gamma-cyclodextrin) encapsulates aminosteroid NMBA molecules in its hydrophobic cavity, forming a tight complex that is excreted renally, removing the NMBA from the neuromuscular junction.",
   "rationale":"Unlike neostigmine (which inhibits acetylcholinesterase), sugammadex physically sequesters the NMBA molecule, reversing blockade without affecting cholinergic receptors.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":367}],"confusable_with":"Neostigmine (increases ACh by inhibiting acetylcholinesterase; causes muscarinic side effects requiring atropine/glycopyrrolate)"},
  {"id":"sugammadex-reversal-5","topic":"Sugammadex: cyclodextrin reversal","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"Residual neuromuscular blockade (residual paralysis) can occur even when train-of-four responses seem normal. At what percentage of receptor blockade does TOF fade still appear normal?",
   "answer":"Up to 70-80% of receptors may remain blocked despite an apparently normal response to train-of-four stimulation; clinical weakness can persist without visible TOF fade.",
   "rationale":"The neuromuscular junction has a large margin of safety; TOF fade only becomes detectable when >70% of receptors are blocked, so absence of fade does not guarantee adequate reversal.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":370}],"confusable_with":""}
]

# ── Topic 22: Surgical Safety Checklists & Time-Outs ─────────────────────────
kps += [
  {"id":"surgical-safety-checklist-1","topic":"Surgical Safety Checklists & Time-Outs","domain":"Patient safety, ethics, professionalism & quality improvement (informed consent, checklists, error reporting, communication, human factors, crisis resource management)","discipline":"anesthesia",
   "stem":"What preventable surgical complications would be reduced if WHO surgical safety checklists were followed in every case?",
   "answer":"Wrong-site surgery, procedures on the wrong patient, retained foreign objects, and medication administration errors would be reduced by consistent checklist use.",
   "rationale":"The WHO checklist addresses pre-incision team verification, site marking, and post-procedure counts; each item targets a specific category of preventable error.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":33}],"confusable_with":""},
  {"id":"surgical-safety-checklist-2","topic":"Surgical Safety Checklists & Time-Outs","domain":"Patient safety, ethics, professionalism & quality improvement (informed consent, checklists, error reporting, communication, human factors, crisis resource management)","discipline":"anesthesia",
   "stem":"For surgical safety checklists to be maximally effective, how must they be executed?",
   "answer":"Checklists must be used consistently, all team members must be focused during execution, and checklists are most effective when performed in an interactive (read-aloud, verbal confirmation) fashion rather than silently.",
   "rationale":"A checklist read by one person without team engagement fails to catch errors; interactive confirmation ensures each item is actively verified by the person responsible for that domain.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":33}],"confusable_with":""},
  {"id":"surgical-safety-checklist-3","topic":"Surgical Safety Checklists & Time-Outs","domain":"Patient safety, ethics, professionalism & quality improvement (informed consent, checklists, error reporting, communication, human factors, crisis resource management)","discipline":"anesthesia",
   "stem":"What is the most common risk factor for surgical fires in the operating room?",
   "answer":"Open delivery of oxygen (especially concentrations >30%) is the most common risk factor for surgical fires; oxygen concentration should be guided by clinical need, not habit.",
   "rationale":"The fire triad requires oxidizer (O2/N2O), ignition source (electrocautery), and fuel (drapes, patient hair); elevated O2 concentration dramatically increases ignition risk.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":32}],"confusable_with":""},
  {"id":"surgical-safety-checklist-4","topic":"Surgical Safety Checklists & Time-Outs","domain":"Patient safety, ethics, professionalism & quality improvement (informed consent, checklists, error reporting, communication, human factors, crisis resource management)","discipline":"anesthesia",
   "stem":"Drug syringes in the anesthetic workspace should be restricted in what way to minimize medication errors?",
   "answer":"Drug syringes and ampules should be restricted to those needed for the current patient; drugs should be consistently diluted to the same concentration, clearly labeled, and scanning of bar-coded labels may further reduce errors.",
   "rationale":"Cluttered workspaces with multiple unlabeled syringes increase wrong-drug error risk; standardized concentrations and labels allow rapid error detection.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":2024}],"confusable_with":""},
  {"id":"surgical-safety-checklist-5","topic":"Surgical Safety Checklists & Time-Outs","domain":"Patient safety, ethics, professionalism & quality improvement (informed consent, checklists, error reporting, communication, human factors, crisis resource management)","discipline":"anesthesia",
   "stem":"Central venous catheter insertion checklists are an example of what broader safety strategy in medicine?",
   "answer":"CVC checklists are a cognitive aid strategy that reduces infection rates and complications by standardizing technique; they represent the broader principle that checklists improve quality and safety in procedural environments.",
   "rationale":"Mandated checklists for CVC insertion (including hand hygiene, maximal barrier precautions, chlorhexidine prep, optimal site selection) dramatically reduced CLABSI rates in landmark studies.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":2210}],"confusable_with":""}
]

# ── Topic 23: Sympathetic blocks ─────────────────────────────────────────────
kps += [
  {"id":"sympathetic-blocks-1","topic":"Sympathetic blocks","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"What is the main limitation of using intrathecal or epidural blocks for selective sympathetic blockade?",
   "answer":"Intrathecal and epidural approaches block both somatic and sympathetic fibers; selective sympathetic blockade is not achievable without concurrent somatic nerve block.",
   "rationale":"The sympathetic preganglionic fibers (B fibers) exit the spinal cord with somatic nerves and travel together; separating their block requires specific ganglion-targeted approaches.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1785}],"confusable_with":"Selective sympathetic blocks (stellate ganglion, celiac plexus, lumbar sympathetic) - these target specific ganglia without somatic block"},
  {"id":"sympathetic-blocks-2","topic":"Sympathetic blocks","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"Sympathetic outflow from the spinal cord is thoracolumbar. Where do sympathetic preganglionic fibers exit, and what fiber type are they?",
   "answer":"Sympathetic preganglionic fibers (small, myelinated B fibers) exit the spinal cord with anterior roots from T1-L2/L3; parasympathetic outflow is craniosacral.",
   "rationale":"The thoracolumbar origin of sympathetic fibers explains why high neuraxial blocks cause sympathectomy from T1 downward; lower block levels produce more limited sympathectomy.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1555}],"confusable_with":"Parasympathetic (craniosacral: CN III, VII, IX, X + S2-4); confusion leads to mislabeling autonomic effects"},
  {"id":"sympathetic-blocks-3","topic":"Sympathetic blocks","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"Radiofrequency ablation (RFA) is used for sympathetic block. What temperature and duration is used for controlled neural ablation?",
   "answer":"RFA uses 60-90 degrees C for 1-3 minutes to ablate the nerve without causing excessive collateral tissue damage.",
   "rationale":"Controlled heat denatures nerve proteins causing conduction block; the temperature-duration combination is calibrated to produce effective analgesia while avoiding surrounding tissue injury.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1797}],"confusable_with":"Cryoneurolysis (uses cold -20 to -70 degrees C; produces temporary analgesia for weeks to months)"},
  {"id":"sympathetic-blocks-4","topic":"Sympathetic blocks","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"Chemical neurolysis with alcohol or phenol produces what duration of sympathetic block, and what is the risk of repeated treatment?",
   "answer":"Chemical neurolysis produces temporary blockade; although initial results may be excellent, pain may recur within weeks to months, and new deafferentation or central pain may develop in the majority of patients.",
   "rationale":"Nerve fiber regeneration and central sensitization mean chemical neurolysis provides temporary relief; repeated treatments have diminishing returns and risk new pain syndromes.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1798}],"confusable_with":""},
  {"id":"sympathetic-blocks-5","topic":"Sympathetic blocks","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"Before performing a neurolytic sympathetic block, what is the standard diagnostic procedure?",
   "answer":"A diagnostic block with local anesthetic should precede any neurolytic procedure to confirm pain relief and patient response; consent for the neurolytic procedure should be obtained in advance and may be performed immediately after a positive diagnostic block.",
   "rationale":"Diagnostic blocks predict response to permanent neurolysis; proceeding to neurolysis without prior diagnostic confirmation risks irreversible nerve damage without therapeutic benefit.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1799}],"confusable_with":""}
]

# ── Topic 24: Systemic Lidocaine Infusion ────────────────────────────────────
kps += [
  {"id":"systemic-lidocaine-infusion-1","topic":"Systemic Lidocaine Infusion","domain":"Pain medicine (acute perioperative pain, multimodal analgesia, chronic pain management, regional techniques for pain, opioid management)","discipline":"anesthesia",
   "stem":"Systemic lidocaine infusion as a perioperative analgesic adjunct primarily reduces what outcome?",
   "answer":"Perioperative IV lidocaine infusion reduces postoperative opioid consumption, pain scores, and incidence of ileus, particularly in abdominal surgery.",
   "rationale":"Lidocaine's sodium channel blockade reduces peripheral and central sensitization; its anti-inflammatory properties reduce cytokine-mediated pain; reduced ileus results from attenuated inflammatory response.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1812}],"confusable_with":"Epidural lidocaine (much higher concentrations at site; different mechanism proportionality)"},
  {"id":"systemic-lidocaine-infusion-2","topic":"Systemic Lidocaine Infusion","domain":"Pain medicine (acute perioperative pain, multimodal analgesia, chronic pain management, regional techniques for pain, opioid management)","discipline":"anesthesia",
   "stem":"A patient undergoing abdominal surgery without epidural has IV lidocaine infusion planned. What is the evidence for this approach?",
   "answer":"In the absence of an epidural catheter, IV lidocaine infusion can reduce opioid requirements and PONV; epidural blockade still provides superior analgesia at rest and with movement compared to systemic opioids alone.",
   "rationale":"Epidural analgesia remains the gold standard for thoraco-abdominal procedures, but IV lidocaine is a useful component of multimodal analgesia when epidural is not feasible or desired.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1812}],"confusable_with":""},
  {"id":"systemic-lidocaine-infusion-3","topic":"Systemic Lidocaine Infusion","domain":"Pain medicine (acute perioperative pain, multimodal analgesia, chronic pain management, regional techniques for pain, opioid management)","discipline":"anesthesia",
   "stem":"What class of medications commonly used for neuropathic pain acts by reducing spontaneous neural discharges via sodium channel stabilization?",
   "answer":"Phenytoin, carbamazepine, valproic acid, and gabapentin reduce spontaneous neural discharges that contribute to neuropathic pain; pregabalin is approved for diabetic neuropathy.",
   "rationale":"Neuropathic pain involves ectopic discharge from injured neurons; sodium channel-stabilizing anticonvulsants reduce this hyperexcitability through membrane-stabilizing mechanisms.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1761}],"confusable_with":"Opioids (reduce neuropathic pain through central mechanisms, not membrane stabilization)"},
  {"id":"systemic-lidocaine-infusion-4","topic":"Systemic Lidocaine Infusion","domain":"Pain medicine (acute perioperative pain, multimodal analgesia, chronic pain management, regional techniques for pain, opioid management)","discipline":"anesthesia",
   "stem":"Intrathecal clonidine added to spinal local anesthetic provides what specific benefit for outpatient surgery?",
   "answer":"Intrathecal clonidine added to spinal anesthetic provides effective alpha-2 agonist analgesia while avoiding opioid side effects (nausea, pruritus, urinary retention) that may delay hospital discharge.",
   "rationale":"Alpha-2 agonists modulate spinal pain transmission without mu-receptor activation; absence of opioid side effects makes this combination attractive for ambulatory settings.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1825}],"confusable_with":"Neuraxial opioids (effective but side effects - nausea, pruritus, urinary retention - may delay discharge)"},
  {"id":"systemic-lidocaine-infusion-5","topic":"Systemic Lidocaine Infusion","domain":"Pain medicine (acute perioperative pain, multimodal analgesia, chronic pain management, regional techniques for pain, opioid management)","discipline":"anesthesia",
   "stem":"IV esmolol has been shown to reduce what perioperative outcomes when used as an anesthetic adjunct?",
   "answer":"IV esmolol reduces volatile anesthetic requirement (reduces MAC), decreases postoperative pain intensity, lowers opioid consumption, and reduces PONV.",
   "rationale":"Beta-blockade reduces sympathetic-mediated sensitization; esmolol's effects on pain and PONV suggest a direct central or peripheral analgesic mechanism beyond heart rate control.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1826}],"confusable_with":""}
]

# ── Topic 25: Systemic labor analgesia ───────────────────────────────────────
kps += [
  {"id":"systemic-labor-analgesia-1","topic":"Systemic labor analgesia","domain":"Obstetric anesthesia (maternal physiology, labor analgesia, cesarean delivery, obstetric emergencies, neonatal resuscitation)","discipline":"anesthesia",
   "stem":"How is the risk of systemic local anesthetic toxicity minimized during epidural analgesia for labor?",
   "answer":"Systemic LA toxicity risk is minimized by slowly administering dilute solutions for labor pain and fractionating the total dose for cesarean section into 5 mL increments with aspiration before each.",
   "rationale":"Incremental dosing limits the amount of LA delivered into an intravascular catheter before toxicity signs appear; dilute concentrations reduce toxic dose exposure during accidental IV injection.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1384}],"confusable_with":""},
  {"id":"systemic-labor-analgesia-2","topic":"Systemic labor analgesia","domain":"Obstetric anesthesia (maternal physiology, labor analgesia, cesarean delivery, obstetric emergencies, neonatal resuscitation)","discipline":"anesthesia",
   "stem":"When a high bupivacaine concentration (0.25%) is used for continuous epidural analgesia, what effect may occur on the second stage of labor?",
   "answer":"Dense regional analgesia/anesthesia with bupivacaine 0.25% may prolong the second stage by approximately 15-30 minutes and remove the urge to push.",
   "rationale":"Intense motor block reduces perineal sensation and motor coordination of expulsive efforts; dilute solutions (0.0625-0.125% bupivacaine) minimize motor block while preserving analgesia.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1372}],"confusable_with":""},
  {"id":"systemic-labor-analgesia-3","topic":"Systemic labor analgesia","domain":"Obstetric anesthesia (maternal physiology, labor analgesia, cesarean delivery, obstetric emergencies, neonatal resuscitation)","discipline":"anesthesia",
   "stem":"Deaths associated with general anesthesia in obstetric patients are generally related to what complications?",
   "answer":"Deaths associated with obstetric GA are generally related to airway problems: inability to intubate, inability to ventilate, or aspiration pneumonitis.",
   "rationale":"Parturients have full stomachs, reduced FRC, edematous airways, and weight gain making intubation more difficult; failed airway management is the leading cause of anesthesia-related maternal mortality.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1403}],"confusable_with":"Regional anesthesia complications (total spinal, LA toxicity; less common than airway-related GA deaths in obstetrics)"},
  {"id":"systemic-labor-analgesia-4","topic":"Systemic labor analgesia","domain":"Obstetric anesthesia (maternal physiology, labor analgesia, cesarean delivery, obstetric emergencies, neonatal resuscitation)","discipline":"anesthesia",
   "stem":"Epidural catheter migration into the intravascular space may be heralded by loss of effective analgesia. What additional signs indicate this and why do they require high suspicion?",
   "answer":"Migration may be heralded by loss of effective analgesia; high suspicion is required because overt signs of systemic toxicity may initially be absent; CNS and cardiac symptoms follow.",
   "rationale":"LA concentration during labor epidural is dilute; early intravascular injection may only cause analgesia failure before toxic plasma concentrations develop; waiting for frank toxicity risks cardiac arrest.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1398}],"confusable_with":""},
  {"id":"systemic-labor-analgesia-5","topic":"Systemic labor analgesia","domain":"Obstetric anesthesia (maternal physiology, labor analgesia, cesarean delivery, obstetric emergencies, neonatal resuscitation)","discipline":"anesthesia",
   "stem":"Magnesium potentiates neuromuscular blocking agents. What clinical guideline applies when NMBAs are needed in a patient on magnesium for preeclampsia?",
   "answer":"Because magnesium potentiates non-depolarizing muscle relaxants, doses of NMBAs should be reduced and guided by peripheral nerve stimulator monitoring.",
   "rationale":"Magnesium competes with calcium at the neuromuscular junction, reducing ACh release and receptor sensitivity; this synergy with NMBAs prolongs and deepens paralysis unexpectedly.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1423}],"confusable_with":"Magnesium toxicity treatment (calcium gluconate given for respiratory arrest; different from NMBA dose adjustment)"}
]

# ── Topic 26: TBI ICP Management & Multimodal Monitoring ─────────────────────
kps += [
  {"id":"tbi-icp-management-1","topic":"TBI: ICP Management & Multimodal Monitoring","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"Normal cerebral perfusion pressure (CPP) is approximately what value, and how is it calculated?",
   "answer":"Normal CPP is approximately 80-100 mmHg; CPP = MAP - ICP. In TBI management, CPP should be maintained at 60-70 mmHg minimum.",
   "rationale":"CPP drives cerebral blood flow; below the autoregulatory threshold (approximately 50 mmHg CPP in normal brains, potentially higher in chronic hypertensives), CBF becomes pressure-passive.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1338}],"confusable_with":"MAP (mean arterial pressure; CPP accounts for ICP which can be elevated in TBI)"},
  {"id":"tbi-icp-management-2","topic":"TBI: ICP Management & Multimodal Monitoring","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"In a TBI patient, at what GCS score is intubation generally indicated?",
   "answer":"Intubation indications in TBI include deteriorating GCS score, typically 8 or less, or concurrent airway/ventilatory compromise from associated injuries.",
   "rationale":"GCS <=8 (severe TBI) indicates inability to protect the airway and likelihood of inadequate ventilation; intubation secures the airway and allows controlled ventilation to optimize CPP.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":808}],"confusable_with":""},
  {"id":"tbi-icp-management-3","topic":"TBI: ICP Management & Multimodal Monitoring","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"Beyond ICP and CPP, what additional parameters does modern multimodal TBI monitoring include?",
   "answer":"Multimodal TBI monitoring now includes partial pressure of brain tissue oxygen (PbtO2) and cerebral metabolic monitoring through microdialysis, alongside ICP and CPP.",
   "rationale":"ICP and CPP monitor global hemodynamic parameters; PbtO2 detects regional ischemia even when ICP/CPP are acceptable; microdialysis detects metabolic crises (lactate/pyruvate ratio) from ischemia or spreading depression.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Traumatic Brain Injury (TBI)","page":10}],"confusable_with":""},
  {"id":"tbi-icp-management-4","topic":"TBI: ICP Management & Multimodal Monitoring","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"In TBI without a surgical clot, what are the primary medical interventions to treat elevated ICP?",
   "answer":"Medical ICP treatments: head elevation 30 degrees, mannitol or hypertonic saline, controlled normocarbia (avoid hypo/hypercarbia), sedation/analgesia, CSF drainage via EVD if placed; avoid corticosteroids (increase mortality in TBI).",
   "rationale":"Each intervention targets a component of the Monro-Kellie doctrine (blood, brain tissue, or CSF); corticosteroids increase mortality in TBI unlike vasogenic edema from tumors.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1338}],"confusable_with":"Corticosteroids for tumor-related ICP (indicated; vasogenic edema responds; TBI does not)"},
  {"id":"tbi-icp-management-5","topic":"TBI: ICP Management & Multimodal Monitoring","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"Patients with elevated ICP who need ICP monitoring should have it in place. In what two clinical scenarios is ICP monitoring specifically indicated?",
   "answer":"ICP monitoring is indicated in patients with elevated ICP and those at risk of developing it (e.g., severe TBI with abnormal CT) to enable appropriate CPP management.",
   "rationale":"ICP monitoring guides targeted therapy; without it, CPP cannot be calculated and treatment of intracranial hypertension is empirical and potentially harmful.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1207}],"confusable_with":""}
]
kps += [{"_type":"illness_script","topic":"TBI: ICP Management & Multimodal Monitoring","discipline":"anesthesia",
  "enabling_conditions":"Head trauma (MVA, falls, assault, sports); coagulopathy increases hematoma risk",
  "pathophysiology":"Primary brain injury (contusion, laceration) + secondary injury (ischemia from elevated ICP reducing CPP, hypoxia, hypoglycemia, spreading cortical depression)",
  "time_course":"Primary injury at impact; secondary injury evolves over hours-days; cerebral edema peaks 24-72 h",
  "key_features":"GCS <=8 triggers intubation; CPP = MAP - ICP, target >=60-70 mmHg; avoid steroids; PbtO2 + microdialysis complement ICP monitoring",
  "consequence_if_missed":"Untreated intracranial hypertension causes herniation, brainstem compression, and death; corticosteroid use increases mortality"}]

print('Topics 20-26 done:', len(kps))
with open('data/kp_part26_batch3.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print('Batch 3 written')
