import json

kps = []

# ── TOPIC 11: Anticholinergic Toxidrome ──────────────────────────────────────
kps += [
  {
    "id": "anticholinergic-1",
    "topic": "Anticholinergic Toxidrome",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "What are the cardinal general findings of the anticholinergic toxidrome?",
    "answer": "Hyperthermia and anhidrosis (dry, flushed skin), along with tachycardia, mydriasis, urinary retention, constipation, and delirium",
    "rationale": "Muscarinic receptor blockade reduces exocrine secretions (dry skin/mouth), impairs thermoregulation (anhidrosis with hyperthermia), and causes tachycardia, mydriasis, and CNS effects.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Anticholinergic Toxidrome", "page": 3}],
    "confusable_with": "sympathomimetic toxidrome (also causes tachycardia and diaphoresis — key difference: anticholinergic causes DRY skin, sympathomimetic causes diaphoresis)"
  },
  {
    "id": "anticholinergic-2",
    "topic": "Anticholinergic Toxidrome",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "More than how many medications have some level of anticholinergic activity?",
    "answer": "More than 600 medications",
    "rationale": "Anticholinergic properties are widespread across drug classes; in most cases these are adverse rather than therapeutic effects, contributing to anticholinergic burden in polypharmacy patients.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Anticholinergic Toxidrome", "page": 2}],
    "confusable_with": "only classically anticholinergic drugs (atropine, scopolamine) — far more medications contribute to anticholinergic burden"
  },
  {
    "id": "anticholinergic-3",
    "topic": "Anticholinergic Toxidrome",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "Why are patients with dementia particularly vulnerable to anticholinergic drug effects?",
    "answer": "Dementia correlates with reduced brain acetylcholine; anticholinergics further deplete cholinergic neurotransmission, worsening cognition",
    "rationale": "Alzheimer disease involves basal forebrain cholinergic neuron loss; any additional cholinergic blockade dramatically worsens cognitive function in these patients.",
    "bloom": "analyze",
    "source": [{"book": "StatPearls: StatPearls   Anticholinergic Toxidrome", "page": 4}],
    "confusable_with": "delirium from any cause (anticholinergic contribution specifically worsens in low-ACh states)"
  },
  {
    "id": "anticholinergic-4",
    "topic": "Anticholinergic Toxidrome",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "What four comorbidities are negatively impacted by anticholinergic drugs and are prevalent in elderly populations?",
    "answer": "Glaucoma, hyperthyroidism, tachyarrhythmia, and benign prostatic hypertrophy",
    "rationale": "Anticholinergics raise intraocular pressure (narrow-angle glaucoma), exacerbate tachycardia, worsen urinary retention in BPH, and may precipitate thyroid storm by increasing heart rate.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Anticholinergic Toxidrome", "page": 4}],
    "confusable_with": "contraindication list for cholinergic agonists (opposite — these are indications for anticholinergics in some contexts, but relative contraindications for overuse)"
  },
  {
    "id": "anticholinergic-5",
    "topic": "Anticholinergic Toxidrome",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "Which anticholinergic medication is FDA-approved as a sleeping aid?",
    "answer": "Diphenhydramine (H1 antihistamine with significant anticholinergic properties)",
    "rationale": "Diphenhydramine blocks muscarinic receptors causing sedation, but also produces all peripheral anticholinergic side effects; its anticholinergic burden is especially problematic in the elderly.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Anticholinergic Toxidrome", "page": 2}],
    "confusable_with": "benzodiazepines (sedatives/hypnotics without anticholinergic mechanism)"
  }
]

# ── TOPIC 12: Antimicrobial Selection: Aminoglycosides, Fluoroquinolones & Macrolides ─
# Note: chunks are largely off-topic (anesthesia pharmacology). Writing limited KPs from relevant fragments.
kps += [
  {
    "id": "abx-aminoglyc-1",
    "topic": "Antimicrobial Selection: Aminoglycosides, Fluoroquinolones & Macrolides",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "Fluoroquinolones are recommended for outpatient CAP with comorbidities for what reasons?",
    "answer": "Coverage of both typical and atypical organisms, oral bioavailability, convenience of monotherapy, low resistance rates in common CAP pathogens",
    "rationale": "Fluoroquinolones provide broad-spectrum monotherapy for CAP with high oral bioavailability allowing outpatient treatment; IDSA/ATS CAP guidelines endorse their use despite adverse event concerns.",
    "bloom": "apply",
    "source": [{"book": "Society Guideline: Guideline   IDSA ATS 2019 CAP Executive Summary", "page": 8}],
    "confusable_with": "fluoroquinolone use for all CAP (concerns about QT prolongation, vascular events, C. diff restrict use to patients with comorbidities or beta-lactam allergy)"
  },
  {
    "id": "abx-aminoglyc-2",
    "topic": "Antimicrobial Selection: Aminoglycosides, Fluoroquinolones & Macrolides",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What specific risk factors should be evaluated AGAINST choosing fluoroquinolones for CAP treatment?",
    "answer": "Documented beta-lactam or macrolide allergy, cardiac arrhythmia (macrolides), vascular disease (fluoroquinolones), history of C. difficile infection",
    "rationale": "Fluoroquinolones are associated with QT prolongation, tendinopathy, and peripheral neuropathy; C. diff history argues against any broad-spectrum agent; individual risk stratification is required.",
    "bloom": "analyze",
    "source": [{"book": "Society Guideline: Guideline   IDSA ATS 2019 CAP Executive Summary", "page": 8}],
    "confusable_with": "fluoroquinolones always safe in elderly (QT prolongation and tendon rupture risk higher with age)"
  },
  {
    "id": "abx-aminoglyc-3",
    "topic": "Antimicrobial Selection: Aminoglycosides, Fluoroquinolones & Macrolides",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "Azithromycin and clindamycin are second-line agents for what prophylaxis in penicillin-allergic patients, and what are their respective serious adverse effects?",
    "answer": "Dental procedure prophylaxis against infective endocarditis in PCN-allergic patients; azithromycin: QT prolongation/torsades; clindamycin: C. difficile colitis",
    "rationale": "Both are recommended alternatives for patients who cannot receive amoxicillin; clinicians must weigh their respective cardiac and GI toxicity profiles against the infectious risk.",
    "bloom": "apply",
    "source": [{"book": "StatPearls: StatPearls   Infective Endocarditis  Treatment & Surgery", "page": 7}],
    "confusable_with": "cephalexin (first-line PCN-allergy alternative only if allergy is non-anaphylactic; cross-reactivity exists)"
  }
]

# ── TOPIC 13: Antimicrobial Selection: Anaerobic Coverage & Metronidazole ───
kps += [
  {
    "id": "abx-anaerobic-1",
    "topic": "Antimicrobial Selection: Anaerobic Coverage & Metronidazole",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What organisms most commonly colonize the fascial planes in polymicrobial necrotizing fasciitis, and from what source?",
    "answer": "Average 5 pathogens per wound including coliforms and anaerobic bacteria, most originating from bowel or genitourinary flora",
    "rationale": "Polymicrobial necrotizing fasciitis involves synergistic aerobe-anaerobe flora that tracks along fascial planes; source is usually bowel or GU flora, requiring broad-spectrum coverage including anaerobic coverage.",
    "bloom": "recall",
    "source": [{"book": "Society Guideline: Guideline   IDSA 2014 SSTI", "page": 21}],
    "confusable_with": "monomicrobial MRSA fasciitis (different pattern; requires MRSA-specific therapy rather than broad polymicrobial coverage)"
  },
  {
    "id": "abx-anaerobic-2",
    "topic": "Antimicrobial Selection: Anaerobic Coverage & Metronidazole",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "Human bite wound infections involve which organisms that resist first-generation cephalosporins and macrolides?",
    "answer": "Eikenella corrodens — resistant to 1st-gen cephalosporins, macrolides, clindamycin, and aminoglycosides; treat with amoxicillin-clavulanate or ampicillin-sulbactam",
    "rationale": "Human bites combine streptococci, S. aureus, and anaerobes with Eikenella; this organism's resistance profile mandates beta-lactam/beta-lactamase inhibitor combinations.",
    "bloom": "apply",
    "source": [{"book": "Society Guideline: Guideline   IDSA 2014 SSTI", "page": 25}],
    "confusable_with": "dog/cat bites (Pasteurella multocida is the key organism — also treated with amoxicillin-clavulanate but with different resistance profile)"
  },
  {
    "id": "abx-anaerobic-3",
    "topic": "Antimicrobial Selection: Anaerobic Coverage & Metronidazole",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "For penicillin-allergic patients requiring treatment of human bite wounds with Eikenella coverage, what regimen is recommended?",
    "answer": "Fluoroquinolone (ciprofloxacin or levofloxacin) PLUS metronidazole, OR moxifloxacin as single agent",
    "rationale": "Moxifloxacin has both aerobic and anaerobic coverage including Eikenella in a single agent; alternative ciprofloxacin/levofloxacin lack anaerobic coverage, requiring metronidazole addition.",
    "bloom": "apply",
    "source": [{"book": "Society Guideline: Guideline   IDSA 2014 SSTI", "page": 25}],
    "confusable_with": "clindamycin alone (Eikenella is resistant to clindamycin; inadequate for human bite wounds)"
  },
  {
    "id": "abx-anaerobic-4",
    "topic": "Antimicrobial Selection: Anaerobic Coverage & Metronidazole",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "In suspected aspiration pneumonia (VAP setting), what additional antimicrobial coverage should be included beyond MRSA and gram-negative bacilli?",
    "answer": "Empiric coverage for oral anaerobes",
    "rationale": "Aspiration pneumonia introduces mouth flora including anaerobes (Fusobacterium, Peptostreptococcus, Prevotella) into the lung; failure to cover anaerobes risks necrotizing pneumonia and abscess formation.",
    "bloom": "apply",
    "source": [{"book": "StatPearls: StatPearls   Shock  Classification & Pathophysiology", "page": 11}],
    "confusable_with": "treating aspiration pneumonia identically to standard HAP/VAP (anaerobic coverage is specifically added for aspiration)"
  },
  {
    "id": "abx-anaerobic-5",
    "topic": "Antimicrobial Selection: Anaerobic Coverage & Metronidazole",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What clinical features of necrotizing fasciitis distinguish it from cellulitis requiring only antibiotics?",
    "answer": "Pain disproportionate to appearance, failure to respond to antibiotics, woody subcutaneous feel extending beyond skin, systemic toxicity/AMS, edema beyond erythema, crepitus (gas in tissues), bullous lesions",
    "rationale": "Necrotizing fasciitis tracks subfascially and cannot be treated with antibiotics alone; surgical debridement is immediately necessary, and delay significantly increases mortality.",
    "bloom": "analyze",
    "source": [{"book": "Society Guideline: Guideline   IDSA 2014 SSTI", "page": 21}],
    "confusable_with": "severe cellulitis (overlying inflammation may mimic fasciitis early; disproportionate pain and wooden consistency are key discriminators)"
  }
]

# ── TOPIC 14: Antimicrobial Selection: Glycopeptides, Lipopeptides & MRSA Agents ─
kps += [
  {
    "id": "abx-glycopeptide-1",
    "topic": "Antimicrobial Selection: Glycopeptides, Lipopeptides & MRSA Agents",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "MRSA accounts for approximately what percentage of culture-positive infections in critically ill ICU patients?",
    "answer": "Approximately 5% of culture-positive infections in critically ill patients (ranges 2-10% by region)",
    "rationale": "MRSA prevalence in the ICU guides empiric MRSA coverage decisions; the decision to add MRSA coverage should be based on local epidemiology and patient-specific risk factors rather than universal empiric use.",
    "bloom": "recall",
    "source": [{"book": "Society Guideline", "page": 19}],
    "confusable_with": "50% MRSA prevalence (gross overestimate; empiric MRSA coverage for all ICU infections would be overtreatment)"
  },
  {
    "id": "abx-glycopeptide-2",
    "topic": "Antimicrobial Selection: Glycopeptides, Lipopeptides & MRSA Agents",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What are the IV oral MRSA treatment options for cellulitis with penetrating trauma or purulent drainage?",
    "answer": "IV: vancomycin, daptomycin, linezolid, or telavancin; Oral: doxycycline, clindamycin, or TMP-SMX",
    "rationale": "Standard cellulitis due to MRSA is uncommon (beta-lactams effective in 96% of routine cellulitis); MRSA-specific agents are reserved for circumstances with higher MRSA likelihood (penetrating trauma, IV drug use, purulent drainage).",
    "bloom": "recall",
    "source": [{"book": "Society Guideline: Guideline   IDSA 2014 SSTI", "page": 16}],
    "confusable_with": "vancomycin for all cellulitis (MRSA coverage usually unnecessary in routine non-purulent cellulitis)"
  },
  {
    "id": "abx-glycopeptide-3",
    "topic": "Antimicrobial Selection: Glycopeptides, Lipopeptides & MRSA Agents",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "When both MRSA and streptococcal coverage are desired for oral therapy, what options achieve this dual coverage?",
    "answer": "Clindamycin alone, OR TMP-SMX plus a beta-lactam, OR doxycycline plus a beta-lactam",
    "rationale": "TMP-SMX and doxycycline cover MRSA but have limited streptococcal activity; adding a beta-lactam adds streptococcal coverage; clindamycin covers both (but check local MRSA clindamycin resistance rates).",
    "bloom": "apply",
    "source": [{"book": "Society Guideline: Guideline   IDSA 2014 SSTI", "page": 16}],
    "confusable_with": "TMP-SMX alone (covers MRSA but inadequate streptococcal coverage for mixed SSTI)"
  },
  {
    "id": "abx-glycopeptide-4",
    "topic": "Antimicrobial Selection: Glycopeptides, Lipopeptides & MRSA Agents",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "MRSA pneumonia commonly follows what viral illness and progresses via what mechanism?",
    "answer": "Follows influenza (enhanced bacterial adhesion and toxin production after viral epithelial damage); resistance via mecA gene; can cause necrotizing pneumonia, bacteremia, sepsis",
    "rationale": "Post-influenza MRSA pneumonia exploits damaged respiratory epithelium; mecA-mediated methicillin resistance requires glycopeptide or alternative MRSA-specific therapy.",
    "bloom": "apply",
    "source": [{"book": "StatPearls", "page": 7}],
    "confusable_with": "community-acquired MSSA pneumonia (may respond to beta-lactams; MRSA requires targeted therapy)"
  }
]

# ── TOPIC 15: Antimicrobial Stewardship ─────────────────────────────────────
# Chunks for this topic are off-topic (ARDS/critical care chunks mislabeled). Writing 3 minimal KPs from the most relevant retrieved content.
kps += [
  {
    "id": "abx-stewardship-1",
    "topic": "Antimicrobial Stewardship",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What duration of antibiotics is recommended for most bacterial skin and soft tissue infections?",
    "answer": "7-14 days",
    "rationale": "IDSA SSTI guidelines specify 7-14 days as appropriate for most bacterial SSTIs, promoting stewardship by avoiding unnecessarily prolonged courses that increase resistance and C. diff risk.",
    "bloom": "recall",
    "source": [{"book": "Society Guideline: Guideline   IDSA 2014 SSTI", "page": 32}],
    "confusable_with": "14-21 days empirically (excessive duration promotes resistance without additional benefit for uncomplicated SSTIs)"
  },
  {
    "id": "abx-stewardship-2",
    "topic": "Antimicrobial Stewardship",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What two considerations define the decision to add MRSA empiric coverage in sepsis and septic shock?",
    "answer": "Likelihood that infection is caused by MRSA AND the risk of harm of withholding (or adding) MRSA treatment for that patient",
    "rationale": "Stewardship principles require risk-benefit analysis: MRSA is only ~5% of ICU infections; universal empiric MRSA coverage over-treats 95% of patients while adding nephrotoxicity and cost.",
    "bloom": "analyze",
    "source": [{"book": "Society Guideline", "page": 19}],
    "confusable_with": "adding MRSA coverage empirically to all septic shock patients (not supported; reserve for high-risk circumstances)"
  },
  {
    "id": "abx-stewardship-3",
    "topic": "Antimicrobial Stewardship",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "In VAP, what should be done within 72 hours if the patient fails to improve or deteriorates despite appropriate antibiotic therapy?",
    "answer": "Evaluate for complications (empyema, abscess, metastatic infection) or an alternative diagnosis/source of infection; consider broadening or changing antibiotics based on culture data",
    "rationale": "Stewardship principles require reassessment; failure to improve indicates either inadequate coverage, wrong diagnosis, or a complication rather than simply continuing or escalating empirically.",
    "bloom": "apply",
    "source": [{"book": "StatPearls: StatPearls   Shock  Classification & Pathophysiology", "page": 11}],
    "confusable_with": "continuing same regimen for 7 days regardless of response (delays recognition of treatment failure or complications)"
  }
]

# ── TOPIC 16: Antiphospholipid Syndrome ──────────────────────────────────────
kps += [
  {
    "id": "aps-1",
    "topic": "Antiphospholipid syndrome",
    "domain": "Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)",
    "discipline": "medicine",
    "stem": "What three laboratory antibodies define antiphospholipid antibody positivity for APS classification?",
    "answer": "Lupus anticoagulant, anticardiolipin antibodies (IgG or IgM), anti-beta2-glycoprotein I antibodies (IgG or IgM)",
    "rationale": "APS requires antiphospholipid antibodies directed against phospholipid-binding proteins; all three categories must be considered for complete workup. At least one must be positive on two occasions >=12 weeks apart.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Antiphospholipid syndrome", "page": 9}],
    "confusable_with": "anti-dsDNA (SLE-specific; not an APS diagnostic antibody)"
  },
  {
    "id": "aps-2",
    "topic": "Antiphospholipid syndrome",
    "domain": "Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)",
    "discipline": "medicine",
    "stem": "APS is characterized by what two major clinical manifestations?",
    "answer": "Thrombosis (venous and/or arterial) and/or recurrent pregnancy loss/complications",
    "rationale": "Antiphospholipid antibodies promote thrombosis via multiple mechanisms (platelet activation, endothelial injury, complement activation); obstetric APS causes placental thrombosis leading to pregnancy loss.",
    "bloom": "recall",
    "source": [{"book": "Miller/Baby Miller", "page": 446}],
    "confusable_with": "SLE alone (can have APS antibodies but without thrombosis/pregnancy loss does not meet APS criteria)"
  },
  {
    "id": "aps-3",
    "topic": "Antiphospholipid syndrome",
    "domain": "Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)",
    "discipline": "medicine",
    "stem": "For APS antibody test to be diagnostic, how many positive tests on how many occasions are required and what is the minimum time between them?",
    "answer": "Positive on 2 or more occasions at least 12 weeks apart",
    "rationale": "Single positive tests may be transiently positive in infections; persistence on two occasions 12 weeks apart confirms true pathologic antibody.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Antiphospholipid syndrome", "page": 9}],
    "confusable_with": "single positive test being diagnostic (transient false-positives occur)"
  },
  {
    "id": "aps-4",
    "topic": "Antiphospholipid syndrome",
    "domain": "Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)",
    "discipline": "medicine",
    "stem": "In a patient with APS who requires surgery, what is the greatest perioperative anticoagulation challenge?",
    "answer": "Balancing thrombosis risk from APS (requires anticoagulation) against surgical bleeding risk; bridging strategies must address the prothrombotic state specific to APS",
    "rationale": "APS patients on long-term anticoagulation have extreme thrombotic risk perioperatively; the use of anticoagulants remains controversial and should be guided by thrombotic risk level.",
    "bloom": "analyze",
    "source": [{"book": "Miller/Baby Miller", "page": 446}],
    "confusable_with": "standard bridging for afib (APS thrombotic risk is higher and approach differs from routine AF bridging)"
  },
  {
    "_type": "illness_script",
    "topic": "Antiphospholipid syndrome",
    "discipline": "medicine",
    "enabling_conditions": "Autoimmune disease (especially SLE), infection-triggered, drug-induced; may be primary (no underlying disease)",
    "pathophysiology": "Antiphospholipid antibodies activate platelets and endothelium, inhibit natural anticoagulant pathways (protein C, annexin V), activate complement — net prothrombotic state",
    "time_course": "Chronic autoimmune condition with episodic thrombotic events; catastrophic APS (CAPS) is rapid multi-organ thrombosis",
    "key_features": "Unexplained venous/arterial thrombosis in young patients, recurrent pregnancy loss, positive antiphospholipid antibodies x2 (12 weeks apart)",
    "consequence_if_missed": "Recurrent thromboembolism, stroke, catastrophic multi-organ failure; obstetric morbidity including fetal loss"
  }
]

print(f"Batch 3: {len(kps)} entries")
with open("C:/Users/Dean/anesthesia_attending/data/_kp_batch3.json", "w", encoding="utf-8") as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Written to _kp_batch3.json")
