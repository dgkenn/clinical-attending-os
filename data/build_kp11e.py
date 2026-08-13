import json, sys
sys.stdout.reconfigure(encoding='utf-8')

kps = []
DI = "anesthesia"

# ── 18: Tracheostomy anesthesia (surgical and percutaneous) ───────────────────
T = "Tracheostomy anesthesia (surgical and percutaneous)"
D = "Subspecialty & out-of-OR anesthesia (ENT/shared airway, ophthalmology, orthopedics, transplant, vascular, ambulatory/office, non-operating-room anesthesia, robotic, laser)"
kps += [
  {"id":"trach-anes-1","topic":T,"domain":D,"discipline":DI,
   "stem":"What are the options for front-of-neck airway when CICO occurs, distinguishing surgical from percutaneous approaches?",
   "answer":"Surgical options: surgical tracheostomy and scalpel cricothyrotomy; percutaneous options: needle/catheter cricothyrotomy and percutaneous dilatational tracheostomy.",
   "rationale":"Surgical approaches are faster and more reliable in emergencies; percutaneous techniques require specialized equipment and carry higher emergency failure rates.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":539}],"confusable_with":""},
  {"id":"trach-anes-2","topic":T,"domain":D,"discipline":DI,
   "stem":"The fiber-optic bronchoscope should be used before withdrawing it after endotracheal tube placement to confirm what?",
   "answer":"Appropriate depth of endotracheal tube placement before it is withdrawn.",
   "rationale":"Resistance to removal of the bronchoscope can indicate inadvertent passage through the Murphy eye or kinking in the pharynx; confirming position before withdrawal prevents unrecognized endobronchial placement.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":299}],"confusable_with":""},
  {"id":"trach-anes-3","topic":T,"domain":D,"discipline":DI,
   "stem":"During TURP, why is it necessary to rely on clinical signs of hypovolemia rather than direct blood loss measurement?",
   "answer":"Blood loss is mixed with irrigating solution and cannot be accurately assessed visually; clinical signs (tachycardia, hypotension) must guide resuscitation.",
   "rationale":"Dilution of blood in the irrigant makes visual estimation impossible; blood loss averages ~3-5 mL/min of resection time and must be estimated from hemodynamic trends.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1133}],"confusable_with":""},
  {"id":"trach-anes-4","topic":T,"domain":D,"discipline":DI,
   "stem":"Percutaneous aortic valve replacement (TAVR) is performed in a hybrid OR under angiographic guidance; during valve deployment, what cardiac intervention is performed?",
   "answer":"Rapid ventricular pacing to reduce cardiac output temporarily, ensuring precise valve positioning without ejection dislodging the prosthesis.",
   "rationale":"Momentary cardiac standstill via rapid pacing (180-220 bpm) reduces stroke volume to near zero, preventing ejection forces from displacing the valve during deployment.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":759}],"confusable_with":""},
  {"id":"trach-anes-5","topic":T,"domain":D,"discipline":DI,
   "stem":"What is the anatomical landmark for tracheostomy tube placement in the neck?",
   "answer":"Air enters through nares, is warmed and humidified through the nasal cavity, passes through the larynx, and enters the trachea; tracheostomy is placed below the cricoid cartilage through tracheal rings 2-4.",
   "rationale":"Placement below the cricoid avoids subglottic damage and the cricothyroid membrane; rings 2-4 provide stable cartilaginous support for the tube.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":278}],"confusable_with":"Cricothyrotomy (through cricothyroid membrane, for emergency access)"}
]

# ── 19: Transesophageal Echocardiography (TEE) in Anesthesia ─────────────────
T = "Transesophageal Echocardiography (TEE) in Anesthesia"
D = "Cardiac anesthesia (valvular heart disease, coronary artery disease, heart failure, pericardial disease, aortic surgery, cardiac rhythm devices, TAVR, transplant)"
kps += [
  {"id":"tee-anes-1","topic":T,"domain":D,"discipline":DI,
   "stem":"What four main applications does intraoperative TEE provide during cardiac surgery?",
   "answer":"Assessment of valvular function (morphology, gradients, regurgitation severity), ventricular function evaluation, IVC assessment for volume status, and detection of air/thrombus.",
   "rationale":"TEE provides real-time high-resolution cardiac imaging unavailable from surface echocardiography; it guides surgical decisions and monitors hemodynamic status throughout the procedure.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":727}],"confusable_with":"TTE (lower resolution, no real-time intraoperative use)"},
  {"id":"tee-anes-2","topic":T,"domain":D,"discipline":DI,
   "stem":"Unlike TTE, TEE is an invasive procedure. What is one specific life-threatening complication of TEE?",
   "answer":"Esophageal perforation (among other serious complications associated with esophageal probe insertion).",
   "rationale":"The TEE probe is advanced blindly into the esophagus and can cause mucosal tears, perforation, or exacerbation of pre-existing esophageal pathology.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":177}],"confusable_with":""},
  {"id":"tee-anes-3","topic":T,"domain":D,"discipline":DI,
   "stem":"Color-flow Doppler TEE is invaluable in aortic insufficiency for what two specific assessments?",
   "answer":"Quantitating the severity of regurgitation and guiding therapeutic interventions (surgical repair or replacement decisions).",
   "rationale":"The regurgitant jet area and width relative to LVOT diameter on color Doppler provides semiquantitative grading of AI severity intraoperatively.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":678}],"confusable_with":""},
  {"id":"tee-anes-4","topic":T,"domain":D,"discipline":DI,
   "stem":"The IVC examination on TEE/TTE is most useful at what extremes to guide fluid management?",
   "answer":"Most useful when IVC is very small and collapsing (suggesting hypovolemia) or very large and non-collapsing (suggesting volume overload or elevated CVP).",
   "rationale":"Intermediate IVC sizes have high variability and should be interpreted with the full clinical picture; extreme values are actionable.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":414}],"confusable_with":""},
  {"id":"tee-anes-5","topic":T,"domain":D,"discipline":DI,
   "stem":"For patients undergoing electrophysiology procedures with fluid distension, what complication must the anesthesiologist anticipate in patients with prior heart failure?",
   "answer":"Volume overload from substantial irrigant absorption; diuretic therapy may be required to avoid acute decompensated heart failure.",
   "rationale":"Long EP procedures can accumulate significant intravascular fluid from catheter irrigation; heart failure patients have limited reserve for this volume load.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":713}],"confusable_with":"TURP syndrome (irrigant is hypotonic; EP irrigant is isotonic)"}
]

# ── 20: Transfusion Medicine in the ICU ───────────────────────────────────────
T = "Transfusion Medicine in the ICU"
D = "Anesthesia critical care (shock & resuscitation, sepsis, ARDS & mechanical ventilation, hemodynamic monitoring, AKI, sedation/delirium, nutrition, end-of-life)"
kps += [
  {"id":"trans-icu-1","topic":T,"domain":D,"discipline":DI,
   "stem":"What are the principles of damage control resuscitation in massive hemorrhage, and which principle addresses coagulopathy directly?",
   "answer":"Permissive hypotension, stop bleeding early, early hemostatic products, and minimize crystalloid; early hemostatic products (blood/plasma/platelets) directly addresses coagulopathy.",
   "rationale":"Replacing clotting factors lost in hemorrhage with plasma and platelets prevents the consumptive coagulopathy that leads to the lethal triad.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":801}],"confusable_with":""},
  {"id":"trans-icu-2","topic":T,"domain":D,"discipline":DI,
   "stem":"Antiphospholipid antibody syndrome (APS) characteristically shows what coagulation test abnormality, and what is the associated thrombotic risk?",
   "answer":"Mild prolongation of aPTT and positive antiphospholipid antibodies (lupus anticoagulant, anticardiolipin); associated with arterial and venous thrombosis and ischemic necrosis.",
   "rationale":"The paradox of APS is that a prolonged aPTT in vitro reflects antibody competition with phospholipid reagent, while in vivo these antibodies cause thrombosis.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":447}],"confusable_with":"DIC (prolonged PT and aPTT from factor consumption, with bleeding)"},
  {"id":"trans-icu-3","topic":T,"domain":D,"discipline":DI,
   "stem":"After massive transfusion with citrated blood products, metabolic alkalosis commonly occurs postoperatively for what reason?",
   "answer":"Citrate and lactate contained in transfusions are metabolized to bicarbonate once tissue perfusion is restored.",
   "rationale":"Citrate is a bicarbonate precursor; when the liver and kidneys clear it after resuscitation, the resulting HCO3 load produces metabolic alkalosis.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1944}],"confusable_with":"Metabolic acidosis from hemorrhagic shock (resolves with restoration of perfusion)"},
  {"id":"trans-icu-4","topic":T,"domain":D,"discipline":DI,
   "stem":"What are the risk factors for postanesthetic apnea in neonates, beyond prematurity?",
   "answer":"Anemia (<30% hematocrit), hypothermia, sepsis, and neurological abnormalities.",
   "rationale":"These factors impair respiratory drive and chemoreceptor sensitivity; even full-term neonates can experience rare apneic spells after general anesthesia.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1477}],"confusable_with":""},
  {"id":"trans-icu-5","topic":T,"domain":D,"discipline":DI,
   "stem":"Allergic transfusion reactions (urticaria, anaphylaxis) are more common with platelet transfusions than erythrocyte transfusions. What is a specific complication associated with platelets?",
   "answer":"Hypersensitivity reactions including urticaria, anaphylaxis, and anaphylactic shock are more frequent with platelet transfusions.",
   "rationale":"Platelets are suspended in donor plasma containing allergens (proteins, IgA); IgA-deficient recipients can form anti-IgA antibodies causing severe anaphylaxis.",
   "bloom":"recall","source":[{"book":"Marino ICU Book","page":520}],"confusable_with":"TRALI (mainly associated with plasma and platelets but different mechanism)"}
]

print(f"Topics 18-20 drafted: {len(kps)} KPs")
