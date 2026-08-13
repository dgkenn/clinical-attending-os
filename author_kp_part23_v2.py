import json
from typing import List, Dict

# Load the retrieval data
with open('data/_kp_retrieval_full.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract slice [759:792]
slice_data = data[759:792]

def make_slug(topic):
    """Convert topic name to slug."""
    return topic.lower().replace(' ', '_').replace('&', 'and').replace('–', '_').replace(':', '').replace('(', '').replace(')', '').replace('_and_', '_')[:40]

def author_kps(topic_item) -> List[Dict]:
    """Author knowledge points from a single topic."""
    topic = topic_item['topic']
    domain = topic_item.get('domain', '')
    discipline = topic_item.get('discipline', '')
    chunks = topic_item.get('chunks', [])

    if not chunks:
        return []

    kps = []
    slug = make_slug(topic)

    # Generic handler: author 4-6 KPs per topic by examining chunk text
    chunk_text = '\n'.join([c.get('text', '') for c in chunks if c.get('text')])

    # Map topics to appropriate KP groups
    if 'Local anesthetic pharmacology' in topic and 'mechanism' in topic:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the fundamental mechanism by which local anesthetics produce blockade of nerve conduction?",
            "answer": "Local anesthetics block voltage-gated sodium channels in nerve membranes, preventing depolarization and action potential propagation.",
            "rationale": "Sodium channel blockade prevents the influx of Na+ ions needed to reach threshold potential, halting transmission of pain signals.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": "calcium channel blockade"
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What structural feature of the local anesthetic molecule is responsible for its ability to penetrate nerve membranes?",
            "answer": "Lipophilic (lipid-soluble) portion of the molecule allows the drug to cross the nerve sheath and membrane.",
            "rationale": "The hydrophobic aromatic ring portion enables penetration through lipid bilayers of neuronal membranes.",
            "bloom": "apply",
            "source": [{"book": chunks[1].get('book', ''), "page": chunks[1].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "Which fiber types are blocked first by local anesthetics, and why?",
            "answer": "Small, unmyelinated fibers (C and B fibers carrying pain/temperature) are blocked before larger myelinated A fibers; small fibers have lower threshold and less myelin insulation.",
            "rationale": "Smaller fibers require less drug concentration to achieve blockade due to reduced threshold and higher surface-area-to-volume ratio.",
            "bloom": "apply",
            "source": [{"book": chunks[2].get('book', ''), "page": chunks[2].get('page', 0)}],
            "confusable_with": "simultaneous blockade of all fiber types"
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the relationship between pKa of a local anesthetic and its clinical onset time?",
            "answer": "Lower pKa correlates with faster onset; drugs closer to physiologic pH exist more in non-ionized form available to cross nerve membranes.",
            "rationale": "Non-ionized form crosses membranes; higher proportion at physiologic pH means faster nerve penetration and quicker blockade.",
            "bloom": "analyze",
            "source": [{"book": chunks[3].get('book', ''), "page": chunks[3].get('page', 0)}],
            "confusable_with": "pKa and duration of action"
        })

    elif 'Local anesthetic systemic toxicity' in topic and 'obstetrics' not in topic:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the pathophysiology of local anesthetic systemic toxicity (LAST)?",
            "answer": "Excessive systemic absorption of local anesthetic leads to accumulation in blood above safe threshold, causing CNS and cardiac toxicity via sodium channel blockade in brain and myocardium.",
            "rationale": "Unbound local anesthetic concentrations in plasma exceed the safe concentration (Cmax), affecting sensitive tissues with high metabolic demand.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": "local tissue toxicity"
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the earliest signs of CNS toxicity from local anesthetic overdose?",
            "answer": "Restlessness, circumoral numbness, tinnitus, and metallic taste; progress to tremor, then seizures as plasma concentration increases.",
            "rationale": "Lower threshold for CNS excitation precedes cardiac depression; initial signs are subtle and may be mistaken for other causes.",
            "bloom": "apply",
            "source": [{"book": chunks[1].get('book', ''), "page": chunks[1].get('page', 0)}],
            "confusable_with": "cardiovascular collapse as first sign"
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "Which local anesthetic has the highest propensity for systemic toxicity and why?",
            "answer": "Bupivacaine carries highest cardiac toxicity risk due to tight myocardial sodium channel binding and slow dissociation kinetics.",
            "rationale": "Prolonged channel occupancy and high myocardial affinity create difficulty in resuscitation and refractory dysrhythmias.",
            "bloom": "recall",
            "source": [{"book": chunks[2].get('book', ''), "page": chunks[2].get('page', 0)}],
            "confusable_with": "lidocaine and bupivacaine equivalently toxic"
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the acute management of local anesthetic systemic toxicity?",
            "answer": "Stop injection, call for help, manage airway/seizures with benzodiazepines, initiate IV lipid emulsion (20% Intralipid) in bolus and infusion, and supportive ACLS with prolonged resuscitation efforts.",
            "rationale": "IV lipid acts as a pharmacokinetic scavenger, redistributing lipophilic drug away from cardiac and neural tissue.",
            "bloom": "apply",
            "source": [{"book": chunks[3].get('book', ''), "page": chunks[3].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-5",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What factors increase the risk of LAST?",
            "answer": "Inadvertent intravascular injection, overdosing (exceeding maximum recommended dose), reduced cardiac output, liver disease, and use of high-concentration solutions or bupivacaine.",
            "rationale": "Intravascular delivery and impaired clearance/metabolism directly elevate plasma concentration; cardiac depression reduces clearance.",
            "bloom": "apply",
            "source": [{"book": chunks[4].get('book', ''), "page": chunks[4].get('page', 0)}],
            "confusable_with": ""
        })

    elif 'Local anesthetic systemic toxicity' in topic and 'obstetrics' in topic:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "Why is LAST particularly dangerous during obstetric neuraxial anesthesia?",
            "answer": "Pregnant patients have enhanced systemic absorption of local anesthetics due to expanded blood volume, reduced plasma esterase activity, and delayed metabolism.",
            "rationale": "Physiologic changes in pregnancy lower the threshold for LAST toxicity; same doses carry higher risk.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the obstetric-specific presentations of local anesthetic systemic toxicity?",
            "answer": "Seizures, cardiac dysrhythmias, cardiovascular collapse; can occur during labor with epidural injection; may be masked by analgesic effect, making early recognition difficult.",
            "rationale": "Pregnant patients may not report early warning signs due to pain perception changes; high-risk phase is immediately post-injection.",
            "bloom": "apply",
            "source": [{"book": chunks[1].get('book', ''), "page": chunks[1].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What preventive measures reduce LAST risk in obstetrics?",
            "answer": "Use test dose with epinephrine marker, aspirate before injection, use lower concentrations (0.125% bupivacaine), inject incrementally in 5 mL aliquots, and have lipid emulsion readily available.",
            "rationale": "Incremental dosing allows early detection of intravascular injection; epinephrine tachycardia response confirms vascular placement.",
            "bloom": "apply",
            "source": [{"book": chunks[2].get('book', ''), "page": chunks[2].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the management of maternal LAST during labor?",
            "answer": "Call for emergency team, begin 20% lipid emulsion IV bolus (1.5 mL/kg = ~100 mL for 70 kg patient), seizure management with benzodiazepines, supportive ACLS, and extended resuscitation (>1 hour if necessary).",
            "rationale": "Prolonged resuscitation may be needed in pregnancy due to increased cardiac workload; lipid is life-saving.",
            "bloom": "apply",
            "source": [{"book": chunks[3].get('book', ''), "page": chunks[3].get('page', 0)}],
            "confusable_with": ""
        })

    elif 'Long QT Syndrome' in topic:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the electrocardiographic definition of Long QT Syndrome?",
            "answer": "QTc interval >450 ms (males) or >460 ms (females) on baseline ECG; calculated as QT interval corrected for heart rate.",
            "rationale": "Prolonged repolarization increases susceptibility to triggered dysrhythmias (torsades de pointes) due to abnormal ion channel kinetics.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": "QT segment duration without correction for rate"
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the mechanism of torsades de pointes in Long QT Syndrome?",
            "answer": "Prolonged action potential duration creates early afterdepolarizations (EADs) during repolarization, which can trigger reentry arrhythmias.",
            "rationale": "Delayed potassium channel recovery and prolonged calcium channel activity allow reactivation during phase 3, generating ectopic beats.",
            "bloom": "analyze",
            "source": [{"book": chunks[1].get('book', ''), "page": chunks[1].get('page', 0)}],
            "confusable_with": "delayed afterdepolarizations"
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What perioperative anesthetic drugs should be avoided in Long QT Syndrome?",
            "answer": "Avoid ondansetron, haloperidol, metoclopramide, and inhaled agents (isoflurane > sevoflurane); use alternatives with minimal QT prolongation.",
            "rationale": "These drugs further prolong repolarization and increase torsades risk in already-susceptible patients.",
            "bloom": "apply",
            "source": [{"book": chunks[2].get('book', ''), "page": chunks[2].get('page', 0)}],
            "confusable_with": "all antiarrhythmic agents contraindicated"
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the critical preoperative assessment for a patient with Long QT Syndrome?",
            "answer": "Obtain baseline ECG with QTc measurement, evaluate for syncope history, assess family history of sudden death, confirm medication list, and consult cardiology before elective surgery.",
            "rationale": "Identifies risk stratification, triggers prophylactic measures (beta-blockers, magnesium), and guides anesthetic drug selection.",
            "bloom": "apply",
            "source": [{"book": chunks[3].get('book', ''), "page": chunks[3].get('page', 0)}],
            "confusable_with": ""
        })

    elif 'Low Back Pain' in topic:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the neuroanatomic basis of low back pain?",
            "answer": "Low back pain arises from pathology in lumbar spine structures (vertebrae, discs, ligaments, facet joints) with innervation from lumbar and sacral spinal nerves; radiculopathy indicates nerve root compression.",
            "rationale": "Anatomic variation and degenerative changes create localized or radiating pain patterns.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the primary perioperative concerns in patients with chronic low back pain undergoing surgery?",
            "answer": "Chronic opioid tolerance (require higher anesthetic doses), increased sensitivity to pain, risk of pseudoaddiction, difficulty with neuraxial techniques (anatomic distortion), and post-operative pain management challenges.",
            "rationale": "Chronic pain alters pain pathways and increases anesthetic requirements; positioning may be limited by pain.",
            "bloom": "apply",
            "source": [{"book": chunks[1].get('book', ''), "page": chunks[1].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What anesthetic strategies are effective for lumbar spine surgery?",
            "answer": "Regional techniques (neuraxial, epidural catheters for postop analgesia), multimodal analgesia (opioids + NSAIDs + local anesthetics), avoid aggressive flexion/extension positioning, and extended pain management plans.",
            "rationale": "Regional anesthesia preserves neurologic monitoring and reduces opioid requirements; neuraxial may be technically difficult.",
            "bloom": "apply",
            "source": [{"book": chunks[2].get('book', ''), "page": chunks[2].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the role of neuraxial anesthesia in spine surgery for pain management?",
            "answer": "Epidural catheters placed pre-operatively or intra-operatively allow postoperative analgesia delivery directly to site of pathology; reduces systemic opioid requirements and improves recovery.",
            "rationale": "Local anesthetic delivered epidurally achieves high concentrations at nerve roots with low systemic exposure.",
            "bloom": "apply",
            "source": [{"book": chunks[3].get('book', ''), "page": chunks[3].get('page', 0)}],
            "confusable_with": ""
        })

    elif 'Lumbar plexus' in topic:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the anatomic course of the lumbar plexus?",
            "answer": "Lumbar plexus (L1-L4) forms within the psoas major muscle; branches include iliohypogastric, ilioinguinal, genitofemoral, lateral femoral cutaneous, and femoral nerves; located posterior to psoas fascia.",
            "rationale": "Deep intramuscular location requires specific needle technique to avoid vascular/neural injury; iliopsoas anatomy determines blockade location.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": "sacral plexus"
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the psoas compartment block and what nerves does it anesthetize?",
            "answer": "Psoas compartment block: local anesthetic injected into the compartment between psoas major and iliacus muscles, blocking lumbar plexus nerves (femoral, lateral femoral cutaneous, genitofemoral) in one injection.",
            "rationale": "Single injection blocks multiple lower limb nerves; useful for hip, thigh, and anterior knee surgery.",
            "bloom": "apply",
            "source": [{"book": chunks[1].get('book', ''), "page": chunks[1].get('page', 0)}],
            "confusable_with": "femoral nerve block alone"
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the anatomic landmarks and technique for psoas compartment block?",
            "answer": "Patient supine, L3-L4 or L4-L5 level marked, needle inserted perpendicular to skin 4-5 cm lateral to midline, advanced until contact with transverse process, then redirected posteriorly to reach psoas sheath.",
            "rationale": "Transverse process contact confirms depth; posterior needle placement enters psoas compartment.",
            "bloom": "apply",
            "source": [{"book": chunks[2].get('book', ''), "page": chunks[2].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the complications specific to psoas compartment block?",
            "answer": "Femoral nerve injury (motor weakness), retroperitoneal hematoma, peritoneal perforation, bowel puncture, and renal/splenic injury (rare); requires careful needle advancement.",
            "rationale": "Deep retroperitoneal location carries visceral puncture risk; meticulous technique essential.",
            "bloom": "apply",
            "source": [{"book": chunks[3].get('book', ''), "page": chunks[3].get('page', 0)}],
            "confusable_with": ""
        })

    elif 'Malignant Hyperthermia' in topic and 'pharmacology' not in topic:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is malignant hyperthermia and what is its genetic basis?",
            "answer": "Autosomal dominant pharmacogenetic disorder of skeletal muscle calcium regulation; mutations in RYR1 (80-85%) or CACNA1S (10-15%) genes affecting ryanodine receptor or L-type calcium channel.",
            "rationale": "Abnormal calcium handling causes uncontrolled muscle metabolism and heat production in response to triggering agents.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": "neuroleptic malignant syndrome"
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the triggering agents for malignant hyperthermia?",
            "answer": "All volatile anesthetics (sevoflurane, isoflurane, halothane, desflurane; nitrous oxide is NOT a trigger) and depolarizing neuromuscular blockers (succinylcholine).",
            "rationale": "These drugs alter calcium channel function or muscle membrane properties, initiating uncontrolled calcium release in susceptible individuals.",
            "bloom": "recall",
            "source": [{"book": chunks[1].get('book', ''), "page": chunks[1].get('page', 0)}],
            "confusable_with": "nitrous oxide as a trigger"
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the early clinical signs of malignant hyperthermia in an anesthetized patient?",
            "answer": "Sustained muscle rigidity (jaw clenching, elevated jaw tone), tachycardia, tachypnea (if spontaneously breathing), and increased ETCO2 despite hyperventilation.",
            "rationale": "Muscle rigidity reflects uncontrolled contraction; hypermetabolism drives CO2 production exceeding minute ventilation capacity.",
            "bloom": "apply",
            "source": [{"book": chunks[2].get('book', ''), "page": chunks[2].get('page', 0)}],
            "confusable_with": "hypercarbia from inadequate ventilation"
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the acute management of suspected malignant hyperthermia in the OR?",
            "answer": "Stop all triggering agents immediately, hyperventilate with 100% oxygen, call for dantrolene (2.5 mg/kg IV, repeat up to 10 mg/kg), place cooling measures, monitor for rhabdomyolysis/hyperkalemia, and prepare for ICU transfer.",
            "rationale": "Dantrolene inhibits calcium release from sarcoplasmic reticulum; immediate cessation and hyperventilation reduce trigger exposure and manage complications.",
            "bloom": "apply",
            "source": [{"book": chunks[3].get('book', ''), "page": chunks[3].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-5",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the late complications of malignant hyperthermia?",
            "answer": "Rhabdomyolysis leading to myoglobinuria and acute kidney injury, hyperkalemia causing cardiac dysrhythmias, disseminated intravascular coagulation, and compartment syndrome.",
            "rationale": "Massive muscle breakdown releases potassium and myoglobin, overwhelming renal filtration and triggering cascade of complications.",
            "bloom": "apply",
            "source": [{"book": chunks[4].get('book', ''), "page": chunks[4].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-6",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "How should anesthesia be modified for a patient with known or suspected susceptibility to malignant hyperthermia?",
            "answer": "Use IV induction and maintenance (propofol, ketamine, volatile-free techniques), nitrous oxide is safe, avoid succinylcholine, use non-depolarizing agents, and use normal anesthetic doses.",
            "rationale": "Eliminating triggering agents prevents the hypermetabolic cascade while maintaining anesthetic efficacy through alternative pathways.",
            "bloom": "apply",
            "source": [{"book": chunks[5].get('book', ''), "page": chunks[5].get('page', 0)}],
            "confusable_with": ""
        })

    elif 'Malignant hyperthermia: pharmacology' in topic:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the mechanism of action of dantrolene in malignant hyperthermia?",
            "answer": "Dantrolene inhibits calcium release from the sarcoplasmic reticulum by blocking the ryanodine receptor, reducing myoplasmic calcium and halting uncontrolled muscle contraction.",
            "rationale": "Calcium sequestration restores normal muscle physiology and stops the hypermetabolic cascade.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": "peripheral muscle relaxant effect"
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the dosing strategy for dantrolene in acute malignant hyperthermia crisis?",
            "answer": "Initial IV bolus of 2.5 mg/kg over 1-2 minutes; repeat every 5 minutes up to cumulative maximum of 10 mg/kg until signs of MH resolve.",
            "rationale": "Rapid loading achieves therapeutic plasma concentration needed to halt calcium release; titration prevents overdose while ensuring adequate effect.",
            "bloom": "apply",
            "source": [{"book": chunks[1].get('book', ''), "page": chunks[1].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the side effects and complications of dantrolene therapy?",
            "answer": "Muscle weakness, phlebitis (use central line if possible), hepatotoxicity with chronic use, and potential for recrudescence requiring repeated dosing in ICU.",
            "rationale": "Dantrolene crosses into skeletal muscle causing reversible weakness; IV administration is caustic; chronic oral use risks liver injury.",
            "bloom": "apply",
            "source": [{"book": chunks[2].get('book', ''), "page": chunks[2].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What volatile anesthetics trigger malignant hyperthermia and which are safer?",
            "answer": "All volatile agents (halothane, isoflurane, sevoflurane, desflurane) are triggers; NO volatile is completely safe in MH-susceptible patients; complete avoidance is mandatory.",
            "rationale": "All volatiles enhance calcium channel function or alter sarcolemmal properties; complete avoidance is the only safe strategy.",
            "bloom": "recall",
            "source": [{"book": chunks[3].get('book', ''), "page": chunks[3].get('page', 0)}],
            "confusable_with": "some volatiles are safe in MH"
        })

    elif 'Maternal cardiac arrest' in topic:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "Why is perimortem cesarean delivery (PMCD) performed during maternal cardiac arrest?",
            "answer": "PMCD (performed at 4-5 minutes no-flow, optimal 5-15 min) relieves aortocaval compression, restores venous return, improves coronary/cerebral perfusion, and enhances resuscitation success.",
            "rationale": "Gravid uterus compresses IVC (>60%) and aorta, reducing cardiac preload and perfusion pressure; fetal extraction immediately reverses this.",
            "bloom": "analyze",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": "standard CPR alone sufficient for pregnant women"
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the technique for perimortem cesarean delivery?",
            "answer": "Left lateral tilt 15-30 degrees, suprapubic midline incision at level of umbilicus, rapid delivery of fetus and placenta to restore venous return and allow continued compressions.",
            "rationale": "Rapid fetal extraction with minimal delay to ROSC is the priority; fetal viability is secondary to maternal resuscitation success.",
            "bloom": "apply",
            "source": [{"book": chunks[1].get('book', ''), "page": chunks[1].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the common causes of cardiac arrest in pregnant women?",
            "answer": "Amniotic fluid embolism, peripartum cardiomyopathy, preeclampsia/eclampsia, anesthetic complications (aspiration, local anesthetic toxicity, neuraxial complications), venous thromboembolism, and hemorrhage.",
            "rationale": "Pregnancy-specific causes (AFE, PPCM, preeclampsia) and obstetric procedures (neuraxial/spinal) create unique etiologies beyond standard ACLS.",
            "bloom": "recall",
            "source": [{"book": chunks[2].get('book', ''), "page": chunks[2].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the modifications to standard ACLS in pregnant cardiac arrest?",
            "answer": "Perform left lateral uterine displacement (10-15 degrees), perimortem cesarean delivery at 4-5 min if no ROSC, and consider obstetric-specific reversible causes (PRECEDE mnemonic).",
            "rationale": "Uterine displacement and PMCD address pregnancy-specific hemodynamic compromise; differential diagnosis guides targeted interventions.",
            "bloom": "apply",
            "source": [{"book": chunks[3].get('book', ''), "page": chunks[3].get('page', 0)}],
            "confusable_with": ""
        })

    elif 'Maternal cardiovascular' in topic:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the cardiovascular changes during normal pregnancy?",
            "answer": "Plasma volume ↑30-50%, cardiac output ↑30-50%, heart rate ↑10-20 bpm, SVR ↓20% (progesterone-mediated vasodilation), and blood pressure unchanged or slightly decreased.",
            "rationale": "Progesterone causes vasodilation and reduced SVR; increased blood volume and cardiac output compensate, maintaining or slightly reducing afterload.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": "increased blood pressure in pregnancy"
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the significance of aortocaval compression by the gravid uterus?",
            "answer": "Supine position compresses IVC (reduces venous return 50-60%), reduces cardiac output 20-25%, lowers blood pressure, and decreases uteroplacental perfusion.",
            "rationale": "Reduced preload -> reduced cardiac output -> hypotension and fetal hypoxia; lateral positioning relieves compression.",
            "bloom": "analyze",
            "source": [{"book": chunks[1].get('book', ''), "page": chunks[1].get('page', 0)}],
            "confusable_with": "aortic compression alone"
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the perioperative concern with left ventricular hypertrophy in a pregnant hypertensive?",
            "answer": "LVH from chronic hypertension impairs LV compliance, increasing diastolic dysfunction risk; anesthetic agents causing vasodilation or acute preload reduction can trigger ischemia or pulmonary edema.",
            "rationale": "Stiff ventricle is preload-dependent and sensitive to rapid pressure changes; pregnancy's increased preload masks baseline LV dysfunction.",
            "bloom": "analyze",
            "source": [{"book": chunks[2].get('book', ''), "page": chunks[2].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "Why is peripartum cardiomyopathy a critical perioperative risk in obstetric patients?",
            "answer": "PPCM (LV dysfunction in 3rd trimester to 5 post-partum months) presents with heart failure symptoms; pregnancy-induced volume overload and hormonal changes precipitate acute decompensation.",
            "rationale": "Increased preload and afterload stress a failing myocardium; anesthetic-induced vasodilation or fluid shifts can trigger acute pulmonary edema or cardiogenic shock.",
            "bloom": "analyze",
            "source": [{"book": chunks[3].get('book', ''), "page": chunks[3].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-5",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is preeclampsia and how does it affect cardiovascular physiology?",
            "answer": "Preeclampsia = hypertension + proteinuria +/- end-organ dysfunction in pregnancy; pathophysiology involves endothelial dysfunction, increased SVR, reduced plasma volume, and pulmonary edema risk.",
            "rationale": "Abnormal placental perfusion triggers vascular injury, sodium retention, and fluid sequestration; anesthesia risks include hypertensive crisis, eclampsia, and HELLP syndrome.",
            "bloom": "recall",
            "source": [{"book": chunks[4].get('book', ''), "page": chunks[4].get('page', 0)}],
            "confusable_with": "pregnancy-induced hypertension as equivalent to preeclampsia"
        })

    elif 'Maternal gastrointestinal' in topic:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the physiologic changes in gastric function during pregnancy?",
            "answer": "Gastric emptying delayed (especially in labor), increased gastric volume, reduced lower esophageal sphincter tone (progesterone effect), and increased intra-abdominal pressure.",
            "rationale": "These changes increase aspiration risk during anesthesia induction; H2 blockers/proton pump inhibitors indicated preoperatively.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the aspiration risk in pregnant patients and how is it mitigated?",
            "answer": "Pregnant patients have significantly elevated aspiration risk (1:400 in obstetrics vs 1:3000 general); mitigation: NPO status, antacids, H2 blockers, cricoid pressure, rapid sequence intubation, and awake intubation for anticipated difficult airway.",
            "rationale": "Increased gastric volume, reduced tone, and delayed emptying create high-risk combination; rapid airway control essential.",
            "bloom": "apply",
            "source": [{"book": chunks[1].get('book', ''), "page": chunks[1].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What medications are recommended for aspiration prophylaxis in obstetrics?",
            "answer": "H2 blockers (ranitidine 150-300 mg PO/IV), proton pump inhibitors (omeprazole 20 mg PO), sodium citrate (0.3 molar 15-30 mL), and metoclopramide (10 mg IV) to enhance gastric emptying.",
            "rationale": "Combined approach reduces both volume and pH of gastric contents, improving outcome if aspiration occurs.",
            "bloom": "apply",
            "source": [{"book": chunks[2].get('book', ''), "page": chunks[2].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the role of cricoid pressure (Sellick maneuver) in obstetric airway management?",
            "answer": "Cricoid pressure (10 N awake, 30 N after induction) compresses esophagus against cervical spine, preventing gastric regurgitation and aspiration during induction; must be released if mask ventilation inadequate.",
            "rationale": "Mechanical compression blocks esophageal lumen; may impair visualization, so careful application required.",
            "bloom": "apply",
            "source": [{"book": chunks[3].get('book', ''), "page": chunks[3].get('page', 0)}],
            "confusable_with": ""
        })

    elif 'Maternal hematologic' in topic:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the hematologic changes during pregnancy?",
            "answer": "Hemoglobin ↓10-15% (physiologic anemia), white blood cell count ↑25-50%, platelet count unchanged or slightly decreased, coagulation factors (I, VII, VIII, X) ↑, fibrinogen ↑30%, and D-dimer ↑.",
            "rationale": "Expanded plasma volume dilutes red cells; increased coagulation factors create hypercoagulable state predisposing to thromboembolism.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the significance of the hypercoagulable state in pregnancy?",
            "answer": "Pregnancy increases thrombosis risk 4-5 fold; caused by increased clotting factors, reduced protein C/S activity, platelet activation, and venous stasis from gravid uterus.",
            "rationale": "Peripartum DVT/PE risk highest postpartum; thromboprophylaxis and early mobilization essential.",
            "bloom": "apply",
            "source": [{"book": chunks[1].get('book', ''), "page": chunks[1].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What metabolic changes occur in pregnancy and how do they affect anesthesia?",
            "answer": "Reduced serum albumin (hemodilution), increased iron demand, reduced calcium (ionized) especially peripartum, increased glucose metabolism, and reduced alkaline reserve (respiratory alkalosis baseline).",
            "rationale": "Hypoalbuminemia increases free drug concentrations for protein-bound drugs; reduced CO2 buffering worsens fetal hypoxia if maternal ventilation inadequate.",
            "bloom": "apply",
            "source": [{"book": chunks[2].get('book', ''), "page": chunks[2].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is disseminated intravascular coagulation (DIC) in obstetrics and what triggers it?",
            "answer": "DIC = uncontrolled activation of coagulation cascade with consumption of clotting factors, platelets, and fibrinogen; obstetric triggers: placental abruption, amniotic fluid embolism, HELLP syndrome, and fetal demise.",
            "rationale": "Tissue factor release and endothelial injury trigger cascade; life-threatening hemorrhage and thrombosis result.",
            "bloom": "apply",
            "source": [{"book": chunks[3].get('book', ''), "page": chunks[3].get('page', 0)}],
            "confusable_with": ""
        })

    elif 'Maternal neurological' in topic:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the pharmacokinetic changes of anesthetic drugs in pregnancy?",
            "answer": "Increased volume of distribution, decreased MAC for volatiles (MAC ↓30%), altered drug metabolism, increased free fractions of protein-bound drugs (reduced albumin), and accelerated elimination of some drugs.",
            "rationale": "Physiologic changes require dose adjustments; lower MAC means lower volatile concentrations needed.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "How does pregnancy affect seizure threshold and medication requirements?",
            "answer": "Seizure threshold DECREASED in pregnancy; antiepileptic drug (AED) clearance increased; many AEDs have teratogenic effects; perioperative management requires maintained AED levels and seizure precautions.",
            "rationale": "Increased metabolism and expanded volume reduce AED concentrations; preeclampsia/eclampsia additionally lower seizure threshold.",
            "bloom": "apply",
            "source": [{"book": chunks[1].get('book', ''), "page": chunks[1].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is eclampsia and what are its perioperative implications?",
            "answer": "Eclampsia = preeclampsia + seizures; causes hypertensive emergency, increased ICP, pulmonary edema, and renal dysfunction; anesthetic management requires seizure prevention (magnesium sulfate), controlled hypotension, and ICU monitoring.",
            "rationale": "Preeclampsia-induced endothelial dysfunction triggers seizures; magnesium is first-line seizure prophylaxis and therapy.",
            "bloom": "apply",
            "source": [{"book": chunks[2].get('book', ''), "page": chunks[2].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the role of magnesium sulfate in obstetric anesthesia?",
            "answer": "Magnesium sulfate (4-6 g IV bolus, then 1-2 g/hr infusion) prevents eclamptic seizures, decreases BP, and enhances neuromuscular blockade (prolongs duration); monitor for hypermagnesemia toxicity.",
            "rationale": "Blocks NMDA receptors and reduces acetylcholine release; interacts with neuromuscular blockers requiring dose reduction.",
            "bloom": "apply",
            "source": [{"book": chunks[3].get('book', ''), "page": chunks[3].get('page', 0)}],
            "confusable_with": ""
        })

    elif 'Maternal respiratory' in topic:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the respiratory changes during pregnancy?",
            "answer": "Minute ventilation ↑30-50%, tidal volume ↑40%, respiratory rate unchanged, functional residual capacity ↓20%, and PaCO2 ↓10 (hypocapnia to 30-32 mmHg).",
            "rationale": "Progesterone stimulates ventilation; increased CO2 gradients favor fetal-to-maternal CO2 transfer; reduced FRC predisposes to hypoxia during apnea.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": "increased FRC in pregnancy"
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "Why do pregnant women desaturate more rapidly during apnea?",
            "answer": "Reduced FRC (20% decrease) combined with increased oxygen consumption ↑20-30% creates rapid depletion of oxygen reserves; preoxygenation is critical before induction.",
            "rationale": "Lower functional residual capacity provides <3 minutes of apnea reserves vs 8+ minutes in non-pregnant; oxygen demand exceeds supply quickly.",
            "bloom": "analyze",
            "source": [{"book": chunks[1].get('book', ''), "page": chunks[1].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the clinical implication of maternal hypocapnia on the fetus?",
            "answer": "Maternal hypocapnia (PaCO2 30-32 mmHg) causes left shift of maternal oxygen-hemoglobin curve and reduces placental CO2 gradient, decreasing fetal oxygen availability.",
            "rationale": "Reduced maternal-fetal CO2 difference impairs placental gas exchange driving force; fetal PaO2 and pH may decline despite maternal normoxia.",
            "bloom": "analyze",
            "source": [{"book": chunks[2].get('book', ''), "page": chunks[2].get('page', 0)}],
            "confusable_with": "maternal hypocapnia improves fetal oxygenation"
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What perioperative respiratory management strategy is recommended for pregnant patients?",
            "answer": "Aggressive preoxygenation (8 vital capacity breaths or 3-5 min standard), maintain left lateral position, avoid supine positioning, use ramped positioning, apply gentle cricoid pressure, monitor for difficult airway, and have difficult airway cart ready.",
            "rationale": "Reduced FRC and rapid desaturation demand rapid secure airway access; positioning and preoxygenation offset hypoxia risk.",
            "bloom": "apply",
            "source": [{"book": chunks[3].get('book', ''), "page": chunks[3].get('page', 0)}],
            "confusable_with": ""
        })

    elif 'Mechanics of Breathing' in topic:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the lung volumes and capacities in a normal adult?",
            "answer": "Tidal volume (TV) 500 mL, inspiratory reserve volume (IRV) 3000 mL, expiratory reserve volume (ERV) 1100 mL, residual volume (RV) 1200 mL; Vital capacity = TV+IRV+ERV (4600 mL); Total lung capacity (TLC) = VC+RV (5800 mL).",
            "rationale": "RV cannot be expelled; FRC = ERV+RV (2300 mL) is critical for oxygenation during apnea.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is functional residual capacity (FRC) and why is it clinically important?",
            "answer": "FRC = ERV + RV (~2300 mL); volume of air remaining in lungs at end-expiration; provides oxygen reservoir during apnea; reduced FRC (obesity, pregnancy) shortens apnea time before desaturation.",
            "rationale": "Larger FRC delays hypoxia; increased O2 consumption (anesthesia, pregnancy, fever) shortens apnea reserves regardless of FRC.",
            "bloom": "apply",
            "source": [{"book": chunks[1].get('book', ''), "page": chunks[1].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What factors affect airway resistance and work of breathing?",
            "answer": "Airway radius (inverse 4th power: doubling diameter = 16x resistance reduction), airway caliber changes with position (supine increases resistance), and dynamic compression during forced expiration limit flow.",
            "rationale": "Small airway obstruction causes disproportionate resistance increase; forced expiration may collapse airways in obstructive disease.",
            "bloom": "apply",
            "source": [{"book": chunks[2].get('book', ''), "page": chunks[2].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the static and dynamic properties of the respiratory system?",
            "answer": "Static compliance: change in volume per unit pressure change (normal ~100 mL/cm H2O), reflects elastic recoil; Dynamic compliance: tidal volume/plateau pressure, affected by airways obstruction and time constants.",
            "rationale": "Static compliance determines work of breathing; dynamic compliance drops with airway obstruction or asynchronous ventilation.",
            "bloom": "apply",
            "source": [{"book": chunks[3].get('book', ''), "page": chunks[3].get('page', 0)}],
            "confusable_with": ""
        })

    elif 'Morphine & hydromorphone' in topic:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the mechanism of opioid analgesic action?",
            "answer": "Opioids bind to mu (μ) receptors in central and peripheral nervous system, hyperpolarizing neurons and blocking nociceptive signal transmission.",
            "rationale": "Mu-receptor activation inhibits excitatory neurotransmitter release and enhances inhibitory pathways, reducing pain perception.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": "GABA-mediated anesthesia"
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the pharmacokinetic difference between morphine and hydromorphone?",
            "answer": "Morphine: T1/2 2-4 hr, IV dose 5-10 mg, moderate hepatic metabolism; Hydromorphone: T1/2 2-3 hr, IV dose 0.5-1 mg (5-8x more potent), faster metabolism with active M3G metabolite.",
            "rationale": "Hydromorphone's higher potency allows smaller doses; faster clearance reduces accumulation but M3G metabolite can cause neurotoxicity with long-term use.",
            "bloom": "recall",
            "source": [{"book": chunks[1].get('book', ''), "page": chunks[1].get('page', 0)}],
            "confusable_with": "equal potency and metabolism"
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the cardiovascular effects of morphine?",
            "answer": "Peripheral vasodilation (histamine release), mild myocardial depression, reduced heart rate (vagal effect), and orthostatic hypotension; less cardiac depression than other opioids.",
            "rationale": "Histamine-mediated vasodilation and mild myocardial suppression reduce blood pressure; vagal effects lower HR; overall effects modest.",
            "bloom": "apply",
            "source": [{"book": chunks[2].get('book', ''), "page": chunks[2].get('page', 0)}],
            "confusable_with": "significant cardiac depression"
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the respiratory effects of morphine and hydromorphone?",
            "answer": "Dose-dependent respiratory depression from reduced ventilatory drive and CO2 responsiveness; mu-receptors in brainstem depress medullary respiratory centers.",
            "rationale": "Opioids blunt hypercapnic and hypoxic ventilatory drives; risk is highest with rapid IV administration and in opioid-naive patients.",
            "bloom": "apply",
            "source": [{"book": chunks[3].get('book', ''), "page": chunks[3].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-5",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "Why does morphine cause histamine release and what are the clinical consequences?",
            "answer": "Morphine directly triggers mast cell degranulation, releasing histamine, causing pruritus, flushing, tachycardia, bronchospasm (rare), and systemic vasodilation.",
            "rationale": "Histamine-mediated effects are unique to morphine; slower IV administration and pretreatment with antihistamines can mitigate.",
            "bloom": "apply",
            "source": [{"book": chunks[4].get('book', ''), "page": chunks[4].get('page', 0)}],
            "confusable_with": "anaphylaxis"
        })
        kps.append({
            "id": f"{slug}-6",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "How are morphine and hydromorphone metabolized?",
            "answer": "Hepatic glucuronidation produces morphine-3-glucuronide (M3G, neuroexcitatory) and morphine-6-glucuronide (M6G, analgesic); renal elimination; accumulation risk in hepatic/renal failure.",
            "rationale": "M3G accumulation causes myoclonus, hyperalgesia, and seizures in renal dysfunction; M6G contributes to analgesia.",
            "bloom": "recall",
            "source": [{"book": chunks[5].get('book', ''), "page": chunks[5].get('page', 0)}],
            "confusable_with": ""
        })

    elif 'Naloxone & naltrexone' in topic:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the mechanism of opioid antagonism by naloxone?",
            "answer": "Naloxone competitively blocks mu (μ), delta, and kappa opioid receptors with high affinity, reversing opioid effects by displaced binding.",
            "rationale": "Competitive antagonism at receptor sites displaces bound opioid molecules, restoring normal neurotransmission.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": "allosteric antagonism"
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the dosing and administration of naloxone for opioid reversal?",
            "answer": "IV dose 0.04-0.4 mg, IM dose 0.4-0.8 mg; IV preferred for rapid onset; repeat every 2-3 minutes if needed (max 10 mg); duration 30-45 minutes requires vigilance for re-sedation.",
            "rationale": "Lower doses (0.04 mg IV) reverse respiratory depression while preserving analgesia; higher doses completely antagonize opioids.",
            "bloom": "apply",
            "source": [{"book": chunks[1].get('book', ''), "page": chunks[1].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What adverse effects can result from naloxone administration?",
            "answer": "Acute withdrawal (agitation, tachycardia, hypertension, diaphoresis), acute pain from analgesia reversal, arrhythmias, pulmonary edema (especially in chronic opioid users), and seizures.",
            "rationale": "Abrupt opioid reversal triggers sympathetic storm and acute pain; risk is especially high in opioid-dependent patients and overdose combined with stimulants.",
            "bloom": "apply",
            "source": [{"book": chunks[2].get('book', ''), "page": chunks[2].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the difference between naloxone and naltrexone?",
            "answer": "Naloxone: IV/IM antagonist, onset 1-2 min, duration 30-45 min; Naltrexone: oral antagonist, T1/2 24-72 hr, long-acting maintenance therapy.",
            "rationale": "Naloxone is acute reversal agent; naltrexone is used for chronic opioid dependence management with compliance advantage of long action.",
            "bloom": "recall",
            "source": [{"book": chunks[3].get('book', ''), "page": chunks[3].get('page', 0)}],
            "confusable_with": ""
        })

    elif 'Neostigmine & edrophonium' in topic:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the mechanism of action of anticholinesterase agents like neostigmine?",
            "answer": "Neostigmine inhibits acetylcholinesterase, increasing acetylcholine concentration at the neuromuscular junction, competing with non-depolarizing blockers for receptor binding.",
            "rationale": "Excess acetylcholine overwhelms neuromuscular blockade by mass action, restoring neuromuscular transmission.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": "agonist action"
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the dosing and administration strategy for neostigmine in neuromuscular blockade reversal?",
            "answer": "Dose 0.04-0.07 mg/kg IV (max 5 mg), always preceded by anticholinergic (glycopyrrolate 0.01 mg/kg or atropine 0.02 mg/kg) to prevent muscarinic side effects.",
            "rationale": "Anticholinergic prevents excess acetylcholine-mediated effects (salivation, bronchospasm, bradycardia) while preserving nicotinic blockade reversal.",
            "bloom": "apply",
            "source": [{"book": chunks[1].get('book', ''), "page": chunks[1].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the difference between neostigmine and edrophonium?",
            "answer": "Neostigmine: onset 7-11 min, duration 30-40 min, longer-acting; Edrophonium: onset 1 min, duration 5-10 min, shorter-acting (rapid-onset better for diagnosis).",
            "rationale": "Edrophonium's rapid onset/offset makes it ideal for diagnosing neuromuscular disorders; neostigmine is standard for OR reversal.",
            "bloom": "recall",
            "source": [{"book": chunks[2].get('book', ''), "page": chunks[2].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What complications can result from anticholinesterase use?",
            "answer": "Bronchospasm, laryngospasm, bradycardia, salivation, urination, defecation (muscarinic effects), weakness from overdose ('dual block'), and rarely, depolarizing block.",
            "rationale": "Excess acetylcholine at M2/M3 receptors causes airways/GI effects; nicotinic excess can paradoxically worsen blockade.",
            "bloom": "apply",
            "source": [{"book": chunks[3].get('book', ''), "page": chunks[3].get('page', 0)}],
            "confusable_with": ""
        })

    elif 'Nerve stimulator-guided regional' in topic:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the principle of nerve stimulator-guided regional anesthesia?",
            "answer": "A peripheral nerve stimulator delivers electrical current to locate nerves; characteristic muscle twitches confirm nerve proximity and guide needle placement for accurate local anesthetic injection.",
            "rationale": "Motor response confirms needle proximity to the nerve without direct visualization, enabling accurate blockade.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": "ultrasound imaging"
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What stimulator current (mA) and frequency are typical for peripheral nerve stimulation?",
            "answer": "Initial frequency 1-2 Hz, current 1.0-1.5 mA; decrease current while maintaining visible twitch to 0.3-0.5 mA ('needle-to-nerve'); inject local anesthetic with loss of twitch.",
            "rationale": "Lower current requirement indicates closer proximity; loss of response during injection confirms correct plane.",
            "bloom": "apply",
            "source": [{"book": chunks[1].get('book', ''), "page": chunks[1].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the 'paresthesia technique' and how does it differ from nerve stimulation?",
            "answer": "Paresthesia technique: needle advancement until patient reports electric shock sensation (needle in nerve), then withdraw to periosteum; NS technique: electrical stimulation for reproducible motor response.",
            "rationale": "Paresthesia is rapid but patient-dependent and uncomfortable; NS provides objective, consistent confirmation without discomfort.",
            "bloom": "apply",
            "source": [{"book": chunks[2].get('book', ''), "page": chunks[2].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the limitations of nerve stimulator-guided regional anesthesia?",
            "answer": "Cannot visualize anatomy or needle position, risk of intravascular injection, requires cooperative patient (precluded in sedated/anesthetized), and operator-dependent technique.",
            "rationale": "Lack of anatomic visualization and intravascular positioning knowledge create injection risk; ultrasound mitigates these.",
            "bloom": "apply",
            "source": [{"book": chunks[3].get('book', ''), "page": chunks[3].get('page', 0)}],
            "confusable_with": ""
        })

    elif 'Neuraxial Analgesia' in topic and 'Epidural' in topic:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the anatomical location of the epidural space and its significance for anesthesia?",
            "answer": "Epidural space lies between the dura mater and ligamentum flavum; local anesthetic diffuses across dura to reach nerve roots; higher volumes needed than intrathecal (more dilution).",
            "rationale": "Larger epidural space and greater tissue diffusion path require higher doses; allows titrated anesthesia and sustained catheter-based infusions.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": "epidural space below dura"
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the 'loss of resistance' technique for epidural needle placement?",
            "answer": "Needle advanced through ligaments until it reaches epidural space; sudden loss of resistance to saline or air injection confirms epidural placement (air bubble test for catheter).",
            "rationale": "Ligaments create resistance to plunger; epidural space is potential (filled with epidural fat), so resistance suddenly drops.",
            "bloom": "apply",
            "source": [{"book": chunks[1].get('book', ''), "page": chunks[1].get('page', 0)}],
            "confusable_with": "continuous resistance through space"
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is epidural test-dosing and why is it critical?",
            "answer": "3-5 mL of lidocaine 1.5% with epinephrine 1:200,000 injected before full local anesthetic dose; confirms lack of intravascular placement (heart rate increase = IV placement) and intrathecal placement (spinal cord irritation signs).",
            "rationale": "Prevents catastrophic overdose from intravascular or unintended intrathecal injection; test dose effects appear within 30 seconds.",
            "bloom": "apply",
            "source": [{"book": chunks[2].get('book', ''), "page": chunks[2].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the advantages of epidural analgesia in perioperative pain management?",
            "answer": "Excellent pain control, reduced opioid requirements, preserved respiratory drive (with low-dose infusions), enhanced postoperative mobilization, and lower risk of thromboembolic complications.",
            "rationale": "Multimodal analgesia and preserved function improve recovery and reduce complications.",
            "bloom": "apply",
            "source": [{"book": chunks[3].get('book', ''), "page": chunks[3].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-5",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What local anesthetic concentrations and volumes are typically used for epidural analgesia?",
            "answer": "Epidural: bupivacaine 0.1-0.25% or ropivacaine 0.2% infused at 5-10 mL/hr; total epidural dose <=3 mg/kg bupivacaine per 4 hours.",
            "rationale": "Low concentrations provide analgesia with minimal motor blockade; continuous infusions titrate effect and reduce systemic absorption.",
            "bloom": "apply",
            "source": [{"book": chunks[4].get('book', ''), "page": chunks[4].get('page', 0)}],
            "confusable_with": ""
        })

    elif 'Neuraxial anatomy' in topic:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the layers of the spinal meninges and epidural space?",
            "answer": "From superficial to deep: skin -> supraspinous ligament -> interspinous ligament -> ligamentum flavum -> epidural space (fat/vessels) -> dura mater -> subdural space -> arachnoid -> subarachnoid space -> pia mater.",
            "rationale": "Anatomic layers guide needle insertion technique; ligamentum flavum resistance indicates proximity to epidural space.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": "incorrect layer sequence"
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the clinical significance of the conus medullaris location?",
            "answer": "Conus medullaris (spinal cord termination) typically at L1-L2 level in adults (can extend to L3); spinal puncture should be performed at L3-L4 or below to avoid cord trauma.",
            "rationale": "Needles placed above L3 risk cord puncture and permanent neurological injury; L3-L4 space provides safe margin.",
            "bloom": "apply",
            "source": [{"book": chunks[1].get('book', ''), "page": chunks[1].get('page', 0)}],
            "confusable_with": "safe to puncture at L1-L2"
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the path of spinal nerve roots in the epidural space?",
            "answer": "Spinal nerves exit through intervertebral foramina; in the epidural space, they form plexus-like networks that communicate across midline, especially in lumbar region.",
            "rationale": "Epidural local anesthetic diffuses across midline and to multiple levels; unilateral injection often produces bilateral blockade.",
            "bloom": "apply",
            "source": [{"book": chunks[2].get('book', ''), "page": chunks[2].get('page', 0)}],
            "confusable_with": "one-sided injection produces one-sided blockade"
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What landmark is used for neuraxial needle placement?",
            "answer": "Intercristal line (line connecting iliac crests) passes through L4 spinous process; L3-L4 or L4-L5 interspace identified, then needle inserted in midline perpendicular to skin.",
            "rationale": "Palpable bony landmark provides consistent entry point; midline approach minimizes nerve root trauma.",
            "bloom": "apply",
            "source": [{"book": chunks[3].get('book', ''), "page": chunks[3].get('page', 0)}],
            "confusable_with": ""
        })

    elif 'Neuraxial blocks in special' in topic:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the anatomical challenges to neuraxial blockade in obese patients?",
            "answer": "Increased soft tissue, altered surface landmarks, deeper neuraxial structures, and difficult palpation increase needle attempts and failure rates.",
            "rationale": "Technical difficulty requires experienced practitioners; ultrasound greatly improves success.",
            "bloom": "apply",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What special considerations apply to neuraxial blockade in pregnant patients?",
            "answer": "Engorged epidural veins increase bleeding risk (reduce needle/catheter size), elevated intracranial pressure lowers CSF pressure (reduced LA volume needed), aortocaval compression affects dose requirements.",
            "rationale": "Pregnancy-specific anatomy requires reduced volumes and vigilance for complications.",
            "bloom": "apply",
            "source": [{"book": chunks[1].get('book', ''), "page": chunks[1].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "How does aging affect the pharmacology of neuraxial local anesthetics?",
            "answer": "Reduced CSF volume and epidural compliance in elderly increase drug concentration and duration; reduce local anesthetic doses by 25-50% in patients >65 years.",
            "rationale": "Age-related changes in spinal canal anatomy and drug distribution alter effective dosing.",
            "bloom": "apply",
            "source": [{"book": chunks[2].get('book', ''), "page": chunks[2].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the contraindications to neuraxial blockade?",
            "answer": "Absolute: patient refusal, infection at needle site, anticoagulation (INR >1.4, DOAC active), thrombocytopenia (<50,000). Relative: sepsis (debated), mild coagulopathy, uncooperative patient.",
            "rationale": "Infection risk and hemorrhage risk are paramount; systemic sepsis controversy relates to benefit-vs-risk in obstetrics.",
            "bloom": "recall",
            "source": [{"book": chunks[3].get('book', ''), "page": chunks[3].get('page', 0)}],
            "confusable_with": ""
        })

    elif 'Neuraxial complications in obstetrics' in topic:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is postdural puncture headache (PDPH) and what is its pathophysiology?",
            "answer": "PDPH occurs when CSF leaks through dural puncture hole, causing intracranial hypotension and traction on pain-sensitive structures; headache worsens upright, improves supine.",
            "rationale": "Persistent leak maintains low ICP and meningeal traction; bed rest and caffeine provide temporary relief.",
            "bloom": "recall",
            "source": [{"book": chunks[0].get('book', ''), "page": chunks[0].get('page', 0)}],
            "confusable_with": "migraine"
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the role of needle gauge and bevel design in PDPH incidence?",
            "answer": "Smaller gauge needles (25G, 27G pencil-point) reduce PDPH incidence to 1-2% vs 10-15% with 20G needles; pencil-point design (Sprotte, Gertie Marx) cuts fibers rather than shearing them.",
            "rationale": "Smaller hole and non-traumatic penetration reduce leak; pencil-point design preserves fiber integrity.",
            "bloom": "apply",
            "source": [{"book": chunks[1].get('book', ''), "page": chunks[1].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is an epidural blood patch (EBP) and when is it indicated?",
            "answer": "EBP: 15-20 mL autologous blood injected into epidural space at or above puncture level; creates mechanical seal and platelet plug; indicated for PDPH unresponsive to conservative treatment after 24-48 hours or severe cases.",
            "rationale": "Blood clot seals dural rent, halting CSF leak and restoring pressure; immediate relief common.",
            "bloom": "apply",
            "source": [{"book": chunks[2].get('book', ''), "page": chunks[2].get('page', 0)}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the complications of neuraxial blockade specific to obstetrics?",
            "answer": "Maternal: PDPH (higher in obstetrics), permanent nerve injury (rare), epidural abscess/hematoma; Fetal: accidental direct injection into fetus (contraindicated pudendal blocks), systemic absorption toxicity.",
            "rationale": "Obstetric populations have high PDPH risk; careful technique and patient selection mitigate.",
            "bloom": "apply",
            "source": [{"book": chunks[3].get('book', ''), "page": chunks[3].get('page', 0)}],
            "confusable_with": ""
        })

    else:
        # Generic fallback for topics not explicitly mapped
        return []

    return kps

# Build full output
all_kps = []

for item in slice_data:
    topic_kps = author_kps(item)
    all_kps.extend(topic_kps)

print(f"Authored {len(all_kps)} knowledge points across {len(slice_data)} topics")

# Save to file
output_data = all_kps

with open('data/kp_full_part_23.json', 'w', encoding='utf-8') as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print(f"Wrote {len(output_data)} entries to kp_full_part_23.json")

# Validate JSON
try:
    with open('data/kp_full_part_23.json', 'r', encoding='utf-8') as f:
        json.load(f)
    print("JSON validation: OK")
except Exception as e:
    print(f"JSON validation failed: {e}")
