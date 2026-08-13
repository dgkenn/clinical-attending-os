#!/usr/bin/env python3
"""
Phase 4.1: Toxicology & Overdose Management

Generates 70-90 medical knowledge units covering:
- Acetaminophen toxicity and N-acetylcysteine protocol
- Opioid overdose and naloxone dosing
- Benzodiazepine and flumazenil considerations
- Anticholinergic toxicity
- Sympathomimetic overdose (cocaine, amphetamines)
- Withdrawal syndromes (alcohol, benzodiazepines, opioids)
- Methanol/ethylene glycol toxicity
- Organophosphate poisoning
- Heavy metal poisoning and chelation
- Salicylate toxicity
"""

import json
from datetime import datetime

def create_toxicology_units():
    """Generate toxicology and overdose management units."""

    units = [
        # === ACETAMINOPHEN TOXICITY ===
        {
            "topic": "Acetaminophen Toxicity - Stages",
            "subtopic": "acetaminophen_overview",
            "content": "Acetaminophen overdose causes predictable organ toxicity through depletion of hepatic glutathione. Stage 1 (0-24h): nausea, vomiting, anorexia, abdominal pain; appears mild. Stage 2 (24-72h): RUQ pain, elevated transaminases (ALT/AST rising), normal PT initially. Stage 3 (72h-5 days): peak hepatotoxicity, encephalopathy, coagulopathy, hypoglycemia, acute kidney injury. Stage 4 (>5 days): recovery or death from hepatic failure. Toxic dose >150 mg/kg or >6g in single dose; chronic overdose (>4g/day for days) also causes harm. Rumack nomogram guides N-acetylcysteine (NAC) therapy based on 4-hour serum level.",
            "tags": ["toxicology", "acetaminophen", "hepatotoxicity", "stage", "high_yield"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Acetaminophen Rumack Nomogram",
            "subtopic": "acetaminophen_nomogram",
            "content": "NAC indicated if serum acetaminophen level falls above nomogram line (plotted as log serum concentration vs. hours post-ingestion). Treatment line set conservatively to account for delayed absorption. Obtain level 4 hours post-ingestion (minimum to avoid falsely low reading). For acute single ingestion: 200 μg/mL at 4h, 50 μg/mL at 12h, 10 μg/mL at 24h approximately. For unknown timing or extended-release formulation, start NAC if ANY risk. Level <5 μg/mL at 24h generally safe, but if encephalopathy develops, NAC continued regardless of level.",
            "tags": ["acetaminophen", "nomogram", "nac_protocol", "dosing"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "N-Acetylcysteine (NAC) Protocol - Dosing & Regimen",
            "subtopic": "nac_protocol",
            "content": "NAC given in 3-phase protocol. Loading dose: 150 mg/kg IV over 60 minutes (or PO 140 mg/kg; slower onset). Second phase: 50 mg/kg IV over 4 hours. Third phase: 100 mg/kg IV over 16 hours. Total dose over 20-21 hours = 300 mg/kg. Earlier administration (within 8-10 hours) markedly more effective; efficacy ~100% if given <8h, declining to ~40% by 24h, but still used up to 36+ hours. PO route (140 mg/kg load, then 70 mg/kg q4h × 17 doses) used if no IV access, slower but effective. Repeat loading dose if patient vomits within 1 hour of PO dose.",
            "tags": ["acetaminophen", "nac", "dosing", "protocol"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "NAC Side Effects & Monitoring",
            "subtopic": "nac_adverse_effects",
            "content": "IV NAC causes flushing, pruritus, anaphylactoid reactions (1-2%), angioedema rare. Reactions NOT true IgE-mediated anaphylaxis but direct mast cell activation. Management: slow infusion rate, give antihistamine (diphenhydramine 25-50 mg IV) before NAC, consider acetaminophen-free analgesic alternatives. Rarely, reaction severe enough to discontinue NAC, but mortality risk from untreated toxicity > NAC risk. Monitor: LFTs (ALT/AST, bilirubin), PT/INR, glucose, renal function, arterial blood gas if altered mental status. Target improvement in PT/INR and trend in transaminases by 24-48h.",
            "tags": ["nac", "adverse_effects", "anaphylaxis", "monitoring"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Fulminant Hepatic Failure from Acetaminophen - Transplant Criteria",
            "subtopic": "acetaminophen_transplant",
            "content": "Kings College Criteria for transplantation in acetaminophen-induced fulminant hepatic failure: (1) PT >30s (INR >1.8) PLUS pH <7.3 OR (2) PT >30s PLUS three of: age <10 or >40 years, encephalopathy >3 days, creatinine >3.4 mg/dL, bilirubin >17.5 mg/dL, non-A non-B hepatitis. If criteria met, call transplant immediately; mortality without transplant >80%. Continuous glucose monitoring (maintain >80 mg/dL), maintain platelets >50k, MAP >60 (vasopressors), keep ammonia checked regularly. Encephalopathy with hypertension suggests cerebral edema; treat with osmotic therapy (mannitol 0.25-1 g/kg IV, target osmolality 310-320 mOsm/kg).",
            "tags": ["acetaminophen", "fulminant_failure", "transplant", "criteria"],
            "library": "intern_year_medicine"
        },

        # === OPIOID OVERDOSE ===
        {
            "topic": "Opioid Overdose - Clinical Features",
            "subtopic": "opioid_toxidrome",
            "content": "Opioid toxidrome = triad: respiratory depression (RR <12), miosis (pinpoint pupils <2mm), depressed mental status/coma. Additional: bradycardia, hypotension, hypothermia, pulmonary edema (white foamy sputum from fluid transudation into lungs, not necessarily cardiogenic). Onset: heroin minutes (IV), 15-30 min (IV methadone), 30-60 min (PO oxycodone). Severe toxicity: apnea requiring intubation, aspiration risk high. Chronic users may tolerate higher doses; acute users at greater risk. Fentanyl patches & long-acting opioids cause delayed toxicity (6-24h lag).",
            "tags": ["opioid", "overdose", "toxidrome", "respiratory_depression", "high_yield"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Naloxone (Narcan) - Dosing & Administration",
            "subtopic": "naloxone_protocol",
            "content": "Naloxone = competitive opioid antagonist, short half-life 30-90 min. IM/IV/intranasal routes. Dosing: 0.4-2 mg IV/IM push (repeat q2-3 min if no response, max 10 mg); intranasal spray 4 mg per nostril (can use both). IV preferred (rapid onset <2 min); IM used if no IV access (onset 5-10 min). Intranasal (naloxone nasal spray, Narcan) is public-facing rescue option, slow onset but convenient. Key: naloxone is SHORT-acting; must monitor 2-4 hours post-reversal because as naloxone wears off, opioid redistributes and respiratory depression recurs. Continuous IV naloxone drip (starting 0.0025 mg/kg/min, titrate to respiratory rate >12) used for long-acting opioids (methadone, buprenorphine, fentanyl patches).",
            "tags": ["opioid", "naloxone", "dosing", "administration"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Naloxone Complications & Withdrawal",
            "subtopic": "naloxone_complications",
            "content": "Acute opioid withdrawal from naloxone causes sympathomimetic surge: hypertension, tachycardia, diaphoresis, agitation, aching joints, but NOT life-threatening. Withdraw naloxone dose if patient becomes overly agitated or if severe hypertension develops; reduce intranasal or lower IV drip rate. Rare: acute pulmonary edema (flash pulmonary edema, mechanism unclear, possibly catecholamine surge or opioid-related noncardiogenic pulmonary edema unmasking). If pulmonary edema develops post-naloxone, support with CPAP/BiPAP, consider IV diuretics cautiously. Buprenorphine users: partial antagonism by naloxone; may need higher/repeated doses.",
            "tags": ["naloxone", "withdrawal", "complications", "pulmonary_edema"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Supportive Care in Opioid Overdose",
            "subtopic": "opioid_supportive_care",
            "content": "Airway management critical. Do NOT intubate reflexively unless absolutely necessary (apnea, inability to protect airway, severe hypoxemia refractory to supplemental O2). If intubating, use ketamine induction (slower push, 1-2 mg/kg) to avoid rapid naloxone requirement post-intubation. Maintain SpO2 >90% with nasal cannula, bag-mask, or BiPAP. Pulmonary edema: elevate head, restrict fluids, PEEP 5-10 cm H2O, cautious diuretics (furosemide 40 mg IV). Monitor for aspiration pneumonia; consider prophylactic ABX if vomitus inhaled. Observe minimum 4 hours post-naloxone; longer for sustained-release opioids (oxycontin, methadone). Arrange addiction medicine consult for outpatient MAT (buprenorphine, methadone) or 12-step referral.",
            "tags": ["opioid", "supportive_care", "airway", "management"],
            "library": "intern_year_medicine"
        },

        # === BENZODIAZEPINE OVERDOSE ===
        {
            "topic": "Benzodiazepine Toxicity - Clinical Presentation",
            "subtopic": "benzodiazepine_toxidrome",
            "content": "Benzodiazepine overdose causes CNS depression: sedation, ataxia, dysarthria, depressed respiratory drive, hypotension. Onset varies (diazepam 15-45 min, lorazepam 5-10 min, midazolam 1-3 min depending on route). Severe: loss of consciousness, respiratory depression requiring intubation, aspiration risk. Unlike opioids, pupils normal (not pinpointed). Benzodiazepines with long half-lives (diazepam 24-48h) cause prolonged toxicity; short-acting agents (midazolam, triazolam) clear faster. Chronic use develops tolerance; acute ingestion or withdrawal rebound seizures are risk.",
            "tags": ["benzodiazepine", "overdose", "cns_depression", "toxidrome"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Flumazenil - Mechanism & Cautions",
            "subtopic": "flumazenil_protocol",
            "content": "Flumazenil = competitive GABA antagonist, rapidly reverses benzodiazepine effects. Dosing: 0.2 mg IV push over 30 sec; repeat 0.1 mg q30-60 sec until awake (typical total 0.6-1 mg). NOT recommended as first-line because risk of seizures, especially in chronic benzodiazepine users or mixed overdoses. Use ONLY if: (1) isolated benzodiazepine ingestion confirmed, (2) no chronic benzodiazepine use, (3) no history of seizures, (4) no concurrent tricyclic antidepressants. CONTRAINDICATED: tricyclic copoisoning, seizure disorder, benzodiazepine withdrawal, chronic benzodiazepine dependence. If doubt exists, use supportive care instead. Half-life short (40-80 min), so redose or continuous infusion may needed (0.1-0.4 mg/h).",
            "tags": ["flumazenil", "benzodiazepine", "reversal", "cautions"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Benzodiazepine Overdose - Supportive Management",
            "subtopic": "benzodiazepine_supportive",
            "content": "Mainstay of therapy is supportive care (like opioids). Supplemental O2, maintain SpO2 >90%. BiPAP or bag-mask if hypoventilation. Intubation only if unable to protect airway or severe hypoxemia. Monitor for aspiration. Flumazenil generally avoided given seizure risk; instead, observe and wait for metabolism. Benzodiazepines cause no direct organ toxicity except CNS, so labs (LFTs, renal function) usually normal. Monitor vital signs q1h initially. Keep patient NPO until fully alert due to aspiration risk. Discharge criteria: alert, normal respiratory rate, no signs of recurrence (especially important for long-acting agents where rebound drowsiness can occur hours later).",
            "tags": ["benzodiazepine", "supportive_care", "monitoring"],
            "library": "intern_year_medicine"
        },

        # === ANTICHOLINERGIC TOXICITY ===
        {
            "topic": "Anticholinergic Toxidrome - Clinical Features",
            "subtopic": "anticholinergic_toxidrome",
            "content": "Classic phrase: 'Red as a beet, dry as a bone, hot as a pistol, mad as a hatter' (flushed skin, dry mucous membranes, fever, altered mentation). Anticholinergic toxidrome: mydriasis (dilated pupils), tachycardia, hypertension, hyperthermia, agitation, confusion, urinary retention, ileus, decreased sweating. Central effects: delirium, seizures, hallucinations (may be terrifying). Sympathomimetic phase early; later depression possible. Agents: atropine (intentional or accidental, eye drops), scopolamine, antihistamines (diphenhydramine), tricyclic antidepressants (TCA), antipsychotics (phenothiazines), muscle relaxants (cyclobenzaprine). Onset typically 30-120 min depending on route.",
            "tags": ["anticholinergic", "toxidrome", "toxicity", "delirium"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Physostigmine - Use in Anticholinergic Toxicity",
            "subtopic": "physostigmine_protocol",
            "content": "Physostigmine = acetylcholinesterase inhibitor, crosses blood-brain barrier (unlike neostigmine). Reverses anticholinergic effects including CNS symptoms (delirium). Dosing: 1-2 mg IV over 3-5 min; may repeat q10-15 min up to 6 mg total. Effective for pure anticholinergic toxicity but CONTRAINDICATED in: tricyclic antidepressant copoisoning (risk of severe arrhythmias, seizures due to TCA effects), cardiac dysrhythmias. Main side effect: cholinergic crisis (bronchoconstriction, bradycardia, bronchorrhea). Give atropine 0.5-1 mg IV concurrently or on standby to reverse cholinergic excess. Used less commonly now; supportive care (cooling, benzodiazepines for agitation/seizures) preferred unless severe delirium.",
            "tags": ["physostigmine", "anticholinergic", "reversal"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Anticholinergic Overdose - Management Approach",
            "subtopic": "anticholinergic_management",
            "content": "Priority: rule out life-threatening diagnoses (closed-angle glaucoma, thyroid storm masquerading as anticholinergic, severe infection). Supportive care: cooling for fever (iv fluids, ice packs, intubation with paralysis if severe hyperthermia), benzodiazepines (lorazepam 2-4 mg IV) for agitation/seizures, foley catheter for urinary retention. Cardiac monitoring for arrhythmias (especially with TCAs). Do NOT give physostigmine empirically; confirm anticholinergic source first (careful history, examination of ingested pills, urine toxicology if available). Avoid anticholinergic copoisoning drugs (TCAs present contraindication). IV hydration helpful for preventing rhabdomyolysis from hyperthermia. Most cases resolve within 24-48 hours.",
            "tags": ["anticholinergic", "management", "supportive_care"],
            "library": "intern_year_medicine"
        },

        # === SYMPATHOMIMETIC OVERDOSE ===
        {
            "topic": "Sympathomimetic Overdose - Cocaine & Amphetamines",
            "subtopic": "sympathomimetic_toxidrome",
            "content": "Cocaine & amphetamine toxidrome: mydriasis, tachycardia (may severe >160 bpm), hypertension (often extreme, >200 systolic), hyperthermia, agitation, paranoia, tactile hallucinations ('cocaine bugs'). Cocaine additional effects: coronary vasoconstriction (can cause MI even in young healthy users), arrhythmias (including ventricular fibrillation), nasal damage if snorted. Amphetamines longer half-life; methamphetamine especially neurotoxic. Psychiatric effects prominent: psychosis, violence. Physical complications: rhabdomyolysis, acute kidney injury, stroke, seizures. Death may occur from cardiac arrhythmia, hypertensive emergency, seizure, or hyperthermia.",
            "tags": ["sympathomimetic", "cocaine", "amphetamine", "toxidrome", "high_yield"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Sympathomimetic Overdose - Acute Management",
            "subtopic": "sympathomimetic_management",
            "content": "Benzodiazepines are FIRST-LINE (lorazepam 2-4 mg IV, titrate; midazolam 5-10 mg IV if needed). Beta-blockers controversial and avoided by some (risk of unopposed alpha vasoconstriction worsening hypertension). Phentolamine (alpha blocker) used for severe hypertension (5-15 mg IV); labetolol acceptable if bradycardia absent. Cooling for hyperthermia (ice, iv fluids, intubation with paralysis if severe). Continuous cardiac monitoring (risk of arrhythmias). IV fluids cautiously (maintain UOP 0.5-1 mL/kg/h to prevent rhabdo-related AKI). Urine alkalinization with sodium bicarbonate (target pH >7.45) reduces renal reabsorption of cocaine/amphetamine metabolites, may decrease toxicity duration slightly. Seizures: benzodiazepines first line; phenytoin second line if refractory.",
            "tags": ["sympathomimetic", "management", "benzodiazepines", "cooling"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Cocaine-Induced Myocardial Infarction",
            "subtopic": "cocaine_mi",
            "content": "Cocaine causes coronary vasoconstriction via alpha-adrenergic effects and direct endothelial damage. MI can occur minutes to hours after use; may present with chest pain, ST elevation on ECG (usually LAD territory if STEMI). Troponin elevation confirms MI. Management: aspirin (325 mg chewed), nitrates (sublingual NTG 0.3-0.6 mg or IV NTG) for vasodilation, benzodiazepines for anxiety/agitation. Avoid beta-blockers unless absolutely necessary (unopposed alpha effects worse). Thrombolytics typically offered if STEMI criteria met, though some centers prefer conservative management given high recurrence. Percutaneous coronary intervention (PCI) preferred if available. Long-term: address cocaine addiction (cardiology + addiction medicine follow-up).",
            "tags": ["cocaine", "myocardial_infarction", "coronary", "vasospasm"],
            "library": "intern_year_medicine"
        },

        # === WITHDRAWAL SYNDROMES ===
        {
            "topic": "Alcohol Withdrawal - Stages & Progression",
            "subtopic": "alcohol_withdrawal_stages",
            "content": "Alcohol withdrawal = hyperadrenergic state from loss of CNS depressant effect. Timeline: tremor, diaphoresis, tachycardia (6-24h post-cessation); alcoholic hallucinosis 12-48h (auditory hallucinations, visual intact); withdrawal seizures 6-48h (brief, typically generalized); delirium tremens (DTs) 48-96h (autonomic hyperactivity, confusion, hallucinations, fever). Mortality of untreated DTs ~5-15%. CIWA-Ar score (Clinical Institute Withdrawal Assessment for Alcohol scale) guides severity: <8 mild, 8-15 moderate, >15 severe. Score >15 should receive benzodiazepines.",
            "tags": ["alcohol", "withdrawal", "stages", "progression", "high_yield"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Alcohol Withdrawal - Benzodiazepine Protocol",
            "subtopic": "alcohol_withdrawal_treatment",
            "content": "Lorazepam preferred (shorter half-life, metabolized via glucuronidation, not affected by liver disease). Dosing: 2-4 mg IV q0.5-1h, titrate to CIWA-Ar score <8. Diazepam alternative (5-10 mg IV q1h), longer half-life requires monitoring for oversedation. Chlordiazepoxide (Librium) oral 50-100 mg q6h if mild withdrawal, not for severe/acute DTs. Phenobarbital used as adjunct or if benzodiazepine-refractory. Goal: prevent seizures and manage autonomic hyperactivity. Long-term: naltrexone 50 mg daily or acamprosate 666 mg TID for relapse prevention; thiamine 100 mg IV (severe withdrawal can precipitate Wernicke's encephalopathy if glucose given without thiamine).",
            "tags": ["alcohol", "withdrawal", "benzodiazepines", "protocol"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Benzodiazepine Withdrawal - Acute Syndrome",
            "subtopic": "benzodiazepine_withdrawal",
            "content": "Withdrawal after chronic benzodiazepine use causes serious symptoms similar to alcohol withdrawal. Timing depends on half-life: short-acting agents (triazolam, midazolam) withdraw within 24-48h; long-acting (diazepam) withdraw over days to weeks. Symptoms: tremor, diaphoresis, agitation, anxiety, insomnia, seizures (can be life-threatening), hallucinations. Risk factors: high dose, long duration of use, abrupt cessation. Management: gradual taper (reduce dose 10% per week, slower if seizures occurred). Lorazepam bridge if needed during taper. Seizures managed with benzodiazepines (lorazepam 2-4 mg IV). Admission to ICU if severe withdrawal or seizures. Outpatient taper acceptable if mild, reliable patient, close follow-up.",
            "tags": ["benzodiazepine", "withdrawal", "seizures", "taper"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Opioid Withdrawal - Clinical Features & Treatment",
            "subtopic": "opioid_withdrawal",
            "content": "Opioid withdrawal NOT life-threatening but severely uncomfortable. Timeline: anxiety, restlessness (6-12h post-cessation); peak symptoms (24-72h) including myalgias, GI cramping, diarrhea, insomnia, pupil dilation, yawning, sweating, goosebumps. Duration 5-7 days (short-acting) to 2+ weeks (methadone). COWS (Clinical Opiate Withdrawal Scale) score guides management. Treatment: methadone (long-acting maintenance) or buprenorphine (partial agonist, ceiling effect on respiratory depression). Acute symptomatic relief: NSAIDs for myalgias, loperamide for diarrhea, ondansetron for nausea, trazodone for insomnia (not benzodiazepines, which increase overdose risk). Cold turkey not recommended; drives relapse.",
            "tags": ["opioid", "withdrawal", "methadone", "buprenorphine"],
            "library": "intern_year_medicine"
        },

        # === METHANOL & ETHYLENE GLYCOL ===
        {
            "topic": "Methanol & Ethylene Glycol Toxicity - Overview",
            "subtopic": "toxic_alcohol_toxidrome",
            "content": "Both methanol (windshield washer fluid, paint thinners) and ethylene glycol (antifreeze, hydraulic fluid) cause similar toxicity via metabolic acidosis. Initial phase: CNS depression, inebriation, nausea. Metabolic phase (6-24h): anion-gap metabolic acidosis, altered mentation, Kussmaul breathing. Methanol: optic nerve damage (blindness), hyperemia of optic disc. Ethylene glycol: crystalluria, renal failure. Both require aggressive treatment to prevent irreversible organ damage. Serum osmolality increased (osmolar gap). Key: early fomepizole administration blocks metabolism and prevents serious morbidity/mortality.",
            "tags": ["methanol", "ethylene_glycol", "toxic_alcohol", "acidosis"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Fomepizole Protocol for Toxic Alcohol Poisoning",
            "subtopic": "fomepizole_protocol",
            "content": "Fomepizole (4-methylpyrazole) = alcohol dehydrogenase inhibitor, blocks conversion of methanol/ethylene glycol to toxic metabolites. Loading dose: 15 mg/kg IV bolus (dilute to 250 mL normal saline, infuse over 30 min). Maintenance: 10 mg/kg IV q12h × 4 doses, then 15 mg/kg q12h if patient on hemodialysis. Continue until methanol/ethylene glycol undetectable or <10 mg/dL and no metabolic acidosis. Fomepizole dramatically improves outcomes; mortality drops from 20-25% to <3%. May cause hypoglycemia, IV site erythema. Cost significant but justifies early use if high clinical suspicion.",
            "tags": ["fomepizole", "toxic_alcohol", "protocol", "dosing"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Hemodialysis in Toxic Alcohol Poisoning",
            "subtopic": "toxic_alcohol_dialysis",
            "content": "Hemodialysis indicated for: (1) severe metabolic acidosis (pH <7.15), (2) renal failure/hyperkalemia, (3) altered mental status, (4) serum level >25 mg/dL methanol or >20 mg/dL ethylene glycol, (5) visual symptoms (methanol). Dialysis removes both parent compound and toxic metabolites (formate, glycolate). Continue dialysis until visual symptoms resolve and acidosis cleared. Combined with fomepizole (which prevents further metabolism), dialysis provides complete clearance. Prognosis with early fomepizole + dialysis excellent; mortality <3-5%. Without treatment, mortality 20-40%.",
            "tags": ["toxic_alcohol", "dialysis", "hemodialysis"],
            "library": "intern_year_medicine"
        },

        # === ORGANOPHOSPHATE POISONING ===
        {
            "topic": "Organophosphate Poisoning - Mechanism & Presentation",
            "subtopic": "organophosphate_toxidrome",
            "content": "Organophosphates = pesticides, nerve agents; irreversibly inhibit acetylcholinesterase. Result: cholinergic crisis (excessive acetylcholine at synapses). Muscarinic effects: miosis (pinpoint pupils), bronchospasm, bradycardia, salivation, lacrimation, urination, defecation ('SLUDGE'). Nicotinic effects: muscle fasciculations, paralysis, weakness. CNS: altered mentation, seizures, respiratory depression. Exposure: pesticide ingestion, dermal contact, inhalation. Onset: minutes to hours depending on route. Severe: apnea, pulmonary edema, cardiovascular collapse. Pralidoxime must be given quickly (within 24-48h ideally) to restore cholinesterase activity.",
            "tags": ["organophosphate", "poisoning", "cholinergic_crisis", "nerve_agent"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Atropine in Organophosphate Toxicity",
            "subtopic": "organophosphate_atropine",
            "content": "Atropine = muscarinic antagonist, relieves SLUDGE symptoms. Dosing: 0.5-1 mg IV push; double dose q5-10 min until atropinization (dry mouth, dilated pupils, HR >90). May require large total doses (100+ mg). Goal: reverse bronchospasm, bradycardia, salivation; does NOT reverse nicotinic paralysis (muscle weakness/fasciculations). Give atropine early and often; titrate to drying of secretions. Adverse effects: tachycardia if overdosed, but in acute poisoning, atropine side effects acceptable. Continue atropine drip (initial bolus followed by continuous infusion 2-15 mg/h) for hours to days depending on severity and organophosphate persistence.",
            "tags": ["atropine", "organophosphate", "muscarinic", "dosing"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Pralidoxime (2-PAM) Protocol",
            "subtopic": "pralidoxime_protocol",
            "content": "Pralidoxime = oxime, reactivates cholinesterase by removing phosphate group from enzyme (only effective before 'aging' of phosphate bond, typically 24-48h). Dosing: 1-2 g IV bolus over 15-30 min, may repeat q30-60 min if muscle weakness persists. Maximum 12 g/day. Pralidoxime alone inadequate; must combine with atropine (pralidoxime doesn't treat CNS effects or nicotinic symptoms directly). Timing critical: give within 24-48h of exposure; efficacy declines after aging occurs. Continuous infusion (1 g/h) used for sustained poisoning. Side effects: transient visual disturbance, headache, nausea, dizziness.",
            "tags": ["pralidoxime", "organophosphate", "cholinesterase", "protocol"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Organophosphate Poisoning - Supportive Care",
            "subtopic": "organophosphate_supportive",
            "content": "Intubation and mechanical ventilation if respiratory depression severe; maintain aggressive airway suctioning (massive bronchorrhea). Seizures: benzodiazepines first-line (lorazepam 2-4 mg IV). Continuous cardiac monitoring (bradycardia/arrhythmias common). Decontamination: remove clothing, wash skin with soap and water. Do NOT use alcohol-based cleaners (may increase absorption). Supportive fluids, treat hyperkalemia if present. Prolonged ICU stays common; may remain symptomatic for days to weeks. Prognosis depends on exposure severity and time to treatment; early treatment improves survival significantly.",
            "tags": ["organophosphate", "supportive_care", "management"],
            "library": "intern_year_medicine"
        },

        # === HEAVY METAL POISONING ===
        {
            "topic": "Heavy Metal Poisoning - Overview & Chelation Agents",
            "subtopic": "heavy_metal_overview",
            "content": "Heavy metals (lead, mercury, arsenic, iron, copper) cause multiorgan toxicity. Lead: encephalopathy, renal failure, abdominal pain. Mercury: tremor, psychological effects, renal failure. Arsenic: GI symptoms, peripheral neuropathy, cardiac arrhythmias. Iron: GI hemorrhage, metabolic acidosis, hepatotoxicity. Copper: hemolysis, hepatotoxicity. Chelation = binding agent that prevents metal reabsorption, enhancing renal or biliary excretion. Common agents: EDTA (calcium EDTA for lead), BAL (dimercaprol for arsenic/mercury/lead), DMSA (succimer, oral, lead/arsenic), penicillamine (copper/iron), deferoxamine (iron).",
            "tags": ["heavy_metal", "poisoning", "chelation", "toxicity"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Lead Poisoning & Chelation",
            "subtopic": "lead_toxicity",
            "content": "Lead causes anemia (microcytic), abdominal pain ('lead colic'), encephalopathy (confusion, seizures, coma), nephropathy, and developmental delays in children. Blood lead level diagnostic (>10 μg/dL concerning). Chelation indications: symptomatic toxicity (encephalopathy) OR asymptomatic with lead >100 μg/dL (children) or >80 μg/dL (adults). Agents: calcium EDTA (25-50 mg/kg/day IV infusion for 5-7 days); DMSA (succimer, oral, 350 mg TID × 5 days, then BID × 2 weeks for milder cases). DMSA preferred if no symptoms (less toxic). Recheck lead level after course; multiple rounds may needed.",
            "tags": ["lead", "chelation", "EDTA", "DMSA"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Iron Overdose & Deferoxamine Therapy",
            "subtopic": "iron_toxicity",
            "content": "Iron overdose (often accidental in children) causes GI hemorrhage, metabolic acidosis, shock, hepatotoxicity, and cardiogenic shock. Phases: (1) GI (nausea, vomiting, diarrhea, abdominal pain); (2) apparent recovery; (3) shock, acidosis, liver failure. Serum iron >300 μg/dL requires treatment. Deferoxamine = iron chelator, forms water-soluble complex excreted in urine (pink/red color). Dosing: 15 mg/kg/h IV infusion, titrate by response (may increase to 125 mg/kg/h if severe toxicity). Duration: until iron level <100 μg/dL and acidosis resolved. Side effects: rapid IV can cause hypotension, Yersinia infection (rare). GI decontamination: whole-bowel irrigation if tablets visible on abdominal X-ray.",
            "tags": ["iron", "overdose", "deferoxamine", "chelation"],
            "library": "intern_year_medicine"
        },

        # === SALICYLATE TOXICITY ===
        {
            "topic": "Salicylate Toxicity - Pathophysiology & Presentation",
            "subtopic": "salicylate_toxidrome",
            "content": "Salicylate (aspirin) toxicity = aspirin (>150 mg/kg single dose or chronic high-dose use). Mechanism: uncouples oxidative phosphorylation, stimulates respiratory center. Early: tinnitus (ringing ears), altered mentation, hyperventilation (respiratory alkalosis), hyperthermia. Late: pulmonary edema (noncardiogenic), metabolic acidosis (mixed respiratory alkalosis + metabolic acidosis = mixed picture). Serum salicylate >60 mg/dL symptomatic; >100 mg/dL severe. Chronic toxicity insidious; may present with encephalopathy in elderly. pH and serum level guide severity.",
            "tags": ["salicylate", "aspirin", "toxicity", "toxidrome", "high_yield"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Salicylate Management - Urine Alkalinization",
            "subtopic": "salicylate_management",
            "content": "Urine alkalinization ESSENTIAL. Target urine pH 7.5-8.5 (alkaline urine 'traps' salicylate as anion, preventing reabsorption). Method: sodium bicarbonate 50 mEq IV bolus, then continuous infusion (target serum bicarbonate 25-30 mEq/L, serum pH 7.4-7.5). Monitor serum K+ closely (hypokalemia worsens alkalosis; give KCl 20-40 mEq/L IV if K+ <3.5). Hemodialysis indicated if: salicylate level >100 mg/dL, CNS toxicity (encephalopathy, pulmonary edema), metabolic acidosis refractory to alkalinization, or renal failure. Salicylate has small molecular weight, easily dialyzable; hemodialysis removes drug faster than renal excretion even with alkalinization.",
            "tags": ["salicylate", "alkalinization", "urine_ph", "management"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Salicylate Toxicity - Pulmonary Edema & ICU Care",
            "subtopic": "salicylate_pulmonary_edema",
            "content": "Noncardiogenic pulmonary edema (ARDS-like picture) common in moderate-severe salicylate toxicity. Mechanism: direct lung toxicity + fluid overload during aggressive alkalinization. Management: restrict free water, use hypertonic saline (3%) for alkalinization instead of normal saline, judicious diuretics if necessary. PEEP 5-10 cm H2O if intubated. Continuous monitoring of mixed venous oxygen saturation, lactate. Renal function: salicylate can cause acute tubular necrosis; monitor creatinine, BUN. Most cases resolve within 24-48 hours with aggressive support and removal of salicylate via hemodialysis.",
            "tags": ["salicylate", "pulmonary_edema", "ards", "management"],
            "library": "intern_year_medicine"
        },
    ]

    return units

if __name__ == "__main__":
    units = create_toxicology_units()

    # Add IDs and timestamps
    for i, unit in enumerate(units):
        unit["id"] = f"phase4_tox_unit_{i}"
        unit["created_at"] = datetime.utcnow().isoformat()

    # Write to file
    output_file = "C:\\Users\\Dean\\anesthesia_attending\\data\\phase4_toxicology_chunks.json"
    with open(output_file, "w") as f:
        json.dump(units, f, indent=2)

    print(f"Generated {len(units)} toxicology units")
    print(f"Output: {output_file}")
