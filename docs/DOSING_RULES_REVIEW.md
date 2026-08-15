# Dosing Rules — Clinician Review Sheet

All 59 rules the drill engine grades against, generated 2026-08-15.
**Machine validation** (tests/test_dosing_rule_validation.py) checks arithmetic
and unit-label consistency at boundary inputs — it cannot check clinical
correctness. **That is this sheet's job: a physician checks each box.**
A rule found wrong: fix `data/dosing_rules.json`, re-run
`python -c "from src.dosing_engine import seed_dosing_rules; seed_dosing_rules('data/dosing_rules.json')"`,
and the tests.

## [ ] Acetaminophen  (`acetaminophen_adult`, tier 1, RECALL-ONLY)
- **Context:** Adult pain / fever — standard ward dose
- **Dose fact:** Acetaminophen: 650–1000 mg PO/IV q4–6h, max 4 g/day (3 g/day in liver disease)
- **Anchor taught:** 'Tylenol = 1 gram q6h, cap at 4 g/day.' Liver disease? Cut to 3 g/day. IV = same dose as PO — don't double-dose by accident when switching routes.
- **Source:** UpToDate acetaminophen dosing; FDA labeling

## [ ] Albuterol nebulizer  (`albuterol_nebulizer`, tier 1, RECALL-ONLY)
- **Context:** Acute bronchospasm / asthma / COPD exacerbation
- **Dose fact:** Albuterol neb: 2.5 mg q20 min × 3 doses for acute bronchospasm, then q1–4h. Continuous: 10–15 mg/hr for status asthmaticus.
- **Anchor taught:** '2.5 mg, q20 min × 3, then PRN.' One vial = 2.5 mg. Severe asthma: go continuous (10 mg/hr). Side effect to warn about: tachycardia and hypokalemia (same mechanism as insulin — shifts K+ into cells).
- **Source:** GINA asthma guidelines; GOLD COPD guidelines; UpToDate albuterol

## [ ] Azithromycin  (`azithromycin_cap`, tier 1, RECALL-ONLY)
- **Context:** Community-acquired pneumonia (atypical coverage)
- **Dose fact:** Azithromycin: 500 mg IV/PO daily for inpatient CAP; 500 then 250 mg daily × 4d for outpatient
- **Anchor taught:** 'Z-pak: 500 first day, 250 × 4 more.' Inpatient: 500 mg daily + ceftriaxone (the combo covers both typical and atypical bugs). QTc risk — check the ECG.
- **Source:** IDSA CAP guidelines 2019; UpToDate azithromycin

## [ ] Cefepime  (`cefepime_standard`, tier 1, RECALL-ONLY)
- **Context:** Hospital-acquired / Pseudomonas-coverage infections
- **Dose fact:** Cefepime: 2 g IV q8h for serious infection/Pseudomonas; reduce dose in CKD. Encephalopathy side effect.
- **Anchor taught:** 'Cefepime 2 g q8h = the Pseudomonas hammer.' Can cause neurotoxicity/encephalopathy — think of it when a patient gets confused after starting it, especially in CKD. Dose-reduce in renal failure.
- **Source:** IDSA HAP/VAP guidelines; UpToDate cefepime

## [ ] Ceftriaxone  (`ceftriaxone_standard`, tier 1, RECALL-ONLY)
- **Context:** Common inpatient infections (CAP, UTI, pyelonephritis)
- **Dose fact:** Ceftriaxone: 1 g IV/IM daily (standard), 2 g IV daily for meningitis/severe infection
- **Anchor taught:** 'Rocephin = 1 g daily, 2 g for the brain.' Meningitis or severe sepsis = 2 g. No renal adjustment needed (mostly biliary excretion). Doesn't cover Pseudomonas or MRSA.
- **Source:** IDSA CAP guidelines 2019; UpToDate ceftriaxone

## [ ] Dexamethasone  (`dexamethasone_standard`, tier 1, RECALL-ONLY)
- **Context:** Steroid for cerebral edema, group, COVID, or adrenal use
- **Dose fact:** Dexamethasone: COVID 6 mg × 10d; cerebral edema 10 mg load then 4 mg q6h; croup 0.6 mg/kg
- **Anchor taught:** 'Dexa has three faces: COVID (6 mg × 10d), brain edema (10/4 load/maintenance), croup (0.6 mg/kg once).' No mineralocorticoid — doesn't worsen fluid retention like hydrocortisone. 1 mg dexa = 7.5 mg prednisone.
- **Source:** WHO RECOVERY trial; UpToDate dexamethasone; ACCP/SRS cerebral edema

## [ ] Enoxaparin (DVT prophylaxis)  (`enoxaparin_dvt_prophylaxis`, tier 1, RECALL-ONLY)
- **Context:** VTE prophylaxis — medical/surgical inpatient
- **Dose fact:** Enoxaparin prophylaxis: 40 mg SQ once daily (standard); 30 mg SQ daily if CrCl <30
- **Anchor taught:** 'Lovenox prophylaxis = 40 mg SQ daily.' Simple flat dose — not weight-based for prophylaxis. CrCl <30? Drop to 30 mg. Ortho surgery often uses 30 mg q12h instead.
- **Source:** ACCP/ASH VTE prophylaxis guidelines; UpToDate enoxaparin

## [ ] Enoxaparin (DVT/PE treatment)  (`enoxaparin_treatment`, tier 1, weight_based)
- **Context:** VTE treatment — full anticoagulation
- **Dose fact:** Enoxaparin treatment dose: 1 mg/kg SQ q12h (DVT/PE)
- **Grades with:** `{"mg_per_kg": 1.0}` over `{"weight_kg": [50, 120]}` → answer in **mg**
- **Anchor taught:** 'Treatment = 1 mg/kg q12h.' Easy '1 mg per kg twice daily.' CrCl <30 = avoid (use UFH instead). Obesity: use actual weight but check anti-Xa levels.
- **Source:** ACCP/ASH VTE treatment guidelines 2021; UpToDate enoxaparin

## [ ] Famotidine  (`famotidine_standard`, tier 1, RECALL-ONLY)
- **Context:** GI prophylaxis / peptic ulcer disease
- **Dose fact:** Famotidine: 20 mg IV q12h inpatient; 20–40 mg PO BID for GERD. Renal dose reduction in CKD.
- **Anchor taught:** 'Pepcid 20 mg IV q12h.' Renally dosed — check the CrCl. CKD patients accumulate it → CNS effects (confusion). Less powerful than pantoprazole but faster onset. H2 blocker vs PPI: H2 for prophylaxis, PPI for healing.
- **Source:** UpToDate famotidine; GI prophylaxis guidelines

## [ ] Furosemide  (`furosemide_iv`, tier 1, RECALL-ONLY)
- **Context:** Acute volume overload / CHF exacerbation — IV dosing
- **Dose fact:** Furosemide IV: 20–40 mg if naive; if on PO, IV dose = PO dose (or up to 2.5× PO for aggressive decongestion)
- **Anchor taught:** Furosemide PO→IV: '1:1 conversion' (40 mg PO = 40 mg IV to start, then can push to 2×–2.5×). PO only 50% absorbed → IV is stronger. DOSE trial: don't be shy — push the dose to get diuresis.
- **Source:** DOSE trial (NEJM 2011); UpToDate furosemide; ACC/AHA CHF guidelines

## [ ] Haloperidol  (`haloperidol_acute_agitation`, tier 1, RECALL-ONLY)
- **Context:** Acute agitation / ICU delirium
- **Dose fact:** Haloperidol: 0.5–5 mg IV/IM/PO q4–6h for agitation; 1–2 mg IV for ICU delirium. Monitor QTc.
- **Anchor taught:** 'Haldol 1–2 mg IV for ICU delirium — watch the QTc.' Start low (0.5 mg in elderly). QTc >500 ms = hold it. EPS treated with diphenhydramine. Lewy body = absolute contraindication (can cause irreversible rigidity).
- **Source:** UpToDate acute agitation; PADIS ICU delirium guidelines 2018

## [ ] Heparin SQ (UFH prophylaxis)  (`heparin_sq_prophylaxis`, tier 1, RECALL-ONLY)
- **Context:** VTE prophylaxis — unfractionated heparin SQ
- **Dose fact:** Heparin SQ prophylaxis: 5,000 units SQ q8–12h (preferred in CKD/renal failure)
- **Anchor taught:** 'Heparin SQ = 5,000 units, q8–12h.' Choose over LMWH when kidneys fail — heparin doesn't accumulate renally. HIT risk: check platelet count after day 4.
- **Source:** ACCP guidelines; UpToDate UFH prophylaxis

## [ ] Hydromorphone  (`hydromorphone_acute_pain`, tier 1, RECALL-ONLY)
- **Context:** Adult acute pain — IV PRN dosing (opioid-naive)
- **Dose fact:** Hydromorphone: 0.2–0.4 mg IV q3–4h (opioid-naive); ~5–7× potency of morphine
- **Anchor taught:** 'Dilaudid = 0.2–0.4 mg IV.' It's 5–7× stronger than morphine — so the dose looks tiny. CKD patients get Dilaudid (not morphine) because no M6G accumulation.
- **Source:** UpToDate opioid dosing; Palliative care dosing references

## [ ] Ibuprofen  (`ibuprofen_adult`, tier 1, RECALL-ONLY)
- **Context:** Adult NSAID dosing — ward use
- **Dose fact:** Ibuprofen: 400–600 mg PO q6–8h, max 2400 mg/day. Avoid in CKD/GI bleed.
- **Anchor taught:** '400–600 q6–8, avoid the 4 CKs': CKD, Clotting disorders, Cardiac failure, keep away from Kids (under 6mo). The triple threat of NSAIDs: kidney, gut, heart.
- **Source:** UpToDate NSAID dosing; ACP/ACR guidelines

## [ ] Insulin (basal-bolus concept)  (`insulin_basal_prandial`, tier 1, RECALL-ONLY)
- **Context:** Inpatient basal-bolus insulin initiation
- **Dose fact:** Basal-bolus insulin: TDD = 0.3–0.5 units/kg/day; 50% basal, 50% prandial. NPO: hold prandial, reduce basal 20–50%.
- **Anchor taught:** '0.4 units/kg/day, half-half.' For a 80 kg patient: 32 units/day → 16 units basal (glargine once daily) + 5–6 units per meal. NPO: give basal but hold meal doses.
- **Source:** ADA inpatient diabetes standards 2024; SHM glycemic management

## [ ] Potassium chloride (KCl) repletion  (`kcl_repletion`, tier 1, RECALL-ONLY)
- **Context:** Hypokalemia — IV or PO repletion
- **Dose fact:** KCl repletion: 40 mEq raises K+ ~1 mEq/L. Max IV rate: 10 mEq/hr peripheral, 20–40 mEq/hr central. Always replete Mg2+ with K+.
- **Anchor taught:** '40 mEq = 1 mEq/L rise.' IV: 10 mEq/hr peripheral, faster needs central + telemetry. Always check and replete magnesium — hypokalemia that won't budge is almost always due to concurrent hypomagnesemia.
- **Source:** UpToDate hypokalemia treatment; SHM hospitalist handbook

## [ ] Ketorolac  (`ketorolac_adult`, tier 1, RECALL-ONLY)
- **Context:** Parenteral NSAID for short-term acute pain
- **Dose fact:** Ketorolac: 15–30 mg IV/IM q6h (15 mg if elderly/<50 kg), max 5 days
- **Anchor taught:** 'Toradol = 30 mg, stop at 5 days.' Elderly or small: halve it to 15 mg. The 5-day limit is hard — renal and GI toxicity stack up fast after that.
- **Source:** UpToDate ketorolac dosing; FDA labeling

## [ ] Levofloxacin  (`levofloxacin_cap`, tier 1, RECALL-ONLY)
- **Context:** CAP monotherapy / UTI / skin infections
- **Dose fact:** Levofloxacin: 750 mg PO/IV daily for CAP/pyelonephritis; renal dosing required; tendinopathy + QTc risks
- **Anchor taught:** 'Levo = 750 mg daily.' Two gotchas: Achilles tendon rupture (especially elderly on steroids) and QTc prolongation. Reserve fluoroquinolones — use them when beta-lactams won't do.
- **Source:** IDSA CAP guidelines; UpToDate levofloxacin

## [ ] Lorazepam  (`lorazepam_acute_agitation`, tier 1, RECALL-ONLY)
- **Context:** Acute agitation, alcohol withdrawal, or acute anxiety
- **Dose fact:** Lorazepam: 0.5–2 mg IV/IM/PO q4–6h; alcohol withdrawal use CIWA-Ar protocol, 1–2 mg per dose
- **Anchor taught:** 'Ativan 1–2 mg, titrate to calm.' Alcohol withdrawal: use a CIWA-Ar score to guide dosing (not fixed schedule). Advantage over diazepam in liver disease: no active metabolite accumulation.
- **Source:** UpToDate alcohol withdrawal; CIWA-Ar protocol; ACEP agitation guidelines

## [ ] Magnesium repletion  (`magnesium_repletion`, tier 1, RECALL-ONLY)
- **Context:** Hypomagnesemia — IV repletion
- **Dose fact:** Magnesium repletion: 2 g IV over 1h (standard); 4 g IV for severe/torsades. Must replete before hypokalemia resolves.
- **Anchor taught:** '2 g mag over 1 hour' for standard repletion. The K+ connection: Na/K-ATPase needs magnesium as cofactor — low Mg = K+ keeps leaking out = refractory hypokalemia. Fix Mg first, then K+ sticks.
- **Source:** UpToDate hypomagnesemia; SHM electrolyte repletion protocols

## [ ] Methylprednisolone  (`methylprednisolone_iv`, tier 1, RECALL-ONLY)
- **Context:** IV steroid for acute flare (COPD, asthma, autoimmune)
- **Dose fact:** Methylprednisolone: 125 mg IV q6–8h for severe asthma/COPD; 1 g IV × 3d for MS relapse
- **Anchor taught:** 'Solu-Medrol 125 mg IV = the standard crash dose.' Equivalence: 4 mg methylpred = 5 mg prednisone. MS relapse gets 1 gram IV × 3 days — a completely different scale.
- **Source:** UpToDate steroid dosing; GINA/GOLD guidelines

## [ ] Metoclopramide  (`metoclopramide_antiemetic`, tier 1, RECALL-ONLY)
- **Context:** Nausea, gastric motility — IV or PO
- **Dose fact:** Metoclopramide: 10 mg IV/PO q6–8h; D2 antagonist — risk of extrapyramidal reactions (especially young patients)
- **Anchor taught:** 'Reglan 10 mg, watch for restlessness.' Akathisia (can't sit still) is the classic extrapyramidal sign. Young patients hit hardest. Treat EPS with diphenhydramine 25–50 mg IV.
- **Source:** UpToDate metoclopramide; FDA labeling

## [ ] Metronidazole  (`metronidazole_standard`, tier 1, RECALL-ONLY)
- **Context:** Anaerobic/C. diff infections
- **Dose fact:** Metronidazole: 500 mg PO/IV q8h for anaerobes; C. diff mild (oral only): 500 mg q8h × 10–14d
- **Anchor taught:** 'Flagyl = 500 mg q8h.' C. diff note: IDSA 2021 now prefers vancomycin PO even for non-severe — metronidazole is second-line. No alcohol (disulfiram-like reaction: flushing, vomiting).
- **Source:** IDSA C. diff guidelines 2021; UpToDate metronidazole

## [ ] Morphine  (`morphine_acute_pain`, tier 1, RECALL-ONLY)
- **Context:** Adult acute pain — IV PRN dosing
- **Dose fact:** Morphine acute pain: 2–4 mg IV q3–4h PRN (opioid-naive adult); halve in elderly/CKD
- **Anchor taught:** 'Morphine = 2–4 mg IV.' Low and slow for opioid-naive. CKD trap: active metabolite M6G accumulates → prolonged respiratory depression. Prefer hydromorphone in renal failure.
- **Source:** UpToDate opioid dosing for acute pain; ACOG/APS guidelines

## [ ] Ondansetron  (`ondansetron_antiemetic`, tier 1, RECALL-ONLY)
- **Context:** Nausea/vomiting — IV or PO antiemetic
- **Dose fact:** Ondansetron: 4 mg IV/PO q6–8h PRN nausea (8 mg for chemo); watch QTc
- **Anchor taught:** 'Zofran = 4 mg.' The '4' is easy to remember. QTc gotcha — if the strip shows prolongation or patient is on other QT drugs, pick a different antiemetic.
- **Source:** UpToDate antiemetic dosing; PONV guidelines

## [ ] Oxycodone  (`oxycodone_oral_pain`, tier 1, RECALL-ONLY)
- **Context:** Adult oral opioid for moderate-severe pain
- **Dose fact:** Oxycodone: 5–10 mg PO q4–6h (opioid-naive); ~1.5× oral morphine potency
- **Anchor taught:** 'Oxy starts at 5 mg PO.' It's not a prodrug (unlike codeine) so it works in CYP2D6 poor metabolizers. Percocet combo: count the APAP toward the daily maximum.
- **Source:** UpToDate opioid dosing; WHO analgesic ladder

## [ ] Pantoprazole  (`pantoprazole_standard`, tier 1, RECALL-ONLY)
- **Context:** Acid suppression / GI prophylaxis — PPI
- **Dose fact:** Pantoprazole: 40 mg PO/IV daily standard; 40 mg IV q12h for active GI bleed; infusion 8 mg/hr post-endoscopy for high-risk ulcer
- **Anchor taught:** 'Protonix 40 mg daily = prophylaxis. 40 mg q12h = active bleed. 8 mg/hr infusion = post-endoscopy high-risk ulcer.' The three tiers of acid suppression: daily, BID, continuous infusion.
- **Source:** UpToDate pantoprazole; GI bleeding guidelines; ACG PPI guidelines

## [ ] Piperacillin-tazobactam  (`pip_tazo_standard`, tier 1, RECALL-ONLY)
- **Context:** Broad-spectrum gram-negative / anaerobic coverage
- **Dose fact:** Piperacillin-tazobactam (Zosyn): 3.375 g IV q6h or 4.5 g IV q6h; extended infusion for Pseudomonas/severe sepsis
- **Anchor taught:** 'Zosyn = 3.375 g q6h (or 4.5 g q6h for the heavy-hitters).' Extended infusion over 4h is the pharmacokinetic trick for Pseudomonas — more time above MIC. No MRSA coverage.
- **Source:** IDSA guidelines; UpToDate piperacillin-tazobactam

## [ ] Prednisone  (`prednisone_standard`, tier 1, RECALL-ONLY)
- **Context:** Oral steroid — standard short course
- **Dose fact:** Prednisone: 40 mg PO × 5d for COPD/asthma exacerbation; 1–2 mg/kg/day for severe autoimmune flare
- **Anchor taught:** 'COPD burst = 40 mg × 5 days.' No taper for short courses. Equivalence to remember: pred 5 mg = methylpred 4 mg = dexa 0.75 mg. Steroids = glucose check every 4–6h.
- **Source:** UpToDate corticosteroid dosing; GOLD COPD guidelines

## [ ] Regular insulin (hyperkalemia)  (`regular_insulin_hyperkalemia`, tier 1, RECALL-ONLY)
- **Context:** Hyperkalemia — insulin to shift K+ intracellularly
- **Dose fact:** Regular insulin hyperkalemia: 10 units IV + D50W 50 mL (if glucose <250). Shifts K+ 0.5–1.5 mEq/L. Recheck BG q1h.
- **Anchor taught:** '10 units + 50 mL D50.' The pairing is the key: insulin drops K+ but also drops glucose — always give D50 together. Check BG every hour afterward. Does not REMOVE potassium — still need kayexalate/patiromer/dialysis.
- **Source:** UpToDate hyperkalemia management; AHA/ACC guidelines

## [ ] Senna / Docusate (bowel regimen)  (`senna_docusate`, tier 1, RECALL-ONLY)
- **Context:** Constipation prevention — bowel regimen on ward
- **Dose fact:** Bowel regimen: senna 2 tabs PO BID + docusate 100 mg PO BID. Always prescribe with opioids. Docusate alone is insufficient.
- **Anchor taught:** 'Senna + Docusate = the opioid bowel kit.' Senna stimulates peristalsis (the active ingredient), docusate softens. Docusate alone does nothing on opioids — the gut is paralyzed by mu receptors and needs stimulation.
- **Source:** UpToDate constipation; SHM opioid bowel management guidelines

## [ ] Vancomycin (weight-based loading dose)  (`vancomycin_weight_based`, tier 1, weight_based)
- **Context:** Serious MRSA infection initial dosing
- **Dose fact:** Vancomycin loading dose: 25–30 mg/kg IV for serious infection (MRSA/bacteremia)
- **Grades with:** `{"mg_per_kg": 25}` over `{"weight_kg": [50, 120]}` → answer in **mg**
- **Anchor taught:** Vanco load = 25 mg/kg (think '25 = quarter-kilo per kg'). Target AUC/MIC ≥400, not just trough. Infuse slowly (2–3h) to avoid red man.
- **Source:** ASHP/IDSA/SIDP vancomycin guidelines 2020

## [ ] Warfarin  (`warfarin_initiation`, tier 1, RECALL-ONLY)
- **Context:** New warfarin initiation — inpatient or outpatient
- **Dose fact:** Warfarin start: 5 mg PO daily (healthy adult); 2–2.5 mg in elderly/liver disease. INR target 2–3 for most.
- **Anchor taught:** 'Warfarin starts at 5 mg.' Half it (2–2.5 mg) for the frail/sick: elderly, liver disease, poor nutrition (vitamin K depleted already). Check INR in 2–3 days.
- **Source:** UpToDate warfarin initiation; ACC/AHA Afib guidelines

## [ ] Amiodarone (ACLS VF/pulseless VT)  (`amiodarone_acls_vfib`, tier 2, mass_to_volume)
- **Context:** Cardiac arrest — pulseless VT / VF
- **Dose fact:** Amiodarone cardiac arrest: 300 mg IV push after 3rd shock, second dose 150 mg
- **Grades with:** `{"dose_mg": 300, "concentration_mg_mL": 50.0}` over `{"weight_kg": [60, 100]}` → answer in **mL**
- **Anchor taught:** Amio arrest = 300 mg first, 150 mg second. '3-1-5': 300 first dose, 150 second. Concentration 50 mg/mL = 6 mL for 300 mg.
- **Source:** AHA ACLS guidelines 2020

## [ ] Bupivacaine (plain)  (`bupivacaine_max`, tier 2, max_dose)
- **Context:** Regional/local anesthesia maximum dose
- **Dose fact:** Bupivacaine max: 2.5 mg/kg (most cardiotoxic LA)
- **Grades with:** `{"mg_per_kg": 2.5, "concentration_mg_mL": 5.0}` over `{"weight_kg": [50, 100], "concentration_pct": {"choices": [0.25, 0.5]}}` → answer in **mL**
- **Anchor taught:** Bupiv max = 2.5 mg/kg — the most dangerous LA, smallest ceiling. 'B for Bupiv = Brutal on the heart' — even small intravascular doses arrest.
- **Source:** Miller's Anesthesia 9th ed; ASRA guidelines

## [ ] Calcium gluconate (hyperkalemia)  (`calcium_gluconate_hyperkalemia`, tier 2, mass_to_volume)
- **Context:** Cardiac membrane stabilization in hyperkalemia
- **Dose fact:** Calcium gluconate hyperkalemia: 1 g IV (10 mL of 10%) over 2–3 min — stabilizes membrane, does NOT lower K+
- **Grades with:** `{"dose_mg": 1000, "concentration_mg_mL": 100.0}` over `{"weight_kg": [60, 100]}` → answer in **mL**
- **Anchor taught:** CaGluc = '1 gram, 10 mL, 10%' — easy triple-10 rule. It buys 30–60 min of cardiac protection while you actually lower the potassium.
- **Source:** UpToDate hyperkalemia management; Marino ICU Book 4th ed

## [ ] Dextrose 50% (D50W)  (`d50_hypoglycemia`, tier 2, mass_to_volume)
- **Context:** Symptomatic hypoglycemia IV treatment
- **Dose fact:** D50W hypoglycemia: 25 g IV = 50 mL of D50W
- **Grades with:** `{"dose_mg": 25000, "concentration_mg_mL": 500.0}` over `{"weight_kg": [50, 100]}` → answer in **mL**
- **Anchor taught:** D50 = '25 grams = 50 mL'. The concentration is 50% = 500 mg/mL. 25 g ÷ 0.5 g/mL = 50 mL. Extravasation causes necrosis — big vein or dilute.
- **Source:** ADA hypoglycemia guidelines; UpToDate inpatient hypoglycemia

## [ ] Dantrolene  (`dantrolene_mh`, tier 2, weight_based)
- **Context:** Malignant hyperthermia treatment
- **Dose fact:** Dantrolene for MH: 2.5 mg/kg IV bolus, repeat q5min to max 10 mg/kg
- **Grades with:** `{"mg_per_kg": 2.5}` over `{"weight_kg": [50, 120]}` → answer in **mg**
- **Anchor taught:** MH: 2.5 mg/kg = DANGER × 2.5. You can repeat up to 10 mg/kg total (4 doses). Every second counts — pre-mixing saves lives.
- **Source:** MHAUS guidelines; Morgan & Mikhail 6th ed

## [ ] Epinephrine (ACLS cardiac arrest)  (`epinephrine_acls_cardiac_arrest`, tier 2, mass_to_volume)
- **Context:** Cardiac arrest (any rhythm) — vasopressor
- **Dose fact:** Epinephrine cardiac arrest: 1 mg IV/IO q3–5 min; 1:10,000 stock = 0.1 mg/mL = 10 mL per dose
- **Grades with:** `{"dose_mg": 1, "concentration_mg_mL": 0.1}` over `{"weight_kg": [60, 100]}` → answer in **mL**
- **Anchor taught:** Epi arrest = 1 mg q3–5 min. Stock is 1:10,000 (0.1 mg/mL) — so 1 mg = 10 mL. Compare anaphylaxis: 0.3–0.5 mg IM from 1:1,000 (much more concentrated).
- **Source:** AHA ACLS guidelines 2020

## [ ] Flumazenil (benzodiazepine reversal)  (`flumazenil_benzo_reversal`, tier 2, mass_to_volume)
- **Context:** Benzodiazepine-induced respiratory depression
- **Dose fact:** Flumazenil: 0.2 mg IV over 15s, repeat q60s to max 1 mg. SHORT half-life — re-sedation risk.
- **Grades with:** `{"dose_mg": 0.2, "concentration_mg_mL": 0.1}` over `{"weight_kg": [50, 100]}` → answer in **mL**
- **Anchor taught:** Flumazenil = 0.2 mg q60s, max 1 mg. Short half-life → re-sedation is the trap. NEVER use in benzo-dependent or TCA overdose (seizures).
- **Source:** Morgan & Mikhail 6th ed; UpToDate benzodiazepine toxicity

## [ ] Heparin (STEMI/ACS bolus)  (`heparin_bolus`, tier 2, weight_based)
- **Context:** STEMI/ACS weight-based heparin bolus
- **Dose fact:** Heparin STEMI bolus: 60 units/kg IV (max 5,000 units), then 12 units/kg/hr maintenance
- **Grades with:** `{"mg_per_kg": 0, "units_per_kg": 60}` over `{"weight_kg": [60, 110]}` → answer in **units**
- **Anchor taught:** Heparin bolus = 60 units/kg for STEMI. '60 for the coronary' — easy 60, capped at 5,000 units. Maintenance 12 units/kg/hr.
- **Source:** AHA/ACC STEMI guidelines 2013/2022 update

## [ ] Hypertonic Saline / Na correction limit  (`hypertonic_saline_na_correction`, tier 2, rate_limited_correction)
- **Context:** Severe symptomatic hyponatremia — max correction rate
- **Dose fact:** Hyponatremia max correction: ≤10 mEq/L per 24h (prevent ODS/CPM); acute seizures: 4–6 mEq rapid raise first
- **Grades with:** `{"max_correction_meq_per_24h": 10, "safe_rapid_bolus_meq": 6}` over `{"weight_kg": [60, 100], "current_na": [115, 125], "target_na_rapid": 121}` → answer in **mEq/L over 24h**
- **Anchor taught:** Na correction max = 10 mEq/24h. Exceed it → ODS (osmotic demyelination = locked-in). For seizing: raise 4–6 mEq FAST first, then slow down to stay under the ceiling.
- **Source:** NEJM 2015 Hyponatremia review; Ellison & Berl NEJM 2007

## [ ] Insulin infusion (DKA/HHS)  (`insulin_drip`, tier 2, infusion_rate)
- **Context:** DKA insulin drip
- **Dose fact:** Insulin drip (DKA): 0.1 units/kg/hr, hold if K+ <3.3, standard conc 1 unit/mL
- **Grades with:** `{"concentration_mcg_mL": null, "concentration_units_per_mL": 1.0, "dose_units_kg_hr": 0.1}` over `{"weight_kg": [60, 120]}` → answer in **units/hr**
- **Anchor taught:** DKA insulin = 0.1 units/kg/hr. '0.1 for DKA' — no bolus (ADA 2009). ALWAYS check K+ first: if <3.3, fix the K+ before touching insulin or you'll arrest the heart.
- **Source:** ADA DKA guidelines 2009/2022; UpToDate DKA management

## [ ] Lidocaine (with epinephrine)  (`lidocaine_max_with_epi`, tier 2, max_dose)
- **Context:** Regional/local anesthesia maximum dose with epinephrine
- **Dose fact:** Lidocaine max (with epi): 7 mg/kg
- **Grades with:** `{"mg_per_kg": 7.0, "concentration_mg_mL": 10.0}` over `{"weight_kg": [50, 100], "concentration_pct": [0.5, 1.0, 1.5, 2.0]}` → answer in **mL**
- **Anchor taught:** Lido+epi = 7 mg/kg — think 'lucky 7'. Epi squeezes the vessels so drug stays local longer, allowing 55% more.
- **Source:** Miller's Anesthesia 9th ed

## [ ] Lidocaine (without epinephrine)  (`lidocaine_max_without_epi`, tier 2, max_dose)
- **Context:** Regional/local anesthesia maximum dose
- **Dose fact:** Lidocaine max (no epi): 4.5 mg/kg
- **Grades with:** `{"mg_per_kg": 4.5, "concentration_mg_mL": 10.0}` over `{"weight_kg": [50, 100], "concentration_pct": [0.5, 1.0, 1.5, 2.0]}` → answer in **mL**
- **Anchor taught:** Lido no-epi = 4.5 mg/kg. Remember '4.5' as 'four-and-a-half' — less than the '7' you get with epi because without vasoconstriction, absorption is faster.
- **Source:** Miller's Anesthesia 9th ed; UpToDate local anesthetic toxicity

## [ ] Magnesium sulfate (eclampsia load)  (`magnesium_eclampsia`, tier 2, mass_to_volume)
- **Context:** Eclampsia seizure prophylaxis/treatment loading dose
- **Dose fact:** Magnesium sulfate eclampsia: 4–6 g IV load over 20–30 min, then 1–2 g/hr
- **Grades with:** `{"dose_mg": 4000, "concentration_mg_mL": 200.0}` over `{"weight_kg": [60, 90]}` → answer in **mL**
- **Anchor taught:** Mag eclampsia = 4–6 g load. Toxicity watch: patellar reflexes gone first, then respiratory arrest. Antidote: 1 g calcium gluconate IV. 'Check reflexes before each dose.'
- **Source:** ACOG Practice Bulletin 2019; Magpie Trial

## [ ] Maintenance Fluids (4-2-1 rule)  (`maintenance_fluids_421`, tier 2, rate_limited_correction)
- **Context:** Pediatric / adult maintenance fluid rate calculation
- **Dose fact:** Maintenance fluids: 4-2-1 rule — 4 for first 10 kg, 2 for next 10 kg, 1 for every kg >20 kg
- **Grades with:** `{"rule": "4-2-1", "rate_first_10kg": 4, "rate_next_10kg": 2, "rate_above_20kg": 1}` over `{"weight_kg": [10, 80]}` → answer in **mL/hr**
- **Anchor taught:** 4-2-1: counts DOWN as weight goes UP. First 10 kg = 4 mL/kg/hr, next 10 kg = 2 mL/kg/hr, rest = 1 mL/kg/hr. Adult shortcut: weight + 40 = mL/hr.
- **Source:** Holliday & Segar 1957; Morgan & Mikhail 6th ed perioperative fluids

## [ ] Mannitol (ICP reduction)  (`mannitol_icp`, tier 2, RECALL-ONLY)
- **Context:** Intracranial hypertension / herniation
- **Dose fact:** Mannitol for ICP: 0.5–1 g/kg IV; 20% mannitol = 5 mL/kg per 1 g/kg dose
- **Anchor taught:** Mannitol = 1 g/kg for herniation (emergent), 0.5 g/kg for ICP maintenance. 20% = 200 mg/mL = 5 mL per gram. Hold if Osm >320.
- **Source:** Neurocritical Care Society guidelines; UpToDate ICP management

## [ ] N-Acetylcysteine (NAC) — acetaminophen overdose  (`nac_acetaminophen_overdose`, tier 2, weight_based)
- **Context:** Acetaminophen hepatotoxicity treatment (IV 21h protocol)
- **Dose fact:** NAC acetaminophen: 150 mg/kg load over 1h, then 50 mg/kg over 4h, then 100 mg/kg over 16h (total 300 mg/kg, 21h)
- **Grades with:** `{"mg_per_kg": 150}` over `{"weight_kg": [50, 100]}` → answer in **mg (loading dose)**
- **Anchor taught:** NAC = 150-50-100 over 1-4-16h (total 300 mg/kg in 21h). The load is the biggest hit: 150 mg/kg. '150 for the liver.'
- **Source:** UpToDate acetaminophen poisoning; Rumack-Matthew nomogram

## [ ] Naloxone (opioid reversal)  (`naloxone_opioid_reversal`, tier 2, weight_based)
- **Context:** Opioid-induced respiratory depression
- **Dose fact:** Naloxone opioid reversal: 0.04–0.1 mg IV q2–3 min, titrate to breathing (not full reversal)
- **Grades with:** `{"mg_per_kg": 0.001}` over `{"weight_kg": [50, 100]}` → answer in **mg**
- **Anchor taught:** Narcan: 'Start LOW — 0.04 mg and go slow.' Full reversal = acute withdrawal + pain crisis. Titrate to respirations, NOT to waking up screaming.
- **Source:** UpToDate opioid overdose; SAMHSA guidelines

## [ ] Norepinephrine  (`norepinephrine_infusion`, tier 2, infusion_rate)
- **Context:** Septic shock vasopressor infusion
- **Dose fact:** Norepinephrine: first-line vasopressor for septic shock, 0.01–0.5 mcg/kg/min, standard conc 16 mcg/mL
- **Grades with:** `{"concentration_mcg_mL": 16.0}` over `{"weight_kg": [50, 120], "dose_mcg_kg_min": [0.05, 0.1, 0.2, 0.3]}` → answer in **mL/hr**
- **Anchor taught:** NE = first-line for sepsis (Surviving Sepsis). Range: 0.01–0.5 mcg/kg/min. Think of it as a dial — start low, titrate to MAP >65.
- **Source:** Marino ICU Book 4th ed; Surviving Sepsis Campaign 2021

## [ ] Pediatric IV Fluid Bolus  (`pediatric_fluid_bolus`, tier 2, weight_based)
- **Context:** Hypovolemia / sepsis fluid resuscitation
- **Dose fact:** Pediatric fluid bolus: 20 mL/kg isotonic crystalloid IV over 5–15 min
- **Grades with:** `{"mg_per_kg": 0, "mL_per_kg": 20}` over `{"weight_kg": [10, 40]}` → answer in **mL**
- **Anchor taught:** Peds bolus = 20 mL/kg. The number is memorable because it matches the adult 'give 2L' feeling — scaled per weight. Cap at 40–60 mL/kg total before escalating.
- **Source:** PALS guidelines; Surviving Sepsis Campaign pediatric 2020

## [ ] Phenylephrine  (`phenylephrine_infusion`, tier 2, infusion_rate)
- **Context:** Vasopressor infusion for hypotension
- **Dose fact:** Phenylephrine: pure alpha-1, 0.5–5 mcg/kg/min, standard conc 100 mcg/mL
- **Grades with:** `{"concentration_mcg_mL": 100.0}` over `{"weight_kg": [50, 100], "dose_mcg_kg_min": [0.5, 1.0, 1.5, 2.0]}` → answer in **mL/hr**
- **Anchor taught:** Phenylepherine = pure alpha. No beta, no HR increase — perfect for tachycardia + hypotension. Dose: 0.5–5 mcg/kg/min.
- **Source:** Miller's Anesthesia 9th ed; Morgan & Mikhail 6th ed

## [ ] Phenytoin / Fosphenytoin (loading dose)  (`phenytoin_load`, tier 2, weight_based)
- **Context:** Status epilepticus second-line agent
- **Dose fact:** Phenytoin/fosphenytoin status epilepticus: 20 mg/kg IV (fosphenytoin preferred, faster infusion rate)
- **Grades with:** `{"mg_per_kg": 20}` over `{"weight_kg": [50, 100]}` → answer in **mg**
- **Anchor taught:** Phenytoin/fosp = 20 mg/kg. Both the same dose: 20 mg/kg. Fosphenytoin is safer (no propylene glycol, faster rate). In NS only — precipitates in dextrose.
- **Source:** Epilepsy Foundation status epilepticus guidelines; Neurocritical Care Society 2012

## [ ] Propofol  (`propofol_induction`, tier 2, weight_based)
- **Context:** Induction of general anesthesia
- **Dose fact:** Propofol induction: 1.5–2.5 mg/kg IV (typical 2 mg/kg)
- **Grades with:** `{"mg_per_kg": 2.0}` over `{"weight_kg": [50, 100]}` → answer in **mg**
- **Anchor taught:** Propofol = 2 mg/kg (think 'P2'). Halve it in elderly/sick — same drop in consciousness, but their cardiovascular reserve is already gone.
- **Source:** Morgan & Mikhail 6th ed; Miller's Anesthesia 9th ed

## [ ] Rocuronium  (`rocuronium_intubation`, tier 2, weight_based)
- **Context:** RSI intubation
- **Dose fact:** Rocuronium RSI: 1.2 mg/kg IV
- **Grades with:** `{"mg_per_kg": 1.2}` over `{"weight_kg": [50, 120]}` → answer in **mg**
- **Anchor taught:** ROC gets 1.2 — the high dose that matches sux speed. Normal induction is only 0.6 mg/kg; doubling it buys the same 60-second window.
- **Source:** Miller's Anesthesia 9th ed; Sugammadex reversal per ASA guidelines

## [ ] Ropivacaine  (`ropivacaine_max`, tier 2, max_dose)
- **Context:** Regional/local anesthesia maximum dose
- **Dose fact:** Ropivacaine max: 3 mg/kg
- **Grades with:** `{"mg_per_kg": 3.0, "concentration_mg_mL": 7.5}` over `{"weight_kg": [50, 100], "concentration_pct": [0.2, 0.5, 0.75]}` → answer in **mL**
- **Anchor taught:** Ropiv = 3 mg/kg — between bupiv (2.5) and lido-no-epi (4.5), safer cardiac profile than bupiv. 'R for Reasonable' — the middle child of regional anesthesia.
- **Source:** Miller's Anesthesia 9th ed

## [ ] Succinylcholine  (`succinylcholine_intubation`, tier 2, weight_based)
- **Context:** RSI intubation
- **Dose fact:** Succinylcholine RSI: 1.5 mg/kg IV
- **Grades with:** `{"mg_per_kg": 1.5}` over `{"weight_kg": [50, 120]}` → answer in **mg**
- **Anchor taught:** Think '1.5 = sux': one-and-a-HALF mg/kg — bigger than roc's RSI dose because sux is short-acting and you can give a full bolus.
- **Source:** Miller's Anesthesia 9th ed; Morgan & Mikhail 6th ed

## [ ] Vasopressin  (`vasopressin_infusion`, tier 2, infusion_rate)
- **Context:** Septic shock adjunct vasopressor
- **Dose fact:** Vasopressin: FIXED 0.03–0.04 units/min (not weight-based), added as NE-sparing adjunct in septic shock
- **Grades with:** `{"concentration_mcg_mL": null, "concentration_units_per_mL": 1.0, "fixed_rate_units_per_min": 0.04}` over `{"weight_kg": [60, 100]}` → answer in **units/hr**
- **Anchor taught:** Vaso = FIXED dose, 0.03–0.04 units/min. Unlike every other vasopressor, it's NOT titrated — it's a flat add-on. 'Vaso is on or off, like a faucet, not a dial.'
- **Source:** Surviving Sepsis Campaign 2021; Marino ICU Book 4th ed
