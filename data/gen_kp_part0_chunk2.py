import json

kps = []

# ── 11: Anticholinergic Toxidrome ─────────────────────────────────────────────
kps += [
  {"id":"anticholinergic-1","topic":"Anticholinergic Toxidrome","domain":"Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)","discipline":"medicine",
   "stem":"A patient has hyperthermia, anhidrosis, mydriasis, tachycardia, urinary retention, and confusion. Which toxidrome does this represent?",
   "answer":"Anticholinergic toxidrome (hot, dry, blind, mad, tachycardic, urinary retention).",
   "rationale":"These are the classic peripheral and central manifestations of muscarinic receptor blockade: loss of cholinergic tone produces anhidrosis, mydriasis, tachycardia, ileus, and urinary retention.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Anticholinergic Toxidrome","page":3}],"confusable_with":"Sympathomimetic toxidrome (also hot/tachycardic but diaphoretic)"},
  {"id":"anticholinergic-2","topic":"Anticholinergic Toxidrome","domain":"Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)","discipline":"medicine",
   "stem":"Which patient population is particularly vulnerable to adverse anticholinergic effects from medications?",
   "answer":"Elderly patients with dementia, glaucoma, hyperthyroidism, tachyarrhythmias, or prostatic hypertrophy.",
   "rationale":"Dementia is associated with reduced brain acetylcholine; anticholinergic burden worsens cognitive impairment. Glaucoma, BPH, and tachyarrhythmia are directly exacerbated by muscarinic blockade.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Anticholinergic Toxidrome","page":4}],"confusable_with":""},
  {"id":"anticholinergic-3","topic":"Anticholinergic Toxidrome","domain":"Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)","discipline":"medicine",
   "stem":"Anticholinergic medications are therapeutically useful for which conditions?",
   "answer":"COPD/asthma (ipratropium, tiotropium), Parkinson disease, urge incontinence, cardiovascular arrhythmias, mydriasis, psychiatric disorders.",
   "rationale":"Controlled muscarinic blockade has targeted therapeutic benefits; ipratropium dilates bronchi by blocking M3 receptors; tiotropium provides long-acting bronchodilation.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Anticholinergic Toxidrome","page":2}],"confusable_with":""},
  {"id":"anticholinergic-4","topic":"Anticholinergic Toxidrome","domain":"Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)","discipline":"medicine",
   "stem":"How many medications possess some level of anticholinergic activity?",
   "answer":"More than 600 medications have some anticholinergic activity.",
   "rationale":"The anticholinergic burden is cumulative; polypharmacy in elderly patients dramatically increases the risk of toxicity even from individually low-potency agents.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Anticholinergic Toxidrome","page":2}],"confusable_with":""},
  {"id":"anticholinergic-5","topic":"Anticholinergic Toxidrome","domain":"Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)","discipline":"medicine",
   "stem":"What lab assay can measure overall anticholinergic drug burden?",
   "answer":"Serum anticholinergic assay measures total anticholinergic activity of all substances present.",
   "rationale":"The serum anticholinergic assay can quantify combined burden from multiple medications; useful in complex elderly patients with polypharmacy-induced cognitive decline.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Anticholinergic Toxidrome","page":4}],"confusable_with":""},
  {"_type":"confusable_pair","topic_a":"Anticholinergic toxidrome","topic_b":"Sympathomimetic toxidrome","discriminator":"Anticholinergic: dry skin, anhidrosis, urinary retention, decreased bowel sounds. Sympathomimetic: diaphoretic, hyperactive bowel sounds. Both cause hyperthermia and tachycardia."}
]

# ── 12: Aminoglycosides, Fluoroquinolones & Macrolides ────────────────────────
# Chunks were off-topic anesthesia content — very thin. Write 3 conservative KPs only.
kps += [
  {"id":"amgly-fq-mac-1","topic":"Antimicrobial Selection: Aminoglycosides, Fluoroquinolones & Macrolides","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"Fluoroquinolones carry a specific cardiac risk when used in patients with which condition?",
   "answer":"Cardiac arrhythmia (QT prolongation risk); fluoroquinolones are cautioned in patients with pre-existing arrhythmia.",
   "rationale":"Fluoroquinolones inhibit cardiac hERG K+ channels, prolonging the QT interval and predisposing to torsades de pointes, particularly in patients with underlying arrhythmias.",
   "bloom":"apply","source":[{"book":"Society Guideline: Guideline   IDSA ATS 2019 CAP Executive Summary","page":8}],"confusable_with":"Macrolides (also QT-prolonging)"},
  {"id":"amgly-fq-mac-2","topic":"Antimicrobial Selection: Aminoglycosides, Fluoroquinolones & Macrolides","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"Fluoroquinolone use is associated with increased risk of what vascular complication?",
   "answer":"Vascular disease (aortic aneurysm/dissection risk); fluoroquinolones are cautioned in patients with pre-existing vascular disease.",
   "rationale":"Fluoroquinolones inhibit collagen synthesis via metalloprotease activation; this is associated with aortic aneurysm and dissection in susceptible patients.",
   "bloom":"recall","source":[{"book":"Society Guideline: Guideline   IDSA ATS 2019 CAP Executive Summary","page":8}],"confusable_with":""},
  {"id":"amgly-fq-mac-3","topic":"Antimicrobial Selection: Aminoglycosides, Fluoroquinolones & Macrolides","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"Azithromycin causes what rare but serious cardiac arrhythmia?",
   "answer":"QT prolongation and torsades de pointes.",
   "rationale":"Azithromycin prolongs the cardiac QT interval by inhibiting hERG channels; this rarely leads to torsades de pointes, particularly in patients with other QT-prolonging factors.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Infective Endocarditis  Treatment & Surgery","page":7}],"confusable_with":"Fluoroquinolone-induced QT prolongation"}
]

# ── 13: Anaerobic Coverage & Metronidazole ────────────────────────────────────
kps += [
  {"id":"anaerobic-abx-1","topic":"Antimicrobial Selection: Anaerobic Coverage & Metronidazole","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"In polymicrobial necrotising fasciitis, what is the average number of pathogens cultured from involved fascial planes?",
   "answer":"Average of 5 pathogens; mostly bowel/GU flora (coliforms and anaerobic bacteria).",
   "rationale":"Necrotising fasciitis of the trunk/perineum is characteristically polymicrobial with mixed aerobe-anaerobe flora from bowel; broad anaerobic coverage is mandatory.",
   "bloom":"recall","source":[{"book":"Society Guideline: Guideline   IDSA 2014 SSTI","page":21}],"confusable_with":"Monomicrobial fasciitis (Group A Strep or CA-MRSA)"},
  {"id":"anaerobic-abx-2","topic":"Antimicrobial Selection: Anaerobic Coverage & Metronidazole","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"In suspected aspiration pneumonia with anaerobic organisms, which empiric antimicrobial regimens are recommended?",
   "answer":"Antibiotic regimens should include coverage for oral anaerobes (e.g., beta-lactam/beta-lactamase inhibitor combinations, or metronidazole added to coverage).",
   "rationale":"Aspiration pneumonia frequently involves anaerobes from oral flora; adding anaerobic coverage (metronidazole, clindamycin, or beta-lactamase inhibitor combinations) is standard.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Shock  Classification & Pathophysiology","page":11}],"confusable_with":"Community-acquired pneumonia (anaerobic coverage typically not needed)"},
  {"id":"anaerobic-abx-3","topic":"Antimicrobial Selection: Anaerobic Coverage & Metronidazole","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"Eikenella corrodens (human bite wounds) is resistant to which antibiotics?",
   "answer":"Resistant to first-generation cephalosporins, macrolides, clindamycin, and aminoglycosides; treat with amoxicillin-clavulanate, ampicillin-sulbactam, or ertapenem.",
   "rationale":"Eikenella's resistance profile distinguishes it from typical oral flora; beta-lactam/beta-lactamase inhibitor combinations exploit its susceptibility.",
   "bloom":"recall","source":[{"book":"Society Guideline: Guideline   IDSA 2014 SSTI","page":25}],"confusable_with":"Pasteurella multocida (cat/dog bites, penicillin sensitive)"},
  {"id":"anaerobic-abx-4","topic":"Antimicrobial Selection: Anaerobic Coverage & Metronidazole","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"In necrotising fasciitis, what is the most critical and time-sensitive initial intervention?",
   "answer":"Surgical debridement — antibiotics alone are insufficient; delay increases mortality.",
   "rationale":"The ischaemic/necrotic tissue is avascular and antibiotic penetration is poor; surgical removal of infected tissue is the definitive treatment.",
   "bloom":"apply","source":[{"book":"Society Guideline: Guideline   IDSA 2014 SSTI","page":21}],"confusable_with":"Starting antibiotics first (appropriate but must not delay surgery)"}
]

# ── 14: Glycopeptides, Lipopeptides & MRSA Agents ────────────────────────────
kps += [
  {"id":"glycopep-mrsa-1","topic":"Antimicrobial Selection: Glycopeptides, Lipopeptides & MRSA Agents","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"MRSA pneumonia presents with what radiographic features and what antibiotic class is empirically required?",
   "answer":"Infiltrates or cavitary lesions on imaging; requires empiric MRSA-targeted therapy (e.g., vancomycin or linezolid).",
   "rationale":"MRSA causes necrotising pneumonia with rapid cavitation; beta-lactams are ineffective due to mecA-mediated resistance.",
   "bloom":"apply","source":[{"book":"StatPearls","page":7}],"confusable_with":"MSSA pneumonia (beta-lactam adequate)"},
  {"id":"glycopep-mrsa-2","topic":"Antimicrobial Selection: Glycopeptides, Lipopeptides & MRSA Agents","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"In patients with sepsis, what factors determine whether MRSA coverage is included empirically?",
   "answer":"(1) Likelihood infection is caused by MRSA; (2) risk of harm from withholding MRSA treatment; (3) risk of harm from MRSA-targeted agents (nephrotoxicity, resistance selection).",
   "rationale":"SSC guidelines recommend balancing these three factors rather than empirical MRSA coverage for all sepsis patients, to limit unnecessary glycopeptide exposure.",
   "bloom":"analyze","source":[{"book":"Society Guideline","page":19}],"confusable_with":""},
  {"id":"glycopep-mrsa-3","topic":"Antimicrobial Selection: Glycopeptides, Lipopeptides & MRSA Agents","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"Cellulitis is rarely caused by MRSA, but MRSA coverage may be prudent in which specific scenarios?",
   "answer":"Cellulitis with penetrating trauma (especially IV drug use), purulent drainage, or concurrent MRSA infection elsewhere.",
   "rationale":"Most cellulitis is caused by streptococci and responds to beta-lactams; MRSA cellulitis is uncommon but risk rises with injection drug use, traumatic wounds, or purulent features.",
   "bloom":"apply","source":[{"book":"Society Guideline: Guideline   IDSA 2014 SSTI","page":16}],"confusable_with":""},
  {"id":"glycopep-mrsa-4","topic":"Antimicrobial Selection: Glycopeptides, Lipopeptides & MRSA Agents","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"What is the recommended duration of antibiotic treatment for most bacterial skin and soft-tissue infections?",
   "answer":"7-14 days.",
   "rationale":"IDSA guidelines recommend this duration for most bacterial SSTIs; shorter courses may be adequate for simple infections, longer for necrotising or immunocompromised cases.",
   "bloom":"recall","source":[{"book":"Society Guideline: Guideline   IDSA 2014 SSTI","page":32}],"confusable_with":""}
]

# ── 15: Antimicrobial Stewardship — chunks entirely off-topic (ARDS/pulm) ─────
# Write minimal KPs from the only usable content (society guideline sepsis ARDS mentions)
kps += [
  {"id":"abx-steward-1","topic":"Antimicrobial Stewardship","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"What is the goal of antimicrobial de-escalation after empiric broad-spectrum therapy is initiated?",
   "answer":"Narrow antibiotic coverage based on culture results and clinical response to minimise resistance selection and adverse effects.",
   "rationale":"Prolonged broad-spectrum coverage selects for resistant organisms and increases Clostridioides difficile risk; stewardship programmes mandate de-escalation once a pathogen is identified.",
   "bloom":"apply","source":[{"book":"Society Guideline","page":37}],"confusable_with":"Antibiotic escalation"},
  {"id":"abx-steward-2","topic":"Antimicrobial Stewardship","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"In ARDS management, why is antibiotic use guided by culture results rather than prophylactically initiated?",
   "answer":"Prophylactic antibiotics do not improve outcomes in ARDS/aspiration pneumonitis and select for resistant organisms; cultures guide targeted therapy.",
   "rationale":"Stewardship principles: antibiotics should be initiated when there is evidence of bacterial infection, not as prophylaxis for non-infectious lung injury.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":2125}],"confusable_with":""}
]

# ── 16: Antiphospholipid Syndrome ─────────────────────────────────────────────
kps += [
  {"id":"aps-1","topic":"Antiphospholipid syndrome","domain":"Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)","discipline":"medicine",
   "stem":"What is the clinical definition of antiphospholipid syndrome (APS)?",
   "answer":"Acquired autoimmune disorder characterised by venous and/or arterial thromboses AND/OR recurrent pregnancy loss, with persistent antiphospholipid antibodies.",
   "rationale":"APS requires both clinical (thrombosis or pregnancy morbidity) and laboratory (positive APLA on two occasions ≥12 weeks apart) criteria.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":446}],"confusable_with":"Inherited thrombophilia (factor V Leiden, prothrombin mutation)"},
  {"id":"aps-2","topic":"Antiphospholipid syndrome","domain":"Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)","discipline":"medicine",
   "stem":"The updated 2023 ACR/EULAR APS classification requires an entry criterion of what?",
   "answer":"At least one positive antiphospholipid antibody (APLA) test within 3 years of an APS-associated clinical criterion.",
   "rationale":"The 2023 criteria tightened the temporal link between APLA positivity and clinical events, using a weighted point-based system to improve diagnostic accuracy.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Antiphospholipid syndrome","page":9}],"confusable_with":""},
  {"id":"aps-3","topic":"Antiphospholipid syndrome","domain":"Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)","discipline":"medicine",
   "stem":"Laboratory confirmation of APS requires antibody positivity on how many occasions and how far apart?",
   "answer":"Two or more occasions at least 12 weeks apart.",
   "rationale":"Transient APLA positivity can occur with infections; persistence at 12-week intervals confirms an autoimmune rather than a transient trigger.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Antiphospholipid syndrome","page":9}],"confusable_with":""},
  {"id":"aps-4","topic":"Antiphospholipid syndrome","domain":"Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)","discipline":"medicine",
   "stem":"In APS-associated DIC, why is antifibrinolytic therapy generally contraindicated?",
   "answer":"Antifibrinolytics can cause catastrophic thrombotic complications in APS-DIC because APS already has a strong pro-thrombotic state.",
   "rationale":"DIC in APS involves both clotting and fibrinolytic activation; suppressing fibrinolysis tips the balance toward life-threatening thrombosis in an already pro-coagulant disease.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":446}],"confusable_with":"Non-APS DIC (antifibrinolytics occasionally used for hyperfibrinolysis)"},
  {"id":"aps-5","topic":"Antiphospholipid syndrome","domain":"Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)","discipline":"medicine",
   "stem":"APS is a recognised risk factor in which obstetric complication?",
   "answer":"Pre-eclampsia (and recurrent pregnancy loss/fetal loss).",
   "rationale":"Antiphospholipid antibodies cause placental thrombosis and inflammation, predisposing to early and late pregnancy losses, pre-eclampsia, and IUGR.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":620}],"confusable_with":""},
  {"_type":"illness_script","topic":"Antiphospholipid syndrome","discipline":"medicine",
   "enabling_conditions":"SLE or other autoimmune disease, prior thrombosis, recurrent pregnancy loss",
   "pathophysiology":"Antiphospholipid antibodies (lupus anticoagulant, anticardiolipin, anti-B2GPI) activate endothelium, platelets, and coagulation cascade -> arterial and venous thrombosis; placental thrombosis causes pregnancy loss",
   "time_course":"Episodic thrombotic events; catastrophic APS (CAPS) is rare but involves multiorgan thrombosis over days",
   "key_features":"DVT/PE, arterial strokes, recurrent pregnancy loss, thrombocytopenia, livedo reticularis",
   "consequence_if_missed":"Recurrent life-threatening thromboembolism; pregnancy loss; CAPS with multi-organ failure"}
]

# ── 17: Antiseizure Medication Pharmacology — chunks off-topic (anaesthesia) ──
# Only usable: benzodiazepine pharmacology chunks + flumazenil
kps += [
  {"id":"asm-pharm-1","topic":"Antiseizure Medication Pharmacology & Selection","domain":"Internal medicine: neurology (ischemic & hemorrhagic stroke, seizures & status epilepticus, altered mental status & delirium, headache, neuromuscular weakness, spinal cord syndromes)","discipline":"medicine",
   "stem":"Benzodiazepines reduce volatile anaesthetic minimum alveolar concentration by approximately how much?",
   "answer":"Approximately 30%.",
   "rationale":"Benzodiazepines enhance GABA-A receptor function, producing CNS depression that synergises with volatile agents; this interaction is clinically important when managing seizures in the perioperative period.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":284}],"confusable_with":""},
  {"id":"asm-pharm-2","topic":"Antiseizure Medication Pharmacology & Selection","domain":"Internal medicine: neurology (ischemic & hemorrhagic stroke, seizures & status epilepticus, altered mental status & delirium, headache, neuromuscular weakness, spinal cord syndromes)","discipline":"medicine",
   "stem":"Flumazenil is a specific antagonist at which receptor and what is its clinical use?",
   "answer":"Specific competitive antagonist at benzodiazepine (GABA-A) receptors; used to reverse benzodiazepine sedation and treat overdose.",
   "rationale":"Flumazenil (imidazobenzodiazepine) competitively displaces benzodiazepines from GABA-A receptors without agonist activity, rapidly reversing sedation.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":466}],"confusable_with":"Naloxone (opioid antagonist, not for BZD reversal)"},
  {"id":"asm-pharm-3","topic":"Antiseizure Medication Pharmacology & Selection","domain":"Internal medicine: neurology (ischemic & hemorrhagic stroke, seizures & status epilepticus, altered mental status & delirium, headache, neuromuscular weakness, spinal cord syndromes)","discipline":"medicine",
   "stem":"Antiparkinsonian drugs and tricyclic antidepressants augment sedation from scopolamine via which mechanism?",
   "answer":"Anticholinergic side effects of these drugs synergise with scopolamine's CNS anticholinergic action.",
   "rationale":"Multiple anticholinergic agents have additive CNS depression through muscarinic blockade in the brain, increasing risk of confusion and over-sedation.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":352}],"confusable_with":""}
]

# ── 18: Aspiration Pneumonia & Pneumonitis ────────────────────────────────────
kps += [
  {"id":"asp-pna-1","topic":"Aspiration Pneumonia & Pneumonitis","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"Aspiration does not always cause aspiration pneumonia. What determines the severity of lung injury?",
   "answer":"The volume and composition of the aspirate (acid content, particulate matter).",
   "rationale":"Acid aspiration causes chemical pneumonitis; particulate aspiration causes mechanical obstruction. Volume of aspirate correlates with injury severity.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":438}],"confusable_with":""},
  {"id":"asp-pna-2","topic":"Aspiration Pneumonia & Pneumonitis","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"What are the predominant pathogens in aspiration pneumonia (not pneumonitis)?",
   "answer":"Aerobic gram-negative bacilli are the predominant pathogens; aerobic gram-positive organisms are second most common; anaerobes are less common than historically thought.",
   "rationale":"Modern aspiration pneumonia microbiology reflects oropharyngeal colonisation with gram-negatives, particularly in hospitalised or elderly patients.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Aspiration Pneumonia and Pneumonitis","page":5}],"confusable_with":"Classic teaching: anaerobe-dominant (less accurate for hospitalised patients)"},
  {"id":"asp-pna-3","topic":"Aspiration Pneumonia & Pneumonitis","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"In patients aged >=70 hospitalised with pneumonia, what is the reported prevalence of dysphagia, and what proportion have silent aspirations?",
   "answer":"Dysphagia prevalence ~91.7%; silent aspirations occur in over 50% of cases.",
   "rationale":"Aspiration pneumonia is strongly associated with age-related pharyngeal dysfunction; silent microaspirations go unrecognised clinically but contribute to recurrent lung injury.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Aspiration Pneumonia and Pneumonitis","page":3}],"confusable_with":""},
  {"id":"asp-pna-4","topic":"Aspiration Pneumonia & Pneumonitis","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"Acute intrinsic pulmonary disorders include which three conditions?",
   "answer":"Pulmonary oedema (including ARDS), infectious pneumonia, and aspiration pneumonitis.",
   "rationale":"These three conditions share the feature of acute alveolar flooding from different mechanisms; distinguishing them guides specific treatment (diuresis vs antibiotics vs supportive).",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":874}],"confusable_with":""},
  {"id":"asp-pna-5","topic":"Aspiration Pneumonia & Pneumonitis","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"Aspiration pneumonia in the US caused approximately how many deaths per year between 1999-2017 and which age group was most affected?",
   "answer":"Average of 58,576 deaths per year; individuals aged 75 or older accounted for the majority.",
   "rationale":"Aspiration pneumonia is an independent risk factor for mortality in the elderly due to impaired swallowing, immune senescence, and comorbidities.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Aspiration Pneumonia and Pneumonitis","page":12}],"confusable_with":""}
]

# ── 19: Aspirin/NSAID Hypersensitivity ───────────────────────────────────────
kps += [
  {"id":"nsaid-hypersens-1","topic":"Aspirin/NSAID hypersensitivity","domain":"Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)","discipline":"medicine",
   "stem":"What is the mechanism of aspirin/NSAID hypersensitivity reactions?",
   "answer":"COX-1 inhibition shunts arachidonic acid toward leukotriene synthesis (5-LOX pathway), triggering bronchospasm and urticaria/angioedema without IgE involvement.",
   "rationale":"ASA-exacerbated respiratory disease (AERD/Samter triad) is pharmacologic not immunologic; avoiding all NSAIDs that inhibit COX-1 prevents reactions.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":460}],"confusable_with":"True IgE-mediated drug allergy"},
  {"id":"nsaid-hypersens-2","topic":"Aspirin/NSAID hypersensitivity","domain":"Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)","discipline":"medicine",
   "stem":"COX-1 maintains which two important physiologic functions relevant to NSAID side effects?",
   "answer":"Gastric mucosal protection AND stimulation of platelet aggregation.",
   "rationale":"COX-1-derived prostaglandins (PGE2, PGI2) protect gastric mucosa; TXA2 mediates platelet aggregation. COX-1 inhibition causes GI ulceration and impaired platelet function.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":460}],"confusable_with":"COX-2 (pro-inflammatory; selective inhibition spares COX-1 protective functions)"},
  {"id":"nsaid-hypersens-3","topic":"Aspirin/NSAID hypersensitivity","domain":"Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)","discipline":"medicine",
   "stem":"Aspirin decreases the protein binding of which co-administered NSAID, increasing its unbound active fraction?",
   "answer":"Ketorolac.",
   "rationale":"Aspirin competitively displaces ketorolac from albumin binding sites, increasing free drug concentration and potentially enhancing both efficacy and toxicity.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":460}],"confusable_with":""},
  {"id":"nsaid-hypersens-4","topic":"Aspirin/NSAID hypersensitivity","domain":"Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)","discipline":"medicine",
   "stem":"In drug allergy evaluation, what is the negative predictive value of penicillin skin testing?",
   "answer":"NPV of penicillin skin testing is approximately 95%.",
   "rationale":"A negative penicillin skin test makes IgE-mediated penicillin hypersensitivity unlikely (~95% confidence), allowing safe administration in most cases.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":192}],"confusable_with":"Graded challenge (used for low-suspicion reactions, not same as skin testing)"}
]

# ── 20: Bacterial Meningitis: Diagnosis & Emergency Management ────────────────
kps += [
  {"id":"bact-mening-dx-1","topic":"Bacterial Meningitis: Diagnosis & Emergency Management","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"What proportion of bacterial meningitis patients have at least 2 of the 4 classic symptoms?",
   "answer":"95% have at least 2 of: fever, neck stiffness, altered mental status, and headache.",
   "rationale":"The classic triad/tetrad is highly sensitive when >=2 features are present; their absence makes bacterial meningitis much less likely.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":123}],"confusable_with":"Viral meningitis (milder, lower fever, lymphocytic pleocytosis)"},
  {"id":"bact-mening-dx-2","topic":"Bacterial Meningitis: Diagnosis & Emergency Management","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"What proportion of bacterial meningitis patients have concurrent bacteremia?",
   "answer":"53% have concurrent bacteremia; blood cultures should always be obtained.",
   "rationale":"Blood cultures are positive in >50% of cases and can establish diagnosis and guide antibiotic de-escalation even if LP is delayed.",
   "bloom":"recall","source":[{"book":"StatPearls","page":4}],"confusable_with":""},
  {"id":"bact-mening-dx-3","topic":"Bacterial Meningitis: Diagnosis & Emergency Management","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"How much delay in antibiotic administration worsens outcomes in bacterial meningitis?",
   "answer":"Delays of 3-6 hours in antibiotic administration are associated with increased mortality and morbidity.",
   "rationale":"Bacterial meningitis is a time-sensitive emergency; empiric antibiotics must be started immediately if LP will be delayed for imaging or other reasons.",
   "bloom":"recall","source":[{"book":"StatPearls","page":4}],"confusable_with":""},
  {"id":"bact-mening-dx-4","topic":"Bacterial Meningitis: Diagnosis & Emergency Management","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"What CSF findings (cells, protein, glucose) characterise bacterial vs viral meningitis?",
   "answer":"Bacterial: WBC <100 to >10,000 (>80% PMN), protein >80 mg/dL, glucose <40 mg/dL. Viral: 50-1000 lymphocytes, protein mildly elevated, glucose normal.",
   "rationale":"Bacterial infection drives neutrophilic pleocytosis, protein elevation from blood-brain barrier disruption, and low glucose from bacterial consumption.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":263}],"confusable_with":"TB meningitis (lymphocytic, very high protein, very low glucose)"},
  {"id":"bact-mening-dx-5","topic":"Bacterial Meningitis: Diagnosis & Emergency Management","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"Kernig and Brudzinski signs have what sensitivity and specificity in bacterial meningitis?",
   "answer":"Both have approximately 5% sensitivity but 95% specificity.",
   "rationale":"Meningeal signs are very specific (positive = strong evidence) but insensitive (negative does not exclude meningitis); clinical judgement including all features is required.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":123}],"confusable_with":"Nuchal rigidity (30% sensitive, 68% specific — more sensitive but less specific)"},
  {"_type":"illness_script","topic":"Bacterial Meningitis: Diagnosis & Emergency Management","discipline":"medicine",
   "enabling_conditions":"Immunocompromise, asplenia, complement deficiency, close contacts, crowded living, recent URI, unvaccinated",
   "pathophysiology":"Bacteria breach blood-brain barrier -> CSF inflammation -> cerebral oedema, raised ICP, vasculitis -> brain injury",
   "time_course":"Hours: rapid deterioration; can progress from headache to coma in <24 h for Neisseria/pneumococcal",
   "key_features":"Fever + neck stiffness + AMS + headache (95% have >=2); Kernig/Brudzinski (specific); petechiae/purpura (meningococcal)",
   "consequence_if_missed":"Death; permanent neurologic deficits (hearing loss, cognitive impairment, cranial nerve palsies)"}
]

# ── 21: Bacterial Meningitis: Pathogen-Specific Treatment ────────────────────
kps += [
  {"id":"bact-mening-tx-1","topic":"Bacterial Meningitis: Pathogen-Specific Treatment","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"What is the empiric antibiotic approach for bacterial meningitis when lumbar puncture will be delayed?",
   "answer":"Start empiric antibiotics immediately (do not wait for LP); obtain blood cultures first.",
   "rationale":"Timely antibiotic administration is paramount; delays of 3-6 hours worsen outcomes. Blood cultures can still establish diagnosis after antibiotics are started.",
   "bloom":"apply","source":[{"book":"StatPearls","page":4}],"confusable_with":"Waiting for LP results before starting antibiotics"},
  {"id":"bact-mening-tx-2","topic":"Bacterial Meningitis: Pathogen-Specific Treatment","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"What additional CSF findings distinguish bacterial from viral meningitis regarding procalcitonin and CRP in blood?",
   "answer":"Elevated C-reactive protein or procalcitonin in blood suggest bacterial rather than viral aetiology.",
   "rationale":"Procalcitonin rises sharply with bacterial infection and systemic inflammation; a markedly elevated level favours bacterial over aseptic meningitis.",
   "bloom":"apply","source":[{"book":"StatPearls","page":4}],"confusable_with":""},
  {"id":"bact-mening-tx-3","topic":"Bacterial Meningitis: Pathogen-Specific Treatment","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"When should lumbar puncture be delayed in suspected bacterial meningitis?",
   "answer":"If patient has unstable vital signs, coagulation abnormalities, or recent seizure — start empiric antibiotics immediately.",
   "rationale":"LP has risk of herniation in high ICP and haemorrhage in coagulopathy; antibiotics should never be withheld while waiting to perform LP in these high-risk scenarios.",
   "bloom":"apply","source":[{"book":"StatPearls","page":4}],"confusable_with":""},
  {"id":"bact-mening-tx-4","topic":"Bacterial Meningitis: Pathogen-Specific Treatment","domain":"Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)","discipline":"medicine",
   "stem":"What is the recommended dose and duration of empiric acyclovir for suspected HSV encephalitis?",
   "answer":"Acyclovir 10 mg/kg IV every 8 hours for 14-21 days.",
   "rationale":"HSV encephalitis is treatable; empiric acyclovir is started in all encephalitis cases because untreated HSV has high mortality and the drug is safe.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Viral Meningitis & Encephalitis","page":4}],"confusable_with":"Bacterial meningitis treatment (no antiviral needed)"}
]

with open('data/kp_part0_chunk2.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print(f"Chunk2 saved: {len(kps)} entries")
