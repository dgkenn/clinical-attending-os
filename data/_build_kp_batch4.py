import json

kps = []

# ── TOPIC 17: Antiseizure Medication Pharmacology & Selection ───────────────
# Chunks for this topic are almost entirely off-topic (anesthesia pharmacology). Very thin relevant content.
kps += [
  {
    "id": "antiseizure-1",
    "topic": "Antiseizure Medication Pharmacology & Selection",
    "domain": "Internal medicine: neurology (ischemic & hemorrhagic stroke, seizures & status epilepticus, altered mental status & delirium, headache, neuromuscular weakness, spinal cord syndromes)",
    "discipline": "medicine",
    "stem": "Benzodiazepines reduce the minimum alveolar concentration (MAC) of volatile anesthetics by approximately how much, and what is the clinical implication for antiseizure medication interactions?",
    "answer": "Benzodiazepines reduce volatile anesthetic MAC by up to 30%; their CNS depressant effects add to other sedatives including antiseizure medications with sedative properties",
    "rationale": "Benzodiazepines enhance GABA-mediated inhibition; this mechanism underlies both their antiseizure and sedative-hypnotic effects, and contributes to additive CNS depression with anesthetic agents.",
    "bloom": "apply",
    "source": [{"book": "Morgan & Mikhail", "page": 284}],
    "confusable_with": "no interaction between benzodiazepines and volatile agents (the MAC-reducing effect is clinically significant)"
  },
  {
    "id": "antiseizure-2",
    "topic": "Antiseizure Medication Pharmacology & Selection",
    "domain": "Internal medicine: neurology (ischemic & hemorrhagic stroke, seizures & status epilepticus, altered mental status & delirium, headache, neuromuscular weakness, spinal cord syndromes)",
    "discipline": "medicine",
    "stem": "The drug of choice for trigeminal neuralgia is carbamazepine. What serious adverse effect requires monitoring?",
    "answer": "Agranulocytosis (also requires monitoring for hepatotoxicity and hyponatremia; SIADH with carbamazepine)",
    "rationale": "Carbamazepine suppresses bone marrow in rare patients, causing potentially fatal agranulocytosis; baseline CBC and periodic monitoring are required.",
    "bloom": "recall",
    "source": [{"book": "Morgan & Mikhail", "page": 1752}],
    "confusable_with": "phenytoin (gingival hyperplasia, Stevens-Johnson syndrome — different adverse profile)"
  },
  {
    "id": "antiseizure-3",
    "topic": "Antiseizure Medication Pharmacology & Selection",
    "domain": "Internal medicine: neurology (ischemic & hemorrhagic stroke, seizures & status epilepticus, altered mental status & delirium, headache, neuromuscular weakness, spinal cord syndromes)",
    "discipline": "medicine",
    "stem": "Flumazenil reverses benzodiazepine effects rapidly. What important limitation applies to its reversal of amnesia?",
    "answer": "Flumazenil promptly reverses hypnotic/sedative effects (<1 min onset) but amnesia is less reliably reversed",
    "rationale": "The amnestic effect of benzodiazepines involves memory consolidation pathways that differ from sedation; flumazenil may not restore explicit memory formation even when sedation is reversed.",
    "bloom": "apply",
    "source": [{"book": "Morgan & Mikhail", "page": 466}],
    "confusable_with": "flumazenil fully reversing all benzodiazepine effects (amnesia component is incompletely reversed)"
  }
]

# ── TOPIC 18: Aspiration Pneumonia & Pneumonitis ─────────────────────────────
kps += [
  {
    "id": "aspiration-pna-1",
    "topic": "Aspiration Pneumonia & Pneumonitis",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What distinguishes aspiration pneumonitis from aspiration pneumonia pathophysiologically?",
    "answer": "Pneumonitis: chemical injury from sterile acid aspirate (no bacteria, no antibiotics needed initially); Pneumonia: bacterial infection from aspiration of colonized oropharyngeal or gastric contents",
    "rationale": "Mendelson syndrome (acid pneumonitis) is a chemical inflammation; true aspiration pneumonia requires bacterial infection and antibiotic treatment; distinguishing them affects management.",
    "bloom": "analyze",
    "source": [{"book": "StatPearls: StatPearls   Aspiration Pneumonia and Pneumonitis", "page": 5}],
    "confusable_with": "treating all aspiration events with antibiotics (only pneumonia, not pneumonitis, requires antibiotics)"
  },
  {
    "id": "aspiration-pna-2",
    "topic": "Aspiration Pneumonia & Pneumonitis",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What are the predominant bacterial pathogens in aspiration pneumonia?",
    "answer": "Aerobic gram-negative bacilli predominate, with aerobic gram-positive organisms second; polymicrobial with anaerobes",
    "rationale": "Aspiration pneumonia (especially hospital-acquired) is polymicrobial; gram-negative bacilli predominate in the nosocomial setting while anaerobes are more prominent in community-acquired aspiration.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Aspiration Pneumonia and Pneumonitis", "page": 5}],
    "confusable_with": "anaerobes always predominant (true for community-acquired aspiration from oral flora; hospital-acquired shifts toward gram-negatives)"
  },
  {
    "id": "aspiration-pna-3",
    "topic": "Aspiration Pneumonia & Pneumonitis",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What patient characteristics most reliably predict aspiration risk in older adults beyond age alone?",
    "answer": "Frailty, poor nutritional status, and limited mobility — not age itself",
    "rationale": "Advanced age alone does not directly predict aspiration pneumonia risk; frailty and functional decline are stronger predictors because they correlate with dysphagia, silent microaspiration, and immune compromise.",
    "bloom": "analyze",
    "source": [{"book": "StatPearls: StatPearls   Aspiration Pneumonia and Pneumonitis", "page": 3}],
    "confusable_with": "age alone as primary risk factor (frailty, malnutrition, and immobility are stronger predictors)"
  },
  {
    "id": "aspiration-pna-4",
    "topic": "Aspiration Pneumonia & Pneumonitis",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What at-risk patient groups have the highest prevalence of aspiration pneumonia according to population data?",
    "answer": "Acute stroke patients (3-50%), post-cardiac arrest, patients with neurodegenerative diseases causing dysphagia; >75 years age group accounts for 76% of aspiration pneumonia deaths in the US",
    "rationale": "Neurological impairment of swallowing is the primary risk factor; silent microaspirations during sleep are common in neurologically impaired patients.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Aspiration Pneumonia and Pneumonitis", "page": 3}],
    "confusable_with": "ICU-intubated patients (VAP is a distinct entity; aspiration pneumonia more classically involves oropharyngeal or gastric content in non-ventilated patients)"
  },
  {
    "id": "aspiration-pna-5",
    "topic": "Aspiration Pneumonia & Pneumonitis",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What criteria define the threshold gastric content risk for aspiration pneumonitis, and when should anesthetic technique be modified?",
    "answer": "Risk threshold: gastric volume >25 mL (0.4 mL/kg) AND pH <2.5; modify technique with RSI, awake intubation, or regional when at risk",
    "rationale": "Below pH 2.5, acid causes severe chemical pneumonitis; below volume threshold, aspirated contents may not be sufficient to cause significant injury; both criteria together define high risk.",
    "bloom": "apply",
    "source": [{"book": "Morgan & Mikhail", "page": 438}],
    "confusable_with": "volume alone defines risk (pH is an equally critical parameter)"
  },
  {
    "_type": "illness_script",
    "topic": "Aspiration Pneumonia & Pneumonitis",
    "discipline": "medicine",
    "enabling_conditions": "Dysphagia (stroke, dementia, Parkinson, head/neck cancer), reduced consciousness (anesthesia, alcohol, seizures), GERD, nasogastric feeds, poor oral hygiene",
    "pathophysiology": "Pneumonitis: chemical injury from acid; Pneumonia: bacterial inoculation of lung from aspirated oropharyngeal flora (polymicrobial, gram-negative bacilli predominate in hospital)",
    "time_course": "Pneumonitis: immediate (within hours); Pneumonia: develops over 24-48h after aspiration event",
    "key_features": "Cough, fever, hypoxia, right lower lobe infiltrate (gravitational); hospital-acquired more often upper lobes; dysphagia history or neurological impairment",
    "consequence_if_missed": "Progression to severe pneumonia, lung abscess, empyema, ARDS, sepsis; mortality 10-15% in hospitalized patients"
  }
]

# ── TOPIC 19: Aspirin/NSAID Hypersensitivity ────────────────────────────────
kps += [
  {
    "id": "nsaid-hypersens-1",
    "topic": "Aspirin/NSAID hypersensitivity",
    "domain": "Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)",
    "discipline": "medicine",
    "stem": "What is the mechanism of aspirin/NSAID-exacerbated respiratory disease (AERD) and what pre-existing condition is almost always present?",
    "answer": "COX-1 inhibition shunts arachidonic acid toward leukotriene production (LTC4/LTD4) causing bronchoconstriction; almost always present in patients with asthma and nasal polyps (Samter triad)",
    "rationale": "AERD is a pharmacological (not IgE-mediated) reaction; COX-1 blockade inhibits protective PGE2 that normally suppresses mast cells, while increasing pro-inflammatory leukotrienes.",
    "bloom": "analyze",
    "source": [{"book": "Morgan & Mikhail", "page": 460}],
    "confusable_with": "IgE-mediated aspirin allergy (AERD is non-immunologic, pharmacologic reaction; cross-reacts with ALL NSAIDs)"
  },
  {
    "id": "nsaid-hypersens-2",
    "topic": "Aspirin/NSAID hypersensitivity",
    "domain": "Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)",
    "discipline": "medicine",
    "stem": "For a patient with documented aspirin/NSAID hypersensitivity requiring analgesia, which analgesic class is safe to use?",
    "answer": "Acetaminophen (does not inhibit peripheral COX enzymes significantly at therapeutic doses); COX-2 selective inhibitors (celecoxib) may be tolerated with caution",
    "rationale": "AERD is triggered by COX-1 inhibition; acetaminophen at standard doses has negligible peripheral COX-1 activity; selective COX-2 inhibitors spare the COX-1/leukotriene pathway.",
    "bloom": "apply",
    "source": [{"book": "Morgan & Mikhail", "page": 460}],
    "confusable_with": "all anti-inflammatory drugs contraindicated (COX-2 selective agents are generally tolerated in AERD at therapeutic doses)"
  },
  {
    "id": "nsaid-hypersens-3",
    "topic": "Aspirin/NSAID hypersensitivity",
    "domain": "Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)",
    "discipline": "medicine",
    "stem": "What is the negative predictive value (NPV) of penicillin skin testing for evaluating drug allergy, and what procedure does it guide?",
    "answer": "NPV of penicillin skin testing is 95%; a negative test guides graded challenge (deliberate rechallenge/test dose procedure)",
    "rationale": "A negative penicillin skin test indicates 95% probability of no IgE-mediated reaction; this allows graded rechallenge which can de-label patients with low-probability penicillin allergy.",
    "bloom": "recall",
    "source": [{"book": "MGH Housestaff Manual", "page": 192}],
    "confusable_with": "100% negative predictive value (5% of skin-test-negative patients may still react; graded challenge with monitoring is still required)"
  },
  {
    "id": "nsaid-hypersens-4",
    "topic": "Aspirin/NSAID hypersensitivity",
    "domain": "Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)",
    "discipline": "medicine",
    "stem": "COX-1 inhibitors reduce platelet aggregation by inhibiting thromboxane A2. What is the clinical interaction between ketorolac and aspirin?",
    "answer": "Aspirin decreases protein binding of ketorolac, increasing the amount of active unbound drug; additive antiplatelet effects increase bleeding risk",
    "rationale": "Ketorolac is highly protein-bound; aspirin displaces it, raising free drug levels and pharmacodynamic activity; concurrent use increases both analgesic effects and GI/bleeding risk.",
    "bloom": "apply",
    "source": [{"book": "Morgan & Mikhail", "page": 460}],
    "confusable_with": "no significant aspirin-NSAID pharmacokinetic interaction (there is a significant interaction via protein binding displacement)"
  }
]

# ── TOPIC 20: Bacterial Meningitis: Diagnosis & Emergency Management ─────────
kps += [
  {
    "id": "bact-mening-dx-1",
    "topic": "Bacterial Meningitis: Diagnosis & Emergency Management",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "95% of bacterial meningitis patients have at least 2 of what 4 classic symptoms?",
    "answer": "Fever, neck stiffness (nuchal rigidity), altered mental status, headache",
    "rationale": "The classic triad/tetrad identifies most bacterial meningitis; while individual signs have variable sensitivity, 95% of patients have at least 2 of these 4 symptoms (NEJM 2004;351:1849).",
    "bloom": "recall",
    "source": [{"book": "MGH Housestaff Manual", "page": 123}],
    "confusable_with": "requiring all 4 symptoms for diagnosis (absence of one symptom does not exclude bacterial meningitis)"
  },
  {
    "id": "bact-mening-dx-2",
    "topic": "Bacterial Meningitis: Diagnosis & Emergency Management",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What is the time window for antibiotic delay that is associated with increased mortality in bacterial meningitis?",
    "answer": "Delays of 3-6 hours are associated with increased mortality; timely antibiotics are essential",
    "rationale": "Each hour of delay in antibiotic administration allows ongoing bacterial replication, cytokine storm escalation, and brain injury; blood cultures should be drawn first but must not delay antibiotics.",
    "bloom": "recall",
    "source": [{"book": "StatPearls", "page": 4}],
    "confusable_with": "waiting for LP before giving antibiotics (if LP will be delayed >30 min, give antibiotics first after blood cultures)"
  },
  {
    "id": "bact-mening-dx-3",
    "topic": "Bacterial Meningitis: Diagnosis & Emergency Management",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What empiric antibiotic regimen should be started for bacterial meningitis when diagnosis will be delayed, and what is added for patients >50 or immunocompromised?",
    "answer": "Ceftriaxone + vancomycin empirically; add ampicillin for age >50 or immunocompromised (Listeria coverage)",
    "rationale": "Ceftriaxone covers pneumococcus and Neisseria; vancomycin adds MRSA/PCN-resistant pneumococcal coverage; ampicillin covers Listeria monocytogenes, which is more common in elderly and immunocompromised patients.",
    "bloom": "apply",
    "source": [{"book": "StatPearls", "page": 4}],
    "confusable_with": "ceftriaxone alone (inadequate: misses PCN-resistant pneumococcus without vancomycin, and Listeria without ampicillin in high-risk patients)"
  },
  {
    "id": "bact-mening-dx-4",
    "topic": "Bacterial Meningitis: Diagnosis & Emergency Management",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What percentage of bacterial meningitis patients have concurrent bacteremia, and what does this imply for workup?",
    "answer": "53% have concurrent bacteremia; blood cultures should be obtained BEFORE antibiotics",
    "rationale": "Blood cultures have high yield in bacterial meningitis and should be obtained immediately before antibiotic administration; a positive blood culture may avoid need for LP or confirm the organism.",
    "bloom": "recall",
    "source": [{"book": "StatPearls", "page": 4}],
    "confusable_with": "LP as the only necessary culture (blood cultures are high yield and should accompany LP workup)"
  },
  {
    "id": "bact-mening-dx-5",
    "topic": "Bacterial Meningitis: Diagnosis & Emergency Management",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What CSF profile distinguishes bacterial from viral meningitis on LP?",
    "answer": "Bacterial: WBC <100 to >10,000 (>80% PMN), protein >100-1000 mg/dL, glucose <40 mg/dL; Viral: WBC 50-1000 (lymphocytic), protein <200, glucose normal-slightly low",
    "rationale": "Bacterial meningitis causes pyogenic (PMN-dominant) CSF inflammation with low glucose from bacterial metabolism and high protein from blood-brain barrier disruption.",
    "bloom": "recall",
    "source": [{"book": "MGH Housestaff Manual", "page": 263}],
    "confusable_with": "early HSV encephalitis (can have early PMN predominance mimicking bacterial; PCR distinguishes)"
  },
  {
    "_type": "illness_script",
    "topic": "Bacterial Meningitis: Diagnosis & Emergency Management",
    "discipline": "medicine",
    "enabling_conditions": "No prior meningococcal or pneumococcal vaccination, immunocompromised state, asplenia, cochlear implant, CSF leak, close-contact exposure (dormitory living)",
    "pathophysiology": "Bacterial invasion of subarachnoid space triggers intense neutrophilic inflammation, cytokine release, cerebral edema, vasculitis, hydrocephalus, and cranial nerve injury",
    "time_course": "Hours to days; petechial rash (meningococcemia) may precede meningeal signs; rapid deterioration possible",
    "key_features": "Fever + headache + meningismus +/- AMS; petechial rash (meningococcemia); CSF PMN pleocytosis, low glucose, high protein",
    "consequence_if_missed": "Septic shock, herniation, deafness, neurocognitive disability, death; time-critical — delays of hours increase mortality"
  }
]

print(f"Batch 4: {len(kps)} entries")
with open("C:/Users/Dean/anesthesia_attending/data/_kp_batch4.json", "w", encoding="utf-8") as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Written to _kp_batch4.json")
