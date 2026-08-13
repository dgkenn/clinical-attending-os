
import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('data/kp_redeep_part11a_partial.json', 'r', encoding='utf-8') as f:
    output = json.load(f)

# ============================================================
# ITEM 371: Coronary Artery Disease in Special Populations
# ============================================================
topic = "Coronary Artery Disease in Special Populations"
domain = "Internal medicine: cardiology (ACS, stable & unstable angina, heart failure, brady/tachyarrhythmias, valvular disease, hypertension & emergencies, lipids, syncope)"
discipline = "medicine"

kps = [
  {"id":"cad-special-pops-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"In AF with moderate-severe rheumatic mitral stenosis or mechanical heart valves, which anticoagulant is preferred and why?",
   "answer":"Warfarin with INR target 2-3 is preferred; DOACs are not recommended in moderate-severe rheumatic mitral stenosis or mechanical heart valves.",
   "rationale":"Randomized trials demonstrated DOAC inferiority versus warfarin in these settings; bleeding risk increases substantially when INR exceeds 4.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   ACC AHA 2023 Atrial Fibrillation","page":33}],
   "confusable_with":"non-valvular AF (DOACs are preferred first-line)"},

  {"id":"cad-special-pops-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Meta-analyses of aspirin in CKD patients show what relative risk reduction for cardiovascular events?",
   "answer":"Aspirin provides consistent RR reduction (RR 1.35; 95% CI 1.10-1.65) for cardiovascular events in CKD, similar to the general population.",
   "rationale":"CKD patients have high baseline cardiovascular risk; despite increased bleeding risk, the absolute benefit of aspirin may remain substantial in high-risk individuals.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":123}],
   "confusable_with":""},

  {"id":"cad-special-pops-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What is the purpose of preoperative cardiac evaluation in a patient scheduled for elective surgery with suspected CAD?",
   "answer":"To identify patients whose outcomes will likely improve with specific medical treatment; rarely may require rescheduling surgery for cardiac optimization.",
   "rationale":"Perioperative myocardial ischemia significantly increases morbidity and mortality; risk stratification guides perioperative management decisions.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":476}],
   "confusable_with":""},

  {"id":"cad-special-pops-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Patients with severe pulmonary hypertension face what specific cardiac risk during anesthesia induction?",
   "answer":"Patients with severe PH are at risk for cardiac arrest during induction of anesthesia; emergent cardiopulmonary bypass may be required.",
   "rationale":"Anesthetic induction causes vasodilation and myocardial depression; in severe PH, acute RV failure and hemodynamic collapse can be precipitous.",
   "bloom":"apply",
   "source":[{"book":"Miller/Baby Miller","page":692}],
   "confusable_with":""},

  {"id":"cad-special-pops-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"In surgical patients with preexisting cardiovascular disease, which diagnoses most commonly arise?",
   "answer":"Arrhythmias, stroke, and thromboembolism are the most common diagnoses in surgical patients with preexisting cardiovascular disease.",
   "rationale":"Surgery triggers a hypercoagulable, sympathetically activated state that precipitates thrombotic and arrhythmic complications in vulnerable patients.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":618}],
   "confusable_with":""},

  {"id":"cad-special-pops-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Why is it nearly universal for a patient with carotid stenosis to also have coronary and peripheral arterial disease?",
   "answer":"Atherosclerosis is a systemic disease; carotid stenosis indicates generalized atherosclerotic involvement with greatly increased risk of coexisting CAD and PAD.",
   "rationale":"Shared risk factors (HTN, dyslipidemia, diabetes, smoking) produce simultaneous plaque development in multiple vascular beds.",
   "bloom":"analyze",
   "source":[{"book":"Morgan & Mikhail","page":960}],
   "confusable_with":""},

  {"id":"cad-special-pops-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"LV ejection fraction impacts what specific AF management decisions?",
   "answer":"LVEF impacts decisions for antiarrhythmic drug therapy and whether to prioritize other rhythm control therapies including catheter ablation.",
   "rationale":"Some antiarrhythmics (flecainide, propafenone) are contraindicated in structural heart disease; reduced EF may favor catheter ablation over drug therapy.",
   "bloom":"apply",
   "source":[{"book":"Society Guideline: Guideline   ACC AHA 2023 Atrial Fibrillation","page":23}],
   "confusable_with":""},
]
output.extend(kps)

# ============================================================
# ITEM 372: Crohn's Disease: Medical Management
# ============================================================
topic = "Crohn's Disease: Medical Management"
domain = "Internal medicine: gastroenterology & hepatology (upper & lower GI bleed, acute liver failure, cirrhosis & its complications, pancreatitis, IBD, bowel obstruction, hepatic encephalopathy)"
discipline = "medicine"

kps = [
  {"id":"crohns-medical-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What approach replaced step-up therapy in Crohn's disease and what guides current treatment selection?",
   "answer":"Risk-factor-based, prognosis-guided therapy (not step-up) is now standard; treatment selection is guided by poor prognostic factors and disease phenotype.",
   "rationale":"Early effective therapy with biologics in high-risk patients prevents complications and surgery better than sequential step-up escalation.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":82}],
   "confusable_with":"ulcerative colitis (similar shift; but UC step-down more common)"},

  {"id":"crohns-medical-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Which features identify poor prognosis in Crohn's disease warranting early aggressive therapy?",
   "answer":"Young age at diagnosis, extensive bowel involvement, ileal/ileocolonic disease, perianal/severe rectal disease, and deep ulceration are poor prognostic factors.",
   "rationale":"These features predict rapid progression to stricturing/penetrating disease, surgical complications, and disability without early immunosuppression.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":82}],
   "confusable_with":""},

  {"id":"crohns-medical-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"How does Crohn's disease cause bowel obstruction, and how does this mechanism differ from adhesive SBO?",
   "answer":"Crohn's disease causes obstruction via fibrotic or inflammatory strictures from transmural inflammation; adhesive SBO results from fibrous bands from prior surgery or inflammation.",
   "rationale":"Crohn's strictures may respond to anti-inflammatory therapy if inflammatory, or require dilation/surgery if fibrotic.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Bowel Obstruction","page":14}],
   "confusable_with":"adhesive SBO (most common cause; no primary bowel inflammation)"},

  {"id":"crohns-medical-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What distinguishes Crohn's disease from ulcerative colitis in terms of GI distribution and depth of inflammation?",
   "answer":"Crohn's disease can involve any part of the GI tract with skip lesions and transmural inflammation; UC has continuous mucosal involvement limited to the colon.",
   "rationale":"Transmural Crohn's inflammation explains its unique complications (fistula, abscess, stricture) not seen in UC's mucosal-limited disease.",
   "bloom":"recall",
   "source":[{"book":"Miller/Baby Miller","page":543}],
   "confusable_with":"ulcerative colitis (continuous, mucosal only, colon-limited)"},

  {"id":"crohns-medical-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What initial evaluation should accompany workup for IBD to exclude infectious mimics?",
   "answer":"Microbiologic studies for bacterial infection and parasitic infestation should be included in the initial evaluation, as infections can produce findings indistinguishable from IBD.",
   "rationale":"Treating infectious colitis (Salmonella, Campylobacter, C. diff, Entamoeba) with immunosuppression without ruling out infection is dangerous.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Ulcerative Colitis  Diagnosis & Classification","page":4}],
   "confusable_with":"C. difficile colitis (especially in hospitalized patients on antibiotics)"},

  {"id":"crohns-medical-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Crohn's disease appears in the differential of what upper GI condition beyond IBD of the colon?",
   "answer":"Crohn's disease is a cause of upper GI ulcers/dyspepsia, appearing in the differential alongside H. pylori, NSAIDs, Zollinger-Ellison syndrome, CMV/HSV, sarcoidosis, and bisphosphonates.",
   "rationale":"Crohn's granulomatous transmural inflammation can affect the esophagus, stomach, and duodenum, mimicking peptic ulcer disease.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":73}],
   "confusable_with":"H. pylori PUD (most common cause; test and treat first)"},

  {"id":"crohns-medical-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Patients with inflammatory bowel disease may also present with low back pain; what makes this pattern different from other spondyloarthropathies?",
   "answer":"In IBD-associated spondyloarthropathy, extraspinal manifestations (GI symptoms, uveitis, skin lesions) are usually more prominent than the back pain itself.",
   "rationale":"IBD-associated spondylitis is a seronegative spondyloarthropathy linked to HLA-B27; anti-TNF therapy may treat both IBD and joint disease.",
   "bloom":"analyze",
   "source":[{"book":"Morgan & Mikhail","page":1745}],
   "confusable_with":"primary ankylosing spondylitis (axial disease dominant; extraspinal less prominent)"},
]
output.extend(kps)

# ============================================================
# ITEM 373: Depression & anxiety screening in primary care & inpatients
# ============================================================
topic = "Depression & anxiety screening in primary care & inpatients"
domain = "General internal medicine, preventive care & geriatrics (admission & cross-cover problems, perioperative medicine, screening & vaccination, polypharmacy & deprescribing, frailty, delirium prevention, goals of care)"
discipline = "medicine"

kps = [
  {"id":"depression-anxiety-screening-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"USPSTF recommends universal depression screening for which specific populations in primary care?",
   "answer":"Universal screening of all adult primary care patients including pregnant and postpartum women (USPSTF Grade B).",
   "rationale":"Perinatal depression is common, often underdiagnosed, and has significant consequences for mother and infant; universal screening improves detection and treatment.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":210}],
   "confusable_with":""},

  {"id":"depression-anxiety-screening-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What validated two-step screening process is recommended for MDD in primary care?",
   "answer":"PHQ-2 for initial screening; if positive, complete with PHQ-9 for severity assessment and diagnostic confirmation.",
   "rationale":"PHQ-2 has high sensitivity; PHQ-9 provides dimensional severity scoring (0-27) that guides treatment selection and intensity.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":210}],
   "confusable_with":"GAD-7 (anxiety screening; used for GAD, not MDD)"},

  {"id":"depression-anxiety-screening-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What is the US lifetime prevalence of MDD and its sex distribution?",
   "answer":"US lifetime prevalence of MDD is approximately 20%; it is more common in women than men.",
   "rationale":"Hormonal factors, higher rates of interpersonal trauma, and reporting differences contribute to the greater female prevalence of MDD.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":210}],
   "confusable_with":""},

  {"id":"depression-anxiety-screening-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"GAD has a US lifetime prevalence of 8% and is more common in women. What comorbid psychiatric conditions coexist in 90% of GAD patients?",
   "answer":"90% of GAD patients meet criteria for at least one comorbid condition: MDD, dysthymia, alcohol use disorder, simple phobia, or social anxiety.",
   "rationale":"Anxiety disorders rarely occur in isolation; comorbid depression and substance use are the most clinically important and require assessment.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":211}],
   "confusable_with":"panic disorder (episodic acute anxiety; distinct from GAD chronic generalized worry)"},

  {"id":"depression-anxiety-screening-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What is the definition of chronic insomnia and how common is insomnia in the general population?",
   "answer":"Chronic insomnia is defined as difficulty initiating or maintaining sleep for >3 months with compromised daytime function; 35-50% of the population is affected.",
   "rationale":"Insomnia has bidirectional relationships with depression and anxiety; its assessment is integral to mental health screening in primary care.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":225}],
   "confusable_with":""},

  {"id":"depression-anxiety-screening-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"In sepsis patients at high risk of multi-organ failure and death, what clinical discussion does SCCM Surviving Sepsis Campaign require?",
   "answer":"A discussion of goals of care and prognosis is essential; patients may accept all treatments or prefer limitations depending on prognosis, invasiveness, and quality of life predictions.",
   "rationale":"Shared decision-making in critical illness respects patient autonomy and aligns care with patient values, especially when prognosis is poor.",
   "bloom":"apply",
   "source":[{"book":"Society Guideline","page":49}],
   "confusable_with":""},

  {"id":"depression-anxiety-screening-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What structured handoff process does the Surviving Sepsis Campaign recommend at care transitions?",
   "answer":"The SSC recommends structured handoff processes at transitions of care; no single tool is specifically recommended over another for sepsis.",
   "rationale":"Care transitions are high-risk periods for information loss; structured handoffs reduce errors and improve continuity for complex sepsis patients.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline","page":52}],
   "confusable_with":""},
]
output.extend(kps)

# ============================================================
# ITEM 374: Dialysis: Peritoneal Dialysis
# ============================================================
topic = "Dialysis: Peritoneal Dialysis"
domain = "Internal medicine: nephrology, fluids & electrolytes"
discipline = "medicine"

kps = [
  {"id":"peritoneal-dialysis-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Below what GFR level are patients dependent on RRT for survival?",
   "answer":"GFR <10 mL/min requires RRT (hemodialysis, hemofiltration, or peritoneal dialysis) for survival.",
   "rationale":"Below GFR 10, residual kidney function cannot maintain adequate uremic toxin clearance and fluid balance to sustain life.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1107}],
   "confusable_with":"CKD stage 5 (GFR <15; dialysis may be initiated at 10-15 based on symptoms)"},

  {"id":"peritoneal-dialysis-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What are the two fundamental solute clearance mechanisms in dialysis?",
   "answer":"Diffusion drives small molecule clearance (urea, creatinine) via concentration gradient; convection removes medium-weight molecules via hydrostatic pressure (ultrafiltration).",
   "rationale":"These mechanisms explain why HD excels at small solute removal and why convective therapies (HF, PD) offer advantages for middle molecules.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":103}],
   "confusable_with":"osmosis (osmotic gradient-driven; not the primary dialysis clearance mechanism)"},

  {"id":"peritoneal-dialysis-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"How does hemodialysis compare to peritoneal dialysis in effectiveness?",
   "answer":"Hemodialysis is more effective than peritoneal dialysis; HD is readily accomplished via temporary internal jugular, subclavian, or femoral catheter in acute settings.",
   "rationale":"HD achieves higher clearance rates and faster fluid removal; PD offers continuous gradual clearance, hemodynamic stability, and home-based therapy.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1112}],
   "confusable_with":"CRRT (continuous RRT; slower than intermittent HD but better hemodynamic tolerance)"},

  {"id":"peritoneal-dialysis-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What bone complication results from secondary hyperparathyroidism in CKD/dialysis patients?",
   "answer":"Secondary hyperparathyroidism in CKD produces renal osteodystrophy (metabolic bone disease), predisposing patients to fractures.",
   "rationale":"Reduced vitamin D activation and hyperphosphatemia in CKD stimulate sustained PTH release, driving bone resorption and impaired mineralization.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1112}],
   "confusable_with":"primary hyperparathyroidism (hypercalcemia predominates; not hypocalcemia)"},

  {"id":"peritoneal-dialysis-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What clinically important phase follows oliguria in intrinsic AKI recovery and what complication can it produce?",
   "answer":"The diuretic phase follows oliguria and often produces very large urinary outputs; this can cause hypovolemia and electrolyte losses (hyponatremia, hypokalemia, hypophosphatemia).",
   "rationale":"Tubular recovery restores GFR before concentrating ability returns; massive diuresis requires careful fluid/electrolyte replacement.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1107}],
   "confusable_with":"diabetes insipidus (also polyuric but from ADH deficiency/resistance)"},

  {"id":"peritoneal-dialysis-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"At what CKD stage should discussions about RRT options (transplantation, PD, HD, conservative management) begin?",
   "answer":"RRT option discussions should begin at CKD stage 5 (GFR 10-15 mL/min) to allow timely access placement, transplant evaluation, and informed decision-making.",
   "rationale":"Early education and preparation prevents emergency dialysis initiation and allows elective, appropriate modality selection.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Dialysis  CRRT in the ICU","page":3}],
   "confusable_with":""},

  {"id":"peritoneal-dialysis-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What lipid abnormality is most common in CKD and dialysis patients and why does it occur?",
   "answer":"Hypertriglyceridemia is the predominant dyslipidemia in CKD; it results from impaired lipoprotein lipase activity and increased VLDL production.",
   "rationale":"CKD reduces lipoprotein lipase and hepatic lipase activity, impairing triglyceride-rich lipoprotein clearance and raising cardiovascular risk.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1112}],
   "confusable_with":""},
]
output.extend(kps)

# ============================================================
# ITEM 375: Dilated Cardiomyopathy
# ============================================================
topic = "Dilated Cardiomyopathy"
domain = "Internal medicine: cardiology (ACS, stable & unstable angina, heart failure, brady/tachyarrhythmias, valvular disease, hypertension & emergencies, lipids, syncope)"
discipline = "medicine"

kps = [
  {"id":"dilated-cardiomyopathy-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Cardiac muscle degeneration is common in muscular dystrophy but develops into DCM or HCM in what proportion of patients?",
   "answer":"Only 10% of muscular dystrophy patients develop dilated or hypertrophic cardiomyopathy despite common cardiac muscle degeneration.",
   "rationale":"Dystrophin deficiency causes cardiomyocyte membrane instability, but cardiac involvement is less universal than skeletal muscle disease.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1024}],
   "confusable_with":""},

  {"id":"dilated-cardiomyopathy-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What temporal trend in peripartum cardiomyopathy has been documented in US nationwide data?",
   "answer":"Increasing incidence of peripartum cardiomyopathy has been documented in US nationwide population-based studies.",
   "rationale":"PPCM incidence correlates with rising rates of advanced maternal age and multiple gestation; outcomes are tracked to improve management.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   ACC AHA 2022 Heart Failure","page":145}],
   "confusable_with":"pre-existing cardiomyopathy worsening in pregnancy (different entity)"},

  {"id":"dilated-cardiomyopathy-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What does family history assessment contribute to the workup of newly diagnosed heart failure?",
   "answer":"Family history identifies possible inherited cardiomyopathy; specific conditions like familial ATTR amyloidosis or genetic DCM require disease-specific therapy and family screening.",
   "rationale":"Approximately 25-35% of DCM cases have identifiable genetic mutations (LMNA, TTN, MYH7); genetic cardiomyopathies require family cascade testing.",
   "bloom":"apply",
   "source":[{"book":"Society Guideline: Guideline   ACC AHA 2022 Heart Failure","page":18}],
   "confusable_with":""},

  {"id":"dilated-cardiomyopathy-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"When should echocardiography be repeated in a patient with known dilated cardiomyopathy?",
   "answer":"Repeat echocardiography only when there is concern for clinical or functional change; routine periodic repeat imaging without clinical indication is not recommended.",
   "rationale":"Repeat imaging without clinical change adds cost without diagnostic yield; clinical decompensation or new symptoms justify reassessment.",
   "bloom":"apply",
   "source":[{"book":"MGH Housestaff Manual","page":25}],
   "confusable_with":""},

  {"id":"dilated-cardiomyopathy-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Androgen deprivation therapy agents (goserelin, leuprolide, anti-androgens) are associated with what cardiac risk?",
   "answer":"ADT is associated with cardiomyopathy and heart failure; this is tracked as a treatment-related cause of DCM in ACC/AHA HF guidelines.",
   "rationale":"ADT causes metabolic syndrome, dyslipidemia, and direct myocardial effects, increasing heart failure risk in prostate cancer patients.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   ACC AHA 2022 Heart Failure","page":145}],
   "confusable_with":"anthracycline cardiomyopathy (cumulative dose-dependent; different mechanism)"},

  {"id":"dilated-cardiomyopathy-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What EF thresholds define HFrEF, HFmrEF, and HFpEF?",
   "answer":"HFrEF: EF ≤40%; HFmrEF (mid-range): EF 41-49%; HFpEF: EF ≥50%.",
   "rationale":"EF-based classification guides prognosis and therapy selection; HFrEF has the strongest evidence for mortality-reducing GDMT.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":25}],
   "confusable_with":""},

  {"id":"dilated-cardiomyopathy-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What connective tissue disorder has the highest incidence of mitral valve prolapse, and what is the pathological finding?",
   "answer":"Marfan syndrome has a high incidence of MVP; the pathological finding is myxomatous degeneration with redundancy of valve leaflets.",
   "rationale":"FBN1 mutation in Marfan syndrome weakens connective tissue in valve leaflets, leading to myxomatous change and prolapse.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":672}],
   "confusable_with":""},
]
output.extend(kps)

# ============================================================
# ITEM 376: Functional GI Disorders & IBS
# ============================================================
topic = "Functional GI Disorders & IBS"
domain = "Internal medicine: gastroenterology & hepatology (upper & lower GI bleed, acute liver failure, cirrhosis & its complications, pancreatitis, IBD, bowel obstruction, hepatic encephalopathy)"
discipline = "medicine"

kps = [
  {"id":"functional-gi-ibs-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What diagnoses must be excluded before making a functional GI disorder diagnosis in chronic abdominal pain?",
   "answer":"Chronic pancreatitis, IBD, mesenteric ischemia, adhesions, cancer, pelvic etiologies, anterior cutaneous nerve entrapment (ACNES), and myofascial pain must be excluded.",
   "rationale":"Functional GI disorders are diagnoses of exclusion; structural, inflammatory, vascular, and neuromuscular causes must be systematically ruled out.",
   "bloom":"analyze",
   "source":[{"book":"MGH Housestaff Manual","page":72}],
   "confusable_with":"IBS (functional; no structural pathology; Rome IV criteria required)"},

  {"id":"functional-gi-ibs-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What physical exam finding helps distinguish anterior cutaneous nerve entrapment from intraabdominal pathology in chronic abdominal pain?",
   "answer":"Positive Carnett sign (pain worsens with abdominal wall tensing) suggests anterior cutaneous nerve entrapment syndrome (ACNES) rather than visceral pathology.",
   "rationale":"In ACNES, pain originates in the abdominal wall nerve; tensing the wall increases palpation pain. Visceral pain decreases when the wall is tensed, shielding the organ.",
   "bloom":"apply",
   "source":[{"book":"MGH Housestaff Manual","page":72}],
   "confusable_with":""},

  {"id":"functional-gi-ibs-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"The McGill Pain Questionnaire defines pain in how many dimensions, and how does this differ from numerical rating scales?",
   "answer":"MPQ defines pain in three major dimensions: (1) sensory-discriminative, (2) motivational-affective, and (3) cognitive-evaluative; NRS/VAS are one-dimensional intensity scales.",
   "rationale":"Multidimensional pain assessment distinguishes nociceptive from neuropathic qualities, guiding more targeted treatment for functional GI disorders.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1730}],
   "confusable_with":"NRS/VAS (one-dimensional; measure intensity but not quality)"},

  {"id":"functional-gi-ibs-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Post-infectious IBS appears in the differential alongside what other diagnoses in the context of diarrheal illness?",
   "answer":"Post-infectious IBS appears alongside CDI, infectious diarrhea, IBD, microscopic colitis, and celiac disease in the differential of diarrhea.",
   "rationale":"Post-infectious IBS develops in approximately 10-15% of patients after acute gastroenteritis, from persistent gut motility and sensory dysregulation.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":124}],
   "confusable_with":"IBD (inflammatory; requires biopsies for diagnosis)"},

  {"id":"functional-gi-ibs-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Functional postoperative GI conditions that can mimic mechanical bowel obstruction include which two entities?",
   "answer":"Postoperative ileus (diffuse bowel dysmotility) and Ogilvie syndrome (acute colonic pseudo-obstruction) are functional conditions mimicking mechanical obstruction.",
   "rationale":"Distinguishing functional from mechanical obstruction is critical; functional conditions typically resolve without surgery while mechanical obstruction may require intervention.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Bowel Obstruction","page":14}],
   "confusable_with":"mechanical SBO (requires surgery if non-resolving; may need CT to distinguish)"},

  {"id":"functional-gi-ibs-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Lower GI bleeding (below the ligament of Treitz) classically presents with which symptoms, and what are the most common etiologies?",
   "answer":"BRBPR, hematochezia, diarrhea, and tenesmus; right colon bleeding may present as melena. Common causes: diverticular disease, polyps/tumor, colitis, vascular malformations.",
   "rationale":"Bleeding location within the colon determines presentation; right-sided blood has more transit time allowing partial digestion (melena-like appearance).",
   "bloom":"recall",
   "source":[{"book":"Intern Notes / Survival Guide","page":40}],
   "confusable_with":"upper GI bleeding (brisk UGIB can cause hematochezia; BUN/Cr ratio >20 suggests upper source)"},
]
output.extend(kps)

# Save partial output B
with open('data/kp_redeep_part11b_partial.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Part B done: {len(output)} items total")
