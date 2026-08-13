#!/usr/bin/env python3
"""
Phase 3.1: Sepsis & Septic Shock Knowledge Units

Generates 50-70 high-acuity medical knowledge units covering:
- Sepsis definition, qSOFA, SOFA scoring
- Early recognition and first-hour bundle
- Source control, antibiotic selection
- Fluid resuscitation and vasopressors
- Monitoring and complications
- Prognosis
"""

import json
from datetime import datetime

def create_sepsis_units():
    """Generate sepsis knowledge units with comprehensive coverage."""

    units = [
        # === DEFINITIONS & SCORING ===
        {
            "topic": "Sepsis Definition (Surviving Sepsis Campaign)",
            "subtopic": "sepsis_definition",
            "content": "Sepsis = life-threatening organ dysfunction caused by dysregulated host response to infection. Operationally: documented or suspected infection + ≥2 SIRS criteria (temp >38°C or <36°C, HR >90, RR >20 or PaCO2 <32, WBC >12k or <4k or >10% bands). The 2016 update emphasizes organ dysfunction (SOFA score) over SIRS, though SIRS remains clinically useful for screening. Key distinction: infection alone is not sepsis; dysregulation is.",
            "tags": ["sepsis", "definition", "sirs_sepsis", "high_yield"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Septic Shock Definition",
            "subtopic": "septic_shock_definition",
            "content": "Septic shock = sepsis + persistent hypotension requiring vasopressors to maintain MAP ≥65 mmHg despite adequate fluid resuscitation + serum lactate >2 mmol/L. Mortality rises sharply with shock; requires urgent vasopressor initiation (within 1 hour if lactate elevated). Unlike cardiogenic shock, peripheral vascular resistance is typically low. Blood cultures must be drawn before antibiotics.",
            "tags": ["sepsis", "shock", "hypotension", "vasopressors"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "qSOFA Score (Quick Sequential Organ Failure Assessment)",
            "subtopic": "qsofa_scoring",
            "content": "qSOFA = bedside tool for rapid sepsis severity assessment. 3 variables: altered mentation (confusion, disorientation), SBP ≤100 mmHg, RR ≥22 breaths/min. Score ≥2 predicts ≥1 bad outcome (ICU admission, death) with 66% sensitivity, 90% specificity. NOT diagnostic for sepsis (use SIRS + infection), but excellent for risk stratification. Used to flag non-ICU patients who may deteriorate rapidly.",
            "tags": ["sepsis", "qsofa", "scoring", "risk_stratification"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "SOFA Score (Sequential Organ Failure Assessment)",
            "subtopic": "sofa_scoring",
            "content": "SOFA = 6-item scoring system tracking organ dysfunction. Cardiovascular: MAP <70 (1pt), vasoactive agents (2-4 pts depending on agent/dose). Respiratory: PaO2/FiO2 ratio <400 (1pt), <300 (2pts), <200 on ventilator (3pts), <100 on ventilator (4pts). Coagulation: platelets <150k (1pt), <100k (2pts), <50k (3pts), <20k (4pts). Liver: bilirubin 1.2-1.9 (1pt), 2.0-5.9 (2pts), 6.0-11.9 (3pts), >12 (4pts). Renal: creatinine 1.2-1.9 or UO <500 mL/day (1pt), 2.0-3.9 or <200 mL/day (2pts), 3.5-4.9 or anuria <12h (3pts), >5.0 or anuria >12h (4pts). CNS: GCS 13-14 (1pt), 10-12 (2pts), 6-9 (3pts), <6 (4pts). Total 0-24; ≥2 suggests high mortality risk.",
            "tags": ["sepsis", "sofa", "organ_failure", "prognosis"],
            "library": "intern_year_medicine"
        },

        # === EARLY RECOGNITION & FIRST HOUR ===
        {
            "topic": "Sepsis First-Hour Bundle (Surviving Sepsis Campaign 2021)",
            "subtopic": "early_recognition",
            "content": "Time-critical interventions within 60 minutes of sepsis recognition: (1) Measure lactate; (2) Obtain blood cultures before antibiotics; (3) Administer broad-spectrum antibiotics (typically 3-drug combination); (4) Initiate IV fluid resuscitation (30 mL/kg crystalloid bolus if hypotensive or lactate ≥4 mmol/L); (5) Apply vasopressors if MAP inadequate after fluids; (6) Reassess lactate if initially elevated. Mortality improves dramatically with each hour of delay, especially for antibiotics.",
            "tags": ["sepsis", "early_recognition", "bundle", "first_hour"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Lactate Clearance in Sepsis",
            "subtopic": "sepsis_monitoring",
            "content": "Serum lactate = surrogate for anaerobic metabolism and tissue hypoperfusion. Normal <2 mmol/L. Elevated lactate (≥2 mmol/L, especially ≥4) indicates inadequate oxygen delivery or mitochondrial dysfunction. Lactate clearance = % decrease in lactate from initial to reassessment (3 hours): >10% clearance = favorable; <10% = poor prognosis, need escalation. Even with normalized MAP, persistent elevated lactate suggests ongoing organ hypoperfusion. Measured in arterial blood or (less reliable) venous blood.",
            "tags": ["sepsis", "lactate", "tissue_perfusion", "monitoring"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Blood Cultures & Timing in Sepsis",
            "subtopic": "sepsis_diagnostics",
            "content": "Blood cultures must be drawn BEFORE antibiotics (even if delay unavoidable, draw first). Ideally 2 sets from different sites (arm vs. line if available, not simultaneous to minimize contamination). Timing: at least 30-60 min before antibiotics started. Culture positivity guides de-escalation; negative cultures don't exclude sepsis (only ~50% culture-positive even with proven infection). Obtain cultures from arterial lines only if >5 cm indwelling. Contamination common (coagulase-negative Staph from skin); clinical judgment needed.",
            "tags": ["sepsis", "blood_culture", "diagnostics", "antibiotics"],
            "library": "intern_year_medicine"
        },

        # === SOURCE CONTROL ===
        {
            "topic": "Source Control in Sepsis - Principles",
            "subtopic": "source_control",
            "content": "Source control = identification and elimination of infection focus. Mandatory for any drainable collection (abscess, empyema, infected fluid) or purulent focus (gangrenous bowel, devitalized tissue). Modalities: percutaneous drainage (preferred if accessible), antibiotics alone insufficient for localized collection. Timing: should occur within 6-12 hours of diagnosis when feasible. Examples: drain abdominal abscess, remove infected lines (CVCs, urinary catheters), debridement of necrotic tissue, appendectomy for perforated appendicitis. Mortality increases if source control delayed.",
            "tags": ["sepsis", "source_control", "drainage", "management"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Infected Central Lines & Line Replacement",
            "subtopic": "source_control",
            "content": "If bacteremia/fungemia and CVCs in situ, remove lines immediately (assuming another access available). Do NOT replace over guidewire (high failure rate, reinfection). Redraw blood cultures from peripheral site after line removal to confirm clearance. If no alternative access, femoral or subclavian line must be placed at different site after thorough skin prep (chlorhexidine, povidone-iodine). Timing: remove line same day; replace after 24h if continued access needed. Some recommendations: retain peripherally-inserted lines (PICCs) only if no other source found and patient improving.",
            "tags": ["sepsis", "source_control", "central_lines", "infection"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Urinary Catheter Management in Sepsis",
            "subtopic": "source_control",
            "content": "Indwelling urinary catheters increase UTI/urosepsis risk. Management: remove catheter as soon as feasible (within 24-48h if possible). If urosepsis diagnosed, remove catheter even if no mechanical obstruction apparent. Urine culture obtained from catheter specimen collection port (NOT from bag). If retention suspected, perform bladder scan; consider intermittent straight cath or suprapubic cath if long-term retention. Antibiotic-coated catheters reduce bacteriuria but do not eliminate sepsis risk.",
            "tags": ["sepsis", "source_control", "urinary_catheter", "urosepsis"],
            "library": "intern_year_medicine"
        },

        # === ANTIBIOTIC SELECTION ===
        {
            "topic": "Empiric Broad-Spectrum Antibiotics - Initial Selection",
            "subtopic": "antibiotics_empiric",
            "content": "First-line broad-spectrum coverage for sepsis of unknown source: combination therapy typically 2-3 drugs. Most common: (1) beta-lactam (piperacillin-tazobactam, meropenem, cefepime) PLUS (2) fluoroquinolone (levofloxacin, ciprofloxacin) for Gram-negative coverage PLUS (3) vancomycin for MRSA if risk factors (healthcare exposure, ICU admission, prior MRSA). Dosing critical: use renal dose adjustments if eGFR <30. Obtain appropriate cultures (blood, urine, respiratory if applicable) BEFORE antibiotics. Redose vancomycin per levels (trough 15-20 mcg/mL); adjust beta-lactams per renal function.",
            "tags": ["sepsis", "antibiotics", "empiric_coverage", "gram_negative"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "De-escalation & Culture-Directed Antibiotics",
            "subtopic": "antibiotics_deescalation",
            "content": "Once culture & susceptibilities available (typically 24-48h), narrow spectrum to target organism. Example: if blood culture grows E. coli susceptible to ceftriaxone, switch from piperacillin-tazobactam + vancomycin + levofloxacin to ceftriaxone monotherapy. De-escalation reduces resistance selection, toxicity, cost. If no organism identified after 72h and patient improving, consider stopping antibiotics. If cultures negative but clinical suspicion remains high (e.g., endocarditis), maintain coverage pending imaging/repeat cultures. Always match antibiotic selection to probable source (e.g., IV drug user → Staph; recent GI surgery → Gram-neg + anaerobes).",
            "tags": ["sepsis", "antibiotics", "deescalation", "culture_directed"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Antibiotic Source-Based Selection",
            "subtopic": "antibiotics_source",
            "content": "Tailor empiric antibiotics to presumed infection source: (1) Respiratory (pneumonia): cefepime, fluoroquinolone, or azithromycin for atypical coverage; (2) Abdominal (peritonitis, cholecystitis): piperacillin-tazobactam, meropenem, or cefepime + metronidazole for anaerobes; (3) Urinary (pyelonephritis, UTI): fluoroquinolone, cephalosporin, or aminoglycoside; (4) Skin/soft tissue (cellulitis, abscess): vancomycin + beta-lactam for group A Strep + MRSA; (5) Meningitis: ceftriaxone 2g q12h + vancomycin 15-20 mg/kg q8-12h + ampicillin if Listeria risk. Source identification often delays diagnosis; empiric broad-spectrum coverage essential initially.",
            "tags": ["sepsis", "antibiotics", "source_directed"],
            "library": "intern_year_medicine"
        },

        # === FLUID RESUSCITATION ===
        {
            "topic": "Crystalloid Fluid Resuscitation - Initial Bolus",
            "subtopic": "fluid_resuscitation",
            "content": "First-line fluid for septic shock: crystalloid IV bolus 30 mL/kg body weight over 1-2 hours (e.g., 2.1 L for 70 kg patient) if hypotensive or lactate ≥4 mmol/L. Monitor for improvement: SBP >90, MAP >65, HR slowing, improved perfusion (warm extremities, capillary refill <2s). Fluid responsiveness assessed by: response to 500 mL bolus (SBP rise >10 mmHg or HR drop >10 bpm); pulse pressure variation <13% on ventilator; inferior vena cava collapsibility >50%. If no improvement after 30 mL/kg, escalate vasopressors. Reassess for over-resuscitation (pulmonary edema, increasing lactate from gut ischemia).",
            "tags": ["sepsis", "fluid_resuscitation", "crystalloid", "bolus"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Vasopressor Selection & Dosing",
            "subtopic": "vasopressors",
            "content": "After fluid resuscitation, if MAP <65 mmHg despite fluids, initiate vasopressor: (1) Norepinephrine (Levophed) = first-line ONLY agent (alpha + beta effects, improves mortality vs. dopamine). Dose 0.01-0.5 mcg/kg/min; target MAP ≥65. (2) Epinephrine = added if norepinephrine + low cardiac output. (3) Dopamine = NO LONGER RECOMMENDED as first-line (increased arrhythmia risk vs. NE). (4) Phenylephrine = pure alpha-agonist, use ONLY if inadequate perfusion contraindication (e.g., ACS). (5) Vasopressin = adjunct to catecholamines in refractory shock, no mortality benefit. Tie to arterial line for continuous monitoring; reassess after each dose change. Wean as MAP/perfusion improves.",
            "tags": ["sepsis", "vasopressors", "norepinephrine", "shock"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Colloid vs. Crystalloid - Current Evidence",
            "subtopic": "fluid_resuscitation",
            "content": "Crystalloid (normal saline, Ringer's lactate) is standard first-line for sepsis fluid resuscitation. Colloids (albumin, dextran, hydroxyethyl starch) have NOT improved mortality vs. crystalloid in major RCTs (ALBIOS, 6S trial, CHEST trial). Albumin expensive, transfusion reaction risk; HES associated with AKI, increased transfusion. Modern practice: crystalloid for initial resuscitation. Albumin may be considered in established sepsis if large volumes crystalloid already given (no mortality benefit, but may reduce further crystalloid accumulation). Avoid HES entirely in sepsis.",
            "tags": ["sepsis", "fluid_resuscitation", "colloid", "evidence"],
            "library": "intern_year_medicine"
        },

        # === ADJUNCTIVE THERAPIES ===
        {
            "topic": "Corticosteroids in Sepsis & Septic Shock",
            "subtopic": "adjunctive_therapy",
            "content": "Role of corticosteroids in sepsis remains controversial. Evidence: low-dose hydrocortisone (50 mg q6h) may benefit refractory septic shock (persistent hypotension despite fluids + vasopressors, especially with adrenal insufficiency). CORTICUS trial showed modest benefit in vasopressor-dependent shock. Mechanism: restore vascular tone, improve myocardial contractility. Typical approach: if vasopressor requirement escalating or prolonged (>48h), consider hydrocortisone 50 mg IV q6h for 7 days OR methylprednisolone 1-2 mg/kg for 3 days. Avoid steroids in early sepsis without refractory shock (may worsen outcomes in milder cases). Screen for adrenal insufficiency (ACTH stimulation) if prolonged ICU stay.",
            "tags": ["sepsis", "corticosteroids", "shock", "refractory"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Inotropes in Sepsis - Indications",
            "subtopic": "adjunctive_therapy",
            "content": "Inotropes (dobutamine, milrinone) improve cardiac contractility but reduce systemic vascular resistance. USE ONLY for low cardiac output states with adequate MAP (not as first-line for septic shock). Indications: persistent hypotension despite vasopressor + fluid resuscitation, plus evidence of low CO (reduced SVO2, prolonged lactate elevation). Dobutamine = beta-1 and beta-2 agonist, increases HR/contractility, reduces afterload. Dose 2-20 mcg/kg/min. Milrinone = phosphodiesterase-3 inhibitor, increases contractility + afterload reduction. Dose 0.25-0.75 mcg/kg/min. Both risk tachycardia, ischemia. Use LOWEST dose for shortest duration; transition to vasopressor-alone strategy if possible. NOT recommended as monotherapy for shock.",
            "tags": ["sepsis", "inotropes", "low_cardiac_output"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Glucose Control in Sepsis",
            "subtopic": "adjunctive_therapy",
            "content": "Hyperglycemia (>180 mg/dL) independently associated with worse outcomes in sepsis. Target: maintain glucose 140-180 mg/dL with IV insulin drips (NOT intensive glycemic control <100, which increased mortality in NICE-SUGAR). Monitor bedside glucose q1-4h initially, less frequently when stable. Insulin dosing: start 1-2 units/h IV, titrate by 0.5-1 unit/h to effect. Recheck glucose after each adjustment. Risk of hypoglycemia: every 1-2h checks, especially when adjusting dosing. Discontinue insulin when oral intake resumes or lactate/LDH improve, transitioning to subcutaneous regimen.",
            "tags": ["sepsis", "glucose_control", "hyperglycemia", "insulin"],
            "library": "intern_year_medicine"
        },

        # === MONITORING & RESPONSE ASSESSMENT ===
        {
            "topic": "Perfusion Assessment in Septic Shock",
            "subtopic": "monitoring_response",
            "content": "Clinical signs of adequate perfusion: warm extremities, normal capillary refill (<2s), conscious/appropriate mental status, urine output >0.5 mL/kg/h. Laboratory markers: lactate <2 mmol/L, normal ScVO2 (central venous oxygen saturation) ≥70% on blood gas, normal anion gap. If inadequate perfusion persists despite MAP ≥65: increase vasopressor dose, reassess fluid status (may need more fluids or diuretics if overloaded), check for ongoing source (e.g., missed bleeding), consider inotropes. Serial lactate measurements every 2-4h guide therapy intensity; persistent elevation despite resuscitation = poor prognostic sign, mortality >20%.",
            "tags": ["sepsis", "monitoring", "perfusion", "assessment"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Central Venous Catheter Monitoring in Sepsis",
            "subtopic": "monitoring_response",
            "content": "Central venous pressure (CVP) monitoring via CVC: normal 8-12 cmH2O. In sepsis, CVP alone is unreliable for fluid responsiveness (variable baseline due to sepsis-induced vasodilation). Useful parameters: CVP response to passive leg raise (increase ≥2 cmH2O suggests continued fluid responsiveness), CVP >15 suggests overload/volume-associated complications. ScVO2 (central venous O2 sat from CVC) ≥70% generally acceptable; <60% suggests inadequate oxygen delivery (increase O2 content, reduce demand, improve cardiac output). CVC allows continuous infusion of vasopressors (required for peripheral access discomfort/extravasation risk).",
            "tags": ["sepsis", "monitoring", "cvc", "cvp"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Urine Output Monitoring in Sepsis",
            "subtopic": "monitoring_response",
            "content": "Target urine output ≥0.5 mL/kg/h (e.g., 35 mL/h for 70 kg patient) reflects adequate renal perfusion. Oliguria (<0.5 mL/kg/h) indicates inadequate renal blood flow OR primary renal injury (AKI). Management: if oliguria with low blood pressure, increase fluids + vasopressors to improve MAP and renal perfusion. If oliguria persists despite MAP ≥65 and adequate perfusion markers, consider AKI likely; avoid aggressive diuretics (may worsen renal function). Monitor urine electrolytes (FeNa) to differentiate prerenal (FeNa <1%) from intrinsic AKI (FeNa >2%). Indwelling catheter allows accurate measurement every 1-2 hours.",
            "tags": ["sepsis", "monitoring", "urine_output", "aki"],
            "library": "intern_year_medicine"
        },

        # === COMPLICATIONS ===
        {
            "topic": "ARDS in Sepsis - Pathophysiology & Management",
            "subtopic": "complications",
            "content": "Acute respiratory distress syndrome (ARDS) develops in 20-40% of sepsis cases, especially pneumonia/aspiration. Berlin definition: PaO2/FiO2 ≤300, bilateral opacities, non-cardiac cause. Pathophysiology: cytokine storm → endothelial injury → capillary leak → pulmonary edema. Management: lung-protective ventilation (6-8 mL/kg IBW, PEEP 5-15 depending on compliance), permissive hypercapnia (PaCO2 <55 acceptable), prone positioning in moderate-severe ARDS (may improve oxygenation). Fluid management: restrictive once stabilized (avoid pulmonary edema). Mortality without mechanical ventilation ~50%; improves with ECMO consideration in refractory cases.",
            "tags": ["sepsis", "complications", "ards", "respiratory_failure"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Acute Kidney Injury in Sepsis",
            "subtopic": "complications",
            "content": "AKI in sepsis = increased creatinine >0.3 mg/dL or ≥50% rise from baseline, OR decreased urine output <0.5 mL/kg/h. Sepsis accounts for ~50% of ICU AKI cases. Mechanism: renal hypoperfusion (septic shock), direct tubular injury (endotoxin, myoglobin from rhabdomyolysis), medications (aminoglycosides, ACE inhibitors during shock). Management: optimize MAP (vasopressors), fluid resuscitation (but avoid overload once stabilized), monitor creatinine + urine output daily, adjust drug dosing (renal function-dependent), consider RRT if K >6, acidemia pH <7.15, pulmonary edema refractory to diuretics, or creatinine >4. Mortality rises with AKI severity; recovery may take weeks.",
            "tags": ["sepsis", "complications", "aki", "renal_failure"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "DIC in Sepsis",
            "subtopic": "complications",
            "content": "Disseminated intravascular coagulation (DIC) occurs in 5-10% of septic shock cases, particularly Gram-negative, meningococcemia. Pathophysiology: tissue factor release → excessive thrombin generation → simultaneous thrombosis + consumption of clotting factors + microangiopathic hemolysis. Presentation: bleeding from multiple sites + thrombosis + organ failure. Lab findings: low platelets, elevated PT/INR, ↓fibrinogen, ↑d-dimer, schistocytes on smear. ISTH scoring helps diagnosis. Management: treat underlying sepsis (antibiotics, source control), supportive transfusion (FFP, platelets, cryoprecipitate), avoid further coagulopathy (strict fluid balance). Prognosis: mortality 30-50% of septic DIC cases.",
            "tags": ["sepsis", "complications", "dic", "coagulopathy"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Sepsis-Induced Cardiomyopathy",
            "subtopic": "complications",
            "content": "Sepsis causes transient myocardial depression in 20-40% of cases, despite adequate filling pressures. Echo findings: reduced EF (often 20-35%), dilated chambers, normal valves. Mechanism: cytokine-mediated myocardial dysfunction (TNF, IL-1, IL-6), impaired contractility recovers over days-weeks. Clinical impact: requires higher fluid volumes, vasopressors, sometimes inotropes. Diagnosis: elevated troponin, BNP/NT-proBNP, echo showing reduced EF. Management: optimize preload (assess with IVC collapsibility, passive leg raise), initiate vasopressors, consider inotropes (milrinone, dobutamine) if low cardiac output persists despite adequate perfusion pressure. Prognosis: most recover completely; EF normalizes by 7-10 days if patient survives.",
            "tags": ["sepsis", "complications", "cardiomyopathy", "myocardial_dysfunction"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Hyperglycemia & Hypoglycemia Complications in Sepsis",
            "subtopic": "complications",
            "content": "Sepsis causes insulin resistance (cytokine-mediated) → hyperglycemia (>180 mg/dL) in 50% non-diabetic patients. Hyperglycemia impairs immune function, increases infection risk, worsens outcomes. Aggressive insulin therapy (<100 mg/dL target) paradoxically WORSENED outcomes in ICU (NICE-SUGAR), likely from hypoglycemia episodes. Modern approach: target 140-180 mg/dL with insulin drips; avoid hypoglycemia (<100) at all costs (increases mortality from seizures, arrhythmias, stroke). Monitor glucose q1-4h. Hypoglycemia in sepsis particularly dangerous (impairs immune response, neurologic complications). Transition to subcutaneous insulin once oral intake resumes.",
            "tags": ["sepsis", "complications", "glucose_dysregulation"],
            "library": "intern_year_medicine"
        },

        # === PROGNOSIS & LONG-TERM OUTCOMES ===
        {
            "topic": "Sepsis Mortality - Risk Factors & Prognosis",
            "subtopic": "prognosis",
            "content": "In-hospital mortality: ~20-30% uncomplicated sepsis, rising to 50%+ in septic shock. Risk factors increasing mortality: age >65, pre-existing comorbidities (COPD, CHF, liver disease, cancer), immunosuppression, delayed antibiotics (each hour delay = ~1% mortality increase), inadequate source control, shock requiring vasopressors, renal failure, ARDS. APACHE II, SOFA scores help prognosticate. Sepsis survivors frequently have long-term disability (weakness, cognitive impairment, PTSD, persistent organ dysfunction) beyond acute hospitalization. Early ICU consultation, aggressive resuscitation, source control, and appropriate antibiotics are critical modifiable factors.",
            "tags": ["sepsis", "prognosis", "mortality", "risk_factors"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Long-Term Outcomes Post-Sepsis",
            "subtopic": "prognosis",
            "content": "Post-sepsis syndrome: survivors often experience weakness, cognitive impairment ('brain fog'), depression, PTSD, functional decline. Critical illness polyneuropathy & myopathy (CIP/CIM) affects 30-50% of sepsis ICU survivors, delaying weaning, causing chronic disability. Rehabilitation often needed; outcomes variable. 1-year mortality in sepsis survivors elevated vs. population (5-10% additional deaths). Immune dysfunction persists post-sepsis: decreased T-cell numbers, impaired response to infections for weeks-months. Goals of care discussion essential; palliative care early in severe sepsis improves outcomes. Follow-up: monitor for recurrent infections, address functional impairment, screen for depression/PTSD.",
            "tags": ["sepsis", "prognosis", "long_term_outcomes", "cip_cim"],
            "library": "intern_year_medicine"
        },

        # === SPECIAL POPULATIONS & CONTEXTS ===
        {
            "topic": "Sepsis in Neutropenic Patients",
            "subtopic": "special_populations",
            "content": "Neutropenic sepsis (absolute neutrophil count <500) requires expedited evaluation. Risk: occult serious infection without typical inflammatory signs (WBC count may remain low). Blood cultures mandatory; empiric broad-spectrum antibiotics STAT (within 1 hour). Common organisms: Gram-negative Enterobacteriaceae, Pseudomonas, Candida in prolonged neutropenia. Typical regimen: cefepime ± aminoglycoside ± vancomycin (depending on institutional resistance patterns). Source often GI tract. Maintain antibiotics until neutrophil recovery (ANC >500). Add antifungal coverage (fluconazole, caspofungin) if prolonged neutropenia (>10 days) or high fever persistence despite antibiotics.",
            "tags": ["sepsis", "special_populations", "neutropenic", "hematologic_malignancy"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Sepsis in Cirrhotic Patients",
            "subtopic": "special_populations",
            "content": "Cirrhosis = profound immunocompromise (complement dysfunction, opsonization impairment, impaired phagocytosis). Sepsis in cirrhosis: mortality 40-60%. Common sources: spontaneous bacterial peritonitis (SBP), UTI, pneumonia, bacteremia. SBP diagnosis: ascitic fluid protein <1 g/dL + PMN count ≥250 cells/mcL in sterile peritonitis (no surgery within 2 weeks, no perforation signs). Empiric antibiotics for SBP: cefotaxime 1g IV q8h or norfloxacin PO 400mg daily (prophylaxis if ascites + low protein). Standard broad-spectrum regimen for other sources. Avoid nephrotoxic agents (NSAIDs, aminoglycosides). Maintain albumin 1.5g/kg if SBP being treated. Prognosis: SBP hospital mortality 10-20% with treatment.",
            "tags": ["sepsis", "special_populations", "cirrhosis", "sbp"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Urosepsis - Recognition & Management",
            "subtopic": "special_populations",
            "content": "Urosepsis = sepsis originating from urinary tract infection. Common in patients with urinary obstruction (stones, strictures, malignancy), indwelling catheters, neurogenic bladder, pregnancy. Risk higher in men >50y and diabetics. Sources: upper UTI (pyelonephritis, perinephric abscess) > lower UTI (cystitis, prostatitis). Management: early antibiotics (fluoroquinolone, cephalosporin, or aminoglycoside covering E. coli, Klebsiella, Pseudomonas), urological imaging (ultrasound, CT) to identify obstruction/abscess, urgent decompression if obstructed (Foley catheter, percutaneous nephrostomy, stent). Remove existing indwelling catheters. Prognosis: excellent with early recognition and drainage (mortality <5% uncomplicated, higher with obstruction/septic shock).",
            "tags": ["sepsis", "special_populations", "urosepsis", "urinary_tract"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Respiratory Tract Sepsis (Pneumonia-Derived)",
            "subtopic": "special_populations",
            "content": "Sepsis from lower respiratory infection: most common source of sepsis overall. Bacteria: S. pneumoniae, H. influenzae (CAP), Pseudomonas, MRSA (HAP/VAP). Presentation: fever, cough, dyspnea, often with ARDS. Diagnosis: CXR (infiltrate), sputum culture (if productive), blood cultures. Empiric treatment: CAP = amoxicillin-clavulanate or fluoroquinolone ± macrolide; HAP/VAP = cefepime/piperacillin-tazobactam ± fluoroquinolone ± vancomycin. Source control: typically medical (antibiotics) unless empyema present (then drainage). Duration: 7-10 days typically for CAP, longer for resistant organisms. Ventilator-associated pneumonia (VAP) in intubated patients adds mortality; minimize sedation, early mobilization, aggressive weaning to reduce risk.",
            "tags": ["sepsis", "special_populations", "respiratory_sepsis", "pneumonia"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Abdominal Sepsis - Perforated Viscus",
            "subtopic": "special_populations",
            "content": "Sepsis from abdominal perforation (peptic ulcer, appendicitis, bowel ischemia) = surgical emergency. Presentation: acute severe abdominal pain, rigidity, rebound tenderness, fever, shock. Diagnosis: upright CXR (free air under diaphragm), CT (if stable). Empiric antibiotics: piperacillin-tazobactam or cefepime + metronidazole to cover Gram-negatives + anaerobes. Source control: emergent surgery (repair perforation, debridement ischemic tissue). Pre-operative resuscitation: aggressive fluids, vasopressors if hypotensive, broad-spectrum antibiotics within 1 hour. Mortality: 10-30% depending on delay to surgery and peritonitis duration. Post-operative: continue antibiotics 5-7 days; remove NG tubes, resume feeds early if feasible.",
            "tags": ["sepsis", "special_populations", "abdominal_sepsis", "surgical"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Sepsis in Pregnancy & Peripartum",
            "subtopic": "special_populations",
            "content": "Sepsis in pregnancy/peripartum period = high-risk, rapid progression. Common sources: chorioamnionitis (intrauterine infection), postpartum endometritis, wound infection post-cesarean, urinary sepsis. Unique considerations: pregnant women have blunted febrile response (immunotolerance), tachycardia/tachypnea normal (hard to distinguish from sepsis), hypotension more damaging (placental perfusion at risk). Diagnosis: fever + leukocytosis + source; SOFA score valid but harder to interpret. Empiric antibiotics: cefoxitin (covers Gram-negatives + anaerobes) or clindamycin + gentamicin; add vancomycin if MRSA risk. Source control: urgent dilation & curettage if retained products (chorioamnionitis/endometritis), adequate drainage. Prognosis: with early antibiotics + source control, mortality <5%. Maternal sepsis also risks fetal loss/prematurity.",
            "tags": ["sepsis", "special_populations", "pregnancy", "peripartum"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Meningococcal Sepsis - Recognition & Urgent Management",
            "subtopic": "special_populations",
            "content": "Neisseria meningitidis causes fulminant sepsis with high mortality if untreated. Presentation: petechial rash (non-blanching, progresses to purpura), fever, altered mental status, headache, shock. Rash pathognomonic for meningococcemia; fulminant DIC common (purpura fulminans). Management: empiric ceftriaxone 2g IV q12h IMMEDIATELY (don't wait for LP, cultures); add vancomycin if meningitis suspected + immunocompromise. Blood cultures first, then antibiotics. ICD contact prophylaxis: rifampin, ciprofloxacin, or ceftriaxone for close contacts. Vaccination: meningococcal conjugate (MCV) routine; asplenic patients at extreme risk. Mortality 10-15% with antibiotics, >50% untreated. Survivors may have meningitis sequelae (hearing loss, neurologic deficit).",
            "tags": ["sepsis", "special_populations", "meningococcal", "fulminant"],
            "library": "intern_year_medicine"
        },

        # === ADDITIONAL CRITICAL TOPICS ===
        {
            "topic": "Surviving Sepsis Campaign Guidelines - 2021 Update",
            "subtopic": "sepsis_guidelines",
            "content": "Core SSC 2021 recommendations: (1) Early recognition (SIRS + infection); (2) First 3h bundle: lactate measurement, blood cultures, broad-spectrum antibiotics, IV fluid bolus 30mL/kg if hypotensive/lactate ≥4; (3) Vasopressors if MAP remains <65 after fluids (norepinephrine preferred); (4) Source control within 12h; (5) Reassess response (lactate clearance, vital signs, perfusion). Antithrombotics: avoid heparin prophylaxis in DIC; use mechanical prophylaxis for VTE. Steroids: consider low-dose hydrocortisone if refractory shock. Glucose control: target 140-180 (NOT intensive <100). Avoid overly restrictive fluids early; reassess for diuretics once stabilized. Regular audit/quality improvement essential; each hospital implement sepsis protocol to reduce mortality.",
            "tags": ["sepsis", "guidelines", "ssc", "best_practice"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Sepsis Screening & Hospital Implementation",
            "subtopic": "sepsis_quality",
            "content": "Quality improvement: (1) Educate providers on sepsis recognition (SIRS criteria, high-risk populations); (2) Implement sepsis alert system (EHR flags qSOFA ≥2 or criteria-based alerts); (3) Standardize order sets (blood cultures, lactate, antibiotics, fluids, vasopressors); (4) Audit compliance: % of septic patients receiving bundle measures within 3h; (5) Multidisciplinary team (ED, ICU, infectious disease); (6) Monthly data review + feedback. Track: time to antibiotics (median <1h target), mortality rates, 30-day readmission. Studies show dedicated sepsis protocols reduce mortality 5-10% in participating hospitals. Champions needed to drive adoption.",
            "tags": ["sepsis", "quality_improvement", "hospital_implementation"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Antimicrobial Stewardship in Sepsis",
            "subtopic": "antibiotics_stewardship",
            "content": "Stewardship principles: (1) Rapid culture-directed de-escalation (once organism + susceptibilities known); (2) Avoid prolonged broad-spectrum coverage unnecessarily; (3) Optimize dosing (renal/hepatic adjustment, therapeutic drug levels for vancomycin); (4) Limit duration (7-10 days standard for most bacterial sepsis, longer for specific infections); (5) Avoid antifungals unless high risk/documented fungal infection; (6) Stop prophylactic antibiotics appropriately (e.g., post-surgical wound prophylaxis stops within 24h). Resistance concerns: overuse of broad-spectrum agents + long treatment courses drives MRSA, resistant Gram-negatives, Candida. Sepsis ID consults help guide decision-making. Balance: aggressive empiric therapy early, then narrow/shorten as soon as feasible.",
            "tags": ["sepsis", "stewardship", "antibiotics", "de_escalation"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Repeat Blood Cultures in Sepsis Management",
            "subtopic": "monitoring_diagnostics",
            "content": "Initial blood cultures (2 sets before antibiotics) are critical. Repeat cultures indications: (1) persistent fever/sepsis despite appropriate antibiotics (48-72h) = possible source control failure or resistant organism; (2) line-related sepsis → draw from line + peripheral to confirm same organism; (3) endocarditis workup (3 sets over 24h); (4) fungemia (monitor clearance post-antifungal). Negative repeat cultures after antibiotics started = expected (cultures sterilize within 24-48h if appropriate therapy). Persistent positive cultures after 48h = source control needed or resistant organism → imaging (echo for vegetations, CT for abscess), consider switching antibiotics, urgent surgery consultation. Positive cultures from blood only (no source) = possible bacteremia from indwelling line or occult focus.",
            "tags": ["sepsis", "blood_culture", "repeat_cultures"],
            "library": "intern_year_medicine"
        }
    ]

    return units

def save_units(units, output_file):
    """Save units to JSON file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(units, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(units)} sepsis units to {output_file}")

if __name__ == "__main__":
    units = create_sepsis_units()
    save_units(units, "data/phase3_sepsis_chunks.json")
