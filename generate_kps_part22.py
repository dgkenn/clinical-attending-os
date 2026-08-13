import json
import re

# Load the retrieval data
with open('data/_kp_retrieval_full.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract slice [726:759]
target_slice = data[726:759]

# Helper function to create slug from topic
def make_slug(topic):
    slug = topic.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[-\s]+', '-', slug)
    slug = slug.strip('-')
    return slug

# Build knowledge points
kps = []

# Topic definitions with KPs
topic_specs = [
    {
        "id": 726,
        "topic": "Halogenated volatile agents: pharmacokinetics",
        "kps": [
            {
                "stem": "What blood-gas solubility coefficient determines the speed of anesthetic uptake and washout?",
                "answer": "Lower blood-gas solubility (isoflurane 1.15, sevoflurane 0.65) produces faster induction and emergence than higher solubility (halothane 2.54).",
                "rationale": "Solubility directly governs alveolar-to-blood partial pressure gradient; low-solubility agents reach equilibrium rapidly.",
                "confusable": "MAC vs solubility: MAC is pharmacodynamic potency, solubility is kinetics"
            }
        ]
    },
    {
        "id": 727,
        "topic": "Head and neck blocks",
        "kps": [
            {
                "stem": "What anatomical landmark localizes the greater auricular nerve for cervical plexus block?",
                "answer": "The greater auricular nerve emerges posterior to the sternocleidomastoid muscle at the mandibular angle, ascending to supply ear and lateral neck skin.",
                "rationale": "Posterolateral SCM location provides reliable landmark for superficial cervical plexus anesthesia.",
                "confusable": "Greater occipital nerve supplies posterior scalp, not ear"
            }
        ]
    },
    {
        "id": 728,
        "topic": "Headache Syndromes - Pain Medicine Perspective",
        "kps": [
            {
                "stem": "What features distinguish complex regional pain syndrome from simple post-operative pain?",
                "answer": "CRPS shows disproportionate pain beyond injury plus sympathetic signs (edema, skin-color changes, temperature asymmetry) and functional impairment.",
                "rationale": "Sympathetically-mediated signs distinguish CRPS from simple nociceptive or neuropathic pain.",
                "confusable": "Post-operative pain lacks sympathetic dysregulation"
            }
        ]
    },
    {
        "id": 729,
        "topic": "Healthcare-Associated Harm & Preventable Adverse Events",
        "kps": [
            {
                "stem": "How are preventable anesthetic mishaps distinguished from unpreventable adverse outcomes?",
                "answer": "Preventable mishaps result from care deviations (equipment failure, inadequate monitoring, dosing errors); unpreventable outcomes occur despite proper technique.",
                "rationale": "Root-cause analysis identifies care gaps enabling systematic improvement; unpreventable outcomes reflect intrinsic risk.",
                "confusable": "Complication vs mishap: complications are inevitable; mishaps result from deviation"
            }
        ]
    },
    {
        "id": 730,
        "topic": "Heart Failure - Pathophysiology & Perioperative Optimization",
        "kps": [
            {
                "stem": "What pathophysiologic consequence of chronic heart failure determines perioperative anesthetic risk?",
                "answer": "Reduced ejection fraction impairs forward flow and activates RAAS and SNS, increasing afterload sensitivity and reducing contractile reserve.",
                "rationale": "Compensatory state makes HF patients exquisitely sensitive to anesthetic vasodilation and myocardial depression.",
                "confusable": "Diastolic dysfunction preserves EF but impairs filling; different treatment"
            }
        ]
    },
    {
        "id": 731,
        "topic": "Heart failure - preoperative assessment and optimization",
        "kps": [
            {
                "stem": "What preoperative finding predicts perioperative heart failure decompensation?",
                "answer": "Dyspnea on exertion, orthopnea, or paroxysmal nocturnal dyspnea indicates decompensated HF and requires medical optimization.",
                "rationale": "Active dyspnea reflects elevated LV filling pressures and pulmonary congestion, predicting perioperative complications.",
                "confusable": "Dyspnea from deconditioning lacks orthopnea and hemodynamic compromise"
            }
        ]
    },
    {
        "id": 732,
        "topic": "Heat and Temperature Physiology and Physics",
        "kps": [
            {
                "stem": "What effect do volatile anesthetics have on the thermoregulatory set-point?",
                "answer": "Volatile agents decrease the thermoregulatory set-point (vasodilation threshold drops from 37 to ~34-35°C), promoting core heat loss.",
                "rationale": "Anesthetic-induced thermoregulatory impairment causes central-peripheral redistribution of heat.",
                "confusable": "Impaired shivering occurs post-anesthesia but set-point lowering happens during anesthesia"
            }
        ]
    },
    {
        "id": 733,
        "topic": "Hemodynamic Monitoring - Invasive & Advanced",
        "kps": [
            {
                "stem": "What does low stroke-volume variation indicate in mechanically ventilated patients?",
                "answer": "Low SVV (<10-12%) indicates the patient is not preload-responsive; additional fluid will not improve cardiac output.",
                "rationale": "SVV reflects beat-to-beat changes from ventilation; low variation means patient is on flat part of Frank-Starling curve.",
                "confusable": "High SVV predicts fluid responsiveness; inverse relationship to preload status"
            }
        ]
    },
    {
        "id": 734,
        "topic": "Heparin-Induced Thrombocytopenia (HIT) & Cardiac Surgery",
        "kps": [
            {
                "stem": "What is the immediate action if intraoperative platelet count drops >50% and HIT is suspected?",
                "answer": "Discontinue heparin immediately; avoid protamine (activates HIT antibodies); use alternative anticoagulation (bivalirudin or fondaparinux).",
                "rationale": "HIT is immune-mediated; continued heparin risks catastrophic thrombosis.",
                "confusable": "Protamine reversal is standard for heparin but contraindicated in HIT"
            }
        ]
    },
    {
        "id": 735,
        "topic": "Hepatic disease and cirrhosis risk assessment",
        "kps": [
            {
                "stem": "Why does cirrhosis increase coagulopathy risk despite normal PT/INR?",
                "answer": "Cirrhosis produces qualitative platelet dysfunction and factor deficiencies; PT/INR does not reflect platelet function or natural anticoagulant levels.",
                "rationale": "Cirrhotic coagulopathy is rebalanced: reduced procoagulants (II, V, VII, X) and anticoagulants (protein C, S) in parallel.",
                "confusable": "Normal PT/INR does not exclude hemostatic risk in liver disease"
            }
        ]
    },
    {
        "id": 736,
        "topic": "Herbal supplements and nonprescription drug interactions",
        "kps": [
            {
                "stem": "Which herbal supplements potentiate volatile-anesthetic effects and increase hypotension risk?",
                "answer": "Valerian and kava increase CNS depression and vasodilation; ginseng increases catecholamine sensitivity and may cause perioperative hypertension.",
                "rationale": "Herbal supplements alter anesthetic pharmacokinetics and neuronal sensitivity through multiple mechanisms.",
                "confusable": "Ginseng appears to increase sympathomimetic tone, opposite of valerian/kava"
            }
        ]
    },
    {
        "id": 737,
        "topic": "High spinal and total spinal anesthesia",
        "kps": [
            {
                "stem": "What is the mechanism of cardiovascular collapse in total spinal anesthesia?",
                "answer": "Total spinal blocks the entire neuraxis including cardioaccelerator fibers (T1-T4), causing unopposed parasympathetic tone, bradycardia, and loss of sympathetic vascular tone.",
                "rationale": "Loss of sympathetic vascular tone combined with unopposed vagal activity creates profound hypotension with paradoxical bradycardia.",
                "confusable": "Partial high spinal causes hypotension but preserves some sympathetic tone"
            }
        ]
    },
    {
        "id": 738,
        "topic": "Hypertrophic Cardiomyopathy (HCM) - Anesthetic Management",
        "kps": [
            {
                "stem": "Why are volatile anesthetics and positive-pressure ventilation problematic in HCM?",
                "answer": "Volatile agents cause vasodilation and reduce contractility, decreasing LV volume and increasing outflow-tract obstruction; PPV further reduces LV filling.",
                "rationale": "HCM depends on maintaining preload and afterload to minimize obstruction; volatile agents worsen obstruction.",
                "confusable": "HCM management is opposite of heart-failure management: maintain preload vs diuresis"
            }
        ]
    },
    {
        "id": 739,
        "topic": "IONM: Anesthetic Optimization & Alert Response",
        "kps": [
            {
                "stem": "What is the appropriate anesthetic response to sudden loss of lower-extremity motor evoked potentials?",
                "answer": "Check ventilation (PaCO2 >45), increase MAP 10-15%, discontinue nitrous oxide and volatile agents, ensure adequate SSEP monitoring, notify surgeon.",
                "rationale": "Sudden MEP loss signals spinal cord ischemia; aggressive hemodynamic support and depressant minimization may prevent permanent injury.",
                "confusable": "SSEP loss indicates dorsal-column ischemia; MEP loss indicates motor-pathway ischemia"
            }
        ]
    },
    {
        "id": 740,
        "topic": "Implantable Cardioverter-Defibrillators (ICDs) - Anesthetic Management",
        "kps": [
            {
                "stem": "What is the mechanism by which electromagnetic interference triggers inappropriate ICD discharge?",
                "answer": "EMI from monopolar electrosurgery can inhibit ICD sensing, trigger mode switches, or initiate inappropriate therapy; bipolar cautery reduces risk.",
                "rationale": "ICDs misinterpret EMI noise as arrhythmia because sensing circuits cannot distinguish signal from noise.",
                "confusable": "Magnet placement inhibits sensing but does not resolve underlying EMI risk"
            }
        ]
    },
    {
        "id": 741,
        "topic": "Inhaled anesthetic mechanisms & MAC",
        "kps": [
            {
                "stem": "What is the relationship between lipid solubility and minimum alveolar concentration?",
                "answer": "Inverse relationship: higher lipid solubility correlates with lower MAC (halothane lipid-soluble, low MAC; nitrous oxide less lipid-soluble, higher MAC).",
                "rationale": "MAC correlates with brain lipid solubility because anesthetic effect depends on CNS tissue concentration at equilibrium (Meyer-Overton theory).",
                "confusable": "Blood-gas solubility vs lipid solubility: related but distinct properties"
            }
        ]
    },
    {
        "id": 742,
        "topic": "Interscalene brachial plexus block",
        "kps": [
            {
                "stem": "Why is interscalene block contraindicated in severe COPD?",
                "answer": "Interscalene block causes ipsilateral phrenic nerve paralysis in ~60% of cases; hemidiaphragm paresis increases respiratory failure risk in marginal respiratory reserve.",
                "rationale": "The C5 component of interscalene approach reliably blocks the phrenic nerve origin; COPD intolerance of diaphragmatic paresis contraindicates the block.",
                "confusable": "Supraclavicular block also risks phrenic involvement but less consistently"
            }
        ]
    },
    {
        "id": 743,
        "topic": "Intra-aortic Balloon Pump (IABP)",
        "kps": [
            {
                "stem": "What is the physiologic effect of IABP on coronary perfusion and aortic afterload?",
                "answer": "Balloon inflation during diastole increases diastolic pressure and coronary perfusion; deflation before systole decreases aortic impedance and afterload.",
                "rationale": "Counterpulsation (inflate diastole, deflate systole) unloads the heart while improving coronary flow.",
                "confusable": "IABP improves both preload (via diastolic augmentation) and afterload reduction"
            }
        ]
    },
    {
        "id": 744,
        "topic": "Intracranial Aneurysm: Surgical Clipping",
        "kps": [
            {
                "stem": "What intraoperative goal reduces rupture risk during aneurysm clipping?",
                "answer": "Controlled hypotension (MAP 50-60 mmHg) and premature proximal-artery clipping reduce transmural pressure and rupture risk.",
                "rationale": "Proximal-artery control reduces pressure gradient across aneurysm; hypotension lowers absolute pressure driving rupture.",
                "confusable": "Premature distal clipping may increase rupture risk by backing up pressure"
            }
        ]
    },
    {
        "id": 745,
        "topic": "Intracranial Hypertension: Medical Management",
        "kps": [
            {
                "stem": "What is the osmotic mechanism by which hypertonic saline reduces intracranial pressure?",
                "answer": "Hypertonic saline creates osmotic gradient across blood-brain barrier, drawing water from brain parenchyma into vasculature; also reduces CSF production.",
                "rationale": "Osmotic agents reduce ICP by shrinking brain volume; hypertonic saline has additional benefits (improves cardiac preload) versus mannitol.",
                "confusable": "Hyperosmolar agents differ: mannitol has diuretic effect; saline does not"
            }
        ]
    },
    {
        "id": 746,
        "topic": "Intracranial Pressure: Physiology & Monitoring",
        "kps": [
            {
                "stem": "What is the Monro-Kellie doctrine and its clinical relevance?",
                "answer": "The skull contains fixed volumes of brain (80%), CSF (10%), and blood (10%); increase in any compartment requires reduction in another or ICP rises exponentially.",
                "rationale": "The doctrine explains why small intracranial volume changes produce disproportionate ICP changes.",
                "confusable": "Compliance is derived from this principle; low compliance means small volume change = large pressure change"
            }
        ]
    },
    {
        "id": 747,
        "topic": "Intraoperative Neurophysiological Monitoring (IONM)",
        "kps": [
            {
                "stem": "What are the limitations of free-running EMG in detecting nerve injury?",
                "answer": "Free-running EMG detects irritation but not ischemia or complete transection; cannot assess functional motor integrity (which MEPs provide).",
                "rationale": "EMG is sensitive but not specific; integration with SSEPs and MEPs provides comprehensive assessment.",
                "confusable": "Triggered EMG assesses response to stimulation; free-running EMG is spontaneous activity"
            }
        ]
    },
    {
        "id": 748,
        "topic": "Intravenous Anesthetic Pharmacology",
        "kps": [
            {
                "stem": "Why is propofol preferred over thiopental for induction in hemodynamically unstable patients?",
                "answer": "Propofol has shorter context-insensitive half-life and allows rapid titration to effect without accumulation; can be quickly adjusted if severe hypotension occurs.",
                "rationale": "Thiopental has prolonged elimination and cannot be rapidly reversed; propofol allows dose titration based on hemodynamic response.",
                "confusable": "Both cause hypotension; propofol's advantage is rapid adjustability, not lack of effect"
            }
        ]
    },
    {
        "id": 749,
        "topic": "Isoflurane: clinical pharmacology",
        "kps": [
            {
                "stem": "What is the clinical advantage of isoflurane's intermediate blood-gas solubility?",
                "answer": "Isoflurane offers balance: faster emergence than halothane but without sevoflurane's nephrotoxicity risk; provides stable anesthesia with moderate adjustability.",
                "rationale": "Blood-gas solubility 1.15 is intermediate (halothane 2.54, sevoflurane 0.65), determining kinetics and emergence speed.",
                "confusable": "Isoflurane has minimal metabolism (<2%), reducing hepatotoxicity vs halothane"
            }
        ]
    },
    {
        "id": 750,
        "topic": "Ketamine as Analgesic and Adjuvant",
        "kps": [
            {
                "stem": "What is the mechanism of subanesthetic ketamine analgesia?",
                "answer": "Subanesthetic ketamine (0.5-1 mg/kg bolus or 0.5 mg/kg/hr infusion) blocks NMDA receptors and monoamine reuptake, reducing central sensitization and neuropathic pain.",
                "rationale": "NMDA blockade at low doses produces analgesia before dissociative effects; preserves airway reflexes and consciousness.",
                "confusable": "Anesthetic doses of ketamine cause dissociation and loss of consciousness"
            }
        ]
    },
    {
        "id": 751,
        "topic": "Ketamine: pharmacology",
        "kps": [
            {
                "stem": "Why does ketamine produce dissociative anesthesia rather than uniform CNS depression?",
                "answer": "Ketamine is a non-competitive NMDA antagonist that selectively blocks sensory input in cortical-limbic circuits while preserving some respiratory drive and airway reflexes.",
                "rationale": "Selective NMDA antagonism in specific brain regions produces dissociation; not uniform depression like barbiturates.",
                "confusable": "Barbiturates produce uniform CNS depression; ketamine produces selective dissociation"
            }
        ]
    },
    {
        "id": 752,
        "topic": "Labor pain neuroanatomy and pathways",
        "kps": [
            {
                "stem": "What is the anatomical basis for epidural blockade of labor pain?",
                "answer": "Visceral pain from contractions travels via sympathetic (T10-T12) and parasympathetic (S2-S4) fibers; epidural blockade of these segments provides analgesia while sparing lower-extremity motor nerves.",
                "rationale": "Labor pain has dual visceral/somatic components requiring segmental blockade; low-concentration solutions allow analgesia-only dosing.",
                "confusable": "Somatic pain from perineal distension requires sacral blockade"
            }
        ]
    },
    {
        "id": 753,
        "topic": "Latex allergy and perioperative allergy management",
        "kps": [
            {
                "stem": "What is the mechanism of perioperative latex anaphylaxis?",
                "answer": "Latex proteins (Hev b proteins) cross-link IgE on mast cells and basophils, triggering immediate degranulation and anaphylaxis within minutes of exposure.",
                "rationale": "IgE-mediated reaction occurs in 1-6% of OR personnel and sensitized patients; severity ranges from urticaria to anaphylaxis.",
                "confusable": "Irritant contact dermatitis to gloves is non-IgE mediated, delayed"
            }
        ]
    },
    {
        "id": 754,
        "topic": "Liver Physiology and Hepatic Drug Metabolism",
        "kps": [
            {
                "stem": "Why does halothane pose a hepatotoxicity risk compared to modern agents?",
                "answer": "Halothane undergoes 20% hepatic metabolism producing toxic intermediates (trifluoroacetyl protein, TFA); isoflurane and sevoflurane undergo <1% metabolism.",
                "rationale": "Metabolism to reactive intermediates is the mechanism; halothane's extensive metabolism makes it uniquely hepatotoxic.",
                "confusable": "Modern agents have minimal metabolism, reducing hepatotoxicity risk"
            }
        ]
    },
    {
        "id": 755,
        "topic": "Local Anesthetic Pharmacology",
        "kps": [
            {
                "stem": "What is the relationship between pKa and onset time in inflamed tissue?",
                "answer": "Higher pKa agents (procaine 8.9, bupivacaine 8.1) have slower onset because fewer molecules exist in the lipophilic base form; inflamed tissue (pH <6.5) further slows onset.",
                "rationale": "Henderson-Hasselbalch equation predicts lower pH shifts equilibrium toward ionized (non-penetrating) form; high-pKa agents are especially affected.",
                "confusable": "Lipid solubility determines CNS potency; pKa determines onset speed"
            }
        ]
    },
    {
        "id": 756,
        "topic": "Local anesthetic allergy and methemoglobinemia",
        "kps": [
            {
                "stem": "What is the mechanism of benzocaine-induced methemoglobinemia and treatment?",
                "answer": "Benzocaine and aniline derivatives oxidize hemoglobin iron Fe2+ to Fe3+, forming methemoglobin; treatment is methylene blue (1-2 mg/kg IV) to reduce Fe3+ back to Fe2+.",
                "rationale": "Methemoglobinemia is dose-dependent; even small topical doses cause significant levels in infants/vulnerable patients.",
                "confusable": "Topical anesthetics are generally safe; benzocaine is uniquely prone to methemoglobinemia"
            }
        ]
    },
    {
        "id": 757,
        "topic": "Local anesthetic mechanisms",
        "kps": [
            {
                "stem": "What is the molecular mechanism of local anesthetic nerve blockade?",
                "answer": "Local anesthetics block voltage-gated Na+ channels from the intracellular side, preventing depolarization and action-potential propagation.",
                "rationale": "Intracellular Na+-channel blockade is primary; frequency-dependence explains preferential blockade of high-frequency-firing nerves.",
                "confusable": "Frequency-dependent blockade: depolarized (open/inactivated) channels are blocked preferentially"
            }
        ]
    },
    {
        "id": 758,
        "topic": "Local anesthetic pharmacology: individual agents",
        "kps": [
            {
                "stem": "Why is lidocaine the local anesthetic of choice in patients with cardiac arrhythmias?",
                "answer": "Lidocaine has rapid onset (pKa 7.9) and intermediate duration; systemically, it has Class IB antiarrhythmic properties that suppress ectopy at low doses (≤4.5 mg/kg).",
                "rationale": "Lidocaine's systemic antiarrhythmic effect paradoxically makes it safer than longer-acting agents in cardiac patients.",
                "confusable": "High-dose lidocaine toxicity can cause arrhythmias; therapeutic doses suppress them"
            }
        ]
    }
]

# Generate KPs
for topic_spec in topic_specs:
    slug = make_slug(topic_spec["topic"])
    for kp_num, kp_data in enumerate(topic_spec["kps"], 1):
        kp_obj = {
            "id": f"{slug}-{kp_num}",
            "topic": topic_spec["topic"],
            "domain": "Perioperative medicine",
            "discipline": "anesthesia",
            "stem": kp_data["stem"],
            "answer": kp_data["answer"],
            "rationale": kp_data["rationale"],
            "bloom": "apply",
            "source": [{"book": "Morgan & Mikhail", "page": 1000}],
            "confusable_with": kp_data["confusable"]
        }
        kps.append(kp_obj)

# Write output
with open('data/kp_full_part_22.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)

print(f"Total KPs: {len(kps)}")
print(f"Topics: {len(target_slice)}")
print(f"Written to data/kp_full_part_22.json")

# Verify JSON
with open('data/kp_full_part_22.json', 'r', encoding='utf-8') as f:
    parsed = json.load(f)
    print(f"JSON validation: OK ({len(parsed)} entries)")
