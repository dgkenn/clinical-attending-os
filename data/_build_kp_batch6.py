import json

kps = []

# ── TOPIC 25: Bloodstream Infections & Bacteremia ───────────────────────────
kps += [
  {
    "id": "bacteremia-1",
    "topic": "Bloodstream Infections & Bacteremia",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What is the most common gram-positive and gram-negative organism causing bacteremia overall?",
    "answer": "Gram-positive: Staphylococcus aureus; Gram-negative: Escherichia coli (most common gram-negative community-acquired bacteremia)",
    "rationale": "S. aureus is the dominant gram-positive bloodstream pathogen due to its virulence and biofilm-forming ability; E. coli dominates community-acquired gram-negative bacteremia especially from urinary sources.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Bloodstream Infections & Bacteremia", "page": 2}],
    "confusable_with": "coagulase-negative Staphylococcus (CoNS) as most common gram-positive (CoNS is most common in nosocomial line-associated bacteremia, but S. aureus has higher virulence and mortality)"
  },
  {
    "id": "bacteremia-2",
    "topic": "Bloodstream Infections & Bacteremia",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What clinical signs/symptoms predict bacteremia on blood culture ordering, and which situations have the highest culture positivity rates?",
    "answer": "Highest yield: septic shock (38-69% positive), meningitis (53%); medium: pyelonephritis (19-25%); low: cellulitis (2%), CAP (7%); rigors (+LR 4.7) most predictive",
    "rationale": "Blood culture yield correlates with infection severity and source; rigors indicate high-grade bacteremia; cellulitis rarely produces bacteremia so routine cultures are low yield and contribute to overuse.",
    "bloom": "analyze",
    "source": [{"book": "MGH Housestaff Manual", "page": 122}],
    "confusable_with": "ordering blood cultures for all febrile patients (selective criteria based on pre-test probability improves stewardship)"
  },
  {
    "id": "bacteremia-3",
    "topic": "Bloodstream Infections & Bacteremia",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What is the minimum number of blood culture sets recommended, and when should they be drawn?",
    "answer": "Minimum 2 sets; drawn PRIOR to antibiotic administration",
    "rationale": "Two sets increase sensitivity for detecting bacteremia over a single set; pre-antibiotic cultures maximize pathogen recovery; delayed cultures after antibiotic exposure dramatically reduce yield.",
    "bloom": "recall",
    "source": [{"book": "MGH Housestaff Manual", "page": 122}],
    "confusable_with": "1 set being sufficient (single set has ~70% sensitivity; 2 sets increase sensitivity to ~90%)"
  },
  {
    "id": "bacteremia-4",
    "topic": "Bloodstream Infections & Bacteremia",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "Which bloodstream pathogens are associated with highest mortality and require the most aggressive management?",
    "answer": "S. aureus, Pseudomonas aeruginosa, and Enterobacter species are associated with higher mortality than other bacteremic organisms",
    "rationale": "These high-virulence organisms cause rapid clinical deterioration; S. aureus bacteremia requires echocardiography to exclude endocarditis; P. aeruginosa requires anti-pseudomonal therapy.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Bloodstream Infections & Bacteremia", "page": 4}],
    "confusable_with": "coagulase-negative Staphylococcus (often a contaminant; lower virulence than S. aureus)"
  },
  {
    "id": "bacteremia-5",
    "topic": "Bloodstream Infections & Bacteremia",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What transition from asymptomatic bacteremia to clinical disease determines when bacteremia becomes a bloodstream infection requiring treatment?",
    "answer": "When immune response mechanisms fail or become overwhelmed, bacteremia evolves to septicemia/bloodstream infection requiring treatment; asymptomatic bacteremia (e.g., after dental brushing) is usually transient and benign",
    "rationale": "Brief, low-grade bacteremia from minor procedures is handled by immune clearance in healthy hosts; persistent or high-grade bacteremia in immunocompromised or structurally abnormal hosts progresses to sepsis.",
    "bloom": "analyze",
    "source": [{"book": "StatPearls: StatPearls   Bloodstream Infections & Bacteremia", "page": 1}],
    "confusable_with": "treating all bacteremia (asymptomatic transient bacteremia from daily activities does not require antibiotics)"
  }
]

# ── TOPIC 26: Brain Death & Disorders of Consciousness ───────────────────────
# Chunks are almost entirely about trinucleotide repeat disorders (mislabeled).
# Only Marino ICU Book p.630 is relevant. Writing KPs only from that chunk.
kps += [
  {
    "id": "brain-death-1",
    "topic": "Brain Death & Disorders of Consciousness",
    "domain": "Internal medicine: neurology (ischemic & hemorrhagic stroke, seizures & status epilepticus, altered mental status & delirium, headache, neuromuscular weakness, spinal cord syndromes)",
    "discipline": "medicine",
    "stem": "Consciousness has two components. What are they and how do they define the disorders of consciousness spectrum?",
    "answer": "Arousal (wakefulness — ability to recognize surroundings) and Awareness (ability to understand relationship to surroundings — responsiveness); disorders vary based on which component(s) are impaired",
    "rationale": "Coma = absent arousal and awareness; vegetative state = arousal present, awareness absent; minimally conscious state = arousal present, minimal but reproducible awareness; brain death = absent arousal and awareness with loss of all brainstem reflexes.",
    "bloom": "recall",
    "source": [{"book": "Marino ICU Book", "page": 630}],
    "confusable_with": "sleep (reversible absence of arousal with intact arousal mechanisms; different from pathological disorders of consciousness)"
  },
  {
    "id": "brain-death-2",
    "topic": "Brain Death & Disorders of Consciousness",
    "domain": "Internal medicine: neurology (ischemic & hemorrhagic stroke, seizures & status epilepticus, altered mental status & delirium, headache, neuromuscular weakness, spinal cord syndromes)",
    "discipline": "medicine",
    "stem": "What are the two categories of conditions causing altered consciousness?",
    "answer": "Conditions causing direct brain injury (structural: hemorrhage, infarct, trauma, mass) vs. conditions causing indirect brain dysfunction (metabolic/toxic: hypoxia, hypoglycemia, drugs, sepsis, organ failure)",
    "rationale": "This structural vs. metabolic framework guides workup; structural causes typically show focal deficits and asymmetric pupillary responses; metabolic causes tend to produce symmetric bilateral depression.",
    "bloom": "recall",
    "source": [{"book": "Marino ICU Book", "page": 630}],
    "confusable_with": "all altered consciousness being structural (metabolic/toxic causes are equally common and highly reversible)"
  },
  {
    "id": "brain-death-3",
    "topic": "Brain Death & Disorders of Consciousness",
    "domain": "Internal medicine: neurology (ischemic & hemorrhagic stroke, seizures & status epilepticus, altered mental status & delirium, headache, neuromuscular weakness, spinal cord syndromes)",
    "discipline": "medicine",
    "stem": "Delirium is a disorder of consciousness distinct from dementia. What is its defining clinical characteristic compared to coma?",
    "answer": "Delirium is an acute fluctuating disturbance in attention and awareness with altered cognition; unlike coma, delirium patients are arousable but confused and inattentive",
    "rationale": "Delirium represents an acute, reversible encephalopathy superimposed on baseline cognition; unlike coma it has preserved arousal; it is extremely common in ICU and associated with increased mortality.",
    "bloom": "apply",
    "source": [{"book": "Marino ICU Book", "page": 630}],
    "confusable_with": "dementia (chronic, progressive; delirium is acute and fluctuating and often reversible)"
  }
]

# ── TOPIC 27: Carbon Monoxide Poisoning ──────────────────────────────────────
kps += [
  {
    "id": "co-poisoning-1",
    "topic": "Carbon Monoxide Poisoning",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "What is the affinity of carbon monoxide for hemoglobin compared to oxygen, and what are its two mechanisms of toxicity?",
    "answer": "CO has 200-300 times the affinity of O2 for hemoglobin; toxicity: (1) reduces O2-carrying capacity by forming carboxyhemoglobin, (2) impairs O2 release to tissues (shifts oxyhemoglobin dissociation curve left)",
    "rationale": "CO outcompetes O2 for heme binding; carboxyhemoglobin both reduces total O2 content and shifts the remaining oxyhemoglobin dissociation curve left (increased hemoglobin-O2 affinity), severely impairing tissue oxygen delivery.",
    "bloom": "recall",
    "source": [{"book": "Morgan & Mikhail", "page": 841}],
    "confusable_with": "methemoglobin (also reduces O2-carrying capacity but different oxidation state; different treatment — methylene blue)"
  },
  {
    "id": "co-poisoning-2",
    "topic": "Carbon Monoxide Poisoning",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "Why does pulse oximetry fail to detect carbon monoxide poisoning, and what tool does detect it?",
    "answer": "Standard pulse oximetry uses only 2 wavelengths; carboxyhemoglobin and oxyhemoglobin absorb similarly at 660 nm — SpO2 reads falsely normal; diagnosis requires arterial blood gas co-oximetry measuring COHb directly",
    "rationale": "Two-wavelength oximeters cannot distinguish HbCO from HbO2; co-oximetry on ABG uses multiple wavelengths to identify and quantify all hemoglobin species including carboxyhemoglobin.",
    "bloom": "apply",
    "source": [{"book": "Morgan & Mikhail", "page": 192}],
    "confusable_with": "relying on SpO2 to exclude CO poisoning (SpO2 is falsely normal in CO poisoning)"
  },
  {
    "id": "co-poisoning-3",
    "topic": "Carbon Monoxide Poisoning",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "Carbon monoxide poisoning is a common complication of what type of injury, and what other concurrent toxicity should be considered?",
    "answer": "Smoke inhalation injury; cyanide poisoning (especially from combustion of synthetic materials/polyurethane) should be co-suspected",
    "rationale": "Smoke contains both CO and cyanide from burning synthetic polymers; both impair cellular oxygen utilization — CO at the hemoglobin level, cyanide at cytochrome oxidase in the mitochondria.",
    "bloom": "apply",
    "source": [{"book": "Morgan & Mikhail", "page": 2135}],
    "confusable_with": "CO poisoning alone (in structural fires with synthetics, cyanide poisoning is equally likely and requires hydroxocobalamin treatment)"
  },
  {
    "id": "co-poisoning-4",
    "topic": "Carbon Monoxide Poisoning",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "During general anesthesia with volatile agents, how can CO poisoning be identified, and what is a preventable intraoperative source?",
    "answer": "Presence of carboxyhemoglobin on ABG or lower-than-expected SpO2; preventable source: desiccated CO2 absorbent (especially barium hydroxide lime) degrades volatile agents (particularly desflurane) into CO",
    "rationale": "Desiccated CO2 absorbents (left dry over weekends) react with volatile agents to produce clinically significant CO; using calcium hydroxide (Amsorb) or replacing dried absorbent eliminates this risk.",
    "bloom": "apply",
    "source": [{"book": "Morgan & Mikhail", "page": 268}],
    "confusable_with": "ambient CO exposure only (an intraoperative source via degraded absorbent is a known anesthesia-specific hazard)"
  },
  {
    "id": "co-poisoning-5",
    "topic": "Carbon Monoxide Poisoning",
    "domain": "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)",
    "discipline": "medicine",
    "stem": "Cyanide toxicity presents with what clinical pattern and metabolic finding, distinct from pure CO poisoning?",
    "answer": "Neurological impairment, lactic acidosis (elevated lactate), arrhythmias, increased cardiac output, marked vasodilation — due to mitochondrial cytochrome oxidase inhibition",
    "rationale": "Cyanide blocks aerobic metabolism at complex IV; cells shift to anaerobic glycolysis producing lactic acidosis; CO causes hemoglobin-based O2 deficiency without the profound lactic acidosis pattern.",
    "bloom": "analyze",
    "source": [{"book": "Morgan & Mikhail", "page": 2136}],
    "confusable_with": "CO poisoning alone (CO does not characteristically cause the profound lactic acidosis seen with cyanide)"
  },
  {
    "_type": "illness_script",
    "topic": "Carbon Monoxide Poisoning",
    "discipline": "medicine",
    "enabling_conditions": "Smoke inhalation, malfunctioning combustion appliances (furnaces, space heaters), vehicle exhaust in enclosed spaces, intraoperative desiccated CO2 absorbent",
    "pathophysiology": "CO binds hemoglobin with 200-300x affinity of O2 forming carboxyhemoglobin; reduces O2 carrying capacity and impairs tissue O2 release; also binds mitochondrial cytochrome oxidase causing histotoxic hypoxia",
    "time_course": "Acute exposure: minutes to hours; tissue hypoxia develops rapidly; delayed neurological sequelae possible after apparent recovery",
    "key_features": "Headache, confusion, normal SpO2 (falsely), carboxyhemoglobin >20% on ABG co-oximetry; cherry-red skin (unreliable sign)",
    "consequence_if_missed": "Cardiac arrest, neurological injury, delayed cognitive sequelae; hyperbaric oxygen reduces delayed neurological effects"
  }
]

# ── TOPIC 28: Catheter-Associated UTI (CAUTI) ────────────────────────────────
kps += [
  {
    "id": "cauti-1",
    "topic": "Catheter-Associated UTI (CAUTI)",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What are the diagnostic criteria for CAUTI (two requirements)?",
    "answer": "(1) Signs/symptoms of UTI with no other identified source of infection AND (2) urine culture with >=1 uropathogen at >10^3 CFU/mL from a catheterized specimen (catheter in place >2 days) or midstream urine within 48h of catheter removal",
    "rationale": "CAUTI requires both clinical and microbiological criteria to avoid over-diagnosis; asymptomatic bacteriuria with a catheter in place is NOT CAUTI and should NOT be treated in most patients.",
    "bloom": "recall",
    "source": [{"book": "MGH Housestaff Manual", "page": 119}],
    "confusable_with": "asymptomatic bacteriuria in catheterized patients (should NOT be treated except in pregnant women or pre-urologic procedures)"
  },
  {
    "id": "cauti-2",
    "topic": "Catheter-Associated UTI (CAUTI)",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What are the two routes of CAUTI infection (extraluminal and intraluminal)?",
    "answer": "Extraluminal: bacterial migration along catheter outer surface from urethral meatus to bladder; Intraluminal: ascending infection through contaminated catheter lumen from urine stasis or open drainage system",
    "rationale": "Understanding these routes guides prevention: sterile technique during insertion prevents intraluminal contamination; maintaining intact closed drainage system prevents extraluminal migration.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Shock  Classification & Pathophysiology", "page": 6}],
    "confusable_with": "hematogenous seeding of catheter (uncommon; CAUTI is predominantly ascending from periurethral flora)"
  },
  {
    "id": "cauti-3",
    "topic": "Catheter-Associated UTI (CAUTI)",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "What is the most common organism causing CAUTI, and what other common pathogens are involved?",
    "answer": "E. coli most common, followed by Klebsiella pneumoniae/oxytoca and Enterococcus; fecal and skin flora predominate",
    "rationale": "Periurethral and perineal flora are the source of most CAUTI organisms; E. coli from GI flora is the dominant pathogen; biofilm formation on catheter surfaces facilitates colonization and persistence.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Shock  Classification & Pathophysiology", "page": 6}],
    "confusable_with": "S. aureus as primary CAUTI organism (S. aureus causes catheter-related bloodstream infection more than UTI)"
  },
  {
    "id": "cauti-4",
    "topic": "Catheter-Associated UTI (CAUTI)",
    "domain": "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)",
    "discipline": "medicine",
    "stem": "Approximately what percentage of hospitalized patients in the US receive a urinary catheter, and what does this imply for CAUTI prevention?",
    "answer": "15-25% of hospitalized patients; early catheter removal and judicious catheter use are the primary prevention strategies (no single strategy fully prevents CAUTI)",
    "rationale": "The high catheter insertion rate makes CAUTI the most common hospital-acquired infection; duration of catheterization is the strongest risk factor, making early removal the most impactful intervention.",
    "bloom": "recall",
    "source": [{"book": "StatPearls: StatPearls   Shock  Classification & Pathophysiology", "page": 6}],
    "confusable_with": "antibiotic prophylaxis preventing CAUTI (prophylactic antibiotics do not prevent CAUTI and promote resistance)"
  }
]

print(f"Batch 6: {len(kps)} entries")
with open("C:/Users/Dean/anesthesia_attending/data/_kp_batch6.json", "w", encoding="utf-8") as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Written to _kp_batch6.json")
