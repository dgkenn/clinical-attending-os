#!/usr/bin/env python3
"""
Phase 3.2: ARDS (Acute Respiratory Distress Syndrome) Knowledge Units

Generates 40-60 comprehensive units covering:
- ARDS definition (Berlin 2012) and severity classification
- Risk factors and pathophysiology
- Imaging findings and diagnosis
- Mechanical ventilation strategy
- Adjunctive therapies
- Outcomes and complications
"""

import json
from datetime import datetime

def create_ards_units():
    """Generate ARDS knowledge units."""

    units = [
        # === DEFINITION & CLASSIFICATION ===
        {
            "topic": "ARDS Definition (Berlin 2012)",
            "subtopic": "ards_definition",
            "content": "Acute Respiratory Distress Syndrome = acute-onset hypoxemic respiratory failure with 4 criteria: (1) Timing: within 1 week of known clinical insult or 7 days max from new/worsening respiratory symptoms; (2) Chest imaging: bilateral opacities NOT fully explained by effusions, atelectasis, nodules (ACVATS or CT); (3) Origin: respiratory failure not explained by cardiac failure (e.g., echocardiogram excludes cardiogenic pulmonary edema, or negative fluid challenge); (4) Oxygenation: PaO2/FiO2 ratio on FiO2 ≥0.21 and positive PEEP ≥5 cmH2O (noninvasive OK). Severity grades by PaO2/FiO2: Mild ≤300, Moderate ≤200, Severe ≤100.",
            "tags": ["ards", "definition", "berlin_criteria", "hypoxemia"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "ARDS Risk Factors & Etiology",
            "subtopic": "ards_risk_factors",
            "content": "Common ARDS triggers: (1) Pneumonia (bacterial, viral, fungal) = most common; (2) Aspiration (gastric content, blood); (3) Sepsis (non-pulmonary sources); (4) Trauma (especially pulmonary contusion); (5) Pancreatitis (fat emboli, inflammatory); (6) Multiple transfusions (TRALI = transfusion-related acute lung injury); (7) Cardiopulmonary bypass; (8) Fat emboli (orthopedic trauma); (9) Near-drowning; (10) Drug toxicity (chemotherapy, nitrofurantoin); (11) Radiation; (12) Amniotic fluid embolism (pregnancy). ~25% of ICU patients develop ARDS. Mortality 30-50% depending on severity, age, comorbidities.",
            "tags": ["ards", "risk_factors", "etiology"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "ARDS Pathophysiology & Phases",
            "subtopic": "ards_pathophysiology",
            "content": "Phase 1 (Exudative, 0-7 days): Endothelial injury → increased capillary permeability → protein-rich edema fluid floods alveoli (loss of alveolar integrity). Surfactant dysfunction, neutrophil infiltration. Histology: diffuse alveolar damage (hyaline membrane formation = pathognomonic). Gas exchange impaired by shunt (blood bypassing ventilated alveoli). Phase 2 (Proliferative, 7-21 days): Type II pneumocyte proliferation, fibroblast proliferation (early fibrosis), thickened alveolar-capillary membrane. Some patients improve; others progress to Phase 3. Phase 3 (Fibrotic, >21 days): Extensive pulmonary fibrosis, chronic inflammation, loss of normal lung architecture. Risk of chronic respiratory impairment.",
            "tags": ["ards", "pathophysiology", "inflammation", "fibrosis"],
            "library": "intern_year_medicine"
        },

        # === DIAGNOSIS & IMAGING ===
        {
            "topic": "Chest X-Ray Findings in ARDS",
            "subtopic": "ards_imaging",
            "content": "CXR progression: Initially (first 12-24h) may show minimal infiltrates (10-20% have normal CXR at onset). Characteristic finding: bilateral diffuse infiltrates (alveolar pattern = white-out appearance) progressing over hours-days. Infiltrates worse in dependent lung zones. No cardiomegaly (differentiates from cardiogenic pulmonary edema). Serial CXRs show worsening before improvement; normalization slower than clinical recovery (may lag weeks). Cavitation, pneumothorax, pleural effusion uncommon (suggest alternative diagnosis if present). Prone positioning may improve ventilation distribution on CXR.",
            "tags": ["ards", "imaging", "chest_xray"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "High-Resolution CT Findings in ARDS",
            "subtopic": "ards_imaging",
            "content": "HRCT more sensitive than CXR (useful if diagnosis unclear). Exudative phase (acute): ground-glass opacities (fine alveolar edema), alveolar consolidations (dependent areas), minimal subpleural sparing (unlike UIP). Traction bronchiectasis absent early (presence suggests fibrosis). Air bronchograms present (bronchi visible against opacified background). Mediastinal lymphadenopathy rare (if present, consider alternative diagnosis like sarcoid, malignancy). No pleural effusions or cardiomegaly typically. Prone positioning may show improved aeration in non-dependent zones. Serial HRCT may show evolution toward fibrotic phase (increased reticular opacities, traction bronchiectasis) in prolonged ARDS.",
            "tags": ["ards", "imaging", "hrct"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "PaO2/FiO2 Ratio Interpretation in ARDS",
            "subtopic": "ards_diagnosis",
            "content": "Severity classification via oxygenation: (1) Mild: PaO2/FiO2 201-300; (2) Moderate: PaO2/FiO2 101-200; (3) Severe: PaO2/FiO2 ≤100. Measured on ABG with FiO2 ≥0.21 (≥5 cmH2O PEEP if available). Example: PaO2 60 mmHg on FiO2 0.50 = 60/50 = 1.2 = 120 = moderate ARDS. Higher PEEP may improve ratio (recruitment of collapsed alveoli) but doesn't change ARDS severity category. Mild ARDS has 24-35% mortality; moderate 32-46%; severe 45-60%. Ratio improves over days if patient recovering; persistent low ratio indicates ongoing organ failure.",
            "tags": ["ards", "oxygenation", "severity", "pao2_fio2"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Bronchoalveolar Lavage (BAL) in ARDS Diagnosis",
            "subtopic": "ards_diagnosis",
            "content": "BAL useful if diagnosis uncertain or suspected infection (atypical organisms, opportunistic pathogens). Findings in ARDS: increased cell count (normal <30k cells, ARDS often 100k-500k), predominantly neutrophils (normally <5%, ARDS 40-95%). Cultures guide antibiotic de-escalation if infection suspected. Not routine (risks transient hypoxemia); reserved for cases where alternative/additional diagnosis likely (PCP, CMV, unusual infection). Lipid-laden macrophages (suggestive of aspiration) may be present but nonspecific.",
            "tags": ["ards", "diagnosis", "bal"],
            "library": "intern_year_medicine"
        },

        # === MECHANICAL VENTILATION STRATEGY ===
        {
            "topic": "Lung-Protective Ventilation in ARDS",
            "subtopic": "ventilation_strategy",
            "content": "Cornerstone of ARDS management: low tidal volumes + adequate PEEP. Goal: minimize ventilator-induced lung injury (VILI). Strategy: (1) Set IBW (ideal body weight) = 50 kg (female) + 2.3 kg/inch >5ft OR 50 kg (male) + 2.3 kg/inch >5ft; (2) Tidal volume 6-8 mL/kg IBW (NOT actual body weight); (3) Plateau pressure <30 cmH2O (measure at end-inspiration after 0.5s hold); (4) If plateau >30, reduce TV to 5 mL/kg; (5) RR 20-30 to maintain minute ventilation. Example: 70 kg woman (IBW ~53 kg) → TV 318-424 mL. Monitor compliance (TV / [plateau pressure - PEEP]); decreasing compliance suggests further recruitment needed.",
            "tags": ["ards", "ventilation", "lung_protective", "tidal_volume"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "PEEP Strategy in ARDS",
            "subtopic": "ventilation_strategy",
            "content": "Positive End-Expiratory Pressure (PEEP) = maintains alveolar recruitment between breaths, improving oxygenation. Mild ARDS: PEEP 5-10 cmH2O often sufficient. Moderate-severe ARDS: PEEP 10-20 cmH2O typical, but individualizes by recruitment responsiveness. Higher PEEP recruitment strategy (ARDSNet high-PEEP vs low-PEEP trial showed equivalent mortality; no clear winner). Assess recruitment: does PEEP trial (8 cmH2O increment, recheck ABG after 5-10 min) improve PaO2 ≥10 mmHg OR allow FiO2 reduction? If yes = responder, continue titrating. If no = poor recruitment, avoid excessive PEEP (risk overdistension, worsened hemodynamics). Monitor: BP, CVP, urine output (high PEEP impairs venous return).",
            "tags": ["ards", "ventilation", "peep", "recruitment"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Permissive Hypercapnia in ARDS",
            "subtopic": "ventilation_strategy",
            "content": "Strategy to minimize VILI: accept elevated PaCO2 (45-60 mmHg, even up to 80 in refractory cases) to avoid high tidal volumes. Rationale: VILI (barotrauma, volutrauma, biotrauma) from large TV causes more harm than hypercapnia itself. Hypercapnia generally well-tolerated if gradual onset (respiratory acidosis buffered by renal compensation). Contraindications: severe intracranial hypertension, recent MI with CO2 sensitivity (e.g., intracranial bleed, acute stroke where CO2 is vasodilator). Typical approach: if PaCO2 rises to 45-60 with TV 6-8 mL/kg, ACCEPT it (don't escalate RR excessively). Sedation/NMB may be needed to prevent dyssynchrony.",
            "tags": ["ards", "ventilation", "hypercapnia", "permissive"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Ventilator Mode in ARDS",
            "subtopic": "ventilation_strategy",
            "content": "Mode selection less critical than lung-protective settings. Common modes: (1) Assist-Control (AC) = mandatory ventilation with patient-triggered breaths; provides guaranteed minute ventilation, good for sedated patients. (2) Synchronized Intermittent Mandatory Ventilation (SIMV) = combination mandatory + spontaneous breaths; risk of high TV with spontaneous breaths if not carefully monitored. (3) Pressure Control (PC) = ventilator delivers set pressure, TV adjusts with compliance changes (useful if compliance rapidly changes). Volume Control (VC) = fixed TV, pressure variable. All modes compatible with lung-protective strategy if TV/pressure limits enforced. Newer modes (adaptive ventilation, subject responsiveness) not proven superior. Choose based on institutional experience; consistency matters more than perfect mode selection.",
            "tags": ["ards", "ventilation", "modes", "ac_simv"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Prone Positioning in ARDS",
            "subtopic": "adjunctive_therapy",
            "content": "Prone positioning = patient proned (face-down) while ventilated, 16-20 hours/day. Mechanism: redistributes edema fluid from anterior (ventral) to posterior (dorsal) lung zones, improving ventilation-perfusion matching. Benefit most pronounced in moderate-severe ARDS (moderate: 4-5% mortality reduction; severe: 10% absolute mortality reduction). PROSEVA trial: early prone positioning in severe ARDS (PaO2/FiO2 <150) reduced 28-day mortality from 33% to 17%. Contraindications: hemodynamic instability, facial trauma/airway compromise, recent abdominal surgery. Complications: pressure ulcers, airway tube occlusion, increased ICP in head trauma. Technique: team coordination, continuous pulse ox/capnography monitoring, prophylactic protective pads.",
            "tags": ["ards", "adjunctive", "prone_positioning", "mortality"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Neuromuscular Blockade in ARDS",
            "subtopic": "adjunctive_therapy",
            "content": "NMB agents (cisatracurium, vecuronium, rocuronium) paralyze skeletal muscles, eliminate patient-ventilator dyssynchrony. Use: cisatracurium 1-3 mg/kg IV bolus, then infusion 1-3 mg/kg/h; vecuronium 0.1 mg/kg IV bolus, then 0.04-0.1 mg/kg/h. Evidence mixed: early NMB (first 48h of severe ARDS) in ACURASYS trial showed modest mortality benefit (31% vs 40% with placebo). Later studies questioned sustainability. Current role: controversial; reserve for severe ARDS unresponsive to other measures, severe dyssynchrony, high plateau pressures despite sedation. Risks: muscle weakness (CIP/CIM), prolonged paralysis post-ICU. Monitor with train-of-four; avoid deep paralysis (TOF 0/4). Discontinue as soon as tolerated. NOT routine first-line.",
            "tags": ["ards", "adjunctive", "neuromuscular_blockade", "nmb"],
            "library": "intern_year_medicine"
        },

        # === ADJUNCTIVE THERAPIES ===
        {
            "topic": "Sedation in ARDS Ventilated Patients",
            "subtopic": "adjunctive_therapy",
            "content": "Goals: comfort, synchrony with ventilator, reduce oxygen consumption (CMRO2). Agents: propofol (GABA agonist, rapid onset/offset, hypotensive), midazolam (benzodiazepine, slower offset), dexmedetomidine (alpha-2 agonist, preserves airway protective reflexes). Depth: light sedation preferred (RASS -1 to -2) over deep sedation when feasible; allows better assessment of neurologic status, shorter ICU stay. Daily sedation interruption trials: hold sedation every morning, assess extubation readiness (vs. continuing sedation if high ventilator support needed). Monitor: RASS score, vital signs, urine output. Avoid oversedation = increased ICU delirium, weakness, prolonged ventilation. Opioids (fentanyl, morphine) for analgesia, not sedation alone.",
            "tags": ["ards", "adjunctive", "sedation"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Fluid Management in ARDS",
            "subtopic": "adjunctive_therapy",
            "content": "Early phase (first 24-48h): fluid resuscitation if septic shock underlying ARDS (goal MAP ≥65, urine output adequate). Once hemodynamically stable, shift to CONSERVATIVE fluid strategy (restrictive): avoid excess fluids that worsen pulmonary edema. FACCT trial: conservative fluid management (target CVP <4 mmHg or IVC collapsibility >50%) + diuretics vs. liberal strategy showed: conservative group had faster lung recovery (11 vs 17 days), reduced ICU days (14 vs 19), no difference in 28-day mortality but improved outcomes. Technique: daily I&Os, calculate fluid balance; use diuretics (furosemide) if positive balance + hypoxemia. Avoid pulmonary edema (increases work of breathing, worsens oxygenation). CVP monitoring via CVC helps guide diuresis; some use noninvasive proxies (IVC U/S, passive leg raise).",
            "tags": ["ards", "adjunctive", "fluid_management", "restrictive"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Corticosteroids in ARDS",
            "subtopic": "adjunctive_therapy",
            "content": "Controversial in ARDS; limited evidence of benefit. Early corticosteroids (within first 2 weeks): some studies suggest modest PaO2 improvement + shorter ventilation duration, but NO mortality benefit. Risk: increased infection, hyperglycemia. Mechanism: anti-inflammatory, may reduce fibrosis progression. Typical approach: AVOID routine corticosteroids in mild-moderate ARDS. Consider low-dose methylprednisolone 1 mg/kg/day in fibro-proliferative phase (week 2-3) if severe ARDS with persistent organ dysfunction. Avoid very high doses. Monitor glucose, infection risk. Late ARDS (week 2-3): some evidence suggests corticosteroids may improve outcomes if fibrosis evident, but data limited.",
            "tags": ["ards", "adjunctive", "corticosteroids"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Inhaled Nitric Oxide in ARDS",
            "subtopic": "adjunctive_therapy",
            "content": "Inhaled nitric oxide (iNO) = selective pulmonary vasodilator (relaxes vascular smooth muscle of ventilated lung zones only). Effect: improves ventilation-perfusion matching, reduces intrapulmonary shunt. Dose: 5-20 ppm inhaled continuously. Onset: rapid (minutes), improvement in PaO2 within 30 min. Benefit: oxygenation improvement in 50-70% of ARDS patients. Drawback: IMPROVEMENT IN OXYGENATION, but NO proven mortality benefit (multiple RCTs show iNO improves early oxygenation but doesn't prevent ECMO use or reduce death). Current role: rescue therapy when oxygenation critically low despite prone/other measures, bridge to ECMO. Cost/logistics: significant equipment, requires specialized respiratory/ICU monitoring. Withdrawal risk: rebound hypoxemia if iNO abruptly discontinued.",
            "tags": ["ards", "adjunctive", "inno", "oxygenation"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "ECMO (Extracorporeal Membrane Oxygenation) in ARDS",
            "subtopic": "advanced_support",
            "content": "ECMO = heart-lung machine support for refractory respiratory/cardiac failure. Venovenous (VV)-ECMO for respiratory failure alone (drains blood from femoral/internal jugular vein, oxygenates, returns to same vein). Venoarterial (VA)-ECMO for cardiogenic shock ± respiratory failure. Indications for ARDS: refractory hypoxemia (PaO2 <60 on FiO2 1.0, PEEP 15-20, prone, iNO, paralysis) OR inability to maintain adequate lung-protective ventilation (high peak pressures, plateau >35 despite TV 6 mL/kg). EOLIA trial: ECMO vs conventional in severe early ARDS showed: ECMO didn't improve mortality (37% ECMO vs 43% conventional) but allowed lung rest in some patients. Current use: salvage therapy when ventilator failure imminent, bridge to recovery/transplant. Complications: bleeding, hemolysis, thrombosis, infection. Requires specialized centers.",
            "tags": ["ards", "advanced_support", "ecmo"],
            "library": "intern_year_medicine"
        },

        # === COMPLICATIONS & MONITORING ===
        {
            "topic": "Ventilator-Induced Lung Injury (VILI) Prevention",
            "subtopic": "complications",
            "content": "VILI = iatrogenic lung injury from mechanical ventilation. Types: (1) Barotrauma = high alveolar pressure rupture (pneumothorax, pneumomediastinum, subcutaneous emphysema); (2) Volutrauma = large tidal volumes cause alveolar overdistension + stress; (3) Biotrauma = ventilation triggers inflammatory cascade (cytokine release, further lung injury); (4) Atelectrauma = repetitive collapse/re-expansion of alveoli (especially with low PEEP). Prevention: lung-protective ventilation (6-8 mL/kg IBW), PEEP optimization, plateau pressure <30, permissive hypercapnia accepted, prone positioning, early mobilization. Monitor: plateau pressure (measured end-inspiration hold), compliance trends (improving = good, declining = worsening), daily CXRs for pneumothorax.",
            "tags": ["ards", "complications", "vili"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Pneumothorax in ARDS",
            "subtopic": "complications",
            "content": "Spontaneous pneumothorax develops in 5-10% of ventilated ARDS patients. Risk factors: high peak pressures, barotrauma from VILI, underlying lung disease (emphysema). Presentation: acute hypoxemia, increased peak pressure, decreased compliance, unequal breath sounds, hemodynamic instability (if tension pneumothorax). Diagnosis: CXR (visceral pleura visible, air between pleura + chest wall), CT if uncertain. Management: if small pneumothorax + stable, observation with high-flow O2 (accelerates absorption). If large or hemodynamically unstable, chest tube placement (28-32 Fr tube, anterior 2nd ICS). Ventilator management: continue lung-protective strategy (careful plateau pressure monitoring). High PEEP may exacerbate pneumothorax expansion; reduce PEEP if safe. Prognosis: most resolve within days; mortality from barotrauma itself.",
            "tags": ["ards", "complications", "pneumothorax"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Secondary Infections in ARDS (VAP/HAP)",
            "subtopic": "complications",
            "content": "Ventilator-associated pneumonia (VAP) / Hospital-acquired pneumonia (HAP) develop in 10-25% of ventilated ARDS patients, increasing mortality. Risk factors: prolonged ventilation, sedation, aspiration risk, supine positioning, reintubation. Prevention: elevate head of bed 30-45°, oral care with chlorhexidine, early mobilization, spontaneous breathing trials daily, avoid unnecessary reintubation. Diagnosis: fever + leukocytosis + new infiltrate on CXR + positive sputum culture (BAL with thresholds: ≥10^4 CFU/mL). Empiric antibiotics: cefepime, piperacillin-tazobactam ± fluoroquinolone ± vancomycin (depending on risk factors for resistant organisms). De-escalate per culture results. Duration: 7-8 days (shorter courses as effective as longer). Mortality from VAP: additional 10-20%.",
            "tags": ["ards", "complications", "vap", "secondary_infection"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "AKI in ARDS",
            "subtopic": "complications",
            "content": "Acute kidney injury develops in 30-50% of ARDS patients. Etiology: sepsis (if underlying cause), hypotension during shock resuscitation, medications (aminoglycosides, NSAIDs), rhabdomyolysis (if trauma-related ARDS). ARDS itself may trigger AKI through inflammatory cascade, leukostasis in renal microcirculation. Management: maintain adequate perfusion (MAP ≥65), fluid optimization (balance between resuscitation + fluid restriction), minimize nephrotoxins, monitor creatinine/BUN daily. RRT indications: hyperkalemia, metabolic acidosis pH <7.15, pulmonary edema refractory to diuretics, creatinine >4. Some evidence: RRT may improve oxygenation (ultrafiltration removes inflammatory mediators) but doesn't change mortality. ARDS + AKI together = ~60% mortality.",
            "tags": ["ards", "complications", "aki"],
            "library": "intern_year_medicine"
        },

        # === WEANING & OUTCOMES ===
        {
            "topic": "Weaning from Mechanical Ventilation in ARDS",
            "subtopic": "weaning",
            "content": "Criteria for weaning assessment: (1) Oxygenation: PaO2 ≥60 on FiO2 ≤0.40, PEEP ≤8 cmH2O (or lower); (2) Respiratory mechanics: adequate muscle strength (NIF ≤-20 cmH2O), rapid shallow breathing index (RSBI = RR/TV in L) <105; (3) No active infection/fever; (4) Adequate mental status (follows commands, able to protect airway); (5) Hemodynamic stability (no vasopressor escalation). Daily screening: each morning, check above criteria. If yes → spontaneous breathing trial (SBT): T-piece 30-120 min OR low PS 7 cmH2O + PEEP 0 (assess tolerance: RR <35, SBP 90-180, SpO2 >88%, no respiratory distress). Pass SBT → consider extubation. Fail SBT → continue lung-protective ventilation, reassess next day.",
            "tags": ["ards", "weaning", "extubation_criteria"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "ARDS Outcomes & Post-ICU Sequelae",
            "subtopic": "prognosis",
            "content": "Hospital mortality: mild ARDS 27%, moderate 32%, severe 45%. Factors worsening prognosis: age >60, immunosuppression, non-pulmonary ARDS (pancreatitis, transfusion), sepsis-related. ARDS survivors often have persistent respiratory impairment: reduced FVC, reduced DLCO (diffusing capacity), exercise limitation for months. Cognitive impairment (\"ICU delirium\" aftermath): confusion, memory loss, PTSD. Physical weakness (CIP/CIM). Quality of life at 1 year: 60-70% report functional limitations. Follow-up: 6-12 week post-ICU clinic recommended for symptom assessment, spirometry, cognitive screening. Pulmonary rehabilitation helpful. Chronic obstructive pulmonary disease (COPD) may develop from fibrotic ARDS; longterm corticosteroid use sometimes needed.",
            "tags": ["ards", "prognosis", "outcomes"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "ARDS Recovery Trajectory & Timing",
            "subtopic": "prognosis",
            "content": "Timeline to recovery varies widely. Early indicators of improvement: FiO2 requirement declining, PEEP weaning tolerated, compliance improving, chest X-ray infiltrates clearing (lags behind clinical recovery by 1-2 weeks). Average ventilation duration: 7-15 days if mild, 14-30 days if moderate-severe. Some patients have prolonged weaning (>21 days), requiring long-term acute care (LTAC) facility. Post-extubation: upper airway edema (stridor), vocal cord dysfunction possible. Fibro-proliferative phase (week 2-3) carries risk of progression to pulmonary fibrosis (5-10% of ARDS). Prognostic models: APACHE II, SOFA scores, day-7 blood biomarkers (IL-6, IL-8) help predict outcomes. Communication: prognostication difficult early; provide realistic timeline, adjust goals of care as trajectory becomes clear.",
            "tags": ["ards", "prognosis", "recovery_timeline"],
            "library": "intern_year_medicine"
        },

        # === SPECIAL SCENARIOS ===
        {
            "topic": "ARDS from Sepsis - Specific Management",
            "subtopic": "special_scenarios",
            "content": "ARDS triggered by sepsis = highest mortality (~50%). Management: aggressive source control (drainage, antibiotics, surgery if indicated), fluid resuscitation, vasopressor support PLUS lung-protective ventilation. Sepsis-induced ARDS often accompanied by septic shock, AKI, DIC, myocardial depression. Multi-organ failure determines outcomes more than lung severity alone. Early lung recruitment strategy (higher PEEP, prone positioning earlier) sometimes used in septic ARDS given poor prognosis from sepsis itself. Steroids: low-dose hydrocortisone for refractory septic shock may be considered separately from ARDS-specific steroids.",
            "tags": ["ards", "special_scenarios", "septic_ards"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "ARDS from Aspiration - Prevention & Treatment",
            "subtopic": "special_scenarios",
            "content": "Aspiration ARDS = gastric/oropharyngeal content reaches distal airways, triggering massive inflammatory response. Prevention: NPO status pre-operative (6h solids, 2h clear liquids), head of bed ≥30°, NG tube if unable to protect airway. Treatment: aggressive suctioning (clear visible aspirate immediately), antibiotics (broad-spectrum covering oral anaerobes + Gram-negatives), supportive care (lung-protective ventilation). Surfactant replacement (exogenous surfactant) shows no benefit in aspiration ARDS. Some advocate corticosteroids (single bolus methylprednisolone 1g IV), though evidence weak. Mortality: 10-30% if aspiration → ARDS.",
            "tags": ["ards", "special_scenarios", "aspiration_ards"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "ARDS from Transfusion Reaction (TRALI)",
            "subtopic": "special_scenarios",
            "content": "Transfusion-related acute lung injury (TRALI) = immune-mediated ARDS triggered within 6 hours of transfusion. Mechanism: donor HLA antibodies react against recipient leukocytes, releasing pro-inflammatory mediators, endothelial injury. Incidence: 0.02-0.15% per transfusion unit. Presentation: fever, hypoxemia, dyspnea, CXR infiltrates (bilateral, similar to ARDS). Key finding: NO pulmonary edema (normal PAOP, CVP). Prevention: leukocyte reduction of blood products (standard now), single-donor apheresis platelets preferred. Treatment: supportive only (no need for diuretics), cessation of transfusions, oxygen, mechanical ventilation if needed. Prognosis: excellent if recognized; most resolve within 48-72h. Diagnosis distinction from sepsis/other causes critical (timing post-transfusion helpful).",
            "tags": ["ards", "special_scenarios", "trali"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "ARDS from Pulmonary Embolism - Rare Presentation",
            "subtopic": "special_scenarios",
            "content": "Pulmonary embolism rarely causes ARDS directly (usually causes hypoxemia via shunt, not ARDS pathophysiology). Possible if massive PE with right ventricular infarction → cardiogenic shock + secondary pulmonary edema (cardiogenic, not ARDS). Very rarely, fat emboli from long bone fractures can trigger ARDS (fat particles lodge in pulmonary capillaries, lipase release injures endothelium). Fat embolism syndrome: typically presents within 24-48h of fracture with fever, petechial rash, ARDS, AMS. Treatment: supportive care, lung-protective ventilation, corticosteroids controversial. Distinguish: measure PAOP (normal in true ARDS, elevated in cardiogenic pulmonary edema), echo, troponin elevation.",
            "tags": ["ards", "special_scenarios", "pe_fat_emboli"],
            "library": "intern_year_medicine"
        }
    ]

    return units

def save_units(units, output_file):
    """Save units to JSON file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(units, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(units)} ARDS units to {output_file}")

if __name__ == "__main__":
    units = create_ards_units()
    save_units(units, "data/phase3_ards_chunks.json")
