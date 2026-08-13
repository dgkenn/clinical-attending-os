import json

entries = []

# ── 175 Small Bowel Obstruction ─────────────────────────────────────────────
entries += [
  {"id":"sbo-01","topic":"Small Bowel Obstruction (SBO)","domain":"Surgery / Acute abdomen","discipline":"surgery",
   "stem":"What is the initial imaging modality of choice for suspected small bowel obstruction?",
   "answer":"Plain abdominal X-ray is the initial imaging of choice; findings include dilated small bowel loops and air-fluid levels on the upright view.",
   "rationale":"Plain films are fast, low-cost, and demonstrate the hallmark dilated loops + air-fluid levels that confirm obstruction before CT is obtained.",
   "bloom":"recall","source":[{"book":"StatPearls Bowel Obstruction","page":1}],"confusable_with":"Large bowel obstruction (colon dilation, haustral markings)"},
  {"id":"sbo-02","topic":"Small Bowel Obstruction (SBO)","domain":"Surgery / Acute abdomen","discipline":"surgery",
   "stem":"On CT of the abdomen for SBO, which finding specifically indicates bowel ischemia or inflammation?",
   "answer":"Bowel wall thickening on CT indicates ischemia or inflammation; mesenteric stranding suggests ischemia or impending perforation.",
   "rationale":"Ischemic bowel loses its normal thin wall as edema and hemorrhage accumulate; surrounding fat stranding reflects inflammatory exudate tracking into the mesentery.",
   "bloom":"apply","source":[{"book":"StatPearls Bowel Obstruction","page":2}],"confusable_with":"Free air (perforation) vs mesenteric stranding (ischemia)"},
  {"id":"sbo-03","topic":"Small Bowel Obstruction (SBO)","domain":"Surgery / Acute abdomen","discipline":"surgery",
   "stem":"What CT finding distinguishes a complete from a partial small bowel obstruction?",
   "answer":"Absence of contrast reaching the colon on CT indicates complete obstruction; partial obstruction allows some contrast to pass.",
   "rationale":"Complete mechanical obstruction prevents any luminal content from traversing the transition point, so no contrast (or gas) appears distal to the site.",
   "bloom":"apply","source":[{"book":"StatPearls Bowel Obstruction","page":2}],"confusable_with":"Functional ileus (gas throughout, no discrete transition point)"},
  {"id":"sbo-04","topic":"Small Bowel Obstruction (SBO)","domain":"Surgery / Acute abdomen","discipline":"surgery",
   "stem":"What is the most common etiology of small bowel obstruction in adults who have had prior abdominal surgery?",
   "answer":"Adhesions from prior abdominal surgery are the most common cause of SBO.",
   "rationale":"Post-surgical adhesions create fibrous bands that can trap or kink loops of small bowel, the dominant mechanism in adults with a surgical history.",
   "bloom":"recall","source":[{"book":"StatPearls Bowel Obstruction","page":3}],"confusable_with":"Incarcerated hernia (second most common cause)"},
  {"id":"sbo-05","topic":"Small Bowel Obstruction (SBO)","domain":"Surgery / Acute abdomen","discipline":"surgery",
   "stem":"A patient with SBO develops board-like rigidity, rebound tenderness, and guarding. What does this indicate and what is the immediate next step?",
   "answer":"Peritonitis signs (rigidity, rebound, guarding) indicate strangulation or perforation — a surgical emergency requiring immediate operative intervention.",
   "rationale":"Peritoneal signs indicate transmural ischemia or frank perforation with contamination of the peritoneal cavity, conditions that are uniformly fatal without urgent surgery.",
   "bloom":"analyze","source":[{"book":"StatPearls Bowel Obstruction","page":4}],"confusable_with":"Simple SBO (no peritoneal signs, may be managed non-operatively initially)"},
  {"id":"sbo-06","topic":"Small Bowel Obstruction (SBO)","domain":"Surgery / Acute abdomen","discipline":"surgery",
   "stem":"When strangulation is suspected in SBO, which additional labs and cultures are indicated?",
   "answer":"Amylase and lipase (may be elevated with strangulation); blood cultures if peritonitis or sepsis is suspected.",
   "rationale":"Strangulated bowel releases amylase from injured mucosa; bacteremia from translocation of gut flora mandates cultures to guide antibiotic therapy.",
   "bloom":"apply","source":[{"book":"StatPearls Bowel Obstruction","page":5}],"confusable_with":"Acute pancreatitis (elevated amylase/lipase without obstruction on CT)"},
  {"id":"sbo-07","topic":"Small Bowel Obstruction (SBO)","domain":"Surgery / Acute abdomen","discipline":"surgery",
   "stem":"A patient with no prior abdominal surgery presents with SBO. What uncommon etiology should be considered?",
   "answer":"In a 'virgin abdomen', adhesion-related SBO is rare; consider familial Mediterranean fever or recurrent serositis as causes.",
   "rationale":"Without prior surgical scarring, the rare causes of peritoneal adhesions — including hereditary periodic fever syndromes causing recurrent serositis — move up the differential.",
   "bloom":"analyze","source":[{"book":"StatPearls Bowel Obstruction","page":3}],"confusable_with":"Crohn's disease stricture (also causes SBO in non-surgical patients)"},
  {"_type":"illness_script","topic":"Small Bowel Obstruction (SBO)","discipline":"surgery",
   "enabling_conditions":"Prior abdominal surgery (adhesions), hernia, Crohn's disease, malignancy",
   "pathophysiology":"Mechanical obstruction → proximal bowel distension → increased intraluminal pressure → impaired venous return → ischemia → translocation/perforation",
   "time_course":"Hours to days; strangulation can develop within hours of complete obstruction",
   "key_features":"Crampy abdominal pain, vomiting, obstipation; dilated loops + air-fluid levels on XR; CT shows transition point ± bowel wall thickening",
   "consequence_if_missed":"Strangulation → bowel necrosis → perforation → sepsis → death"}
]

# ── 176 Spontaneous Bacterial Peritonitis ────────────────────────────────────
entries += [
  {"id":"sbp-01","topic":"Spontaneous Bacterial Peritonitis (SBP)","domain":"Internal medicine: hepatology/GI","discipline":"medicine",
   "stem":"What ascitic fluid cell count defines the diagnosis of spontaneous bacterial peritonitis?",
   "answer":"Ascitic fluid PMN count ≥ 250 cells/mcL in the absence of surgical peritonitis or perforation defines SBP.",
   "rationale":"The PMN threshold is the diagnostic standard because culture-negative SBP (i.e., organisms not recovered) is common; PMN elevation alone is sufficient to initiate treatment.",
   "bloom":"recall","source":[{"book":"Curated Units","page":0}],"confusable_with":"Secondary bacterial peritonitis (PMN ≥250 but caused by perforated viscus — requires surgery)"},
  {"id":"sbp-02","topic":"Spontaneous Bacterial Peritonitis (SBP)","domain":"Internal medicine: hepatology/GI","discipline":"medicine",
   "stem":"What ascitic protein level is a risk factor for SBP, and why?",
   "answer":"Ascitic fluid protein < 1 g/dL is a risk factor for SBP because low opsonic activity impairs bacterial clearance from the peritoneal fluid.",
   "rationale":"Complement and immunoglobulin concentrations in ascites track with protein content; protein < 1 g/dL leaves ascites nearly devoid of opsonins, enabling bacterial proliferation.",
   "bloom":"apply","source":[{"book":"Curated Units","page":0}],"confusable_with":"Exudative ascites (protein > 2.5 g/dL, suggests malignancy or TB peritonitis)"},
  {"id":"sbp-03","topic":"Spontaneous Bacterial Peritonitis (SBP)","domain":"Internal medicine: hepatology/GI","discipline":"medicine",
   "stem":"Why are cirrhotic patients particularly susceptible to SBP?",
   "answer":"Cirrhosis causes profound immunocompromise via complement dysfunction, impaired opsonization, and reduced phagocytic capacity.",
   "rationale":"The liver normally synthesizes complement and clears gut-translocated bacteria via Kupffer cells; cirrhotic dysfunction of both mechanisms allows bacterial seeding of ascites.",
   "bloom":"apply","source":[{"book":"Curated Units","page":0}],"confusable_with":"SBP in non-cirrhotic ascites (rare; from malignancy or cardiac ascites)"},
  {"id":"sbp-04","topic":"Spontaneous Bacterial Peritonitis (SBP)","domain":"Internal medicine: hepatology/GI","discipline":"medicine",
   "stem":"What is the approximate mortality of sepsis in a patient with underlying cirrhosis?",
   "answer":"Sepsis in cirrhotic patients carries approximately 40–60% mortality.",
   "rationale":"Cirrhosis severely blunts the ability to mount an effective immune response and handle hemodynamic stress, amplifying sepsis mortality well above that of non-cirrhotic patients.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1191}],"confusable_with":"Hepatorenal syndrome (functional renal failure triggered by sepsis in cirrhosis)"},
  {"id":"sbp-05","topic":"Spontaneous Bacterial Peritonitis (SBP)","domain":"Internal medicine: hepatology/GI","discipline":"medicine",
   "stem":"Approximately what percentage of hospitalized cirrhotic patients develop SBP?",
   "answer":"Approximately 10% of patients with cirrhosis develop SBP.",
   "rationale":"Gut bacterial translocation through the impaired intestinal barrier is common in advanced cirrhosis; roughly 1 in 10 cirrhotic inpatients will have SBP at any admission.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":94}],"confusable_with":""},
  {"_type":"illness_script","topic":"Spontaneous Bacterial Peritonitis (SBP)","discipline":"medicine",
   "enabling_conditions":"Cirrhosis with ascites, ascitic protein < 1 g/dL, prior SBP episode, active GI bleed",
   "pathophysiology":"Bacterial translocation across impaired gut mucosa → seeding of low-opsonic ascites → unchecked proliferation (no complement/phagocyte clearance)",
   "time_course":"Subacute onset over 24–72 h; may present without classic peritoneal signs in cirrhotic patients",
   "key_features":"Fever, abdominal pain/tenderness, worsening encephalopathy; ascitic PMN ≥ 250 cells/mcL; often culture-negative",
   "consequence_if_missed":"Septic shock, hepatorenal syndrome, death (mortality 40–60% in cirrhosis)"}
]

# ── 177 Syncope ──────────────────────────────────────────────────────────────
entries += [
  {"id":"syncope-01","topic":"Syncope: Evaluation and Management","domain":"Internal medicine: cardiology/neurology","discipline":"medicine",
   "stem":"What proportion of ED visits does syncope represent, and what makes risk stratification challenging?",
   "answer":"Syncope accounts for 1–3.5% of ED visits and 6% of hospital admissions; the challenge is that most causes are benign but life-threatening etiologies (cardiac, structural) must not be missed.",
   "rationale":"The broad differential — from benign vasovagal to immediately lethal arrhythmia — and the transient, self-resolving nature of the event make stratifying which patients need admission difficult.",
   "bloom":"recall","source":[{"book":"StatPearls Syncope","page":2}],"confusable_with":"Seizure (post-ictal confusion, tongue biting, incontinence distinguish)"},
  {"id":"syncope-02","topic":"Syncope: Evaluation and Management","domain":"Internal medicine: cardiology/neurology","discipline":"medicine",
   "stem":"What two minimum investigations should be performed in an older adult presenting with syncope?",
   "answer":"ECG and blood glucose are the minimum investigations in older adults with syncope.",
   "rationale":"Arrhythmia and hypoglycemia are common, reversible, potentially lethal causes of transient loss of consciousness in the elderly that an ECG and glucose immediately screen for.",
   "bloom":"apply","source":[{"book":"StatPearls Syncope","page":4}],"confusable_with":""},
  {"id":"syncope-03","topic":"Syncope: Evaluation and Management","domain":"Internal medicine: cardiology/neurology","discipline":"medicine",
   "stem":"What first-line interventions are used for reflex (vasovagal) syncope with associated volume depletion?",
   "answer":"Compression stockings and IV fluids for volume depletion; midodrine is used for refractory reflex syncope.",
   "rationale":"Venous pooling and hypovolemia trigger the vasovagal reflex; compression stockings reduce venous pooling and fluids restore preload, while midodrine (alpha-agonist) raises standing blood pressure in refractory cases.",
   "bloom":"apply","source":[{"book":"StatPearls Syncope","page":5}],"confusable_with":"Orthostatic hypotension (treated similarly but distinct from classic vasovagal)"},
  {"id":"syncope-04","topic":"Syncope: Evaluation and Management","domain":"Internal medicine: cardiology/neurology","discipline":"medicine",
   "stem":"In hypertrophic cardiomyopathy (HCM), what is the clinical significance of syncope?",
   "answer":"Syncope is a presenting symptom of HCM and indicates high risk for sudden cardiac death from dynamic outflow obstruction or arrhythmia.",
   "rationale":"Exertional syncope in HCM reflects either LVOT obstruction worsened by catecholamine-mediated vasodilation or ventricular tachyarrhythmia; either mechanism carries significant mortality risk without intervention.",
   "bloom":"analyze","source":[{"book":"Miller","page":494}],"confusable_with":"Aortic stenosis (also exertional syncope, but fixed obstruction rather than dynamic)"},
  {"_type":"illness_script","topic":"Syncope: Evaluation and Management","discipline":"medicine",
   "enabling_conditions":"Dehydration, prolonged standing, Valsalva (vasovagal); structural heart disease (HCM, AS); arrhythmia (long QT, WPW, sick sinus)",
   "pathophysiology":"Transient global cerebral hypoperfusion from BP/CO drop → loss of consciousness; spontaneous recovery when supine restores perfusion",
   "time_course":"Sudden onset, seconds to < 1 min loss of consciousness, rapid full recovery (distinguishes from seizure/TIA)",
   "key_features":"Prodrome (nausea, diaphoresis, tunnel vision) in vasovagal; no prodrome in cardiac; ECG/glucose mandatory in elderly",
   "consequence_if_missed":"Missed cardiac/structural cause → sudden cardiac death; missed hypoglycemia → prolonged neuroglycopenia"}
]

# ── 178 Thyroid Storm ────────────────────────────────────────────────────────
entries += [
  {"id":"thyroid-storm-01","topic":"Thyroid Storm","domain":"Internal medicine: endocrinology","discipline":"medicine",
   "stem":"What are the four cardinal clinical features of thyroid storm?",
   "answer":"Hyperpyrexia, tachycardia, altered consciousness (agitation, delirium, or coma), and hypotension are the cardinal features of thyroid storm.",
   "rationale":"Massive thyroid hormone excess produces a hypermetabolic state with uncontrolled thermogenesis, adrenergic hyperactivity causing tachycardia, CNS excitation progressing to obtundation, and circulatory collapse.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1226}],"confusable_with":"Malignant hyperthermia (rigidity + elevated CK + respiratory/lactic acidosis distinguishes MH)"},
  {"id":"thyroid-storm-02","topic":"Thyroid Storm","domain":"Internal medicine: endocrinology","discipline":"medicine",
   "stem":"What three features distinguish thyroid storm from malignant hyperthermia in the differential of hyperpyrexia in the OR?",
   "answer":"Thyroid storm has NO muscle rigidity, NO significantly elevated CK, and NO marked lactic or respiratory acidosis — all of which are hallmarks of MH.",
   "rationale":"MH involves pathological calcium release from skeletal muscle producing rigidity and massive ATP consumption with lactate and CO2 generation; thyroid storm is a hormonal/adrenergic crisis without primary muscle pathology.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1227}],"confusable_with":"Neuroleptic malignant syndrome (also has rigidity + elevated CK, differentiating from thyroid storm)"},
  {"id":"thyroid-storm-03","topic":"Thyroid Storm","domain":"Internal medicine: endocrinology","discipline":"medicine",
   "stem":"Why is aspirin contraindicated as an antipyretic in thyroid storm?",
   "answer":"Aspirin displaces thyroid hormone from plasma proteins, acutely increasing free (active) thyroid hormone levels and worsening the storm.",
   "rationale":"Thyroid hormones are highly protein-bound; aspirin competes for binding sites on albumin and TBG, releasing free T3/T4 into circulation at the worst possible time.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":86}],"confusable_with":"Acetaminophen (safe antipyretic in thyroid storm; does not displace thyroid hormone)"},
  {"id":"thyroid-storm-04","topic":"Thyroid Storm","domain":"Internal medicine: endocrinology","discipline":"medicine",
   "stem":"What are the four key components of treatment for thyroid storm?",
   "answer":"Cooling + acetaminophen (NOT aspirin), generous IV fluids, vasopressors for hypotension, and ventricular rate control (beta-blocker).",
   "rationale":"Cooling addresses hyperpyrexia; fluids counter the hypermetabolic fluid deficit; vasopressors support refractory vasodilation; rate control reduces the adrenergic tachycardia driving high-output failure.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1226}],"confusable_with":""},
  {"_type":"illness_script","topic":"Thyroid Storm","discipline":"medicine",
   "enabling_conditions":"Pre-existing hyperthyroidism (often undiagnosed) precipitated by surgery, infection, trauma, or iodine load",
   "pathophysiology":"Massive free thyroid hormone surge → extreme adrenergic activation → thermogenesis, tachyarrhythmia, high-output cardiac failure, CNS excitation",
   "time_course":"Acute onset intraoperatively or within hours of precipitant; life-threatening within 24 h if untreated",
   "key_features":"Hyperpyrexia, tachycardia, agitation/delirium, hypotension; NO rigidity, NO elevated CK (distinguishes from MH)",
   "consequence_if_missed":"Refractory heart failure, multi-organ failure, death"},
  {"_type":"confusable_pair","topic_a":"Thyroid Storm","topic_b":"Malignant Hyperthermia",
   "discriminator":"MH has muscle rigidity + elevated CK + marked lactic/respiratory acidosis; thyroid storm has none of these — both have hyperpyrexia and tachycardia"}
]

# ── 179 RBC Transfusion ──────────────────────────────────────────────────────
entries += [
  {"id":"rbc-transfusion-01","topic":"Transfusion medicine: red blood cell transfusion","domain":"Anesthesia / Perioperative medicine","discipline":"anesthesia",
   "stem":"What preservative solution is used for blood storage, and what are its components?",
   "answer":"CPDA-1 (citrate-phosphate-dextrose-adenine) is the standard blood storage preservative.",
   "rationale":"Citrate chelates calcium to prevent clotting; phosphate buffers pH; dextrose fuels RBC glycolysis; adenine supports ATP synthesis — together extending RBC viability.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1958}],"confusable_with":""},
  {"id":"rbc-transfusion-02","topic":"Transfusion medicine: red blood cell transfusion","domain":"Anesthesia / Perioperative medicine","discipline":"anesthesia",
   "stem":"At what blood loss threshold should RBC transfusion be considered in a patient with normal baseline hematocrit?",
   "answer":"Transfusion is generally considered after blood loss exceeding 10–20% of blood volume in a patient with normal hematocrit.",
   "rationale":"Below the 10–20% threshold, compensatory mechanisms (increased CO, oxygen extraction) maintain tissue oxygen delivery; beyond this, the oxygen-carrying deficit becomes clinically significant.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1960}],"confusable_with":"Anemic patients (threshold shifts — transfuse at lower absolute loss due to reduced reserve)"},
  {"id":"rbc-transfusion-03","topic":"Transfusion medicine: red blood cell transfusion","domain":"Anesthesia / Perioperative medicine","discipline":"anesthesia",
   "stem":"What is cell salvage, and what is the main technical hazard to red cells during the process?",
   "answer":"Cell salvage centrifuges, washes, and returns the patient's own shed blood; excessive suction pressure causes red cell trauma (hemolysis).",
   "rationale":"High shear forces at the suction tip lyse erythrocytes; washed salvaged blood contains fewer intact RBCs and releases free hemoglobin if suction is too aggressive.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1965}],"confusable_with":""},
  {"id":"rbc-transfusion-04","topic":"Transfusion medicine: red blood cell transfusion","domain":"Anesthesia / Perioperative medicine","discipline":"anesthesia",
   "stem":"What is citrate toxicity, when does it occur, and what is the hemodynamic consequence?",
   "answer":"Citrate toxicity causes hypocalcemia and cardiac depression when blood is transfused faster than ~1 unit per 5 minutes, because citrate overwhelms hepatic metabolism.",
   "rationale":"Citrate in stored blood chelates ionized calcium; at slow rates the liver metabolizes citrate quickly, but massive rapid transfusion outpaces hepatic clearance, causing ionized hypocalcemia that depresses myocardial contractility.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1963}],"confusable_with":"Hyperkalemia from stored blood (also occurs with massive transfusion, distinct mechanism)"},
  {"id":"rbc-transfusion-05","topic":"Transfusion medicine: red blood cell transfusion","domain":"Anesthesia / Perioperative medicine","discipline":"anesthesia",
   "stem":"What does a 'type and screen' test and how long does it take?",
   "answer":"Type and screen performs ABO/Rh typing and an indirect Coombs test for unexpected antibodies; it requires approximately 45 minutes.",
   "rationale":"The indirect Coombs test detects patient antibodies against a panel of donor RBC antigens, enabling rapid crossmatch if transfusion is unexpectedly needed during surgery.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1969}],"confusable_with":"Type and crossmatch (specific donor unit compatibility tested — needed when transfusion is likely)"},
  {"id":"rbc-transfusion-06","topic":"Transfusion medicine: red blood cell transfusion","domain":"Anesthesia / Perioperative medicine","discipline":"anesthesia",
   "stem":"When is autologous pre-donation indicated?",
   "answer":"Autologous donation is appropriate for elective surgery with a high probability of transfusion, allowing the patient's own blood to be collected in advance.",
   "rationale":"Autologous transfusion eliminates alloimmunization, infectious transmission, and most transfusion reactions, making it the safest option when planned well before surgery.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1967}],"confusable_with":"Cell salvage (intraoperative, not pre-donated)"}
]

# ── 180 Transfusion Reactions ────────────────────────────────────────────────
entries += [
  {"id":"transfusion-rx-01","topic":"Transfusion reactions","domain":"Anesthesia / Perioperative medicine","discipline":"anesthesia",
   "stem":"What defines a 'massive transfusion' and what is the Stanford massive transfusion guideline ratio?",
   "answer":"Massive transfusion = transfusion of > 1 blood volume (~10 units pRBC) in 24 hours. Stanford MTG: 6 pRBC + 4 FFP + 1 platelet apheresis unit.",
   "rationale":"Replacing one blood volume with only pRBCs causes dilutional coagulopathy and thrombocytopenia; balanced component therapy with FFP and platelets prevents the lethal triad of trauma (acidosis, hypothermia, coagulopathy).",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":51}],"confusable_with":"1:1:1 ratio (trauma protocol — equal parts RBC:FFP:platelets)"},
  {"id":"transfusion-rx-02","topic":"Transfusion reactions","domain":"Anesthesia / Perioperative medicine","discipline":"anesthesia",
   "stem":"What is the 1:1:1 transfusion ratio and in what clinical context is it used?",
   "answer":"1:1:1 ratio (RBC:FFP:platelets) is the trauma massive transfusion protocol, designed to approximate whole blood and prevent dilutional coagulopathy.",
   "rationale":"Trauma patients lose all blood components simultaneously; replacing with packed RBCs alone depletes coagulation factors and platelets, so equal-ratio replacement restores hemostatic function.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1963}],"confusable_with":"Stanford MTG (6:4:1 ratio — similar philosophy, different numeric formula)"},
  {"id":"transfusion-rx-03","topic":"Transfusion reactions","domain":"Anesthesia / Perioperative medicine","discipline":"anesthesia",
   "stem":"A patient develops fever, flank pain, hemoglobinuria, and hypotension minutes after starting a transfusion. What are the FIRST three actions?",
   "answer":"(1) STOP the transfusion immediately. (2) Notify the blood bank. (3) Recheck unit label vs. patient ID bracelet.",
   "rationale":"Acute hemolytic transfusion reaction from ABO incompatibility requires immediate cessation to limit antibody-antigen complex formation; the blood bank must be notified and the ID error identified to prevent further harm.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":740}],"confusable_with":"Febrile non-hemolytic reaction (fever without hemolysis; treat with antipyretics, not automatic stop)"},
  {"id":"transfusion-rx-04","topic":"Transfusion reactions","domain":"Anesthesia / Perioperative medicine","discipline":"anesthesia",
   "stem":"After stopping a suspected hemolytic transfusion reaction, what two laboratory tests are immediately drawn?",
   "answer":"Draw blood to check for hemoglobin in plasma (hemolysis) and repeat compatibility testing (crossmatch).",
   "rationale":"Plasma hemoglobin confirms intravascular hemolysis; repeat crossmatch identifies whether the original compatibility test was performed on the correct patient sample or if an error occurred.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":740}],"confusable_with":""},
  {"id":"transfusion-rx-05","topic":"Transfusion reactions","domain":"Anesthesia / Perioperative medicine","discipline":"anesthesia",
   "stem":"What is HIT, and what distinguishes it from simple heparin-induced thrombocytopenia?",
   "answer":"HIT (heparin-induced thrombocytopenia with thrombosis) is caused by heparin-dependent PF4 antibodies that activate platelets, leading to thrombocytopenia AND thromboembolism — not just low platelet count.",
   "rationale":"PF4-heparin immune complexes bind and activate platelet FcγRIIa receptors causing platelet consumption and a prothrombotic state; the hallmark is paradoxical thrombosis despite low platelet count.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":740}],"confusable_with":"Non-immune heparin-associated thrombocytopenia (mild, no thrombosis, resolves without stopping heparin)"},
  {"_type":"illness_script","topic":"Transfusion reactions","discipline":"anesthesia",
   "enabling_conditions":"Blood product administration; ABO incompatibility (acute hemolytic), leukocyte antibodies (febrile non-hemolytic), IgA deficiency (anaphylactic), fluid overload (TACO), lung injury (TRALI)",
   "pathophysiology":"Acute hemolytic: ABO antibody → complement activation → intravascular hemolysis → renal failure; TRALI: donor anti-HLA antibodies → neutrophil activation → capillary leak",
   "time_course":"Acute hemolytic: within minutes; TRALI: within 6 h; TACO: within 6 h; febrile: within 1–2 h",
   "key_features":"Hemolytic: fever, flank pain, hemoglobinuria, hypotension; TRALI: bilateral pulmonary infiltrates, hypoxia, fever (no elevated CVP); TACO: hypoxia + elevated CVP",
   "consequence_if_missed":"Acute hemolytic → DIC, renal failure, death; TRALI → ARDS"}
]

# ── 181 Upper GI Bleed ───────────────────────────────────────────────────────
entries += [
  {"id":"ugib-01","topic":"Upper GI Bleed: Initial Evaluation & Risk Stratification","domain":"Internal medicine: gastroenterology","discipline":"medicine",
   "stem":"How is an upper GI bleed anatomically defined?",
   "answer":"UGIB is defined as bleeding proximal to the ligament of Treitz.",
   "rationale":"The ligament of Treitz marks the duodenojejunal junction; bleeding proximal to this landmark presents as hematemesis or melena whereas distal bleeding typically causes hematochezia.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":70}],"confusable_with":"Lower GIB (distal to ligament of Treitz, typically hematochezia)"},
  {"id":"ugib-02","topic":"Upper GI Bleed: Initial Evaluation & Risk Stratification","domain":"Internal medicine: gastroenterology","discipline":"medicine",
   "stem":"What is the positive likelihood ratio of melena for localizing GI bleeding to the upper tract?",
   "answer":"Melena has a +LR of 25 for UGIB.",
   "rationale":"The dark, tarry stool of melena results from hemoglobin oxidation by gastric acid and gut bacteria, which requires ≥14 hours of transit — placing the source in the upper tract.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":70}],"confusable_with":"Hematochezia (bright red per rectum, +LR for lower GIB — though brisk UGIB can also cause hematochezia)"},
  {"id":"ugib-03","topic":"Upper GI Bleed: Initial Evaluation & Risk Stratification","domain":"Internal medicine: gastroenterology","discipline":"medicine",
   "stem":"What BUN/creatinine ratio supports a diagnosis of UGIB and what is the specificity threshold?",
   "answer":"BUN/Cr > 30 has a +LR of 7.5 for UGIB; BUN/Cr > 35 is approximately 100% specific.",
   "rationale":"Blood in the upper GI tract is digested and absorbed as protein, raising BUN disproportionately to creatinine; the ratio exceeds 35 almost exclusively in UGIB.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":70}],"confusable_with":"AKI (BUN/Cr ratio typically < 20 unless pre-renal; lower GIB typically BUN/Cr < 20)"},
  {"id":"ugib-04","topic":"Upper GI Bleed: Initial Evaluation & Risk Stratification","domain":"Internal medicine: gastroenterology","discipline":"medicine",
   "stem":"A patient with bright red blood per rectum has a BUN/Cr of 38. What does this suggest?",
   "answer":"Despite hematochezia, a BUN/Cr > 35 strongly suggests an UGIB source (brisk bleed) rather than lower GIB.",
   "rationale":"Brisk UGIB can overwhelm colonic transit and present as hematochezia; the markedly elevated BUN/Cr from protein digestion exposes the upper-tract origin.",
   "bloom":"analyze","source":[{"book":"Intern Notes","page":13}],"confusable_with":"Lower GIB (BUN/Cr typically < 20 in true lower source)"},
  {"id":"ugib-05","topic":"Upper GI Bleed: Initial Evaluation & Risk Stratification","domain":"Internal medicine: gastroenterology","discipline":"medicine",
   "stem":"What does hematemesis definitively indicate about the location of GI bleeding?",
   "answer":"Hematemesis indicates a bleeding source proximal to the ligament of Treitz.",
   "rationale":"Vomiting blood requires the source to be within reach of retrograde emesis — stomach or proximal duodenum — definitively localizing UGIB.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":70}],"confusable_with":"Coffee-ground emesis (older blood, also UGIB but lower-acuity rate of bleeding)"}
]

# ── 182 Urinalysis Interpretation (thin chunks) ──────────────────────────────
entries += [
  {"id":"ua-interp-01","topic":"Urinalysis Interpretation","domain":"Internal medicine: nephrology","discipline":"medicine",
   "stem":"Why does serum creatinine only approximate GFR accurately at steady state?",
   "answer":"Serum creatinine reflects GFR at steady state because creatinine production and excretion must be balanced; in acute changes, creatinine lags behind true GFR changes.",
   "rationale":"Creatinine rises only as it accumulates with reduced filtration; in acute kidney injury, a normal-appearing creatinine may mask significant GFR decline in the first 24–48 hours.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":99}],"confusable_with":"Cystatin C (less affected by muscle mass and steady-state lag)"},
  {"id":"ua-interp-02","topic":"Urinalysis Interpretation","domain":"Internal medicine: nephrology","discipline":"medicine",
   "stem":"Which common medications falsely elevate serum creatinine without affecting true GFR?",
   "answer":"Trimethoprim, H2 blockers (e.g., cimetidine), and dronedarone inhibit tubular creatinine secretion, raising serum creatinine without changing GFR.",
   "rationale":"These drugs competitively block the organic cation transporter responsible for tubular creatinine secretion, causing a benign apparent rise in creatinine that does not reflect reduced filtration.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":99}],"confusable_with":"True AKI (distinguish by absence of other AKI markers, stable urine output, drug timing)"},
  {"id":"ua-interp-03","topic":"Urinalysis Interpretation","domain":"Internal medicine: nephrology","discipline":"medicine",
   "stem":"For reliable albuminuria or proteinuria measurement in children per KDIGO 2024, when should the urine sample be collected?",
   "answer":"KDIGO 2024 recommends first-morning urine for albuminuria/proteinuria assessment in children.",
   "rationale":"First-morning urine avoids orthostatic (postural) proteinuria, which is benign and common in children and adolescents — a timed or random sample may falsely suggest pathological proteinuria.",
   "bloom":"recall","source":[{"book":"KDIGO 2024 CKD","page":39}],"confusable_with":"24-hour urine collection (older gold standard, now largely replaced by spot albumin:creatinine ratio)"},
  {"id":"ua-interp-04","topic":"Urinalysis Interpretation","domain":"Internal medicine: nephrology","discipline":"medicine",
   "stem":"A patient with new creatinine of 2.1 mg/dL was started on trimethoprim-sulfamethoxazole 3 days ago for a UTI. Urinalysis is normal. What is the most likely explanation?",
   "answer":"Trimethoprim inhibits tubular creatinine secretion, causing a spurious rise in serum creatinine without true GFR reduction; urinalysis is normal because renal parenchyma is unaffected.",
   "rationale":"This is a pharmacological effect on creatinine handling, not nephrotoxicity; the normal urinalysis (no casts, no hematuria/proteinuria) supports a non-structural cause of the creatinine rise.",
   "bloom":"analyze","source":[{"book":"MGH Housestaff Manual","page":99}],"confusable_with":"TMP-SMX-induced AIN (interstitial nephritis — would have pyuria, eosinophiluria, elevated creatinine with urinalysis changes)"}
]

# ── 183 VTE Prophylaxis ──────────────────────────────────────────────────────
entries += [
  {"id":"vte-ppx-01","topic":"VTE prophylaxis","domain":"Internal medicine / Surgery: thromboembolism","discipline":"medicine",
   "stem":"What is the standard UFH dose for VTE prophylaxis, and how does obesity change dosing?",
   "answer":"Standard UFH prophylaxis: 5,000 units SQ BID–TID. In obesity, increase to 5,000–7,500 units TID.",
   "rationale":"Standard-dose UFH is inadequate in obese patients due to increased volume of distribution and altered heparin binding; higher doses are needed to achieve prophylactic anti-Xa levels.",
   "bloom":"recall","source":[{"book":"Miller","page":773}],"confusable_with":"Therapeutic UFH dosing (weight-based IV, 80 units/kg bolus + 18 units/kg/h — far higher than prophylaxis)"},
  {"id":"vte-ppx-02","topic":"VTE prophylaxis","domain":"Internal medicine / Surgery: thromboembolism","discipline":"medicine",
   "stem":"When is mechanical thromboprophylaxis preferred over pharmacological VTE prophylaxis?",
   "answer":"Mechanical prophylaxis (compression stockings, intermittent pneumatic compression devices) is preferred when bleeding risk is increased.",
   "rationale":"In patients with high bleeding risk (recent surgery, thrombocytopenia, active bleeding), pharmacological anticoagulation is contraindicated; mechanical compression maintains venous flow without hemostatic impairment.",
   "bloom":"apply","source":[{"book":"StatPearls","page":4}],"confusable_with":""},
  {"id":"vte-ppx-03","topic":"VTE prophylaxis","domain":"Internal medicine / Surgery: thromboembolism","discipline":"medicine",
   "stem":"What VTE prophylaxis agent is recommended for moderate-risk patients and for high-risk trauma/orthopedic patients?",
   "answer":"LMWH is recommended for both moderate VTE risk and high-risk trauma/orthopedic surgical patients.",
   "rationale":"LMWH provides predictable anti-Xa activity with once or twice-daily dosing; it is the evidence-based standard for moderate and high-risk categories (orthopedic, trauma) over UFH due to superior efficacy data.",
   "bloom":"recall","source":[{"book":"StatPearls","page":3}],"confusable_with":"UFH (preferred in renal failure, cancer inpatients with low GFR — LMWH renally cleared)"},
  {"id":"vte-ppx-04","topic":"VTE prophylaxis","domain":"Internal medicine / Surgery: thromboembolism","discipline":"medicine",
   "stem":"Why might withholding VTE prophylaxis in some hypercoagulable states paradoxically increase thrombosis risk?",
   "answer":"In some conditions, pro-coagulant factors may not be suppressed as much as anticoagulant factors when prophylaxis is withheld, paradoxically elevating net clotting potential.",
   "rationale":"Coagulation is a balance between pro- and anticoagulant proteins; in certain disease states (e.g., liver disease), anticoagulant factors (protein C, S) decline disproportionately, creating net thrombophilia despite 'low' factor levels.",
   "bloom":"analyze","source":[{"book":"StatPearls","page":3}],"confusable_with":""},
  {"id":"vte-ppx-05","topic":"VTE prophylaxis","domain":"Internal medicine / Surgery: thromboembolism","discipline":"medicine",
   "stem":"Which VTE prophylaxis agent is preferred in cancer inpatients with low GFR?",
   "answer":"UFH (unfractionated heparin) is preferred in cancer inpatients with low GFR because LMWH is renally cleared and accumulates with renal impairment.",
   "rationale":"LMWH relies on renal excretion; in significant renal dysfunction, anti-Xa levels rise unpredictably, increasing bleeding risk — UFH is cleared hepatically and is safer.",
   "bloom":"apply","source":[{"book":"StatPearls","page":4}],"confusable_with":"LMWH (preferred in cancer with normal renal function — superior to UFH for cancer-associated VTE)"}
]

# ── 184 Volume Status Assessment ────────────────────────────────────────────
entries += [
  {"id":"volume-01","topic":"Volume Status Assessment","domain":"Anesthesia / Critical care","discipline":"anesthesia",
   "stem":"What clinical signs indicate hypovolemia on physical examination?",
   "answer":"Hypovolemia signs: decreased skin turgor, thready pulse, dry mucous membranes, tachycardia, orthostasis, decreased urine output, and rising hematocrit.",
   "rationale":"Volume depletion reduces venous return, triggering tachycardia and peripheral vasoconstriction (thready pulse); renal conservation of water reduces UOP; hemoconcentration raises Hct.",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":46}],"confusable_with":"Cardiac tamponade (hypotension + tachycardia but with elevated JVP, not decreased)"},
  {"id":"volume-02","topic":"Volume Status Assessment","domain":"Anesthesia / Critical care","discipline":"anesthesia",
   "stem":"What ultrasound finding of the inferior vena cava indicates acute significant blood loss?",
   "answer":"A nearly collapsed (flat) IVC on ultrasound indicates acute blood loss and severe hypovolemia.",
   "rationale":"The IVC fills with venous return; acute hemorrhage dramatically reduces central venous pressure and IVC transmural pressure, causing near-complete collapse visible on subxiphoid ultrasound.",
   "bloom":"apply","source":[{"book":"Stanford CA-1","page":46}],"confusable_with":"Plethoric IVC with reduced respiratory variation (suggests elevated CVP/volume overload)"},
  {"id":"volume-03","topic":"Volume Status Assessment","domain":"Anesthesia / Critical care","discipline":"anesthesia",
   "stem":"What are the radiographic signs of pulmonary volume overload?",
   "answer":"Increased pulmonary vascular markings, Kerley B lines, and diffuse alveolar infiltrates on CXR indicate radiographic volume overload.",
   "rationale":"Elevated pulmonary capillary wedge pressure forces fluid into interstitial (Kerley B lines = fluid in interlobular septa) then alveolar spaces (diffuse infiltrates), with increased vascular markings from pulmonary venous hypertension.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1947}],"confusable_with":"ARDS (bilateral alveolar infiltrates but not cardiogenic; normal CVP/PCWP)"},
  {"id":"volume-04","topic":"Volume Status Assessment","domain":"Anesthesia / Critical care","discipline":"anesthesia",
   "stem":"What is stroke volume variation (SVV) and what threshold indicates fluid responsiveness in a mechanically ventilated patient?",
   "answer":"SVV > 15% during controlled mechanical ventilation indicates fluid responsiveness; normal SVV is < 10–15%.",
   "rationale":"Positive pressure ventilation cyclically alters venous return; a large SVV (>15%) means the heart is operating on the steep portion of the Frank-Starling curve and will increase CO with a fluid bolus.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1946}],"confusable_with":"Pulse pressure variation (PPV — similar concept, also >13% suggests fluid responsiveness)"},
  {"id":"volume-05","topic":"Volume Status Assessment","domain":"Anesthesia / Critical care","discipline":"anesthesia",
   "stem":"What signs indicate hypervolemia on physical examination?",
   "answer":"Hypervolemia signs: pitting edema, pulmonary rales, wheezing (cardiac asthma), and elevated jugular venous pressure (JVP).",
   "rationale":"Excess intravascular volume raises capillary hydrostatic pressure, driving fluid into interstitial spaces (edema) and alveoli (rales/wheezing), with elevated CVP visible as raised JVP.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1947}],"confusable_with":"Bronchospasm (wheezing without edema or elevated JVP)"}
]

# ── 185 Acetaminophen ────────────────────────────────────────────────────────
entries += [
  {"id":"apap-01","topic":"Acetaminophen (Paracetamol)","domain":"Pharmacology / Analgesia","discipline":"anesthesia",
   "stem":"What routes of administration are available for acetaminophen in the perioperative setting?",
   "answer":"Acetaminophen is available orally, rectally, and intravenously (IV preparation: Ofirmev).",
   "rationale":"The IV formulation (Ofirmev) allows acetaminophen delivery when the oral route is unavailable perioperatively, providing a parenteral non-opioid analgesic option.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1757}],"confusable_with":"Ketorolac (also IV non-opioid but an NSAID with different contraindication profile)"},
  {"id":"apap-02","topic":"Acetaminophen (Paracetamol)","domain":"Pharmacology / Analgesia","discipline":"anesthesia",
   "stem":"What is acetaminophen's role in multimodal analgesia and what is its perioperative benefit?",
   "answer":"Acetaminophen is a core component of multimodal analgesia (oral/rectal/parenteral); preoperative oral administration reduces postoperative opioid requirements.",
   "rationale":"Preemptive acetaminophen blunts central sensitization and provides baseline analgesia, reducing the opioid dose needed postoperatively and thereby decreasing opioid-related side effects.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1831}],"confusable_with":"NSAIDs (also reduce opioid consumption but different mechanism and contraindications)"},
  {"id":"apap-03","topic":"Acetaminophen (Paracetamol)","domain":"Pharmacology / Analgesia","discipline":"anesthesia",
   "stem":"What is the antidote for acetaminophen overdose?",
   "answer":"N-acetylcysteine (NAC) is the antidote for acetaminophen overdose.",
   "rationale":"NAC replenishes hepatic glutathione stores, allowing detoxification of NAPQI (the toxic acetaminophen metabolite), preventing centrilobular hepatic necrosis.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2160}],"confusable_with":"Flumazenil (benzodiazepine antidote), naloxone (opioid antidote) — different drug classes"}
]

# ── 186 COPD/Asthma Preoperative ─────────────────────────────────────────────
entries += [
  {"id":"copd-preop-01","topic":"COPD and asthma — preoperative optimization","domain":"Anesthesia / Pulmonology","discipline":"anesthesia",
   "stem":"What FEV1 threshold in COPD patients is associated with dyspnea on exertion?",
   "answer":"FEV1 < 50% predicted (approximately 1.2–1.5 L) is associated with dyspnea on exertion in COPD patients.",
   "rationale":"Below 50% predicted FEV1, expiratory flow limitation is severe enough that the increased ventilatory demand of ordinary exertion can no longer be met without symptoms.",
   "bloom":"recall","source":[{"book":"Miller","page":784}],"confusable_with":"FEV1/FVC < 0.70 (diagnostic criterion for obstruction, not the symptom threshold)"},
  {"id":"copd-preop-02","topic":"COPD and asthma — preoperative optimization","domain":"Anesthesia / Pulmonology","discipline":"anesthesia",
   "stem":"What are the intraoperative signs of bronchospasm in a ventilated patient?",
   "answer":"Intraoperative bronchospasm: wheezing, increasing peak airway pressures (with plateau pressure often unchanged), decreasing exhaled tidal volumes, and a slowly rising (shark-fin) capnograph waveform.",
   "rationale":"Bronchospasm increases expiratory resistance, requiring higher peak pressures to deliver the same tidal volume; plateau pressure is unchanged because parenchymal compliance is unaffected; incomplete exhalation creates the sawtooth capnograph pattern.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":868}],"confusable_with":"Tension pneumothorax (also high peak pressure + decreasing Vt, but absent breath sounds unilaterally + hemodynamic collapse)"},
  {"id":"copd-preop-03","topic":"COPD and asthma — preoperative optimization","domain":"Anesthesia / Pulmonology","discipline":"anesthesia",
   "stem":"What is the risk of positive pressure ventilation in a patient with pulmonary bullae?",
   "answer":"Positive pressure ventilation in patients with bullae risks bulla expansion, rupture, tension pneumothorax, and bronchopleural fistula (BPF).",
   "rationale":"Bullae are thin-walled non-communicating or partially communicating airspaces; positive pressure preferentially inflates these low-resistance structures, dramatically increasing the risk of rupture.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":872}],"confusable_with":""},
  {"id":"copd-preop-04","topic":"COPD and asthma — preoperative optimization","domain":"Anesthesia / Pulmonology","discipline":"anesthesia",
   "stem":"What is the average cost burden added per postoperative pulmonary complication episode?",
   "answer":"Postoperative pulmonary complications (PPCs) add an average of > $25,000 per episode in additional costs.",
   "rationale":"PPCs (pneumonia, respiratory failure, bronchospasm, atelectasis) prolong ICU and hospital stay; this cost burden underscores the value of aggressive preoperative optimization of COPD and asthma.",
   "bloom":"recall","source":[{"book":"Miller","page":784}],"confusable_with":""}
]

# ── 187 Chronic Medication Management ────────────────────────────────────────
entries += [
  {"id":"chronic-med-01","topic":"Chronic medication management — continuation and cessation","domain":"Anesthesia / Pharmacology","discipline":"anesthesia",
   "stem":"How should buprenorphine be managed perioperatively for a patient on stable maintenance therapy?",
   "answer":"Maintain stable buprenorphine dosage perioperatively; add full agonist opioids titrated to pain reduction, or use nonopioid adjuvants (clonidine, ketamine) for acute pain.",
   "rationale":"Abrupt buprenorphine cessation risks withdrawal and relapse; buprenorphine's partial agonism and ceiling effect can be overcome by sufficient doses of full opioid agonists for acute pain.",
   "bloom":"apply","source":[{"book":"Miller","page":749}],"confusable_with":"Methadone maintenance (also continued perioperatively but has different opioid interaction profile)"},
  {"id":"chronic-med-02","topic":"Chronic medication management — continuation and cessation","domain":"Anesthesia / Pharmacology","discipline":"anesthesia",
   "stem":"What is the evidence base for cannabinoids in chronic non-cancer pain management?",
   "answer":"There is insufficient robust evidence to recommend cannabinoids for chronic non-cancer pain.",
   "rationale":"Existing trials are small, short-term, and heterogeneous; systematic reviews have not established reliable efficacy or safety compared to established analgesics for this indication.",
   "bloom":"recall","source":[{"book":"Miller","page":827}],"confusable_with":""},
  {"id":"chronic-med-03","topic":"Chronic medication management — continuation and cessation","domain":"Anesthesia / Pharmacology","discipline":"anesthesia",
   "stem":"What is the most effective intervention for tobacco cessation?",
   "answer":"Combination counseling plus pharmacotherapy (varenicline, bupropion, or NRT) is the most effective intervention for tobacco cessation.",
   "rationale":"Behavioral counseling addresses psychological dependence while pharmacotherapy (especially varenicline) reduces nicotine cravings and withdrawal; combination therapy consistently outperforms either alone.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":213}],"confusable_with":"NRT alone (effective but inferior to combination therapy)"},
  {"id":"chronic-med-04","topic":"Chronic medication management — continuation and cessation","domain":"Anesthesia / Pharmacology","discipline":"anesthesia",
   "stem":"What are the first-line pharmacological treatments for alcohol use disorder?",
   "answer":"Naltrexone and acamprosate are first-line pharmacological treatments for alcohol use disorder.",
   "rationale":"Naltrexone blocks the reward effect of alcohol via mu-opioid receptor antagonism; acamprosate reduces glutamate-mediated excitability during abstinence; both reduce relapse rates.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":216}],"confusable_with":"Disulfiram (aversion therapy, second-line; requires complete abstinence to initiate)"}
]

# ── 188 Clinical Opioid Pharmacology ─────────────────────────────────────────
entries += [
  {"id":"opioid-pharm-01","topic":"Clinical Opioid Pharmacology","domain":"Pharmacology / Analgesia","discipline":"anesthesia",
   "stem":"How does naltrexone differ from naloxone as an opioid antagonist?",
   "answer":"Naltrexone is a pure opioid antagonist with significantly longer half-life than naloxone and high mu-receptor affinity; it is given orally for maintenance of opioid addiction.",
   "rationale":"Naltrexone's longer duration (24+ hours after single dose vs 30–90 min for naloxone) makes it suitable for once-daily oral dosing in addiction maintenance, whereas naloxone's short duration makes it the reversal agent for acute overdose.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":466}],"confusable_with":"Naloxone (IV/IM, short-acting, for acute reversal of respiratory depression)"},
  {"id":"opioid-pharm-02","topic":"Clinical Opioid Pharmacology","domain":"Pharmacology / Analgesia","discipline":"anesthesia",
   "stem":"What are alvimopan and methylnaltrexone, and what is their clinical use?",
   "answer":"Alvimopan and methylnaltrexone are peripherally acting opioid receptor antagonists used to treat postoperative ileus without reversing central analgesia.",
   "rationale":"Their quaternary ammonium structure (methylnaltrexone) or restricted CNS penetration (alvimopan) confines antagonism to the gut, restoring bowel motility inhibited by opioids without precipitating systemic withdrawal or pain.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":466}],"confusable_with":"Naloxone/naltrexone (also antagonists but with central effects — reverse analgesia and cause withdrawal)"},
  {"id":"opioid-pharm-03","topic":"Clinical Opioid Pharmacology","domain":"Pharmacology / Analgesia","discipline":"anesthesia",
   "stem":"Why do older adult patients generally require reduced opioid doses compared to younger adults?",
   "answer":"Older adults have reduced dose requirements for opioids (as well as propofol, etomidate, benzodiazepines, and barbiturates) due to pharmacokinetic and pharmacodynamic changes of aging.",
   "rationale":"Aging reduces hepatic mass and blood flow (reduced first-pass and clearance), decreases plasma protein binding, increases CNS sensitivity, and reduces volume of distribution, collectively raising drug effect for the same dose.",
   "bloom":"apply","source":[{"book":"Miller","page":161}],"confusable_with":""},
  {"id":"opioid-pharm-04","topic":"Clinical Opioid Pharmacology","domain":"Pharmacology / Analgesia","discipline":"anesthesia",
   "stem":"What is remifentanil-induced acute tolerance and what is its clinical consequence?",
   "answer":"Remifentanil infusion induces acute opioid tolerance via NMDA-receptor upregulation; consequence: larger-than-usual postoperative opioid doses are needed for analgesia.",
   "rationale":"Continuous mu-receptor stimulation activates NMDA-mediated counter-regulatory pathways and receptor down-regulation; this sensitizes patients to pain (opioid-induced hyperalgesia) and blunts postoperative opioid effect.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1490}],"confusable_with":"Opioid tolerance from chronic use (same mechanism but develops over weeks, not during a single infusion)"},
  {"id":"opioid-pharm-05","topic":"Clinical Opioid Pharmacology","domain":"Pharmacology / Analgesia","discipline":"anesthesia",
   "stem":"What was the original drug and indication for high-dose opioid anesthesia?",
   "answer":"High-dose opioid anesthesia was originally described using morphine for open heart surgery, later replaced by fentanyl congeners.",
   "rationale":"Cardiac surgery patients were too hemodynamically fragile for inhalational agents; high-dose morphine (then fentanyl/sufentanil) provided stable hemodynamics with minimal myocardial depression.",
   "bloom":"recall","source":[{"book":"Miller","page":161}],"confusable_with":""}
]

# ── 189 Perioperative DM Glucose Management ───────────────────────────────────
entries += [
  {"id":"dm-periop-01","topic":"Diabetes mellitus — perioperative glucose management","domain":"Anesthesia / Endocrinology","discipline":"anesthesia",
   "stem":"How should NPH insulin be managed on the morning of surgery?",
   "answer":"Give half the usual morning NPH dose with a 5% dextrose infusion at 1.5 mL/kg/h on the morning of surgery.",
   "rationale":"Full NPH dosing without oral intake risks intraoperative hypoglycemia; halving the dose with a dextrose infusion maintains basal insulin coverage while providing glucose substrate.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1222}],"confusable_with":"Long-acting insulin (glargine/detemir) — generally give full dose the night before, not halved on morning of surgery"},
  {"id":"dm-periop-02","topic":"Diabetes mellitus — perioperative glucose management","domain":"Anesthesia / Endocrinology","discipline":"anesthesia",
   "stem":"What perioperative complications are associated with hyperglycemia?",
   "answer":"Perioperative hyperglycemia increases risk for cardiovascular events and infectious complications (wound infection, pneumonia, sepsis).",
   "rationale":"Hyperglycemia impairs neutrophil function, complement activity, and wound healing, while glycosylated endothelium is prone to thrombosis — collectively increasing infectious and cardiac morbidity.",
   "bloom":"apply","source":[{"book":"Miller","page":231}],"confusable_with":"Hypoglycemia (also harmful perioperatively but through neurological, not infectious/CV mechanisms)"},
  {"id":"dm-periop-03","topic":"Diabetes mellitus — perioperative glucose management","domain":"Anesthesia / Endocrinology","discipline":"anesthesia",
   "stem":"What HbA1c thresholds define diabetes mellitus and impaired fasting glucose?",
   "answer":"HbA1c ≥ 6.5% = diabetes mellitus; HbA1c 5.7–6.4% = impaired fasting glucose (pre-diabetes).",
   "rationale":"HbA1c reflects average blood glucose over ~3 months; the 6.5% threshold has high specificity for the microvascular complications that define DM, while 5.7–6.4% identifies individuals at elevated risk.",
   "bloom":"recall","source":[{"book":"Miller","page":783}],"confusable_with":"Fasting plasma glucose thresholds (≥126 mg/dL = DM; 100–125 = impaired fasting glucose — same categories, different test)"}
]

# ── 190 Handoffs & Care Transitions (thin chunks) ────────────────────────────
entries += [
  {"id":"handoffs-01","topic":"Handoffs & Care Transitions","domain":"Patient safety / Quality improvement","discipline":"medicine",
   "stem":"Why are structured handoffs important for patient safety during care transitions?",
   "answer":"Effective structured handoffs maintain continuity of care and prevent mismanagement; shared electronic documentation and real-time updates facilitate seamless transitions.",
   "rationale":"Information lost or distorted at handoff is a leading contributor to adverse events; structured tools (SBAR, I-PASS) and electronic records reduce errors of omission and commission.",
   "bloom":"apply","source":[{"book":"StatPearls Hemorrhagic Shock","page":14}],"confusable_with":""},
  {"id":"handoffs-02","topic":"Handoffs & Care Transitions","domain":"Patient safety / Quality improvement","discipline":"medicine",
   "stem":"What elements should a structured handoff communication include?",
   "answer":"A complete handoff includes: current clinical status, active problems, pending tasks, anticipated events/contingency plans, and verification of understanding by the receiving provider.",
   "rationale":"Each element closes a specific safety gap: status provides situational awareness; pending tasks prevent items from falling through; contingency planning prepares the receiving team for likely deteriorations.",
   "bloom":"apply","source":[{"book":"StatPearls Pituitary Apoplexy","page":8}],"confusable_with":""},
  {"id":"handoffs-03","topic":"Handoffs & Care Transitions","domain":"Patient safety / Quality improvement","discipline":"medicine",
   "stem":"What is the primary risk when verbal handoffs are not supported by shared electronic documentation?",
   "answer":"Without written documentation, critical information (pending labs, medication changes, clinical trajectory) can be omitted or distorted, leading to mismanagement.",
   "rationale":"Human working memory is limited and subject to proactive/retroactive interference; documentation externalizes memory, providing a retrievable, verifiable record that persists beyond the verbal exchange.",
   "bloom":"analyze","source":[{"book":"StatPearls Hemorrhagic Shock","page":14}],"confusable_with":""}
]

# ── 191 Hypertension Preoperative (thin chunks) ──────────────────────────────
entries += [
  {"id":"htn-preop-01","topic":"Hypertension — preoperative evaluation and management","domain":"Anesthesia / Cardiology","discipline":"anesthesia",
   "stem":"What is the classic triad of pheochromocytoma that prompts preoperative workup?",
   "answer":"Pheochromocytoma classic triad: symptomatic sympathetic hyperactivity (episodic hypertension, headache, diaphoresis, palpitations) caused by excess catecholamines and metanephrines.",
   "rationale":"Pheochromocytoma secretes epinephrine and norepinephrine episodically, producing the classic hypertensive crises; biochemical confirmation (urinary/plasma metanephrines) is required before adrenalectomy.",
   "bloom":"recall","source":[{"book":"Miller","page":551}],"confusable_with":"Essential hypertension (persistent, not episodic; no catecholamine excess)"},
  {"id":"htn-preop-02","topic":"Hypertension — preoperative evaluation and management","domain":"Anesthesia / Cardiology","discipline":"anesthesia",
   "stem":"What components are included in the preoperative history of present illness for anesthetic risk assessment?",
   "answer":"Preoperative HPI includes: patient age, sex, surgical diagnosis, proposed procedure, and relevant comorbidities.",
   "rationale":"These elements define baseline physiological reserve and procedural risk, allowing individualized risk stratification and modification of anesthetic plan before surgery.",
   "bloom":"recall","source":[{"book":"Miller","page":222}],"confusable_with":""},
  {"id":"htn-preop-03","topic":"Hypertension — preoperative evaluation and management","domain":"Anesthesia / Cardiology","discipline":"anesthesia",
   "stem":"A patient with known pheochromocytoma is scheduled for elective adrenalectomy. What is the critical preoperative preparation?",
   "answer":"Preoperative alpha-adrenergic blockade (phenoxybenzamine or doxazosin) for at least 10–14 days is required before pheochromocytoma resection to prevent intraoperative hypertensive crisis.",
   "rationale":"Surgical manipulation of the tumor releases massive catecholamines; pre-blocking alpha receptors prevents hypertensive emergency, cardiac arrhythmias, and stroke during resection.",
   "bloom":"apply","source":[{"book":"Miller","page":551}],"confusable_with":"Beta-blockade alone (contraindicated first without alpha block — causes unopposed alpha vasoconstriction and severe hypertension)"}
]

# ── 192 Infection Control (thin chunks) ──────────────────────────────────────
entries += [
  {"id":"infect-ctrl-01","topic":"Infection Control & Prevention","domain":"Patient safety / Infectious disease","discipline":"medicine",
   "stem":"What are the top three causes of pregnancy-related death according to CDC 2017 data?",
   "answer":"Cardiovascular disease (14%), infection/sepsis (13%), and cardiomyopathy (12%) are the top three causes of pregnancy-related mortality.",
   "rationale":"This epidemiological data shifts the focus of obstetric care: infection/sepsis is not the top cause but is the second most common, underscoring the importance of sepsis prevention and early recognition in obstetric patients.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1383}],"confusable_with":"Hemorrhage (11%, 4th — historically considered the leading cause but now surpassed)"},
  {"id":"infect-ctrl-02","topic":"Infection Control & Prevention","domain":"Patient safety / Infectious disease","discipline":"medicine",
   "stem":"What is the clinical presentation of varicella zoster reactivation?",
   "answer":"VZV reactivation (herpes zoster) presents as an erythematous vesicular rash in a dermatomal distribution; T3–L3 dermatomes are most commonly affected.",
   "rationale":"Latent VZV in dorsal root ganglia reactivates under immune compromise, producing painful vesicles confined to the sensory dermatome of the affected ganglion.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1748}],"confusable_with":"HSV (not dermatomal), contact dermatitis (bilateral/non-dermatomal)"},
  {"id":"infect-ctrl-03","topic":"Infection Control & Prevention","domain":"Patient safety / Infectious disease","discipline":"medicine",
   "stem":"What is the framework for standard precautions in hospital infection control?",
   "answer":"CDC standard precautions apply to all patient care regardless of known infection status: hand hygiene, PPE (gloves, gown, mask, eye protection) based on anticipated exposure, and safe sharps handling.",
   "rationale":"Standard precautions assume any patient may harbor transmissible pathogens, eliminating the need to know infection status before protecting healthcare workers and preventing cross-contamination.",
   "bloom":"recall","source":[{"book":"Marino ICU","page":34}],"confusable_with":"Transmission-based precautions (contact, droplet, airborne — additional layer for known pathogens; do not replace standard precautions)"},
  {"id":"infect-ctrl-04","topic":"Infection Control & Prevention","domain":"Patient safety / Infectious disease","discipline":"medicine",
   "stem":"What percentage of pregnancy-related deaths are attributable to infection/sepsis per CDC 2017?",
   "answer":"Infection/sepsis accounts for 13% of pregnancy-related deaths.",
   "rationale":"Recognition of sepsis as a leading obstetric killer — second only to cardiovascular disease — justifies aggressive sepsis screening protocols and early antibiotic administration in febrile obstetric patients.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1383}],"confusable_with":""}
]

# ── 193 Informed Consent ──────────────────────────────────────────────────────
entries += [
  {"id":"informed-consent-01","topic":"Informed Consent","domain":"Medical ethics / Law","discipline":"medicine",
   "stem":"What does the legal doctrine res ipsa loquitur mean in the context of anesthesia liability?",
   "answer":"Res ipsa loquitur ('the thing speaks for itself') means the injury is so clearly the result of negligence that the event itself establishes a prima facie case without requiring expert testimony on the mechanism.",
   "rationale":"In anesthesia, this applies to injuries that could not occur without negligence (e.g., wrong-site nerve block, dental injury during elective intubation in a patient with normal anatomy), where the outcome alone implies a breach of duty.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":477}],"confusable_with":"Negligence per se (violation of a specific statute establishes negligence without res ipsa)"},
  {"id":"informed-consent-02","topic":"Informed Consent","domain":"Medical ethics / Law","discipline":"medicine",
   "stem":"Compared with sedative premedication, how does a preoperative anesthesiologist visit affect patient anxiety?",
   "answer":"A preoperative visit by the anesthesiologist produces a greater reduction in patient anxiety than sedative premedication drugs.",
   "rationale":"Informed explanation of the anesthetic plan addresses cognitive anxiety (fear of the unknown), which pharmacological sedation cannot resolve; this finding supports mandatory preoperative anesthesia consultation.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":489}],"confusable_with":""},
  {"id":"informed-consent-03","topic":"Informed Consent","domain":"Medical ethics / Law","discipline":"medicine",
   "stem":"What is one of the core purposes of the preoperative anesthetic evaluation beyond clinical assessment?",
   "answer":"The preoperative evaluation provides the patient with an estimate of anesthetic risk and is an opportunity to obtain informed consent.",
   "rationale":"Patients have a right to understand risks before consenting to anesthesia; the preoperative visit is the primary setting where anesthetic risks (awareness, PONV, dental injury, cardiovascular events) are disclosed.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":489}],"confusable_with":""},
  {"id":"informed-consent-04","topic":"Informed Consent","domain":"Medical ethics / Law","discipline":"medicine",
   "stem":"What category of NQF serious reportable event is relevant to anesthesia quality and safety?",
   "answer":"'Intraoperative death in an ASA class I patient' is an NQF serious reportable event (never event) in anesthesia.",
   "rationale":"ASA I patients should have essentially no anesthesia-attributable mortality; an intraoperative death in this class implies a preventable error, making it a never event that must be reported and investigated.",
   "bloom":"recall","source":[{"book":"Miller","page":861}],"confusable_with":""}
]

# ── 194 Informed Consent & Capacity Assessment ───────────────────────────────
entries += [
  {"id":"consent-capacity-01","topic":"Informed consent and capacity assessment","domain":"Medical ethics / Law","discipline":"medicine",
   "stem":"What are the three elements required for valid informed consent?",
   "answer":"Valid informed consent requires: (1) disclosure of relevant clinical information (diagnosis, intervention, purpose, risks/benefits, alternatives including no treatment); (2) a voluntary decision; (3) decision-making capacity.",
   "rationale":"All three elements must be present; absence of any one invalidates consent — coerced decisions (not voluntary), incapacitated patients (no capacity), or uninformed consent (no disclosure) are each legally and ethically deficient.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":205}],"confusable_with":"Assent (from patients who lack capacity — desirable but not legally binding consent)"},
  {"id":"consent-capacity-02","topic":"Informed consent and capacity assessment","domain":"Medical ethics / Law","discipline":"medicine",
   "stem":"What must clinicians clarify before surgery in a patient with a pre-existing DNR order?",
   "answer":"Perioperative DNR status must be explicitly clarified: discuss with the patient (or surrogate) whether DNR applies in the OR, or whether specific limits on resuscitation are requested.",
   "rationale":"Standard DNR orders may be automatically suspended perioperatively in some institutions; this practice requires explicit patient/surrogate endorsement, not unilateral clinician override.",
   "bloom":"apply","source":[{"book":"Miller","page":874}],"confusable_with":""},
  {"id":"consent-capacity-03","topic":"Informed consent and capacity assessment","domain":"Medical ethics / Law","discipline":"medicine",
   "stem":"Which key academic references define the legal and clinical framework for informed consent and capacity assessment?",
   "answer":"Foundational references include Psychosomatics 1997;38:119 (capacity assessment) and NEJM 2007;357:1834 (informed consent framework).",
   "rationale":"These landmark papers define the components of capacity (understanding, appreciation, reasoning, communication of a choice) and the standards for disclosure that underpin modern consent doctrine.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":205}],"confusable_with":""},
  {"id":"consent-capacity-04","topic":"Informed consent and capacity assessment","domain":"Medical ethics / Law","discipline":"medicine",
   "stem":"A patient refuses a blood transfusion for religious reasons and has decision-making capacity. What is the clinician's obligation?",
   "answer":"A capacitated adult's informed refusal must be respected even if the clinician disagrees; the clinician should document the discussion and the patient's understanding of consequences.",
   "rationale":"Autonomy is a foundational bioethical principle; the right to refuse treatment, even life-saving treatment, is legally protected for adults with intact decision-making capacity.",
   "bloom":"analyze","source":[{"book":"MGH Housestaff Manual","page":205}],"confusable_with":"Advance directive (documents future wishes for when capacity is lost — distinct from contemporaneous refusal)"}
]

# ── 195 Medication Safety ─────────────────────────────────────────────────────
entries += [
  {"id":"med-safety-01","topic":"Medication Safety","domain":"Patient safety / Quality improvement","discipline":"medicine",
   "stem":"What are three types of errors the WHO Surgical Safety Checklist is specifically designed to prevent?",
   "answer":"The WHO Surgical Safety Checklist prevents wrong-site surgery, wrong-patient procedures, retained foreign objects, and medication errors.",
   "rationale":"Each checklist pause (Sign In, Time Out, Sign Out) targets a specific error category: identity/site verification prevents wrong-patient/site, count protocols prevent retained objects, and medication verification prevents drug errors.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":33}],"confusable_with":""},
  {"id":"med-safety-02","topic":"Medication Safety","domain":"Patient safety / Quality improvement","discipline":"medicine",
   "stem":"What makes the WHO Surgical Safety Checklist most effective?",
   "answer":"The checklist is most effective when used interactively (verbal confirmation by each team member) rather than passively read by one person.",
   "rationale":"Interactive checklists engage team situational awareness and create shared mental models; passive recitation by one provider does not activate the error-catching function of team verification.",
   "bloom":"apply","source":[{"book":"Miller","page":861}],"confusable_with":""},
  {"id":"med-safety-03","topic":"Medication Safety","domain":"Patient safety / Quality improvement","discipline":"medicine",
   "stem":"What is an NQF 'serious reportable event' (never event) in the surgical setting?",
   "answer":"NQF serious reportable events include intraoperative death in an ASA class I patient — an outcome that should never occur with proper care.",
   "rationale":"Never events are defined by the NQF as serious, largely preventable, and unambiguous; they serve as sentinel indicators of systemic safety failures requiring root cause analysis.",
   "bloom":"recall","source":[{"book":"Miller","page":861}],"confusable_with":"Adverse events (harm that occurs despite appropriate care — not necessarily preventable)"}
]

# ── 196 Multimodal Analgesia ──────────────────────────────────────────────────
entries += [
  {"id":"multimodal-01","topic":"Multimodal Analgesia Principles","domain":"Anesthesia / Pain medicine","discipline":"anesthesia",
   "stem":"What is the multimodal analgesia approach and what drug classes does it include?",
   "answer":"Multimodal analgesia combines interventional techniques (epidural, peripheral nerve catheters/blocks) with systemic agents: NSAIDs, acetaminophen, gabapentin/pregabalin, ketamine, IV lidocaine, and opioids.",
   "rationale":"Different analgesic mechanisms act at different points in the pain pathway; combining agents allows lower doses of each, reducing dose-dependent side effects while achieving superior analgesia compared to opioids alone.",
   "bloom":"recall","source":[{"book":"Miller","page":744}],"confusable_with":"Opioid-only analgesia (single mechanism, higher dose requirements, more side effects)"},
  {"id":"multimodal-02","topic":"Multimodal Analgesia Principles","domain":"Anesthesia / Pain medicine","discipline":"anesthesia",
   "stem":"What routes are available for patient-controlled analgesia (PCA)?",
   "answer":"PCA can be delivered via oral, IV, subcutaneous, epidural, intrathecal, and peripheral nerve catheter routes.",
   "rationale":"The principle of PCA (patient self-titration within a clinician-set parameters) is not limited to IV opioids; the same titration concept applies to epidural and perineural delivery of local anesthetics and opioids.",
   "bloom":"recall","source":[{"book":"Miller","page":747}],"confusable_with":""},
  {"id":"multimodal-03","topic":"Multimodal Analgesia Principles","domain":"Anesthesia / Pain medicine","discipline":"anesthesia",
   "stem":"How long does intraarticular opioid injection provide postoperative analgesia, and via what mechanism?",
   "answer":"Intraarticular opioid injection provides analgesia for up to 24 hours postoperatively via activation of peripheral opioid receptors on primary afferent nerve terminals.",
   "rationale":"Inflamed peripheral tissues upregulate opioid receptor expression on sensory nerve endings; local opioid binding inhibits afferent nociceptive signaling without significant systemic absorption.",
   "bloom":"apply","source":[{"book":"Miller","page":752}],"confusable_with":"Systemic IV opioids (central mechanism, more side effects)"},
  {"id":"multimodal-04","topic":"Multimodal Analgesia Principles","domain":"Anesthesia / Pain medicine","discipline":"anesthesia",
   "stem":"What preoperative supplement reduces postoperative morphine consumption and at what dose?",
   "answer":"Vitamin C 2 g preoperatively reduces postoperative morphine consumption.",
   "rationale":"Vitamin C (ascorbic acid) has antioxidant and neuromodulatory properties; preoperative dosing reduces oxidative stress from surgical trauma and may attenuate central sensitization, decreasing opioid requirements.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1538}],"confusable_with":""}
]

# ── 197 NPO Guidelines ────────────────────────────────────────────────────────
entries += [
  {"id":"npo-01","topic":"NPO guidelines and aspiration risk","domain":"Anesthesia / Perioperative medicine","discipline":"anesthesia",
   "stem":"What are the physiological consequences of prolonged preoperative fasting?",
   "answer":"Prolonged NPO fasting causes insulin resistance; overnight fast plus mechanical bowel prep causes dehydration, resulting in discomfort, drowsiness, and orthostatic hypotension.",
   "rationale":"Prolonged carbohydrate restriction induces insulin resistance via downregulation of insulin signaling; combined with fluid restriction from bowel prep, patients arrive hypovolemic and metabolically stressed.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1819}],"confusable_with":""},
  {"id":"npo-02","topic":"NPO guidelines and aspiration risk","domain":"Anesthesia / Perioperative medicine","discipline":"anesthesia",
   "stem":"For a high-risk aspiration patient (full stomach, GERD, morbid obesity), what four interventions reduce aspiration risk?",
   "answer":"Metoclopramide (promotility), H2 blocker or antacid (reduce gastric acidity/volume), awake regional anesthesia or awake intubation in upright position (or RSI with ETT), leaving NGT to suction, and cricoid pressure until ETT confirmed.",
   "rationale":"Full-stomach patients require both pharmacological aspiration prophylaxis and an airway strategy that bypasses the period of unprotected airway; RSI with cricoid pressure or awake intubation are the accepted standards.",
   "bloom":"apply","source":[{"book":"Stanford CA-1","page":74}],"confusable_with":"Standard induction (appropriate only for fasted, low-risk patients)"},
  {"id":"npo-03","topic":"NPO guidelines and aspiration risk","domain":"Anesthesia / Perioperative medicine","discipline":"anesthesia",
   "stem":"Despite clear evidence for liberalized fasting guidelines, what is the clinical reality?",
   "answer":"Compliance with evidence-based fasting guidelines remains low in clinical practice; many institutions still default to excessive 'NPO after midnight' restrictions.",
   "rationale":"Institutional inertia, medico-legal concern, and scheduling unpredictability perpetuate overly conservative fasting, imposing unnecessary metabolic and hemodynamic stress on patients.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1819}],"confusable_with":""}
]

# ── 198 NSAIDs/COX Inhibitors ─────────────────────────────────────────────────
entries += [
  {"id":"nsaid-01","topic":"NSAIDs and COX-Inhibitors","domain":"Pharmacology / Analgesia","discipline":"anesthesia",
   "stem":"What are the three analgesic benefits of NSAIDs in the postoperative setting?",
   "answer":"NSAIDs reduce postoperative pain intensity, decrease opioid consumption, and decrease opioid-related side effects.",
   "rationale":"By inhibiting peripheral and central COX-mediated prostaglandin synthesis, NSAIDs address inflammatory pain independently of opioids, allowing dose reduction and fewer opioid adverse effects.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1831}],"confusable_with":""},
  {"id":"nsaid-02","topic":"NSAIDs and COX-Inhibitors","domain":"Pharmacology / Analgesia","discipline":"anesthesia",
   "stem":"What advantage do COX-2 selective inhibitors have over non-selective NSAIDs, and what shared risk remains?",
   "answer":"COX-2 inhibitors reduce NSAID-related platelet dysfunction and GI bleeding (vs non-selective NSAIDs); however, the risk of renal dysfunction (especially with hypovolemia, heart failure, cirrhosis, diabetic nephropathy, hypercalcemia) is shared.",
   "rationale":"COX-2 is the dominant isoform in platelets and GI mucosa (COX-1 actually protects GI mucosa); COX-2 selectivity spares these; however, renal prostaglandin synthesis uses both COX isoforms to maintain GFR under stress.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1831}],"confusable_with":"Non-selective NSAIDs (inhibit COX-1 + COX-2 → platelet inhibition + GI ulceration, in addition to renal risk)"},
  {"id":"nsaid-03","topic":"NSAIDs and COX-Inhibitors","domain":"Pharmacology / Analgesia","discipline":"anesthesia",
   "stem":"In which patient populations is NSAID/COX-2 inhibitor use most likely to cause renal complications?",
   "answer":"Patients with hypovolemia, heart failure, cirrhosis, diabetic nephropathy, or hypercalcemia are at highest risk for NSAID-induced renal dysfunction.",
   "rationale":"These conditions render the kidney prostaglandin-dependent for afferent arteriolar dilation to maintain GFR; COX inhibition removes this compensatory mechanism, precipitating acute kidney injury.",
   "bloom":"analyze","source":[{"book":"MGH Housestaff Manual","page":99}],"confusable_with":""}
]

# ── 199 Obesity Perioperative ─────────────────────────────────────────────────
entries += [
  {"id":"obesity-periop-01","topic":"Obesity — perioperative considerations","domain":"Anesthesia / Perioperative medicine","discipline":"anesthesia",
   "stem":"What type of ventilatory defect does marked obesity produce?",
   "answer":"Marked obesity produces a restrictive ventilatory defect due to reduced chest wall compliance and reduced functional residual capacity.",
   "rationale":"Excess chest wall and abdominal adipose tissue limit diaphragmatic excursion and reduce thoracic compliance; FRC falls (especially supine), predisposing to atelectasis and rapid oxygen desaturation.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":877}],"confusable_with":"Obstructive defect (COPD/asthma — reduced FEV1/FVC rather than reduced TLC/FVC)"},
  {"id":"obesity-periop-02","topic":"Obesity — perioperative considerations","domain":"Anesthesia / Perioperative medicine","discipline":"anesthesia",
   "stem":"What are the major postoperative complications in OSA patients following surgery?",
   "answer":"OSA patients are vulnerable postoperatively to hypertension, hypoxia, arrhythmias, myocardial infarction, pulmonary edema, stroke, and death.",
   "rationale":"The loss of upper airway tone with anesthesia and opioid analgesics exacerbates OSA; cyclic hypoxia and hypercapnia trigger sympathetic surges that drive the cardiovascular complications.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1240}],"confusable_with":""},
  {"id":"obesity-periop-03","topic":"Obesity — perioperative considerations","domain":"Anesthesia / Perioperative medicine","discipline":"anesthesia",
   "stem":"What two airway challenges are anticipated in the morbidly obese patient?",
   "answer":"Both difficult mask ventilation and difficult intubation are anticipated in morbidly obese patients.",
   "rationale":"Excess pharyngeal soft tissue and limited neck extension reduce mask seal and view at laryngoscopy; reduced FRC means desaturation occurs rapidly during apnea, compressing the safe apnea time for intubation attempts.",
   "bloom":"apply","source":[{"book":"Miller","page":540}],"confusable_with":""},
  {"id":"obesity-periop-04","topic":"Obesity — perioperative considerations","domain":"Anesthesia / Perioperative medicine","discipline":"anesthesia",
   "stem":"How should sedative premedication be administered in the obese patient?",
   "answer":"Obese patients are more sensitive to respiratory depressant effects of sedatives; give in incremental doses with careful titration, particularly in patients with OSA.",
   "rationale":"Increased airway collapsibility and reduced respiratory reserve in obesity amplify the airway-obstructing and apnea-inducing effects of sedatives; standard bolus dosing risks respiratory compromise before any monitoring is applied.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":877}],"confusable_with":""}
]

# ── 200 Opioid Dose Conversion ────────────────────────────────────────────────
entries += [
  {"id":"opioid-conv-01","topic":"Opioid Dose Conversion and Equianalgesic Dosing","domain":"Pharmacology / Pain medicine","discipline":"anesthesia",
   "stem":"Why cannot methadone be converted to or from other opioids using standard equianalgesic tables?",
   "answer":"Methadone cannot be converted linearly; it has complex pharmacokinetics and NMDA antagonist activity. It is dosed TID for neuropathic pain management.",
   "rationale":"Methadone's variable half-life (8–59 h), active metabolites, and NMDA receptor antagonism make its equianalgesic ratio with other opioids highly variable and patient-dependent; standard conversion tables underestimate its potency.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":165}],"confusable_with":"Morphine (predictable equianalgesic conversion via standard tables)"},
  {"id":"opioid-conv-02","topic":"Opioid Dose Conversion and Equianalgesic Dosing","domain":"Pharmacology / Pain medicine","discipline":"anesthesia",
   "stem":"What are the IV fentanyl dosing parameters for acute pain: starting dose, interval, onset, and duration?",
   "answer":"IV fentanyl: 25–50 mcg q 15–30 min; onset < 1 min; duration 45 min to 2+ hours.",
   "rationale":"Fentanyl's high lipophilicity enables rapid CNS penetration (onset < 1 min); redistribution rather than elimination terminates its effect initially, giving a 45-minute clinical duration despite a longer elimination half-life.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":63}],"confusable_with":"Morphine IV (onset 5–10 min; duration 3–4 h — slower and longer)"},
  {"id":"opioid-conv-03","topic":"Opioid Dose Conversion and Equianalgesic Dosing","domain":"Pharmacology / Pain medicine","discipline":"anesthesia",
   "stem":"What is the oral morphine time to onset, peak effect, and duration?",
   "answer":"Oral morphine: onset 30–60 min; peak effect 90–120 min; duration 4–12 hours.",
   "rationale":"Oral morphine undergoes significant first-pass hepatic metabolism; GI absorption rate determines the delayed onset compared to IV; the active metabolite morphine-6-glucuronide contributes to the prolonged duration.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":737}],"confusable_with":"IV morphine (onset 5–10 min; peak 20 min — same drug, different route)"},
  {"id":"opioid-conv-04","topic":"Opioid Dose Conversion and Equianalgesic Dosing","domain":"Pharmacology / Pain medicine","discipline":"anesthesia",
   "stem":"What is the remifentanil bolus and infusion dosing range?",
   "answer":"Remifentanil: bolus 0–1 mcg/kg; infusion 0.25–1 mcg/kg/min.",
   "rationale":"Remifentanil's ester structure allows rapid hydrolysis by nonspecific plasma and tissue esterases; this ultra-short action (context-sensitive half-time ~3–4 min regardless of infusion duration) mandates continuous infusion for sustained effect.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":63}],"confusable_with":"Sufentanil (longer duration, not context-insensitive)"},
  {"id":"opioid-conv-05","topic":"Opioid Dose Conversion and Equianalgesic Dosing","domain":"Pharmacology / Pain medicine","discipline":"anesthesia",
   "stem":"What important pharmacological property do ALL opioid analgesics share regarding sedation and analgesia?",
   "answer":"All opioids are respiratory depressants with effects synergistic with other CNS sedatives; none provide amnestic effects.",
   "rationale":"Opioids act on mu-receptors in the brainstem respiratory centers; co-administration with benzodiazepines or other sedatives produces synergistic respiratory depression; the absence of amnesia is an important distinction from anesthetic agents.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":737}],"confusable_with":"Benzodiazepines (anxiolytic + amnestic but only mild analgesic effect)"}
]

# ── 201 Opioid Safety / Naloxone ──────────────────────────────────────────────
entries += [
  {"id":"opioid-safety-01","topic":"Opioid Safety, Monitoring, and Naloxone","domain":"Pharmacology / Patient safety","discipline":"anesthesia",
   "stem":"What is the recommended titration strategy for naloxone to reverse opioid-induced respiratory depression, and why?",
   "answer":"Titrate naloxone in small increments (80 mcg IV per dose in adults) to avoid sudden pain, hemodynamic complications (hypertension, tachycardia, pulmonary edema), and to preserve as much analgesia as possible.",
   "rationale":"Bolus naloxone reverses all opioid analgesia simultaneously, causing acute pain, catecholamine surge with cardiovascular complications, and pulmonary edema from sudden sympathetic activation; incremental dosing allows selective reversal of respiratory depression.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":2113}],"confusable_with":"Full-dose naloxone bolus (appropriate in complete apnea/cardiac arrest from opioid — speed overrides titration)"},
  {"id":"opioid-safety-02","topic":"Opioid Safety, Monitoring, and Naloxone","domain":"Pharmacology / Patient safety","discipline":"anesthesia",
   "stem":"What is the fetal effect of maternal opioid administration and which specific FHR change indicates it?",
   "answer":"All opioids readily cross the placenta; fetal effects include decreased fetal heart rate variability and neonatal respiratory depression.",
   "rationale":"Lipophilic opioids cross the placental barrier proportional to their lipid solubility; fetal mu-receptor activation reduces variability in the fetal ANS-mediated FHR and depresses fetal/neonatal respiratory drive.",
   "bloom":"apply","source":[{"book":"Miller","page":609}],"confusable_with":"Late decelerations (FHR pattern from uteroplacental insufficiency, distinct from opioid effect on variability)"},
  {"id":"opioid-safety-03","topic":"Opioid Safety, Monitoring, and Naloxone","domain":"Pharmacology / Patient safety","discipline":"anesthesia",
   "stem":"A patient in the PACU has respiratory rate of 5 breaths/min after fentanyl. Why should naloxone be titrated rather than given as a full bolus?",
   "answer":"Titration minimizes sudden analgesia reversal and hemodynamic complications (hypertension, tachycardia, acute pulmonary edema) while reversing respiratory depression; a full bolus causes abrupt pain and catecholamine surge.",
   "rationale":"Sudden complete opioid reversal activates the sympathetic nervous system; catecholamine-induced pulmonary vasoconstriction can precipitate flash pulmonary edema, a potentially fatal complication of bolus naloxone.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":2113}],"confusable_with":""}
]

# ── 202 Opioid Side Effects ───────────────────────────────────────────────────
entries += [
  {"id":"opioid-se-01","topic":"Opioid Side Effects and Management","domain":"Pharmacology / Pain medicine","discipline":"anesthesia",
   "stem":"What is the distinction between physical dependence and psychological dependence (addiction) in clinical opioid therapy?",
   "answer":"Physical dependence (withdrawal on abrupt discontinuation) is an expected pharmacological effect; psychological dependence (drug craving) is rare in patients receiving opioids for clinical pain management.",
   "rationale":"The neurobiological pathways for physical tolerance/dependence differ from addiction circuitry; patients in genuine pain rarely develop compulsive drug-seeking behavior when opioids are appropriately prescribed.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1763}],"confusable_with":"Opioid use disorder (meets DSM criteria for addiction — distinct from physical dependence on prescribed opioids)"},
  {"id":"opioid-se-02","topic":"Opioid Side Effects and Management","domain":"Pharmacology / Pain medicine","discipline":"anesthesia",
   "stem":"What is the primary cause of postoperative shivering, and what is its physiological significance?",
   "answer":"Primary cause of postoperative shivering is perioperative hypothermia; shivering greatly increases O2 consumption, catecholamine release, cardiac output, heart rate, and blood pressure.",
   "rationale":"Muscle thermogenesis through shivering is 4–5× more metabolically costly than basal state; in patients with marginal cardiac or pulmonary reserve, the resulting increase in oxygen demand and cardiac work can precipitate ischemia or failure.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":310}],"confusable_with":"Nonthermoregulatory shivering (may involve spinal cord mechanisms and is not abolished by warming alone)"},
  {"id":"opioid-se-03","topic":"Opioid Side Effects and Management","domain":"Pharmacology / Pain medicine","discipline":"anesthesia",
   "stem":"What clinical problem arises from large-dose remifentanil infusions used intraoperatively?",
   "answer":"Large-dose remifentanil infusion induces acute opioid tolerance, requiring much larger-than-usual postoperative opioid doses for adequate analgesia.",
   "rationale":"Continuous high-level mu-receptor stimulation upregulates NMDA receptors and downregulates mu-receptors, creating a sensitized pain state (hyperalgesia) and blunting subsequent opioid effect.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1830}],"confusable_with":""},
  {"id":"opioid-se-04","topic":"Opioid Side Effects and Management","domain":"Pharmacology / Pain medicine","discipline":"anesthesia",
   "stem":"How do alvimopan and methylnaltrexone treat opioid-induced constipation/ileus without reversing analgesia?",
   "answer":"Alvimopan and methylnaltrexone are peripherally restricted opioid receptor antagonists that block gut mu-receptors to restore bowel motility without crossing the blood-brain barrier to reverse central analgesia.",
   "rationale":"Opioid-induced constipation/ileus is mediated entirely by peripheral mu-receptors in the enteric nervous system; antagonism at these sites restores motility without affecting the CNS analgesic effect.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":466}],"confusable_with":"Naloxone (also reverses ileus at high doses but reverses central analgesia and may precipitate withdrawal)"}
]

# ── 203 Pain Assessment (thin chunks) ────────────────────────────────────────
entries += [
  {"id":"pain-assess-01","topic":"Pain Assessment Tools and Documentation","domain":"Anesthesia / Pain medicine","discipline":"anesthesia",
   "stem":"What tool is used to diagnose postoperative delirium in the ICU and PACU?",
   "answer":"The Confusion Assessment Method (CAM, or CAM-ICU) is the validated tool for diagnosing postoperative delirium.",
   "rationale":"CAM assesses acute onset, inattention, disorganized thinking, and altered consciousness — the four features required to diagnose delirium; the ICU version substitutes nonverbal attention tests for aphasic or intubated patients.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":484}],"confusable_with":"NRS pain scale (assesses pain intensity, not delirium)"},
  {"id":"pain-assess-02","topic":"Pain Assessment Tools and Documentation","domain":"Anesthesia / Pain medicine","discipline":"anesthesia",
   "stem":"Which classic study supports the preoperative anesthesiologist visit over sedative premedication for anxiety reduction?",
   "answer":"Classic studies show a preoperative visit by the anesthesiologist produces greater anxiety reduction than sedative premedication drugs.",
   "rationale":"Patient anxiety is cognitively mediated by fear of the unknown; informed explanation addresses the root cause, whereas sedatives blunt awareness without resolving the underlying anxiety source.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":484}],"confusable_with":""},
  {"id":"pain-assess-03","topic":"Pain Assessment Tools and Documentation","domain":"Anesthesia / Pain medicine","discipline":"anesthesia",
   "stem":"Why are standard pain scales less reliable in cognitively impaired or intubated ICU patients?",
   "answer":"Standard verbal NRS/VAS scales require self-report; cognitively impaired or intubated patients cannot self-report reliably, requiring behavioral observation scales (CPOT, BPS) validated for non-verbal patients.",
   "rationale":"Self-report is the gold standard for pain assessment; when it is unavailable, physiological (HR, BP) and behavioral (grimacing, guarding) proxies are used with validated behavioral tools to estimate pain.",
   "bloom":"analyze","source":[{"book":"Miller","page":682}],"confusable_with":""},
  {"id":"pain-assess-04","topic":"Pain Assessment Tools and Documentation","domain":"Anesthesia / Pain medicine","discipline":"anesthesia",
   "stem":"Why does geriatric pain management require special attention to analgesic dosing?",
   "answer":"Elderly patients require reduced doses of common analgesics (opioids, benzodiazepines, sedatives) due to altered pharmacokinetics and pharmacodynamics of aging.",
   "rationale":"Aging reduces hepatic/renal clearance, plasma protein binding, and volume of distribution, raising drug levels for the same dose; increased CNS sensitivity amplifies pharmacodynamic effects further.",
   "bloom":"apply","source":[{"book":"Miller","page":774}],"confusable_with":""}
]

# ── 204 Postoperative Pain Management ────────────────────────────────────────
entries += [
  {"id":"postop-pain-01","topic":"Postoperative Pain Management Protocols","domain":"Anesthesia / Pain medicine","discipline":"anesthesia",
   "stem":"What are the key goals of an Enhanced Recovery Program (ERP) in the context of postoperative pain?",
   "answer":"ERP goals: evidence-based practices, care continuity, reduction of care variation, minimization of organ dysfunction, decrease in complications, and acceleration of convalescence.",
   "rationale":"ERP bundles multimodal analgesia, early mobilization, and optimized fluid management into standardized protocols; reduction in variation drives measurable improvements in outcomes across institutions.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1811}],"confusable_with":""},
  {"id":"postop-pain-02","topic":"Postoperative Pain Management Protocols","domain":"Anesthesia / Pain medicine","discipline":"anesthesia",
   "stem":"What is gabapentin's original indication and how is it used in postoperative pain?",
   "answer":"Gabapentin was originally developed as an antiepileptic; it is now used as part of multimodal postoperative pain protocols.",
   "rationale":"Gabapentin inhibits voltage-gated calcium channels at the alpha-2-delta subunit, reducing excitatory neurotransmitter release from dorsal horn neurons — reducing central sensitization and opioid requirements postoperatively.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1832}],"confusable_with":"Pregabalin (same mechanism, more predictable bioavailability)"},
  {"id":"postop-pain-03","topic":"Postoperative Pain Management Protocols","domain":"Anesthesia / Pain medicine","discipline":"anesthesia",
   "stem":"What monitoring requirement applies to IV lidocaine when used for postoperative pain?",
   "answer":"IV lidocaine for postoperative pain requires cardiovascular monitoring; use is limited to PACU, ICU, or monitored ward settings.",
   "rationale":"Systemic lidocaine at analgesic doses (1–1.5 mg/kg/h infusion) carries risk of cardiac toxicity (arrhythmia, heart block) and CNS toxicity (seizure); continuous monitoring is mandatory.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1835}],"confusable_with":"Epidural lidocaine (local; cardiac monitoring less critical due to low systemic absorption)"},
  {"id":"postop-pain-04","topic":"Postoperative Pain Management Protocols","domain":"Anesthesia / Pain medicine","discipline":"anesthesia",
   "stem":"What is high-volume local anesthetic infiltration (LIA) and in which surgeries is it popular?",
   "answer":"LIA = infiltration of large volumes of local anesthetic + epinephrine ± NSAIDs into the surgical field; popular for total hip and total knee arthroplasty.",
   "rationale":"High-volume dilute LA floods the pericapsular tissue and periosteum, blocking multiple sensory afferents; epinephrine prolongs duration and reduces systemic absorption; adding NSAIDs (ketorolac) provides additional anti-inflammatory effect.",
   "bloom":"recall","source":[{"book":"Miller","page":744}],"confusable_with":"Peripheral nerve block (targeted neuraxial approach vs. field infiltration of LIA)"}
]

# ── 205 Preoperative Medication Reconciliation ────────────────────────────────
entries += [
  {"id":"med-recon-01","topic":"Preoperative medication reconciliation and deprescribing","domain":"Anesthesia / Perioperative medicine","discipline":"anesthesia",
   "stem":"What are the key steps in a complete perioperative medication reconciliation?",
   "answer":"Confirm current medications with patient and family; ask about administration system (blister packs, pill boxes); review prior notes and discharge summaries.",
   "rationale":"Patients frequently omit OTC medications, herbals, or recently prescribed drugs; multiple information sources (patient, family, prior records, dispensing systems) must be cross-checked to generate a complete and accurate medication list.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":171}],"confusable_with":""},
  {"id":"med-recon-02","topic":"Preoperative medication reconciliation and deprescribing","domain":"Anesthesia / Perioperative medicine","discipline":"anesthesia",
   "stem":"Why is flumazenil administration hazardous in a patient with chronic benzodiazepine use?",
   "answer":"Flumazenil given to a chronic benzodiazepine user may precipitate acute benzodiazepine withdrawal and seizures.",
   "rationale":"Chronic benzodiazepine exposure down-regulates GABA-A receptors; abrupt pharmacological reversal with flumazenil unmasks receptor hyposensitivity and can trigger status epilepticus in dependent patients.",
   "bloom":"apply","source":[{"book":"Miller","page":141}],"confusable_with":"Acute benzodiazepine overdose (flumazenil appropriate here; distinguish from chronic use)"},
  {"id":"med-recon-03","topic":"Preoperative medication reconciliation and deprescribing","domain":"Anesthesia / Perioperative medicine","discipline":"anesthesia",
   "stem":"What is the recommended preoperative anxiolytic for the majority of surgical patients?",
   "answer":"Midazolam 1–2 mg IV is the standard and effective preoperative anxiolytic/amnestic.",
   "rationale":"Midazolam's rapid onset, short duration, and reversibility (flumazenil) make it ideal for preoperative anxiolysis; the low dose minimizes residual sedation without significant hemodynamic depression.",
   "bloom":"recall","source":[{"book":"Miller","page":233}],"confusable_with":"Oral lorazepam (longer duration, less titratable — less ideal for day-surgery settings)"}
]

# ── 206 CRM / TeamSTEPPS ──────────────────────────────────────────────────────
entries += [
  {"id":"crm-01","topic":"Teamwork, Crew Resource Management & TeamSTEPPS","domain":"Patient safety / Communication","discipline":"medicine",
   "stem":"From what industry was Crew Resource Management (CRM) originally adapted?",
   "answer":"CRM was developed in the aviation industry to promote teamwork and allow any personnel to intervene or call for investigation of any safety concern.",
   "rationale":"Aviation recognized that most crashes involved communication and coordination failures, not technical errors; CRM training addresses these human factors; anesthesia adopted CRM because the OR shares the same time-pressure, high-stakes dynamic.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":56}],"confusable_with":""},
  {"id":"crm-02","topic":"Teamwork, Crew Resource Management & TeamSTEPPS","domain":"Patient safety / Communication","discipline":"medicine",
   "stem":"Under CRM principles, what should an anesthesiologist do when concerned about the safety of a surgical management plan?",
   "answer":"The anesthesiologist should voice concerns clearly and not proceed until a safe agreed-upon plan is in place.",
   "rationale":"Graded assertiveness — speaking up through a hierarchy — is a core CRM behavior; the anesthesiologist has both the authority and the professional obligation to halt a case until safety concerns are resolved.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":57}],"confusable_with":""},
  {"id":"crm-03","topic":"Teamwork, Crew Resource Management & TeamSTEPPS","domain":"Patient safety / Communication","discipline":"medicine",
   "stem":"How is communication defined in the CRM framework?",
   "answer":"Communication in CRM = clear and accurate sending AND receiving of information, instructions, and commands — a two-way verification process.",
   "rationale":"One-way information transfer is insufficient; closed-loop communication (receiver confirms receipt and understanding) is required to ensure accuracy, particularly critical for drug dosing or emergency commands.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":56}],"confusable_with":""},
  {"id":"crm-04","topic":"Teamwork, Crew Resource Management & TeamSTEPPS","domain":"Patient safety / Communication","discipline":"medicine",
   "stem":"What cognitive skill does CRM define as 'analysis', and why is it essential in the OR?",
   "answer":"CRM analysis = the ability to develop short-term, long-term, and contingency plans — essential in the OR to anticipate complications before they occur.",
   "rationale":"Anticipatory planning (mental simulation of 'what if') allows teams to prepare equipment and personnel for predictable crises, converting potential catastrophes into manageable events.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":57}],"confusable_with":""}
]

# ── 207 VTE Risk Stratification ────────────────────────────────────────────────
entries += [
  {"id":"vte-risk-01","topic":"VTE risk stratification and prophylaxis","domain":"Internal medicine / Surgery: thromboembolism","discipline":"medicine",
   "stem":"What is the core tension in perioperative antithrombotic decision-making?",
   "answer":"Perioperative antithrombotic management must balance the risk of surgical bleeding (if anticoagulation is continued) against the risk of thromboembolism (if anticoagulation is interrupted).",
   "rationale":"Both over-anticoagulation (surgical hemorrhage) and under-anticoagulation (DVT/PE/stroke) are potentially fatal; individualized risk stratification using validated tools is required to find the optimal balance.",
   "bloom":"apply","source":[{"book":"Miller","page":456}],"confusable_with":""},
  {"id":"vte-risk-02","topic":"VTE risk stratification and prophylaxis","domain":"Internal medicine / Surgery: thromboembolism","discipline":"medicine",
   "stem":"What VTE prophylaxis agents are recommended for moderate-risk vs. high-risk (trauma/orthopedic) surgical patients?",
   "answer":"Moderate VTE risk → LMWH; high-risk trauma/orthopedic → LMWH (both categories). Increased bleeding risk in any category → mechanical prophylaxis (IPC devices, compression stockings).",
   "rationale":"LMWH's predictable anti-Xa activity and once-daily dosing make it the evidence-based standard across both moderate and high-risk surgical populations; mechanical prophylaxis becomes the default when pharmacological agents are contraindicated.",
   "bloom":"recall","source":[{"book":"Miller","page":773}],"confusable_with":"Fondaparinux (acceptable for high-risk orthopedic but renally cleared; less commonly used)"},
  {"id":"vte-risk-03","topic":"VTE risk stratification and prophylaxis","domain":"Internal medicine / Surgery: thromboembolism","discipline":"medicine",
   "stem":"What factors determine when to discontinue a DOAC before surgery?",
   "answer":"DOAC discontinuation timing depends on the procedural bleeding risk (low vs. high-risk procedure) and the patient's renal function (affects drug clearance).",
   "rationale":"Renally cleared DOACs (dabigatran, apixaban, rivaroxaban) accumulate with reduced GFR; low-bleeding-risk procedures may only need 24-hour interruption vs 48–96 hours for high-risk procedures or impaired renal function.",
   "bloom":"apply","source":[{"book":"Miller","page":227}],"confusable_with":"Warfarin discontinuation (INR-guided, typically 5 days preop — different from DOAC management)"},
  {"id":"vte-risk-04","topic":"VTE risk stratification and prophylaxis","domain":"Internal medicine / Surgery: thromboembolism","discipline":"medicine",
   "stem":"What is the UFH prophylaxis dose and how does obesity modify it?",
   "answer":"Standard UFH prophylaxis: 5,000 units SQ BID–TID; obesity requires 5,000–7,500 units TID.",
   "rationale":"Increased adipose volume of distribution and higher heparin binding to proteins in obesity reduce the effective anti-Xa level of standard-dose UFH; dose escalation is needed to maintain prophylactic activity.",
   "bloom":"recall","source":[{"book":"StatPearls","page":3}],"confusable_with":"LMWH weight-based dosing (enoxaparin 40 mg daily standard; 40 mg BID for BMI > 40)"},
  {"id":"vte-risk-05","topic":"VTE risk stratification and prophylaxis","domain":"Internal medicine / Surgery: thromboembolism","discipline":"medicine",
   "stem":"Why is a multidisciplinary team approach emphasized in perioperative VTE management?",
   "answer":"Perioperative VTE management requires coordinated input from surgery, anesthesia, hematology/medicine, and pharmacy to individualize the balance of thrombotic and bleeding risk.",
   "rationale":"No single specialty has full visibility into all risk factors: surgeons know procedural bleeding risk; hematologists know thrombophilia burden; anesthesiologists manage neuraxial anticoagulation windows; pharmacists flag drug interactions.",
   "bloom":"apply","source":[{"book":"Miller","page":456}],"confusable_with":""}
]

# Write output
out_path = r"C:\Users\Dean\anesthesia_attending\data\kp_catalog_part_6.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(entries, f, indent=2, ensure_ascii=False)

print(f"Written {len(entries)} entries to {out_path}")
