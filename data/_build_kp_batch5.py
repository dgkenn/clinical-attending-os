import json

kps = []

# ── TOPIC 21: Bacterial Meningitis: Pathogen-Specific Treatment ──────────────
kps += [
  {
    "id": "bact-mening-tx-1",
    "topic": "Bacterial Meningitis: Pathogen-Specific Treatment",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "In bacterial meningitis, for which patient groups should ampicillin be added to the empiric ceftriaxone + vancomycin regimen?",
    "answer": "Patients >50 years old AND immunocompromised patients (for Listeria monocytogenes coverage)",
    "rationale": "Listeria monocytogenes is resistant to cephalosporins; ampicillin (or penicillin G) is required for coverage; risk of Listeria meningitis is highest in elderly, immunocompromised, and neonates.",
    "bloom": "apply",
    "source": [{"book": "StatPearls", "page": 4}],
    "confusable_with": "universal ampicillin for all meningitis (only adds benefit for high-Listeria-risk groups; unnecessary in young healthy adults)"
  },
  {
    "id": "bact-mening-tx-2",
    "topic": "Bacterial Meningitis: Pathogen-Specific Treatment",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What CSF findings differentiate bacterial, viral, TB, and fungal meningitis on LP analysis?",
    "answer": "Bacterial: PMN predominance, low glucose (<40), high protein (100-1000); Viral: lymphocytic, normal glucose, protein <200; TB: lymphocytic, very low glucose (<45), elevated protein (>2000 with subarachnoid block); Fungal: lymphocytic, low glucose, India ink/CrAg for Cryptococcus",
    "rationale": "CSF cell type, glucose, and protein pattern rapidly narrow the etiologic differential while awaiting cultures; India ink and cryptococcal antigen are rapid diagnostic tools for fungal meningitis.",
    "bloom": "analyze",
    "source": [{"book": "MGH Housestaff Manual", "page": 263}],
    "confusable_with": "viral meningitis when early bacterial (early bacterial meningitis may show lymphocytic predominance before PMN shift develops)"
  },
  {
    "id": "bact-mening-tx-3",
    "topic": "Bacterial Meningitis: Pathogen-Specific Treatment",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "Bacterial meningitis can cause what four neurological complications beyond direct meningeal inflammation?",
    "answer": "Seizures, stroke (infectious vasculitis), hydrocephalus, and cranial nerve deficits (especially TB and fungal)",
    "rationale": "Meningeal inflammation triggers vasculitis causing ischemic stroke; CSF outflow obstruction causes hydrocephalus; basal meningeal thickening (TB/fungal) compresses cranial nerves.",
    "bloom": "recall",
    "source": [{"book": "MGH Housestaff Manual", "page": 123}],
    "confusable_with": "complications only occurring after treatment (vasculitis and hydrocephalus occur during acute infection)"
  },
  {
    "id": "bact-mening-tx-4",
    "topic": "Bacterial Meningitis: Pathogen-Specific Treatment",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What physical examination signs have high specificity but low sensitivity for bacterial meningitis?",
    "answer": "Kernig sign (5% Sn, 95% Sp), Brudzinski sign (5% Sn, 95% Sp); Jolt accentuation (64% Sn, 43% Sp); Nuchal rigidity (30% Sn, 68% Sp)",
    "rationale": "Classic meningeal signs are highly specific (few false positives) but miss half or more cases; their absence does not exclude bacterial meningitis, especially in elderly and immunocompromised patients.",
    "bloom": "analyze",
    "source": [{"book": "MGH Housestaff Manual", "page": 123}],
    "confusable_with": "negative Kernig/Brudzinski excluding bacterial meningitis (very low sensitivity; these signs may be absent)"
  },
  {
    "id": "bact-mening-tx-5",
    "topic": "Bacterial Meningitis: Pathogen-Specific Treatment",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "TB meningitis sensitivity of Mycobacterium tuberculosis culture from CSF is less than what percentage, and how does this affect management?",
    "answer": "MTb culture Sn <60%; empiric anti-TB therapy should not be delayed while awaiting cultures if clinical suspicion is high; NAAT not FDA-approved for CSF",
    "rationale": "TB meningitis is culture-insensitive due to paucibacillary CSF; diagnosis requires clinical, epidemiological, and CSF biochemical context; empiric treatment is warranted in high-suspicion cases.",
    "bloom": "analyze",
    "source": [{"book": "MGH Housestaff Manual", "page": 263}],
    "confusable_with": "TB culture as the diagnostic gold standard (its low sensitivity makes clinical diagnosis necessary)"
  }
]

# ── TOPIC 22: Basic apatite (hydroxyapatite) deposition disease ──────────────
# Chunks are almost entirely off-topic (echocardiography, gout, AKI).
# Writing minimal KPs from the gout differential/CPPD chunks.
kps += [
  {
    "id": "hydroxyapatite-1",
    "topic": "Basic apatite (hydroxyapatite) deposition disease",
    "domain": "Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)",
    "discipline": "medicine",
    "stem": "Basic apatite (hydroxyapatite) deposition disease and calcium pyrophosphate deposition disease (CPPD) are both in the differential for what presentation?",
    "answer": "Acute inflammatory arthritis (crystal arthritis); CPPD classically causes pseudogout; basic apatite causes calcific tendinitis and Milwaukee shoulder syndrome",
    "rationale": "Both are calcium-based crystal deposition diseases; basic apatite deposits in periarticular and articular tissues causing acute or chronic inflammatory arthropathy distinct from urate-based gout.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Gout  acute management", "page": 23}],
    "confusable_with": "gout (monosodium urate crystals; negatively birefringent needle-shaped; different crystal and management)"
  },
  {
    "id": "hydroxyapatite-2",
    "topic": "Basic apatite (hydroxyapatite) deposition disease",
    "domain": "Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)",
    "discipline": "medicine",
    "stem": "Crystal identification in synovial fluid by compensated polarized light microscopy remains the gold standard for which crystal arthropathy, and what are the crystal characteristics for CPPD?",
    "answer": "Polarized microscopy is gold standard for CPPD; crystals are rhomboid-shaped and weakly positively birefringent",
    "rationale": "Calcium pyrophosphate crystals appear positively birefringent and rhomboid under polarized light; this distinguishes CPPD from gout (negatively birefringent needle-shaped monosodium urate crystals).",
    "bloom": "recall",
    "source": [{"book": "StatPearls", "page": 5}],
    "confusable_with": "gout crystals (negatively birefringent needle-shaped; opposite birefringence to CPPD)"
  },
  {
    "id": "hydroxyapatite-3",
    "topic": "Basic apatite (hydroxyapatite) deposition disease",
    "domain": "Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)",
    "discipline": "medicine",
    "stem": "What metabolic workup should be performed for new-onset CPPD or calcium crystal deposition disease?",
    "answer": "Calcium, magnesium, phosphate, PTH, iron studies, TSH, uric acid (screen for hyperparathyroidism, hemochromatosis, hypomagnesemia, hypothyroidism as secondary causes)",
    "rationale": "Secondary causes of CPPD require targeted treatment beyond symptom control; metabolic abnormalities promote pyrophosphate or apatite crystal formation and joint deposition.",
    "bloom": "apply",
    "source": [{"book": "StatPearls", "page": 5}],
    "confusable_with": "uric acid alone (appropriate for gout but insufficient metabolic workup for calcium crystal diseases)"
  }
]

# ── TOPIC 23: Beta-Blocker & Calcium Channel Blocker Toxicity ────────────────
kps += [
  {
    "id": "bb-ccb-tox-1",
    "topic": "Beta-Blocker & Calcium Channel Blocker Toxicity",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "What is the first-line treatment for severe calcium channel blocker toxicity that has emerged as potent therapy by addressing the metabolic deficit?",
    "answer": "Hyperinsulinemic euglycemia (HIE): high-dose insulin (1 unit/kg bolus then 0.5-1 unit/kg/h) with glucose infusion",
    "rationale": "CCB toxicity shifts myocardial substrate preference from free fatty acids to carbohydrates; high-dose insulin overcomes CCB-induced insulin resistance and impaired glucose catabolism, improving cardiac output.",
    "bloom": "apply",
    "source": [{"book": "StatPearls: StatPearls   Beta Blocker & Calcium Channel Blocker Toxicity", "page": 5}],
    "confusable_with": "calcium salts alone (initial measure but insufficient for severe toxicity; HIE is more potent for reversing cardiac depression)"
  },
  {
    "id": "bb-ccb-tox-2",
    "topic": "Beta-Blocker & Calcium Channel Blocker Toxicity",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "Why are conventional decontamination methods (hemodialysis, urinary alkalinization) ineffective for CCB toxicity?",
    "answer": "Due to CCBs' large volume of distribution and lipophilic nature; whole bowel irrigation is used for extended-release preparations",
    "rationale": "Highly lipophilic drugs with large Vd are not effectively removed by dialysis or enhanced excretion; WBI mechanically clears extended-release tablets before systemic absorption is complete.",
    "bloom": "apply",
    "source": [{"book": "StatPearls: StatPearls   Beta Blocker & Calcium Channel Blocker Toxicity", "page": 4}],
    "confusable_with": "salicylate toxicity where urinary alkalinization is effective (salicylates have small Vd and are renally eliminated)"
  },
  {
    "id": "bb-ccb-tox-3",
    "topic": "Beta-Blocker & Calcium Channel Blocker Toxicity",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "Initial bradycardia and hypotension should prompt consideration of what differential diagnosis beyond CCB toxicity?",
    "answer": "Beta-blocker toxicity, tricyclic antidepressant toxicity, sedative-hypnotic toxicity, organophosphate poisoning",
    "rationale": "Multiple drug classes cause bradycardia plus hypotension; toxicology consultation and systematic approach are essential as treatments differ (e.g., atropine for organophosphates, TCA management differs from CCB).",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Beta Blocker & Calcium Channel Blocker Toxicity", "page": 7}],
    "confusable_with": "CCB toxicity as only cause of bradycardia + hypotension (multiple toxidromes share this presentation)"
  },
  {
    "id": "bb-ccb-tox-4",
    "topic": "Beta-Blocker & Calcium Channel Blocker Toxicity",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "What is a theoretical concern about IV calcium administration in digoxin toxicity, and how does clinical evidence address it?",
    "answer": "Theoretical concern: calcium potentiates digoxin's inotropic effect causing irreversible stone heart (non-contractile diastolic arrest); however, multiple clinical studies have NOT confirmed this concern in practice",
    "rationale": "The stone heart theory arose from mechanistic reasoning but lacks RCT evidence; calcium may be used carefully in digoxin-toxic hyperkalemia though caution is still exercised.",
    "bloom": "analyze",
    "source": [{"book": "StatPearls: StatPearls   Digoxin Toxicity", "page": 8}],
    "confusable_with": "calcium absolutely contraindicated in digoxin toxicity (the concern is theoretical; clinical evidence does not confirm the risk)"
  },
  {
    "id": "bb-ccb-tox-5",
    "topic": "Beta-Blocker & Calcium Channel Blocker Toxicity",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "For refractory shock from CCB or BB toxicity not responding to pharmacologic measures, what rescue intervention should be considered?",
    "answer": "Veno-arterial ECMO (VA-ECMO)",
    "rationale": "ECMO provides mechanical circulatory support bypassing the severely depressed cardiac output from CCB/BB toxicity; it is a bridge to recovery as drug effects dissipate.",
    "bloom": "apply",
    "source": [{"book": "StatPearls: StatPearls   Beta Blocker & Calcium Channel Blocker Toxicity", "page": 7}],
    "confusable_with": "IABP (can be used but less effective for cardiogenic shock from CCB than ECMO in severe cases)"
  },
  {
    "_type": "illness_script",
    "topic": "Beta-Blocker & Calcium Channel Blocker Toxicity",
    "discipline": "medicine",
    "enabling_conditions": "Intentional overdose, dosing error in elderly, extended-release formulations causing delayed peak toxicity",
    "pathophysiology": "CCBs block L-type Ca channels reducing myocardial contractility and conduction; BBs block beta-1 receptors causing negative chronotropy/inotropy; both impair mitochondrial oxidative metabolism",
    "time_course": "Immediate-release: toxicity within 1-2h; extended-release: delayed 6-12h, potential biphasic course",
    "key_features": "Bradycardia, hypotension, heart block, hyperglycemia (CCBs > BBs); CCBs cause more metabolic derangement; BBs cause more bronchospasm",
    "consequence_if_missed": "Refractory cardiogenic shock, complete heart block, cardiac arrest; extended-release formulations cause delayed deterioration after initial stability"
  }
]

# ── TOPIC 24: Beta-lactam allergy evaluation & penicillin skin testing ────────
kps += [
  {
    "id": "betalactam-allergy-1",
    "topic": "Beta-lactam allergy evaluation & penicillin skin testing",
    "domain": "Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)",
    "discipline": "medicine",
    "stem": "What is the negative predictive value of penicillin skin testing, and what is the contraindication to graded rechallenge?",
    "answer": "NPV = 95%; contraindicated in severe non-IgE-mediated reactions (DRESS, Stevens-Johnson syndrome, TEN)",
    "rationale": "Skin testing evaluates IgE-specific antibodies only; for severe T-cell mediated reactions (SJS/TEN, DRESS), provocation rechallenge risks potentially fatal re-exposure without the protection skin testing provides.",
    "bloom": "recall",
    "source": [{"book": "MGH Housestaff Manual", "page": 192}],
    "confusable_with": "graded challenge contraindicated for all drug reactions (only severe non-IgE reactions are absolute contraindications)"
  },
  {
    "id": "betalactam-allergy-2",
    "topic": "Beta-lactam allergy evaluation & penicillin skin testing",
    "domain": "Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)",
    "discipline": "medicine",
    "stem": "First and second generation cephalosporins have similar side chains with which other antibiotic class that creates cross-reactivity risk?",
    "answer": "Penicillins (shared R1 side chain similarity with 1st and 2nd generation cephalosporins); true cross-reactivity rate is much lower than historically quoted 10%",
    "rationale": "Cross-reactivity between penicillins and cephalosporins is due to similar R1 side chains rather than the beta-lactam ring; modern estimates of clinically significant cross-reactivity are approximately 1-2%, not 10%.",
    "bloom": "apply",
    "source": [{"book": "Stanford CA-1", "page": 92}],
    "confusable_with": "all cephalosporins equally cross-reactive with penicillin (only 1st/2nd gen share structural similarity; 3rd/4th gen have different side chains)"
  },
  {
    "id": "betalactam-allergy-3",
    "topic": "Beta-lactam allergy evaluation & penicillin skin testing",
    "domain": "Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)",
    "discipline": "medicine",
    "stem": "Apparent allergic reactions to amide local anesthetics (e.g., lidocaine) are most often caused by what component other than the active drug?",
    "answer": "Methylparaben preservative in multi-dose vials — reactions often disappear when preservative-free formulations are used",
    "rationale": "Amide local anesthetic allergy is rare; most apparent reactions are to preservatives (methylparaben, which resembles PABA — the true allergen in ester local anesthetics), explaining false-positive skin tests.",
    "bloom": "analyze",
    "source": [{"book": "Morgan & Mikhail", "page": 432}],
    "confusable_with": "true allergy to the local anesthetic molecule itself (preservative is the more common cause of apparent reactions)"
  },
  {
    "id": "betalactam-allergy-4",
    "topic": "Beta-lactam allergy evaluation & penicillin skin testing",
    "domain": "Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)",
    "discipline": "medicine",
    "stem": "When should outpatient referral for penicillin skin testing be considered for an inpatient with unclear penicillin allergy?",
    "answer": "When the reaction is unclear AND the patient is likely to need that drug class in the future",
    "rationale": "Inpatient de-labeling of penicillin allergy via skin testing reduces unnecessary use of broader-spectrum antibiotics; outpatient referral is appropriate when hospitalization does not allow full evaluation.",
    "bloom": "apply",
    "source": [{"book": "MGH Housestaff Manual", "page": 192}],
    "confusable_with": "skin testing all patients who report any penicillin reaction (targeted approach based on likely future need is more practical)"
  }
]

print(f"Batch 5: {len(kps)} entries")
with open("C:/Users/Dean/anesthesia_attending/data/_kp_batch5.json", "w", encoding="utf-8") as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Written to _kp_batch5.json")
