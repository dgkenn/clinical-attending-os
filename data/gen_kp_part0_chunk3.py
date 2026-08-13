import json

kps = []

# ── 22: Basic apatite (hydroxyapatite) deposition disease ────────────────────
# Chunks mostly off-topic (echo hemodynamics, gout DDx, AKI, DM).
# Usable: gout DDx mentions basic calcium phosphate; CPPD criteria mention basic bloodwork
kps += [
  {"id":"bapd-1","topic":"Basic apatite (hydroxyapatite) deposition disease","domain":"Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)","discipline":"medicine",
   "stem":"Basic calcium phosphate (apatite) deposition disease is on the differential diagnosis of which acute joint condition?",
   "answer":"Acute gout flare — basic calcium phosphate crystal disease and CPPD must be distinguished from gout and from septic arthritis.",
   "rationale":"Crystal arthropathies overlap clinically; definitive diagnosis requires synovial fluid analysis with polarised microscopy to identify crystal type.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Gout  acute management","page":23}],"confusable_with":"Gout (monosodium urate crystals, negatively birefringent), CPPD (calcium pyrophosphate, positively birefringent)"},
  {"id":"bapd-2","topic":"Basic apatite (hydroxyapatite) deposition disease","domain":"Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)","discipline":"medicine",
   "stem":"What basic blood tests are included in the workup of crystal deposition diseases including apatite and CPPD?",
   "answer":"Basic metabolic panel (calcium, magnesium, phosphate), PTH, iron studies, TSH, and uric acid.",
   "rationale":"Secondary causes of crystal deposition include hyperparathyroidism (elevated calcium/PTH), haemochromatosis (iron studies), hypothyroidism (TSH), and hyperuricaemia.",
   "bloom":"recall","source":[{"book":"StatPearls","page":5}],"confusable_with":""},
  {"id":"bapd-3","topic":"Basic apatite (hydroxyapatite) deposition disease","domain":"Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)","discipline":"medicine",
   "stem":"Crystal identification in synovial fluid distinguishes which crystal arthropathies?",
   "answer":"Gout (monosodium urate, needle-shaped, negatively birefringent), CPPD (calcium pyrophosphate, rhomboid/blunt-ended, positively birefringent), apatite (not birefringent — identified by special staining/electron microscopy).",
   "rationale":"Polarised microscopy is the standard initial test; apatite crystals are too small for standard polarised microscopy and require Alizarin Red S or electron microscopy.",
   "bloom":"analyze","source":[{"book":"StatPearls","page":5}],"confusable_with":""}
]

# ── 23: Beta-Blocker & CCB Toxicity ──────────────────────────────────────────
kps += [
  {"id":"bb-ccb-tox-1","topic":"Beta-Blocker & Calcium Channel Blocker Toxicity","domain":"Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)","discipline":"medicine",
   "stem":"What is the key metabolic difference between beta-blocker and CCB toxicity in adult patients?",
   "answer":"CCB toxicity is more likely to cause hyperglycemia; beta-blockers are less likely to cause hyperglycemia.",
   "rationale":"CCBs block pancreatic beta-cell calcium channels, impairing insulin secretion and causing hyperglycaemia; beta-blockers do not have this effect.",
   "bloom":"analyze","source":[{"book":"StatPearls: StatPearls   Beta Blocker & Calcium Channel Blocker Toxicity","page":7}],"confusable_with":"Beta-blocker toxicity (may cause hypoglycaemia by masking symptoms)"},
  {"id":"bb-ccb-tox-2","topic":"Beta-Blocker & Calcium Channel Blocker Toxicity","domain":"Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)","discipline":"medicine",
   "stem":"Why are conventional decontamination measures (haemodialysis, urinary alkalinisation) ineffective in CCB overdose?",
   "answer":"CCBs have large volume of distribution and are lipophilic, making extracorporeal removal ineffective.",
   "rationale":"High lipophilicity and extensive tissue distribution mean that very little drug is in the blood at any time; whole bowel irrigation is the mainstay for extended-release preparations.",
   "bloom":"analyze","source":[{"book":"StatPearls: StatPearls   Beta Blocker & Calcium Channel Blocker Toxicity","page":4}],"confusable_with":"Dialysable drugs (lithium, salicylates — small Vd, low protein binding)"},
  {"id":"bb-ccb-tox-3","topic":"Beta-Blocker & Calcium Channel Blocker Toxicity","domain":"Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)","discipline":"medicine",
   "stem":"Hyperinsulinemic euglycemia (HIE) therapy is used in severe CCB toxicity. What is the proposed mechanism?",
   "answer":"CCB toxicity shifts myocardial substrate utilisation away from fatty acids toward glucose; high-dose insulin provides glucose as an energy substrate and has direct positive inotropic effects.",
   "rationale":"Calcium channel blockade impairs myocardial fatty acid oxidation; high-dose insulin (with glucose to prevent hypoglycaemia) supports myocardial metabolism.",
   "bloom":"analyze","source":[{"book":"StatPearls: StatPearls   Beta Blocker & Calcium Channel Blocker Toxicity","page":5}],"confusable_with":""},
  {"id":"bb-ccb-tox-4","topic":"Beta-Blocker & Calcium Channel Blocker Toxicity","domain":"Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)","discipline":"medicine",
   "stem":"Why is IV calcium theoretically concerning in digoxin toxicity when used to treat CCB overdose-related hyperkalaemia?",
   "answer":"Calcium potentiates digoxin's positive inotropic effect, theoretically causing 'stone heart' (irreversible diastolic contracture); however, multiple studies have not confirmed this risk in clinical practice.",
   "rationale":"The 'stone heart' theory holds that excess intracellular calcium combined with digoxin's Na+/K+-ATPase inhibition causes irreversible tetanic contraction; clinical evidence is reassuring.",
   "bloom":"analyze","source":[{"book":"StatPearls: StatPearls   Digoxin Toxicity","page":8}],"confusable_with":""},
  {"id":"bb-ccb-tox-5","topic":"Beta-Blocker & Calcium Channel Blocker Toxicity","domain":"Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)","discipline":"medicine",
   "stem":"In refractory CCB shock not responding to initial treatment, what mechanical/salvage option should be considered?",
   "answer":"Veno-arterial ECMO (VA-ECMO).",
   "rationale":"VA-ECMO provides mechanical circulatory support and allows time for drug elimination and myocardial recovery in CCB-induced refractory cardiogenic shock.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Beta Blocker & Calcium Channel Blocker Toxicity","page":7}],"confusable_with":""},
  {"_type":"confusable_pair","topic_a":"Beta-blocker toxicity","topic_b":"Calcium channel blocker toxicity","discriminator":"Both: bradycardia + hypotension. CCB: hyperglycaemia (blocks pancreatic insulin), preserved/high cardiac output in DHP-CCBs. BB: normoglycaemia or hypoglycaemia, bronchospasm (beta-2 blockade)."}
]

# ── 24: Beta-lactam allergy evaluation ────────────────────────────────────────
kps += [
  {"id":"betalactam-allergy-1","topic":"Beta-lactam allergy evaluation & penicillin skin testing","domain":"Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)","discipline":"medicine",
   "stem":"What is the negative predictive value of penicillin skin testing and what does a negative result mean clinically?",
   "answer":"NPV ~95%; a negative skin test makes IgE-mediated penicillin allergy unlikely, allowing administration in most patients.",
   "rationale":"Penicillin skin testing detects drug-specific IgE antibodies; a negative result reduces (but does not eliminate) risk of immediate hypersensitivity.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":192}],"confusable_with":"Graded challenge (test dose for low-suspicion reactions)"},
  {"id":"betalactam-allergy-2","topic":"Beta-lactam allergy evaluation & penicillin skin testing","domain":"Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)","discipline":"medicine",
   "stem":"When is referral for outpatient penicillin skin testing appropriate?",
   "answer":"When the reaction history is unclear AND the patient is likely to require that drug in the future.",
   "rationale":"Clarifying penicillin allergy status avoids unnecessary use of broader-spectrum or less effective alternatives; skin testing should be performed when the clinical need is foreseeable.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":192}],"confusable_with":""},
  {"id":"betalactam-allergy-3","topic":"Beta-lactam allergy evaluation & penicillin skin testing","domain":"Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)","discipline":"medicine",
   "stem":"Most apparent allergic reactions to amide local anaesthetics are attributed to what rather than true allergy?",
   "answer":"The preservative methylparaben (in multi-dose vials) rather than the amide agent itself.",
   "rationale":"Amide local anaesthetics rarely cause true IgE-mediated allergy; reactions are typically vasovagal or due to preservatives; skin testing often fails to confirm true allergy.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":432}],"confusable_with":"True amide LA allergy (rare)"},
  {"id":"betalactam-allergy-4","topic":"Beta-lactam allergy evaluation & penicillin skin testing","domain":"Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)","discipline":"medicine",
   "stem":"In latex allergy, which food allergies should raise suspicion and which occupational group is most at risk?",
   "answer":"Foods: tropical fruits (mango, kiwi, avocado, banana, fig, chestnut). High-risk group: healthcare workers (frequent exposure) and children with spina bifida.",
   "rationale":"Latex-fruit syndrome occurs because latex and certain tropical fruits share cross-reactive proteins; healthcare workers develop sensitisation through occupational exposure.",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":79}],"confusable_with":""}
]

# ── 25: Bloodstream Infections & Bacteremia ──────────────────────────────────
kps += [
  {"id":"bsi-bact-1","topic":"Bloodstream Infections & Bacteremia","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"What is bacteremia in strictest definition and when does it progress to a bloodstream infection?",
   "answer":"Bacteremia = bacteria present in blood. It progresses to a bloodstream infection (BSI) when immune mechanisms are overwhelmed, potentially evolving to septicemia.",
   "rationale":"Not all bacteremia causes clinical infection; transient bacteremia (e.g., dental procedures) is common and cleared by normal immune mechanisms.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Bloodstream Infections & Bacteremia","page":1}],"confusable_with":"Septicemia (bacteremia + systemic inflammatory response)"},
  {"id":"bsi-bact-2","topic":"Bloodstream Infections & Bacteremia","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"What is the most common gram-negative cause of bacteremia and the most common gram-positive cause?",
   "answer":"E. coli (most common gram-negative); Staphylococcus aureus (most common gram-positive).",
   "rationale":"E. coli BSI typically arises from urinary or GI sources; S. aureus BSI is associated with skin/line infections and carries higher mortality due to metastatic seeding.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Bloodstream Infections & Bacteremia","page":2}],"confusable_with":""},
  {"id":"bsi-bact-3","topic":"Bloodstream Infections & Bacteremia","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"Which BSI pathogens are associated with higher mortality rates?",
   "answer":"S. aureus, Pseudomonas aeruginosa, and Enterobacter species.",
   "rationale":"These organisms have higher virulence, propensity for antimicrobial resistance, and capacity for metastatic seeding (S. aureus endocarditis/osteomyelitis).",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Bloodstream Infections & Bacteremia","page":4}],"confusable_with":""},
  {"id":"bsi-bact-4","topic":"Bloodstream Infections & Bacteremia","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"In febrile neutropenia, what organisms account for gram-negative vs gram-positive BSI?",
   "answer":"~40% GNRs (E. coli, Klebsiella > Pseudomonas); ~60% GPCs (CoNS > MSSA/MRSA, streptococci, enterococci).",
   "rationale":"Neutropenic patients develop BSI from translocation of gut bacteria (GNRs) and skin/line organisms (GPCs); empiric coverage must address both.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":161}],"confusable_with":""}
]

# ── 26: Brain Death & Disorders of Consciousness ─────────────────────────────
# Chunks were mostly trinucleotide repeat disorder content; only Marino ICU Book p630 is usable
kps += [
  {"id":"brain-death-1","topic":"Brain Death & Disorders of Consciousness","domain":"Internal medicine: neurology (ischemic & hemorrhagic stroke, seizures & status epilepticus, altered mental status & delirium, headache, neuromuscular weakness, spinal cord syndromes)","discipline":"medicine",
   "stem":"Consciousness has two components. What are they and how are they defined?",
   "answer":"Arousal (wakefulness — ability to recognise surroundings) and awareness (responsiveness — understanding one's relationship to surroundings).",
   "rationale":"The arousal-awareness framework allows classification of disorders of consciousness: coma (absent both), vegetative state (arousal without awareness), MCS (minimal awareness).",
   "bloom":"recall","source":[{"book":"Marino ICU Book","page":630}],"confusable_with":""},
  {"id":"brain-death-2","topic":"Brain Death & Disorders of Consciousness","domain":"Internal medicine: neurology (ischemic & hemorrhagic stroke, seizures & status epilepticus, altered mental status & delirium, headache, neuromuscular weakness, spinal cord syndromes)","discipline":"medicine",
   "stem":"Arousal and awareness together define different states. What state is characterised by absent arousal and absent awareness?",
   "answer":"Coma.",
   "rationale":"In coma both arousal (wakefulness) and awareness (responsiveness) are absent; this distinguishes coma from vegetative state (arousal preserved but no awareness).",
   "bloom":"recall","source":[{"book":"Marino ICU Book","page":630}],"confusable_with":"Vegetative state (arousal present but awareness absent)"}
]

# ── 27: Carbon Monoxide Poisoning ─────────────────────────────────────────────
kps += [
  {"id":"co-poison-1","topic":"Carbon Monoxide Poisoning","domain":"Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)","discipline":"medicine",
   "stem":"Carbon monoxide has how many times greater affinity for haemoglobin than oxygen?",
   "answer":"200-300 times greater affinity than oxygen for haemoglobin.",
   "rationale":"This massive affinity advantage means even trace CO exposure causes significant carboxyhaemoglobin formation, shifting the oxygen-haemoglobin dissociation curve leftward.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":841}],"confusable_with":"Cyanide (binds cytochrome enzymes, not haemoglobin primarily)"},
  {"id":"co-poison-2","topic":"Carbon Monoxide Poisoning","domain":"Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)","discipline":"medicine",
   "stem":"Why does pulse oximetry give a falsely HIGH reading in carbon monoxide poisoning?",
   "answer":"Carboxyhaemoglobin (COHb) and oxyhaemoglobin absorb light similarly at 660 nm; standard two-wavelength pulse oximeters cannot distinguish them.",
   "rationale":"Standard pulse oximetry uses only 660 nm (red) and 940 nm (infrared); CO-haemoglobin absorbs similarly to oxyHb at 660 nm, falsely registering as saturated haemoglobin.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":192}],"confusable_with":""},
  {"id":"co-poison-3","topic":"Carbon Monoxide Poisoning","domain":"Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)","discipline":"medicine",
   "stem":"How can CO poisoning occur during general anaesthesia with volatile agents?",
   "answer":"Desflurane (and other volatiles) are degraded by desiccated CO2 absorbents (particularly barium hydroxide lime, or dry soda lime) producing clinically significant CO.",
   "rationale":"When CO2 absorbents are allowed to desiccate, the exothermic reaction with halogenated volatiles (especially desflurane) generates CO; using calcium hydroxide absorbents or keeping absorbents moist prevents this.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":268}],"confusable_with":""},
  {"id":"co-poison-4","topic":"Carbon Monoxide Poisoning","domain":"Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)","discipline":"medicine",
   "stem":"After smoke inhalation, what toxic gases beyond CO are commonly produced and how does cyanide exert its toxic effect?",
   "answer":"Cyanide and hydrogen sulfide are common; cyanide binds cytochrome enzymes and inhibits cellular ATP production, causing lactic acidosis.",
   "rationale":"Combustion of synthetic materials (polyurethane) releases cyanide; cyanide poisoning manifests with neurological impairment, lactic acidosis, and cardiovascular collapse.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2136}],"confusable_with":"CO poisoning (different mechanism; treat with hydroxocobalamin vs O2)"},
  {"id":"co-poison-5","topic":"Carbon Monoxide Poisoning","domain":"Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)","discipline":"medicine",
   "stem":"What immediate treatment is given for CO poisoning?",
   "answer":"100% high-flow oxygen; hyperbaric oxygen (HBO) for severe cases (LOC, neurologic deficits, COHb >25%, pregnancy).",
   "rationale":"High FiO2 competes with CO for haemoglobin binding and accelerates CO elimination; HBO further accelerates CO release and may reduce delayed neurologic sequelae.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":2135}],"confusable_with":"Cyanide treatment (hydroxocobalamin or amyl nitrite)"},
  {"_type":"illness_script","topic":"Carbon Monoxide Poisoning","discipline":"medicine",
   "enabling_conditions":"House fire, enclosed-space combustion, faulty heating equipment, desiccated anaesthetic CO2 absorbent",
   "pathophysiology":"CO-haemoglobin: 200-300x O2 affinity, tissue hypoxia; CO binds myoglobin/cytochromes directly impairing cellular respiration",
   "time_course":"Symptoms correlate with COHb level: headache at 10-20%, confusion at 20-40%, coma/death at >60%",
   "key_features":"Headache, confusion, cherry-red skin (unreliable), normal SpO2 on standard pulse oximetry despite severe hypoxia",
   "consequence_if_missed":"Death; delayed neuropsychiatric sequelae even with survival (memory loss, parkinsonism)"}
]

# ── 28: Catheter-Associated UTI (CAUTI) ──────────────────────────────────────
kps += [
  {"id":"cauti-1","topic":"Catheter-Associated UTI (CAUTI)","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"What is the IDSA definition of CAUTI vs asymptomatic bacteriuria in a catheterised patient?",
   "answer":"CAUTI: bacteriuria with symptoms referable to a UTI with no other identified source. Asymptomatic bacteriuria: bacteriuria >=100,000 CFU/mL WITHOUT symptoms — should NOT be treated (exceptions: pregnancy, recent renal transplant, pre-urologic procedure).",
   "rationale":"Treating asymptomatic bacteriuria in catheterised patients does not improve outcomes and selects for resistant organisms; treatment should be reserved for true CAUTI.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":119}],"confusable_with":"Asymptomatic bacteriuria (treat only in specific exceptions)"},
  {"id":"cauti-2","topic":"Catheter-Associated UTI (CAUTI)","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"What proportion of hospitalised US patients receive a urinary catheter and what are the two routes of CAUTI infection?",
   "answer":"~15-25% of hospitalised patients; extraluminal (migration along outer catheter surface) and intraluminal (ascending through the lumen via urinary stasis or break in closed system).",
   "rationale":"Understanding transmission routes guides prevention: sterile technique, closed drainage systems, and prompt catheter removal reduce both extraluminal and intraluminal infection.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Shock  Classification & Pathophysiology","page":6}],"confusable_with":""},
  {"id":"cauti-3","topic":"Catheter-Associated UTI (CAUTI)","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"CAUTI symptom timing criterion: how long after catheter removal can symptoms still qualify as CAUTI?",
   "answer":"Symptoms must begin while the CVC/catheter is in place OR within 48 hours of its removal.",
   "rationale":"The 48-hour window acknowledges that bacteria colonising the urinary tract during catheterisation may cause infection shortly after removal.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Shock  Classification & Pathophysiology","page":12}],"confusable_with":"Community-acquired UTI (no recent catheter use)"},
  {"id":"cauti-4","topic":"Catheter-Associated UTI (CAUTI)","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"No single strategy prevents CAUTI. What is the most important modifiable risk factor to address?",
   "answer":"Duration of catheterisation — remove the urinary catheter as soon as no longer clinically indicated.",
   "rationale":"CAUTI risk is directly proportional to duration of catheterisation; daily assessment of catheter necessity and prompt removal is the most effective prevention strategy.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":772}],"confusable_with":""}
]

# ── 29: Chest Trauma — chunks entirely off-topic ─────────────────────────────
# Usable: Stanford CA-1 p73 (laryngospasm/airway), MGH p55 (VTE after trauma)
kps += [
  {"id":"chest-trauma-1","topic":"Chest Trauma","domain":"Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)","discipline":"medicine",
   "stem":"In chest trauma with pneumothorax, how does positive-pressure ventilation (PPV) affect bullae or pneumothorax?",
   "answer":"PPV increases pressure in a pneumothorax/bulla and can convert a simple pneumothorax to tension pneumothorax; chest tube drainage is required before PPV in most cases.",
   "rationale":"Positive pressure applied to a non-communicating gas collection creates a one-way valve effect; intrathoracic pressure rises with each breath, eventually causing cardiovascular collapse.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":505}],"confusable_with":""},
  {"id":"chest-trauma-2","topic":"Chest Trauma","domain":"Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)","discipline":"medicine",
   "stem":"After chest trauma with rib fractures, what is the most life-threatening early complication detectable on physical exam by tracheal deviation and decreased breath sounds?",
   "answer":"Tension pneumothorax — tracheal deviation away from the affected side, absent breath sounds, hypotension.",
   "rationale":"Tension pneumothorax compresses the mediastinum; tracheal deviation is a late sign indicating severe mediastinal shift; immediate needle decompression is required.",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":54}],"confusable_with":"Haemothorax (dull percussion, no tracheal deviation)"},
  {"id":"chest-trauma-3","topic":"Chest Trauma","domain":"Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)","discipline":"medicine",
   "stem":"After major trauma, what is the recommended anticoagulation approach for proximal DVT?",
   "answer":"Anticoagulate with DOAC preferred over VKA/LMWH for at least 3 months; in malignancy-related DVT prefer DOAC over LMWH.",
   "rationale":"Proximal DVT carries high PE risk; anticoagulation guidelines recommend at least 3 months regardless of symptoms, with agent selection based on bleeding risk and comorbidities.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":55}],"confusable_with":"Distal DVT (individualised decision)"}
]

# ── 30: Coagulopathy & Hematologic Emergencies in ICU ────────────────────────
# Most chunks off-topic. Usable: Morgan p1353 balanced resuscitation, Miller p446 DIC
kps += [
  {"id":"coag-heme-icu-1","topic":"Coagulopathy & Hematologic Emergencies in ICU","domain":"Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)","discipline":"medicine",
   "stem":"In trauma-associated coagulopathy, what is balanced resuscitation?",
   "answer":"Administering blood products in a balanced ratio (e.g., 1:1:1 — PRBCs:FFP:platelets) to prevent dilutional coagulopathy from crystalloid-dominant resuscitation.",
   "rationale":"Crystalloid resuscitation dilutes clotting factors and platelets; balanced resuscitation replaces all components of blood and reduces the lethal triad of coagulopathy, acidosis, and hypothermia.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1353}],"confusable_with":"Crystalloid resuscitation"},
  {"id":"coag-heme-icu-2","topic":"Coagulopathy & Hematologic Emergencies in ICU","domain":"Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)","discipline":"medicine",
   "stem":"In DIC, why is antifibrinolytic therapy generally contraindicated?",
   "answer":"Risk of catastrophic thrombotic complications from suppressing the compensatory fibrinolytic response in an already pro-thrombotic state.",
   "rationale":"DIC involves simultaneous clot formation and fibrinolysis; blocking fibrinolysis without addressing underlying clot generation risks end-organ infarction.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":446}],"confusable_with":"Primary hyperfibrinolysis (antifibrinolytics indicated)"},
  {"id":"coag-heme-icu-3","topic":"Coagulopathy & Hematologic Emergencies in ICU","domain":"Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)","discipline":"medicine",
   "stem":"In DIC with thrombocytopenia, when should platelet transfusion be considered?",
   "answer":"In a non-bleeding patient, treatment with platelet transfusion is not usually indicated unless platelet count is very low or there is active haemorrhage.",
   "rationale":"Transfused platelets are consumed in DIC; transfusion is reserved for active bleeding or procedures, not prophylaxis, to avoid fuelling the consumptive coagulopathy.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":446}],"confusable_with":"Immune thrombocytopenia (transfusion threshold different)"}
]

# ── 31: Corticosteroid complications ─────────────────────────────────────────
# Usable: StatPearls Adrenal Crisis p12, Pituitary Apoplexy (stress dose steroids)
kps += [
  {"id":"steroid-comp-1","topic":"Corticosteroid complications & steroid-sparing strategies","domain":"Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)","discipline":"medicine",
   "stem":"What proportion of adrenal crisis patients do NOT have a prior diagnosis of adrenal insufficiency?",
   "answer":"More than 50% of adrenal crisis patients have no prior diagnosis of adrenal insufficiency.",
   "rationale":"Adrenal crisis can be the first presentation; clinicians must maintain awareness especially in patients on long-term corticosteroids or with pituitary disease.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Adrenal Crisis","page":12}],"confusable_with":""},
  {"id":"steroid-comp-2","topic":"Corticosteroid complications & steroid-sparing strategies","domain":"Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)","discipline":"medicine",
   "stem":"In pituitary apoplexy, what is the immediate corticosteroid management principle?",
   "answer":"Rapid initiation of corticosteroid (stress-dose) therapy to prevent life-threatening adrenal crisis.",
   "rationale":"Pituitary apoplexy destroys corticotroph cells, causing acute secondary adrenal insufficiency; emergency hydrocortisone administration is life-saving.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Pituitary Apoplexy","page":1}],"confusable_with":""},
  {"id":"steroid-comp-3","topic":"Corticosteroid complications & steroid-sparing strategies","domain":"Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)","discipline":"medicine",
   "stem":"Long-term topical corticosteroid use to the eye can cause which two serious complications?",
   "answer":"Steroid-induced ocular hypertension (glaucoma) and posterior subcapsular cataracts.",
   "rationale":"Corticosteroids increase aqueous humour production and reduce outflow (glaucoma mechanism); they also promote posterior subcapsular lens opacification directly.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Bone marrow transplantation  complications","page":29}],"confusable_with":""},
  {"id":"steroid-comp-4","topic":"Corticosteroid complications & steroid-sparing strategies","domain":"Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)","discipline":"medicine",
   "stem":"Patients on long-term corticosteroids should be educated to do what in the setting of illness or physiologic stress?",
   "answer":"Increase (sick-day rules/stress dose) their corticosteroid dose during illness, surgery, or physiologic stress to prevent adrenal crisis.",
   "rationale":"Chronic exogenous steroid use suppresses the HPA axis; during stress the adrenal gland cannot mount an appropriate cortisol surge, requiring supplementation.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Adrenal Crisis","page":12}],"confusable_with":""}
]

# ── 32: Digoxin Toxicity ──────────────────────────────────────────────────────
kps += [
  {"id":"digoxin-tox-1","topic":"Digoxin Toxicity","domain":"Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)","discipline":"medicine",
   "stem":"In a patient on digoxin, which electrolyte imbalance significantly increases the risk of digoxin toxicity and should be actively prevented?",
   "answer":"Hypokalaemia — target plasma K+ >4 mEq/L in digoxin-treated patients.",
   "rationale":"Potassium competes with digoxin at the Na+/K+-ATPase; hypokalaemia reduces competition, increasing digoxin binding and toxicity at any given serum digoxin level.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1882}],"confusable_with":"Hyperkalaemia (also affects cardiac conduction)"},
  {"id":"digoxin-tox-2","topic":"Digoxin Toxicity","domain":"Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)","discipline":"medicine",
   "stem":"Hypomagnesaemia potentiates digoxin toxicity via which electrolyte interaction?",
   "answer":"Hypomagnesaemia causes renal K+ wasting and hypokalaemia, which then sensitises the myocardium to digoxin toxicity.",
   "rationale":"Magnesium is required for renal K+ retention; hypoMg causes hypokalaemia, which then potentiates digoxin toxicity; both electrolytes must be replenished.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1899}],"confusable_with":""},
  {"id":"digoxin-tox-3","topic":"Digoxin Toxicity","domain":"Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)","discipline":"medicine",
   "stem":"Why is IV calcium administration to treat hyperkalaemia in digoxin-toxic patients historically concerning?",
   "answer":"Calcium potentiates digoxin's positive inotropic effect, with theoretical risk of 'stone heart' (irreversible diastolic contracture); however clinical studies have not confirmed significant harm.",
   "rationale":"The concern is that excess intracellular calcium combined with Na+/K+-ATPase inhibition by digoxin could cause tetanic myocardial contraction; in practice, the risk appears lower than originally feared.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1886}],"confusable_with":""},
  {"id":"digoxin-tox-4","topic":"Digoxin Toxicity","domain":"Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)","discipline":"medicine",
   "stem":"What factors promote formation of abnormal cardiac impulses that can lead to digoxin-associated arrhythmias?",
   "answer":"Increased catecholamines, electrolyte disorders (hyperkalaemia, hypokalaemia, hypercalcaemia), ischaemia, hypoxia, mechanical stretch, and digoxin toxicity itself.",
   "rationale":"Digoxin triggers delayed after-depolarisations in Purkinje tissue; these factors lower the threshold for after-depolarisation reaching action potential threshold.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":607}],"confusable_with":""},
  {"id":"digoxin-tox-5","topic":"Digoxin Toxicity","domain":"Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)","discipline":"medicine",
   "stem":"What ECG sequence is seen with progressive hyperkalaemia and how does this relate to digoxin toxicity?",
   "answer":"Peaked T waves -> widened QRS -> prolonged PR -> sine wave pattern -> VF/asystole; hyperkalaemia accentuates the cardiac toxicity of digoxin.",
   "rationale":"Hyperkalaemia and digoxin both affect cardiac automaticity and conduction; co-occurrence accelerates progression to fatal arrhythmia.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1886}],"confusable_with":""},
  {"_type":"illness_script","topic":"Digoxin Toxicity","discipline":"medicine",
   "enabling_conditions":"Digoxin therapy with hypokalaemia, hypomagnesaemia, renal failure (reduced clearance), drug interactions (amiodarone, verapamil), overdose",
   "pathophysiology":"Excess Na+/K+-ATPase inhibition -> intracellular Na+ accumulation -> increased intracellular Ca2+ via Na+/Ca2+ exchanger -> delayed after-depolarisations -> arrhythmias; increased vagal tone -> AV block",
   "time_course":"Acute: rapid arrhythmia onset; chronic toxicity: insidious with GI prodrome (nausea/vomiting/xanthopsia)",
   "key_features":"GI symptoms (nausea, vomiting, abdominal pain), visual disturbances (yellow/green halos), bradycardia, AV block, ventricular arrhythmias",
   "consequence_if_missed":"Life-threatening arrhythmias; treatment: digoxin-specific Fab antibody fragments (Digibind); correct hypokalaemia"}
]

with open('data/kp_part0_chunk3.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print(f"Chunk3 saved: {len(kps)} entries")
