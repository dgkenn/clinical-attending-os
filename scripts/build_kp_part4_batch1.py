
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/_kp_redeepen.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

kps = []

# ── [132] Frailty assessment & clinical implications ──────────────────────────
T = 'Frailty assessment & clinical implications'
DOM = ('General internal medicine, preventive care & geriatrics (admission & cross-cover problems, '
       'perioperative medicine, screening & vaccination, polypharmacy & deprescribing, frailty, '
       'delirium prevention, goals of care)')
DIS = 'medicine'
kps += [
  {'id':'frailty-assessment-d1','topic':T,'domain':DOM,'discipline':DIS,
   'stem':'What five criteria define frailty in the Fried phenotype model?',
   'answer':'Unintentional weight loss, exhaustion, low physical activity, slowness (gait speed), and weakness (grip strength); 3+ of 5 = frail',
   'rationale':'The Fried criteria operationalise frailty as a distinct biological syndrome of diminished physiological reserve predicting adverse outcomes.',
   'bloom':'recall','source':[{'book':'Morgan & Mikhail','page':1494}],'confusable_with':'disability (functional limitation without the frailty phenotype)'},
  {'id':'frailty-assessment-d2','topic':T,'domain':DOM,'discipline':DIS,
   'stem':'An older patient scores 3/5 on the Fried frailty index before elective surgery. How does frailty compare to chronological age as a risk predictor?',
   'answer':'Frailty is a stronger independent predictor of postoperative morbidity and mortality than age alone',
   'rationale':'Multiple studies demonstrate frailty predicts surgical outcomes beyond chronological age, justifying preoperative frailty screening.',
   'bloom':'apply','source':[{'book':'Miller/Baby Miller','page':677}],'confusable_with':'ASA physical status (does not formally incorporate frailty phenotype)'},
  {'id':'frailty-assessment-d3','topic':T,'domain':DOM,'discipline':DIS,
   'stem':'Which two opioids should be avoided in frail older patients due to renally-cleared active metabolites?',
   'answer':'Meperidine (accumulates normeperidine: pro-convulsant, anticholinergic) and morphine (accumulates M6G/M3G); fentanyl is preferred',
   'rationale':'Reduced renal clearance in frail/older patients leads to toxic metabolite accumulation causing delirium, seizures, and respiratory depression.',
   'bloom':'apply','source':[{'book':'Miller/Baby Miller','page':675}],'confusable_with':'fentanyl (no active metabolites, safe in renal impairment)'},
  {'id':'frailty-assessment-d4','topic':T,'domain':DOM,'discipline':DIS,
   'stem':'What mnemonic organises the domains of the Comprehensive Geriatric Assessment (CGA)?',
   'answer':'The Geriatric 5Ms: Mind, Mobility, Medications, Matters most, Multicomplexity',
   'rationale':'The 5Ms framework ensures systematic identification of medical and psychosocial factors causing functional limitations.',
   'bloom':'recall','source':[{'book':'MGH Housestaff Manual','page':170}],'confusable_with':''},
  {'id':'frailty-assessment-d5','topic':T,'domain':DOM,'discipline':DIS,
   'stem':'What single prognostic question should trigger a serious illness conversation about goals of care?',
   'answer':'"Would I be surprised if this patient died in the next year?" -- if not surprised, initiate goals-of-care discussion',
   'rationale':'The surprise question is a validated, practical tool to prompt timely advance care planning before crisis.',
   'bloom':'apply','source':[{'book':'MGH Housestaff Manual','page':166}],'confusable_with':''},
  {'id':'frailty-assessment-d6','topic':T,'domain':DOM,'discipline':DIS,
   'stem':'The Mini-Cog screen comprises which two elements, and what score suggests possible cognitive impairment?',
   'answer':'3-item recall plus clock draw test; score 0-2 out of 5 suggests possible dementia',
   'rationale':'Mini-Cog is brief, validated, and less education-biased than MMSE, making it practical for perioperative cognitive screening.',
   'bloom':'recall','source':[{'book':'Morgan & Mikhail','page':1494}],'confusable_with':'MMSE (longer, more education-sensitive)'},
  {'id':'frailty-assessment-d7','topic':T,'domain':DOM,'discipline':DIS,
   'stem':'In LVAD candidacy evaluation, what frailty tool has been prospectively validated to predict post-implant outcomes?',
   'answer':'Fried frailty criteria; prospective assessment predicts similar mortality risk across INTERMACS profiles',
   'rationale':'Frailty independently predicts LVAD outcomes beyond INTERMACS profile, supporting its routine use in advanced HF evaluation.',
   'bloom':'apply','source':[{'book':'Society Guideline: Guideline   ACC AHA 2022 Heart Failure','page':135}],'confusable_with':''},
  {'id':'frailty-assessment-d8','topic':T,'domain':DOM,'discipline':DIS,
   'stem':'When should serious illness conversations be proactively initiated in a patient with progressive disease?',
   'answer':'Early in disease course as outpatient, or when: new/progressive serious illness (e.g., advanced cancer, ESRD, ESLD, HF, COPD), increasing hospitalisations, or intolerance of guideline-directed therapies',
   'rationale':'Early goals-of-care discussions improve care alignment, reduce unwanted aggressive end-of-life treatment, and improve quality of life.',
   'bloom':'apply','source':[{'book':'MGH Housestaff Manual','page':166}],'confusable_with':''},
]
kps.append({'_type':'illness_script','topic':T,'discipline':DIS,
  'enabling_conditions':'Age >70, multiple chronic diseases, malnutrition, sedentary lifestyle',
  'pathophysiology':'Cumulative depletion of physiological reserves across multiple organ systems; chronic inflammation, anorexia, and inactivity create a self-reinforcing cycle',
  'time_course':'Gradual onset over years; may be accelerated by acute hospitalisation (deconditioning)',
  'key_features':'Weight loss, exhaustion, weakness, slowness, low activity; distinct from disability and comorbidity',
  'consequence_if_missed':'Undertriage of perioperative risk; failure to engage goals of care; accelerated deconditioning during hospitalisation'})

# ── [133] Functional decline, mobility & rehabilitation ───────────────────────
T = 'Functional decline, mobility & rehabilitation in hospitalized older adults'
kps += [
  {'id':'functional-decline-mobility-d1','topic':T,'domain':DOM,'discipline':DIS,
   'stem':'Why is delirium superimposed on dementia (DSD) frequently missed in hospitalised older adults?',
   'answer':'Hypoactive DSD mimics baseline dementia; a coordinated interprofessional approach is required; underdiagnosis costs $38-152 billion annually in the US',
   'rationale':'Lack of proper evaluation and the expectation that older patients with dementia are "always confused" leads to systematic underrecognition.',
   'bloom':'analyze','source':[{'book':'StatPearls: StatPearls   Delirium  Diagnosis, Subtypes & Assessment','page':8}],'confusable_with':'dementia exacerbation (chronic change vs acute-on-chronic)'},
  {'id':'functional-decline-mobility-d2','topic':T,'domain':DOM,'discipline':DIS,
   'stem':'What three patient factors independently predict need for post-acute (skilled nursing) care after hospitalisation?',
   'answer':'Living alone, impaired mobility, and depression; also comorbidity burden',
   'rationale':'These factors predict inability to safely perform ADLs at home and guide discharge planning to appropriate post-acute level of care.',
   'bloom':'recall','source':[{'book':'MGH Housestaff Manual','page':271}],'confusable_with':''},
  {'id':'functional-decline-mobility-d3','topic':T,'domain':DOM,'discipline':DIS,
   'stem':'What important limitation of skilled nursing facilities must clinicians communicate when planning post-acute discharge?',
   'answer':'SNFs cannot perform rapid diagnostics (e.g., CT scanning) and are the largest source of Medicare regional cost variation and readmission risk',
   'rationale':'Patients discharged to SNF need monitoring contingencies and clear return-to-ED criteria because of limited on-site diagnostic capability.',
   'bloom':'apply','source':[{'book':'MGH Housestaff Manual','page':271}],'confusable_with':''},
  {'id':'functional-decline-mobility-d4','topic':T,'domain':DOM,'discipline':DIS,
   'stem':'For hospitalised HF patients, what do RCTs of exercise training show regarding mortality and hospitalisation?',
   'answer':'Modest reductions in all-cause mortality and hospitalisation rates that were borderline significant on primary analysis, with reductions in CV mortality or HF hospitalisations after prespecified adjustment',
   'rationale':'Even modest exercise reduces maladaptive cardiac remodelling and deconditioning, supporting early mobility protocols in HF.',
   'bloom':'apply','source':[{'book':'Society Guideline: Guideline   ACC AHA 2022 Heart Failure','page':39}],'confusable_with':''},
  {'id':'functional-decline-mobility-d5','topic':T,'domain':DOM,'discipline':DIS,
   'stem':'Cerebral amyloid angiopathy (CAA) predominantly affects which vascular compartment, and what is its main acute complication in older adults?',
   'answer':'CAA affects small cortical and leptomeningeal vessels (amyloid-beta deposition); main acute complication is lobar intracerebral haemorrhage',
   'rationale':'CAA weakens vessel walls leading to spontaneous lobar bleeds, which must be distinguished from hypertensive deep haemorrhages in older patients with functional decline.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Cerebral Amyloid Angiopathy (CAA)','page':1}],'confusable_with':'hypertensive intracerebral haemorrhage (deep basal ganglia/thalamus vs lobar location)'},
  {'id':'functional-decline-mobility-d6','topic':T,'domain':DOM,'discipline':DIS,
   'stem':'KDIGO 2024 recommends what protein intake target for CKD G3-G5 patients to balance nutrition with slowing progression?',
   'answer':'0.8 g/kg/day; avoid >1.3 g/kg/day in patients at risk of CKD progression',
   'rationale':'Excess protein increases glomerular hyperfiltration; severe restriction risks malnutrition and functional decline in older CKD patients.',
   'bloom':'recall','source':[{'book':'Society Guideline: Guideline   KDIGO 2024 CKD','page':93}],'confusable_with':''},
  {'id':'functional-decline-mobility-d7','topic':T,'domain':DOM,'discipline':DIS,
   'stem':'An older inpatient with frailty has a hospital course complicated by deconditioning. Which opioid analgesic is preferred and why?',
   'answer':'Fentanyl; no active metabolites, no significant renal accumulation, and fewer pharmacokinetic concerns in older patients',
   'rationale':'Avoiding renally-cleared active metabolites (meperidine/morphine) reduces delirium risk and supports early mobility and rehabilitation.',
   'bloom':'apply','source':[{'book':'Miller/Baby Miller','page':675}],'confusable_with':'meperidine (anticholinergic, normeperidine accumulation -> delirium)'},
]

# ── [134] Gestational Diabetes ────────────────────────────────────────────────
T = 'Gestational Diabetes & Diabetes in Pregnancy'
DOM2 = ('Internal medicine: endocrinology (diabetes & inpatient glucose, DKA & HHS, thyroid disorders & '
        'storm, adrenal insufficiency, calcium disorders, pituitary)')
kps += [
  {'id':'gestational-diabetes-d1','topic':T,'domain':DOM2,'discipline':DIS,
   'stem':'Obesity in pregnancy is independently associated with increased risk of which four obstetric complications?',
   'answer':'Gestational hypertension, preeclampsia, gestational diabetes mellitus, and delivery of large-for-gestational-age infants',
   'rationale':'Obesity-driven insulin resistance and systemic inflammation amplify all placental-mediated pregnancy complications.',
   'bloom':'recall','source':[{'book':'Morgan & Mikhail','page':1387}],'confusable_with':''},
  {'id':'gestational-diabetes-d2','topic':T,'domain':DOM2,'discipline':DIS,
   'stem':'Classic symptoms of hyperglycaemia in newly diagnosed diabetes include which four features, and what does polyuria reflect?',
   'answer':'Polyuria (osmotic diuresis), polydipsia, weight loss, blurred vision; polyuria reflects glucose exceeding renal threshold causing water diuresis',
   'rationale':'Each symptom reflects downstream consequences of insulin deficiency and hyperglycaemia.',
   'bloom':'recall','source':[{'book':'Miller/Baby Miller','page':546}],'confusable_with':''},
  {'id':'gestational-diabetes-d3','topic':T,'domain':DOM2,'discipline':DIS,
   'stem':'The ADA recommends diabetes screening starting at what age in asymptomatic adults, and how often is it repeated if normal?',
   'answer':'Age >= 35; repeat every 3 years if normal; annually if pre-diabetes; earlier/more frequent with risk factors',
   'rationale':'Risk-stratified screening captures the rising prevalence of T2DM in younger adults and the disproportionate burden in high-risk groups.',
   'bloom':'recall','source':[{'book':'MGH Housestaff Manual','page':181}],'confusable_with':''},
  {'id':'gestational-diabetes-d4','topic':T,'domain':DOM2,'discipline':DIS,
   'stem':'Multiple gestation carries increased risk of gestational diabetes in addition to which other major complications?',
   'answer':'Preterm labour, hypertensive disorders, hyperemesis gravidarum, anaemia, PPROM, IUGR, and intrauterine fetal demise',
   'rationale':'Amplified placental mass and hormone production in multiple gestations increase insulin resistance and all placenta-mediated risks.',
   'bloom':'recall','source':[{'book':'Miller/Baby Miller','page':619}],'confusable_with':''},
  {'id':'gestational-diabetes-d5','topic':T,'domain':DOM2,'discipline':DIS,
   'stem':'What enzyme causes gestational arginine vasopressin disorder (gestational DI), and in what trimester does it present?',
   'answer':'Cysteine aminopeptidase (vasopressinase) secreted by the fetus degrades AVP; presents in the third trimester',
   'rationale':'Vasopressinase activity exceeds the capacity to synthesise AVP, creating transient central-type DI that resolves 2-3 weeks postpartum.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Diabetes Insipidus (DI)','page':9}],'confusable_with':'central DI (pituitary origin, not vasopressinase-mediated)'},
  {'id':'gestational-diabetes-d6','topic':T,'domain':DOM2,'discipline':DIS,
   'stem':'Why is gestational AVP disorder often under-diagnosed during pregnancy?',
   'answer':'Polyuria during pregnancy is considered normal and does not generally cause complications, so the diagnosis is frequently overlooked',
   'rationale':'Physiological polyuria of pregnancy masks pathological AVP-deficient polyuria, requiring a high index of suspicion.',
   'bloom':'analyze','source':[{'book':'StatPearls: StatPearls   Diabetes Insipidus (DI)','page':9}],'confusable_with':''},
  {'id':'gestational-diabetes-d7','topic':T,'domain':DOM2,'discipline':DIS,
   'stem':'In obstetric anesthesia, what communication failure is a leading driver of malpractice payments against anesthesiologists?',
   'answer':'Delays in care and miscommunication about the urgency level (category) of cesarean delivery',
   'rationale':'Failure to convey urgency category (I-IV) delays time-to-incision and can result in preventable fetal and maternal harm.',
   'bloom':'apply','source':[{'book':'Morgan & Mikhail','page':1387}],'confusable_with':''},
]
kps.append({'_type':'illness_script','topic':T,'discipline':DIS,
  'enabling_conditions':'Obesity, prior GDM, family history T2DM, PCOS, multiple gestation, advanced maternal age',
  'pathophysiology':'Placental hormones (hPL, progesterone, cortisol) cause insulin resistance exceeding pancreatic compensatory capacity',
  'time_course':'Diagnosed at 24-28 weeks with OGTT; resolves postpartum; 50% develop T2DM within 10 years',
  'key_features':'Hyperglycaemia on screening, often asymptomatic mother, macrosomia/polyhydramnios on ultrasound',
  'consequence_if_missed':'Macrosomia, shoulder dystocia, neonatal hypoglycaemia, stillbirth; long-term maternal T2DM'})

print(f'Batch 1 KPs: {len(kps)}')
with open('data/_part4_batch1.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print('Batch 1 written OK')
