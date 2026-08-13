#!/usr/bin/env python3
"""
FINAL Phase 4 Generation: Comprehensive 750+ units

Creates massive expansion covering:
- All toxicology scenarios (100+ units)
- All trauma management (120+ units)
- All procedures (100+ units)
- All OB/GYN (80+ units)
- All pediatrics (100+ units)
- All geriatrics (80+ units)
- All communication (60+ units)
- All QI/safety (70+ units)
- All palliative (60+ units)
- All administrative (30+ units)

TOTAL: ~790 units
"""

import json
from pathlib import Path
from datetime import datetime

def generate_phase4_final():
    """Generate comprehensive final Phase 4 data."""

    # Load existing
    comp_path = Path("data") / "phase4_comprehensive.json"
    with comp_path.open("r", encoding="utf-8") as f:
        units = json.load(f)

    unit_id_counter = len(units) + 1000

    # MASSIVE EXPANSION DATA
    additional_units_text = """
# TOXICOLOGY DEEP DIVE (targeting 100+ total)
Tricyclic antidepressant poisoning: amitriptyline, nortriptyline, imipramine. Anticholinergic effects (dry mouth, urinary retention, hyperthermia), CNS depression, cardiac arrhythmias (QRS widening, torsades). Treatment: sodium bicarbonate 1-2 mEq/kg IV to alkalinize plasma (target pH 7.45-7.55); increases protein binding; slows metabolism. Intubation if altered mental status. Monitor cardiac rhythm continuously. Mortality 5-15% if severe ingestion.

Phenothiazine antipsychotic overdose: chlorpromazine, perphenazine. Anticholinergic + dopamine blockade → CNS depression, hypotension, QT prolongation, dystonia, neuroleptic malignant syndrome. Minimal antidote (supportive care); avoid gastric lavage (aspiration risk); activated charcoal. Benzodiazepines for seizures/dystonia.

Stimulant overdose comparison: cocaine = sympathomimetic + local anesthetic (sodium channel blockade, arrhythmias); amphetamine = longer acting, more CNS than cardiac. Both: hypertension, tachycardia, hyperthermia, myocardial ischemia, stroke, seizures. Cocaine MI risk via coronary vasospasm. Treatment: benzodiazepines, phentolamine for hypertension, cooling.

Beta-blocker overdose: bradycardia, hypotension, altered mental status, seizures, hypoglycemia, bronchospasm. Glucagon 3-10 mg IV bolus (bypasses beta receptor), repeated q5-10min; atropine for bradycardia (limited efficacy). IV calcium gluconate, insulin with dextrose, lipid emulsion (propranolol).

Calcium channel blocker overdose: diltiazem, verapamil. Severe bradycardia, hypotension, AV block, cardiogenic shock. High-dose insulin with dextrose (HIET: High-dose Insulin Euglycemia Therapy); 1 unit/kg IV, then 0.5-1 unit/kg/min infusion. Atropine, pacing, vasopressors. Calcium salt (calcium gluconate or chloride) less effective than insulin.

Digoxin toxicity: narrow therapeutic window (0.5-2 ng/mL). Toxicity at any level if hypokalemia. Early: nausea, vomiting, anorexia. Arrhythmias: bradycardia, bigeminy, ventricular tachycardia, AV block. Hyperkalemia prognostic sign (severe toxicity). Treatment: potassium repletion if hypokalemia, antiarrhythmics (procainamide), digoxin-specific Fab antibody (DigiFab) for severe toxicity.

Theophylline toxicity: caffeine-like bronchodilator. Toxicity: nausea, vomiting, tachycardia, hypertension, seizures, arrhythmias. Mechanism: phosphodiesterase inhibition, adenosine antagonism. Treatment: activated charcoal (multiple doses, enterohepatic recirculation); phenobarbital for seizures; propranolol for arrhythmias. Charcoal hemoperfusion rarely used.

Anticancer drug toxicity: cisplatin (nephrotoxicity, ototoxicity, neuropathy), doxorubicin (cardiomyopathy), methotrexate (hepatotoxicity, neurotoxicity, nephrotoxicity). Management: hydration, ototoxicity screening, cardiology follow-up, folinic acid (leucovorin) for high-dose methotrexate rescue.

Envenomation (snake bite): hemotoxic (tissue destruction), neurotoxic (paralysis), coagulopathy. North American: rattlesnakes (hemotoxic), coral snakes (neurotoxic). Treatment: antivenom (species-specific), supportive care, monitor coagulation studies. No suction/ice/tourniquets; immobilize, elevate to heart level.

Envenomation (spider bite): brown recluse (necrotic), black widow (neurotoxic). Brown recluse: loxoscelism (hemolysis, necrotic skin ulcer). Black widow: latrodectism (severe muscle pain, autonomic dysfunction). Treatment: antivenin (rare, only for severe), supportive care, benzodiazepines, analgesics.

Plant toxins (mushrooms): amatoxin (Amanita phalloides death cap) → hepatorenal failure. Presentation: triphasic (asymptomatic, GI phase, apparent recovery, hepatic failure). No specific antidote; aggressive supportive care, consider high-dose penicillin. Mortality 50% if untreated.

Herbal medicine toxicity: kava (hepatotoxicity), ma huang (ephedrine toxicity), licorice (hypokalemia, hypertension). Difficult to detect (not listed as ingredient); ask specifically about herbal use.

Illicit drug contamination: fentanyl + heroin, xylazine (tranquilizer + opioid = deadly combination), levamisole (immunosuppression). Naloxone may not reverse xylazine (sympathomimetics used). Updated polysubstance toxidrome thinking.

Pesticide herbicide toxicity: paraquat (lung toxicity, fibrosis), glyphosate (gastrointestinal injury). No specific antidotes; supportive care, oxygen avoidance in paraquat (paradoxically worsens pulmonary fibrosis).

Household chemical poisoning: drain cleaners (caustic, esophageal burns), corrosive acids/bases (ingestion → perforation). Treatment: dilution (water/milk, avoid neutralization heat), NPO, avoid gastric decontamination (risk of aspiration/perforation), monitor for perforation.

Drug interaction lethality: MAOI + serotonergic agents (serotonin syndrome), MAOI + tyramine (hypertensive crisis), QT-prolonging drugs (torsades), warfarin + NSAIDs (bleeding).

# TRAUMA DEEP DIVE (targeting 120+ total)
Penetrating neck trauma: risk airway/vascular injury. Surgical airway vs. percutaneous intubation (traumatic induction risks; ketamine often preferred). CTA angiography preferred over traditional angiography. Zones: Zone I (base of neck → clavicle), Zone II (clavicle to angle of mandible), Zone III (angle of mandible to skull base). Different operative thresholds by zone.

Penetrating chest wall (thoracic): assess for hemopneumothorax, cardiac/great vessel injury, esophageal injury. FAST exam critical (pericardial fluid = tamponade). Small pneumothorax may be observed; larger (>2 cm at hilum) or hemothorax → tube thoracostomy. Persistent air leak suggests bronchial injury (rare, needs OR).

Resuscitative thoracotomy indications: penetrating trauma with witnessed/near-witnessed arrest, signs of life on-scene (pupils reactive, gasping, spontaneous movement). Blunt trauma arrest: CPR alone may be equivalent (most have non-salvageable injuries).

Blunt myocardial injury (cardiac contusion): troponin elevation, arrhythmias, reduced EF on echo. Prognosis: most recover fully; monitoring in ICU, serial troponins. If hemodynamically unstable, echo to assess wall motion abnormalities.

Abdominal solid organ injuries (liver, spleen, kidney): Non-operative management (NOM) if hemodynamically stable (SBP >90, no peritonitis). ICU monitoring, serial exams, CT imaging. Indications for OR: hemodynamic deterioration, peritonitis, other injuries requiring OR. Most resolve with NOM (80-90% success).

Retroperitoneal hemorrhage (pelvic, aortic region): high mortality if massive. Pelvic binder reduces bleeding. Aortic injuries often fatal pre-hospital; survivors need ASAP angiography or OR. Aortic injury high suspicion if widened mediastinum on CXR, severe deceleration mechanism, thoracic spine fracture.

Brachial plexus injury (birth trauma, traction injury): assess nerve function immediately. Upper trunk (Erb) → arm adduction weakness; lower trunk (Klumpke) → claw hand. Recovery in weeks-months if traction injury; if root avulsion, permanent. Referral to neurosurgery if no improvement by 3 months.

Compartment syndrome: "pain out of proportion" is key sign; pain with passive stretch. Compartments: anterior, lateral, posterior (leg); dorsal, palmar (hand). Measurement: intracompartmental pressure >20-30 mmHg relative to diastolic BP indicates emergency fasciotomy. Reperfusion rhabdomyolysis, hyperkalemia risk after fasciotomy.

Crush syndrome timing: "Golden period" <6 hours for limb salvage; >12 hours amputation often necessary. Rhabdomyolysis management: aggressive IV hydration, urine alkalinization, monitor for hyperkalemia.

Burn severity assessment: rule of nines (head 9%, arms 18%, trunk 36%, legs 36%), depth (1st degree erythema, 2nd partial thickness blistering, 3rd full thickness charred, 4th subcutaneous), %TBSA = indicator for inhalation injury risk and fluid resuscitation need.

Fluid resuscitation in burn: Parkland formula = 4 mL × TBSA% × kg body weight over 24h; give half in first 8h. Goal: urine output 0.5 mL/kg/h (darker urine indicates myoglobinuria → increase fluids). Rhabdomyolysis risk; hyperkalemia, AKI monitoring.

Inhalation injury (smoke inhalation): thermal (above vocal cords rare), chemical (CO, hydrogen cyanide, acrylonitrile). Carboxyhemoglobin/cyanide levels, ABG, lactate elevation. Treatment: 100% O2, intubation if stridor/carbonaceous sputum, cyanide antidotes if cyanide toxicity suspected.

Acute coronary occlusion post-trauma: stress-induced takotsubo cardiomyopathy (reversible), coronary artery dissection (spontaneous), or true ACS (in pre-existing disease). Troponin elevation, ECG changes. Angiography if unstable or high suspicion.

Torso hemorrhage imaging: CT trauma pan-scan increasingly used (head, C-spine, chest, abdomen/pelvis). Trade-off: rapid diagnosis vs. radiation exposure, iodine contrast (renal function). Hemodynamically unstable: selective imaging (FAST + CT chest/abdomen if time allows) vs. straight to OR.

Resuscitative laparotomy findings: assess all quadrants, prioritize bleeding control over repair. Hepatic hemorrhage: packing often preferred (leave packs in place, remove in 24-72h OR); whipple rarely done acutely. Pancreatic injury: usually conservatively managed unless ductal injury proven.

Injury severity score (ISS): aggregate of 3 highest AIS (Abbreviated Injury Scale) scores from different body regions; score >15 = major trauma. Predictive of mortality, ICU admission. Used for research/benchmarking.

Massive transfusion complications: DIC (activated clotting → thrombosis, bleeding), citrate toxicity (preservative in RBC → hypocalcemia), hypothermia (cold fluids), acidosis, hyperkalemia (RBC breakdown), ARDS (transfusion-related acute lung injury, TRALI).

Vascular injury management: temporary shunts in prehospital/ED (aortic, iliac, femoral) to restore distal perfusion while moving to OR. Interposition grafts, primary repair depending on vessel type/injury.

Traumatic amputation: replantation possible if <8h warm ischemia (<24h cold ischemia with icing). Transfer to specialized center ASAP. Preserve distal part (ice in saline-soaked gauze, dry dressing, NOT dry ice). Prognosis: thumb/hand replantation better outcomes than proximal limb.

Tetanus risk in trauma: clean wound + tetanus up-to-date = no vaccine; >10y since vaccine = booster. Dirty wound + unknown vaccination = tetanus Ig + vaccine. Prophylactic antibiotics (cephalosporin, not penicillin if allergy).

# PROCEDURES DETAILED (targeting 100+ total)
Ultrasound-guided central line: safer than landmark; identifies vessel, depth, guidewire trajectory. Static vs. dynamic visualization. Risk: vessel puncture, hemothorax (subclavian), IJ best for landmark blind but ultrasound reduces risk further.

Arterial line complications: distal ischemia (Doppler to confirm patency), pseudoaneurysm (ultrasound diagnosis, thrombin injection therapy), infection (daily assessment, remove if signs), thrombosis (heparin-bonded catheters reduce risk).

Chest tube troubleshooting: tube not functioning (malposition, clot obstruction). Signs: no swinging (fluid level doesn't change with respiration), no bubbling (no air leak). Milk tubes (gently milk blood clots through tubing), elevate drainage chamber. If persistent, imaging to confirm position, consider repositioning or new tube.

Pleural effusion drainage: ultrasound-guided thoracentesis safer. Contraindications: coagulopathy, thrombocytopenia <20k, single kidney. Complications: pneumothorax, hemothorax, infection. Analysis: cell count, protein, LDH, glucose, culture, cytology depending on suspected pathology.

Transvenous pacing: used for symptomatic bradycardia refractory to atropine. Insertion: place central line, advance pacing catheter through central vein into RV. Confirmation: capture (paced QRS), sensing (pacemaker recognizes intrinsic rhythm). Complications: perforation, arrhythmia provocation, loss of capture.

Hemodialysis access (emergent): femoral vein catheter (risk DVT, infection), less ideal long-term. Permanent: AV fistula (radiocephalic preferred) or graft. Complications: thrombosis, infection, steal syndrome (distal hand ischemia), aneurysm (fistula).

Bedside laparotomy (exploratory): rapid assessment in unstable patient; can close if minor finding, leave open if major hemorrhage (packing, temporary closure). ICU monitoring, re-explore in 24-48h.

Peritoneal lavage (diagnostic): less common now (replaced by CT/FAST), used for abdominal trauma if CT unavailable. Infuse 1L warm saline, drain gravity, analyze for RBC/WBC/bacteria count.

Bedside ultrasound: POCUS (point-of-care ultrasound). Indications: cardiac (ejection fraction, pericardial fluid), lung (B-lines indicating pulmonary edema, pneumothorax), abdominal (FAST, AAA, IVC diameter), DVT/thrombosis. Training: certification programs, credentialing required.

Transesophageal echocardiography (TEE): superior for endocarditis vegetations, cardiac source of embolism, aortic dissection. Probe advancement requires skill; risks esophageal perforation. Operator-dependent.

Bronchoscopy indications: hemoptysis (localize, can treat with epinephrine/thrombin), aspiration (remove foreign body), difficult intubation (assess anatomy), cough workup, BAL (bronchoalveolar lavage for infection workup), biopsy.

Rigid vs. flexible bronchoscopy: flexible (most common, smaller, can navigate distally), rigid (wider channel for therapeutic intervention, maintains airway, used for foreign body removal in children).

Endotracheal tube complications: sinusitis (frequent), subglottic stenosis (delayed, from high cuff pressures), tracheal stenosis (late complication), ventilator-associated pneumonia, tube malposition (right mainstem intubation, esophageal).

Tracheostomy complications: early (bleeding, infection, tube obstruction), late (tracheal stenosis, subglottic stenosis, tracheal-innominate fistula). Decannulation: capping trial then remove tube, monitor for aspiration.

Temporary abdominal closure (VAC): vacuum-assisted closure after damage control laparotomy or massive abdominal wound. Dressing changes q2-3d, allows gradual fascial closure without tension.

Incision and drainage (abscess): localize with ultrasound/CT, aspirate for culture (before antibiotics if possible), pack with gauze or place drain. Follow-up imaging to confirm resolution.

Balloon catheter for hemorrhage control: gastric (Sengstaken-Blakemore) for variceal bleeding (temporary bridge to endoscopy), urinary (Foley) for bladder tamponade, aortic (REBOA) for massive hemorrhage.

Resuscitative liquid ventilation: experimental (perfluorodecalin), allows gas exchange without air. Used for ARDS with severe refractory hypoxemia; improves lung compliance, reduces barotrauma. Limited availability.

# OB/GYN EMERGENCIES EXPANDED (targeting 80+ total)
Shoulder dystocia: fetal shoulder lodged behind maternal pubic symphysis after fetal head delivery. Maneuvers: McRoberts (hip hyperflexion), suprapubic pressure, posterior arm extraction, Zavanelli (replace head, emergent cesarean). Complication: brachial plexus injury (Erb/Klumpke).

Uterine rupture: catastrophic obstetric emergency. Signs: vaginal bleeding, severe abdominal pain, shock, fetal distress. Risk: prior uterine surgery (cesarean, curettage), high-dose oxytocin. Management: immediate cesarean hysterectomy (preserves fertility goal competed with survival), massive transfusion protocol.

Placental abruption: premature separation of placenta. Signs: dark vaginal bleeding, abdominal pain, uterine tenderness, DIC. Risk: hypertension, trauma, cocaine use. Management: deliver fetus ASAP (vaginal if stable, cesarean if unstable/fetal distress); transfusion, DIC management.

Cervical laceration: occurs with instrumentation/rapid delivery. Heavy bleeding if cervical artery involved. Management: visualize with speculum, suture with absorbable suture (usually 2-0 chromic), avoid kinking vaginal vessels.

Maternal stroke (peripartum): hypercoagulable state, arterial dissection risk, peripartum cardiomyopathy. Imaging: CT or MRI (avoid gadolinium in 3rd trimester if possible). Thrombolytics (tPA) debated (bleeding risk), thrombectomy if large vessel occlusion.

Maternal pulmonary embolism: leading cause of non-obstetric maternal death. VTE risk increases 5-10× in pregnancy. Presentation: dyspnea, chest pain, hemoptysis. Diagnosis: PE protocol CT pulmonary angiography (radiation <50 mRad, fetal risk minimal). Treatment: anticoagulation (unfractionated heparin preferred, switch post-delivery).

Obstetric fistula: traumatic (prolonged labor, instrumental delivery), iatrogenic (surgical). Vesicovaginal (bladder → vagina) most common; ureterovaginal, rectovaginal less common. Symptoms: continuous leakage, odor, infection. Repair: surgical, 3-4 months post-injury (allow inflammation to resolve).

Retained products of conception: post-abortion/delivery, incomplete evacuation. Symptoms: vaginal bleeding, cramping, fever if infected. Imaging: ultrasound (intrauterine tissue), uterus measurements asymmetric. Management: D&C (curettage), IV antibiotics if infected, RhIG if Rh-negative.

Inversion of uterus: rare (1 in 2,000-5,000 deliveries), usually from excessive cord traction or fundal pressure. Acute: inverted uterus visible at vaginal introitus, hemorrhage, shock. Management: immediate replacement (ease back in, hydrodissection technique), anesthesia, oxytocin post-reduction. Chronic inversion: hysterectomy.

Uterine atony recurrent: first-line management inadequate (massage, oxytocin, ergotamine, misoprostol all failed). Consider uterine balloon tamponade (Bakri balloon, intrauterine Foley catheter) or uterine artery embolization. Last resort: hysterectomy (preserves other organs unlike hysterectomy).

Thromboembolic disease in pregnancy: DVT risk 5-10×, PE 5×. Hypercoagulability + venous stasis (gravid uterus compresses IVC). Anticoagulation: unfractionated heparin (UFH) or low-molecular-weight heparin (LMWH) preferred (warfarin teratogenic). Prophylaxis if high-risk (prior VTE, thrombophilia, immobility).

Pregnancy-associated thrombotic microangiopathy (TMA): HUS (hemolytic uremic syndrome), thrombotic thrombocytopenic purpura (TTP). Present with hemolysis, thrombocytopenia, renal dysfunction. Plasmapheresis first-line.

Maternal cardiac arrhythmia: palpitations common in pregnancy (normal adaptation), but sustained/symptomatic arrhythmia needs treatment. SVT: adenosine safe (minimal fetal exposure). AFib: rate control (beta-blockers, diltiazem). VT rare but life-threatening; defibrillation safe, ICD placement if structural disease.

Septic shock in pregnancy: more aggressive, higher mortality. Common sources: chorioamnionitis (intrauterine infection), UTI (pyelonephritis), pneumonia. Aggressive fluid resuscitation, broad-spectrum antibiotics, delivery (removes infected tissue source).

Gestational hypertension evolution: gestational HTN → preeclampsia → eclampsia → HELLP. Without preeclampsia; 5-10% develop it by delivery. Monitor BP, symptoms, labs q2-3d.

Postpartum hypertension: resolves in most within weeks, but some develop eclampsia postpartum. Can be severe (>180/120); treat aggressively. Labetalol, nifedipine, hydralazine (avoid ACE-I/ARBs immediately postpartum while breastfeeding established).

Postpartum infection (endometritis, surgical site infection): fever + lower abdominal pain ± purulent lochia (endometritis). Culture amniotic fluid/lochia. Antibiotics: cefotetan + doxycycline (or cefoxitin + doxycycline). Complications: sepsis, bacteremia, abscess formation.

Postpartum venous thromboembolism: risk peaks 1-3 weeks post-delivery. Immobility (bedrest post-cesarean), vessel injury, tissue factor release from placenta. Anticoagulation: UFH or LMWH; warfarin acceptable if breastfeeding (minimal transfer). Prophylaxis if extended immobility post-cesarean.

Breastfeeding complications: mastitis (infection of breast tissue, fever + localized erythema, antibiotics + continue breastfeeding), abscess (fluctuant mass, drain or needle aspiration + antibiotics), plugged duct (localized tenderness, express more), engorgement (manage with cold/compression/analgesia).

# PEDIATRIC CRITICAL CARE EXPANDED (targeting 100+ total)
Pediatric airway anatomy: large occiput (neck flexion → airway obstruction), relatively large tongue, anterior larynx, funnel-shaped subglottis (narrowest at cricoid, not glottis). Implications: straight blade preferred for visualization, shorter neck extension needed, smaller tube sizes.

Pediatric intubation step-by-step: preoxygenation, induction (propofol/etomidate in septic), succinylcholine (1-1.5 mg/kg) or rocuronium (1.2 mg/kg), intubate with straight blade or video laryngoscope. Tube size = (age+16)/4 or visual estimate. Length = 3×tube diameter from teeth. Confirm with capnography + CXR.

Pediatric sepsis bundle: source identification, blood cultures, broad-spectrum antibiotics <1h, fluid resuscitation 20 mL/kg, vasopressor if shocked after fluids, corticosteroid if catecholamine refractory (controversial but may help).

Pediatric shock compensation: younger children compensate longer (normal BP maintained despite shock) → rely on perfusion signs (mental status, urine output, skin perfusion, lactate) not just BP.

Pediatric ARDS management: lung-protective ventilation (TV 6-8 mL/kg IBW), permissive hypercapnia (target pH >7.20), PEEP titration, prone positioning (moderate-severe), neuromuscular blockade if needed, fluid conservative strategy.

Pediatric sedation scales: RASS (Richmond Agitation-Sedation Scale) adapted for pediatrics, or SedaScore. Goal: light sedation (arousable to voice) unless paralyzed. Avoid deep sedation (delirium risk, prolonged recovery).

Pediatric norepinephrine dosing: 0.05-0.5 mcg/kg/min IV; requires central line (peripheral extravasation → necrosis). First-line for septic shock after fluid resuscitation.

Pediatric epinephrine dosing: 0.1-0.3 mcg/kg/min for inotropic support, 0.1 mg/kg IV q3-5min for cardiac arrest. Dosing weight-based; no max dose like adults.

Pediatric medication errors: common due to weight-based dosing, decimal point errors, mg vs. mL confusion, concentration variations. Safeguards: double-check weight, use weight-based calculators, avoid abbreviations.

Pediatric fever management: fever is symptom, not disease. Aggressive treatment (cooling, antipyretics) no evidence of benefit; may harm. Treat underlying infection. Acetaminophen/ibuprofen if uncomfortable.

Pediatric abdominal trauma: solid organs (liver, spleen, kidney) managed non-operatively in hemodynamically stable patients; success rates high (90%+). Monitor closely, serial exams, repeat imaging if clinical change.

Pediatric head injury: lower mortality with aggressive ICP management; TBI most common cause of pediatric death. CPP maintenance (age-adjusted normal BP), osmotic therapy, sedation/analgesia, avoid hyperthermia/hypoxemia, seizure prophylaxis.

Pediatric status epilepticus: first-line benzodiazepine (lorazepam 0.1 mg/kg IV); second-line fosphenytoin/levetiracetam/valproate; third-line induction anesthesia (propofol/pentobarbital). Causes: fever (febrile seizure), infection, metabolic, toxin, idiopathic.

Pediatric hyperglycemia: stress-induced (trauma, infection, critical illness) vs. type 1 DM DKA. Goal glucose 100-180 mg/dL (tight control increases hypoglycemia risk in peds). Insulin drip if sustained elevation; monitor glucose q1-2h.

Pediatric renal replacement therapy: CRRT (continuous renal replacement therapy) preferred over intermittent hemodialysis in unstable patients; smaller circuit, less hypotension, better clearance in acidosis. Indications: K >6.5, severe acidosis, refractory fluid overload, AKI with rising creatinine.

Pediatric coagulopathy: lower factor levels than adults (approach adult levels by age 6-12mo). FFP 10 mL/kg, cryoprecipitate 1 unit/2kg, platelets 10 mL/kg (1 unit per 5 kg). Prothrombin complex concentrate not established in peds (limited data).

Pediatric DIC management: treat underlying cause, transfuse based on labs (platelets if <20k, FFP if coagulopathy, cryoprecipitate if fibrinogen <100), monitor platelet/fibrinogen closely. Avoid heparin.

Pediatric pain assessment: FLACC <3 years, faces scale 3-8 years, numeric scale >8 years. Undertreated pain common; ensure adequate analgesia. Withdrawal syndrome if opioid cessation (taper slowly).

Pediatric nutrition: higher metabolic demands than adults. Enteral preferred over parenteral (GI translocation risk lower). Protein 1.5-2 g/kg (higher than adults). Early feeding within 24-48h if tolerated.

Pediatric delirium: CAM-ICU adapted for peds (pCAM-ICU), less common than adults but serious (increased mortality). Causes: infection, hypoxemia, medication, sleep disruption. Prevention: early mobilization, family presence, orientation.

# GERIATRIC MEDICINE EXPANDED (targeting 80+ total)
Acute delirium in elderly: sudden onset (key distinguishing feature from dementia), fluctuating course, inattention. Common triggers: infection, medications, metabolic abnormalities, hypoxemia. Delirium subtypes: hyperactive (agitated, obvious), hypoactive (lethargic, often missed), mixed.

Prevention of hospital-acquired delirium: multicomponent intervention (early mobilization, sleep hygiene, reorientation, sensory aids, minimize sedating drugs) reduces incidence 33-65%. Earlier discharge, reduced complications, lower mortality.

Delirium medication management: avoid benzodiazepines (worsen cognition), anticholinergics, opioids (minimize). Haloperidol (off-label, not FDA approved) sometimes used but no mortality benefit, possible harm. Supportive care + treat cause is foundation.

Cardiovascular changes in aging: reduced beta-adrenergic responsiveness, increased diastolic dysfunction, increased arrhythmia risk. Medications need adjustment: beta-blockers less effective for rate control, ACE-I/ARBs improve diastolic function.

Renal function in elderly: GFR declines ~0.8 mL/min/year; creatinine may be normal (less muscle mass). Cockcroft-Gault more accurate than eGFR for medication dosing. Hyperkalemia risk increases with ACE-I/ARB use + renal disease + NSAIDs.

Medication metabolism in elderly: reduced hepatic metabolism (reduced cytochrome P450 activity), reduced renal clearance, increased volume of distribution for lipophilic drugs. Result: longer half-lives, increased toxicity risk. Dosing: start low, go slow.

Adrenal insufficiency in elderly: may present subtly (fatigue, hyponatremia, hypotension). Causes: long-term corticosteroid use (most common), adrenal metastases, pituitary adenoma. Diagnosis: cortisol <3 mcg/dL rules out insufficiency. Treatment: glucocorticoid + mineralocorticoid replacement.

Hypothyroidism in elderly: insidious presentation (fatigue, cognitive decline attributed to aging). TSH slightly elevated in older adults (upper limit normal ~4-5 mIU/L in many refs, vs. 2.5 in younger). Levothyroxine: start 25-50 mcg daily, titrate slowly (risk atrial fibrillation if too rapid), target TSH 0.5-2.5.

Hyperthyroidism in elderly: may present atypically (apathy, depression, AF) without classic hyperactivity. Amiodarone-induced (drug side effect), thyroiditis, Graves. Treatment: depends on cause; PTU preferred initially (blocks conversion T4→T3, safer than propylthiouracil for liver).

Cognitive impairment reversible causes: B12 deficiency, thyroid dysfunction, normal pressure hydrocephalus (classic triad: dementia, gait disturbance, incontinence), subdural hematoma (trauma may be minor, forgotten), depression (pseudodementia). Screen all.

Lewy body dementia: visual hallucinations, Parkinsonism, fluctuation. Avoid antipsychotics (can precipitate neuroleptic malignant syndrome). Cholinesterase inhibitors sometimes helpful.

Frontotemporal dementia: personality change, disinhibition, language decline. Younger onset (50-60s). Behavioral management difficult. No pharmacotherapy proven effective.

Hyponatremia in elderly: SIADH common (lung cancer, CNS disease), medication-induced (SSRIs, NSAIDs), volume depletion, adrenal insufficiency. Correction: rate <8-10 mEq/L/day (risk osmotic demyelination). Fluid restriction for SIADH, normal saline for hypovolemia, hypertonic saline (3%) if symptomatic (seizures).

Hyperkalemia in elderly: ACE-I/ARB + NSAIDs + renal disease = triple threat. EKG changes: peaked T waves (earliest), QRS widening (late, dangerous). Treatment: calcium gluconate (stabilize membrane), insulin + dextrose, beta-agonists, diuretics, dialysis if severe.

Hyperglycemia in elderly: goals relaxed (150-180 mg/dL acceptable to avoid hypoglycemia). Hypoglycemia more dangerous (stroke, MI, death). Medications: avoid sulfonylureas (hypoglycemia risk), metformin if renal function normal, GLP-1 agonist (weight loss benefit).

Atrial fibrillation in elderly: stroke risk higher (CHADS2 score); anticoagulation almost always indicated. DOAC preferred (easier, no monitoring). Aspirin alone insufficient. Rate vs. rhythm control: rate control acceptable (lenient HR <110).

Syncope evaluation in elderly: common, high morbidity/mortality (falls, fractures). Causes: arrhythmia (EKG, Holter/telemetry), orthostatic hypotension, carotid sinus hypersensitivity. Falls from syncope may be misattributed to weakness/dizziness.

Aspiration risk: dysphagia common post-stroke, Parkinson, dementia. Speech/swallow therapy assessment critical. Thickened liquids, small bites, upright positioning reduce risk. PEG tubes debated (not prevention of aspiration, though may reduce food aspiration).

Anticholinergic burden in elderly: anticholinergic drugs (antihistamines, antispasmodics, tricyclic antidepressants, benzodiazepines) increase dementia/cognitive impairment risk, urinary retention, constipation. Beers Criteria lists agents to avoid. Calculate Anticholinergic Cognitive Burden (ACB) scale.

Hypoalbuminemia in elderly: nutritional marker; increases drug toxicity (less protein binding), predicts mortality. Nutrition screening mandatory (MNA, SNAQ). Supplementation if malnourished.

Pressure injury prevention: immobility + malnutrition + moisture = high risk. Alternating pressure mattresses, frequent turning, skin care, nutrition optimization. Healing difficult in elderly (longer time, higher costs).

End-of-life planning: advance directives, healthcare proxy, POLST form (Physician Orders for Life-Sustaining Treatment, legally binding in many states). Conversation when patient has capacity (before crisis). Values exploration: focus on quality of life, function, what patient considers acceptable.

# COMMUNICATION SKILLS EXPANDED (targeting 60+ total)
Active listening techniques: reflection ('So what you're saying is...'), summarization, open-ended questions, silence (allow patient to process). Avoid: interrupting, task-focused responses, dismissive language.

Empathetic response phrases: 'I can see how that would be frightening,' 'That sounds incredibly difficult,' 'I'm here to help.' Validate emotion without necessarily agreeing with factual beliefs.

Managing patient expectation: early in encounter, assess expectations (what do they hope will happen?), compare with realistic outcomes, negotiate plan together. Prevents conflict later.

Discussing treatment limitations: cancer patient with metastatic disease wanting curative treatment. Acknowledge wish, explain why impossible, transition to realistic goals (comfort, time with family). Offer supportive care, palliative consult.

Conflict resolution in ICU: family wants continued aggressive care despite poor prognosis. Approach: validate feelings, share clinical info (prognosis, what ICU interventions can/can't achieve), explore values, offer ethics consultation if needed.

Dealing with hostility: stay calm, don't escalate, set boundaries ('I want to help, but I need to speak respectfully'), involve security if threatening. Chart objective facts.

Team dynamics and hierarchy: junior doctors/nurses may fear speaking up about senior errors. CRM principles: speak up culture, no question is stupid, safety above hierarchy.

Bedside teaching (attending/resident/student): balance patient care with education. Brief cases on rounds to maintain efficiency; avoid lengthy presentations.

Informed consent documentation: document key elements discussed (diagnosis, treatment options, risks/benefits, alternatives, consequences of refusal). Patient understanding should be demonstrated (teach-back, questions answered).

Cultural sensitivity in discussions: dietary restrictions, decision-making preferences (individual vs. family), prayer/spiritual needs, end-of-life expectations. Ask, don't assume.

Disclosure of medical errors: prompt (same day), honest ('I made an error...'), explain impact/plan to prevent. Apology important. Avoid defensive/blaming language. Legal/risk management involvement depends on severity.

Difficult conversations checklist: setting (private, quiet), time (unhurried), family present (ask patient), accurate information (get facts straight), empathetic tone, offer support/resources, confirm understanding.

Phone conversations with families: clear speech, confirm identity, summarize key points before hanging up, offer follow-up contact. Document what was discussed.

Negotiating goals of care: explore patient values (QOL, independence, time with family, pain-free vs. cure-focused). Align medical recommendations with values. Update as condition changes.

Discussing organ donation: recent death, family grieving. Support staff or chaplain assist. Ensure patient would have wanted this (prior wishes, family knowledge). No pressure; donation gift to society.

Discussing code status: multiple times, not just once. Reassess as condition changes. Clarify: CPR (chest compressions, intubation, ICU); DNR (no CPR, focus comfort); DNI (no intubation, other measures ok).

Managing unrealistic expectations: patient with stage 4 cancer wanting '100% cure.' Acknowledge hope, explain realistic prognosis, transition to achievable goals (symptom control, time with family, dignity).

Asking for permission to share bad news: 'Do you want me to tell you everything I know about your condition, even if it's not what you want to hear?' Most say yes; respects autonomy.

Using translators: speak clearly (not louder), provide concepts not word-by-word translation, allow extra time, verify understanding. Avoid jargon/idioms.

Debriefing after critical event: team gathers soon after (resuscitation, patient death, trauma), reviews what went well, what to improve, emotional support. Improves morale, reduces moral injury.

# QUALITY & SAFETY EXPANDED (targeting 70+ total)
Adverse event tracking: report in system (not punitive), investigate root cause, implement fixes, monitor for effectiveness. Culture of safety essential (no blame, learning focus).

Never events prevention: retained foreign object (surgical counts), wrong site surgery (time-out, marking), wrong patient (ID verification), catheter-associated infections (bundle approach), medication errors (independent double-checks).

Checklist implementation: surgical safety checklist (WHO) reduces mortality 30-40%. Pre-op, post-op, post-anesthesia briefing. Compliance and team buy-in critical.

Error recovery: systems designed to allow safe recovery (double-checks, expert consultation, escalation pathways). Example: wrong antibiotic ordered, caught before administration, prevented harm.

Medication safety: tall-man lettering (LORazepam vs. LOPERamide), dose caps (max daily dose clearly labeled), independent verification (pharmacist + nurse check), smart pumps (catch programmed overdoses).

Surgical site infections: bundle (skin antiseptic, appropriate antibiotics timing, temperature management, glucose control). Laparoscopic < open risk. Timing antibiotics <60 min pre-incision reduces risk.

Ventilator-associated pneumonia bundle: HOB 30-45°, daily sedation vacation, daily spontaneous breathing trial, oral care, avoid unnecessary reintubations. VAP rate reduces with bundle compliance.

CAUTI prevention: use catheter only if necessary, remove ASAP, sterile insertion technique, proper maintenance (closed system, secure), avoid unnecessary irrigation. Most common HAI; most preventable.

CLABSI prevention: aseptic insertion (maximal sterile precautions), maintain sterility of dressing, prompt removal (no dwell time beyond medically necessary), education of staff. Zero-CLABSI programs achievable.

Hand hygiene monitoring: secret shoppers, direct observation, feedback to staff. Highest compliance before/after patient contact (not after touching environment). Alcohol hand rubs > soap/water for most (except C. diff, norovirus).

MRSA screening and isolation: screen on admission (nares swab, other sites if high risk), contact precautions if positive (gown/gloves), decolonization with mupirocin (topical) controversial. Reduces spread within hospital.

Hospital-grade disinfectants: quaternary ammonium compounds, hypochlorite, isopropyl alcohol. Correct concentration, contact time, resistant organisms (norovirus, cryptosporidium require specific agents). Environmental cleaning critical (high-touch surfaces).

Antibiotic stewardship metrics: days of therapy (DOT) vs. defined daily doses (DDD), appropriate use of broad-spectrum agents (reduced over time as cultures return), Clostridium difficile rates (lower with stewardship). Annual reports to clinicians, targets set.

Staff burnout and error rate: fatigued staff make more errors. 24-hour shifts associated with more adverse events (vs. 16-hour limits). Scheduling, adequate staffing, support resources reduce burnout and errors.

Mortality and morbidity rounds: peer review of adverse outcomes, learning (not punishment), cases discussed without defensive tone. Prevents repeat mistakes, identifies system issues.

Patient satisfaction surveys: HCAHPS (Hospital Consumer Assessment of Healthcare Providers and Systems); used for metrics/payment. Scores driven by communication, pain control, cleanliness, staff responsiveness.

Transparency reporting: mortality rates by hospital/surgeon, infection rates, readmission rates publicly available (Leapfrog Hospital Safety Grades, CMS Hospital Compare). Drives quality improvement.

Incident command system (ICS): during surge/disaster, clear chain of command (incident commander at top), roles defined (medical officer, logistics, planning). Improves coordination, prevents chaos.

Failure mode and effects analysis (FMEA): proactively identify where process can fail (e.g., central line insertion), assess risk, implement safeguards before failure occurs. Reduces adverse events.

Pareto analysis: 80% of problems from 20% of causes. Identify high-impact causes, focus efforts there (vs. spreading resources thin). Example: 80% of VAP from 3 ICUs (focus on those 3).

Benchmarking: compare own hospital's metrics to peer group, regional, national standards. Identify gaps, implement best practices from leaders.

Sustainability of QI initiatives: many fail due to loss of momentum/resources. Assign ownership, ongoing measurement, reinforce importance at leadership level, link to compensation/metrics.

# PALLIATIVE CARE EXPANDED (targeting 60+ total)
Prognostic communication: difficult but essential. Use evidence-based estimates (median survival, % alive at specific timepoints) but acknowledge uncertainty. Separate prognosis (disease course) from life expectancy (total time).

Cachexia and wasting: metabolic derangement; appetite stimulants (megestrol acetate, mirtazapine) have limited benefit. Focus on foods patient enjoys, smaller frequent meals, avoid forced feeding. Comfort over nutrition.

Constipation management: near-universal with opioids. Stool softener + osmotic laxative (miralax) scheduled (not PRN); senna if needed. Avoid anticholinergics. Monitor frequency, consistency.

Bowel obstruction in terminal cancer: distinguish complete vs. partial. Partial: NGT, TPN often manage. Complete: palliative approach (surgical intervention only if specific block, expected survival >3 months). Symptom control (antisecretory drugs, steroids) prioritized.

Ascites management: paracentesis for comfort (remove up to 5-10L at once), reaccumulates in 2-4 weeks. Diuretics (spironolactone) if future taps planned; dietary sodium restriction. Goal: comfort.

Pleural effusion: thoracentesis if dyspneic (temporary relief), pleurodesis if recurrent (talc or chemotherapy agent), indwelling catheter if expected survival <6 months (outpatient drainage).

Depression in terminal illness: common (20-50%), undertreated. SSRIs take 2-4 weeks onset (too late if dying soon); methylphenidate faster onset, better tolerability. Psychotherapy, spiritual care adjuncts.

Anxiety management: short-acting benzodiazepines (lorazepam) for acute anxiety, buspirone or SSRIs for sustained (if time allows). Breathing exercises, relaxation, music therapy non-pharmacologic.

Delirium in dying: different from depression/anxiety. Causes: infection, medication, metabolic, hypoxemia (consider reversibility). Antipsychotics (haloperidol, olanzapine) symptomatic relief but don't alter course. Family education key.

Death rattle (terminal secretions): alarming to family, not distressing to patient. Anticholinergics (scopolamine patch, atropine drops) reduce secretions. Positioning (turn to side), gentle suctioning (avoid aggressive).

Dyspnea in end-of-life: opioids most effective (morphine, fentanyl patches), add benzodiazepine if anxious, supplemental oxygen if comfort (no evidence survival benefit). Fan, cool air, positioning, reassurance.

Myoclonus (muscle jerks): opioid-induced; benzodiazepines (lorazepam, clonazepam) treat. Rotation to different opioid may help (less metabolite accumulation).

Terminal extubation: process of removing endotracheal tube in dying patient. Extubate compassionately (medications on board: sedation, opioids for comfort), family present, continue comfort measures post-extubation. Often patient breathes briefly; expected/normal.

Spiritual care: chaplaincy referral for all patients (not just religious). Prayers, rituals, meaning exploration, existential concerns. Respects diverse beliefs.

Legacy work: life review, ethical wills (non-legal wishes for family), letters, recordings for children. Meaningful, provides sense of completion.

Family support post-death: grief support, helpline/support groups, bereavement follow-up. High-risk bereaved tracked for complicated grief.

Hospice transition: goal-concordant care at end-of-life, usually at home or hospice facility. Holistic (physical, emotional, spiritual), family-centered, 24/7 support. Medicare/Medicaid covered.

Inpatient hospice: specialized hospital units or designated beds. Benefits: familiar environment, family/friends, specialized staff, symptom management expertise.

Concurrent palliative/curative care: not mutually exclusive. Early palliative referral (at diagnosis serious illness) improves outcomes. Combine aggressive treatment with parallel comfort goals.

Moral distress: clinician caring for patient whose values conflict with own (e.g., patient requesting withdrawal of life support patient believes unethical). Ethics consultation, peer support, autonomy respect vs. conscience objection management.

# ADMINISTRATIVE & CAREER EXPANDED (targeting 30+ total)
Physician wellness programs: EAP (employee assistance program), mental health services, peer support, mindfulness programs, yoga, financial counseling. Employer-sponsored, confidential.

Work-life balance by specialty: surgery (high hours, autonomy), pediatrics (high emotion, good hours usually), emergency medicine (schedule flexibility but high stress), critical care (shift work, high acuity).

Career development milestones: postgraduate training (residency 3-5 years, fellowship 2-3 years), board certification (written exam + oral), maintenance of certification (MOC, self-directed learning annually).

Leadership training: courses/coaching for physicians pursuing leadership (medical director, CMO, residency program director). Skills: communication, team management, finance, quality improvement.

Physician engagement: involves physicians in hospital/system decisions, shared decision-making, value their input. Reduces burnout, improves quality metrics. Culture shift away from top-down mandates.

Physician compensation: varies by specialty (orthopedic > pediatric), location, experience, practice type (private > employed > academic). RVU-based (relative value unit, productivity-based) common; can incentivize quantity over quality if not careful.

Group dynamics in medicine: team-based care increasingly common. Interdisciplinary rounds, shared protocols, mutual support. Benefits: reduced errors, shared burden. Challenges: role clarity, communication.

Feedback and performance reviews: 360 feedback (from colleagues, staff, patients), objective metrics (patient satisfaction, quality data, financial metrics), alignment with institutional goals. Transparent, regular feedback improves performance.

Conflict resolution: peer review, mediation, arbitration if disputes arise. Address early before escalates. Professional conduct, appropriate boundaries with colleagues/staff/patients.

Continuing education: required for licensure (CME credits), board certification maintenance, specialty-specific updates. Online, conferences, journal clubs. Keep knowledge current.

Malpractice insurance: tail coverage important if changing jobs, retiring. Occurrence vs. claims-made policies. Legal defense, patient communication after adverse event.

Documentation for legal protection: clear, timely, objective facts, legible, no alterations/gaps, specific diagnosis/plan, reason for decisions. Poor documentation = poor defense.

Breach of confidentiality: HIPAA violations, patient privacy breaches. Report breaches, correct systems, educate staff. Fines up to $100+ per violation, plus reputation damage.

Physician-industry relationships: COI (conflict of interest) disclosures required for speaking, research, consulting. Sunshine Act transparency. Importance: maintain trust, objectivity.

Academic advancement: teaching, research, service at academic institutions. Promotion tracks (tenure, associate prof, full prof). Different metrics: publication count, grant funding, teaching evaluations.

Transitioning to industry: pharma, medical device, biotech, consulting. Different culture, hours, expectations. Clinical knowledge valued; regulatory, market understanding needed.

Retirement planning: physician income typically allows later career flexibility. Retirement accounts (401k, IRA), taxable accounts, real estate. Financial advisor essential. Physician-specific financial planning.

Physician mentorship: formal or informal, guides early-career physicians in navigating specialty, career planning, work-life balance, developing expertise. Bidirectional (mentor learns too).

Teaching skills development: effective teaching requires skill development (presentation, feedback, assessment). Courses available; practice improves ability.

Healthcare policy involvement: physicians at table for healthcare decisions (quality, safety, cost, access). Advocacy on issues affecting medicine (insurance, regulations, research funding).

# ADDITIONAL CRITICAL TOPICS
Obstetric anesthesia complications: failed epidural (1-2%), dural puncture headache (0.5-1%, treated with blood patch), local anesthetic toxicity (seizures, cardiac depression, treat with lipid emulsion).

Anesthesia-related complications: malignant hyperthermia, awareness under anesthesia (1 in 1000), post-operative nausea/vomiting, sore throat, vocal cord injury, aspiration.

Critical illness myopathy: muscle breakdown in ICU (steroids + paralytic agents + sepsis + prolonged immobility). Weakness persists weeks-months. Prevention: minimize paralytics, mobilize early, minimize steroids.

Healthcare disparities: minority patients receive lower quality care (less likely to get guideline-directed therapy, higher mortality, fewer interventions). Systemic issues; addressing requires awareness + systems change.

Telehealth in critical care: remote presence (robotic), telepaths (remote radiologists), telemedicine (video consultation). Expands access, reduces travel; challenges in hands-on care (physical exam limited).

Artificial intelligence in ICU: predictive models (sepsis prediction, deterioration alerts), automated documentation, image analysis. Promise: earlier intervention, efficiency; concerns: bias, accountability, validation needed.

Ethical frameworks: autonomy, beneficence, non-maleficence, justice. Principle-based approach to ethical dilemmas. Conflicts between principles (autonomy vs. beneficence) require navigation.

Social determinants of health: poverty, housing, food insecurity, discrimination predispose to illness. Healthcare addresses medical aspect only. Partnerships with social services critical.

Climate change and health: heat-related illness, air quality decline, infectious disease spread, mental health impacts. Physician advocacy important for planetary health.
"""

    # Convert bulk text to individual units
    lines = additional_units_text.strip().split('\n')
    current_topic = None

    for line in lines:
        if line.startswith('# '):
            current_topic = line.replace('# ', '').replace(' (targeting', '').rstrip(')')
        elif line.strip() and not line.startswith('# '):
            # Extract section name from topic if present
            section = current_topic.split()[0].lower() if current_topic else "general"

            units.append({
                "id": f"phase4_unit_{unit_id_counter}",
                "text": line.strip(),
                "metadata": {
                    "topic": current_topic or "Clinical Essentials",
                    "topic_tags": [section, "clinical", "evidence-based"],
                    "library": "intern_year_medicine",
                    "source_name": "Phase 4 Knowledge Base - Final",
                    "book": "Phase 4 - Remaining Essentials (Final Expansion)",
                    "section": section,
                    "created_at": datetime.now().isoformat(),
                    "chunk_type": "fact"
                }
            })
            unit_id_counter += 1

    return units


if __name__ == "__main__":
    units = generate_phase4_final()

    # Save to JSON
    output_path = Path("data") / "phase4_final.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(units, f, indent=2, ensure_ascii=False)

    # Statistics
    by_section = {}
    for unit in units:
        section = unit["metadata"]["section"]
        by_section[section] = by_section.get(section, 0) + 1

    print(f"[OK] Phase 4 final expansion completed: {len(units)} total units")
    print(f"  Output: {output_path}\n")

    print("PHASE 4 FINAL BREAKDOWN:")
    total_count = 0
    for section, count in sorted(by_section.items()):
        total_count += count
        print(f"  {section:30s}: {count:3d} units")

    print(f"\nTotal Phase 4 Units: {total_count}")
    print(f"Estimated Cumulative (Phases 1-4): ~{total_count + 475} units")
    print(f"Target: 1,200 units")
