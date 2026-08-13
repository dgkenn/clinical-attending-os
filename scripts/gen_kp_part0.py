"""
Generate KPs for topics 0-32 from _kp_redeepen.json -> data/kp_redeep_part_0.json
Run from repo root: python scripts/gen_kp_part0.py
"""
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/_kp_redeepen.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

slice_data = data[0:33]
kps = []

# ── helpers ──────────────────────────────────────────────────────────────────
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
# TOPIC 0: Anaphylaxis
# ══════════════════════════════════════════════════════════════════════════════
t = 'Anaphylaxis'
dom = slice_data[0]['domain']
d = 'medicine'

kps.append(kp(0,1,t,dom,d,
    'Allergic reactions account for approximately what fraction of all anesthetic complications, and what is the reported intraoperative mortality?',
    'Approximately 10% of all anesthetic complications; mortality ~3.4%.',
    'Multiple sensitizing drugs are given concurrently at induction, raising allergen exposure across a brief window.',
    'recall', 'Stanford CA-1', 78, 'anaphylactoid reaction (non-IgE, clinically identical)'))

kps.append(kp(0,2,t,dom,d,
    'More than 90% of intraoperative anaphylactic reactions occur within what time window, and what clinical principle does this imply?',
    'Within 3 minutes; the faster the onset, the more severe the course.',
    'Rapid mast-cell degranulation produces an immediate systemic mediator flood; delayed reactions tend to be milder.',
    'recall', 'Stanford CA-1', 78, 'delayed latex reaction (may occur hours into case)'))

kps.append(kp(0,3,t,dom,d,
    'A patient under halothane anesthesia develops intraoperative anaphylaxis. What is the maximum safe epinephrine dose and why?',
    'Epinephrine should not exceed 1.5 mcg/kg when halothane is used; halothane sensitizes the myocardium to epinephrine-induced arrhythmias.',
    'Halothane potentiates catecholamine-triggered ventricular arrhythmias by altering myocardial membrane ion channel kinetics.',
    'apply', 'Morgan & Mikhail', 261, 'desflurane (safe up to 4.5 mcg/kg; no myocardial sensitization)'))

kps.append(kp(0,4,t,dom,d,
    'Under desflurane anesthesia, up to what epinephrine dose can be given without heightened arrhythmia risk?',
    'Up to 4.5 mcg/kg; desflurane does not sensitize the myocardium to epinephrine.',
    'Unlike halothane, desflurane does not augment catecholamine-triggered ventricular dysrhythmias.',
    'recall', 'Morgan & Mikhail', 268, 'halothane (limit 1.5 mcg/kg)'))

kps.append(kp(0,5,t,dom,d,
    'After post-extubation laryngeal edema following an intraoperative allergic reaction, what two agents are used?',
    'IV dexamethasone 0.25-0.5 mg/kg to prevent edema formation PLUS nebulized racemic epinephrine (0.25-0.5 mL of 2.25% solution in 2.5 mL NS).',
    'Dexamethasone reduces vascular permeability; racemic epinephrine causes alpha-mediated vasoconstriction to shrink mucosal swelling.',
    'apply', 'Morgan & Mikhail', 1475, 'systemic IM epinephrine (appropriate for anaphylaxis but different dosing from airway edema treatment)'))

kps.append(kp(0,6,t,dom,d,
    'Which patient populations mandate latex allergy screening before anesthesia?',
    'Healthcare workers (repeated exposure), children with spina bifida (multiple procedures), urogenital abnormalities (repeat catheterization), and patients with allergy to tropical fruits (mango, kiwi, avocado, passion fruit, banana, fig, chestnut).',
    'Latex proteins cross-react with tropical fruit antigens (latex-fruit syndrome), indicating shared epitope sensitization.',
    'recall', 'Stanford CA-1', 79, 'latex irritant contact dermatitis (non-IgE; no anaphylaxis risk)'))

kps.append(kp(0,7,t,dom,d,
    'A latex-allergic patient requires an elective case. What OR scheduling strategy minimizes airborne latex exposure?',
    'Schedule as the first case of the day; aerosolized latex from powdered gloves accumulates throughout the day.',
    'First-case rooms have lowest residual latex aerosol concentrations before other cases contaminate the air.',
    'apply', 'Stanford CA-1', 79, ''))

kps.append(kp(0,8,t,dom,d,
    'Why is identifying the causative agent of intraoperative anaphylaxis often difficult?',
    'Multiple drugs (NMBAs, antibiotics, colloids) are given in rapid succession at induction, making temporal attribution ambiguous.',
    'NMBAs and perioperative antibiotics are the most common triggers and are given within minutes of each other.',
    'analyze', 'Stanford CA-1', 37, ''))

kps.append(script(t, d,
    'Recent drug exposure in OR (NMBAs, antibiotics, latex, colloids); prior IgE sensitization.',
    'IgE-mediated mast cell/basophil degranulation releases histamine, tryptase, leukotrienes -> vasodilation, bronchospasm, capillary leak.',
    '>90% within 3 min of exposure; onset speed inversely correlates with severity.',
    'Urticaria/flushing, bronchospasm, cardiovascular collapse (hypotension + tachycardia), angioedema.',
    'Cardiovascular arrest; 3.4% mortality even treated; delayed recognition worsens outcome.'))

kps.append(pair('Anaphylaxis','Anaphylactoid reaction',
    'Anaphylaxis = IgE-mediated (requires prior sensitization); anaphylactoid = direct mast-cell degranulation (contrast, vancomycin). Clinically identical; treatment is the same: epinephrine first.'))

# ══════════════════════════════════════════════════════════════════════════════
# TOPIC 1: Septic Shock
# ══════════════════════════════════════════════════════════════════════════════
t = 'Septic Shock'
dom = slice_data[1]['domain']
d = 'medicine'

kps.append(kp(1,1,t,dom,d,
    'What is the MAP target for vasopressor therapy in septic shock, and when is a lower permissive target of MAP >60 appropriate?',
    'Target MAP >65 mmHg (standard); MAP >60 may be appropriate in select patients to reduce vasopressor exposure (JAMA 2020).',
    'Higher MAP targets require more vasopressor with potential ischemic end-organ effects; permissive hypotension may reduce harm in some cohorts.',
    'apply', 'MGH Housestaff Manual', 66, 'cardiogenic shock (may require higher MAP for coronary perfusion)'))

kps.append(kp(1,2,t,dom,d,
    'What is the first-choice vasopressor in septic shock, and at what dose is vasopressin added?',
    'Norepinephrine (levo) is first-choice; add vasopressin (0.04 U/min, not titrated) when NE reaches 5-15 mcg/min.',
    'Vasopressin acts on V1 receptors independent of adrenergic pathways, maintaining vasomotor tone when catecholamine receptors are downregulated in prolonged shock.',
    'apply', 'MGH Housestaff Manual', 66, 'dopamine (acceptable alternative but more arrhythmias; now second-line)'))

kps.append(kp(1,3,t,dom,d,
    'In the FACTT trial comparing fluid strategies for ALI/sepsis patients, what outcome advantage did the conservative fluid group demonstrate?',
    'Conservative fluid patients had improved lung function, improved CNS function, decreased need for sedation and mechanical ventilation, with no increase in organ failure.',
    'Excess fluid exacerbates pulmonary and cerebral edema; once the cause of hypoperfusion is controlled, ongoing fluid delivery is harmful.',
    'analyze', 'Miller/Baby Miller', 764, 'liberal fluid strategy (more fluid worsens outcomes in ALI/sepsis after initial resuscitation)'))

kps.append(kp(1,4,t,dom,d,
    'Norepinephrine has what receptor profile and what primary effect in septic shock?',
    'Norepinephrine is a prominent alpha-1 agonist with mild beta-1 activity; overall effect is widespread systemic vasoconstriction with variable effects on cardiac output.',
    'Alpha-1 mediated vasoconstriction restores SVR and MAP in distributive shock; modest beta-1 activity avoids excessive chronotropy.',
    'recall', 'Marino ICU Book', 718, 'epinephrine (strong alpha + beta; reserve for NE-refractory shock or anaphylaxis)'))

kps.append(kp(1,5,t,dom,d,
    'What is the initial dose range for norepinephrine infusion in septic shock?',
    'Initial: 2-12 mcg/min via peripheral IV if <10 mcg/min; max 35-100 mcg/min.',
    'Norepinephrine is preferred for its reliable alpha-1 pressor effect; early dosing at lower rates reduces peripheral ischemia risk.',
    'recall', 'MGH Housestaff Manual', 67, ''))

kps.append(kp(1,6,t,dom,d,
    'When should epinephrine be added in septic shock management?',
    'Epinephrine is recommended when norepinephrine alone is insufficient to achieve MAP targets.',
    'Epinephrine provides combined alpha and beta stimulation, increasing both SVR and cardiac output, but at risk of increased lactate and arrhythmias.',
    'apply', 'MGH Housestaff Manual', 66, 'dobutamine (use for cardiogenic shock component; does not increase SVR)'))

kps.append(kp(1,7,t,dom,d,
    'The RUSH exam (Rapid Ultrasound for Shock) helps identify which obstructive causes during evaluation of undifferentiated shock?',
    'Pericardial tamponade, pulmonary edema, pneumothorax, and occult intra-abdominal hemorrhage.',
    'Bedside ultrasound rapidly characterizes cardiac function and fluid status, enabling differentiation of distributive, obstructive, hypovolemic, and cardiogenic shock.',
    'apply', 'StatPearls: StatPearls   Distributive Shock (Non septic)', 4, 'CT scan (slower; avoid in hemodynamically unstable patients)'))

kps.append(kp(1,8,t,dom,d,
    'What lactate threshold carries prognostic significance in severe sepsis?',
    'Lactate >4 mEq/L is strongly correlated with mortality in severe sepsis.',
    'Hyperlactatemia reflects impaired tissue oxygen utilization from microcirculatory failure; it predicts organ failure and death independent of blood pressure.',
    'recall', 'Marino ICU Book', 153, 'mixed venous O2 saturation (complementary marker of global O2 delivery/consumption balance)'))

kps.append(script(t, d,
    'Known or suspected infection; immunosuppression, invasive devices, prolonged hospitalization increase risk.',
    'Gram-negative lipopolysaccharide or gram-positive toxins trigger systemic inflammatory cascade -> vasodilation, capillary leak, myocardial depression, organ failure.',
    'Sepsis criteria met first (SOFA >=2); shock develops over hours as resuscitation fails to restore perfusion.',
    'Hypotension despite fluid resuscitation, vasopressor requirement to maintain MAP >65, lactate >2 mmol/L, fever/hypothermia, organ dysfunction (AKI, encephalopathy).',
    'Multi-organ failure, ARDS, refractory shock, death; early antibiotics + source control are time-critical.'))

# ══════════════════════════════════════════════════════════════════════════════
# TOPIC 2: Hospital-Acquired and Ventilator-Associated Pneumonia
# ══════════════════════════════════════════════════════════════════════════════
t = 'Hospital-Acquired and Ventilator-Associated Pneumonia'
dom = slice_data[2]['domain']
d = 'medicine'

kps.append(kp(2,1,t,dom,d,
    'How is hospital-acquired pneumonia (HAP) defined, and how does VAP differ?',
    'HAP: pneumonia developing >=48h after hospital admission. VAP: pneumonia developing >=48h after endotracheal intubation.',
    'The 48-hour threshold distinguishes community-acquired pathogens from hospital-acquired organisms in both categories.',
    'recall', 'MGH Housestaff Manual', 117, 'healthcare-associated pneumonia (HCAP) — no longer recommended as a distinct category per 2016 IDSA/ATS guidelines'))

kps.append(kp(2,2,t,dom,d,
    'What clinical criteria define VAP diagnosis?',
    'New or progressive infiltrate on CXR PLUS at least 2 of 3: fever, leukocytosis, purulent tracheal secretions.',
    'No single sign is sufficient; combination criteria increase specificity for distinguishing true VAP from non-infectious VAEs (atelectasis, ARDS).',
    'apply', 'MGH Housestaff Manual', 117, 'ventilator-associated events (VAEs) — non-infectious causes of clinical deterioration in ventilated patients'))

kps.append(kp(2,3,t,dom,d,
    'What organisms are the predominant pathogens in HAP/VAP versus community-acquired pneumonia (CAP)?',
    'HAP/VAP: gram-negative bacilli (Pseudomonas, Klebsiella) and MRSA. CAP: Streptococcus pneumoniae and H. influenzae.',
    'Hospital flora evolve toward resistant gram-negatives under antibiotic selection pressure; MRSA prevalence increases with ICU exposure.',
    'recall', 'Curated Units', 0, 'S. pneumoniae (dominant in CAP but uncommon in HAP/VAP)'))

kps.append(kp(2,4,t,dom,d,
    'For HAP/VAP empiric therapy, what antibiotic spectrum is required?',
    'Anti-pseudomonal coverage (cefepime or piperacillin-tazobactam) +/- fluoroquinolone +/- vancomycin for MRSA risk; de-escalate based on cultures.',
    'Pseudomonas and MRSA are prevalent in hospital-acquired organisms; broad initial coverage reduces early mortality; culture-directed de-escalation limits resistance.',
    'apply', 'Curated Units', 0, 'CAP empiric therapy (amoxicillin-clavulanate or fluoroquinolone; insufficient for HAP/VAP)'))

kps.append(kp(2,5,t,dom,d,
    'Gram-negative organisms account for the majority of infection-related SIRS in HAP/VAP through what mechanism?',
    'Gram-negative LPS (lipopolysaccharides) are the most commonly recognized triggers of the systemic inflammatory response, activating TLR4-mediated cytokine release.',
    'LPS activates pattern-recognition receptors, triggering a cytokine cascade that can cause widespread organ dysfunction if prolonged.',
    'recall', 'Morgan & Mikhail', 2148, 'gram-positive organisms (can also cause SIRS via exotoxins/superantigens)'))

kps.append(kp(2,6,t,dom,d,
    'What does evidence from Chastre et al. (JAMA 2003) show about VAP antibiotic duration?',
    '8-day antibiotic courses have similar efficacy to 15-day courses for VAP in adults.',
    'Shorter courses reduce antibiotic selective pressure and resistance emergence without worsening outcomes for most VAP episodes.',
    'recall', 'Marino ICU Book', 563, 'prolonged therapy (15 days increases resistance without mortality benefit in most VAP)'))

kps.append(kp(2,7,t,dom,d,
    'MRSA is responsible for approximately what proportion of hospital-acquired S. aureus pneumonias?',
    'Approximately 51% of hospital-acquired S. aureus pneumonias are MRSA; 49% are MSSA.',
    'MRSA prevalence in HAP mandates empiric vancomycin or linezolid when MRSA risk factors are present until cultures confirm susceptibility.',
    'recall', 'StatPearls', 3, 'community-acquired S. aureus pneumonia (MRSA less common; ~3% of CAP cases)'))

kps.append(kp(2,8,t,dom,d,
    'What is the antibiotic treatment distinction between MRSA and MSSA staphylococcal pneumonia?',
    'MRSA requires vancomycin or linezolid; MSSA is treated with anti-staphylococcal penicillins (nafcillin) or cefazolin.',
    'Methicillin resistance alters the beta-lactam binding protein (PBP2a), rendering all beta-lactams ineffective against MRSA.',
    'apply', 'StatPearls', 3, 'MSSA (beta-lactam therapy effective and preferred for MSSA due to better tissue penetration than vancomycin)'))

# ══════════════════════════════════════════════════════════════════════════════
# TOPIC 3: ICU Sedation
# ══════════════════════════════════════════════════════════════════════════════
t = 'ICU Sedation'
dom = slice_data[3]['domain']
d = 'medicine'

kps.append(kp(3,1,t,dom,d,
    'Why is etomidate not recommended for prolonged ICU sedation, particularly in septic patients?',
    'Etomidate consistently suppresses adrenocortical function when infused for ICU sedation, with reports of increased mortality in critically ill (especially septic) patients.',
    'Etomidate irreversibly inhibits 11-beta-hydroxylase, blocking cortisol synthesis; adrenal insufficiency worsens hemodynamics in sepsis.',
    'recall', 'Morgan & Mikhail', 290, 'single-dose etomidate for induction (transient suppression; acceptable for single use)'))

kps.append(kp(3,2,t,dom,d,
    'Why is propofol contraindicated for prolonged sedation of critically ill pediatric ICU patients?',
    'Propofol infusion syndrome (PRIS) is associated with mortality in critically ill children receiving prolonged propofol sedation.',
    'PRIS involves metabolic acidosis, rhabdomyolysis, cardiac failure, and renal failure; mechanism involves mitochondrial respiratory chain disruption.',
    'recall', 'Morgan & Mikhail', 1456, 'adult ICU patients (prolonged propofol generally acceptable in adults at <4 mg/kg/h with monitoring)'))

kps.append(kp(3,3,t,dom,d,
    'What are the consequences of prolonged neuromuscular blockade in the ICU as highlighted by its historical overuse?',
    'Prolonged NMB is associated with critical illness myopathy (CIM), causing prolonged weakness and ventilator dependence.',
    'Immobility and continuous neuromuscular blockade deprive muscles of activity-dependent trophic stimuli, accelerating atrophy and myopathy.',
    'recall', 'Morgan & Mikhail', 2158, 'critical illness polyneuropathy (CIP) — axonal injury, often co-occurs with CIM)'))

kps.append(kp(3,4,t,dom,d,
    'What is the rationale and benefit of daily sedation interruption (sedation vacation) in mechanically ventilated ICU patients?',
    'Daily sedation interruption reduces total sedative exposure, shortens mechanical ventilation duration, and decreases ICU LOS.',
    'Accumulated sedative burden prolongs unconsciousness beyond clinical need; planned awakening trials allow neurologic assessment and earlier weaning.',
    'analyze', 'StatPearls: StatPearls   ICU Sedation', 1, ''))

kps.append(kp(3,5,t,dom,d,
    'Etomidate increases the amplitude of somatosensory evoked potentials but has what effect on auditory evoked potentials?',
    'Etomidate increases amplitude of SSEPs but INCREASES LATENCY and REDUCES AMPLITUDE of auditory evoked potentials.',
    'Differential effects on evoked potential modalities reflect etomidate-specific subcortical inhibition patterns, relevant when monitoring these signals intraoperatively.',
    'recall', 'Morgan & Mikhail', 290, 'ketamine (increases amplitude of SSEPs similar to etomidate but different cardiovascular profile)'))

kps.append(kp(3,6,t,dom,d,
    'Flumazenil reverses benzodiazepine sedation, but what limitation requires monitoring after reversal?',
    'Flumazenil has rapid hepatic clearance; repeat doses may be required after 1-2 hours to prevent re-sedation, especially with long-acting benzodiazepines.',
    'Benzodiazepine elimination half-lives often exceed flumazenil duration (0.7-1.3h); re-sedation is common without repeat dosing or vigilant monitoring.',
    'apply', 'Morgan & Mikhail', 467, ''))

kps.append(kp(3,7,t,dom,d,
    'Physical restraints for ICU patients with delirium were historically common. What is the current evidence-based concern?',
    'Restraints are considered inhumane and should only be used as a last resort for patient protection; they are associated with adverse consequences.',
    'Restraint-associated immobility accelerates delirium, causes injury, and does not address underlying agitation; non-pharmacologic de-escalation is preferred.',
    'analyze', 'Morgan & Mikhail', 2158, ''))

kps.append(kp(3,8,t,dom,d,
    'Why do infants and young children require larger weight-adjusted doses of propofol compared to adults?',
    'Larger volume of distribution and higher plasma clearance in infants/young children require higher weight-adjusted infusion rates (up to 250 mcg/kg/min for maintenance).',
    'Greater body water fraction and immature protein binding increase Vd; higher hepatic blood flow per body weight increases clearance in young children.',
    'recall', 'Morgan & Mikhail', 1456, ''))

# ══════════════════════════════════════════════════════════════════════════════
# TOPIC 4: Mechanical Ventilation: Physiology & Modes
# ══════════════════════════════════════════════════════════════════════════════
t = 'Mechanical Ventilation: Physiology & Modes'
dom = slice_data[4]['domain']
d = 'medicine'

kps.append(kp(4,1,t,dom,d,
    'What is the key disadvantage of conventional pressure control ventilation (PCV) compared to volume control?',
    'PCV does not guarantee tidal volume; VT varies with lung/chest wall compliance and patient effort, risking volutrauma or hypoventilation.',
    'In PCV the driving pressure is fixed; any change in respiratory system compliance directly alters the delivered volume.',
    'recall', 'Morgan & Mikhail', 2164, 'volume control (VCV) — guarantees VT but risks barotrauma if compliance changes'))

kps.append(kp(4,2,t,dom,d,
    'Volume-cycled ventilators terminate inspiration when a preset volume is delivered, but what safety mechanism prevents pulmonary barotrauma?',
    'A secondary pressure limit cycles the ventilator to expiration if inspiratory pressure exceeds the set limit even before target VT is reached.',
    'If compliance decreases abruptly (bronchospasm, pneumothorax), the pressure limit prevents dangerous over-distension by aborting inspiration.',
    'apply', 'Morgan & Mikhail', 2181, 'pressure-cycled ventilators (terminate on pressure; VT is variable and not guaranteed)'))

kps.append(kp(4,3,t,dom,d,
    'Time-cycled ventilators cycle to expiration after what event, and how is VT determined?',
    'Time-cycled ventilators cycle at a predetermined time interval; VT is the product of flow rate and inspiratory time.',
    'Fixed timing means VT depends on both set flow and the compliance/resistance of the respiratory system, making it variable.',
    'recall', 'Morgan & Mikhail', 2190, 'volume-cycled (terminates on preset volume, not time)'))

kps.append(kp(4,4,t,dom,d,
    'In IMV (intermittent mandatory ventilation) with pressure-controlled breaths, how does PC-IMV differ from PC-CMV?',
    'In PC-IMV: machine-initiated breaths are time-cycled and pressure-limited, but the patient can breathe spontaneously between mandatory breaths with unassisted flow.',
    'PC-IMV allows patient-initiated spontaneous breaths between mandatory breaths, supporting weaning by gradually reducing mandatory rate.',
    'recall', 'Morgan & Mikhail', 2186, 'AC (assist-control) — ALL patient-triggered breaths also receive full ventilator support'))

kps.append(kp(4,5,t,dom,d,
    'When peak airway pressure rises simultaneously with elevated PEEP and arterial hypotension occurs, what diagnosis must be urgently excluded?',
    'Tension pneumothorax; the hypotension is caused by high intrathoracic pressure impeding venous return.',
    'Increased PEEP elevates intrathoracic pressure; if combined with a new air leak, venous return is progressively impaired causing obstructive shock.',
    'apply', 'Miller/Baby Miller', 380, 'auto-PEEP (also raises peak pressure but without the immediate cardiovascular collapse of tension pneumothorax)'))

kps.append(kp(4,6,t,dom,d,
    'What does the rapid shallow breathing index (RSBI) threshold indicate about weaning success or failure?',
    'RSBI >105 breaths/min/L predicts weaning failure; values below this threshold are better at identifying patients likely to succeed.',
    'RSBI = RR/VT; high values indicate rapid shallow breathing pattern characteristic of respiratory muscle fatigue and inability to sustain spontaneous ventilation.',
    'apply', 'Miller/Baby Miller', 770, 'MIF (maximum inspiratory force) — tests muscle strength but RSBI tests pattern'))

kps.append(kp(4,7,t,dom,d,
    'What is the ETCO2-to-PaCO2 gradient, and what does its increase indicate?',
    'ETCO2 is almost always lower than PaCO2; an increased gradient (>5-10 mmHg) indicates increased alveolar dead space.',
    'Dead space ventilation (V/Q = infinity regions) dilutes alveolar CO2 before reaching the capnograph, widening the ETCO2-PaCO2 gradient.',
    'analyze', 'Miller/Baby Miller', 382, 'elevated ETCO2 (reflects increased PaCO2 or shunted CO2; gradient direction is reversed from dead space)'))

kps.append(kp(4,8,t,dom,d,
    'In neonates, why are both hyperoxia and hypoxia risk factors for retinopathy of prematurity (ROP) but not the primary causes?',
    'ROP risk increases primarily with low birth weight and complexity of comorbidities; hyperoxia and hypoxia are contributing risk factors, not the sole causes.',
    'ROP is a multifactorial vascular developmental disorder; oxygen exposure is one modifiable factor among many including prematurity and infection.',
    'analyze', 'Morgan & Mikhail', 2164, ''))

# ══════════════════════════════════════════════════════════════════════════════
# TOPIC 5: Neurocritical Care Essentials
# ══════════════════════════════════════════════════════════════════════════════
t = 'Neurocritical Care Essentials'
dom = slice_data[5]['domain']
d = 'medicine'

kps.append(kp(5,1,t,dom,d,
    'What is the neurological significance of targeted temperature management (TTM) for interpretation of prognostic markers after cardiac arrest?',
    'TTM alters the timeframe for neurological recovery and changes the interpretation of standard prognostic markers; prognostication should be deferred accordingly.',
    'Hypothermia slows metabolism and drug clearance, delaying evolution of EEG findings, pupillary responses, and clinical examination — all standard prognostic tools.',
    'analyze', 'MGH Housestaff Manual', 204, 'early neuroprognostication (unreliable within 72h post-cardiac arrest without TTM-adjusted timelines)'))

kps.append(kp(5,2,t,dom,d,
    'After aneurysmal subarachnoid hemorrhage (aSAH), what drug is used to prevent vasospasm, and for how long?',
    'Nimodipine (oral calcium channel blocker) for up to 14 days; however, clazosentan (endothelin antagonist) showed no mortality or outcome benefit in subsequent studies.',
    'Nimodipine reduces cerebral vasospasm-related ischemia; its benefit is outcome-based despite variable angiographic vasospasm reduction.',
    'recall', 'StatPearls: StatPearls   Subarachnoid Hemorrhage (SAH)', 10, 'clazosentan (reduces angiographic vasospasm but does not improve clinical outcomes)'))

kps.append(kp(5,3,t,dom,d,
    'Per NCS/SCCM 2015 guidelines, how should antithrombotic agents be managed after aneurysmal SAH?',
    'All antithrombotic agents should be discontinued and anticoagulation reversed until the aneurysm is definitively treated.',
    'Ongoing anticoagulation after SAH dramatically increases risk of re-bleeding, which carries 40-80% mortality.',
    'apply', 'StatPearls: StatPearls   Subarachnoid Hemorrhage (SAH)', 10, ''))

kps.append(kp(5,4,t,dom,d,
    'Prone positioning and lung recruitment maneuvers for refractory hypoxemia can cause what cardiac complication?',
    'Both interventions can cause hemodynamic compromise by compressing the heart/great vessels and increasing right ventricular afterload.',
    'Colocation of heart and lungs in the thorax means that lung recruitment elevates intrathoracic pressure, reducing venous return and compressing cardiac structures.',
    'analyze', 'Miller/Baby Miller', 92, ''))

kps.append(kp(5,5,t,dom,d,
    'For right-to-left cardiac shunts (e.g., congenital heart disease), what ventilatory strategy lowers pulmonary vascular resistance and reduces shunting?',
    'Hyperventilation (hypocapnia) with 100% oxygen effectively lowers PVR; avoid acidosis, hypercapnia, hypoxia, sympathetic activation, and high mean airway pressures.',
    'Hypocapnia causes pulmonary vasoconstriction relief; hypoxia and acidosis are potent pulmonary vasoconstrictors that worsen right-to-left shunting.',
    'apply', 'Morgan & Mikhail', 708, 'left-to-right shunts (benefit from systemic vasodilation and increases in PVR to reduce shunt fraction)'))

kps.append(kp(5,6,t,dom,d,
    'Intracranial hypertension is defined as sustained ICP above what threshold?',
    'ICP >15 mmHg sustained; management targets cerebral perfusion pressure (CPP = MAP - ICP).',
    'Normal ICP is 5-15 mmHg; values above 15 reduce CPP and cerebral blood flow, risking ischemia and herniation.',
    'recall', 'Morgan & Mikhail', 967, ''))

kps.append(kp(5,7,t,dom,d,
    'Statin therapy for aSAH vasospasm prevention has what evidence-based status?',
    'Statins demonstrate no benefit in reducing vasospasm or improving short-term or long-term outcomes in aSAH; routine initiation is not recommended.',
    'Early clinical promise from small trials was not replicated in adequately powered studies; continuing pre-existing statins is reasonable but de-novo initiation is not evidence-based.',
    'recall', 'StatPearls: StatPearls   Subarachnoid Hemorrhage (SAH)', 10, 'nimodipine (does have evidence for outcome benefit in aSAH)'))

kps.append(kp(5,8,t,dom,d,
    'In anesthesia for neurosurgical procedures with increased ICP, what induction approach blunts the ICP response to laryngoscopy?',
    'Propofol 1.5-3 mg/kg prior to rapid-onset NMB reduces ICP elevation at intubation; etomidate also blunts ICP while maintaining cerebral perfusion pressure.',
    'Laryngoscopy stimulates sympathetic reflex; prior propofol/etomidate reduces cerebral metabolic rate and blunts the cerebrovascular response.',
    'apply', 'Morgan & Mikhail', 982, 'ketamine (avoid in raised ICP; increases cerebral metabolic rate and ICP)'))

# ══════════════════════════════════════════════════════════════════════════════
# TOPIC 6: Pneumonia: Special Populations & Organisms
# ══════════════════════════════════════════════════════════════════════════════
t = 'Pneumonia: Special Populations & Organisms'
dom = slice_data[6]['domain']
d = 'medicine'

kps.append(kp(6,1,t,dom,d,
    'What proportion of hospital-acquired S. aureus pneumonia cases are due to MRSA versus MSSA?',
    'Approximately 51% MRSA and 49% MSSA in hospital-acquired pneumonia; in CAP, S. aureus causes ~3% of cases.',
    'Hospital selection pressure favors MRSA; community-acquired S. aureus pneumonia is less common and more often MSSA.',
    'recall', 'StatPearls', 3, ''))

kps.append(kp(6,2,t,dom,d,
    'What is the nasal swab sensitivity for predicting MRSA pneumonia, and how does it affect antibiotic decisions?',
    'Nasal swab has high sensitivity (96.1-99.2%) for MRSA; a negative nasal swab can de-escalate empiric MRSA coverage.',
    'MRSA nasal colonization predicts MRSA pneumonia with high sensitivity; negative swab substantially lowers the probability of MRSA as the pathogen.',
    'apply', 'StatPearls: StatPearls   Pneumonia  Special Populations & Organisms', 5, 'positive swab (high negative predictive value is the clinical utility; positive is less specific)'))

kps.append(kp(6,3,t,dom,d,
    'The HCAP (healthcare-associated pneumonia) category was previously used for broader empiric antibiotic selection. What do 2016 IDSA/ATS guidelines recommend instead?',
    'HCAP is no longer recommended as a category; empiric extended-spectrum therapy should be based on local culture data and validated risk factor scores, not HCAP classification alone.',
    'HCAP over-predicted resistant organisms leading to unnecessary broad-spectrum antibiotic overuse; evidence-based risk stratification is now preferred.',
    'analyze', 'Society Guideline: Guideline   IDSA ATS 2019 CAP Executive Summary', 9, 'HAP/VAP (still valid; defined by timing in hospital, not healthcare exposure)'))

kps.append(kp(6,4,t,dom,d,
    'In sepsis from lower respiratory infection, what are the most common causative bacteria for CAP versus HAP/VAP?',
    'CAP: S. pneumoniae, H. influenzae. HAP/VAP: Pseudomonas aeruginosa, MRSA (and other resistant gram-negatives).',
    'Hospital-acquired organisms reflect the local ICU flora shaped by antibiotic selection pressure; community organisms are typically drug-susceptible.',
    'recall', 'Curated Units', 0, ''))

kps.append(kp(6,5,t,dom,d,
    'Staphylococcal pneumonia has a broad and nonspecific clinical presentation. Which organisms must be considered in the differential diagnosis?',
    'S. pneumoniae, H. influenzae, Mycoplasma, Chlamydia, Legionella, gram-negative bacilli, Group A Streptococcus, anaerobes.',
    'Overlapping symptoms (fever, cough, infiltrate) require culture-driven therapy; empiric coverage must span the likely organisms pending identification.',
    'recall', 'StatPearls', 6, ''))

kps.append(kp(6,6,t,dom,d,
    'A patient with penicillin allergy requires surgical antibiotic prophylaxis. What alternatives are recommended?',
    'Clindamycin or vancomycin for patients with penicillin allergies or specific risk factors for cephalosporin cross-reactivity.',
    'Beta-lactam cross-reactivity with cephalosporins is low (~1%) but clinically important; clindamycin or vancomycin provide non-beta-lactam gram-positive coverage.',
    'apply', 'StatPearls', 17, 'cephalosporins (may cross-react in severe penicillin allergy; avoid if history of anaphylaxis to penicillin)'))

kps.append(kp(6,7,t,dom,d,
    'What typical antibiotic duration is recommended for CAP versus HAP/VAP caused by resistant organisms?',
    'CAP: typically 7-10 days. HAP/VAP: 8 days shown equivalent to 15 days for most organisms; shorter courses favored to limit resistance.',
    'Evidence from Chastre et al. (JAMA 2003) showed 8 vs 15 days non-inferior for VAP; shorter courses reduce selection pressure.',
    'recall', 'Marino ICU Book', 563, ''))

kps.append(kp(6,8,t,dom,d,
    'Late ICU admission (>24h after ED presentation) in community-acquired pneumonia is associated with what outcome?',
    'Late ICU admission for CAP is associated with higher mortality.',
    'Delayed escalation of care allows pneumonia to progress to ARDS and septic shock without early ICU-level monitoring and intervention.',
    'analyze', 'Society Guideline: Guideline   IDSA ATS 2019 CAP Executive Summary', 12, ''))

# ══════════════════════════════════════════════════════════════════════════════
# TOPIC 7: RA: treatment & treat-to-target strategy
# ══════════════════════════════════════════════════════════════════════════════
t = 'RA: treatment & treat-to-target strategy'
dom = slice_data[7]['domain']
d = 'medicine'

kps.append(kp(7,1,t,dom,d,
    'SGLT2 inhibitors are now recommended by ADA guidelines as first-line agents for which subset of diabetic patients with cardiovascular disease?',
    'SGLT2 inhibitors are first-line for hyperglycemia in patients with diabetes AND heart failure or high risk of HF.',
    'SGLT2 inhibitors reduce HF hospitalization and cardiovascular events in diabetic patients with or at high risk of HF, beyond glucose lowering.',
    'apply', 'Society Guideline: Guideline   ACC AHA 2022 Heart Failure', 92, 'metformin (first-line for most T2DM but no specific HF outcome data; SGLT2i preferred when HF present)'))

kps.append(kp(7,2,t,dom,d,
    'In patients with atrial fibrillation and heart failure, what score guides anticoagulation decisions?',
    'CHA2DS2-VASc score guides AF anticoagulation; long-term warfarin is well-established for stroke prevention, with randomized trial evidence for reduced embolic rates and mortality.',
    'AF doubles stroke risk; CHA2DS2-VASc stratifies additional comorbidities to determine net benefit of anticoagulation versus bleeding risk.',
    'apply', 'Society Guideline: Guideline   ACC AHA 2022 Heart Failure', 93, ''))

kps.append(kp(7,3,t,dom,d,
    'Why is low-dose dopamine not recommended for renal protection in AKI or oliguric PACU patients?',
    'Although low-dose dopamine can increase urine output, there is NO evidence it is renoprotective; it is not a recommended strategy for prevention or treatment of AKI.',
    'Renal-dose dopamine increases GFR by vasodilation but does not prevent tubular injury; clinical trials showed no improvement in AKI outcomes.',
    'recall', 'Miller/Baby Miller', 732, 'norepinephrine (vasopressor of choice in septic AKI; maintains MAP and renal perfusion pressure)'))

kps.append(kp(7,4,t,dom,d,
    'What urinary catheter issue should be excluded first when evaluating oliguria in the PACU?',
    'Urinary catheter obstruction or dislodgment — easily remedied and often overlooked before pursuing more invasive workup.',
    'Mechanical obstruction of urine drainage is a common, reversible cause of apparent oliguria; confirming catheter patency is the first diagnostic step.',
    'apply', 'Miller/Baby Miller', 732, 'hypovolemia (second most common cause; manage after confirming catheter patency)'))

kps.append(kp(7,5,t,dom,d,
    'Routine assessment of patient-reported health status in heart failure can facilitate what management advantage beyond identifying symptoms?',
    'Routine health status assessment can identify patients needing additional interventions (e.g., diuretic escalation) and improves shared decision-making about prognosis and goals of care.',
    'Subjective symptom burden often predicts decompensation risk; proactive monitoring enables earlier escalation before hospitalization.',
    'analyze', 'Society Guideline: Guideline   ACC AHA 2022 Heart Failure', 108, ''))

kps.append(kp(7,6,t,dom,d,
    'When should a patient with cirrhosis be referred for liver transplant evaluation?',
    'Refer when MELD score >10 (to allow time for evaluation); strong indication when MELD >=15 or complications develop (ascites, variceal bleed, hepatic encephalopathy, HRS).',
    'MELD score reflects 3-month transplant-free mortality; early referral at MELD >10 allows evaluation before decompensation reduces operative candidacy.',
    'apply', 'MGH Housestaff Manual', 98, 'MELD-Na (incorporates sodium as a marker of cirrhosis severity; used for waitlist prioritization)'))

kps.append(kp(7,7,t,dom,d,
    'What additional contraception guidance applies to patients on hormonal contraceptives who receive sugammadex?',
    'Patients using hormonal contraceptives must use an additional non-hormonal contraceptive method for 7 days after sugammadex.',
    'Sugammadex binds and eliminates rocuronium but also affects the metabolism/efficacy of progestin-containing hormonal contraceptives.',
    'apply', 'Stanford CA-1', 40, ''))

kps.append(kp(7,8,t,dom,d,
    'What is the ADA screening recommendation for type 2 diabetes in average-risk adults?',
    'Begin screening at age 35; repeat every 3 years if normal, every year if pre-diabetes; screen earlier if BMI >=25 plus risk factors.',
    'Earlier and more frequent testing in high-risk individuals (family history, obesity, prior gestational DM, non-white ethnicity) identifies pre-diabetes when lifestyle intervention is most effective.',
    'recall', 'MGH Housestaff Manual', 181, ''))

# ══════════════════════════════════════════════════════════════════════════════
# TOPIC 8: Rheumatoid arthritis: pathogenesis & diagnosis
# ══════════════════════════════════════════════════════════════════════════════
t = 'Rheumatoid arthritis: pathogenesis & diagnosis'
dom = slice_data[8]['domain']
d = 'medicine'

# Chunks mostly off-topic (primary ovarian insufficiency). Extract what is relevant.
kps.append(kp(8,1,t,dom,d,
    'In psoriatic arthritis, in approximately what percentage of patients does arthritis precede skin manifestations, making diagnosis more difficult?',
    'Approximately 17% of psoriatic arthritis patients develop arthritis BEFORE skin manifestations, complicating early diagnosis.',
    'Absence of psoriatic skin findings shifts the differential toward other seronegative arthritides, requiring careful family history and examination for subtle skin/nail changes.',
    'recall', 'StatPearls: StatPearls   Psoriatic arthritis', 4, 'rheumatoid arthritis (symmetric, small joint involvement; RF/anti-CCP positive in most cases)'))

kps.append(kp(8,2,t,dom,d,
    'Rheumatoid arthritis shares overlapping musculoskeletal symptoms with which other systemic autoimmune diseases that may complicate diagnosis?',
    'SLE, systemic sclerosis, psoriatic arthritis, Sjogren syndrome, and polymyositis/dermatomyositis can all present with overlapping joint and constitutional symptoms.',
    'Undifferentiated connective tissue disease (UCTD) may evolve into any of these defined entities; serologic panels (ANA, RF, anti-CCP, anti-dsDNA) help distinguish.',
    'analyze', 'StatPearls', 3, 'undifferentiated CTD (does not yet meet full classification criteria for any defined disease)'))

kps.append(kp(8,3,t,dom,d,
    'What imaging modality helps differentiate undifferentiated connective tissue disease from Sjogren syndrome at the salivary glands?',
    'Salivary gland ultrasonography was found to be a good test for differentiating undifferentiated CTD from Sjogren syndrome.',
    'Sjogren syndrome causes characteristic echostructural changes in parotid and submandibular glands detectable by ultrasound, even before clinical sicca symptoms are prominent.',
    'apply', 'StatPearls', 4, 'labial gland biopsy (gold standard for Sjogren diagnosis but more invasive)'))

kps.append(kp(8,4,t,dom,d,
    'Annual incidence of psoriatic arthritis among patients with existing psoriasis is approximately how much, and cumulative 10-year prevalence?',
    'Annual incidence ~1.9-2.7 per 100 psoriasis patients; cumulative prevalence ~3.1% at 10 years.',
    'Not all psoriasis patients develop joint involvement; recognizing the minority who do requires regular musculoskeletal screening at dermatology visits.',
    'recall', 'StatPearls: StatPearls   Psoriatic arthritis', 4, ''))

kps.append(kp(8,5,t,dom,d,
    'The 2018 ACR/NPF psoriatic arthritis guidelines use what classification criteria tool?',
    'The Classification Criteria for Psoriatic Arthritis (CASPAR) guides accurate diagnosis along with the 2018 ACR/NPF treatment guidelines.',
    'CASPAR criteria incorporate psoriasis, psoriatic nail changes, negative RF, dactylitis, and periarticular new bone formation on imaging.',
    'recall', 'StatPearls: StatPearls   Psoriatic arthritis', 2, 'ACR 2010 RA criteria (different criteria for RA; requires RF/anti-CCP serology)'))

kps.append(kp(8,6,t,dom,d,
    'Primary ovarian insufficiency (POI) is diagnosed in women under what age, based on what laboratory findings?',
    'Women <40 years; diagnosed with amenorrhea >=4-6 months, low estradiol, and elevated FSH.',
    'POI reflects depletion of ovarian follicles before natural menopause age; elevated FSH reflects loss of negative feedback from estrogen and inhibin.',
    'recall', 'StatPearls: StatPearls   Rheumatoid arthritis  pathogenesis & diagnosis', 1, 'premature menopause (same entity; now termed POI to reflect intermittent function possible)'))

kps.append(kp(8,7,t,dom,d,
    'In women with POI post-hysterectomy, what hormonal replacement strategy is appropriate?',
    'Estrogen-only therapy (no progestogen needed without a uterus); topical estrogen for vaginal atrophy symptoms.',
    'Progestogen is added to estrogen therapy only to protect the endometrium in women with an intact uterus; post-hysterectomy patients do not require it.',
    'apply', 'StatPearls: StatPearls   Rheumatoid arthritis  pathogenesis & diagnosis', 7, 'combined estrogen + progestogen (appropriate for women with intact uterus to prevent endometrial hyperplasia)'))

kps.append(kp(8,8,t,dom,d,
    'Arthritis manifestations coincide with psoriatic skin disease at initial presentation in approximately what percentage of patients?',
    'Approximately 15% of psoriatic arthritis patients have simultaneous onset of skin and joint disease.',
    'The variable temporal relationship between skin and joint involvement in psoriatic disease complicates classification; concurrent onset occurs in a minority.',
    'recall', 'StatPearls: StatPearls   Psoriatic arthritis', 4, ''))

# ══════════════════════════════════════════════════════════════════════════════
# TOPIC 9: Sjogren syndrome
# ══════════════════════════════════════════════════════════════════════════════
t = 'Sjogren syndrome'
dom = slice_data[9]['domain']
d = 'medicine'

kps.append(kp(9,1,t,dom,d,
    'Sjogren syndrome can be secondary to which other systemic autoimmune diseases?',
    'Secondary Sjogren syndrome occurs in association with SLE, rheumatoid arthritis, and systemic sclerosis (secondary to salivary gland inflammatory infiltrates or fibrosis).',
    'Lymphocytic infiltration of exocrine glands is the common pathological mechanism; it may occur as part of the broader autoimmune tissue injury in connective tissue diseases.',
    'recall', 'StatPearls: StatPearls   Systemic sclerosis (scleroderma)', 9, 'primary Sjogren syndrome (no other CTD; sicca symptoms are the defining presentation)'))

kps.append(kp(9,2,t,dom,d,
    'Anti-Ro/SSA antibodies in Sjogren syndrome are associated with what characteristic skin manifestation when drug-induced lupus is present?',
    'Anti-Ro/SSA antibodies are strongly associated with photodistributed annular or psoriasiform rashes in subacute cutaneous lupus erythematosus.',
    'Anti-Ro/SSA antibodies define a subset of lupus with photosensitive rash; they are shared between Sjogren syndrome and SLE, reflecting overlapping B-cell autoimmunity.',
    'recall', 'StatPearls: StatPearls   Drug induced lupus', 5, 'anti-dsDNA antibodies (specific for SLE; not typical in Sjogren syndrome)'))

kps.append(kp(9,3,t,dom,d,
    'Dry mouth in systemic sclerosis often arises from what two mechanisms that mimic Sjogren syndrome?',
    'Salivary gland fibrosis secondary to systemic sclerosis OR secondary Sjogren syndrome from lymphocytic infiltrates — both can occur in the same patient.',
    'Systemic sclerosis can cause salivary dysfunction through direct fibrosis or by triggering a secondary autoimmune lymphocytic infiltration resembling primary Sjogren.',
    'analyze', 'StatPearls: StatPearls   Systemic sclerosis (scleroderma)', 7, 'primary Sjogren syndrome (autoimmune without underlying connective tissue disease)'))

kps.append(kp(9,4,t,dom,d,
    'Salivary gland ultrasonography provides what diagnostic advantage in evaluating suspected Sjogren syndrome?',
    'Salivary gland ultrasound is a good noninvasive test for differentiating undifferentiated CTD from Sjogren syndrome, detecting characteristic echostructural changes.',
    'Glandular inhomogeneity, hypoechoic areas, and parenchymal changes on ultrasound correlate with lymphocytic infiltration and predict labial biopsy findings.',
    'apply', 'StatPearls', 4, 'Schirmer test (measures tear production; assesses lacrimal gland function, not salivary)'))

kps.append(kp(9,5,t,dom,d,
    'Ianalumab, a dual-action monoclonal antibody targeting B lymphocytes expressing BAFF, has shown effectiveness in which autoimmune condition?',
    'Ianalumab has shown effectiveness in Sjogren syndrome.',
    'BAFF (B-cell activating factor) is overexpressed in Sjogren syndrome and drives B-cell survival and autoantibody production; targeting BAFF and BAFF-R reduces disease activity.',
    'recall', 'StatPearls: StatPearls   Lupus nephritis', 15, ''))

kps.append(kp(9,6,t,dom,d,
    'Sjogren syndrome anti-Ro/SSA antibodies also appear in what other autoimmune conditions, suggesting shared B-cell autoimmunity?',
    'Anti-Ro/SSA antibodies appear in SLE, drug-induced lupus, and systemic sclerosis — reflecting overlapping autoimmune epitope targeting across CTDs.',
    'Shared autoantigens between conditions explain serological overlap; anti-Ro/SSA positivity requires clinical correlation with full disease criteria.',
    'analyze', 'StatPearls: StatPearls   Drug induced lupus', 8, ''))

kps.append(kp(9,7,t,dom,d,
    'Primary biliary cirrhosis has a recognized association with which systemic autoimmune diseases?',
    'Primary biliary cirrhosis (now primary biliary cholangitis) is associated with secondary Sjogren syndrome and systemic sclerosis.',
    'Bile duct-targeting autoimmunity in PBC shares pathogenetic mechanisms with exocrine gland autoimmunity in Sjogren syndrome; AMA antibodies are the key diagnostic marker.',
    'recall', 'StatPearls: StatPearls   Systemic sclerosis (scleroderma)', 12, 'autoimmune hepatitis (ANA/SMA positive; more hepatocellular than cholestatic pattern)'))

kps.append(script(t, d,
    'Middle-aged women predominantly; association with other CTDs (SLE, RA, SSc); genetic (HLA-DR3).',
    'Lymphocytic infiltration of exocrine glands (lacrimal, salivary) destroys secretory acini; B-cell hyperactivation produces anti-Ro/SSA and anti-La/SSB autoantibodies.',
    'Insidious onset over years; sicca symptoms (dry eyes, dry mouth) appear gradually; extraglandular manifestations (arthralgia, interstitial nephritis, neuropathy) develop later.',
    'Keratoconjunctivitis sicca, xerostomia, parotid enlargement, fatigue; anti-Ro/SSA and anti-La/SSB positive.',
    'Increased B-cell lymphoma risk (~44x); extraglandular organ involvement missed; neonatal lupus if mother anti-Ro positive (fetal heart block risk).'))

# ══════════════════════════════════════════════════════════════════════════════
# TOPIC 10: Acute Kidney Injury in the ICU
# ══════════════════════════════════════════════════════════════════════════════
t = 'Acute Kidney Injury in the ICU'
dom = slice_data[10]['domain']
d = 'anesthesia'

kps.append(kp(10,1,t,dom,d,
    'In hepatorenal syndrome (HRS), terlipressin is initiated at what dose, and escalated how if response is inadequate?',
    'Terlipressin: 1 mg IV every 6 hours; escalate to 2 mg every 6 hours at 48-72 hours if creatinine reduction is <20-30%.',
    'Terlipressin is a vasopressin analogue that reduces splanchnic vasodilation and increases renal perfusion pressure in cirrhotic patients with HRS.',
    'apply', 'StatPearls: StatPearls   Hepatorenal Syndrome (HRS)', 8, 'albumin alone (insufficient for HRS; must combine with vasoconstrictor)'))

kps.append(kp(10,2,t,dom,d,
    'Continuous terlipressin infusion (starting 2 mg/day) compared to intermittent bolus dosing shows what clinical advantage?',
    'Continuous infusion demonstrates equivalent efficacy with reduced adverse effects compared to intermittent bolus dosing.',
    'Continuous infusion avoids peak plasma levels that cause vasoconstriction-related side effects (myocardial ischemia, bowel ischemia), maintaining therapeutic levels more smoothly.',
    'apply', 'StatPearls: StatPearls   Hepatorenal Syndrome (HRS)', 8, ''))

kps.append(kp(10,3,t,dom,d,
    'In AKI management in the PACU, what is the urine output threshold that defines oliguria and triggers evaluation?',
    'Urine output <0.5 mL/kg/hr defines oliguria; first step is to rule out catheter obstruction/dislodgment before further workup.',
    'Post-surgical oliguria has multiple causes (hypovolemia, obstruction, AKI); a systematic approach starting with the simplest reversible cause prevents unnecessary interventions.',
    'apply', 'Miller/Baby Miller', 732, ''))

kps.append(kp(10,4,t,dom,d,
    'In Budd-Chiari syndrome, which features are associated with particularly poor prognosis?',
    'Involvement of all 3 hepatic veins or portal vein, older age, high Child-Pugh score, and chronic disease at presentation carry poor prognosis.',
    'Extensive venous occlusion increases portal hypertension and hepatic congestion; chronic presentation implies established fibrosis with less reversibility.',
    'recall', 'StatPearls: StatPearls   Budd Chiari Syndrome', 6, 'acute Budd-Chiari (sudden thrombosis; potentially reversible with anticoagulation or TIPS)'))

kps.append(kp(10,5,t,dom,d,
    'Phosphate homeostasis significantly influences recovery outcomes in acute liver failure. What phosphate pattern predicts improved versus poor recovery?',
    'Hypophosphatemia (<2.5 mg/dL) correlates with improved recovery; severe hyperphosphatemia (>5 mg/dL) precludes neurological recovery.',
    'Phosphate is consumed by regenerating hepatocytes; paradoxically, very low phosphate indicates active hepatic regeneration, while persistent high phosphate reflects massive necrosis.',
    'analyze', 'StatPearls: StatPearls   Acute Liver Failure (ALF)', 12, ''))

kps.append(kp(10,6,t,dom,d,
    'GFR estimation using combined creatinine and cystatin C equations provides what advantage over creatinine-only formulas?',
    'Combined creatinine/cystatin C provides greater accuracy when muscle wasting or loss affects creatinine-based GFR estimation or when high GFR accuracy is required (e.g., drug dosing).',
    'Cystatin C is not affected by muscle mass; its addition corrects creatinine-based underestimation in sarcopenic or malnourished ICU patients.',
    'apply', 'Society Guideline: Guideline   KDIGO 2024 CKD', 63, 'creatinine-only GFR estimation (underestimates GFR in muscle-wasted patients; overestimates in obesity)'))

kps.append(kp(10,7,t,dom,d,
    'Norepinephrine in severe septic shock affects renal function through what mechanism?',
    'Norepinephrine restores MAP (via alpha-1 vasoconstriction) and thus improves renal perfusion pressure, with reported beneficial effects on renal function in severe septic shock.',
    'In sepsis, splanchnic vasodilation causes relative renal ischemia despite normal or elevated cardiac output; norepinephrine corrects systemic vasodilation to restore filtration pressure.',
    'analyze', 'Society Guideline: Guideline   KDIGO 2012 AKI', 129, 'dopamine at low doses (urine output increases but no renoprotection proven)'))

kps.append(kp(10,8,t,dom,d,
    'AN-69 hemodialysis membrane reactions are pH-dependent. What does this imply for clinical management?',
    'AN-69 membrane reactions (bradykinin release) are pH-dependent and preventable by appropriate buffer/pH management of the circuit.',
    'Low pH dialysate increases bradykinin generation from AN-69 membranes, causing hypotension; adequate buffering reduces this complication.',
    'apply', 'Society Guideline: Guideline   KDIGO 2012 AKI', 140, ''))

kps.append(script(t, d,
    'ICU patients with sepsis, major surgery, nephrotoxin exposure, contrast, rhabdomyolysis, or pre-existing CKD.',
    'Renal hypoperfusion (ischemic) or direct tubular toxicity -> tubular cell death, intraluminal casts, decreased GFR; in sepsis: microvascular dysfunction even with preserved flow.',
    'Often develops within 48-72h of ICU admission; follows a spectrum from mild (KDIGO stage 1) to anuric (stage 3) requiring RRT.',
    'Rising creatinine, oliguria (<0.5 mL/kg/hr), hyperkalemia, metabolic acidosis, fluid overload.',
    'Volume overload, hyperkalemia-induced arrhythmia, uremia; dialysis delay in HRS increases mortality; missed catheter obstruction leads to unnecessary workup.'))

print('Topics 0-10 KP count:', len(kps))
