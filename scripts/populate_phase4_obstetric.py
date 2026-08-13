#!/usr/bin/env python3
"""
Phase 4.4: Obstetric Emergencies

Generates 60-80 medical knowledge units covering:
- Preeclampsia/eclampsia and magnesium sulfate protocol
- HELLP syndrome
- Gestational diabetes management
- Placental abruption
- Placenta previa
- Amniotic fluid embolism
- Peripartum cardiomyopathy
- Maternal sepsis
- Postpartum hemorrhage
- Shoulder dystocia
"""

import json
from datetime import datetime

def create_obstetric_units():
    """Generate obstetric emergency units."""

    units = [
        # === PREECLAMPSIA & ECLAMPSIA ===
        {
            "topic": "Preeclampsia - Definition & Risk Factors",
            "subtopic": "preeclampsia_overview",
            "content": "Preeclampsia = new-onset hypertension (SBP ≥140 or DBP ≥90) after 20 weeks gestation + proteinuria (≥0.3 g/24h or ≥1+ on dipstick) OR new end-organ dysfunction without proteinuria (liver injury, creatinine >1.1, thrombocytopenia <100k, pulmonary edema, cerebral symptoms). Onset typically 2nd-3rd trimester; early-onset <34 weeks (more severe). Risk factors: first pregnancy, age >35 or <18, obesity, chronic hypertension, diabetes, prior preeclampsia. Pathophysiology: placental ischemia, abnormal trophoblastic invasion, endothelial dysfunction.",
            "tags": ["preeclampsia", "pregnancy", "hypertension", "high_yield"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Eclampsia - Seizures & Management",
            "subtopic": "eclampsia",
            "content": "Eclampsia = preeclampsia + seizures (tonic-clonic, generalized). Seizures may occur without warning, antecedent symptoms may be absent. Presentation: headache, visual changes, epigastric pain (are warning signs but eclampsia can present suddenly). Seizure management: ensure airway safety (position on side, prevent aspiration), give oxygen, apply fetal monitoring. Magnesium sulfate FIRST-LINE: 4-6 g IV bolus over 15-20 min (loading), then 1-2 g/h infusion. Prevents recurrent seizures (prevents ~60% of seizures in preeclampsia). Anticonvulsants (lorazepam, phenytoin) second-line if continued seizures despite magnesium.",
            "tags": ["eclampsia", "seizures", "magnesium", "pregnancy"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Magnesium Sulfate Dosing & Toxicity",
            "subtopic": "magnesium_protocol",
            "content": "Loading: 4-6 g IV slow push (or 10-14 g IM divided, less common now). Maintenance: 1-2 g/h IV infusion for seizure prophylaxis and treatment (typically continued 12-24h post-delivery or after last seizure). Monitoring: deep tendon reflexes (hypermagnesemia abolishes reflexes), respiratory depression (magnesium depresses respiratory drive). Therapeutic level 4-7 mg/dL; toxicity begins >10 mg/dL. Signs of excess: loss of deep tendon reflexes (loss indicates severe toxicity), respiratory depression. Discontinue if reflexes lost, monitor closely. Fetal effects: minimal (not teratogenic); used in preeclampsia for seizure prevention and in preterm labor. Hypocalcemia can occur; have calcium gluconate available as antidote if severe toxicity.",
            "tags": ["magnesium", "dosing", "toxicity", "preeclampsia"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Hypertension Management in Preeclampsia - Antihypertensive Choice",
            "subtopic": "preeclampsia_antihypertensives",
            "content": "Severe range hypertension in preeclampsia: SBP ≥160 or DBP ≥110. Goal: reduce by 15-25% (NOT to normotension, which may compromise placental perfusion). First-line agents: IV labetalol (20 mg initial, then 40-80 mg q10 min, max 220 mg) or IV hydralazine (5-10 mg initial, q20 min). Oral nifedipine (immediate-release 10-20 mg q20 min, avoid extended-release) alternative if IV unavailable. Avoid ACE inhibitors, ARBs (teratogenic in pregnancy). Methyldopa safe but slow-acting (30 min). Goal SBP 140-150 (permissive hypertension to maintain placental perfusion). Delivery definitive treatment.",
            "tags": ["preeclampsia", "hypertension", "antihypertensives"],
            "library": "intern_year_medicine"
        },

        # === HELLP SYNDROME ===
        {
            "topic": "HELLP Syndrome - Hemolysis, Elevated Liver Enzymes, Low Platelets",
            "subtopic": "hellp_syndrome",
            "content": "HELLP = life-threatening variant of preeclampsia. Hemolysis: schistocytes on blood smear, elevated indirect bilirubin (>1.2), elevated LDH (>600). Elevated liver enzymes: AST >70 U/L (often >1000), indicative of liver ischemia/infarction. Low platelets: <100k (often <50k), risk of bleeding. Onset: 3rd trimester (30-36 weeks) or postpartum (72h post-delivery, 'late HELLP'). Presentation: malaise, RUQ pain, nausea; may be mistaken for gastroenteritis. Complications: DIC, acute liver failure, placental abruption, pulmonary edema. Mortality 1-3% despite optimal management; fetal mortality 5-15%.",
            "tags": ["hellp", "hemolysis", "liver", "pregnancy"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "HELLP Management & Delivery",
            "subtopic": "hellp_management",
            "content": "Immediate management: magnesium sulfate (seizure prophylaxis), control hypertension (labetalol/hydralazine), IV fluids cautiously (risk of pulmonary edema). Platelet transfusion: indicated if <50k or active bleeding; prophylactic transfusion before procedures if <50k. Fresh frozen plasma if coagulopathy (PT prolonged, low fibrinogen). Corticosteroids: betamethasone 12 mg IM × 2 doses (48h apart) to accelerate fetal lung maturity if <34 weeks. Deliver urgently: vaginal delivery if no contraindications (spontaneous labor, favorable cervix), cesarean if failed labor or fetal distress. Timing: consider expectant management 24-48h if <32 weeks and mother/fetus stable to gain fetal maturity benefit, but monitor intensively.",
            "tags": ["hellp", "management", "delivery"],
            "library": "intern_year_medicine"
        },

        # === GESTATIONAL DIABETES ===
        {
            "topic": "Gestational Diabetes Mellitus (GDM) - Screening & Diagnosis",
            "subtopic": "gdm_overview",
            "content": "GDM = glucose intolerance first recognized during pregnancy (typically 2nd-3rd trimester). Screening: 50 g oral glucose tolerance test (OGTT) at 24-28 weeks (fasting not required). If result >140 mg/dL, proceed to 3-hour 100 g OGTT. Diagnosis: ≥2 abnormal values on 3-hour test (fasting >95, 1-h >180, 2-h >155, 3-h >140 mg/dL). Risk factors: maternal age >25, obesity, family history diabetes, prior GDM, polycystic ovary syndrome. Complications: maternal (preeclampsia risk increases), fetal (macrosomia, birth injury, neonatal hypoglycemia), long-term (both mother and infant at risk for type 2 diabetes).",
            "tags": ["gdm", "gestational_diabetes", "screening"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "GDM Management - Diet, Monitoring, Insulin",
            "subtopic": "gdm_management",
            "content": "First-line: medical nutrition therapy (30-33 kcal/kg/day, 45-50% carbs, emphasis on complex carbs/fiber). Self-monitored blood glucose (fasting <95, 1-h post-prandial <140 mg/dL targets). Home glucose monitoring 3-4 times daily (fasting + 1h after main meals). Insulin: if glucose targets not met with diet (25-40% of women). Insulin types: NPH (basal, longer-acting, 0.5-1 U/kg/day divided), regular or rapid-acting (bolus with meals). Metformin: some data support use (500-2000 mg daily divided) as alternative/adjunct to insulin; fewer hypoglycemia episodes. Glyburide: second-generation sulfonylurea, controversial (higher rates of neonatal hypoglycemia in some studies). Monitor fetal growth with ultrasound (monthly at diagnosis, q2w if insulin-requiring).",
            "tags": ["gdm", "management", "insulin", "monitoring"],
            "library": "intern_year_medicine"
        },

        # === PLACENTAL ABRUPTION ===
        {
            "topic": "Placental Abruption - Presentation & Severity",
            "subtopic": "abruption_overview",
            "content": "Placental abruption = premature separation of placenta from uterine wall. Presentation: vaginal bleeding (may be concealed behind placenta), abdominal/back pain (may be severe), uterine tenderness/contractions, fetal distress on monitoring. Severity: mild (small area, mother stable, fetus reassuring), moderate (moderate bleeding, maternal tachycardia/tachypnea, fetal distress), severe (massive bleeding, maternal shock, fetal demise). Risk factors: trauma (motor vehicle accident, fall, intimate partner violence), hypertension, smoking, cocaine use, prior abruption. Complications: hemorrhagic shock, DIC (from thromboplastin release), acute renal failure, fetal death.",
            "tags": ["abruption", "placental", "hemorrhage", "pregnancy"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Placental Abruption - Management & Delivery",
            "subtopic": "abruption_management",
            "content": "Immediate: two large-bore IVs, type & cross, CBC, coagulation panel (PT, aPTT, fibrinogen, D-dimer), initiate fetal monitoring (continuous). IV fluids, blood products as needed (maintain Hgb >7 g/dL). Magnesium sulfate if <34 weeks (neuroprotection). Delivery urgent: vaginal acceptable if mother/fetus stable, cervix favorable; cesarean if fetal distress, maternal shock, failed labor, or incomplete dilation after reasonable trial. Massive transfusion protocol if hemorrhage refractory (1:1:1 RBC:FFP:platelets). Monitor closely for DIC (consumption of platelets, fibrinogen, prolonged PT/aPTT); manage with appropriate blood products. Fetal prognosis depends on severity and timing to delivery.",
            "tags": ["abruption", "management", "delivery"],
            "library": "intern_year_medicine"
        },

        # === PLACENTA PREVIA ===
        {
            "topic": "Placenta Previa - Definition & Management",
            "subtopic": "placenta_previa",
            "content": "Placenta previa = placental implantation covering cervical os (complete) or near it (partial/low-lying). Risk: vaginal bleeding (painless) in 2nd-3rd trimester. Diagnosis: ultrasound (transvaginal more accurate). At delivery: vaginal delivery impossible if complete/partial previa (placenta would deliver before baby). Management in pregnancy: pelvic rest (avoid sexual intercourse, strenuous activity), avoid tampons. Anticipate delivery: planned cesarean section at 39 weeks (or earlier if bleeding complicates). Major complications: massive bleeding at delivery (especially if placenta accreta coexisting), need massive transfusion, ICU care. Maternal morbidity significant with previa + accreta.",
            "tags": ["placenta_previa", "bleeding", "pregnancy"],
            "library": "intern_year_medicine"
        },

        # === AMNIOTIC FLUID EMBOLISM ===
        {
            "topic": "Amniotic Fluid Embolism (AFE) - Pathophysiology & Presentation",
            "subtopic": "afe_overview",
            "content": "AFE = rare but catastrophic entry of amniotic fluid into maternal circulation during labor/delivery/postpartum. Pathophysiology: fetal fluid enters maternal venous system (from uterine vein trauma), triggers inflammatory cascade (similar to anaphylaxis), pulmonary vasospasm, right heart failure. Presentation: sudden onset dyspnea, hypotension, loss of consciousness, seizures, cardiac arrest (often during labor or immediately post-delivery). May have rash (fetal squames in skin), fever, coagulopathy, pink frothy sputum (pulmonary edema). Incidence ~1 per 30,000 deliveries; mortality 60-80% despite aggressive resuscitation. Risk factors: operative delivery (induction, cesarean, forceps), maternal age >35, placental abruption.",
            "tags": ["afe", "amniotic_fluid", "embolism", "emergency"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "AFE Management - Resuscitation & Supportive Care",
            "subtopic": "afe_management",
            "content": "Management: immediate resuscitation (ACLS protocol), high-flow O2 (100%), intubation if respiratory failure. IV access × 2, aggressive fluid resuscitation (crystalloid + PRBCs). Pulmonary artery catheter (Swan-Ganz) may help guide management if available. Vasopressor support (dopamine, dobutamine, norepinephrine) for shock. Treat coagulopathy: FFP, cryoprecipitate for low fibrinogen, platelets if <50k. ECMO consideration if refractory cardiac arrest (some centers use ECMO-assisted resuscitation in AFE). No specific antidotes; supportive care + time are mainstay. Maternal mortality ~60%; fetal survival depends on timing (those delivered during initial resuscitation have better fetal outcomes). Antihistamines, steroids sometimes used though evidence limited.",
            "tags": ["afe", "resuscitation", "management"],
            "library": "intern_year_medicine"
        },

        # === PERIPARTUM CARDIOMYOPATHY ===
        {
            "topic": "Peripartum Cardiomyopathy - Definition & Diagnosis",
            "subtopic": "ppcardiomyopathy",
            "content": "Peripartum cardiomyopathy = dilated cardiomyopathy occurring in pregnancy or early postpartum (typically within 5 months post-delivery). Presentation: dyspnea, orthopnea, edema, fatigue (may be mistaken for normal pregnancy changes). Diagnosis: EKG (nonspecific changes), echocardiogram (dilated LV, reduced ejection fraction <45%), elevated troponin/BNP. Etiology unclear (autoimmune? viral? pregnancy-related hemodynamic stress?). Risk factors: advanced maternal age, multiparity, hypertension, preeclampsia. Prognosis: variable; ~50% recover LV function with optimal medical management, 25% have persistent dysfunction, 25% fatal or need transplant.",
            "tags": ["cardiomyopathy", "peripartum", "pregnancy"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Peripartum Cardiomyopathy Management",
            "subtopic": "ppcardiomyopathy_management",
            "content": "Medical management: ACE inhibitors (lisinopril, enalapril; teratogenic in pregnancy so avoid 1st trimester but used postpartum), beta-blockers (labetalol safe in pregnancy, carvedilol/metoprolol postpartum), diuretics (furosemide for volume overload), aldosterone antagonist (spironolactone). Anticoagulation: warfarin or heparin if EF <35% (risk of thrombus/stroke). Inotropic support if hemodynamically unstable (dobutamine, milrinone for acute decompensation). Mechanical support (IABP, LVAD) bridge to recovery or transplant if refractory heart failure. Delivery: vaginal preferred if stable; cesarean if maternal deterioration. Avoid NSAIDs, avoid pregnancy recurrence (high risk of recurrent cardiomyopathy with subsequent pregnancies; counseling needed).",
            "tags": ["cardiomyopathy", "management", "pregnancy"],
            "library": "intern_year_medicine"
        },

        # === MATERNAL SEPSIS ===
        {
            "topic": "Maternal Sepsis - Recognition in Pregnancy",
            "subtopic": "maternal_sepsis",
            "content": "Sepsis in pregnancy often presents atypically. SIRS criteria differ: tachycardia baseline higher in pregnancy (>100 might be normal); tachypnea >20; temperature extremes. Sources: chorioamnionitis (intrauterine infection), postpartum endometritis, UTI/pyelonephritis, surgical site infection (post-cesarean), pneumonia. Recognition challenging: pregnancy symptoms overlap (fatigue, nausea). Key: maintain high suspicion, obtain blood cultures early, broad-spectrum antibiotics early. Aggressive fluid resuscitation; vasopressors if hypotensive. Source control (delivery if intrauterine infection, antibiotics for UTI, wound drainage if needed).",
            "tags": ["sepsis", "maternal", "pregnancy", "infection"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Chorioamnionitis - Diagnosis & Treatment",
            "subtopic": "chorioamnionitis",
            "content": "Chorioamnionitis = intrauterine infection (bacteria ascend through cervix). Diagnosis: fever (>38.0°C) + ≥2: maternal tachycardia (>100), fetal tachycardia (>160), fundal tenderness, foul-smelling amniotic fluid, elevated maternal WBC (>15k). Amniotic fluid gram stain/culture definitive but delivery often urgent. Treatment: immediate delivery (induction if favorable cervix, cesarean if unfavorable/failed induction) + antibiotics. Regimen: ampicillin 2 g IV q6h + gentamicin 5 mg/kg IV q24h + clindamycin 900 mg IV q8h (if cesarean or suspected anaerobes). Continue antibiotics 24h post-delivery (total 48h minimum). Maternal outcomes generally good with prompt antibiotics + delivery. Fetal/neonatal sepsis risk; neonates given sepsis workup.",
            "tags": ["chorioamnionitis", "infection", "pregnancy"],
            "library": "intern_year_medicine"
        },

        # === POSTPARTUM HEMORRHAGE ===
        {
            "topic": "Postpartum Hemorrhage (PPH) - Definition & Etiology",
            "subtopic": "pph_overview",
            "content": "PPH = blood loss >500 mL vaginal delivery, >1000 mL cesarean delivery in first 24h. Major risk factors: uterine atony (60%), placenta previa/accreta (15%), retained placenta (5%), coagulopathy (5%), other (lacerations, uterine rupture) (10%). 4Ts mnemonic: Tone (atony), Tissue (retained products), Thrombin (coagulopathy), Trauma (lacerations). Early PPH (first 24h) vs. late PPH (24h-12 weeks). Presentation: heavy vaginal bleeding, passage of clots, signs of shock (tachycardia, hypotension). Massive transfusion protocol if refractory bleeding.",
            "tags": ["pph", "postpartum_hemorrhage", "bleeding", "high_yield"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Uterine Atony - Management",
            "subtopic": "uterine_atony",
            "content": "Uterine atony = inadequate uterine muscle contraction post-delivery, most common cause of PPH. Management: immediate uterine massage (vigorous external massage through abdominal wall, stimulates contraction), IV oxytocin bolus (10 U IV push, then continuous infusion 10-80 mL/h), then methylergonovine (Methergine) 0.2 mg IM/IV q2-4h (NOT if hypertensive, contraindicated in preeclampsia). If refractory: misoprostol 1000 μg rectal (slow onset but no contraindications), carboprost (Hemabate) 250 μg IM q15 min (max 8 doses) - potent uterotonic, use cautiously. Intervention radiology: angiographic embolization if medical management fails. Surgery: uterine compression (B-Lynch suture), hysterectomy last resort (high morbidity).",
            "tags": ["atony", "uterine", "hemorrhage", "management"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Retained Placenta - Diagnosis & Management",
            "subtopic": "retained_placenta",
            "content": "Retained placenta = placenta not delivered within 30-60 min of fetal delivery. Diagnosis clinical (failure to deliver, bleeding continuing). Risk: manual removal needed (increased infection, hemorrhage). Complications: placenta accreta (abnormal invasion, high bleeding/hysterectomy risk). Management: oxytocin bolus first (may stimulate contraction/delivery). Manual removal: controlled cord traction, fundal support, hand inserted to separate placenta from uterus (requires anesthesia/analgesia). Ensure placenta completely delivered (retained fragments → infection, hemorrhage). Send for pathology. If placenta accreta suspected, prepare for possible hysterectomy (embolization alternative at some centers).",
            "tags": ["retained_placenta", "hemorrhage", "management"],
            "library": "intern_year_medicine"
        },

        # === SHOULDER DYSTOCIA ===
        {
            "topic": "Shoulder Dystocia - Recognition & Risk Factors",
            "subtopic": "shoulder_dystocia",
            "content": "Shoulder dystocia = fetal anterior shoulder impacted behind maternal pubic symphysis after fetal head delivered (rare but perinatal emergency). Presentation: head delivers, face retracts ('turtle sign'), body does not follow. Risk factors: fetal macrosomia (GDM), maternal obesity, prolonged 2nd stage, operative delivery. Fetal complication: brachial plexus injury (Erb palsy, 5-15% if dystocia occurs), hypoxia, death if not resolved quickly. Maternal: lacerations, hemorrhage.",
            "tags": ["shoulder_dystocia", "obstetric_emergency", "high_yield"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Shoulder Dystocia Resolution - McRoberts Maneuver & Techniques",
            "subtopic": "dystocia_resolution",
            "content": "Immediate recognition critical; call for help (obstetrics, pediatrics, anesthesia). McRoberts maneuver FIRST: sharply hyperabduct maternal hips/thighs to flatten sacral promontory, increases pelvic outlet (resolves ~60% of cases). If unsuccessful: suprapubic pressure (NOT fundal pressure, worsens impaction) applied above pubic symphysis posterior-downward to dislodge anterior shoulder. Posterior shoulder delivery: reach posteriorly, deliver posterior shoulder first (sweeping mechanism), often allows anterior shoulder to follow. Zavanelli maneuver (last resort): replace fetal head back into vagina, proceed to emergent cesarean (high maternal/fetal morbidity). Prognosis: most resolve with McRoberts + suprapubic pressure; brachial plexus injury rates low with rapid management.",
            "tags": ["dystocia", "maneuvrs", "resolution"],
            "library": "intern_year_medicine"
        },
    ]

    return units

if __name__ == "__main__":
    units = create_obstetric_units()

    # Add IDs and timestamps
    for i, unit in enumerate(units):
        unit["id"] = f"phase4_obs_unit_{i}"
        unit["created_at"] = datetime.utcnow().isoformat()

    # Write to file
    output_file = "C:\\Users\\Dean\\anesthesia_attending\\data\\phase4_obstetric_chunks.json"
    with open(output_file, "w") as f:
        json.dump(units, f, indent=2)

    print(f"Generated {len(units)} obstetric units")
    print(f"Output: {output_file}")
