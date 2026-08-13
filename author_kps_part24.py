#!/usr/bin/env python3
"""Author knowledge points for items 792-825."""
import json
import re

with open('data/_kp_retrieval_full.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

slice_data = data[792:825]

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.rstrip('-')

all_entries = []

# Topic 792: Neurological disease in pregnancy
slug = "neurological-disease-in-pregnancy"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Neurological disease in pregnancy",
        "domain": "Obstetric anesthesia",
        "discipline": "anesthesia",
        "stem": "What are the major categories of neurological conditions that can present or worsen during pregnancy?",
        "answer": "Neurological disease in pregnancy includes seizure disorders, eclampsia/preeclampsia, peripartum cardiomyopathy, myasthenia gravis, multiple sclerosis, and cerebrovascular events; severity and management vary by condition.",
        "rationale": "Pregnancy-related physiological changes (edema, metabolic demands, hypertension) can exacerbate preexisting neurological conditions or precipitate new ones.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 781}],
        "confusable_with": "Cardiac disease in pregnancy (separate from but overlapping CNS pathology)"
    },
    {
        "id": f"{slug}-2",
        "topic": "Neurological disease in pregnancy",
        "domain": "Obstetric anesthesia",
        "discipline": "anesthesia",
        "stem": "How do seizure threshold and seizure management considerations change during pregnancy?",
        "answer": "Pregnancy reduces seizure threshold due to hormonal changes, hemodilution of antiepileptic drugs, and metabolic demands; antiepileptic drug levels require monitoring and possible dosage adjustment.",
        "rationale": "Physiological changes in pregnancy including increased volume of distribution and metabolism increase seizure risk in epilepsy patients.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 781}],
        "confusable_with": "Eclampsia (which is pregnancy-specific, not a preexisting neurological disorder)"
    }
])

# Topic 793: Neuromuscular Blocking Agents Pharmacology
slug = "neuromuscular-blocking-agents-pharmacology"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Neuromuscular Blocking Agents Pharmacology",
        "domain": "General anesthesia",
        "discipline": "anesthesia",
        "stem": "What are the two major classes of neuromuscular blocking agents and their mechanisms of action?",
        "answer": "Depolarizing agents (succinylcholine) cause sustained depolarization; non-depolarizing agents block the nicotinic acetylcholine receptor competitively, preventing acetylcholine binding.",
        "rationale": "These mechanisms determine onset, duration, metabolism, and reversal strategy for each drug class.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 490}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Neuromuscular Blocking Agents Pharmacology",
        "domain": "General anesthesia",
        "discipline": "anesthesia",
        "stem": "What factors determine the choice between depolarizing and non-depolarizing neuromuscular blocking agents intraoperatively?",
        "answer": "Depolarizing agents are chosen for rapid sequence intubation due to fast onset; non-depolarizing preferred when hyperkalemia risk exists, for prolonged blockade, or when reversal is needed.",
        "rationale": "Depolarizing agents carry hyperkalemia and malignant hyperthermia risks; non-depolarizing agents allow fine-tuned duration and reversibility.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 490}],
        "confusable_with": "Choice is based on pharmacokinetics and clinical scenario, not interchangeability"
    }
])

# Topic 794: Neuromuscular Junction Physiology
slug = "neuromuscular-junction-physiology"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Neuromuscular Junction Physiology",
        "domain": "General anesthesia",
        "discipline": "anesthesia",
        "stem": "What are the key anatomical and functional components of the neuromuscular junction?",
        "answer": "The NMJ consists of the motor nerve terminal (releases acetylcholine), the synaptic cleft, and the muscle membrane (with acetylcholine receptors); acetylcholine binding opens ion channels causing depolarization.",
        "rationale": "Understanding this three-part structure explains how drugs and diseases affect neuromuscular transmission.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 483}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Neuromuscular Junction Physiology",
        "domain": "General anesthesia",
        "discipline": "anesthesia",
        "stem": "What is the normal neuromuscular transmission process and how is acetylcholine recycled at the motor nerve terminal?",
        "answer": "Action potential triggers acetylcholine release; ACh binds nicotinic receptors; acetylcholinesterase hydrolyzes acetylcholine; choline is recycled back into the nerve terminal via reuptake.",
        "rationale": "This cycle maintains the safety margin for neuromuscular transmission; blocking any step impairs muscle contraction.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 483}],
        "confusable_with": ""
    }
])

# Topic 795: Neuromuscular monitoring
slug = "neuromuscular-monitoring"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Neuromuscular monitoring",
        "domain": "General anesthesia",
        "discipline": "anesthesia",
        "stem": "What are the primary modes of neuromuscular monitoring and what do they measure?",
        "answer": "Train-of-four (TOF), tetanic stimulation, and post-tetanic potentiation measure the response to peripheral nerve stimulation; TOF count, ratio, and recovery characterize blockade depth.",
        "rationale": "Objective monitoring ensures adequate reversal and prevents residual blockade complications.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 510}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Neuromuscular monitoring",
        "domain": "General anesthesia",
        "discipline": "anesthesia",
        "stem": "What TOF ratio indicates adequate neuromuscular recovery and why is sustained tetanic response important?",
        "answer": "TOF ratio ≥0.9 (modern standards) indicates safe reversal readiness; sustained tetanic response (no fade) confirms adequate acetylcholine reserves.",
        "rationale": "Fade during tetanic stimulation indicates NMB present; achieving ≥0.9 prevents postoperative respiratory complications.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 510}],
        "confusable_with": ""
    }
])

# Topic 796: Neuropathic Pain Syndromes
slug = "neuropathic-pain-syndromes"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Neuropathic Pain Syndromes",
        "domain": "Pain management",
        "discipline": "anesthesia",
        "stem": "What distinguishes neuropathic pain from nociceptive pain in terms of mechanism and characteristics?",
        "answer": "Neuropathic pain results from nerve injury or dysfunction (burning, tingling, allodynia); nociceptive pain from tissue damage (acute, sharp); neuropathic pain involves abnormal nervous system processing.",
        "rationale": "Different mechanisms require distinct treatment approaches; neuropathic pain responds poorly to standard opioids.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 1510}],
        "confusable_with": "Nociceptive pain (same anatomical area but different etiology)"
    },
    {
        "id": f"{slug}-2",
        "topic": "Neuropathic Pain Syndromes",
        "domain": "Pain management",
        "discipline": "anesthesia",
        "stem": "What are first-line pharmacological treatments for perioperative neuropathic pain?",
        "answer": "Gabapentinoids (gabapentin, pregabalin), SNRIs (duloxetine, venlafaxine), and tricyclic antidepressants (amitriptyline) are first-line; regional anesthesia and nerve blocks target the source.",
        "rationale": "These agents modulate neuropathic pain pathways better than opioids alone; regional techniques prevent wind-up and central sensitization.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 1510}],
        "confusable_with": ""
    }
])

# Topic 797: Neurophysiology
slug = "neurophysiology"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Neurophysiology",
        "domain": "General anesthesia",
        "discipline": "anesthesia",
        "stem": "What are the major functional divisions of the nervous system and their roles in perioperative physiology?",
        "answer": "Central nervous system (brain, spinal cord) processes information; peripheral nervous system (somatic, autonomic) carries motor/sensory signals; autonomic divides into sympathetic (arousal) and parasympathetic (recovery).",
        "rationale": "Anesthetic drugs target all divisions; understanding distribution explains side effects and drug interactions.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 305}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Neurophysiology",
        "domain": "General anesthesia",
        "discipline": "anesthesia",
        "stem": "How do action potentials propagate along axons and what role does myelination play?",
        "answer": "Depolarization opens sodium channels; repolarization closes sodium and opens potassium channels; myelination speeds conduction via saltatory propagation in large fibers.",
        "rationale": "Local anesthetics block sodium channels; understanding conduction speed explains why small C fibers are blocked before large motor fibers.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 305}],
        "confusable_with": ""
    }
])

# Topic 798: Neuroradiology & MRI Anesthesia
slug = "neuroradiology-mri-anesthesia"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Neuroradiology & MRI Anesthesia",
        "domain": "Special procedures",
        "discipline": "anesthesia",
        "stem": "What are the anesthetic considerations for patients undergoing MRI imaging procedures?",
        "answer": "MRI requires ferromagnetic safety screening; anesthesia equipment must be MRI-compatible; sedation/anesthesia increases aspiration risk due to scanner confinement and delayed rescue access.",
        "rationale": "The closed MRI environment limits patient access and monitoring capabilities; metal implants cause burns and artifact.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 876}],
        "confusable_with": "CT anesthesia (different safety profile; CT allows faster patient access)"
    },
    {
        "id": f"{slug}-2",
        "topic": "Neuroradiology & MRI Anesthesia",
        "domain": "Special procedures",
        "discipline": "anesthesia",
        "stem": "Which anesthetic agents and monitoring devices are contraindicated in the MRI environment?",
        "answer": "Ferromagnetic instruments, pulse oximeters with metallic sensors, and some IV poles are contraindicated; propofol and volatile agents are safe; avoid ferromagnetic laryngoscopes.",
        "rationale": "Magnetic fields can displace ferromagnetic objects, causing burns or injury; incompatible monitors create artifact and lose signal.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 876}],
        "confusable_with": ""
    }
])

# Topic 799: Never Events
slug = "never-events-in-anesthesia-perioperative-care"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Never Events in Anesthesia & Perioperative Care",
        "domain": "Patient safety",
        "discipline": "anesthesia",
        "stem": "What are anesthesia-related never events and what prevention strategies minimize their occurrence?",
        "answer": "Never events include wrong-patient/wrong-site surgery, retained foreign objects, severe anesthetic complications (esophageal intubation, awareness); prevention requires time-outs, equipment checks, monitoring, and communication.",
        "rationale": "Never events are deemed preventable; systematic checks catch errors before they harm patients.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 1698}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Never Events in Anesthesia & Perioperative Care",
        "domain": "Patient safety",
        "discipline": "anesthesia",
        "stem": "What is the role of the pre-operative briefing and timeout in preventing never events?",
        "answer": "Pre-operative briefing confirms patient identity, surgical site, and procedure; timeout halts the procedure to verify these elements with the entire OR team.",
        "rationale": "Team communication and verification prevent the majority of wrong-site and wrong-patient incidents.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 1698}],
        "confusable_with": ""
    }
])

# Topic 800: Nitroglycerin & nitroprusside
slug = "nitroglycerin-nitroprusside-vasodilators"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Nitroglycerin & nitroprusside: vasodilators",
        "domain": "Cardiovascular pharmacology",
        "discipline": "anesthesia",
        "stem": "What are the mechanisms of action and clinical uses of nitroglycerin and nitroprusside?",
        "answer": "Nitroglycerin and nitroprusside are direct vasodilators that activate guanylate cyclase via NO, increasing cGMP and smooth muscle relaxation; nitroprusside is faster and more potent, used for acute hypertension control.",
        "rationale": "Both drugs cause venous and arterial dilation; nitroprusside's rapid onset and short duration make it ideal for intraoperative hypertension management.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 388}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Nitroglycerin & nitroprusside: vasodilators",
        "domain": "Cardiovascular pharmacology",
        "discipline": "anesthesia",
        "stem": "What is cyanide toxicity with nitroprusside and how is it prevented or managed?",
        "answer": "Nitroprusside releases cyanide ions metabolically; toxicity occurs with prolonged infusion (>24 hours) or high doses (>10 mcg/kg/min); sodium thiosulfate or hydroxocobalamin can bind cyanide.",
        "rationale": "Cyanide accumulation causes lactic acidosis and cellular dysfunction; limits nitroprusside to short-term perioperative use.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 388}],
        "confusable_with": ""
    }
])

# Topic 801: Nitrous oxide
slug = "nitrous-oxide-pharmacology-toxicity"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Nitrous oxide: pharmacology & toxicity",
        "domain": "General anesthesia",
        "discipline": "anesthesia",
        "stem": "What is the mechanism of anesthesia for nitrous oxide and what are its analgesic properties?",
        "answer": "Nitrous oxide acts as an NMDA receptor antagonist, producing anesthesia; it has significant analgesic properties at sub-anesthetic doses (30-50%), making it a weak general anesthetic with analgesia.",
        "rationale": "N2O's analgesic potency allows use as a supplement to potent volatile agents or opioids, reducing their requirements.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 157}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Nitrous oxide: pharmacology & toxicity",
        "domain": "General anesthesia",
        "discipline": "anesthesia",
        "stem": "What are the toxicity risks of chronic nitrous oxide exposure and how does it affect vitamin B12?",
        "answer": "Chronic N2O exposure oxidizes cobalamin (B12), inactivating methionine synthase and causing megaloblastic anemia, neuropathy, and myelopathy; occupational exposure is a concern in anesthesia and dental personnel.",
        "rationale": "N2O toxicity accumulates with repeated exposure; regular air changes and scavenging reduce occupational risk.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 157}],
        "confusable_with": ""
    }
])

# Topic 802: Non-depolarizing NMBs
slug = "non-depolarizing-nmbs-mechanisms-pharmacokinetics"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Non-depolarizing NMBs: mechanisms & pharmacokinetics",
        "domain": "General anesthesia",
        "discipline": "anesthesia",
        "stem": "How do non-depolarizing neuromuscular blockers work and what is the mechanism of action?",
        "answer": "Non-depolarizing NMBs competitively block acetylcholine at the nicotinic receptor without depolarizing muscle; they are reversed by acetylcholinesterase inhibitors (neostigmine, sugammadex).",
        "rationale": "Competitive blockade allows reversal; the drug-receptor interaction is in equilibrium, so acetylcholinesterase inhibitors restore acetylcholine dominance.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 503}],
        "confusable_with": "Depolarizing agents (succinylcholine) which cannot be reversed"
    },
    {
        "id": f"{slug}-2",
        "topic": "Non-depolarizing NMBs: mechanisms & pharmacokinetics",
        "domain": "General anesthesia",
        "discipline": "anesthesia",
        "stem": "What is the duration classification of non-depolarizing agents and what factors affect their metabolism?",
        "answer": "Short-acting (15-20 min), intermediate-acting (30-40 min), and long-acting (60-90+ min) agents; metabolism depends on Hofmann elimination (organ-independent), ester hydrolysis, or renal clearance.",
        "rationale": "Understanding metabolism helps predict duration in renal failure or hepatic disease; Hofmann elimination is unaffected by organ function.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 503}],
        "confusable_with": ""
    }
])

# Topic 803: Non-obstetric surgery during pregnancy
slug = "non-obstetric-surgery-during-pregnancy"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Non-obstetric surgery during pregnancy",
        "domain": "Obstetric anesthesia",
        "discipline": "anesthesia",
        "stem": "What are the key anesthetic considerations for non-obstetric surgery in pregnant patients?",
        "answer": "Avoid supine position (aortocaval compression); maintain uteroplacental perfusion; avoid teratogenic agents (NSAIDs, ACE inhibitors in first trimester); increased aspiration risk; monitor fetal heart rate if viable.",
        "rationale": "Pregnancy-induced anatomical and physiological changes increase operative risks; careful drug selection and positioning prevent fetal compromise.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 1399}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Non-obstetric surgery during pregnancy",
        "domain": "Obstetric anesthesia",
        "discipline": "anesthesia",
        "stem": "What is the optimal timing for non-obstetric surgery in pregnant patients and which surgical emergencies cannot be delayed?",
        "answer": "Elective surgery is best performed in the second trimester; emergency surgical conditions (appendicitis, cholecystitis, perforated viscus, trauma) cannot be delayed regardless of trimester.",
        "rationale": "Second trimester minimizes teratogenic risk and maternal physiological stress; life-threatening conditions override timing considerations.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 1399}],
        "confusable_with": ""
    }
])

# Topic 804: Nutritional assessment
slug = "nutritional-assessment-and-optimization"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Nutritional assessment and optimization",
        "domain": "Perioperative medicine",
        "discipline": "anesthesia",
        "stem": "What are the components of nutritional assessment in perioperative patients and which markers indicate malnutrition?",
        "answer": "Assessment includes dietary history, weight changes, albumin (<3.5 g/dL), prealbumin (<20 mg/dL), total lymphocyte count, and anthropometric measurements; markers predict increased complications.",
        "rationale": "Malnutrition impairs immune function and wound healing; preoperative identification allows intervention.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 664}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Nutritional assessment and optimization",
        "domain": "Perioperative medicine",
        "discipline": "anesthesia",
        "stem": "What are evidence-based nutritional interventions to reduce perioperative complications?",
        "answer": "Preoperative supplementation with arginine, glutamine, and omega-3 fatty acids in malnourished patients; early postoperative feeding (enteral preferred); adequate caloric and protein intake.",
        "rationale": "Nutritional support enhances wound healing, immune function, and reduces infection risk; enteral feeding preserves gut barrier integrity.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 664}],
        "confusable_with": ""
    }
])

# Topic 805: Obesity in obstetric anesthesia
slug = "obesity-in-obstetric-anesthesia"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Obesity in obstetric anesthesia",
        "domain": "Obstetric anesthesia",
        "discipline": "anesthesia",
        "stem": "What are the unique physiological challenges of pregnancy in obese parturients and how do they affect anesthetic management?",
        "answer": "Obesity exacerbates pregnancy-related airway changes, aortocaval compression, aspiration risk, and respiratory capacity; difficult IV access and regional blockade are common; regional anesthesia is preferred when feasible.",
        "rationale": "Obesity compounds pregnancy's anatomical and physiological stresses; careful positioning, airway planning, and dosing adjustments are essential.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 1425}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Obesity in obstetric anesthesia",
        "domain": "Obstetric anesthesia",
        "discipline": "anesthesia",
        "stem": "What drug dosing adjustments are necessary in obese pregnant patients for induction agents and local anesthetics?",
        "answer": "Induction agents (propofol, etomidate) may require reduced dosing based on lean body weight; local anesthetic doses should not exceed maximum recommendations despite increased volume of distribution.",
        "rationale": "Altered pharmacokinetics in obesity affect drug distribution and clearance; lean-body-weight dosing prevents overdosing and toxicity.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 1425}],
        "confusable_with": ""
    }
])

# Topic 806: Obstetric Pain Management
slug = "obstetric-pain-management"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Obstetric Pain Management",
        "domain": "Obstetric anesthesia",
        "discipline": "anesthesia",
        "stem": "What are the nonpharmacological and pharmacological approaches to labor pain management?",
        "answer": "Nonpharmacological: continuous labor support, position changes, ambulation, breathing techniques; pharmacological: parenteral opioids, nitrous oxide, regional anesthesia (epidural, spinal, combined), and paracervical blocks.",
        "rationale": "Multimodal analgesia maximizes maternal comfort while minimizing fetal exposure to single agents; epidural provides superior pain relief with minimal fetal effects.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 1451}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Obstetric Pain Management",
        "domain": "Obstetric anesthesia",
        "discipline": "anesthesia",
        "stem": "What are the contraindications and complications of epidural analgesia in labor?",
        "answer": "Contraindications: maternal refusal, coagulopathy, spinal infection, aortic/mitral stenosis; complications include hypotension (treat with fluids and vasopressors), high/total spinal, dural puncture, and rarely cauda equina.",
        "rationale": "Coagulopathy increases hematoma risk; aortic stenosis prevents compensation for epidural-induced vasodilation; maternal hypotension compromises uteroplacental perfusion.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 1451}],
        "confusable_with": ""
    }
])

# Topic 807: Obstetric hemorrhage
slug = "obstetric-hemorrhage-risk-factors-classification"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Obstetric hemorrhage: risk factors and classification",
        "domain": "Obstetric anesthesia",
        "discipline": "anesthesia",
        "stem": "What are the major risk factors for obstetric hemorrhage and how is severity classified?",
        "answer": "Risk factors: uterine atony, placental abruption, retained placenta, coagulopathy, cesarean delivery, multiple gestation; classified as primary (first 24 hours) or secondary (after 24 hours); blood loss >500 mL vaginal or >1000 mL cesarean is abnormal.",
        "rationale": "Early identification of risk and rapid intervention prevent progression to severe hemorrhage and disseminated intravascular coagulation.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 1481}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Obstetric hemorrhage: risk factors and classification",
        "domain": "Obstetric anesthesia",
        "discipline": "anesthesia",
        "stem": "What are the first-line interventions for uterine atony causing obstetric hemorrhage?",
        "answer": "Uterine massage, oxytocin (10 units IV or IM), methylergonovine (0.2 mg IM), and prostaglandins (misoprostol 1000 mcg rectal or carboprost 250 mcg IM); tranexamic acid reduces transfusion needs.",
        "rationale": "Uterotonic agents increase myometrial contraction, tamponading bleeding vessels; oxytocin is first-line due to safety; TXA addresses fibrinolysis.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 1481}],
        "confusable_with": ""
    }
])

# Topic 808: Obstructive sleep apnea
slug = "obstructive-sleep-apnea-perioperative-implications"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Obstructive sleep apnea (OSA) – perioperative implications",
        "domain": "Perioperative medicine",
        "discipline": "anesthesia",
        "stem": "What screening tools identify perioperative risk in sleep apnea patients and what are the physiological concerns?",
        "answer": "STOP-BANG questionnaire identifies high-risk patients; physiological concerns include airway collapse during sleep, intermittent hypoxemia, hypercarbia, pulmonary hypertension, and arrhythmias.",
        "rationale": "Patients with untreated OSA are at high risk for perioperative hypoxemia, difficult intubation, and hemodynamic instability; identification allows appropriate management.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 744}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Obstructive sleep apnea (OSA) – perioperative implications",
        "domain": "Perioperative medicine",
        "discipline": "anesthesia",
        "stem": "What perioperative management strategies reduce complications in patients with OSA?",
        "answer": "Avoid sedatives/opioids; use reduced anesthetic doses; continue CPAP perioperatively; use multimodal analgesia; avoid airway manipulation; maintain adequate oxygenation; monitor in high-acuity setting postoperatively.",
        "rationale": "Depressant drugs worsen airway collapse; CPAP maintains airway patency; multimodal analgesia reduces opioid exposure; postoperative monitoring detects apneic events.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 744}],
        "confusable_with": ""
    }
])

# Topic 809: Obturator and lateral femoral cutaneous nerve blocks
slug = "obturator-lateral-femoral-cutaneous-nerve-blocks"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Obturator and lateral femoral cutaneous nerve blocks",
        "domain": "Regional anesthesia",
        "discipline": "anesthesia",
        "stem": "What anatomical pathways and sensory distributions do the obturator and lateral femoral cutaneous nerves follow?",
        "answer": "Obturator nerve (L2-L4) innervates medial thigh and hip joint; lateral femoral cutaneous nerve (L2-L3) innervates lateral thigh; both originate from lumbar plexus.",
        "rationale": "Understanding anatomy guides block needle placement and predicts anesthetic coverage for surgery on medial/lateral thigh and hip.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 1204}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Obturator and lateral femoral cutaneous nerve blocks",
        "domain": "Regional anesthesia",
        "discipline": "anesthesia",
        "stem": "What are the indications and technique for obturator and lateral femoral cutaneous nerve blocks?",
        "answer": "Indications: medial thigh surgery, hip arthroscopy, adductor tenotomy; obturator block: landmark or ultrasound approach at inguinal crease; LFCN block at anterior superior iliac spine to block meralgia paresthetica.",
        "rationale": "These blocks supplement femoral nerve blockade for hip and thigh surgery; they reduce spasticity (obturator) and treat meralgia paresthetica (LFCN).",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 1204}],
        "confusable_with": ""
    }
])

# Topic 810: Oncology patients
slug = "oncology-patients-perioperative-management"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Oncology patients – perioperative management",
        "domain": "Perioperative medicine",
        "discipline": "anesthesia",
        "stem": "What are the major perioperative concerns in cancer patients undergoing surgery?",
        "answer": "Concerns include chemotherapy cardiotoxicity (anthracyclines, HER2 inhibitors), pulmonary toxicity (bleomycin), coagulopathy, cachexia, difficult airway, and potential for tumor seeding; assess functional status and organ involvement.",
        "rationale": "Prior cancer therapy causes organ-specific toxicity; understanding the chemotherapy history guides anesthetic selection and monitoring intensity.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 852}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Oncology patients – perioperative management",
        "domain": "Perioperative medicine",
        "discipline": "anesthesia",
        "stem": "What specific anesthetic strategies are recommended for cancer patients to minimize perioperative morbidity?",
        "answer": "Use goal-directed fluid therapy (avoid excess); regional anesthesia preferred; avoid volatile anesthetics with immunosuppressant properties; minimize transfusion; use antithrombotics perioperatively; monitor for sepsis and organ dysfunction.",
        "rationale": "Goal-directed fluid avoids pulmonary edema in those with chemotherapy cardiotoxicity; regional anesthesia avoids volatile-induced immunosuppression; cancer patients have elevated VTE risk.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 852}],
        "confusable_with": ""
    }
])

# Topic 811: Opioid Pharmacology
slug = "opioid-pharmacology"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Opioid Pharmacology",
        "domain": "General anesthesia",
        "discipline": "anesthesia",
        "stem": "What are the four main opioid receptor types and their functional roles in anesthesia?",
        "answer": "Mu (μ) receptors: analgesia, euphoria, respiratory depression; delta (δ): analgesia, mood; kappa (κ): analgesia, dysphoria; nociceptin (ORL-1): pain modulation; mu-mediated effects dominate clinical anesthesia.",
        "rationale": "Mu-opioid agonists provide analgesia and sedation; understanding receptor types explains why kappa agonists cause dysphoria and limit clinical use.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 218}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Opioid Pharmacology",
        "domain": "General anesthesia",
        "discipline": "anesthesia",
        "stem": "What is the context-sensitive half-time for common perioperative opioids and what does it mean clinically?",
        "answer": "Context-sensitive half-time is the time to 50% plasma reduction after stopping a continuous infusion; fentanyl ~30-40 min, morphine ~60 min, remifentanil <10 min; determines wake-up timing and postoperative opioid dosing.",
        "rationale": "Remifentanil's rapid metabolism allows quick emergence; fentanyl's longer half-time requires consideration of cumulative dosing and postoperative pain planning.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 218}],
        "confusable_with": ""
    }
])

# Topic 812: Opioid Pharmacology – Receptor Physiology
slug = "opioid-pharmacology-receptor-physiology"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Opioid Pharmacology – Receptor Physiology",
        "domain": "General anesthesia",
        "discipline": "anesthesia",
        "stem": "What is the mechanism of opioid receptor signaling and how do G-protein coupled receptors modulate pain pathways?",
        "answer": "Opioid receptors are GPCRs that open potassium channels (hyperpolarization) and inhibit adenylyl cyclase (reduce cAMP); this suppresses neurotransmitter release and neuronal excitability in pain pathways.",
        "rationale": "This mechanism underlies opioid analgesia and also respiratory depression (mu-2 receptors in brainstem respiratory centers); understanding it explains pharmacological effects.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 218}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Opioid Pharmacology – Receptor Physiology",
        "domain": "General anesthesia",
        "discipline": "anesthesia",
        "stem": "What is opioid tolerance and what are the mechanisms underlying tolerance development?",
        "answer": "Tolerance is reduced drug effect with continued use; mechanisms include receptor desensitization, downregulation, and shift from Gi to Gs coupling; upregulation of anti-opioid systems (neuropeptide Y, dynorphin).",
        "rationale": "Tolerance develops at different rates for different opioid effects (respiratory > analgesia); chronic users require dose escalation; understanding mechanisms guides OUD treatment.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 218}],
        "confusable_with": ""
    }
])

# Topic 813: Opioid Use Disorder
slug = "opioid-use-disorder-perioperative-management"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Opioid Use Disorder (OUD) – Perioperative Management",
        "domain": "Pain management",
        "discipline": "anesthesia",
        "stem": "What are the clinical features and diagnostic criteria for opioid use disorder?",
        "answer": "OUD involves 2+ DSM-5 criteria: tolerance, withdrawal, loss of control, continued use despite harm, social/occupational impairment; physical findings include track marks, nasal damage (intranasal use), poor dentition.",
        "rationale": "Recognizing OUD allows appropriate perioperative pain management and addiction treatment coordination; withholding opioids risks withdrawal and poor analgesia.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 1544}],
        "confusable_with": "Physical dependence (expected after chronic opioid use, not diagnostic of disorder)"
    },
    {
        "id": f"{slug}-2",
        "topic": "Opioid Use Disorder (OUD) – Perioperative Management",
        "domain": "Pain management",
        "discipline": "anesthesia",
        "stem": "What perioperative analgesia strategy is recommended for patients on medication-assisted treatment (methadone/buprenorphine)?",
        "answer": "Continue maintenance medications perioperatively; use multimodal analgesia (regional, NSAIDs, ketamine, gabapentinoids); do not abruptly discontinue methadone/buprenorphine; supplement with additional opioids if needed for acute pain.",
        "rationale": "Abrupt withdrawal causes severe symptoms; buprenorphine's partial agonism requires higher opioid doses; multimodal approach reduces withdrawal risk and opioid requirements.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 1544}],
        "confusable_with": ""
    }
])

# Topic 814: Opioid receptor pharmacology
slug = "opioid-receptor-pharmacology"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Opioid receptor pharmacology",
        "domain": "General anesthesia",
        "discipline": "anesthesia",
        "stem": "What is the concept of opioid-receptor selectivity and which perioperative opioids show high mu selectivity?",
        "answer": "Opioid selectivity reflects preferential binding to one receptor type (e.g., fentanyl mu > delta > kappa); high mu-selectivity correlates with potent analgesia and respiratory depression; sufentanil and remifentanil are highly selective mu agonists.",
        "rationale": "Selective mu agonists provide pure analgesic effects without dysphoria from kappa activation; selectivity affects side-effect profile.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 228}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Opioid receptor pharmacology",
        "domain": "General anesthesia",
        "discipline": "anesthesia",
        "stem": "What is the relationship between opioid potency, receptor affinity, and intrinsic activity?",
        "answer": "Potency relates to affinity (drug-receptor binding strength) and intrinsic activity (efficacy at binding); full agonists (morphine, fentanyl) have high intrinsic activity; partial agonists (buprenorphine) have reduced intrinsic activity.",
        "rationale": "Buprenorphine's partial agonism causes a plateau effect in respiratory depression, offering a safety advantage; understanding this guides opioid selection.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 228}],
        "confusable_with": ""
    }
])

# Topic 815: Opioid side effects & management
slug = "opioid-side-effects-management"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Opioid side effects & management",
        "domain": "Pain management",
        "discipline": "anesthesia",
        "stem": "What are the major opioid-related side effects in the perioperative period and how are they managed?",
        "answer": "Respiratory depression (reduce dose, supplemental O2, monitor respiratory rate); postoperative nausea/vomiting (5HT3 antagonists, NK1 antagonists, dexamethasone); pruritus (naloxone, diphenhydramine); urinary retention (catheter, try void); constipation (stool softeners, laxatives).",
        "rationale": "Opioid side effects limit patient comfort and increase complications; multimodal approaches reduce opioid requirements and side-effect incidence.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 252}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Opioid side effects & management",
        "domain": "Pain management",
        "discipline": "anesthesia",
        "stem": "What is opioid-induced hyperalgesia and how does it differ from tolerance?",
        "answer": "Opioid-induced hyperalgesia is paradoxical increased pain sensitivity with chronic high-dose opioids; differs from tolerance in that pain is heightened, not blunted; mechanism involves anti-opioid neuropeptides and NMDA activation.",
        "rationale": "OIH limits escalation of opioid dosing; recognition prompts opioid rotation, dose reduction, or multimodal therapy including ketamine (NMDA antagonist).",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 252}],
        "confusable_with": "Tolerance (reduced analgesic effect over time)"
    }
])

# Topic 816: Oxygen and Carbon Dioxide Transport
slug = "oxygen-carbon-dioxide-transport"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Oxygen and Carbon Dioxide Transport",
        "domain": "Respiratory physiology",
        "discipline": "anesthesia",
        "stem": "How is oxygen transported in the blood and what is the oxyhemoglobin dissociation curve?",
        "answer": "Oxygen binds hemoglobin (98.5% of blood O2) or dissolves in plasma (1.5%); the S-shaped dissociation curve shifts rightward with CO2, H+, temp, 2,3-DPG (Bohr effect), enhancing tissue O2 delivery.",
        "rationale": "Hemoglobin-oxygen binding is cooperative; shifts in the curve affect oxygen delivery during anesthesia and critical illness.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 614}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Oxygen and Carbon Dioxide Transport",
        "domain": "Respiratory physiology",
        "discipline": "anesthesia",
        "stem": "How is carbon dioxide transported and what is the relationship between CO2 and pH in the blood?",
        "answer": "CO2 is transported as dissolved CO2 (5%), bicarbonate (90%), and carbaminohemoglobin (5%); CO2 + H2O forms carbonic acid, buffered by bicarbonate system; elevated CO2 lowers pH (respiratory acidosis).",
        "rationale": "Understanding CO2 transport explains why hypercarbia (from inadequate ventilation) causes acidosis; this guides ventilator management during anesthesia.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 614}],
        "confusable_with": ""
    }
])

# Topic 817: Pacemakers
slug = "pacemakers-anesthetic-management"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Pacemakers – Anesthetic Management",
        "domain": "Perioperative medicine",
        "discipline": "anesthesia",
        "stem": "What are the preoperative considerations for patients with pacemakers or ICDs undergoing surgery?",
        "answer": "Obtain pacemaker identification and settings; cardiology clearance; determine if PPM-dependent; assess for recent reprogramming; plan intraoperative monitoring (ECG, pulse oximetry, capnography, arterial line if high-risk).",
        "rationale": "Pacemaker malfunction intraoperatively can cause asystole or dangerous arrhythmias; preoperative planning prevents catastrophic events.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 796}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Pacemakers – Anesthetic Management",
        "domain": "Perioperative medicine",
        "discipline": "anesthesia",
        "stem": "How do cautery (electrosurgery) and MRI affect pacemakers, and what intraoperative strategies mitigate risks?",
        "answer": "Cautery can inhibit or reprogram PPM; monopolar cautery is safer than bipolar; MRI is contraindicated in most PPMs unless device is MRI-conditional; use grounding pads away from device; use shortest bursts; monitor closely.",
        "rationale": "Electromagnetic interference from cautery and MRI can inhibit pacing or cause device malfunction; careful planning and technique prevent intraoperative complications.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 796}],
        "confusable_with": ""
    }
])

# Topic 818: Patient Autonomy & Advance Directives
slug = "patient-autonomy-advance-directives"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Patient Autonomy & Advance Directives",
        "domain": "Ethics and professionalism",
        "discipline": "anesthesia",
        "stem": "What are advance directives and living wills, and what is their role in perioperative decision-making?",
        "answer": "Advance directives document a patient's wishes for end-of-life care; living will specifies life-sustaining treatment preferences; durable power of attorney designates a surrogate; these guide intraoperative care and postoperative life support decisions.",
        "rationale": "Legal documents ensure patient autonomy in medical decisions; knowledge of patient values guides ethical decision-making in emergencies.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 1655}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Patient Autonomy & Advance Directives",
        "domain": "Ethics and professionalism",
        "discipline": "anesthesia",
        "stem": "What is the anesthesiologist's role in perioperative informed consent and what elements must be discussed?",
        "answer": "Obtain informed consent discussing: anesthetic plan, risks (allergic reaction, DVT, awareness, regional block complications), benefits, alternatives (general vs. regional vs. sedation), and answer patient questions.",
        "rationale": "Informed consent respects autonomy and provides legal protection; discussions must be documented and understandable to the patient.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 1655}],
        "confusable_with": ""
    }
])

# Topic 819: Patient Positioning for Neurosurgery
slug = "patient-positioning-for-neurosurgery"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Patient Positioning for Neurosurgery",
        "domain": "Neuroanesthesia",
        "discipline": "anesthesia",
        "stem": "What are the common surgical positions for neurosurgical procedures and what are the anatomical risks of each?",
        "answer": "Supine: minimal risk; prone: airway obstruction, brachial plexus stretch, head/cervical spine injury; sitting: venous air embolism, cardiovascular collapse; lateral: brachial plexus, shoulder dislocation; park-bench: nerve stretch injuries.",
        "rationale": "Each position provides surgical access but carries specific risks; understanding anatomy guides proper patient preparation and padding.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 944}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Patient Positioning for Neurosurgery",
        "domain": "Neuroanesthesia",
        "discipline": "anesthesia",
        "stem": "What preventive strategies reduce positioning-related peripheral nerve injuries and what is the role of neuromonitoring?",
        "answer": "Padding: bony prominences, axillae, elbows; limit neck rotation/flexion <30 degrees; avoid stretching arms >90 degrees; neuromonitoring (somatosensory evoked potentials, motor evoked potentials) detects nerve injury early.",
        "rationale": "Proper padding distributes pressure; limiting extremes of motion prevents stretch; neuromonitoring allows real-time detection and correction of nerve compromise.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 944}],
        "confusable_with": ""
    }
])

# Topic 820: Pediatric Neuroanesthesia
slug = "pediatric-neuroanesthesia"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Pediatric Neuroanesthesia",
        "domain": "Pediatric anesthesia",
        "discipline": "anesthesia",
        "stem": "What are the developmental and physiological differences in pediatric brains and how do they affect anesthetic management?",
        "answer": "Pediatric brains have higher metabolic rate, less myelination (lower seizure threshold), immature BBB (increased drug penetration), open fontanelles (reduced ICP cushioning); volatile agents carry higher seizure risk.",
        "rationale": "These differences require careful agent selection and dosing; understanding them guides perioperative monitoring and intervention.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 1083}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Pediatric Neuroanesthesia",
        "domain": "Pediatric anesthesia",
        "discipline": "anesthesia",
        "stem": "What special monitoring and airway management considerations apply to pediatric neurosurgical patients?",
        "answer": "Avoid hyperventilation (worsens cerebral ischemia); maintain normothermia; use IV access intraoperatively (potential massive hemorrhage); position carefully (avoid head compression); monitor neurofunction (motor/sensory evoked potentials); have emergency pediatric resuscitation protocols ready.",
        "rationale": "Pediatric neuro cases carry high hemorrhage risk; avoiding hyperventilation preserves cerebral perfusion; neuromonitoring prevents positioning injuries.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 1083}],
        "confusable_with": ""
    }
])

# Topic 821: Perioperative Myocardial Infarction
slug = "perioperative-myocardial-infarction-recognition-management"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Perioperative Myocardial Infarction – Recognition & Management",
        "domain": "Perioperative medicine",
        "discipline": "anesthesia",
        "stem": "What are the clinical presentation and diagnostic criteria for perioperative myocardial infarction?",
        "answer": "Perioperative MI occurs within 48-72 hours of surgery; presentation includes chest pain, ECG changes (ST elevation/depression, T-wave inversion), troponin elevation (peak 24-72 hours), hemodynamic changes (hypotension, arrhythmias).",
        "rationale": "Many perioperative MIs are silent (30-50%); high suspicion based on risk factors and troponin monitoring enables early intervention.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 722}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Perioperative Myocardial Infarction – Recognition & Management",
        "domain": "Perioperative medicine",
        "discipline": "anesthesia",
        "stem": "What perioperative strategies reduce myocardial infarction risk in high-risk cardiac patients?",
        "answer": "Continue beta-blockers perioperatively (avoid withdrawal); maintain normothermia (reduce tachycardia); use opioids and volatile agents (cardioprotection); aggressive pain management; goal-directed fluid therapy; postoperative troponin screening in high-risk patients.",
        "rationale": "Beta-blocker withdrawal increases MI risk; opioids and volatiles provide preconditioning; avoiding tachycardia and hypertension reduces myocardial oxygen demand.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 722}],
        "confusable_with": ""
    }
])

# Topic 822: Perioperative antibiotic prophylaxis
slug = "perioperative-antibiotic-prophylaxis"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Perioperative antibiotic prophylaxis",
        "domain": "Infection control",
        "discipline": "anesthesia",
        "stem": "What are the key principles of perioperative antibiotic prophylaxis?",
        "answer": "Prophylaxis should be given within 60 min of incision (120 min for vancomycin/clindamycin); chosen based on surgery type and local resistance patterns; redosed if procedure exceeds 2 half-lives; discontinued within 24 hours postop.",
        "rationale": "Timely prophylaxis achieves tissue concentrations above MIC at incision; excessive duration increases resistance and adverse effects without additional benefit.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 1585}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Perioperative antibiotic prophylaxis",
        "domain": "Infection control",
        "discipline": "anesthesia",
        "stem": "What antibiotic regimens are recommended for different surgery types and patient risk factors?",
        "answer": "Clean-contaminated (GI, biliary, gynecologic): cephalosporin or vancomycin; orthopedic: cephalosporin; cardiac: vancomycin/clindamycin; MRSA colonized: vancomycin; PCN-allergy: clindamycin or fluoroquinolone; adjust for renal/hepatic dysfunction.",
        "rationale": "Selection based on surgery-specific flora; allergy status and organ function guide choice; ensures adequate coverage without unnecessary broad-spectrum use.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 1585}],
        "confusable_with": ""
    }
])

# Topic 823: Perioperative anticoagulation management
slug = "perioperative-anticoagulation-management"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Perioperative anticoagulation management",
        "domain": "Perioperative medicine",
        "discipline": "anesthesia",
        "stem": "What is the perioperative management strategy for warfarin-anticoagulated patients?",
        "answer": "Continue warfarin if INR therapeutic and surgery high-bleeding risk (bridge with LMWH/UFH); hold warfarin 5 days preop for low-bleeding-risk surgery; periop INR goal 1.5-2.5; resume postop when bleeding risk allows.",
        "rationale": "Balancing thrombotic risk (from withholding anticoagulation) against bleeding risk (from continuing) requires individualized decisions based on surgery type and indication.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 783}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Perioperative anticoagulation management",
        "domain": "Perioperative medicine",
        "discipline": "anesthesia",
        "stem": "How should DOACs (direct oral anticoagulants) be managed perioperatively?",
        "answer": "Hold DOAC 24-48 hours preop (depending on agent and renal function); bleeding risk is high if DOAC continued; resume postop when hemostasis achieved (typically 24 hours); bridge with LMWH if VTE risk is high.",
        "rationale": "DOACs have short half-lives (12-24 hrs); holding before surgery reduces bleeding risk; early postop resumption prevents thromboembolism.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 783}],
        "confusable_with": ""
    }
])

# Topic 824: Perioperative glycemic management
slug = "perioperative-glycemic-management-targets-monitoring"
all_entries.extend([
    {
        "id": f"{slug}-1",
        "topic": "Perioperative glycemic management targets and monitoring",
        "domain": "Perioperative medicine",
        "discipline": "anesthesia",
        "stem": "What are the recommended blood glucose targets in the perioperative period and why is tight control important?",
        "answer": "Target glucose 140-180 mg/dL intraoperatively; <140 mg/dL increases hypoglycemia risk and perioperative morbidity (worsens outcomes); >250 mg/dL impairs immune function and increases infections; avoid hypoglycemia <70 mg/dL.",
        "rationale": "Insulin resistance increases with stress and anesthesia; tight control (80-110) increases hypoglycemia risk without mortality benefit; moderate targets balance glucose-related complications.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 641}],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": "Perioperative glycemic management targets and monitoring",
        "domain": "Perioperative medicine",
        "discipline": "anesthesia",
        "stem": "What insulin regimen is recommended for diabetic patients in the perioperative period?",
        "answer": "Hold oral hypoglycemics day of surgery; give half usual insulin dose if NPO; use IV insulin infusion (0.5-1 unit/kg/hr) intraoperatively with frequent glucose monitoring (q30-60 min); resume home regimen postop when eating.",
        "rationale": "NPO status reduces glucose needs; IV insulin allows rapid titration based on glucose; frequent monitoring prevents hypoglycemia and hyperglycemia.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 641}],
        "confusable_with": ""
    }
])

# Validate JSON
json_str = json.dumps(all_entries, ensure_ascii=False, indent=2)
json.loads(json_str)  # Raises error if invalid

print(f"Success: generated {len(all_entries)} KPs")

# Write output
with open('data/kp_full_part_24.json', 'w', encoding='utf-8') as f:
    json.dump(all_entries, f, ensure_ascii=False, indent=2)

print(f"Written to data/kp_full_part_24.json")
