"""
Generate KPs for topics 11-21 (part b)
"""
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/_kp_redeepen.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

slice_data = data[0:33]
kps = []

def kp(idx, n, topic, domain, disc, stem, answer, rationale, bloom, book, page, confusable=''):
    slug = topic.lower().replace(' ','_').replace(':','').replace('(','').replace(')','').replace('&','').replace('/','').replace(',','').replace('—','').replace('-','_').replace('.','').replace("'",'')
    slug = '_'.join(slug.split())[:40]
    return {
        'id': f'{slug}-d{n}',
        'topic': topic,
        'domain': domain,
        'discipline': disc,
        'stem': stem,
        'answer': answer,
        'rationale': rationale,
        'bloom': bloom,
        'source': [{'book': book, 'page': page}],
        'confusable_with': confusable
    }

def script(topic, disc, enabling, patho, course, features, consequence):
    return {
        '_type': 'illness_script',
        'topic': topic,
        'discipline': disc,
        'enabling_conditions': enabling,
        'pathophysiology': patho,
        'time_course': course,
        'key_features': features,
        'consequence_if_missed': consequence
    }

def pair(a, b, discriminator):
    return {'_type': 'confusable_pair', 'topic_a': a, 'topic_b': b, 'discriminator': discriminator}

# ══════════════════════════════════════════════════════════════════════════════
# TOPIC 11: Acute Liver Failure in the ICU
# ══════════════════════════════════════════════════════════════════════════════
t = 'Acute Liver Failure in the ICU'
dom = slice_data[11]['domain']
d = 'anesthesia'

kps.append(kp(11,1,t,dom,d,
    'In acute liver failure with cerebral edema, what are the two options for managing intracranial hypertension, and what risk does mannitol carry?',
    'Hypertonic saline (target Na 145-155 mEq/L) or mannitol both reduce ICP; mannitol carries increased risk of AKI and rebound intracranial hypertension.',
    'Mannitol causes osmotic diuresis that can precipitate AKI in a patient with already compromised renal function (hepatorenal physiology); hypertonic saline avoids this.',
    'apply', 'StatPearls: StatPearls   Acute Liver Failure (ALF)', 12, 'hyperventilation (transient ICP reduction but not recommended for sustained management in ALF)'))

kps.append(kp(11,2,t,dom,d,
    'In acute liver failure, hypophosphatemia below what level actually indicates a favorable prognosis?',
    'Hypophosphatemia <2.5 mg/dL correlates with improved recovery, reflecting active hepatic regeneration consuming phosphate.',
    'Regenerating hepatocytes require phosphate for nucleotide and membrane synthesis; paradoxically low phosphate signals hepatocyte regrowth.',
    'analyze', 'StatPearls: StatPearls   Acute Liver Failure (ALF)', 12, 'hyperphosphatemia in ALF (>5 mg/dL indicates massive necrosis without regeneration; poor prognosis)'))

kps.append(kp(11,3,t,dom,d,
    'After liver transplant, what post-operative complication related to coagulation requires monitoring?',
    'Fibrinolysis — detectable by point-of-care viscoelastic testing (TEG/ROTEM); epsilon-aminocaproic acid or tranexamic acid are indicated when identified but should not be used prophylactically.',
    'Reperfusion of the graft releases tissue plasminogen activator causing fibrinolysis; prophylactic antifibrinolytics are avoided to prevent thrombotic complications.',
    'apply', 'Morgan & Mikhail', 1213, ''))

kps.append(kp(11,4,t,dom,d,
    'In liver failure ICU patients, systemic pooling of blood and fluid transudation cause what hemodynamic physiology?',
    'Relative hypovolemia from splanchnic blood pooling and capillary leak, similar to distributive shock physiology.',
    'Portal hypertension and splanchnic vasodilation in cirrhosis/ALF redistribute effective circulating volume away from kidneys and brain, causing hyperdynamic but inadequate systemic perfusion.',
    'recall', 'Morgan & Mikhail', 2126, 'true hypovolemia (distinguishable by response to volume loading and absence of splanchnic redistribution)'))

kps.append(kp(11,5,t,dom,d,
    'Hepatorenal syndrome albumin infusions increase renal perfusion through what mechanism?',
    'Albumin increases effective arterial blood volume through both oncotic AND non-oncotic mechanisms, enhancing cardiac contractility and renal perfusion.',
    'Non-oncotic albumin effects include free radical scavenging and stabilization of endothelial function; these supplement the osmotic volume-expanding effect.',
    'analyze', 'StatPearls: StatPearls   Hepatorenal Syndrome (HRS)', 8, 'crystalloid (expands volume but lacks non-oncotic benefits of albumin; less effective in HRS)'))

kps.append(kp(11,6,t,dom,d,
    'What MELD score threshold represents a strong indication for liver transplant referral, and what additional variable does MELD-Na add?',
    'MELD >=15 (or any decompensating complication); MELD-Na incorporates serum sodium as a marker of cirrhosis severity.',
    'Hyponatremia independently predicts 90-day waitlist mortality in cirrhotic patients beyond what MELD alone captures, improving risk stratification.',
    'recall', 'StatPearls', 4, 'Child-Pugh score (older score; incorporates encephalopathy/ascites but less quantitative than MELD)'))

kps.append(kp(11,7,t,dom,d,
    'Postoperative jaundice after abdominal surgery can be prehepatic, hepatic, or posthepatic. Which posthepatic cause is unique to the postoperative period?',
    'Postoperative cholecystitis, postoperative pancreatitis, retained common bile duct stone, or bile duct injury from surgery are posthepatic causes specific to the perioperative context.',
    'Bile duct injury and acalculous cholecystitis are surgical/ICU-specific causes; hepatic causes (ischemic hepatitis from intraoperative hypoperfusion) are also unique to the OR.',
    'analyze', 'Morgan & Mikhail', 1174, 'hepatic causes of postop jaundice (ischemic hepatocyte injury from intraoperative hypoperfusion or volatile agents)'))

kps.append(kp(11,8,t,dom,d,
    'In acute pancreatitis, what CT severity index score range indicates severe disease?',
    'CT severity index score 8-10 indicates severe acute pancreatitis; 0-2 is mild, 4-6 is moderate.',
    'CT-based Balthazar criteria combined with degree of pancreatic necrosis provide a composite severity score to guide prognosis and intensity of monitoring.',
    'recall', 'StatPearls: StatPearls   Acute Pancreatitis', 16, 'APACHE II score (clinical severity score without imaging; complementary but different from CT index)'))

kps.append(script(t, d,
    'Acetaminophen overdose (most common in West), viral hepatitis (A, B, E), Wilson disease, Budd-Chiari, drug-induced.',
    'Massive hepatocyte necrosis -> coagulopathy (decreased clotting factor synthesis), encephalopathy (ammonia accumulation), hypoglycemia, renal failure (HRS), immune dysregulation.',
    'Hyperacute (<7 days jaundice-to-encephalopathy) vs. acute (8-28 days) vs. subacute (5-12 weeks); acetaminophen is typically hyperacute.',
    'Jaundice, coagulopathy (INR >1.5), encephalopathy, hypoglycemia; ALT/AST markedly elevated initially then may fall paradoxically with massive necrosis.',
    'Cerebral herniation from intracranial hypertension (leading cause of death); infection; multi-organ failure; survival <20% without transplant in fulminant cases.'))

# ══════════════════════════════════════════════════════════════════════════════
# TOPIC 12: Congenital heart disease (CHD) — general principles
# ══════════════════════════════════════════════════════════════════════════════
t = 'Congenital heart disease (CHD) — general principles'
dom = slice_data[12]['domain']
d = 'anesthesia'

kps.append(kp(12,1,t,dom,d,
    'In a patient with right-to-left intracardiac shunt, what is the risk of IV air bubbles and how does it manifest?',
    'Air emboli can pass directly from venous to systemic (potentially cerebral) arterial circulation through the right-to-left shunt, causing paradoxical air embolism and stroke.',
    'Normal pulmonary capillary filtration removes small air emboli; in right-to-left shunts, this filter is bypassed and venous air reaches systemic circulation directly.',
    'recall', 'Morgan & Mikhail', 351, 'left-to-right shunt (venous air stays in pulmonary circuit; no paradoxical embolism risk)'))

kps.append(kp(12,2,t,dom,d,
    'To LOWER pulmonary vascular resistance in a patient with right-to-left shunting, what ventilatory maneuvers are effective?',
    'Hyperventilation (hypocapnia) with 100% oxygen lowers PVR; avoid acidosis, hypercapnia, hypoxia, sympathetic tone elevation, and high mean airway pressures.',
    'Hypoxia and hypercapnia are potent pulmonary vasoconstrictors; correcting them reduces right-to-left shunt fraction and improves systemic oxygenation.',
    'apply', 'Morgan & Mikhail', 708, 'left-to-right shunts (want increased PVR to reduce shunt; opposite strategy)'))

kps.append(kp(12,3,t,dom,d,
    'Induction of general anesthesia in a patient with cardiac tamponade can precipitate what hemodynamic catastrophe?',
    'Severe hypotension; anesthetic agents cause vasodilation and myocardial depression that removes the compensatory mechanisms sustaining blood pressure in tamponade.',
    'Tamponade physiology depends on tachycardia, increased SVR, and sympathetic tone to maintain cardiac output; anesthesia eliminates all three compensatory mechanisms.',
    'apply', 'Morgan & Mikhail', 708, 'constrictive pericarditis (requires hemodynamic consideration but more gradual decompensation)'))

kps.append(kp(12,4,t,dom,d,
    'Preexcited atrial fibrillation (Wolff-Parkinson-White) with rapid ventricular response and hemodynamic instability requires what immediate intervention?',
    'Electrical cardioversion; rate-slowing AV nodal agents (digoxin, verapamil, beta-blockers) are CONTRAINDICATED as they can accelerate conduction through the accessory pathway.',
    'WPW accessory pathway lacks AV nodal conduction delay; blocking the AV node drives all conduction through the accessory pathway, potentially causing ventricular fibrillation.',
    'apply', 'Society Guideline: Guideline   ACC AHA 2023 Atrial Fibrillation', 100, 'AF without preexcitation (AV nodal agents safe; electrical cardioversion for instability same)'))

kps.append(kp(12,5,t,dom,d,
    'Topically applied timolol eye drops (beta-blocker) used for glaucoma can cause what systemic cardiac effect?',
    'Timolol, a nonselective beta-blocker, reduces heart rate after ophthalmic application due to systemic absorption via the nasolacrimal duct.',
    'Ocular topical drugs drain into the nasolacrimal system, enter the systemic circulation without first-pass hepatic metabolism, causing significant beta-blockade.',
    'apply', 'Morgan & Mikhail', 1254, 'halothane + epinephrine eye drops (ventricular arrhythmias from halothane sensitization)'))

kps.append(kp(12,6,t,dom,d,
    'Factors that INCREASE pulmonary vascular resistance — relevant to avoid in patients with right-to-left CHD shunting — include which list?',
    'Acidosis, hypercapnia, hypoxia, enhanced sympathetic tone, and high mean airway pressures all increase PVR.',
    'Each of these triggers pulmonary arteriolar vasoconstriction via distinct mechanisms (hypoxic pulmonary vasoconstriction, CO2 effects on vessel tone, sympathetic innervation).',
    'recall', 'Morgan & Mikhail', 708, ''))

kps.append(kp(12,7,t,dom,d,
    'Magnesium toxicity in an obstetric patient on magnesium sulfate presents with what clinical signs, and how is it treated?',
    'Hyporeflexia, excessive sedation, blurred vision, respiratory compromise, and cardiac depression; treat with IV calcium gluconate 1 g over 10 min.',
    'Magnesium competitively inhibits calcium at neuromuscular junctions and cardiac ion channels; calcium gluconate reverses these effects by restoring calcium-mediated signaling.',
    'apply', 'Morgan & Mikhail', 1423, 'magnesium therapeutic range (4-7 mEq/L for seizure prophylaxis; toxicity at >7 mEq/L)'))

kps.append(kp(12,8,t,dom,d,
    'Cardiovascular disease is the leading contributor to maternal mortality in the United States. Which acquired forms are most commonly encountered in pregnancy?',
    'Peripartum cardiomyopathy, pulmonary hypertension, and ischemic heart disease are the most common acquired cardiovascular diseases in pregnancy.',
    'Each presents unique anesthetic challenges: peripartum cardiomyopathy limits output reserve; pulmonary HTN can rapidly decompensate with increased preload of delivery; IHD limits coronary reserve.',
    'recall', 'Morgan & Mikhail', 781, ''))

# ══════════════════════════════════════════════════════════════════════════════
# TOPIC 13: Local Anesthetic Systemic Toxicity (LAST)
# ══════════════════════════════════════════════════════════════════════════════
t = 'Local Anesthetic Systemic Toxicity (LAST): Mechanisms & Recognition'
dom = slice_data[13]['domain']
d = 'anesthesia'

kps.append(kp(13,1,t,dom,d,
    'Which optical isomer of bupivacaine blocks cardiac sodium channels more avidly and dissociates more slowly, explaining its greater cardiotoxicity?',
    'The R(+) optical isomer of bupivacaine has tighter, slower sodium channel binding; levobupivacaine (S-) and ropivacaine (S-) have lower cardiotoxicity.',
    'Sodium channel blockade during the cardiac action potential systole with slow recovery prevents normal electrical depolarization and causes refractory ventricular dysrhythmia.',
    'recall', 'Morgan & Mikhail', 432, 'lidocaine (faster sodium channel dissociation; much less cardiotoxic than bupivacaine)'))

kps.append(kp(13,2,t,dom,d,
    'What is the recommended lipid emulsion rescue dose for bupivacaine-induced cardiac toxicity refractory to standard resuscitation?',
    '20% Intralipid 1.5 mL/kg IV bolus; must be available wherever epidural blocks are performed.',
    'Lipid emulsion creates a lipid sink that sequesters bupivacaine away from cardiac sodium channels, restoring cardiac function.',
    'apply', 'Morgan & Mikhail', 432, 'standard ACLS alone (often ineffective in bupivacaine cardiac arrest; lipid emulsion must be added)'))

kps.append(kp(13,3,t,dom,d,
    'Early CNS signs of intravascular local anesthetic injection include which symptoms, and why does detecting them matter?',
    'Tinnitus, dizziness, perioral/circumoral numbness, or metallic taste indicate CNS LAST before seizures or cardiac arrest develop.',
    'CNS toxicity threshold for local anesthetics is lower than cardiac toxicity; early CNS symptoms provide a warning window to stop injection before fatal cardiac effects occur.',
    'recall', 'Morgan & Mikhail', 1399, 'cardiac LAST (occurs at higher plasma levels; CNS symptoms are the earlier warning)'))

kps.append(kp(13,4,t,dom,d,
    'What is the clinical principle embodied by the phrase "every dose is a test dose" in epidural anesthesia?',
    'Every incremental injection of local anesthetic through an epidural catheter should be treated as a potential test dose — aspirate, inject in small aliquots (no more than 5 mL at a time), and observe for early toxicity signs.',
    'Epidural catheters can migrate into epidural veins; incremental dosing limits the total intravascular bolus if unintentional IV injection occurs.',
    'apply', 'Morgan & Mikhail', 1598, 'single-shot epidural (no catheter migration risk; still requires aspiration and incremental injection)'))

kps.append(kp(13,5,t,dom,d,
    'Epinephrine in the epidural test dose serves what specific purpose, and what is its limitation in obstetric patients?',
    'Epinephrine causes tachycardia within 30-60 seconds if intravascular injection occurred (heart rate rise of 20-30 bpm); unreliable in parturients due to marked baseline heart rate variability with contractions.',
    'Contractions cause physiologic tachycardia in laboring patients, making epinephrine-induced HR increase an unreliable marker of intravascular injection.',
    'analyze', 'Morgan & Mikhail', 1399, 'CNS symptoms from test dose (more reliable in obstetric patients)'))

kps.append(kp(13,6,t,dom,d,
    'Peripheral nerve block injury most commonly produces what symptoms, and what is the appropriate initial response?',
    'Minor paresthesia and subjectively decreased sensation are most common; symptoms usually resolve spontaneously with patient reassurance and intermittent follow-up.',
    'Most peripheral nerve injuries after regional anesthesia are neurapraxia from transient local ischemia or mild trauma; full recovery within weeks is typical.',
    'apply', 'Morgan & Mikhail', 1612, 'permanent nerve injury (rare; requires formal neurological assessment if symptoms persist >4-6 weeks)'))

kps.append(kp(13,7,t,dom,d,
    'Ropivacaine appears to have less cardiac toxicity than bupivacaine milligram for milligram. What is the clinical implication for pediatric caudal anesthesia?',
    '0.2% ropivacaine is preferred over bupivacaine in pediatric caudal blocks for its superior cardiac safety profile.',
    'Children have smaller total body weight; ropivacaine's lower cardiotoxic potential provides a greater safety margin when the margin between effective and toxic doses is narrow.',
    'apply', 'Morgan & Mikhail', 1472, 'bupivacaine 0.25% (commonly used but with greater cardiotoxicity risk in small children)'))

kps.append(kp(13,8,t,dom,d,
    'To minimize total dose and reduce LAST risk in regional anesthesia, what general principle applies?',
    'Administer only the minimum required dose for a given regional anesthetic; risk is proportional to total local anesthetic dose delivered.',
    'Lower concentration and volume reduce systemic absorption; combining with epinephrine (vasoconstriction) further slows absorption and lowers peak plasma levels.',
    'apply', 'Morgan & Mikhail', 435, ''))

kps.append(script(t, d,
    'Regional anesthesia (epidural, peripheral nerve block, intercostal); peak risk at vascular injection during epidural or when performing blocks near major vessels (interscalene, paravertebral).',
    'LA absorbed intravascularly inhibits cardiac sodium and calcium channels (causing dysrhythmia/arrest) and CNS sodium channels (causing seizures); bupivacaine causes cardiac arrest before seizures.',
    'CNS symptoms first (tinnitus, perioral numbness, seizure) -> cardiac symptoms (arrhythmia, asystole); can be biphasic.',
    'Circumoral numbness, tinnitus, metallic taste, seizure, cardiovascular collapse; bupivacaine cardiac arrest is refractory.',
    'Cardiac arrest refractory to standard ACLS; permanent neurological injury; death if lipid emulsion rescue not available.'))

kps.append(pair('LAST from bupivacaine','LAST from lidocaine',
    'Bupivacaine: slow Na channel dissociation -> refractory ventricular arrhythmias; cardiac arrest may precede or occur without CNS seizures. Lidocaine: faster channel recovery; seizures typically precede cardiac toxicity and cardiac arrest is more responsive to ACLS.'))

# ══════════════════════════════════════════════════════════════════════════════
# TOPIC 14: Lung Isolation Equipment
# ══════════════════════════════════════════════════════════════════════════════
t = 'Lung Isolation Equipment'
dom = slice_data[14]['domain']
d = 'anesthesia'

kps.append(kp(14,1,t,dom,d,
    'Blind insertion of a left-sided double-lumen tube (DLT) alone results in malposition in approximately what percentage of cases?',
    'Approximately 35% of blind DLT insertions are malpositioned; fiberoptic bronchoscope confirmation is mandatory.',
    'Blind technique relies on tactile resistance at the carina as the only feedback; the bronchoscope directly visualizes bronchial tube placement and confirms isolation.',
    'recall', 'Miller/Baby Miller', 512, ''))

kps.append(kp(14,2,t,dom,d,
    'What are the two techniques for left-sided DLT insertion described in standard practice?',
    '(1) Blind technique: advance past glottis, rotate 90 degrees counterclockwise, advance until resistance — then CONFIRM with fiberoptic bronchoscope. (2) Direct bronchoscopic guidance from the start.',
    'Blind technique is faster but unreliable (35% malposition rate); bronchoscopic confirmation is required regardless of technique used.',
    'apply', 'Miller/Baby Miller', 512, ''))

kps.append(kp(14,3,t,dom,d,
    'In patients with pulmonary bullae requiring positive-pressure ventilation, what lung isolation consideration is paramount?',
    'Low airway pressures must be maintained; adequate expertise and equipment for chest drain insertion and lung isolation must be immediately available in case of bulla rupture or tension pneumothorax.',
    'Positive pressure ventilation makes bulla pressure positive relative to adjacent lung, causing expansion and risk of rupture — which can cause bronchopleural fistula or tension pneumothorax.',
    'apply', 'Miller/Baby Miller', 505, ''))

kps.append(kp(14,4,t,dom,d,
    'Nitrous oxide diffuses into a pulmonary bulla more quickly than nitrogen exits. What clinical consequence does this cause?',
    'Nitrous oxide causes bulla expansion during N2O anesthesia; risk of rupture, tension pneumothorax, and bronchopleural fistula is increased.',
    'N2O diffuses 34x faster than nitrogen; it enters enclosed gas spaces (bullae, pneumothorax, bowel) far faster than nitrogen exits, increasing their volume and pressure.',
    'apply', 'Miller/Baby Miller', 505, 'pneumothorax management (N2O also contraindicated with known pneumothorax)'))

kps.append(kp(14,5,t,dom,d,
    'In one-lung ventilation (OLV), what tidal volume and peak airway pressure limits are recommended to prevent barotrauma?',
    'OLV: VT 4-6 mL/kg; peak airway pressure <35 cmH2O (versus two-lung VT of 6-8 mL/kg).',
    'With only one lung receiving ventilation, the same VT causes twice the alveolar distension; smaller VT prevents volutrauma and barotrauma in the ventilated lung.',
    'recall', 'Miller/Baby Miller', 518, ''))

kps.append(kp(14,6,t,dom,d,
    'During OLV, decreasing FiO2 from 1.0 is recommended when tolerated. What benefit does this provide?',
    'Lower FiO2 during OLV aids absorption atelectasis in the non-dependent (non-ventilated) lung, speeding lung collapse for better surgical exposure.',
    'Nitrogen (an inert gas) slows atelectasis; replacing it with high FiO2 oxygen causes absorption atelectasis in non-ventilated areas — useful for collapsing the operative lung.',
    'apply', 'Miller/Baby Miller', 518, ''))

kps.append(kp(14,7,t,dom,d,
    'Standard precautions in infection control apply to all patients. What is the single most important action to prevent healthcare-associated infection transmission?',
    'Hand hygiene is the most important action to stop the spread of infection — using alcohol-based hand rub (ABHR) or soap and water.',
    'Most nosocomial pathogens are transmitted via contaminated hands; hand hygiene breaks the chain of transmission regardless of organism.',
    'recall', 'MGH Housestaff Manual', 134, 'PPE (important adjunct but less effective than consistent hand hygiene)'))

kps.append(kp(14,8,t,dom,d,
    'What lung isolation indications arise in the setting of massive pulmonary hemorrhage?',
    'Massive hemoptysis (>500-600 mL/24h) may require lung isolation to protect the non-bleeding lung from blood flooding while source control is achieved.',
    'Blood in the tracheobronchial tree from the bleeding lung can overflow into the contralateral lung, causing asphyxiation; lung isolation separates the bleeding side.',
    'apply', 'Morgan & Mikhail', 916, ''))

# ══════════════════════════════════════════════════════════════════════════════
# TOPIC 15: Malignant Hyperthermia: Preoperative Screening & Safe Anesthesia
# ══════════════════════════════════════════════════════════════════════════════
t = 'Malignant Hyperthermia: Preoperative Screening & Safe Anesthesia'
dom = slice_data[15]['domain']
d = 'anesthesia'

kps.append(kp(15,1,t,dom,d,
    'The mortality rate for MH, even with prompt dantrolene treatment, ranges from what percentage?',
    '5% to 30% mortality even with prompt treatment.',
    'Despite dantrolene, the hypermetabolic cascade from uncontrolled intracellular calcium release can cause irreversible hyperthermia, acidosis, rhabdomyolysis, and multi-organ failure.',
    'recall', 'Morgan & Mikhail', 1982, ''))

kps.append(kp(15,2,t,dom,d,
    'What is the mechanism of action and initial dose of dantrolene in treating an MH episode?',
    'Dantrolene 2.5 mg/kg IV; inhibits calcium ion release from sarcoplasmic reticulum by binding Ryr1 receptor; repeat every 5 min until episode terminates (max 10 mg/kg).',
    'MH is caused by uncontrolled calcium release through mutant Ryr1 channels; dantrolene directly plugs the channel, stopping the calcium flood and halting the hypermetabolic state.',
    'apply', 'Morgan & Mikhail', 1982, 'succinylcholine reversal (sugammadex/neostigmine; not related to MH treatment)'))

kps.append(kp(15,3,t,dom,d,
    'What is the first action when MH is suspected intraoperatively?',
    'Discontinue the volatile anesthetic agent and succinylcholine immediately; notify the surgeon; call for help; then administer dantrolene.',
    'Removing the triggering agent stops ongoing Ryr1 channel activation; dantrolene must follow immediately — delay in either step worsens outcomes.',
    'apply', 'Morgan & Mikhail', 1989, 'beta-blockers (used for symptomatic tachycardia but not the primary treatment and do not address the underlying mechanism)'))

kps.append(kp(15,4,t,dom,d,
    'Neuromuscular blocking agents have what relationship to malignant hyperthermia triggering?',
    'Volatile anesthetic agents trigger MH; succinylcholine is also a trigger. Non-depolarizing NMBDs (rocuronium, vecuronium) are NOT triggers and are safe in MH-susceptible patients.',
    'MH susceptibility is due to Ryr1 mutations causing abnormal calcium channel sensitivity; only agents that increase cytoplasmic calcium via Ryr1 (volatile agents, succinylcholine) are triggers.',
    'recall', 'Morgan & Mikhail', 1986, 'succinylcholine (IS a trigger; controversy over whether it triggers without volatile agent)'))

kps.append(kp(15,5,t,dom,d,
    'Neuroleptic malignant syndrome (NMS) clinically resembles MH. What key features help differentiate them?',
    'NMS: occurs with antidopaminergic drugs, develops over DAYS (not minutes to hours); NO muscle rigidity of the MH severity, NO markedly elevated EtCO2 or metabolic acidosis. MH: acute onset, intraoperative, extreme metabolic acidosis, masseter rigidity.',
    'NMS develops as dopaminergic receptor blockade accumulates over time; MH is an acute hypermetabolic crisis triggered by specific anesthetic agents.',
    'analyze', 'Stanford CA-1', 85, 'serotonin syndrome (similar rapid onset to MH; caused by serotonergic drug interactions; no EtCO2 rise; clonus is hallmark)'))

kps.append(kp(15,6,t,dom,d,
    'Conventional dantrolene formulation is 20 mg lyophilized powder requiring dissolution in 60 mL sterile water. What is a practical preparation challenge this creates?',
    'Reconstitution of the initial dose (2.5 mg/kg) can be unavoidably time-consuming with conventional formulation; a newer, more concentrated formulation (Ryanodex) enables faster preparation.',
    'MH is a rapidly lethal emergency; any delay in dantrolene administration worsens outcomes; the newer formulation addresses preparation speed at the cost of higher price.',
    'apply', 'Morgan & Mikhail', 1990, ''))

kps.append(kp(15,7,t,dom,d,
    'In a patient with a known personal or family history of MH, what anesthetic agents are safe to use?',
    'Total intravenous anesthesia (TIVA) with propofol, opioids, non-depolarizing NMBDs, nitrous oxide, and regional anesthesia techniques are all safe; avoid all volatile halogenated agents and succinylcholine.',
    'Safe agents do not activate Ryr1 channels; TIVA completely avoids all triggering agents and is the preferred technique for MH-susceptible patients.',
    'apply', 'Morgan & Mikhail', 1523, 'desflurane (a volatile agent; MH trigger despite being newer)'))

kps.append(kp(15,8,t,dom,d,
    'Shivering can occasionally cause hyperthermia mimicking MH. What features of shivering-related hyperthermia help exclude MH?',
    'Shivering-related hyperthermia (38-39 C) resolves when shivering stops; absent the metabolic acidosis, rhabdomyolysis, EtCO2 rise, and masseter rigidity characteristic of true MH.',
    'Shivering increases O2 consumption and CO2 production but lacks the uncontrolled intracellular calcium release of MH; it is self-limiting once thermoregulatory shivering stops.',
    'analyze', 'Morgan & Mikhail', 1985, 'MH (progressive temperature rise beyond 39C, EtCO2 rise, acidosis, rigidity — key distinguishing features)'))

kps.append(pair('Malignant hyperthermia','Neuroleptic malignant syndrome',
    'MH: acute (minutes) onset; intraoperative volatile agent/succinylcholine trigger; extreme EtCO2 rise, metabolic acidosis, masseter rigidity; treat with dantrolene. NMS: subacute (days) onset; antidopaminergic drugs; lead-pipe rigidity; autonomic instability; treat with dopamine agonists/dantrolene.'))

# ══════════════════════════════════════════════════════════════════════════════
# TOPIC 16: Malignant hyperthermia (pediatric domain)
# ══════════════════════════════════════════════════════════════════════════════
t = 'Malignant hyperthermia'
dom = slice_data[16]['domain']
d = 'anesthesia'

kps.append(kp(16,1,t,dom,d,
    'Children are more susceptible than adults to which succinylcholine-related complications that overlap with MH presentation?',
    'Children are more susceptible to cardiac arrhythmias, hyperkalemia, rhabdomyolysis, myoglobinemia, masseter spasm, and MH from succinylcholine.',
    'Pediatric skeletal muscle has higher proportions of immature acetylcholine receptor isoforms that respond differently to depolarizing blockers; unmasked Duchenne or other myopathies can cause life-threatening hyperkalemia.',
    'recall', 'Morgan & Mikhail', 1458, 'adult response to succinylcholine (hyperkalemia can still occur but much less commonly than in children with undiagnosed myopathy)'))

kps.append(kp(16,2,t,dom,d,
    'When a child experiences cardiac arrest after succinylcholine administration, what immediate treatment must be instituted?',
    'Immediate treatment for hyperkalemia (calcium, bicarbonate, insulin/glucose, hyperventilation); prolonged CPR potentially including cardiopulmonary bypass may be required.',
    'Succinylcholine-induced hyperkalemia in children with undiagnosed myopathy (Duchenne) causes VF; standard ACLS may be insufficient without definitive hyperkalemia reversal.',
    'apply', 'Morgan & Mikhail', 1458, ''))

kps.append(kp(16,3,t,dom,d,
    'Nearly 50% of patients who have an MH episode have had previous uneventful anesthesia. What does this imply for preoperative screening?',
    'A negative anesthetic history does NOT exclude MH susceptibility; susceptibility exists with every exposure but triggers are not always present (volatile agent + succinylcholine both needed historically).',
    'MH is exposure-dependent; previous uneventful anesthesia may have used non-triggering agents or insufficient trigger concentration; vigilance is required on every exposure.',
    'analyze', 'Morgan & Mikhail', 1986, ''))

kps.append(kp(16,4,t,dom,d,
    'About half of MH cases in the past decade were associated with volatile anesthetic as the only trigger. What does this imply about succinylcholine\'s role?',
    'Succinylcholine as a trigger independent of volatile agents is now controversial; volatile agents alone are sufficient triggers in approximately 50% of recent MH cases.',
    'Modern anesthesia practice uses succinylcholine less frequently; its independent triggering role is uncertain, but volatile agents remain unambiguous triggers.',
    'analyze', 'Morgan & Mikhail', 1986, ''))

kps.append(kp(16,5,t,dom,d,
    'Paramyotonia congenita is a rare disorder where myotonia worsens with activity and after exposure to what trigger?',
    'Cold temperatures trigger myotonia in paramyotonia congenita; stiffness worsens with activity (unlike classical myotonia which improves); mexiletine blocks the cold response.',
    'Paramyotonia is caused by SCN4A mutations causing cold-sensitive sodium channel gating defects; action potential prolongation causes persistent depolarization and muscle stiffness.',
    'recall', 'Morgan & Mikhail', 1045, 'myotonia congenita (warms up with repeated activity — opposite direction)'))

kps.append(kp(16,6,t,dom,d,
    'Patients with periodic paralysis who require NMBDs have what characteristic pattern of response?',
    'Response to NMBDs is unpredictable in periodic paralysis; neuromuscular monitoring is mandatory, and succinylcholine and depolarizing agents should be avoided due to hyperkalemia risk.',
    'Periodic paralysis involves ion channel channelopathies that alter neuromuscular junction physiology; unpredictable NMB sensitivity necessitates quantitative TOF monitoring.',
    'apply', 'Morgan & Mikhail', 1025, ''))

kps.append(kp(16,7,t,dom,d,
    'Duchenne and Becker muscular dystrophy anesthetic management is complicated by what cardiac and pulmonary comorbidities?',
    'Cardiac involvement: arrhythmias or congestive heart failure. Pulmonary: hypoventilation, recurrent infections. CK markedly elevated; succinylcholine is absolutely contraindicated.',
    'Progressive dystrophin deficiency causes cardiomyopathy and respiratory muscle weakness; anesthesia compounds both — succinylcholine causes fatal hyperkalemia from membrane fragility.',
    'apply', 'Morgan & Mikhail', 1043, ''))

kps.append(kp(16,8,t,dom,d,
    'After initial dantrolene control of an MH episode, what maintenance dose is given?',
    '1 mg/kg IV maintenance dantrolene after initial episode control; continued monitoring for recurrence for at least 24-48 hours.',
    'MH can recur after apparent control as triggering agents redistribute or calcium stores partially refill; maintenance dosing prevents recrudescence.',
    'apply', 'Morgan & Mikhail', 1990, ''))

# ══════════════════════════════════════════════════════════════════════════════
# TOPIC 17: MH — recognition and management (subspecialty)
# ══════════════════════════════════════════════════════════════════════════════
t = 'Malignant hyperthermia (MH) — recognition and management'
dom = slice_data[17]['domain']
d = 'anesthesia'

kps.append(kp(17,1,t,dom,d,
    'Thyroid storm is a differential diagnosis for intraoperative hyperthermia. What features distinguish thyroid storm from MH?',
    'Thyroid storm is NOT associated with muscle rigidity, elevated CK, or marked metabolic/respiratory acidosis; EtCO2 is normal; temperature rises are less extreme.',
    'MH results from uncoupled mitochondrial metabolism and calcium-driven hypermetabolism; thyroid storm is adrenergic/thyroid hormone-mediated without calcium-mediated muscle hypermetabolism.',
    'analyze', 'Morgan & Mikhail', 1227, 'NMS (also lacks the EtCO2 rise and metabolic acidosis of MH)'))

kps.append(kp(17,2,t,dom,d,
    'Thyroid storm treatment includes what key components including heart rate control?',
    'IV beta-blocker (esmolol infusion, target HR <100/min), hydration and cooling, propylthiouracil/methimazole, and iodine.',
    'Beta-blockers reduce sympathetic manifestations and block peripheral T4-to-T3 conversion (PTU also blocks this); iodine acutely inhibits thyroid hormone release.',
    'apply', 'Morgan & Mikhail', 1227, 'dantrolene for thyroid storm (not indicated; effective only for MH which has Ryr1-mediated pathophysiology)'))

kps.append(kp(17,3,t,dom,d,
    'In the OR, when a patient shows unexplained tachycardia (145 bpm) and hypertension despite high sevoflurane concentrations and fentanyl, what diagnosis should be considered?',
    'MH should be considered when tachycardia and hemodynamic deterioration are accompanied by PVC/arrhythmias despite high volatile agent concentrations — the anesthetic response is paradoxical in MH.',
    'MH increases sympathetic tone and hypermetabolism; the tachycardia and arrhythmias are driven by intracellular calcium flooding and metabolic acidosis, not inadequate anesthesia depth.',
    'analyze', 'Morgan & Mikhail', 86, 'light anesthesia (tachycardia/hypertension respond to increased anesthetic depth; MH worsens with volatile agents)'))

kps.append(kp(17,4,t,dom,d,
    'Serotonin syndrome (associated with MAOIs + meperidine or MAOIs + SSRIs) is distinguishable from MH by what hallmark finding?',
    'Clonus (spontaneous or induced) and hyperreflexia are hallmarks of serotonin syndrome; MH has muscle RIGIDITY without clonus, and has elevated EtCO2 not seen in serotonin syndrome.',
    'Serotonin syndrome involves CNS serotonin receptor excess causing central and peripheral hyperexcitability; MH involves peripheral skeletal muscle calcium release without serotonergic mechanism.',
    'analyze', 'Stanford CA-1', 85, 'NMS (lead-pipe rigidity; autonomic instability; develops over days)'))

kps.append(kp(17,5,t,dom,d,
    'First-generation antipsychotics predispose to NMS through what mechanism, and what treatment is used for severe NMS?',
    'First-generation antipsychotics cause strong dopamine receptor blockade leading to extrapyramidal rigidity (mechanism of NMS); severe NMS is treated with dantrolene, bromocriptine/amantadine/levodopa (dopaminergic agonists), or muscle paralysis.',
    'Loss of dopaminergic modulation of the hypothalamus and basal ganglia causes hyperthermia and rigidity in NMS; restoring dopaminergic signaling reverses the syndrome.',
    'apply', 'Morgan & Mikhail', 1994, 'mild NMS (resolves spontaneously after drug withdrawal without dantrolene)'))

kps.append(kp(17,6,t,dom,d,
    'In anesthetizing an MH-susceptible patient for ambulatory surgery, what must be confirmed before proceeding?',
    'Both infrastructure and operational policies must be consistent with safe anesthetic practice; non-OR settings must have dantrolene available and staff trained in MH management.',
    'Remote locations may lack emergency MH supplies; a patient with MH susceptibility should only be anesthetized where dantrolene and resuscitation capability are immediately available.',
    'apply', 'Morgan & Mikhail', 1512, ''))

kps.append(kp(17,7,t,dom,d,
    'Why should desflurane be avoided in MH-susceptible patients despite being a newer volatile agent?',
    'Desflurane is a halogenated volatile agent and is an MH trigger; all halogenated inhaled anesthetics trigger MH regardless of generation.',
    'MH susceptibility is determined by the Ryr1 receptor\'s response to inhaled agents; desflurane activates Ryr1 similarly to halothane/sevoflurane despite different chemical properties.',
    'recall', 'Morgan & Mikhail', 268, 'nitrous oxide (NOT a trigger; can be used in MH-susceptible patients)'))

kps.append(kp(17,8,t,dom,d,
    'What is the mechanism by which desflurane undergoes degradation by desiccated CO2 absorbents to produce carbon monoxide?',
    'Desiccated CO2 absorbents (especially barium hydroxide lime or strong base absorbents) degrade desflurane (and other volatile agents) to clinically important levels of carbon monoxide.',
    'CO production risk is highest with desiccated absorbents left in circuit overnight; calcium hydroxide-based absorbents or prevention of desiccation avoids this.',
    'apply', 'Morgan & Mikhail', 268, 'compound A from sevoflurane (nephrotoxic degradation product in desiccated absorbents; different gas from CO)'))

# ══════════════════════════════════════════════════════════════════════════════
# TOPIC 18: Massive Hemorrhage: Transfusion Complications
# ══════════════════════════════════════════════════════════════════════════════
t = 'Massive Hemorrhage: Transfusion Complications'
dom = slice_data[18]['domain']
d = 'anesthesia'

kps.append(kp(18,1,t,dom,d,
    'What is transfusion-associated circulatory overload (TACO) and when is it most likely to occur during massive hemorrhage resuscitation?',
    'TACO occurs when blood products are administered at a rate exceeding cardiac output; most likely when providers continue transfusing after bleeding has been controlled.',
    'Once hemorrhage is controlled, the cardiac output cannot accommodate the ongoing high-rate infusion; poor communication between resuscitation and surgical teams is the key risk factor.',
    'recall', 'Morgan & Mikhail', 1332, 'TRALI (transfusion-related acute lung injury — onset within 6h of transfusion; different mechanism from TACO)'))

kps.append(kp(18,2,t,dom,d,
    'What is the single greatest transfusion risk patients face during trauma resuscitation in modern practice?',
    'Transfusion-associated circulatory overload (TACO) — not infectious complications, which have been largely controlled.',
    'Modern blood safety measures have dramatically reduced viral transmission; the predominant risk has shifted to TACO from over-resuscitation after hemorrhage control.',
    'recall', 'Morgan & Mikhail', 1965, 'TRALI (second most common transfusion-related mortality; still significant)'))

kps.append(kp(18,3,t,dom,d,
    'To reduce the risk of TRALI (transfusion-related acute lung injury), what change has been implemented in donor selection?',
    'Blood banks now accept plasma and platelet donations ONLY from males or from females who have never been pregnant or who have tested negative for anti-HLA antibodies.',
    'TRALI is mediated by anti-HLA or anti-neutrophil antibodies from multiparous female donors reacting with recipient leukocytes in the lung microvasculature.',
    'recall', 'Morgan & Mikhail', 1332, 'TACO (cardiogenic pulmonary edema from volume excess; different mechanism from immune-mediated TRALI)'))

kps.append(kp(18,4,t,dom,d,
    'Modern trauma massive transfusion protocols (MTPs) favor earlier plasma and platelet administration. What ratio approximates the evidence-based approach?',
    'Earlier administration of plasma and platelets alongside RBCs (balanced resuscitation); recent practice with trauma particularly favors 1:1:1 FFP:platelets:pRBC ratios.',
    'Trauma coagulopathy begins early from dilution, consumption, and fibrinolysis; replacing coagulation factors from the start prevents the lethal triad of acidosis/coagulopathy/hypothermia.',
    'apply', 'Morgan & Mikhail', 1471, 'crystalloid-only resuscitation (worsens dilutional coagulopathy and hypothermia in massive hemorrhage)'))

kps.append(kp(18,5,t,dom,d,
    'One unit of platelets per 10 kg weight raises platelet count by approximately how much?',
    'Approximately 50,000/microL per unit per 10 kg of body weight.',
    'Standard platelet dosing guideline enables calculation of target platelet count increase in massively transfused patients with thrombocytopenia.',
    'recall', 'Morgan & Mikhail', 1471, ''))

kps.append(kp(18,6,t,dom,d,
    'TRALI manifests with what clinical features and time course?',
    'Fever, pulmonary infiltrates on CXR, cyanosis, hypoxemic respiratory failure, systemic hypotension — onset within 6 hours of transfusion; ~80% recover within 48-96 hours with supportive care.',
    'TRALI mimics ARDS but is immune-mediated; anti-HLA antibodies activate pulmonary neutrophils causing capillary leak and non-cardiogenic pulmonary edema.',
    'recall', 'Miller/Baby Miller', 727, 'TACO (cardiogenic pulmonary edema; onset rapid during infusion; responds to diuresis; no fever)'))

kps.append(kp(18,7,t,dom,d,
    'Fibrinolysis detected by viscoelastic coagulation analysis (TEG/ROTEM) after massive transfusion is treated with what agents, and what is the caveat?',
    'Epsilon-aminocaproic acid or tranexamic acid are indicated when fibrinolysis is detected; should NOT be used prophylactically due to thrombotic risk.',
    'Antifibrinolytics block plasmin formation; prophylactic use can cause pathological clotting; treat only confirmed fibrinolysis on point-of-care testing.',
    'apply', 'Morgan & Mikhail', 1213, ''))

kps.append(kp(18,8,t,dom,d,
    'In vascular surgery with large intraoperative blood loss, what autotransfusion technique is routinely used?',
    'Cell saver (blood scavenging device for autotransfusion) is routinely used in aortic surgery to collect and reinfuse shed blood.',
    'Cell saver reduces allogeneic transfusion requirements by recovering the patient\'s own washed RBCs; contraindicated when surgical field is contaminated with malignant cells or infection.',
    'apply', 'Morgan & Mikhail', 777, ''))

kps.append(pair('TACO','TRALI',
    'TACO: cardiogenic pulmonary edema from volume overload; elevated BNP/pro-BNP; responds to diuresis; no fever typically. TRALI: immune-mediated non-cardiogenic pulmonary edema within 6h of transfusion; anti-HLA antibodies from multiparous donors; normal to low BNP; treatment supportive only.'))

# ══════════════════════════════════════════════════════════════════════════════
# TOPIC 19: Massive hemoptysis and pulmonary hemorrhage
# ══════════════════════════════════════════════════════════════════════════════
t = 'Massive hemoptysis and pulmonary hemorrhage'
dom = slice_data[19]['domain']
d = 'anesthesia'

kps.append(kp(19,1,t,dom,d,
    'Massive hemoptysis is classically defined as what volume of blood loss from the tracheobronchial tree over what time period?',
    'More than 500-600 mL within 24 hours from the tracheobronchial tree.',
    'The threshold defines hemoptysis severe enough to risk asphyxiation, not just hemorrhagic shock; the airway blood-flooding is the immediate threat to life.',
    'recall', 'Morgan & Mikhail', 916, 'submassive hemoptysis (<500 mL/24h; managed more conservatively without urgent lung isolation)'))

kps.append(kp(19,2,t,dom,d,
    'Pulmonary lobe torsion after pneumonectomy or lobectomy causes hemoptysis through what mechanism?',
    'Torsion occludes the pulmonary vein of the affected lobe causing venous outflow obstruction, leading to hemorrhagic infarction and hemoptysis; diagnosis suggested by expanding homogeneous density on CXR and closed lobar orifice on bronchoscopy.',
    'Venous occlusion without arterial occlusion causes congestion and capillary rupture; the diagnosis must be made rapidly as delayed re-expansion leads to irreversible infarction.',
    'analyze', 'Morgan & Mikhail', 916, 'pulmonary artery torsion (arterial occlusion; causes infarction without the venous congestion hemorrhage pattern)'))

kps.append(kp(19,3,t,dom,d,
    'In bronchiectasis, what are the common precipitating insults that lead to airway dilatation and recurrent hemoptysis?',
    'Recurrent infection (MAC, TB, Pseudomonas, ABPA), inhalation injury, GERD/aspiration, impaired immunity (CF, ciliary dyskinesia, immunodeficiency), and obstruction (foreign body, tumor).',
    'Bronchiectasis results from chronic airway infection and inflammation causing irreversible structural airway damage; each recurrent infection dilates and further destroys the bronchial wall.',
    'recall', 'MGH Housestaff Manual', 52, ''))

kps.append(kp(19,4,t,dom,d,
    'Granulomatosis with polyangiitis (GPA, Wegener) can cause pulmonary hemorrhage through what pathological mechanism?',
    'GPA causes necrotizing granulomatous vasculitis of small arteries and veins in the lungs; granulomas or thrombi can occlude lumens and rupture vessels causing alveolar hemorrhage.',
    'The targeted biopsy strategy (guided by CT to active lesions) is recommended over blind biopsy to improve diagnostic yield given GPA\'s patchy distribution.',
    'recall', 'StatPearls: StatPearls   Granulomatosis with polyangiitis (GPA Wegener)', 5, 'microscopic polyangiitis (MPA — non-granulomatous small vessel vasculitis; also causes pulmonary hemorrhage)'))

kps.append(kp(19,5,t,dom,d,
    'Patent ductus arteriosus (PDA) and foramen ovale together in neonates can cause pulmonary hemorrhage through what mechanism?',
    'Unrestricted PFO with PDA allows left-to-right shunting of excess pulmonary venous blood into both ventricles, preventing stress failure and capillary rupture; restrictive PFO with PDA causes pulmonary venous congestion and capillary rupture.',
    'Hemodynamic offloading through the PFO protects against pulmonary capillary rupture; restricted interatrial communication prevents this protection, causing pressure-related pulmonary hemorrhage.',
    'analyze', 'StatPearls: StatPearls   Pulmonary Vasculitis and Hemorrhage', 3, ''))

kps.append(kp(19,6,t,dom,d,
    'Microscopic polyangiitis (MPA) causes pulmonary hemorrhage with what other characteristic organ manifestation?',
    'MPA causes pulmonary-renal syndrome: alveolar hemorrhage (hemoptysis) plus rapidly progressive glomerulonephritis (RPGN); palpable purpura and mononeuritis multiplex are also seen.',
    'MPA is an ANCA-associated vasculitis affecting small vessels; renal and pulmonary capillaritis are the dominant life-threatening manifestations requiring immunosuppression.',
    'recall', 'StatPearls: StatPearls   Microscopic polyangiitis (MPA)', 5, 'GPA (also ANCA-positive but granulomatous; predilection for upper airways and sinuses plus lung/kidney)'))

kps.append(kp(19,7,t,dom,d,
    'Pulmonary hypertension iNO vasoreactivity testing: what defines a positive response that guides treatment in idiopathic pulmonary arterial hypertension?',
    'Positive vasoreactivity response: mPAP reduction >=10 mmHg to reach mPAP <=40 mmHg with increased or unchanged cardiac output; identifies candidates for calcium channel blocker therapy.',
    'Only ~10% of iPAH patients are vasoreactive; these patients have better prognosis and can be treated with CCBs rather than prostacyclin/PDE5 inhibitors.',
    'apply', 'MGH Housestaff Manual', 56, ''))

kps.append(kp(19,8,t,dom,d,
    'Respiratory distress in a patient with active hemoptysis requires what immediate assessment beyond confirming code status?',
    'Confirm SpO2, respiratory rate (measure directly, not charted value), work of breathing (WOB — retractions, tripoding, diaphoresis); low threshold to call rapid response; plan for airway protection.',
    'In massive hemoptysis, progressive airway flooding can cause rapid decompensation; early assessment and potential lung isolation planning must occur before hypoxia is severe.',
    'apply', 'MGH Housestaff Manual', 46, ''))

# ══════════════════════════════════════════════════════════════════════════════
# TOPIC 20: Mechanical Ventilation Modes and Settings (anesthesia ICU)
# ══════════════════════════════════════════════════════════════════════════════
t = 'Mechanical Ventilation Modes and Settings'
dom = slice_data[20]['domain']
d = 'anesthesia'

kps.append(kp(20,1,t,dom,d,
    'What does PRVC (pressure-regulated volume control) combine, and what is its main clinical advantage?',
    'PRVC (also called PCV-VG) combines pressure control breath delivery with an automatic pressure adjustment to guarantee a set tidal volume; advantage is combining VT guarantee with decelerating flow waveform.',
    'Decelerating flow of pressure control optimizes gas distribution while volume guarantee prevents hypoventilation if compliance changes.',
    'recall', 'Miller/Baby Miller', 769, 'pure volume control (square flow waveform; higher peak pressures)'))

kps.append(kp(20,2,t,dom,d,
    'In ARDS requiring mechanical ventilation, corticosteroids and baricitinib target what pathophysiology?',
    'They target the innate/adaptive immune overactivation releasing pro-inflammatory cytokines (IL-6, IL-1beta, TNF-alpha) that potentiate lung injury and diffuse alveolar damage.',
    'Cytokine-mediated alveolar damage is the primary driver of ARDS progression; immunomodulation reduces this pathway.',
    'apply', 'StatPearls: StatPearls   Mechanical Ventilation  Modes and Settings', 13, ''))

kps.append(kp(20,3,t,dom,d,
    'When peak airway pressure rises AND PEEP also increases AND hypotension develops, what specific emergency must be ruled out immediately?',
    'Tension pneumothorax; the simultaneous rise in peak pressure and PEEP with hypotension from reduced venous return is the classic triad.',
    'Tension pneumothorax causes progressive air accumulation under pressure, shifting mediastinum and compressing the contralateral lung and great vessels — reducing venous return to a critical level.',
    'apply', 'Miller/Baby Miller', 380, 'auto-PEEP (elevated intrinsic PEEP from air trapping; also causes hypotension but without the same acute escalation)'))

kps.append(kp(20,4,t,dom,d,
    'ECMO cannulation for veno-venous ECMO uses what cannula configuration, and what should be avoided?',
    'VV-ECMO: drainage cannula in femoral vein near IVC-RA junction, return cannula in internal jugular vein near SVC-RA junction; dual-lumen catheters should be avoided (require specialized guidance, prone to mispositioning).',
    'VV-ECMO drains deoxygenated blood, passes it through a membrane oxygenator, and returns oxygenated blood; correct positioning prevents recirculation and maximizes gas exchange.',
    'apply', 'StatPearls: StatPearls   Mechanical Ventilation  Modes and Settings', 10, 'VA-ECMO (also provides cardiac support; different cannula configuration including arterial return)'))

kps.append(kp(20,5,t,dom,d,
    'Volume control ventilation (VCV) provides what type of inspiratory flow pattern, and what are its trade-offs compared to PCV?',
    'VCV provides a constant (square) inspiratory flow pattern; guarantees VT but produces higher peak airway pressures than PCV for same VT, especially when compliance is poor.',
    'Constant flow fills lung linearly; deceleration flow in PCV better matches the declining compliance during lung filling, reducing peak pressure while achieving similar mean airway pressures.',
    'recall', 'Miller/Baby Miller', 768, ''))

kps.append(kp(20,6,t,dom,d,
    'Turbine-based anesthesia machine ventilators are primarily what type of generators, and what advantage does the turbine provide?',
    'Turbine ventilators are primarily pressure generators placed directly within the circle system; advantage: can generate volume control, pressure control, pressure support, and APRV from a single turbine.',
    'Turbine placement within the circle system eliminates the need for a driving gas and allows precise flow control for multiple modes, unlike traditional bellows-driven systems.',
    'recall', 'Miller/Baby Miller', 271, ''))

kps.append(kp(20,7,t,dom,d,
    'Noninvasive ventilation (NIV) in chronic settings: what empiric bilevel (BiPAP S/T) settings can be used while awaiting formal polysomnography titration for OSA?',
    'Autotitrating NIV modes such as volume-assured pressure support (VAPS) with auto-EPAP can adjust EPAP to maintain upper airway patency empirically before formal PAP titration.',
    'Auto-EPAP algorithms titrate to eliminate apneas and hypopneas automatically; this interim approach maintains airway patency without PSG guidance.',
    'apply', 'StatPearls: StatPearls   Noninvasive Ventilation (NIV)', 6, ''))

kps.append(kp(20,8,t,dom,d,
    'What is the closed-loop communication step required before emergency endotracheal intubation in the ICU?',
    'A time-out must be conducted to review patient details, consent, and anticipated intubation approach — unless a life-threatening emergency precludes it.',
    'Structured team communication before intubation reduces errors (wrong-patient, wrong-approach); the life-threatening exception acknowledges that deliberate communication must sometimes yield to speed.',
    'apply', 'StatPearls: StatPearls   Mechanical Ventilation  Modes and Settings', 7, ''))

# ══════════════════════════════════════════════════════════════════════════════
# TOPIC 21: Neuromuscular Monitoring: Principles
# ══════════════════════════════════════════════════════════════════════════════
t = 'Neuromuscular Monitoring: Principles'
dom = slice_data[21]['domain']
d = 'anesthesia'

kps.append(kp(21,1,t,dom,d,
    'Monitoring of neuromuscular blockade and pharmacological reversal are described as what standard of care?',
    'Monitoring of NMB and pharmacological reversal are the standard of care; postoperative residual paralysis occurs frequently without it.',
    'Residual NMB (TOF ratio <0.9) causes pharyngeal dysfunction and aspiration risk; quantitative monitoring is needed because clinical tests (sustained head lift) are inadequate.',
    'recall', 'Stanford CA-1', 37, 'qualitative (subjective) TOF assessment (unreliable; cannot confirm TOF ratio >=0.9 without quantitative device)'))

kps.append(kp(21,2,t,dom,d,
    'The current challenges and opportunities in neuromuscular reversal and monitoring are described in what landmark 2017 publication?',
    'Brull SJ, Kopman AF. "Current status of neuromuscular reversal and monitoring: challenges and opportunities." Anesthesiology 2017;126:173.',
    'This reference established the evidence base for quantitative NMB monitoring as standard of care and outlined persistent gaps in clinical practice.',
    'recall', 'Morgan & Mikhail', 220, ''))

kps.append(kp(21,3,t,dom,d,
    'In cerebral aneurysm surgery, what monitoring modality is used for detection of venous air embolism given the potential for sitting position?',
    'Precordial Doppler sonography detects venous air embolism in patients in the sitting position (e.g., posterior fossa surgery); highly sensitive for small air volumes.',
    'The sitting position places the operative field above the heart; venous air entrainment can occur and must be detected early; Doppler detects air before hemodynamic compromise.',
    'apply', 'Morgan & Mikhail', 995, 'TEE (gold standard for air detection but more invasive; Doppler is used for routine monitoring)'))

kps.append(kp(21,4,t,dom,d,
    'Somatosensory evoked potential (SSEP) monitoring during spine surgery: what drug class affects latency and amplitude most significantly?',
    'Inhaled anesthetic agents (volatile agents) dose-dependently increase latency and decrease amplitude of cortical SSEPs; total IV anesthesia (TIVA) with propofol/opioids is preferred for SSEP monitoring.',
    'Volatile agents inhibit cortical synaptic transmission; the amplitude reduction can mask the signal changes from cord injury that SSEP monitoring is designed to detect.',
    'apply', 'Miller/Baby Miller', 599, 'nitrous oxide (also reduces SSEP amplitude but less than equipotent volatile agents)'))

kps.append(kp(21,5,t,dom,d,
    'Spinal cord injury classification as "complete" versus "incomplete" depends on what criterion?',
    '"Complete" SCI: no motor or sensory function below the level of injury. "Incomplete": partial injury with some residual sensory or motor function below the level.',
    'ASIA classification guides prognosis; incomplete injuries have varying recovery potential; complete injuries below C4 may still preserve some autonomic function.',
    'recall', 'Miller/Baby Miller', 809, ''))

kps.append(kp(21,6,t,dom,d,
    'Head injury patients with GCS <=8 or signs of intracranial hypertension generally require airway management. What nasal airway caution applies?',
    'Nasal airways and nasogastric tubes should be avoided if possible in TBI patients with facial fractures or suspected skull base fractures due to risk of intracranial insertion.',
    'Cribriform plate fractures allow nasal tubes to penetrate the intracranial vault; oral routes (OGT, oral airway) are safe alternatives.',
    'apply', 'Miller/Baby Miller', 808, ''))

kps.append(kp(21,7,t,dom,d,
    'Anesthesiologists are described as being at the forefront of patient monitoring. Monitoring devices are organized in modern anesthesia by what principle?',
    'Monitoring devices are organized by organ system rather than by physical property or technique, reflecting a physiologic approach to patient assessment.',
    'Organ-based monitoring organization aligns assessment with clinical pathophysiology rather than technology type, facilitating comprehensive patient monitoring across systems.',
    'recall', 'Miller/Baby Miller', 375, ''))

kps.append(kp(21,8,t,dom,d,
    'In spinal anesthesia, the motor block during a subdural block is modest despite extensive sensory blockade. Why?',
    'Subdural space is relatively more capacious in posterior and lateral aspects, sparing the anterior motor roots while extensively blocking posterior (sensory) roots.',
    'Subdural space distributes local anesthetic posteriorly and laterally; motor fibers in the anterior spinal cord roots receive less drug than the sensory fibers, creating dissociated block.',
    'analyze', 'Miller/Baby Miller', 339, 'high spinal (affects motor equally or more than sensory)'))

print('Topics 11-21 KP count:', len(kps))
