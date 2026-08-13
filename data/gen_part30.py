import json, sys

data = json.load(open('data/_kp_retrieval_full.json', encoding='utf-8'))
items = data[990:1023]

kps = []

# ── 990 Tuberculosis ──────────────────────────────────────────────────────────
kps += [
  {"id":"tuberculosis-1","topic":"Tuberculosis","domain":items[0]["domain"],"discipline":"medicine",
   "stem":"A patient with known pulmonary disease presents with massive hemoptysis. What conditions produce this?",
   "answer":"Hemoptysis etiologies include tuberculosis, bronchiectasis, neoplasm, biopsy complication, and historically pulmonary artery catheter balloon rupture.",
   "rationale":"TB causes cavitary disease with erosion into bronchial vessels, making it a classic cause of massive hemoptysis.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":916}],"confusable_with":"bronchiectasis"},
  {"id":"tuberculosis-2","topic":"Tuberculosis","domain":items[0]["domain"],"discipline":"medicine",
   "stem":"A patient presents with chronic back pain but is afebrile with normal leukocyte count. What infectious etiology must be considered?",
   "answer":"Spinal tuberculosis (Pott disease) can present with chronic back pain without fever or leukocytosis.",
   "rationale":"Mycobacterium tuberculosis causes vertebral osteomyelitis with an indolent course that often lacks systemic inflammatory signs.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1744}],"confusable_with":"pyogenic vertebral osteomyelitis (fever and leukocytosis typical)"},
  {"id":"tuberculosis-3","topic":"Tuberculosis","domain":items[0]["domain"],"discipline":"medicine",
   "stem":"A patient with a granulomatous lung disease is found to have hypercalcemia with suppressed PTH. What mechanism explains this?",
   "answer":"Granulomatous disorders (TB, sarcoidosis) cause PTH-independent hypercalcemia via extrarenal 1-alpha-hydroxylase activity producing excess 1,25-dihydroxyvitamin D.",
   "rationale":"Activated macrophages in granulomas convert 25-OH vitamin D to the active form independent of PTH regulation.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1889}],"confusable_with":"primary hyperparathyroidism (elevated PTH, not suppressed)"},
  {"id":"tuberculosis-4","topic":"Tuberculosis","domain":items[0]["domain"],"discipline":"medicine",
   "stem":"What class of immunological reaction underlies tuberculin skin test reactivity and TB granuloma formation?",
   "answer":"Type IV (delayed-type, T-cell mediated) hypersensitivity reaction.",
   "rationale":"Type IV reactions are mediated by sensitized T-lymphocytes and occur 48-72 hours after antigen exposure, producing granuloma formation in TB.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2033}],"confusable_with":"type III hypersensitivity (immune complex, causes serum sickness)"},
  {"id":"tuberculosis-5","topic":"Tuberculosis","domain":items[0]["domain"],"discipline":"medicine",
   "stem":"What infectious diseases pose occupational risk to OR and anesthesia personnel?",
   "answer":"Hospital workers are exposed to respiratory viral infections, rubella, tuberculosis, and SARS-CoV-2 from community and patient contact.",
   "rationale":"Aerosolizing airway procedures (intubation, bronchoscopy) place anesthesia providers at elevated risk for airborne pathogens including M. tuberculosis.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2043}],"confusable_with":""}
]
kps.append({"_type":"illness_script","topic":"Tuberculosis","discipline":"medicine",
  "enabling_conditions":"Immunocompromise (HIV, TNF inhibitors, malnutrition), endemic area or close-contact exposure, incarceration, healthcare work",
  "pathophysiology":"Mycobacterium tuberculosis infects macrophages, evades phagolysosomal killing; type IV hypersensitivity drives caseating granuloma formation and cavitation",
  "time_course":"Primary infection often asymptomatic; latent TB reactivates years to decades later; active disease progresses over weeks to months",
  "key_features":"Chronic cough, hemoptysis, night sweats, weight loss, fever; spinal TB presents as chronic back pain without fever; granulomatous hypercalcemia possible",
  "consequence_if_missed":"Progressive pulmonary destruction, dissemination (miliary TB, meningitis), transmission to contacts and OR personnel"})

# ── 991 Ulcerative Colitis ────────────────────────────────────────────────────
kps += [
  {"id":"ulcerative-colitis-1","topic":"Ulcerative Colitis: Medical & Surgical Management","domain":items[1]["domain"],"discipline":"medicine",
   "stem":"How do ulcerative colitis and Crohn disease differ in anatomic distribution and bowel-wall involvement?",
   "answer":"UC causes continuous mucosal inflammation confined to colon (rectum first); Crohn disease causes transmural, skip-lesion inflammation affecting any GI segment.",
   "rationale":"Transmural Crohn inflammation produces fistulas and strictures; UC is limited to mucosa/submucosa enabling total proctocolectomy as cure.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":543}],"confusable_with":"Crohn disease"},
  {"id":"ulcerative-colitis-2","topic":"Ulcerative Colitis: Medical & Surgical Management","domain":items[1]["domain"],"discipline":"medicine",
   "stem":"What diagnostic test confirms ulcerative colitis and what must be excluded first?",
   "answer":"Colonoscopy confirms UC; microbiologic studies for bacterial and parasitic infection must be included in the initial evaluation as these can produce indistinguishable findings.",
   "rationale":"Infectious colitis (e.g., C. difficile, Campylobacter) can mimic idiopathic UC; treating as IBD without excluding infection risks harm.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Ulcerative Colitis  Diagnosis & Classification","page":4}],"confusable_with":"infectious colitis"},
  {"id":"ulcerative-colitis-3","topic":"Ulcerative Colitis: Medical & Surgical Management","domain":items[1]["domain"],"discipline":"medicine",
   "stem":"What long-term cancer complication is associated with longstanding extensive ulcerative colitis?",
   "answer":"Patients with longstanding UC (especially pancolitis >8-10 years) have significantly increased risk of colorectal cancer requiring periodic colonoscopic surveillance.",
   "rationale":"Chronic mucosal inflammation drives dysplastic transformation; surveillance colonoscopy allows early detection.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Ulcerative Colitis  Diagnosis & Classification","page":4}],"confusable_with":""},
  {"id":"ulcerative-colitis-4","topic":"Ulcerative Colitis: Medical & Surgical Management","domain":items[1]["domain"],"discipline":"medicine",
   "stem":"What intraoperative triggers must be avoided to prevent vasoactive mediator release in patients with conditions like carcinoid or inflammatory bowel disease?",
   "answer":"Avoid anxiety, noxious stimuli, hypercapnia, and hypothermia intraoperatively, as all can stimulate vasoactive substance release.",
   "rationale":"Sympathetic activation and physiologic perturbations trigger mediator release (serotonin, histamine, prostaglandins) causing hemodynamic instability.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":554}],"confusable_with":""},
  {"id":"ulcerative-colitis-5","topic":"Ulcerative Colitis: Medical & Surgical Management","domain":items[1]["domain"],"discipline":"medicine",
   "stem":"What standard colonoscopy preparation sequence is used, and when should the prep begin?",
   "answer":"Patient starts clear liquids at noon the day prior; SUPREP 6 oz + 10 oz water then 32 oz water over one hour, repeated; prep starts no later than 6 PM.",
   "rationale":"Adequate preparation is essential for mucosal visualization; split-dose or evening-start regimens improve bowel cleanliness and tolerability.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":79}],"confusable_with":""}
]
kps.append({"_type":"illness_script","topic":"Ulcerative Colitis: Medical & Surgical Management","discipline":"medicine",
  "enabling_conditions":"Young adults 15-35 yr (bimodal peak 55-65 yr), genetic predisposition, Western diet, altered gut microbiome",
  "pathophysiology":"Aberrant mucosal immune response produces continuous superficial (mucosal/submucosal) colonic inflammation starting at rectum and extending proximally",
  "time_course":"Relapsing-remitting; flares of bloody diarrhea; colorectal cancer risk rises after 8-10 years pancolitis",
  "key_features":"Bloody diarrhea, urgency, tenesmus, cramping; continuous rectal-first involvement on colonoscopy; extraintestinal manifestations (arthritis, uveitis, PSC)",
  "consequence_if_missed":"Fulminant colitis, toxic megacolon, perforation; missed colorectal cancer without surveillance"})

# ── 992 Vaccination in adults ─────────────────────────────────────────────────
kps += [
  {"id":"vaccination-adults-1","topic":"Vaccination in adults","domain":items[2]["domain"],"discipline":"medicine",
   "stem":"What vaccine benefit has been demonstrated specifically in COPD patients?",
   "answer":"Influenza vaccination reduces serious illness such as lower respiratory tract infections requiring hospitalization and death in people with COPD; pneumococcal vaccine provides significant protection against community-acquired pneumonia.",
   "rationale":"COPD patients have impaired mucociliary clearance and FEV1 decline, making respiratory infections more severe; vaccines reduce hospitalization and mortality.",
   "bloom":"recall","source":[{"book":"Society Guideline: Guideline   GOLD 2024 COPD Full Report","page":57}],"confusable_with":""},
  {"id":"vaccination-adults-2","topic":"Vaccination in adults","domain":items[2]["domain"],"discipline":"medicine",
   "stem":"What is the recommended pneumococcal vaccination approach for adults who have never received a pneumococcal conjugate vaccine?",
   "answer":"PCV20 x1 alone OR PCV15 x1 followed by PPSV23 x1 at least 8 weeks to 1 year later.",
   "rationale":"Conjugate vaccines (PCV) produce stronger immune memory via T-cell-dependent responses; polysaccharide (PPSV23) broadens serotype coverage.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":219}],"confusable_with":"influenza vaccine schedule"},
  {"id":"vaccination-adults-3","topic":"Vaccination in adults","domain":items[2]["domain"],"discipline":"medicine",
   "stem":"What are the contraindications to live attenuated influenza vaccine (LAIV)?",
   "answer":"LAIV is contraindicated in pregnancy, immunocompromised patients and healthcare workers caring for them, and adults with significant comorbidities; it is approved only for healthy non-pregnant adults under age 49.",
   "rationale":"Live vaccines replicate in the host; immunocompromised patients risk disseminated infection and pregnant patients risk fetal harm.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Community Acquired Pneumonia (CAP)","page":6}],"confusable_with":"inactivated influenza vaccine (safe in pregnancy and immunocompromise)"},
  {"id":"vaccination-adults-4","topic":"Vaccination in adults","domain":items[2]["domain"],"discipline":"medicine",
   "stem":"What special populations require hepatitis A vaccination according to CDC guidance?",
   "answer":"Hepatitis A vaccine is indicated for travelers to endemic countries, HIV-infected persons, men who have sex with men, and persons with any drug use.",
   "rationale":"These populations have increased risk of fecal-oral transmission and are more likely to develop severe disease from HAV infection.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":219}],"confusable_with":"hepatitis B vaccine indications"},
  {"id":"vaccination-adults-5","topic":"Vaccination in adults","domain":items[2]["domain"],"discipline":"medicine",
   "stem":"What is the recommended COVID-19 vaccination approach for non-immunocompromised adults regardless of prior vaccination history?",
   "answer":"A single dose of the updated mRNA vaccine (e.g., 2023-24 formulation) is recommended for all non-immunocompromised adults regardless of prior vaccination history.",
   "rationale":"Annual updated mRNA vaccines target current circulating variants; prior immunity wanes over time, making annual revaccination necessary.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Community Acquired Pneumonia (CAP)","page":6}],"confusable_with":"immunocompromised adults (require additional doses)"}
]

# ── 993 Accreditation, Credentialing & Privileging ────────────────────────────
kps += [
  {"id":"accreditation-1","topic":"Accreditation, Credentialing & Privileging","domain":items[3]["domain"],"discipline":"medicine",
   "stem":"What US federal body drives many of the mandated policies carried out by healthcare facilities?",
   "answer":"The Centers for Medicare and Medicaid Services (CMS) drive many mandated policies and procedures carried out by facilities.",
   "rationale":"CMS conditions of participation are the regulatory foundation; accreditation bodies such as TJC and DNV GL act as CMS-approved surveyors.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":57}],"confusable_with":"The Joint Commission (TJC accredits but CMS sets the regulatory mandate)"},
  {"id":"accreditation-2","topic":"Accreditation, Credentialing & Privileging","domain":items[3]["domain"],"discipline":"medicine",
   "stem":"What do accreditation agencies examine and determine during facility review?",
   "answer":"Accreditation agencies examine processes and procedures and determine whether facilities have appropriate policies and whether those policies are actually followed.",
   "rationale":"Structure-process-outcome framework: accreditation focuses on process (policies) and structure (resources), aiming to improve outcomes through standardized practice.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":58}],"confusable_with":""},
  {"id":"accreditation-3","topic":"Accreditation, Credentialing & Privileging","domain":items[3]["domain"],"discipline":"medicine",
   "stem":"What accreditation requirements exist for anesthesia fellowship programs?",
   "answer":"Fellowship programs in Adult Cardiac Anesthesia, Critical Care Medicine, Pediatric Anesthesiology, Obstetric Anesthesiology, Regional Anesthesia/Acute Pain, Sleep Medicine, Palliative Care, and Chronic Pain have specific accreditation requirements.",
   "rationale":"Subspecialty accreditation ensures trainees achieve defined competencies beyond general residency training in complex or specialized domains.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":28}],"confusable_with":""},
  {"id":"accreditation-4","topic":"Accreditation, Credentialing & Privileging","domain":items[3]["domain"],"discipline":"medicine",
   "stem":"What is the role of accreditation in reducing healthcare disparities and fraudulent claims?",
   "answer":"Requirement of certification from an accrediting agency (TJC, DNV GL) helps reduce fraudulent claims and disparities in levels of care.",
   "rationale":"Standardized accreditation processes enforce minimum safety and quality thresholds across institutions, leveling care quality and enabling payer accountability.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":58}],"confusable_with":""}
]

# ── 994 Carcinoid tumors and neuroendocrine tumors ────────────────────────────
kps += [
  {"id":"carcinoid-net-1","topic":"Carcinoid tumors and neuroendocrine tumors","domain":items[4]["domain"],"discipline":"medicine",
   "stem":"Which functional neuroendocrine tumor types have direct implications for anesthetic management?",
   "answer":"Insulinomas, gastrinomas, VIPomas, and carcinoid tumors are functional NETs with anesthetic management implications.",
   "rationale":"These tumors secrete active hormones (insulin, gastrin, VIP, serotonin/histamine) that cause hemodynamic and metabolic crises if not managed perioperatively.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":553}],"confusable_with":"non-functional NETs (no hormonal symptoms)"},
  {"id":"carcinoid-net-2","topic":"Carcinoid tumors and neuroendocrine tumors","domain":items[4]["domain"],"discipline":"medicine",
   "stem":"What is the definitive treatment for localized pancreatic neuroendocrine tumors, and what is the role of surgery in metastatic disease?",
   "answer":"Surgical resection is the treatment of choice for localized pancreatic NETs; surgical debulking may be of benefit in metastatic disease.",
   "rationale":"Complete resection offers cure for localized disease; cytoreductive surgery in metastatic disease can reduce hormonal burden and may improve outcomes.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":553}],"confusable_with":""},
  {"id":"carcinoid-net-3","topic":"Carcinoid tumors and neuroendocrine tumors","domain":items[4]["domain"],"discipline":"medicine",
   "stem":"What is the preferred surgical approach for localized pulmonary carcinoid tumors without lymph node involvement?",
   "answer":"Lobectomy is the preferred surgical resection for localized pulmonary carcinoid tumors; pneumonectomy or bilobectomy may be needed for central lesions; segmentectomy/wedge resection may be considered for small peripheral tumors.",
   "rationale":"Adequate resection margins and lymph node sampling are critical in pulmonary NETs given malignant potential; anatomic resection (lobectomy) provides oncologic adequacy.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Carcinoid Tumors & Neuroendocrine Tumors (NETs)","page":12}],"confusable_with":""},
  {"id":"carcinoid-net-4","topic":"Carcinoid tumors and neuroendocrine tumors","domain":items[4]["domain"],"discipline":"medicine",
   "stem":"What intraoperative anesthetic goals minimize carcinoid crisis risk during surgery for carcinoid tumors?",
   "answer":"Minimize anxiety, noxious stimuli, hypercapnia, and hypothermia; hypotension may occur from mediator release; octreotide should be available.",
   "rationale":"Stimuli that activate the sympathetic system or alter physiology trigger serotonin and histamine release from carcinoid tumors, causing bronchospasm and hemodynamic instability.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":554}],"confusable_with":""},
  {"id":"carcinoid-net-5","topic":"Carcinoid tumors and neuroendocrine tumors","domain":items[4]["domain"],"discipline":"medicine",
   "stem":"What trend has been observed in the incidence of neuroendocrine tumors including pulmonary NETs in recent decades?",
   "answer":"The incidence of NETs including pulmonary NETs has demonstrated an upward trend in recent decades, attributable to advancements in medical investigations and improved detection rates.",
   "rationale":"Improved imaging (CT, MRI, PET) and pathology recognition have increased detection of NETs that were previously undiagnosed or misclassified.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Carcinoid Tumors & Neuroendocrine Tumors (NETs)","page":4}],"confusable_with":""}
]
kps.append({"_type":"illness_script","topic":"Carcinoid tumors and neuroendocrine tumors","discipline":"medicine",
  "enabling_conditions":"MEN-1 syndrome, sporadic mutation; women slightly more affected than men; pulmonary NETs often incidental",
  "pathophysiology":"Enterochromaffin cells secrete serotonin, histamine, and other vasoactive peptides; carcinoid syndrome (hepatic metastases allow systemic mediator circulation) causes flushing, diarrhea, bronchoconstriction, right heart valvulopathy",
  "time_course":"Indolent; carcinoid syndrome only emerges after hepatic metastases bypass first-pass hepatic metabolism",
  "key_features":"Episodic flushing, diarrhea, bronchoconstriction, carcinoid heart disease; intraoperative hemodynamic crises triggered by manipulation or stress",
  "consequence_if_missed":"Carcinoid crisis (severe bronchospasm, hemodynamic collapse) during surgery without octreotide prophylaxis"})

# ── 995 Clinician Wellness & Burnout Prevention ───────────────────────────────
kps += [
  {"id":"clinician-wellness-1","topic":"Clinician Wellness & Burnout Prevention","domain":items[5]["domain"],"discipline":"medicine",
   "stem":"What behavioral signs may indicate substance misuse in an anesthesia colleague?",
   "answer":"Signs include hostility, spending excess time at hospital when off duty, volunteering for extra calls, refusing relief, requesting frequent bathroom breaks, and signing out increasing or disproportionate amounts of opioids.",
   "rationale":"Substance use disorders in anesthesia providers are often masked by professional functioning; diversion behaviors (excessive opioid sign-outs) and avoidance of oversight are early warning signs.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":48}],"confusable_with":"burnout (different etiology and intervention required)"},
  {"id":"clinician-wellness-2","topic":"Clinician Wellness & Burnout Prevention","domain":items[5]["domain"],"discipline":"medicine",
   "stem":"What are the three basic psychological needs recognized as critical for life satisfaction and clinician well-being?",
   "answer":"Autonomy, competence, and relatedness (belonging) are the three basic psychological needs critical for life satisfaction and supporting well-being (self-determination theory).",
   "rationale":"Self-determination theory identifies these three needs as fundamental; their satisfaction supports intrinsic motivation and psychological health, while their frustration drives burnout.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":45}],"confusable_with":"Maslow's hierarchy (different framework)"},
  {"id":"clinician-wellness-3","topic":"Clinician Wellness & Burnout Prevention","domain":items[5]["domain"],"discipline":"medicine",
   "stem":"What effect has physician burnout been shown to have on patient safety?",
   "answer":"Residents at higher risk for burnout and depression reported more medication errors and mistakes with negative consequences for patients than residents with lesser risk.",
   "rationale":"Burnout impairs attention, decision-making, and empathy; emotional distress during training predicts future burnout as a practicing physician.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":44}],"confusable_with":""},
  {"id":"clinician-wellness-4","topic":"Clinician Wellness & Burnout Prevention","domain":items[5]["domain"],"discipline":"medicine",
   "stem":"What intervention has been shown in a randomized study to reduce physician burnout?",
   "answer":"A 6-month professional coaching intervention decreased overall burnout by 17.1% in the intervention group, while burnout in the control group did not decrease.",
   "rationale":"Coaching supports self-reflection, goal-setting, and coping skill development; unlike resilience-only approaches, coaching addresses both individual and systemic contributors.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":50}],"confusable_with":""},
  {"id":"clinician-wellness-5","topic":"Clinician Wellness & Burnout Prevention","domain":items[5]["domain"],"discipline":"medicine",
   "stem":"What are the cornerstones of self-care at the foundational level of the health professional wellness hierarchy?",
   "answer":"Adequate nutrition, hydration, exercise, and sleep are the cornerstones of self-care at the basics level of the health professional wellness hierarchy.",
   "rationale":"The wellness hierarchy places individual physiologic basics at the foundation; systems-level interventions are prioritized for sustainable improvement but individual self-care remains essential.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":49}],"confusable_with":""}
]

# ── 996 Closed Claims Analysis & Anesthesia Liability ─────────────────────────
kps += [
  {"id":"closed-claims-1","topic":"Closed Claims Analysis & Anesthesia Liability","domain":items[6]["domain"],"discipline":"anesthesia",
   "stem":"What trend was observed in pediatric anesthesia closed claims from 1973 to 2000 regarding death, brain damage, and respiratory events?",
   "answer":"A decrease in the proportion of claims for death and brain damage and a reduction in claims related to respiratory events were noted over the three decades.",
   "rationale":"Improvements in monitoring (pulse oximetry, capnography), equipment, and training progressively reduced the most severe anesthetic complications in pediatric patients.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2021}],"confusable_with":""},
  {"id":"closed-claims-2","topic":"Closed Claims Analysis & Anesthesia Liability","domain":items[6]["domain"],"discipline":"anesthesia",
   "stem":"What complication from central line placement most commonly led to a claim for patient death in closed claims analysis?",
   "answer":"Cardiac tamponade following central line placement often led to a claim for patient death; guidewire/catheter embolisms caused less severe injuries but were generally attributed to substandard care.",
   "rationale":"Tamponade requires immediate pericardiocentesis; delayed recognition during line placement (especially with stiff wires or long catheters) is often fatal.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2018}],"confusable_with":""},
  {"id":"closed-claims-3","topic":"Closed Claims Analysis & Anesthesia Liability","domain":items[6]["domain"],"discipline":"anesthesia",
   "stem":"In closed claims analysis of cardiac arrest during spinal anesthesia, what was the most common presenting symptom and what treatment delay was identified?",
   "answer":"Bradycardia was the most common presenting symptom (hypotension second); epinephrine was not given until a mean of 8 minutes after onset of asystole.",
   "rationale":"High spinal blockade causes sympathectomy with vagal dominance; delayed epinephrine administration worsens outcomes because CPR alone is often insufficient in neuraxial cardiac arrest.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":856}],"confusable_with":""},
  {"id":"closed-claims-4","topic":"Closed Claims Analysis & Anesthesia Liability","domain":items[6]["domain"],"discipline":"anesthesia",
   "stem":"What do closed claims analyses identify as a common contributor to anesthetic misadventure?",
   "answer":"Multiple factors often combine to create an anesthetic misadventure; incorrect drug labels are one example, and inadequate preparation is another contributing factor.",
   "rationale":"Swiss cheese model of error: single safeguard failures rarely cause harm, but multiple simultaneous failures align to produce adverse events.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":2048}],"confusable_with":""}
]

# ── 997 Complex Regional Pain Syndrome (CRPS) ─────────────────────────────────
kps += [
  {"id":"crps-1","topic":"Complex Regional Pain Syndrome (CRPS)","domain":items[7]["domain"],"discipline":"anesthesia",
   "stem":"What are the two subtypes of complex regional pain syndrome and how do they differ?",
   "answer":"CRPS type 1 (formerly reflex sympathetic dystrophy): no identifiable nerve injury. CRPS type 2 (formerly causalgia): follows a specific nerve injury.",
   "rationale":"Both subtypes share autonomic features (vasomotor, sudomotor changes) and pain disproportionate to injury; the distinction is presence of a documented peripheral nerve lesion.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1703}],"confusable_with":"diabetic peripheral neuropathy (symmetric stocking-glove distribution, no autonomic features of CRPS)"},
  {"id":"crps-2","topic":"Complex Regional Pain Syndrome (CRPS)","domain":items[7]["domain"],"discipline":"anesthesia",
   "stem":"What clinical presentation characterizes complex regional pain syndrome in the affected extremity?",
   "answer":"CRPS manifests with pain disproportionate to any inciting event in a distal extremity, usually after trauma or prolonged immobilization, with significant autonomic features (vasomotor, sudomotor changes).",
   "rationale":"Central and peripheral sensitization, combined with sympathetic dysregulation, produce the characteristic allodynia, hyperalgesia, and autonomic instability.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":825}],"confusable_with":"peripheral arterial disease (pain but ischemic, not autonomic-mediated)"},
  {"id":"crps-3","topic":"Complex Regional Pain Syndrome (CRPS)","domain":items[7]["domain"],"discipline":"anesthesia",
   "stem":"What peripheral nerve mechanisms contribute to neuropathic and complex regional pain syndromes?",
   "answer":"Peripheral mechanisms include spontaneous discharges, sensitization of receptors to mechanical/thermal/chemical stimuli, upregulation of adrenergic receptors, and neural inflammation.",
   "rationale":"Adrenergic receptor upregulation is the basis for sympathetically maintained pain in CRPS, where norepinephrine abnormally activates nociceptors.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1726}],"confusable_with":""},
  {"id":"crps-4","topic":"Complex Regional Pain Syndrome (CRPS)","domain":items[7]["domain"],"discipline":"anesthesia",
   "stem":"What historical term was used for CRPS type 2, and when was it first identified?",
   "answer":"Causalgia (meaning burning pain) was first identified by Weir Mitchell in injured veterans of the American Civil War; it typically follows gunshot wounds to peripheral nerves.",
   "rationale":"Recognition of causalgia as a distinct post-nerve-injury pain syndrome established the connection between peripheral nerve damage and chronic sympathetically-mediated pain.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1747}],"confusable_with":""}
]
kps.append({"_type":"illness_script","topic":"Complex Regional Pain Syndrome (CRPS)","discipline":"anesthesia",
  "enabling_conditions":"Trauma or fracture (even minor), surgery, prolonged immobilization; CRPS type 2 after peripheral nerve injury",
  "pathophysiology":"Peripheral sensitization (adrenergic receptor upregulation, spontaneous discharges) plus central sensitization (wind-up, WDR neuron expansion) driven by sympathetic dysregulation",
  "time_course":"Develops weeks to months after inciting event; can be progressive with trophic changes; early treatment improves prognosis",
  "key_features":"Burning pain disproportionate to injury, allodynia, autonomic changes (skin color/temperature/sweating), trophic changes (nail/hair growth changes), distal extremity",
  "consequence_if_missed":"Progression to permanent disability with limb dystrophy; early sympathetic blockade (stellate, lumbar sympathetic) may prevent chronification"})

# ── 998 Conflict of Interest & Industry Relationships ─────────────────────────
kps += [
  {"id":"coi-1","topic":"Conflict of Interest & Industry Relationships","domain":items[8]["domain"],"discipline":"medicine",
   "stem":"How do major clinical practice guidelines manage author conflicts of interest?",
   "answer":"Guidelines include appendices disclosing author relationships with industry and other entities, identifying relevant financial conflicts; content reviewers with conflicts are excluded from relevant sections.",
   "rationale":"Transparency in COI disclosure allows readers to evaluate potential bias; guideline integrity depends on methodological rigor independent of industry influence.",
   "bloom":"recall","source":[{"book":"Society Guideline: Guideline   ACC AHA 2023 Atrial Fibrillation","page":3}],"confusable_with":""},
  {"id":"coi-2","topic":"Conflict of Interest & Industry Relationships","domain":items[8]["domain"],"discipline":"medicine",
   "stem":"What is the ADA standard regarding the relationship between clinical judgment and evidence-based guidelines?",
   "answer":"The ADA Standards of Care recommendations are not intended to preclude clinical judgment; they must be applied in the context of individual patient situations.",
   "rationale":"Guidelines synthesize population-level evidence; individual patient factors, comorbidities, and values may justify deviation from guidelines when clinically appropriate.",
   "bloom":"recall","source":[{"book":"Society Guideline: Guideline   ADA Standards of Care 2024 Overview","page":2}],"confusable_with":""},
  {"id":"coi-3","topic":"Conflict of Interest & Industry Relationships","domain":items[8]["domain"],"discipline":"medicine",
   "stem":"What disclosure format do ACC/AHA guidelines use for guideline committee members?",
   "answer":"ACC/AHA guidelines include appendices listing each committee member's organizational and financial relationships with industry, including specific companies and nature of relationship (consultant, speaker, research support).",
   "rationale":"Granular disclosure of specific company relationships enables readers to assess direction and magnitude of potential bias more accurately than simple yes/no conflict statements.",
   "bloom":"recall","source":[{"book":"Society Guideline: Guideline   ACC AHA 2022 Heart Failure","page":151}],"confusable_with":""}
]

# ── 999 Disclosure of Medical Errors & Adverse Events ─────────────────────────
kps += [
  {"id":"disclosure-errors-1","topic":"Disclosure of Medical Errors & Adverse Events","domain":items[9]["domain"],"discipline":"anesthesia",
   "stem":"What approach do most risk managers advocate following an adverse anesthetic outcome?",
   "answer":"Most risk managers advocate frank and honest disclosure of adverse events to patients or approved family members; it is possible to express sorrow without admitting guilt.",
   "rationale":"Open disclosure reduces patient anger, supports trust, and often decreases litigation; expressing empathy without admitting legal liability is both ethically sound and strategically appropriate.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":2009}],"confusable_with":""},
  {"id":"disclosure-errors-2","topic":"Disclosure of Medical Errors & Adverse Events","domain":items[9]["domain"],"discipline":"anesthesia",
   "stem":"What action must an anesthesia provider take immediately after receiving notification of a malpractice complaint?",
   "answer":"The defendant must contact their malpractice insurer/risk management department, who will appoint legal counsel.",
   "rationale":"Malpractice insurers provide legal defense; early notification preserves coverage and enables proper legal strategy; independent action without insurer notification may void coverage.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2009}],"confusable_with":""},
  {"id":"disclosure-errors-3","topic":"Disclosure of Medical Errors & Adverse Events","domain":items[9]["domain"],"discipline":"anesthesia",
   "stem":"What constitutes a National Quality Forum Serious Reportable Event beyond Joint Commission sentinel events?",
   "answer":"NQF Serious Reportable Events include intraoperative death in an ASA class I patient and death or disability from irretrievable loss of an irreplaceable biologic specimen.",
   "rationale":"Never events represent errors so serious and preventable that they should be transparently reported; they reflect systemic failures requiring root cause analysis.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":861}],"confusable_with":"Joint Commission sentinel events (overlapping but different lists)"},
  {"id":"disclosure-errors-4","topic":"Disclosure of Medical Errors & Adverse Events","domain":items[9]["domain"],"discipline":"anesthesia",
   "stem":"What is the focus of root cause analysis following an adverse event?",
   "answer":"RCA focuses strictly on system processes and not on individual provider behavior; a causal factor chart is created examining every step of the process that resulted in the event.",
   "rationale":"Systems-focused analysis identifies modifiable process failures rather than blaming individuals; blame-free culture encourages reporting and enables systemic improvement.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":860}],"confusable_with":"peer review (evaluates individual provider performance)"}
]

# ── 1000 Fall Prevention & Positioning Safety ──────────────────────────────────
kps += [
  {"id":"fall-positioning-1","topic":"Fall Prevention & Positioning Safety","domain":items[10]["domain"],"discipline":"anesthesia",
   "stem":"How does general anesthesia alter hemodynamic responses to positional changes compared with the awake state?",
   "answer":"Anesthesia blunts autonomic reflexes that normally compensate for positional hemodynamic changes, exaggerating the cardiovascular response to position shifts.",
   "rationale":"General anesthesia suppresses sympathetic vasomotor reflexes; positional changes (e.g., head-up tilt) can cause profound hypotension that would be corrected in an awake patient.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":361}],"confusable_with":""},
  {"id":"fall-positioning-2","topic":"Fall Prevention & Positioning Safety","domain":items[10]["domain"],"discipline":"anesthesia",
   "stem":"What patient risk factors are associated with perioperative ischemic optic neuropathy (ION) in the prone position?",
   "answer":"Risk factors for ION include hypertension, diabetes, atherosclerosis, morbid obesity, and tobacco use; large-volume crystalloid use, anemia, and increased intraocular/venous pressure from prone positioning are additional contributors.",
   "rationale":"ION results from ischemia to the optic nerve; prone positioning raises intraocular pressure and reduces perfusion pressure, particularly with anemia and hemodilution from large crystalloid volumes.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":373}],"confusable_with":"central retinal artery occlusion (external eye pressure, not ION)"},
  {"id":"fall-positioning-3","topic":"Fall Prevention & Positioning Safety","domain":items[10]["domain"],"discipline":"anesthesia",
   "stem":"What are the risk factors identified for ulnar nerve injury claims in anesthesia closed claims?",
   "answer":"Risk factors for ulnar injury include diabetes, alcohol use disorder, cigarette smoking, and cancer; in 27% of claims, inadequate elbow padding was explicitly documented.",
   "rationale":"Ulnar nerve at the elbow is susceptible to external compression and stretch; proper padding reduces but does not eliminate risk, particularly in patients with preexisting neuropathy.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":371}],"confusable_with":"brachial plexus injury (different mechanism and positioning factors)"},
  {"id":"fall-positioning-4","topic":"Fall Prevention & Positioning Safety","domain":items[10]["domain"],"discipline":"anesthesia",
   "stem":"What effect does anesthesia have on functional residual capacity (FRC) when a patient is placed supine?",
   "answer":"FRC decreases when non-anesthetized people lie down; this decrease is further exaggerated during general anesthesia due to loss of respiratory muscle tone and diaphragm elevation.",
   "rationale":"Reduced FRC decreases the oxygen reserve and promotes atelectasis; lung-protective strategies and positioning adjustments help mitigate this during anesthesia.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":361}],"confusable_with":""}
]

# ── 1001 Fibromyalgia and Central Sensitization Syndromes ─────────────────────
kps += [
  {"id":"fibromyalgia-1","topic":"Fibromyalgia and Central Sensitization Syndromes","domain":items[11]["domain"],"discipline":"anesthesia",
   "stem":"What spinal cord mechanism amplifies pain signaling in central sensitization syndromes?",
   "answer":"Wind-up: WDR (wide dynamic range) neurons increase their discharge frequency with repetitive stimuli, exhibit prolonged discharge even after C-fiber input stops, and expand their receptive fields.",
   "rationale":"Repeated C-fiber activation causes NMDA receptor-dependent potentiation of dorsal horn neurons, amplifying pain signals and leading to widespread hyperalgesia characteristic of fibromyalgia.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1724}],"confusable_with":"peripheral sensitization (local nociceptor sensitization, not central amplification)"},
  {"id":"fibromyalgia-2","topic":"Fibromyalgia and Central Sensitization Syndromes","domain":items[11]["domain"],"discipline":"anesthesia",
   "stem":"What peripheral nociceptor changes contribute to neuropathic pain states including central sensitization?",
   "answer":"Peripheral mechanisms include spontaneous discharges, sensitization of receptors to mechanical/thermal/chemical stimuli, upregulation of adrenergic receptors, and neural inflammation.",
   "rationale":"Peripheral sensitization lowers the threshold for nociceptor activation; ongoing peripheral input drives and maintains central sensitization in the dorsal horn.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1726}],"confusable_with":""},
  {"id":"fibromyalgia-3","topic":"Fibromyalgia and Central Sensitization Syndromes","domain":items[11]["domain"],"discipline":"anesthesia",
   "stem":"What pharmacological agents are FDA-approved or commonly used for central sensitization pain syndromes including fibromyalgia?",
   "answer":"Pregabalin (Lyrica) is FDA-approved for fibromyalgia; phenytoin, carbamazepine, valproic acid, clonazepam, and gabapentin are commonly used for neuropathic pain with spontaneous neural discharges.",
   "rationale":"These agents reduce neuronal hyperexcitability by blocking sodium channels or calcium channels (gabapentinoids), damping central sensitization.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1761}],"confusable_with":""},
  {"id":"fibromyalgia-4","topic":"Fibromyalgia and Central Sensitization Syndromes","domain":items[11]["domain"],"discipline":"anesthesia",
   "stem":"What is the natural history of myofascial trigger points and how do latent trigger points differ from active ones?",
   "answer":"Active trigger points produce pain on stimulation and ensuing muscle spasm; when the acute episode subsides they become latent (tender but not pain-producing) and can be reactivated later.",
   "rationale":"Trigger points develop after acute injury; persistent muscle spasm sustains the pain cycle; latent trigger points explain recurrence after apparent resolution.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1734}],"confusable_with":"fibromyalgia tender points (widespread, not localized trigger points with referred pain)"},
  {"id":"fibromyalgia-5","topic":"Fibromyalgia and Central Sensitization Syndromes","domain":items[11]["domain"],"discipline":"anesthesia",
   "stem":"What is thought to be the initiating sequence in the development of chronic centralized pain states?",
   "answer":"An initiating factor triggers sensitization of the peripheral and central nervous system, which leads to development of a centralized neuropathic pain state.",
   "rationale":"Peripheral injury activates and sensitizes nociceptors; sustained input drives NMDA-dependent central sensitization that may persist even after peripheral healing.",
   "bloom":"analyze","source":[{"book":"StatPearls: StatPearls   MEN Syndromes (Multiple Endocrine Neoplasia)","page":9}],"confusable_with":""}
]

# ── 1002 Head and Neck Regional Blocks ────────────────────────────────────────
kps += [
  {"id":"head-neck-blocks-1","topic":"Head and Neck Regional Blocks","domain":items[12]["domain"],"discipline":"anesthesia",
   "stem":"For what surgical procedure is the cervical plexus block most commonly used to provide anesthesia in a conscious patient?",
   "answer":"Cervical plexus block is used most often to provide anesthesia in conscious patients undergoing carotid endarterectomy.",
   "rationale":"Awake carotid endarterectomy with cervical plexus block allows continuous neurological monitoring during carotid clamping, detecting cerebral ischemia that cannot be assessed under general anesthesia.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":346}],"confusable_with":"superficial cervical plexus block alone (deep block required for surgical anesthesia)"},
  {"id":"head-neck-blocks-2","topic":"Head and Neck Regional Blocks","domain":items[12]["domain"],"discipline":"anesthesia",
   "stem":"For a patient with submandibular infection spreading along tissue planes and displacing the airway, what intubation approach is indicated?",
   "answer":"Awake intubation (oral or nasal fiberoptic) is indicated; spontaneous ventilation must be preserved because mask ventilation and direct laryngoscopy may fail with airway displacement.",
   "rationale":"Ludwig angina and deep space neck infections cause airway distortion making conventional laryngoscopy hazardous; awake fiberoptic preserves airway and allows confirmation before induction.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":550}],"confusable_with":"rapid sequence induction (contraindicated if airway displacement present)"},
  {"id":"head-neck-blocks-3","topic":"Head and Neck Regional Blocks","domain":items[12]["domain"],"discipline":"anesthesia",
   "stem":"What anesthesia machine safety system prevents interchangeable connection of different medical gas hoses to incorrect outlets?",
   "answer":"The Diameter Index Safety System (DISS) uses different diameter threaded connectors for each gas at pressures up to 200 psi, preventing cross-connection.",
   "rationale":"DISS ensures that oxygen, nitrous oxide, and air lines cannot be inadvertently swapped, preventing delivery of hypoxic gas mixtures.",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":76}],"confusable_with":"Pin Index Safety System (PISS applies to cylinders, DISS to pipeline connections)"}
]

# ── 1003 Human Factors & Cognitive Error in Clinical Practice ─────────────────
kps += [
  {"id":"human-factors-1","topic":"Human Factors & Cognitive Error in Clinical Practice","domain":items[13]["domain"],"discipline":"anesthesia",
   "stem":"How does quality differ from safety in clinical practice, and why do they not always overlap?",
   "answer":"Quality and safety do not always overlap; a process can be made incrementally safer by adding checks or equipment, but this may reduce efficiency and not always improve quality outcomes.",
   "rationale":"Safety is about preventing harm; quality encompasses doing the right thing for the right patient at the right time; maximum safety measures (e.g., requiring fiberoptic for every case) may impede overall care quality.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":854}],"confusable_with":""},
  {"id":"human-factors-2","topic":"Human Factors & Cognitive Error in Clinical Practice","domain":items[13]["domain"],"discipline":"anesthesia",
   "stem":"What is the key limitation of eGFRcr (creatinine-based eGFR) and when should eGFRcr-cys be used instead?",
   "answer":"eGFRcr is less accurate in situations where creatinine production is abnormal; eGFRcr-cys should be used when eGFRcr is less accurate and GFR affects clinical decision-making.",
   "rationale":"Serum creatinine varies with muscle mass, diet, and tubular secretion; cystatin C is less affected by these factors, improving GFR estimation accuracy in extremes of body composition.",
   "bloom":"apply","source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":36}],"confusable_with":""}
]

# ── 1004 Informed Consent for Research & Clinical Trials ─────────────────────
kps += [
  {"id":"informed-consent-research-1","topic":"Informed Consent for Research & Clinical Trials","domain":items[14]["domain"],"discipline":"medicine",
   "stem":"What ethical challenge is unique to resuscitation research clinical trials?",
   "answer":"Randomization in resuscitation trials often occurs before informed consent can be obtained, necessitating a balance between risk, randomization, and ethical requirements for informed consent.",
   "rationale":"Exception from informed consent (EFIC) regulations allow enrollment in emergency research when the patient is incapacitated and delay for consent would eliminate trial eligibility.",
   "bloom":"analyze","source":[{"book":"StatPearls: StatPearls   ACLS  Non Shockable Rhythms (PEA & Asystole)","page":1}],"confusable_with":""},
  {"id":"informed-consent-research-2","topic":"Informed Consent for Research & Clinical Trials","domain":items[14]["domain"],"discipline":"medicine",
   "stem":"What is a time-limited trial in the context of perioperative decision-making?",
   "answer":"A time-limited trial is an agreement between clinicians and a patient or family to use certain medical therapies over a defined period to evaluate improvement or deterioration according to agreed-upon clinical outcomes.",
   "rationale":"Time-limited trials allow ethical initiation of potentially beneficial but burdensome therapy while honoring patient values; they avoid open-ended commitment to interventions that may not achieve goals.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":873}],"confusable_with":""},
  {"id":"informed-consent-research-3","topic":"Informed Consent for Research & Clinical Trials","domain":items[14]["domain"],"discipline":"medicine",
   "stem":"What is the reported incidence of awareness recall during major trauma surgery compared with routine anesthesia?",
   "answer":"Recall rates for intraoperative events during major trauma surgery have been reported as high as 43%; awareness during cardiac surgery is also elevated.",
   "rationale":"Hemodynamic instability in trauma limits anesthetic depth; reduced anesthetic agents are used to maintain perfusion, increasing awareness risk.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2029}],"confusable_with":"awareness under routine general anesthesia (incidence approximately 0.1-0.2%)"}
]

# ── 1005 Interventional Pain Procedures — Sympathetic Blocks ──────────────────
kps += [
  {"id":"sympathetic-blocks-1","topic":"Interventional Pain Procedures — Sympathetic Blocks","domain":items[15]["domain"],"discipline":"anesthesia",
   "stem":"What prognostic information does pain relief following a diagnostic nerve block provide?",
   "answer":"Pain relief following a diagnostic nerve block carries favorable prognostic implications for a subsequent therapeutic series of blocks and can help identify pain mechanisms.",
   "rationale":"Diagnostic blocks delineate the neural pathway responsible for pain; a positive response predicts therapeutic benefit from more definitive interventional or neuroablative procedures.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1767}],"confusable_with":""},
  {"id":"sympathetic-blocks-2","topic":"Interventional Pain Procedures — Sympathetic Blocks","domain":items[15]["domain"],"discipline":"anesthesia",
   "stem":"What is a major limitation of neurolytic nerve blocks (alcohol or phenol) for pain management?",
   "answer":"Although initial results may be excellent, the original pain may recur or new deafferentation/central pain may develop in most patients within weeks to months.",
   "rationale":"Neurolytic agents cause Wallerian degeneration; aberrant regeneration and deafferentation pain can be worse than the original nociceptive pain being treated.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1798}],"confusable_with":""},
  {"id":"sympathetic-blocks-3","topic":"Interventional Pain Procedures — Sympathetic Blocks","domain":items[15]["domain"],"discipline":"anesthesia",
   "stem":"What is the archetypal chronic pain syndrome thought to have sympathetically mediated pain?",
   "answer":"Complex regional pain syndrome (CRPS) is the archetypal syndrome with an element of sympathetically mediated pain, manifesting with disproportionate pain in a distal extremity usually after trauma.",
   "rationale":"Sympathetic blockade (stellate or lumbar sympathetic block) can relieve pain in sympathetically-maintained CRPS, confirming the sympathetic contribution.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":825}],"confusable_with":""},
  {"id":"sympathetic-blocks-4","topic":"Interventional Pain Procedures — Sympathetic Blocks","domain":items[15]["domain"],"discipline":"anesthesia",
   "stem":"What sympathectomy effect does neuraxial block have on the gut?",
   "answer":"Neuraxial block-induced sympathectomy allows vagal dominance, producing a small, contracted gut with active peristalsis; postoperative epidural analgesia with local anesthetics hastens the return of bowel function.",
   "rationale":"The GI tract is predominantly parasympathetically (vagally) innervated; sympathectomy from neuraxial block removes inhibitory adrenergic tone, restoring peristalsis.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1557}],"confusable_with":""}
]

# ── 1006 Intrathecal Drug Delivery Systems (IDDS) ─────────────────────────────
kps += [
  {"id":"idds-1","topic":"Intrathecal Drug Delivery Systems (IDDS)","domain":items[16]["domain"],"discipline":"anesthesia",
   "stem":"What are the two primary advantages of intrathecal drug delivery systems for chronic pain?",
   "answer":"IDDS may improve analgesia and, via a drug-sparing effect, decrease systemic side effects associated with oral or intravenous agents.",
   "rationale":"Direct delivery to the CSF allows markedly lower total drug doses (morphine: IT 1/300th of oral dose) producing equivalent or superior analgesia with fewer systemic adverse effects.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1753}],"confusable_with":"epidural drug delivery (IT requires even lower doses)"},
  {"id":"idds-2","topic":"Intrathecal Drug Delivery Systems (IDDS)","domain":items[16]["domain"],"discipline":"anesthesia",
   "stem":"What scheduling principle should guide chronic cancer pain medication dosing?",
   "answer":"Drug therapy should be provided on a fixed time schedule rather than as needed, with additional short-acting medication available for breakthrough pain.",
   "rationale":"Around-the-clock dosing maintains steady analgesic blood levels, prevents pain recurrence, and reduces total drug consumption versus reactive PRN dosing.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1753}],"confusable_with":""},
  {"id":"idds-3","topic":"Intrathecal Drug Delivery Systems (IDDS)","domain":items[16]["domain"],"discipline":"anesthesia",
   "stem":"What is ziconotide and why is it used for refractory intrathecal pain management?",
   "answer":"Ziconotide is a direct-acting N-type calcium channel blocker approved for intrathecal use; it may be helpful for refractory pain or as a first-line agent when opioids are contraindicated.",
   "rationale":"Ziconotide blocks calcium-dependent neurotransmitter release at dorsal horn synapses; it is non-opioid, avoiding tolerance and opioid-related side effects.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1753}],"confusable_with":"opioid IDDS (tolerance develops; ziconotide avoids this)"},
  {"id":"idds-4","topic":"Intrathecal Drug Delivery Systems (IDDS)","domain":items[16]["domain"],"discipline":"anesthesia",
   "stem":"What advantage does continuous intraspinal infusion have over intermittent bolus neuraxial administration?",
   "answer":"Continuous intraspinal infusion reduces drug requirements, minimizes side effects, and decreases the likelihood of intrathecal or epidural catheter complications compared with intermittent boluses.",
   "rationale":"Steady-state drug delivery avoids peak-trough fluctuations that cause alternating side effects and breakthrough pain with intermittent bolus techniques.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1764}],"confusable_with":""},
  {"id":"idds-5","topic":"Intrathecal Drug Delivery Systems (IDDS)","domain":items[16]["domain"],"discipline":"anesthesia",
   "stem":"What adjuvant drug classes may be added to opioid therapy to increase analgesia quality and decrease opioid side effects?",
   "answer":"Antidepressants and anticonvulsants (adjuvant analgesics) may be used with opioids to increase analgesia quality and decrease opioid-related side effects.",
   "rationale":"Antidepressants (TCAs, SNRIs) and anticonvulsants (gabapentinoids) have independent analgesic mechanisms allowing opioid dose reduction while maintaining pain control.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1753}],"confusable_with":""}
]

# ── 1007 Justice, Equity & Health Disparities in Anesthesia ───────────────────
kps += [
  {"id":"equity-anesthesia-1","topic":"Justice, Equity & Health Disparities in Anesthesia","domain":items[17]["domain"],"discipline":"anesthesia",
   "stem":"What factors are understood to contribute to health disparities and perioperative vulnerability?",
   "answer":"Vulnerability to perioperative stress results from the confluence of physical, physiologic, psychological, and social factors; causes of health disparities are multifactorial and likely include factors affecting historically marginalized populations.",
   "rationale":"Social determinants of health (poverty, racism, limited healthcare access) compound physiologic risk in perioperative care, explaining differential outcomes across demographic groups.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":788}],"confusable_with":""},
  {"id":"equity-anesthesia-2","topic":"Justice, Equity & Health Disparities in Anesthesia","domain":items[17]["domain"],"discipline":"anesthesia",
   "stem":"What role do accreditation agencies play in reducing disparities in levels of care?",
   "answer":"Accreditation requirements help reduce disparities in levels of care by ensuring facilities meet minimum standards of policies and procedures.",
   "rationale":"Without minimum accreditation standards, resource-poor institutions may provide substantially lower quality care; standardized accreditation reduces but does not eliminate these gaps.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":58}],"confusable_with":""},
  {"id":"equity-anesthesia-3","topic":"Justice, Equity & Health Disparities in Anesthesia","domain":items[17]["domain"],"discipline":"anesthesia",
   "stem":"What is identified as contributing to racial and ethnic disparities in perioperative outcomes including obstetric anesthesia?",
   "answer":"Racial and ethnic disparities in perioperative outcomes exist; the US has the highest maternal mortality rate among developed countries with cardiovascular disease as a major contributor, and racial disparities in obstetric outcomes are documented.",
   "rationale":"Structural racism affects access to prenatal care, quality of intrapartum monitoring, and response to complications, contributing to disproportionately higher maternal mortality in Black women.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1441}],"confusable_with":""}
]

# ── 1008 Lower Extremity Regional Analgesia ───────────────────────────────────
kps += [
  {"id":"lower-extremity-regional-1","topic":"Lower Extremity Regional Analgesia","domain":items[18]["domain"],"discipline":"anesthesia",
   "stem":"What are the benefits of lower extremity perineural catheters for major joint surgery?",
   "answer":"Lower extremity perineural catheters for hip, knee, ankle, and foot surgery may decrease clinical complications and facilitate earlier range-of-motion achievement and ambulation.",
   "rationale":"Continuous regional analgesia reduces opioid requirements, enabling earlier mobilization which decreases DVT risk and speeds rehabilitation after major joint surgery.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":753}],"confusable_with":""},
  {"id":"lower-extremity-regional-2","topic":"Lower Extremity Regional Analgesia","domain":items[18]["domain"],"discipline":"anesthesia",
   "stem":"What is a saddle block and how is it achieved with hyperbaric spinal anesthesia?",
   "answer":"A saddle block is achieved by keeping the patient in the sitting position after injecting hyperbaric spinal anesthetic; the solution pools in the most dependent area (sacral region), anesthetizing the perineum.",
   "rationale":"Hyperbaric solutions are denser than CSF; gravity in the sitting position concentrates the anesthetic in the sacral roots, producing perineal anesthesia appropriate for anorectal surgery.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1582}],"confusable_with":"isobaric spinal (position-independent spread)"},
  {"id":"lower-extremity-regional-3","topic":"Lower Extremity Regional Analgesia","domain":items[18]["domain"],"discipline":"anesthesia",
   "stem":"For what clinical situation are continuous peripheral nerve block infusions typically reserved?",
   "answer":"Continuous peripheral nerve block infusions are typically reserved for patients having procedures expected to result in significant postoperative pain.",
   "rationale":"The risks and logistics of catheter management (infection, dislodgement, local anesthetic toxicity) are justified only when the expected pain benefit is substantial.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1619}],"confusable_with":""},
  {"id":"lower-extremity-regional-4","topic":"Lower Extremity Regional Analgesia","domain":items[18]["domain"],"discipline":"anesthesia",
   "stem":"What metabolism pathway differentiates amino-ester from amino-amide local anesthetics?",
   "answer":"Amino-ester local anesthetics undergo hydrolysis by plasma esterases; amino-amide local anesthetics undergo metabolism by hepatic microsomal enzymes.",
   "rationale":"This metabolic difference explains why patients with pseudocholinesterase deficiency are at risk from ester LAs (prolonged effect), while severe hepatic disease impairs amide LA clearance.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":175}],"confusable_with":"amide toxicity in hepatic failure vs. ester sensitivity in pseudocholinesterase deficiency"}
]

# ── 1009 MAOI interactions and psychiatric medication perioperative management ─
kps += [
  {"id":"maoi-periop-1","topic":"MAOI interactions and psychiatric medication perioperative management","domain":items[19]["domain"],"discipline":"anesthesia",
   "stem":"What considerations apply when managing psychotropic medications in patients with renal impairment?",
   "answer":"Check liver, renal, and cardiac function before initiating psychotropics; avoid drug-drug interactions especially with SSRIs (CYP450 inhibition) and carbamazepine (enzyme inducer); avoid duplication with sedatives, opioids, or anticholinergics.",
   "rationale":"Renally cleared psychotropics accumulate in CKD causing toxicity; CYP450 interactions can dramatically raise or lower drug levels; anticholinergic burden causes delirium in vulnerable patients.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Approach to Anaphylaxis","page":26}],"confusable_with":""},
  {"id":"maoi-periop-2","topic":"MAOI interactions and psychiatric medication perioperative management","domain":items[19]["domain"],"discipline":"anesthesia",
   "stem":"What considerations apply to ECT and its anesthetic management regarding seizure duration?",
   "answer":"ECT seizures lasting more than 120 seconds may be harmful; adjustment of stimulation by the ECT physician and possible intervention by the anesthesia provider may be necessary.",
   "rationale":"ECT requires a therapeutic seizure of adequate duration (>25 seconds); prolonged seizures increase neurologic risk and may require pharmacologic termination with benzodiazepines.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":715}],"confusable_with":""},
  {"id":"maoi-periop-3","topic":"MAOI interactions and psychiatric medication perioperative management","domain":items[19]["domain"],"discipline":"anesthesia",
   "stem":"What delirium features per DSM-V must be present for the diagnosis?",
   "answer":"Delirium requires: (1) disturbance of consciousness with reduced ability to focus/sustain/shift attention; (2) disturbance in cognition (memory, disorientation, language, perception); (3) change from baseline developing over hours to days.",
   "rationale":"DSM-V criteria distinguish delirium from dementia (chronic, stable cognitive impairment) and depression (no acute attentional disturbance); correct classification guides management.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":207}],"confusable_with":"dementia (chronic, not acute fluctuating; no attentional disturbance)"}
]

# ── 1010 Malpractice, Negligence & Legal Foundations ─────────────────────────
kps += [
  {"id":"malpractice-1","topic":"Malpractice, Negligence & Legal Foundations","domain":items[20]["domain"],"discipline":"anesthesia",
   "stem":"What four elements must a plaintiff prove to establish medical negligence?",
   "answer":"Duty (professional relationship established), Breach (deviation from standard of care), Causation (breach caused harm), and Damages (actual harm resulted).",
   "rationale":"All four elements must be proven by preponderance of the evidence; absence of any one element defeats a negligence claim, regardless of poor outcome.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":488}],"confusable_with":"res ipsa loquitur (shifts burden of proof to defendant in certain obvious negligence cases)"},
  {"id":"malpractice-2","topic":"Malpractice, Negligence & Legal Foundations","domain":items[20]["domain"],"discipline":"anesthesia",
   "stem":"What is the doctrine of res ipsa loquitur and when does it apply in medical malpractice?",
   "answer":"Res ipsa loquitur applies when the injury could not have occurred in the absence of negligence (e.g., retained sponge on chest radiograph after thoracotomy); the plaintiff must establish the event could not occur without negligence.",
   "rationale":"Res ipsa loquitur shifts the burden of proof to the defendant; it does not apply when the adverse event (e.g., cardiac arrest) can occur without negligence.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":489}],"confusable_with":"standard negligence (plaintiff must prove all 4 elements; res ipsa shifts burden)"},
  {"id":"malpractice-3","topic":"Malpractice, Negligence & Legal Foundations","domain":items[20]["domain"],"discipline":"anesthesia",
   "stem":"What is the OSHA maximum acceptable trace concentration of nitrous oxide and halogenated agents in the OR?",
   "answer":"OSHA sets maximum acceptable trace concentrations of less than 25 ppm for nitrous oxide and 0.5 ppm for halogenated agents.",
   "rationale":"Chronic exposure to trace anesthetic agents has been associated with concerns about reproductive effects and other health risks; scavenging systems are required to maintain levels below these limits.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2007}],"confusable_with":""},
  {"id":"malpractice-4","topic":"Malpractice, Negligence & Legal Foundations","domain":items[20]["domain"],"discipline":"anesthesia",
   "stem":"What is the first action an anesthesia provider must take upon receiving a malpractice complaint?",
   "answer":"The defendant must contact their malpractice insurer and risk management department, who will appoint legal counsel.",
   "rationale":"Malpractice insurers provide the legal defense; early notification preserves coverage and allows counsel to guide all subsequent communications and documentation.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2009}],"confusable_with":""}
]

# ── 1011 Neuraxial Analgesia — Intrathecal Opioids ────────────────────────────
kps += [
  {"id":"neuraxial-it-opioids-1","topic":"Neuraxial Analgesia — Intrathecal Opioids","domain":items[21]["domain"],"discipline":"anesthesia",
   "stem":"Why are spinal opioids and local anesthetics most commonly combined rather than used alone for obstetric analgesia?",
   "answer":"Combining spinal opioids and local anesthetics provides superior analgesia to either alone; synergy decreases dose requirements, reduces side effects, and provides excellent analgesia with few motor side effects.",
   "rationale":"Opioids act on spinal opioid receptors while local anesthetics block sodium channels; the two mechanisms are additive to synergistic, allowing lower doses of each with fewer dose-dependent side effects.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1391}],"confusable_with":""},
  {"id":"neuraxial-it-opioids-2","topic":"Neuraxial Analgesia — Intrathecal Opioids","domain":items[21]["domain"],"discipline":"anesthesia",
   "stem":"What opioid characteristics make intrathecal morphine less ideal as a sole agent for labor analgesia?",
   "answer":"Intrathecal morphine has slow onset (45-60 min) and doses sufficient for adequate analgesia are associated with a high incidence of side effects; it is therefore rarely used alone.",
   "rationale":"Morphine is hydrophilic; slow CSF penetration to dorsal horn receptors delays onset; the dose needed for effective analgesia causes pruritus, nausea, and respiratory depression.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1392}],"confusable_with":"intrathecal fentanyl (lipophilic, rapid onset, shorter duration)"},
  {"id":"neuraxial-it-opioids-3","topic":"Neuraxial Analgesia — Intrathecal Opioids","domain":items[21]["domain"],"discipline":"anesthesia",
   "stem":"What is the significance of dural erosion by an epidural catheter and how does it present?",
   "answer":"Dural erosion (catheter migrating intrathecally) presents with slowly progressive motor blockade of lower extremities and rising sensory blockade level; overt systemic toxicity signs may be absent.",
   "rationale":"A catheter that gradually erodes through the dura delivers epidural drug concentrations into the subarachnoid space; rising block with no systemic toxicity signs requires high suspicion.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1398}],"confusable_with":"intravascular catheter migration (systemic toxicity: tinnitus, perioral numbness, seizure)"},
  {"id":"neuraxial-it-opioids-4","topic":"Neuraxial Analgesia — Intrathecal Opioids","domain":items[21]["domain"],"discipline":"anesthesia",
   "stem":"What is the advantage of a multi-orifice epidural catheter over a single-orifice catheter?",
   "answer":"Multi-orifice catheters are associated with fewer unilateral blocks and greatly reduce the incidence of false-negative aspiration when assessing for intravascular or intrathecal catheter placement.",
   "rationale":"Multiple orifices distribute solution more evenly and prevent aspiration of blood or CSF through a single port from being missed when another port is open in a different space.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1396}],"confusable_with":""},
  {"id":"neuraxial-it-opioids-5","topic":"Neuraxial Analgesia — Intrathecal Opioids","domain":items[21]["domain"],"discipline":"anesthesia",
   "stem":"Why are NSAIDs such as ketorolac not recommended as antepartum analgesic therapy?",
   "answer":"Ketorolac and other NSAIDs are not recommended antepartum because they suppress uterine contractions and promote premature closure of the fetal ductus arteriosus.",
   "rationale":"Prostaglandins maintain ductal patency and contribute to uterine contractility; NSAID-mediated prostaglandin inhibition risks premature ductal constriction and impaired labor.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1390}],"confusable_with":"acetaminophen (safe in pregnancy; no cyclooxygenase effects on ductus)"}
]

# ── 1012 Patient Safety Reporting Systems ─────────────────────────────────────
kps += [
  {"id":"patient-safety-reporting-1","topic":"Patient Safety Reporting Systems","domain":items[22]["domain"],"discipline":"anesthesia",
   "stem":"What did closed claims analysis reveal about adverse respiratory events in anesthesia?",
   "answer":"Death or brain damage occurred in the majority of adverse respiratory event claims; respiratory events are the leading category of preventable anesthetic harm historically.",
   "rationale":"Adverse respiratory events (esophageal intubation, failed airway, hypoventilation) are particularly harmful because hypoxemia causes irreversible brain injury rapidly.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":856}],"confusable_with":""},
  {"id":"patient-safety-reporting-2","topic":"Patient Safety Reporting Systems","domain":items[22]["domain"],"discipline":"anesthesia",
   "stem":"What does the Institute of Medicine report 'To Err Is Human' identify as a model for quality and safety in medicine?",
   "answer":"Clinical anesthesia practice is specifically identified in 'To Err Is Human' as an area in which very impressive improvements in safety have been made, making it a model for medicine.",
   "rationale":"Anesthesia mortality declined from approximately 1:5,000 in the 1980s to 1:200,000-300,000 through standardization of monitoring, training, and protocols.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":853}],"confusable_with":""},
  {"id":"patient-safety-reporting-3","topic":"Patient Safety Reporting Systems","domain":items[22]["domain"],"discipline":"anesthesia",
   "stem":"What quality improvement roles does the Anesthesia Quality Institute serve?",
   "answer":"The AQI allows individual practices and individual physicians to compare their performance with a national database of anesthesia quality data.",
   "rationale":"Benchmarking against national data enables identification of outliers and drives quality improvement through transparent performance comparison.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2205}],"confusable_with":""}
]

# ── 1013 Pediatric-specific preoperative considerations ───────────────────────
kps += [
  {"id":"pediatric-preop-1","topic":"Pediatric-specific preoperative considerations","domain":items[23]["domain"],"discipline":"anesthesia",
   "stem":"What perioperative complication is more likely in female patients compared to male patients?",
   "answer":"Postoperative nausea and vomiting (PONV) is more likely in female patients.",
   "rationale":"Female sex is a major independent risk factor for PONV; together with history of PONV/motion sickness, non-smoking status, and opioid use it forms the Apfel PONV risk score.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":221}],"confusable_with":""},
  {"id":"pediatric-preop-2","topic":"Pediatric-specific preoperative considerations","domain":items[23]["domain"],"discipline":"anesthesia",
   "stem":"What are the goals of prehabilitation programs before major surgery?",
   "answer":"Prehabilitation targets: (1) improved physical fitness, (2) dietary interventions supporting anabolism, (3) anti-stress interventions for resilience/self-efficacy, and (4) cessation of adverse behaviors (smoking, alcohol).",
   "rationale":"Physiologic reserve determines the ability to withstand the catabolic stress of surgery; prehabilitation increases reserve preoperatively to improve postoperative recovery.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":241}],"confusable_with":""},
  {"id":"pediatric-preop-3","topic":"Pediatric-specific preoperative considerations","domain":items[23]["domain"],"discipline":"anesthesia",
   "stem":"What hemoglobin A1C level represents the threshold above which diabetes is associated with increased risk of cardiovascular events and infectious complications?",
   "answer":"Hyperglycemia (regardless of HbA1C threshold) is associated with cardiovascular events and infectious complications including wound infection, pneumonia, and sepsis; HbA1C assesses long-term glucose control perioperatively.",
   "rationale":"Acute perioperative hyperglycemia, not just chronic elevation, drives adverse outcomes through impaired neutrophil function and endothelial damage.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":231}],"confusable_with":""},
  {"id":"pediatric-preop-4","topic":"Pediatric-specific preoperative considerations","domain":items[23]["domain"],"discipline":"anesthesia",
   "stem":"What functional capacity threshold corresponds to approximately 4 METs in the preoperative assessment?",
   "answer":"Climbing one flight of stairs requires approximately 4 METs; patients unable to perform this without symptoms have limited functional capacity indicating higher perioperative cardiac risk.",
   "rationale":"Four METs is the threshold below which perioperative cardiac risk increases substantially; assessment without formal testing uses activities-of-daily-living equivalents.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":484}],"confusable_with":""}
]

# ── 1014 Peer Review, Performance Improvement & Accountability ────────────────
kps += [
  {"id":"peer-review-1","topic":"Peer Review, Performance Improvement & Accountability","domain":items[24]["domain"],"discipline":"anesthesia",
   "stem":"What is the major obstacle to establishing clear quality benchmarks in anesthesia?",
   "answer":"A major obstacle is a clear understanding of how anesthetic interventions affect patient outcomes, because much of the patient's postoperative course is influenced by surgical and patient factors beyond anesthesia control.",
   "rationale":"Confounding by surgical complexity and patient comorbidity makes it difficult to attribute outcomes specifically to anesthesia; process measures are used as surrogates.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":857}],"confusable_with":""},
  {"id":"peer-review-2","topic":"Peer Review, Performance Improvement & Accountability","domain":items[24]["domain"],"discipline":"anesthesia",
   "stem":"What does current evidence suggest about the relationship between outcome reporting and actual improvement in outcomes?",
   "answer":"Current evidence is mixed regarding whether outcome reporting improves outcomes; two studies suggest that knowing one's outcomes may not by itself improve performance.",
   "rationale":"Outcome data alone is insufficient for quality improvement; data must be coupled with actionable feedback, education, and system-level interventions to drive change.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":859}],"confusable_with":""}
]

# ── 1015 Perioperative Beta-Blocker & Protocol Safety (POISE Lessons) ─────────
kps += [
  {"id":"periop-bb-poise-1","topic":"Perioperative Beta-Blocker & Protocol Safety (POISE Lessons)","domain":items[25]["domain"],"discipline":"anesthesia",
   "stem":"What safety principles apply to the use of long-acting anesthetic premedication agents?",
   "answer":"In most centers, concern for patient safety and lack of equipment preclude anesthesia induction in the preoperative holding room; long-acting agents should be used cautiously due to prolonged sedation risk.",
   "rationale":"Long-acting premedications given outside monitored settings risk undetected respiratory depression; patient location and monitoring capability must match sedation depth.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":297}],"confusable_with":""},
  {"id":"periop-bb-poise-2","topic":"Perioperative Beta-Blocker & Protocol Safety (POISE Lessons)","domain":items[25]["domain"],"discipline":"anesthesia",
   "stem":"What NQF Serious Reportable Events specifically relate to anesthesia care?",
   "answer":"NQF adds intraoperative death in an ASA class I patient and death or disability from irretrievable loss of an irreplaceable biologic specimen to the Joint Commission sentinel event list.",
   "rationale":"These events are defined as never-acceptable outcomes reflecting failure of basic safety systems; they trigger mandatory reporting and root cause analysis.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":861}],"confusable_with":""},
  {"id":"periop-bb-poise-3","topic":"Perioperative Beta-Blocker & Protocol Safety (POISE Lessons)","domain":items[25]["domain"],"discipline":"anesthesia",
   "stem":"How did adoption of specialty-wide standards in anesthesia monitoring contribute to patient safety?",
   "answer":"Adoption of specialty-wide monitoring standards (pulse oximetry, capnography) by the ASA was a key driver of the dramatic reduction in anesthesia-related death and brain damage over the past four decades.",
   "rationale":"Mandatory continuous monitoring transforms latent physiologic deterioration into detectable signals enabling timely intervention before irreversible harm occurs.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":855}],"confusable_with":""}
]

# ── 1016 Pheochromocytoma and paraganglioma preoperative preparation ──────────
kps += [
  {"id":"pheo-paraganglioma-1","topic":"Pheochromocytoma and paraganglioma preoperative preparation","domain":items[26]["domain"],"discipline":"anesthesia",
   "stem":"What is the classic triad of symptoms caused by hormonally active pheochromocytomas?",
   "answer":"The classic triad of hormonally active pheochromocytoma is caused by sympathetic nervous system hyperactivity from excess catecholamine and metanephrine secretion: episodic hypertension, headache, and diaphoresis.",
   "rationale":"Catecholamine surges activate alpha- and beta-adrenergic receptors; alpha-1 causes vasoconstriction (hypertension), beta-1 causes tachycardia/arrhythmias.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":551}],"confusable_with":"essential hypertension (sustained, not episodic; no headache/diaphoresis triad)"},
  {"id":"pheo-paraganglioma-2","topic":"Pheochromocytoma and paraganglioma preoperative preparation","domain":items[26]["domain"],"discipline":"anesthesia",
   "stem":"Why is preoperative preparation necessary before surgical resection of catecholamine-secreting paragangliomas?",
   "answer":"Preoperative preparation prevents hypertensive crisis, malignant arrhythmias, and multiorgan failure intraoperatively.",
   "rationale":"Intraoperative tumor manipulation causes abrupt catecholamine release; without preoperative alpha-blockade and volume loading, hypertensive emergency and refractory arrhythmias are likely.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Pheochromocytoma & Paraganglioma","page":11}],"confusable_with":"non-secreting paraganglioma (observation may be acceptable; no preop catecholamine blockade needed)"},
  {"id":"pheo-paraganglioma-3","topic":"Pheochromocytoma and paraganglioma preoperative preparation","domain":items[26]["domain"],"discipline":"anesthesia",
   "stem":"What is the standard treatment for catecholamine-secreting pheochromocytoma or paraganglioma?",
   "answer":"Removal (surgical resection) of catecholamine-secreting tumors is standard; without removal, patients are at risk for stroke, arrhythmia, and heart attack from dangerously high blood pressure.",
   "rationale":"Definitive cure requires elimination of the catecholamine source; chronic exposure to excess catecholamines causes cardiomyopathy and end-organ damage.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Pheochromocytoma & Paraganglioma","page":19}],"confusable_with":""},
  {"id":"pheo-paraganglioma-4","topic":"Pheochromocytoma and paraganglioma preoperative preparation","domain":items[26]["domain"],"discipline":"anesthesia",
   "stem":"When is observation acceptable for paraganglioma management?",
   "answer":"Observation is acceptable for small, asymptomatic, non-secreting head and neck paragangliomas.",
   "rationale":"Non-secreting head and neck paragangliomas have low malignant potential and slow growth; observation avoids surgical morbidity in patients where the benefit-risk ratio favors watchful waiting.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Pheochromocytoma & Paraganglioma","page":11}],"confusable_with":"catecholamine-secreting tumors (require resection)"}
]
kps.append({"_type":"illness_script","topic":"Pheochromocytoma and paraganglioma preoperative preparation","discipline":"anesthesia",
  "enabling_conditions":"Sporadic (most common), MEN2, VHL syndrome, NF1, SDH gene mutations; adrenal or extra-adrenal (paraganglioma)",
  "pathophysiology":"Catecholamine-secreting chromaffin cells release norepinephrine, epinephrine, and dopamine in episodic or sustained fashion; alpha/beta-adrenergic stimulation causes hypertension, tachycardia, arrhythmias, and cardiomyopathy",
  "time_course":"Often episodic attacks; surgical stress or tumor manipulation causes acute catecholamine crisis",
  "key_features":"Episodic hypertension, headache, diaphoresis (classic triad); palpitations, pallor; hypertensive emergency during induction or tumor manipulation",
  "consequence_if_missed":"Intraoperative hypertensive crisis, malignant arrhythmia, stroke, or cardiac arrest without preoperative alpha-blockade"})

# ── 1017 Physician Impairment & Substance Use Disorders ───────────────────────
kps += [
  {"id":"physician-impairment-1","topic":"Physician Impairment & Substance Use Disorders","domain":items[27]["domain"],"discipline":"medicine",
   "stem":"What behavioral signs in an anesthesia provider suggest possible substance use disorder or diversion?",
   "answer":"Signs include hostility, excessive time at hospital when off duty, volunteering for extra calls, refusing relief, requesting frequent bathroom breaks, and signing out disproportionate or increasing quantities of opioids.",
   "rationale":"Anesthesia providers have privileged access to potent opioids; diversion behaviors manifest as unusual patterns around opioid access that bypass normal oversight.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":48}],"confusable_with":"burnout without substance use"},
  {"id":"physician-impairment-2","topic":"Physician Impairment & Substance Use Disorders","domain":items[27]["domain"],"discipline":"medicine",
   "stem":"What treatment is typically recommended for an anesthesia provider diagnosed with a substance use disorder?",
   "answer":"Treatment generally involves referral to an inpatient facility that specializes in physician substance use disorders.",
   "rationale":"Anesthesia providers with substance use disorders require inpatient treatment given access to controlled substances; return-to-work decisions require structured monitoring programs.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":48}],"confusable_with":""},
  {"id":"physician-impairment-3","topic":"Physician Impairment & Substance Use Disorders","domain":items[27]["domain"],"discipline":"medicine",
   "stem":"What evidence-based approach is most effective for treating tobacco use disorder?",
   "answer":"Combination of counseling and pharmacotherapy is most effective; a quit date should be set (typically in 2-4 weeks), and abrupt cessation is more effective than gradual reduction.",
   "rationale":"Pharmacotherapy (varenicline, bupropion, NRT) combined with behavioral support doubles cessation rates compared with either alone; abrupt cessation reduces exposure faster.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":216}],"confusable_with":""},
  {"id":"physician-impairment-4","topic":"Physician Impairment & Substance Use Disorders","domain":items[27]["domain"],"discipline":"medicine",
   "stem":"What screening tool is used to detect alcohol use disorder and its equivalent for detecting alcohol dependence?",
   "answer":"AUDIT-C screens for unhealthy alcohol use; CAGE questionnaire detects alcohol dependence.",
   "rationale":"AUDIT-C (3 questions on frequency, quantity, binge drinking) is sensitive for any unhealthy use; CAGE (Cut down, Annoyed, Guilty, Eye-opener) is specific for dependence.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":212}],"confusable_with":"AUDIT-C (screening) vs CAGE (dependence) vs DAST (drug use)"}
]

# ── 1018 Pregnancy and obstetric considerations in non-obstetric surgery ───────
kps += [
  {"id":"pregnancy-nonob-surgery-1","topic":"Pregnancy and obstetric considerations in non-obstetric surgery","domain":items[28]["domain"],"discipline":"anesthesia",
   "stem":"What is the incidence of non-obstetric surgery during pregnancy and what are the most common indications?",
   "answer":"The overall incidence of non-obstetric surgery during pregnancy is 1-2%; most common indications are trauma, appendicitis, cholecystitis, and malignancy.",
   "rationale":"Pregnancy does not protect against surgical emergencies; management must balance maternal surgical need with fetal safety considerations including teratogenicity and uterine perfusion.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":626}],"confusable_with":""},
  {"id":"pregnancy-nonob-surgery-2","topic":"Pregnancy and obstetric considerations in non-obstetric surgery","domain":items[28]["domain"],"discipline":"anesthesia",
   "stem":"What additional management considerations apply to anesthesia for non-obstetric surgery in pregnancy beyond routine hemodynamic and ventilation management?",
   "answer":"Management must also address uterine perfusion (avoid hypotension, hypoxemia, hypocarbia), teratogenicity of anesthetic agents (especially first trimester), and fetal monitoring.",
   "rationale":"Uterine blood flow is pressure-dependent and autoregulation-limited; maternal hypotension directly reduces uteroplacental perfusion causing fetal hypoxia.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":626}],"confusable_with":""},
  {"id":"pregnancy-nonob-surgery-3","topic":"Pregnancy and obstetric considerations in non-obstetric surgery","domain":items[28]["domain"],"discipline":"anesthesia",
   "stem":"What is the highest risk period for pulmonary aspiration during obstetric anesthesia?",
   "answer":"The interval of complete loss of airway reflexes is when pulmonary aspiration risk is highest; if a difficult intubation is anticipated, awake intubation is indicated over rapid sequence induction.",
   "rationale":"Pregnant patients have delayed gastric emptying, increased gastric acid production, and reduced lower esophageal sphincter tone; aspiration during this window can cause Mendelson syndrome.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":545}],"confusable_with":""},
  {"id":"pregnancy-nonob-surgery-4","topic":"Pregnancy and obstetric considerations in non-obstetric surgery","domain":items[28]["domain"],"discipline":"anesthesia",
   "stem":"What etomidate dose is associated with minimal fetal cardiovascular effects at induction?",
   "answer":"At typical induction doses (0.3 mg/kg), etomidate has minimal effects on fetal cardiovascular function; larger doses of ketamine (>9 mg/kg) are associated with newborn depression.",
   "rationale":"Etomidate provides hemodynamic stability with minimal placental transfer effects at standard doses, making it useful for obstetric induction when hemodynamic stability is critical.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":618}],"confusable_with":"thiopental (historically used; ketamine alternative in hemorrhagic patients)"}
]

# ── 1019 Quality Improvement Methodology ──────────────────────────────────────
kps += [
  {"id":"qi-methodology-1","topic":"Quality Improvement Methodology","domain":items[29]["domain"],"discipline":"anesthesia",
   "stem":"What does the Physician Quality Reporting System (PQRS) encourage and what quality measures are relevant to anesthesia?",
   "answer":"PQRS encourages eligible professionals to submit quality care information to Medicare; anesthesia-relevant measures include timing of preoperative antibiotics and patient temperature in the PACU after colorectal surgery.",
   "rationale":"Process measures like antibiotic timing and normothermia are linked to outcome benefits (reduced SSI, reduced cardiac events); reporting drives adoption of evidence-based practices.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2211}],"confusable_with":""},
  {"id":"qi-methodology-2","topic":"Quality Improvement Methodology","domain":items[29]["domain"],"discipline":"anesthesia",
   "stem":"What did the 1999 Institute of Medicine report 'To Err Is Human' identify as the basis for quality improvement in healthcare?",
   "answer":"'To Err Is Human' identified anesthesia as an area with impressive safety improvements and called for system-level analysis of error rather than individual blame to drive quality improvement.",
   "rationale":"The report established the modern patient safety movement; its focus on system-level causes (vs. individual error) is the foundation of root cause analysis and FMEA approaches.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":853}],"confusable_with":""},
  {"id":"qi-methodology-3","topic":"Quality Improvement Methodology","domain":items[29]["domain"],"discipline":"anesthesia",
   "stem":"What is the purpose of the Anesthesia Quality Institute (AQI) in quality improvement?",
   "answer":"The AQI allows individual practices and physicians to compare their performance with national anesthesia data, enabling benchmarking and identification of quality gaps.",
   "rationale":"Comparative performance data drives quality improvement by identifying outliers and enabling best-practice adoption; the AQI provides anesthesia-specific national benchmarks.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2205}],"confusable_with":""}
]

# ── 1020 Radiofrequency Ablation (RFA) Techniques ────────────────────────────
kps += [
  {"id":"rfa-1","topic":"Radiofrequency Ablation (RFA) Techniques","domain":items[30]["domain"],"discipline":"anesthesia",
   "stem":"What is the physical mechanism of percutaneous radiofrequency ablation (RFA) for pain management?",
   "answer":"RFA relies on heat produced by radiofrequency current flow from an active electrode at the tip of a specialized needle, creating a controlled thermal lesion in targeted nerve tissue.",
   "rationale":"Tissue temperatures of 60-90 degrees C for 1-3 minutes ablate the nerve without causing excessive collateral damage; heat denatures proteins and disrupts nerve conduction.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1796}],"confusable_with":"cryoneurolysis (uses cold to produce temporary analgesia lasting weeks to months)"},
  {"id":"rfa-2","topic":"Radiofrequency Ablation (RFA) Techniques","domain":items[30]["domain"],"discipline":"anesthesia",
   "stem":"What are the most common clinical applications of radiofrequency ablation in pain management?",
   "answer":"RFA is most commonly used for trigeminal rhizotomy and medial branch (facet joint) rhizotomy; it has also been used for dorsal root rhizotomy and lumbar sympathectomy.",
   "rationale":"Medial branch RFA for cervicogenic/lumbar facet pain is the most performed pain intervention; controlled heat ablates the medial branch innervating the facet joint, providing durable analgesia.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1797}],"confusable_with":"epidural steroid injection (anti-inflammatory, not ablative)"},
  {"id":"rfa-3","topic":"Radiofrequency Ablation (RFA) Techniques","domain":items[30]["domain"],"discipline":"anesthesia",
   "stem":"What interventional options exist for cancer pain and what is the role of RFA among them?",
   "answer":"Cancer pain interventional options include nerve blocks with local anesthetics and steroid or neurolytic solution, radiofrequency ablation, neuromodulatory techniques, and multidisciplinary treatment.",
   "rationale":"RFA provides non-chemical neurolysis in cancer pain; it is particularly useful when pharmacotherapy is inadequate and surgery is not feasible, offering durable pain relief.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1756}],"confusable_with":""},
  {"id":"rfa-4","topic":"Radiofrequency Ablation (RFA) Techniques","domain":items[30]["domain"],"discipline":"anesthesia",
   "stem":"What rare serious complication is associated with cervical epidural steroid injections?",
   "answer":"Cervical epidural steroid injections are associated with a rare but serious risk of catastrophic complications including spinal cord infarction.",
   "rationale":"Particulate steroid emboli into a feeder artery or direct intravascular injection into radicular arteries can cause anterior spinal artery syndrome with permanent paralysis.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":828}],"confusable_with":"lumbar epidural steroid injections (lower but not zero risk)"}
]

# ── 1021 Restrictive lung disease and pulmonary hypertension ──────────────────
kps += [
  {"id":"restrictive-ld-pah-1","topic":"Restrictive lung disease and pulmonary hypertension","domain":items[31]["domain"],"discipline":"anesthesia",
   "stem":"What hemodynamic criteria define portopulmonary hypertension (POPH)?",
   "answer":"POPH requires mean pulmonary artery pressure (mPAP) greater than 25 mmHg at rest, pulmonary vascular resistance (PVR) greater than 240 dyn-s-cm-5, and a transpulmonary gradient greater than 12 mmHg (mPAP minus PAOP).",
   "rationale":"The elevated PVR and transpulmonary gradient distinguish POPH from passive pulmonary hypertension due to elevated left-heart filling pressures (PAOP elevated, PVR normal).",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1198}],"confusable_with":"passive pulmonary hypertension from left heart disease (elevated PAOP, normal PVR)"},
  {"id":"restrictive-ld-pah-2","topic":"Restrictive lung disease and pulmonary hypertension","domain":items[31]["domain"],"discipline":"anesthesia",
   "stem":"What is the gold standard for diagnosing pulmonary hypertension, and what additional testing guides treatment in idiopathic PH?",
   "answer":"Right heart catheterization (RHC) is the gold standard; vasoreactivity testing with inhaled NO (+response: decrease mPAP >=10 mmHg to mPAP <=40 mmHg with maintained or increased CO) guides treatment in idiopathic PH.",
   "rationale":"Vasoreactivity testing identifies patients who may respond to calcium channel blockers (the only proven benefit of CCBs in PH); non-responders require targeted PH therapy.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":56}],"confusable_with":"echocardiography (screens for PH but RHC required for definitive hemodynamic diagnosis)"},
  {"id":"restrictive-ld-pah-3","topic":"Restrictive lung disease and pulmonary hypertension","domain":items[31]["domain"],"discipline":"anesthesia",
   "stem":"What imaging findings suggest elevated pulmonary pressures on CT scan?",
   "answer":"CT findings of elevated pulmonary pressures include increased diameter of pulmonary vessels, possible right ventricular enlargement with bowing of the interventricular septum into the left ventricular lumen, and signs of pulmonary venous congestion.",
   "rationale":"Right heart pressure overload causes RV dilation; the interventricular septum shifts leftward (D-sign), reducing LV preload and cardiac output.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Pleural Effusion  Diagnosis","page":5}],"confusable_with":""},
  {"id":"restrictive-ld-pah-4","topic":"Restrictive lung disease and pulmonary hypertension","domain":items[31]["domain"],"discipline":"anesthesia",
   "stem":"What caution must be applied to sedative premedication in obese patients with pulmonary or sleep-related disease?",
   "answer":"Obese patients may be more sensitive to the respiratory depressant effects of sedative premedication; if used, these should be given in incremental doses and carefully titrated.",
   "rationale":"Obesity reduces FRC and respiratory reserve; sedatives can precipitate upper airway obstruction and hypoventilation, particularly in patients with obstructive sleep apnea.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":540}],"confusable_with":""}
]

# ── 1022 Root Cause Analysis (RCA) & Systems Thinking ────────────────────────
kps += [
  {"id":"rca-systems-1","topic":"Root Cause Analysis (RCA) & Systems Thinking","domain":items[32]["domain"],"discipline":"anesthesia",
   "stem":"What is the defining characteristic of root cause analysis compared to superficial causal analysis of adverse events?",
   "answer":"RCA is a systematic approach to finding the underlying cause(s) of an error or adverse event (rather than the superficial/proximate cause), using techniques such as the 5 Whys.",
   "rationale":"Addressing only proximate causes fails to prevent recurrence; RCA traces through causal chains to modifiable system factors (process gaps, missing protocols) that allowed the error.",
   "bloom":"recall","source":[{"book":"Curated Units","page":0}],"confusable_with":"incident reporting (identifies events but does not analyze causes)"},
  {"id":"rca-systems-2","topic":"Root Cause Analysis (RCA) & Systems Thinking","domain":items[32]["domain"],"discipline":"anesthesia",
   "stem":"When was root cause analysis originally developed and in what industry?",
   "answer":"Root cause analysis was developed by manufacturers in the 1950s to better understand industrial events; it was subsequently adapted to healthcare quality and patient safety.",
   "rationale":"Healthcare borrowed RCA from aviation and manufacturing safety frameworks; industrial reliability engineering methods translate well to complex high-stakes clinical systems.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":859}],"confusable_with":"FMEA (failure mode effects analysis - prospective, not reactive)"},
  {"id":"rca-systems-3","topic":"Root Cause Analysis (RCA) & Systems Thinking","domain":items[32]["domain"],"discipline":"anesthesia",
   "stem":"What is the 5 Whys technique in root cause analysis?",
   "answer":"The 5 Whys technique involves asking 'Why?' repeatedly (typically 5 times) after an adverse event until the root cause is identified. Example: patient fall -> siderail not up -> nurse unaware of fall risk -> risk assessment not completed -> no standard protocol for fall risk screening.",
   "rationale":"Iterative questioning moves analysis from proximate cause (siderail) to system-level root cause (missing standard process), enabling systematic rather than blame-based remediation.",
   "bloom":"apply","source":[{"book":"Curated Units","page":0}],"confusable_with":""},
  {"id":"rca-systems-4","topic":"Root Cause Analysis (RCA) & Systems Thinking","domain":items[32]["domain"],"discipline":"anesthesia",
   "stem":"What is the focus of RCA with respect to individual provider behavior?",
   "answer":"RCA focuses strictly on system processes and not on individual provider behavior; a causal factor chart examines every step of the process that resulted in the event.",
   "rationale":"Blame-free, system-focused analysis promotes reporting and psychological safety; provider behavior is shaped by system design, so system fixes have broader impact than punishing individuals.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":860}],"confusable_with":"peer review (evaluates individual provider competence and decision-making)"},
  {"id":"rca-systems-5","topic":"Root Cause Analysis (RCA) & Systems Thinking","domain":items[32]["domain"],"discipline":"anesthesia",
   "stem":"What is the role of the ASA in quality improvement and how does it compare performance across practices?",
   "answer":"The ASA sponsors the Anesthesia Quality Institute (AQI), which allows individual practices and physicians to compare their performance against a national database.",
   "rationale":"Peer comparison data reveals performance outliers; benchmarking motivates quality improvement by making variation visible and providing targets for improvement.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2205}],"confusable_with":""}
]

print(f"Total KPs: {len(kps)}")
scripts = sum(1 for k in kps if k.get("_type") == "illness_script")
pairs = sum(1 for k in kps if k.get("_type") == "confusable_pair")
regular = len(kps) - scripts - pairs
print(f"Regular KPs: {regular}, Scripts: {scripts}, Pairs: {pairs}")

with open("data/kp_full_part_30.json", "w", encoding="utf-8") as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Written OK")
