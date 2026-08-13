import json, sys
sys.stdout.reconfigure(encoding='utf-8')

kps = []
DI = "anesthesia"

# ── 21: Transfusion Medicine: Compatibility & Emergency Protocols ─────────────
T = "Transfusion Medicine: Compatibility & Emergency Protocols"
D = "Anesthesia critical care (shock & resuscitation, sepsis, ARDS & mechanical ventilation, hemodynamic monitoring, AKI, sedation/delirium, nutrition, end-of-life)"
kps += [
  {"id":"trans-compat-1","topic":T,"domain":D,"discipline":DI,
   "stem":"In an emergency requiring transfusion before full compatibility testing, what is the most desirable approach?",
   "answer":"Transfuse type-specific, partially crossmatched pRBCs; if blood type unknown, use O-negative uncrossmatched blood.",
   "rationale":"Type-specific blood eliminates major ABO incompatibility; the partial crossmatch detects most clinically significant antibodies without the 45-minute full crossmatch delay.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":471}],"confusable_with":"O-positive blood (acceptable for males and post-menopausal females when O-neg is scarce)"},
  {"id":"trans-compat-2","topic":T,"domain":D,"discipline":DI,
   "stem":"The antibody screen (indirect Coombs test) detects antibodies against what?",
   "answer":"Common minor RBC surface antigens (non-ABO antibodies in recipient serum).",
   "rationale":"The antibody screen uses reagent red cells of known antigenicity; agglutination identifies clinically significant alloantibodies that could cause delayed hemolytic transfusion reactions.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":471}],"confusable_with":"Direct Coombs test (detects antibodies already on patient's RBCs)"},
  {"id":"trans-compat-3","topic":T,"domain":D,"discipline":DI,
   "stem":"The full crossmatch (indirect Coombs test) requires approximately how long and what does it detect?",
   "answer":"45 minutes; detects antibodies in recipient serum against donor RBC antigens (non-ABO hemolytic antibodies).",
   "rationale":"Mixing recipient serum with donor cells and adding Coombs reagent identifies antibody-antigen reactions that would cause delayed hemolytic reactions.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1958}],"confusable_with":"Type and screen (no donor cells used, takes less time)"},
  {"id":"trans-compat-4","topic":T,"domain":D,"discipline":DI,
   "stem":"Blood banks now accept plasma and platelet donations from female donors only under what condition, and why?",
   "answer":"Only from females who have never been pregnant or who have been tested and found anti-HLA negative; to prevent TRALI (transfusion-related acute lung injury).",
   "rationale":"Multiparous women develop anti-HLA and anti-HNA antibodies from fetal sensitization; these antibodies in donor plasma activate recipient neutrophils causing TRALI.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1332}],"confusable_with":"TACO (transfusion-associated circulatory overload, the biggest transfusion risk in trauma resuscitation now)"},
  {"id":"trans-compat-5","topic":T,"domain":D,"discipline":DI,
   "stem":"What is now the greatest transfusion risk patients face during trauma resuscitation, having surpassed TRALI?",
   "answer":"Transfusion-associated circulatory overload (TACO).",
   "rationale":"As TRALI prevention through male-only and screened female plasma donation has reduced TRALI incidence, TACO has emerged as the most common serious transfusion complication in resuscitation.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1332}],"confusable_with":"TRALI"}
]

# ── 22: Tricuspid Valve Disease ───────────────────────────────────────────────
T = "Tricuspid Valve Disease"
D = "Cardiac anesthesia (valvular heart disease, coronary artery disease, heart failure, pericardial disease, aortic surgery, cardiac rhythm devices, TAVR, transplant)"
kps += [
  {"id":"tricuspid-vd-1","topic":T,"domain":D,"discipline":DI,
   "stem":"What is the most common cause of clinically significant tricuspid regurgitation?",
   "answer":"Dilation of the right ventricle from pulmonary hypertension (secondary/functional TR).",
   "rationale":"Pulmonary hypertension increases RV afterload causing RV dilation; the dilated annulus distorts leaflet coaptation, producing functional regurgitation without primary leaflet disease.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":679}],"confusable_with":"Rheumatic TR (primary leaflet disease, less common cause)"},
  {"id":"tricuspid-vd-2","topic":T,"domain":D,"discipline":DI,
   "stem":"For clinically significant tricuspid regurgitation, what hemodynamic goals should anesthetic management target?",
   "answer":"Avoid hypovolemia and factors that increase right ventricular afterload (hypoxia, acidosis, hypercarbia); maintain effective right ventricular stroke volume.",
   "rationale":"TR physiology depends on maintaining adequate preload and minimizing RV afterload; hypoxia-induced pulmonary vasoconstriction worsens TR and RV failure.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":680}],"confusable_with":"Mitral regurgitation goals (focus on LV afterload reduction)"},
  {"id":"tricuspid-vd-3","topic":T,"domain":D,"discipline":DI,
   "stem":"Tricuspid regurgitation is most commonly trivial (trace to mild). What symptom does clinically significant TR produce?",
   "answer":"Hepatomegaly, ascites, peripheral edema from elevated right-sided pressures (systemic venous hypertension).",
   "rationale":"Significant TR causes chronic elevation of right atrial and systemic venous pressure, resulting in hepatic congestion, ascites, and edema.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":679}],"confusable_with":"Left heart failure symptoms (orthopnea, pulmonary edema)"},
  {"id":"tricuspid-vd-4","topic":T,"domain":D,"discipline":DI,
   "stem":"Sympathetic fibers innervate what cardiac structures and what is their primary effect on contractility?",
   "answer":"Atrial and ventricular muscle; sympathetic activation is the most important physiologic determinant of myocardial contractility.",
   "rationale":"Norepinephrine released from sympathetic terminals binds beta-1 receptors, increasing intracellular cAMP, calcium entry, and myocardial contractile force.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":580}],"confusable_with":""},
  {"id":"tricuspid-vd-5","topic":T,"domain":D,"discipline":DI,
   "stem":"Large left-to-right shunts causing congestive heart failure and pulmonary hypertension are more commonly encountered in adults with which congenital defect?",
   "answer":"Atrial septal defect (ASD), particularly ostium primum defects with large shunts.",
   "rationale":"ASDs often allow chronic left-to-right shunting for decades before symptoms develop; the chronic pulmonary overcirculation causes pulmonary hypertension and eventually right heart failure.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":688}],"confusable_with":"VSD (typically presents earlier in childhood)"}
]
kps.append({"_type":"confusable_pair","topic_a":"Functional tricuspid regurgitation","topic_b":"Primary (rheumatic) tricuspid regurgitation",
   "discriminator":"Functional TR has a structurally normal valve with dilated annulus from RV volume/pressure overload; rheumatic TR has thickened, fused leaflets with concurrent mitral and aortic involvement"})

# ── 23: Univent tube and single-lumen tube with bronchial blocker ─────────────
T = "Univent tube and single-lumen tube with bronchial blocker"
D = "Subspecialty & out-of-OR anesthesia (ENT/shared airway, ophthalmology, orthopedics, transplant, vascular, ambulatory/office, non-operating-room anesthesia, robotic, laser)"
kps += [
  {"id":"univent-bb-1","topic":T,"domain":D,"discipline":DI,
   "stem":"What is the major advantage of a single-lumen tube with bronchial blocker over a double-lumen tube for lung isolation?",
   "answer":"The single-lumen tube does not need to be replaced with a conventional tracheal tube if the patient will remain intubated postoperatively.",
   "rationale":"DLTs are large and uncomfortable for long-term intubation; a single-lumen tube with a removable blocker can remain in place for postoperative ventilation without tube exchange.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":902}],"confusable_with":"Double-lumen tube advantage: ability to independently suction and ventilate each lung"},
  {"id":"univent-bb-2","topic":T,"domain":D,"discipline":DI,
   "stem":"What is the major disadvantage of a single-lumen tube with bronchial blocker compared with a double-lumen tube?",
   "answer":"The bronchial blocker must be advanced, positioned, and inflated under direct visualization via flexible bronchoscope, adding time and technical complexity.",
   "rationale":"Unlike a DLT where the bronchial lumen provides a built-in guide, the blocker is a separate device that requires bronchoscopic guidance for correct placement.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":902}],"confusable_with":""},
  {"id":"univent-bb-3","topic":T,"domain":D,"discipline":DI,
   "stem":"Problems with a left-sided double-lumen tube are usually related to three possibilities: tube tip too distal, too proximal, or wrong side. What complication occurs if the bronchial cuff is too distal on the left?",
   "answer":"The bronchial cuff can obstruct the left upper lobe bronchus, causing left upper lobe collapse during one-lung ventilation.",
   "rationale":"The left main bronchus is long enough that excessive advancement occludes the LUL takeoff; careful bronchoscopic confirmation prevents this.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":901}],"confusable_with":""},
  {"id":"univent-bb-4","topic":T,"domain":D,"discipline":DI,
   "stem":"During one-lung anesthesia, if hypoxemia develops, what is the first intervention to confirm?",
   "answer":"Adequate position of the endobronchial tube or bronchial blocker must be confirmed by repeat fiberoptic bronchoscopy, as surgical traction can displace the tube.",
   "rationale":"Tube migration during surgery is common; malpositioning causes ventilation of the wrong lung or inadequate isolation, both contributing to hypoxemia.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":913}],"confusable_with":""},
  {"id":"univent-bb-5","topic":T,"domain":D,"discipline":DI,
   "stem":"After thoracic surgery, most patients are extubated shortly after surgery for what specific reason?",
   "answer":"To decrease the risk of pulmonary barotrauma, particularly blowout (rupture) of the bronchial suture line.",
   "rationale":"Positive-pressure ventilation after pneumonectomy or lobectomy creates tension at the bronchial stump; early extubation to spontaneous breathing eliminates this risk.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":914}],"confusable_with":""}
]

print(f"Topics 21-23 drafted: {len(kps)} KPs")
