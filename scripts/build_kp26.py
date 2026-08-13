import json, sys
sys.stdout.reconfigure(encoding='utf-8')

kps = []

# ── Topic 0: Remifentanil pharmacology ──────────────────────────────────────
kps += [
  {"id":"remifentanil-pharmacology-1","topic":"Remifentanil: pharmacology","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"An opioid is infused at 0.25-1 mcg/kg/min during cardiac surgery via TCI. What property makes this drug uniquely suitable for prolonged infusions requiring rapid offset?",
   "answer":"Remifentanil is hydrolyzed by plasma esterases yielding a context-sensitive half-time of approximately 3 minutes regardless of infusion duration.",
   "rationale":"Ester hydrolysis by nonspecific plasma esterases (not pseudocholinesterase) produces an inactive acid metabolite, ensuring predictable rapid offset even after hours of infusion.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":737}],"confusable_with":"Sufentanil (context-sensitive half-time increases with infusion duration)"},
  {"id":"remifentanil-pharmacology-2","topic":"Remifentanil: pharmacology","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"During cardiac surgery a patient receives a high-dose opioid plus a benzodiazepine for anesthesia. What hemodynamic interaction is amplified?",
   "answer":"The opioid-benzodiazepine combination markedly reduces arterial blood pressure and peripheral vascular resistance through synergistic sympatholysis.",
   "rationale":"Both drug classes attenuate sympathetic tone; their combination produces supra-additive vasodilation beyond either drug alone, particularly observed in cardiac surgery patients.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":284}],"confusable_with":""},
  {"id":"remifentanil-pharmacology-3","topic":"Remifentanil: pharmacology","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"A patient develops severe acute pain immediately after a remifentanil infusion is discontinued at end of case. What should have been done before stopping the infusion?",
   "answer":"Administer bridge analgesia (e.g., morphine, ketorolac, or neuraxial opioid) before stopping remifentanil to cover its near-immediate analgesic offset.",
   "rationale":"Remifentanil's approximately 3 min context-sensitive half-time leaves no residual analgesia once discontinued; without a bridge, acute severe pain and opioid-induced hyperalgesia can occur.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":2098}],"confusable_with":"Fentanyl (prolonged residual analgesia after long infusions due to context-sensitive accumulation)"},
  {"id":"remifentanil-pharmacology-4","topic":"Remifentanil: pharmacology","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"Which receptor does remifentanil primarily act at, and what antagonist reverses its effects?",
   "answer":"Remifentanil acts at the mu opioid receptor; naloxone (pure mu antagonist) reverses its effects; naltrexone is a longer-acting oral antagonist used for addiction maintenance.",
   "rationale":"All clinical opioid analgesia and respiratory depression is mediated via mu receptors; competitive antagonism by naloxone reverses all mu-mediated effects.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":466}],"confusable_with":"Naltrexone (oral, long-acting; not for acute perioperative reversal)"},
  {"id":"remifentanil-pharmacology-5","topic":"Remifentanil: pharmacology","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"An older patient requires remifentanil for anesthesia. How does aging alter opioid dose requirement?",
   "answer":"Older adults require lower opioid doses; pharmacodynamic sensitivity is increased and clearance of many drugs is reduced with age.",
   "rationale":"The principal pharmacodynamic change with aging is increased sensitivity to anesthetic and analgesic drugs, plus reduced hepatic/renal clearance, requiring dose reduction across opioids, benzodiazepines, and hypnotics.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1490}],"confusable_with":""}
]

# ── Topic 1: Renal Physiology ────────────────────────────────────────────────
kps += [
  {"id":"renal-physiology-1","topic":"Renal Physiology","domain":"Anesthesia: basic & clinical sciences (relevant anatomy, respiratory/cardiac/renal/neuro physiology, pharmacokinetics/dynamics principles, physics of gases & flow, statistics)","discipline":"anesthesia",
   "stem":"A hospitalized patient's serum creatinine rises 0.3 mg/dL within 48 hours. By KDIGO criteria, what does this define?",
   "answer":"AKI Stage 1: serum Cr rise >=0.3 mg/dL within 48 h; OR >=1.5x baseline within 7 days; OR urine output <0.5 mL/kg/h for >=6 h.",
   "rationale":"KDIGO 2012 standardized AKI diagnosis using absolute or relative creatinine criteria or oliguria thresholds to enable early recognition.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":99}],"confusable_with":"CKD (defined by abnormalities present >3 months)"},
  {"id":"renal-physiology-2","topic":"Renal Physiology","domain":"Anesthesia: basic & clinical sciences (relevant anatomy, respiratory/cardiac/renal/neuro physiology, pharmacokinetics/dynamics principles, physics of gases & flow, statistics)","discipline":"anesthesia",
   "stem":"A patient's creatinine is rising 1.2 mg/dL/day. What GFR assumption must be made?",
   "answer":"When creatinine is changing rapidly (delta-Cr >1 mg/dL/day), serum Cr does not approximate GFR at steady state; assume GFR <10 mL/min.",
   "rationale":"Serum creatinine only approximates GFR under steady-state conditions; during acute injury, rising creatinine lags behind the true degree of GFR loss.",
   "bloom":"analyze","source":[{"book":"MGH Housestaff Manual","page":99}],"confusable_with":""},
  {"id":"renal-physiology-3","topic":"Renal Physiology","domain":"Anesthesia: basic & clinical sciences (relevant anatomy, respiratory/cardiac/renal/neuro physiology, pharmacokinetics/dynamics principles, physics of gases & flow, statistics)","discipline":"anesthesia",
   "stem":"A patient on trimethoprim has a rising creatinine but stable BUN. What is the mechanism?",
   "answer":"Trimethoprim and H2-blockers (e.g., cimetidine) impair tubular creatinine secretion without reducing GFR; BUN remains stable confirming no true GFR loss.",
   "rationale":"Creatinine is both filtered and secreted; drugs blocking tubular secretion raise serum Cr independent of GFR; BUN stability confirms this artifact.",
   "bloom":"analyze","source":[{"book":"MGH Housestaff Manual","page":99}],"confusable_with":"True AKI (where BUN rises proportionally with Cr)"},
  {"id":"renal-physiology-4","topic":"Renal Physiology","domain":"Anesthesia: basic & clinical sciences (relevant anatomy, respiratory/cardiac/renal/neuro physiology, pharmacokinetics/dynamics principles, physics of gases & flow, statistics)","discipline":"anesthesia",
   "stem":"A patient with chronic hypertension develops oliguria intraoperatively despite MAP of 70 mmHg. What physiologic principle explains this?",
   "answer":"Chronic hypertension shifts renal autoregulation to a higher MAP range; a MAP of 70 mmHg may fall below the autoregulatory threshold for these kidneys, making urine output blood pressure-dependent.",
   "rationale":"Structural vascular changes from chronic hypertension reset renal autoregulation upward; what maintains flow in normotensive kidneys may be inadequate in hypertensive patients.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1087}],"confusable_with":""},
  {"id":"renal-physiology-5","topic":"Renal Physiology","domain":"Anesthesia: basic & clinical sciences (relevant anatomy, respiratory/cardiac/renal/neuro physiology, pharmacokinetics/dynamics principles, physics of gases & flow, statistics)","discipline":"anesthesia",
   "stem":"In the PACU, a patient has urine output <0.5 mL/kg/h. What is the single most easily remedied cause to exclude first?",
   "answer":"Urinary catheter obstruction or dislodgment is the most easily remedied and often overlooked cause of postoperative oliguria.",
   "rationale":"Before attributing oliguria to volume depletion or intrinsic renal injury, confirming catheter patency by flushing or repositioning takes seconds and avoids unnecessary fluid or vasopressor administration.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":732}],"confusable_with":""}
]

# ── Topic 2: Renal Protection During Cardiac Surgery ─────────────────────────
kps += [
  {"id":"renal-protection-cardiac-1","topic":"Renal Protection During Cardiac Surgery","domain":"Cardiovascular & cardiac anesthesia (CABG, valvular, cardiopulmonary bypass, TEE basics, cardiac physiology, hemodynamic & vasoactive management, ICDs/pacemakers)","discipline":"anesthesia",
   "stem":"A patient with a creatinine clearance of 65 mL/min is scheduled for CABG. Why might clinical signs of renal dysfunction be absent?",
   "answer":"The kidney has a large functional reserve; GFR can decrease from 120 to 60 mL/min without clinical signs or symptoms.",
   "rationale":"Subclinical nephron loss is compensated by hyperfiltration in remaining nephrons; clinical manifestations appear only after substantial GFR reduction.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1117}],"confusable_with":""},
  {"id":"renal-protection-cardiac-2","topic":"Renal Protection During Cardiac Surgery","domain":"Cardiovascular & cardiac anesthesia (CABG, valvular, cardiopulmonary bypass, TEE basics, cardiac physiology, hemodynamic & vasoactive management, ICDs/pacemakers)","discipline":"anesthesia",
   "stem":"What is the primary intraoperative renal protection strategy during cardiopulmonary bypass?",
   "answer":"Maintain adequate intravascular volume and cardiac output to ensure renal perfusion; avoid nephrotoxins; ensure MAP above the patient's autoregulatory threshold during bypass.",
   "rationale":"Renal ischemia from low flow, hypotension, or hemodilution during CPB is the dominant mechanism of cardiac surgery-associated AKI.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1092}],"confusable_with":""},
  {"id":"renal-protection-cardiac-3","topic":"Renal Protection During Cardiac Surgery","domain":"Cardiovascular & cardiac anesthesia (CABG, valvular, cardiopulmonary bypass, TEE basics, cardiac physiology, hemodynamic & vasoactive management, ICDs/pacemakers)","discipline":"anesthesia",
   "stem":"Why is renal management in patients with mild-to-moderate renal insufficiency as critical as in frank kidney failure when planning cardiac surgery?",
   "answer":"Procedures with high incidence of postoperative kidney failure (cardiac, aortic surgery) can precipitate acute decompensation in patients with preexisting renal insufficiency; even mild dysfunction markedly increases risk.",
   "rationale":"Preexisting CKD limits renal reserve, so an additional ischemic insult from CPB, hypotension, or contrast can cause irreversible failure.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1092}],"confusable_with":""},
  {"id":"renal-protection-cardiac-4","topic":"Renal Protection During Cardiac Surgery","domain":"Cardiovascular & cardiac anesthesia (CABG, valvular, cardiopulmonary bypass, TEE basics, cardiac physiology, hemodynamic & vasoactive management, ICDs/pacemakers)","discipline":"anesthesia",
   "stem":"Low-dose dopamine was historically used for renal protection in cardiac surgery. What does current evidence show?",
   "answer":"Dopamine has not been shown to benefit renal function in shock states; its routine use is questionable as it may increase mortality and arrhythmic events.",
   "rationale":"Despite theoretical dopaminergic vasodilation of renal vasculature, randomized trials showed no renal protection and potential harms from arrhythmias.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":98}],"confusable_with":"Fenoldopam (selective DA1 agonist with some evidence in high-risk cardiac surgery)"},
  {"id":"renal-protection-cardiac-5","topic":"Renal Protection During Cardiac Surgery","domain":"Cardiovascular & cardiac anesthesia (CABG, valvular, cardiopulmonary bypass, TEE basics, cardiac physiology, hemodynamic & vasoactive management, ICDs/pacemakers)","discipline":"anesthesia",
   "stem":"Even mild renal dysfunction before cardiac surgery has what implication for perioperative outcomes?",
   "answer":"Even mild renal dysfunction is associated with an increased likelihood of poor postoperative outcomes; renal disease is prevalent and amplifies risk for cardiac surgery patients.",
   "rationale":"Pre-existing CKD reduces the kidney's tolerance for additional ischemic or hemodynamic insults, making it a significant independent risk factor.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":522}],"confusable_with":""}
]

# ── Topic 3: Renal disease and perioperative AKI prevention ──────────────────
kps += [
  {"id":"renal-aki-prevention-1","topic":"Renal disease and perioperative AKI prevention","domain":"Preoperative evaluation & perioperative medicine (risk stratification, cardiac/pulmonary/endocrine optimization, NPO & aspiration risk, chronic medication management, frailty, consent)","discipline":"anesthesia",
   "stem":"By KDIGO 2012, what three criteria diagnose AKI?",
   "answer":"AKI: serum Cr rise >=0.3 mg/dL within 48 h; OR >=1.5x baseline within 7 days; OR urine output <0.5 mL/kg/h for >=6 h.",
   "rationale":"KDIGO standardized AKI diagnosis to enable early recognition and staging regardless of absolute creatinine value.",
   "bloom":"recall","source":[{"book":"Society Guideline: Guideline   KDIGO 2012 AKI","page":22}],"confusable_with":"CKD (eGFR <60 or kidney damage markers for >3 months)"},
  {"id":"renal-aki-prevention-2","topic":"Renal disease and perioperative AKI prevention","domain":"Preoperative evaluation & perioperative medicine (risk stratification, cardiac/pulmonary/endocrine optimization, NPO & aspiration risk, chronic medication management, frailty, consent)","discipline":"anesthesia",
   "stem":"Which antihypertensive drug classes are common co-contributors to perioperative AKI and require careful preoperative review?",
   "answer":"ACE inhibitors and ARBs impair autoregulation of GFR; they are common co-contributors to perioperative AKI and often held before major surgery.",
   "rationale":"ACE inhibitors and ARBs block angiotensin II-mediated efferent arteriolar constriction, which is the compensatory mechanism maintaining GFR during hypotension or volume depletion.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Acute kidney injury","page":6}],"confusable_with":"NSAIDs (reduce afferent arteriolar dilation; also nephrotoxic but different mechanism)"},
  {"id":"renal-aki-prevention-3","topic":"Renal disease and perioperative AKI prevention","domain":"Preoperative evaluation & perioperative medicine (risk stratification, cardiac/pulmonary/endocrine optimization, NPO & aspiration risk, chronic medication management, frailty, consent)","discipline":"anesthesia",
   "stem":"When BUN and creatinine are still within the normal range but AKI is developing, what may be the only detectable sign?",
   "answer":"Decline in urine output below 0.5 mL/kg/h for >=6 h may be the only sign of AKI before creatinine rises.",
   "rationale":"Creatinine rises only after significant nephron mass is lost or acute injury evolves; oliguria can precede laboratory evidence of AKI by hours.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Acute kidney injury","page":2}],"confusable_with":""},
  {"id":"renal-aki-prevention-4","topic":"Renal disease and perioperative AKI prevention","domain":"Preoperative evaluation & perioperative medicine (risk stratification, cardiac/pulmonary/endocrine optimization, NPO & aspiration risk, chronic medication management, frailty, consent)","discipline":"anesthesia",
   "stem":"A prerenal oliguric patient is conserving sodium maximally. What hormone mediates this response?",
   "answer":"Aldosterone (via the renin-angiotensin-aldosterone system activated by decreased renal blood flow) mediates tubular sodium conservation to restore intravascular volume.",
   "rationale":"Decreased renal blood flow from hypovolemia or reduced cardiac output triggers RAAS; aldosterone acts on the distal tubule and collecting duct to reabsorb sodium.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":528}],"confusable_with":"ADH/vasopressin (mediates water retention; released in parallel but separate mechanism)"},
  {"id":"renal-aki-prevention-5","topic":"Renal disease and perioperative AKI prevention","domain":"Preoperative evaluation & perioperative medicine (risk stratification, cardiac/pulmonary/endocrine optimization, NPO & aspiration risk, chronic medication management, frailty, consent)","discipline":"anesthesia",
   "stem":"What initial laboratory and urine studies are warranted in all patients presenting with AKI?",
   "answer":"Comprehensive metabolic panel, urine electrolytes (for FeNa), urine osmolality, and urinalysis with microscopy; also review contrast exposure and nephrotoxic medications.",
   "rationale":"These tests distinguish prerenal (FeNa <1%, concentrated urine), intrinsic/ATN (muddy brown casts, FeNa >2%), and postrenal AKI, guiding targeted intervention.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Acute kidney injury","page":6}],"confusable_with":""}
]

# ── Topic 4: Sciatic nerve blocks ────────────────────────────────────────────
kps += [
  {"id":"sciatic-nerve-blocks-1","topic":"Sciatic nerve blocks","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"What nerve roots comprise the sciatic nerve, and which lower extremity territory does it NOT cover?",
   "answer":"Sciatic nerve = L4, L5, S1-S3; it does not cover the medial leg and ankle (saphenous nerve, a femoral nerve branch), which requires a separate saphenous or femoral block.",
   "rationale":"The sciatic supplies the entire lower limb below the knee except the medial strip; complete lower extremity anesthesia for surgery requiring medial ankle coverage needs combined sciatic and saphenous/femoral blockade.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1670}],"confusable_with":"Femoral nerve block (covers anterior thigh and medial leg/knee, not posterior or foot)"},
  {"id":"sciatic-nerve-blocks-2","topic":"Sciatic nerve blocks","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"At the popliteal fossa, the sciatic nerve divides into two terminal branches. What are they, and how is the block needle directed under ultrasound?",
   "answer":"The sciatic divides into the common peroneal (lateral) and tibial (medial) nerves at or proximal to the popliteal crease; the needle is inserted lateral to the transducer in-plane, traversing the biceps femoris.",
   "rationale":"In-plane ultrasound needle visualization ensures real-time tip tracking; inserting lateral to the transducer allows optimal nerve contact at the division or proximal to it.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1676}],"confusable_with":""},
  {"id":"sciatic-nerve-blocks-3","topic":"Sciatic nerve blocks","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"For a subgluteal sciatic nerve block, what key vascular landmark near the nerve must be identified with color Doppler?",
   "answer":"The inferior gluteal artery and vein lie adjacent to the sciatic nerve at the subgluteal level; color-flow Doppler identifies these vessels before needle insertion.",
   "rationale":"Unrecognized vascular puncture at the subgluteal level can cause significant hematoma; ultrasound with Doppler is essential to map these vessels.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1673}],"confusable_with":""},
  {"id":"sciatic-nerve-blocks-4","topic":"Sciatic nerve blocks","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"How are sciatic and femoral nerve blocks classified in terms of regional anesthetic complexity compared to penile blocks and epidurals?",
   "answer":"Sciatic and femoral nerve blocks are intermediate-complexity peripheral nerve blocks, more complex than simple peripheral blocks (penile, ilioinguinal) but less complex than major conduction blocks (spinal, epidural).",
   "rationale":"A complexity hierarchy guides training requirements, supervision levels, and consent; ultrasound guidance has expanded safety across all tiers.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1471}],"confusable_with":""},
  {"id":"sciatic-nerve-blocks-5","topic":"Sciatic nerve blocks","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"What technical adjunct makes sciatic blocks safe in pediatric patients?",
   "answer":"Ultrasound guidance enables safe performance of sciatic blocks (gluteal or popliteal approach) in children and infants, allowing visualization of nerve and adjacent structures.",
   "rationale":"Small anatomy in children makes landmark-based and nerve stimulator techniques less reliable; ultrasound provides direct nerve imaging to minimize risk.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1473}],"confusable_with":""}
]

# ── Topic 5: Separation from CPB - Weaning Strategy ─────────────────────────
kps += [
  {"id":"separation-cpb-weaning-1","topic":"Separation from CPB - Weaning Strategy","domain":"Cardiovascular & cardiac anesthesia (CABG, valvular, cardiopulmonary bypass, TEE basics, cardiac physiology, hemodynamic & vasoactive management, ICDs/pacemakers)","discipline":"anesthesia",
   "stem":"Before weaning from mechanical ventilation (after cardiac surgery), what pH threshold must be met?",
   "answer":"pH must be greater than 7.25 and adequate arterial O2 saturation on FiO2 <=0.4-0.5 before mechanical ventilation weaning is attempted.",
   "rationale":"Acidosis depresses myocardial contractility and increases ventilatory work; a pH >7.25 ensures sufficient respiratory muscle function and hemodynamic stability for a weaning trial.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2195}],"confusable_with":""},
  {"id":"separation-cpb-weaning-2","topic":"Separation from CPB - Weaning Strategy","domain":"Cardiovascular & cardiac anesthesia (CABG, valvular, cardiopulmonary bypass, TEE basics, cardiac physiology, hemodynamic & vasoactive management, ICDs/pacemakers)","discipline":"anesthesia",
   "stem":"What rapid shallow breathing index (RSBI) threshold predicts successful extubation versus likely failure?",
   "answer":"RSBI (RR/TV) greater than 105 breaths/min/L predicts extubation failure; values below this threshold are more likely to succeed.",
   "rationale":"RSBI integrates respiratory rate and tidal volume; a high ratio indicates rapid shallow breathing pattern consistent with respiratory muscle fatigue or insufficient reserve.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":770}],"confusable_with":"MIF (maximum inspiratory force; different measure of respiratory muscle strength)"},
  {"id":"separation-cpb-weaning-3","topic":"Separation from CPB - Weaning Strategy","domain":"Cardiovascular & cardiac anesthesia (CABG, valvular, cardiopulmonary bypass, TEE basics, cardiac physiology, hemodynamic & vasoactive management, ICDs/pacemakers)","discipline":"anesthesia",
   "stem":"What minimum inspiratory force (MIF) value indicates adequate respiratory muscle strength to sustain ventilation?",
   "answer":"MIF more negative than -20 cmH2O indicates some respiratory muscle strength; normal is -100 cmH2O; MIF less negative than -20 suggests insufficient strength.",
   "rationale":"MIF measures the negative pressure generated during maximal inspiratory effort against an occluded airway; values less negative than -20 cmH2O indicate inability to sustain adequate spontaneous ventilation.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":770}],"confusable_with":"PEEP (positive end-expiratory pressure; unrelated to inspiratory effort)"},
  {"id":"separation-cpb-weaning-4","topic":"Separation from CPB - Weaning Strategy","domain":"Cardiovascular & cardiac anesthesia (CABG, valvular, cardiopulmonary bypass, TEE basics, cardiac physiology, hemodynamic & vasoactive management, ICDs/pacemakers)","discipline":"anesthesia",
   "stem":"Prior to extubation after cardiac surgery, what tidal volume and vital capacity criteria must be met?",
   "answer":"Tidal volume >5 mL/kg and vital capacity >15 mL/kg are required; also SpO2 >90% on FiO2 <0.4, RR 6-30, and adequate neuromuscular reversal.",
   "rationale":"These ventilatory parameters confirm adequate respiratory muscle strength and lung compliance to sustain spontaneous ventilation without mechanical support.",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":70}],"confusable_with":""},
  {"id":"separation-cpb-weaning-5","topic":"Separation from CPB - Weaning Strategy","domain":"Cardiovascular & cardiac anesthesia (CABG, valvular, cardiopulmonary bypass, TEE basics, cardiac physiology, hemodynamic & vasoactive management, ICDs/pacemakers)","discipline":"anesthesia",
   "stem":"Dynamic hyperinflation (auto-PEEP) is a ventilator complication. How is it diagnosed?",
   "answer":"Auto-PEEP is detected by end-expiratory hold: auto-PEEP = end-expiratory pressure minus set PEEP; diagnosis confirmed by end-expiratory flow >0 due to incomplete alveolar emptying.",
   "rationale":"Incomplete exhalation allows air trapping and intrinsic PEEP to develop, increasing work of breathing and reducing weaning success; adjusting I:E ratio and RR resolves it.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":58}],"confusable_with":"High set PEEP (external, intentional; auto-PEEP is unintentional and additive)"}
]

# ── Topic 6: Sevoflurane clinical pharmacology ───────────────────────────────
kps += [
  {"id":"sevoflurane-pharmacology-1","topic":"Sevoflurane: clinical pharmacology","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"What minimum alveolar concentration (MAC) of a potent inhalation agent should be administered to minimize risk of intraoperative awareness?",
   "answer":"At least 0.5-0.7 MAC of the inhalation agent should be administered; a low anesthetic gas concentration alarm should be set.",
   "rationale":"Concentrations below 0.5 MAC may be insufficient to reliably prevent awareness; monitoring end-tidal agent concentration provides a continuous safety check.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":204}],"confusable_with":"MAC-awake (0.3-0.4 MAC; the concentration at which 50% of patients respond to command)"},
  {"id":"sevoflurane-pharmacology-2","topic":"Sevoflurane: clinical pharmacology","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"MAC-amnesia for inhaled anesthetics is thought to be what value relative to MAC?",
   "answer":"MAC-amnesia (preventing conscious recall in 50% of patients) is likely less than MAC-awake and considerably less than MAC-immobility.",
   "rationale":"Amnesia, loss of consciousness, and suppression of movement have different concentration requirements; amnesia requires the lowest drug concentration.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":114}],"confusable_with":"MAC-awake (approximately 0.3-0.4 MAC; end-point is response to verbal command, not recall)"},
  {"id":"sevoflurane-pharmacology-3","topic":"Sevoflurane: clinical pharmacology","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"Older adult patients display what key pharmacodynamic difference with inhaled anesthetics?",
   "answer":"MAC decreases with increasing age; older adults require lower concentrations of inhaled anesthetics for equivalent clinical effect.",
   "rationale":"Age-related reduction in neuronal density and changes in receptor function reduce anesthetic requirements; MAC decreases approximately 6% per decade after age 40.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1490}],"confusable_with":""},
  {"id":"sevoflurane-pharmacology-4","topic":"Sevoflurane: clinical pharmacology","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"During cardiopulmonary bypass, how should anesthetic gas concentration be monitored to prevent awareness?",
   "answer":"Monitor anesthetic gas concentration continuously from the bypass circuit; set an alarm for low gas concentration and maintain at least 0.5-0.7 MAC.",
   "rationale":"The CPB circuit dilutes inhaled agents; without monitoring the bypass gas output, patients may receive sub-anesthetic concentrations without the anesthesiologist being aware.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":204}],"confusable_with":""},
  {"id":"sevoflurane-pharmacology-5","topic":"Sevoflurane: clinical pharmacology","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"What induction agent provides the smoothest inhalation induction and is preferred for asthmatic patients?",
   "answer":"Sevoflurane provides the smoothest inhalation induction and is the preferred inhaled agent for asthmatic patients requiring inhalation induction.",
   "rationale":"Sevoflurane has low airway pungency and bronchodilating properties; it causes less airway reactivity and coughing than desflurane or isoflurane during induction.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":867}],"confusable_with":"Desflurane (pungent; causes cough, bronchospasm, and laryngospasm if used for induction)"}
]

# ── Topic 7: Specific block-surgery pairings ─────────────────────────────────
# Chunks are predominantly AKI content, not block-surgery pairing content
# Write 4 KPs from the available relevant block/decision chunks
kps += [
  {"id":"block-surgery-pairings-1","topic":"Specific block-surgery pairings and decision-making","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"A patient presents with AKI (oliguria, Cr 2.1 rising). How does acute kidney failure primarily affect anesthetic drug management?",
   "answer":"AKI causes retention of nitrogenous waste products (azotemia), impairs drug/metabolite excretion, alters volume of distribution, and may worsen coagulopathy; dose adjustments for renally cleared drugs are required.",
   "rationale":"Rapid deterioration in kidney function impairs excretion of drugs and metabolites that behave as toxins; altered drug handling requires careful dose selection.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1106}],"confusable_with":""},
  {"id":"block-surgery-pairings-2","topic":"Specific block-surgery pairings and decision-making","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"A patient with narrow complex SVT (stable) requires cardioversion. What drug is first-line?",
   "answer":"Stable narrow-complex SVT: adenosine first (paroxysmal SVT); amiodarone for stable SVT when adenosine fails; synchronized cardioversion for unstable patients.",
   "rationale":"Adenosine blocks AV node conduction terminating most re-entrant SVTs; amiodarone is used for refractory or rate-control situations; cardioversion is reserved for hemodynamic instability.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":2139}],"confusable_with":"Amiodarone IV bolus (150 mg over 10 min for VT or refractory SVT, not first-line stable SVT)"},
  {"id":"block-surgery-pairings-3","topic":"Specific block-surgery pairings and decision-making","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"AKI is defined as a broad clinical syndrome. What is the key defining characteristic that distinguishes it from other kidney conditions?",
   "answer":"AKI is defined by an abrupt decrease in kidney function (over hours to days) that includes but is not limited to acute renal failure.",
   "rationale":"The KDIGO definition encompasses a spectrum from mild acute kidney function decline to complete acute renal failure, requiring standardized criteria for early recognition.",
   "bloom":"recall","source":[{"book":"Society Guideline: Guideline   KDIGO 2012 AKI","page":22}],"confusable_with":"CKD (gradual, >3 months); AKF (older term for severe end of AKI spectrum)"},
  {"id":"block-surgery-pairings-4","topic":"Specific block-surgery pairings and decision-making","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"What electrolyte disturbances does AKI commonly produce beyond azotemia?",
   "answer":"AKI causes accumulation of water, sodium, and metabolic products; common electrolyte disturbances include hyperkalemia, hyperphosphatemia, metabolic acidosis, and hyponatremia.",
   "rationale":"Failed renal excretion of potassium and hydrogen ions causes life-threatening hyperkalemia and acidosis; these must be identified and managed perioperatively.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Acute kidney injury","page":2}],"confusable_with":""}
]

# ── Topic 8: Spinal (intrathecal) local anesthetics ──────────────────────────
kps += [
  {"id":"spinal-intrathecal-la-1","topic":"Spinal (intrathecal) local anesthetics","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"A hyperbaric solution of which two local anesthetics is typically used for spinal anesthesia for cesarean delivery, and how do they differ in duration?",
   "answer":"Hyperbaric lidocaine (50-60 mg) or bupivacaine (10-15 mg); bupivacaine is chosen if surgery will likely exceed 45 minutes due to longer duration.",
   "rationale":"Hyperbaric solutions sink in CSF allowing positional control; bupivacaine provides 90-120 min anesthesia versus lidocaine's 45-90 min, matching different surgical time requirements.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1405}],"confusable_with":"Isobaric bupivacaine (less predictable spread; used for specific positional requirements)"},
  {"id":"spinal-intrathecal-la-2","topic":"Spinal (intrathecal) local anesthetics","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"What two intrathecal opioid adjuncts are commonly added to local anesthetic for spinal anesthesia, and what do they provide?",
   "answer":"Fentanyl 12.5-25 mcg or sufentanil 5-7.5 mcg significantly potentiate intrathecal local anesthetic block; they enhance analgesia quality and duration.",
   "rationale":"Intrathecal opioids act on spinal cord dorsal horn opioid receptors, providing synergistic analgesia with local anesthetics while reducing required LA dose.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1402}],"confusable_with":"Epidural opioids (require higher doses; different pharmacokinetic profile)"},
  {"id":"spinal-intrathecal-la-3","topic":"Spinal (intrathecal) local anesthetics","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"When does epidural catheter tip migration into the intrathecal space occur silently, and how does it present?",
   "answer":"Intrathecal catheter migration can occur without blood or CSF on aspiration; it presents as slowly progressive motor blockade of the lower extremities and a rising sensory level.",
   "rationale":"An epidural catheter eroding through the dura may not yield CSF on aspiration due to catheter tip geometry; clinical signs (progressive motor block, rising sensory level) are the warning.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1598}],"confusable_with":"Total spinal (more abrupt onset if large volume injected intrathecally)"},
  {"id":"spinal-intrathecal-la-4","topic":"Spinal (intrathecal) local anesthetics","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"How are amide vs ester local anesthetics distinguished metabolically, and which type includes lidocaine?",
   "answer":"Ester local anesthetics (one i in -caine: procaine, tetracaine) are hydrolyzed by plasma pseudocholinesterase and RBC esterase; amide LAs (two i's in name: lidocaine, bupivacaine) are metabolized by liver.",
   "rationale":"The i-mnemonic (amIde has 2 I's) helps distinguish classes; esters generate PABA metabolites that can cause allergic reactions; amides are safer in most allergy contexts.",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":82}],"confusable_with":""},
  {"id":"spinal-intrathecal-la-5","topic":"Spinal (intrathecal) local anesthetics","domain":"Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)","discipline":"anesthesia",
   "stem":"Epinephrine is sometimes added to spinal local anesthetic solutions. Through what mechanisms does it prolong blockade?",
   "answer":"Epinephrine prolongs spinal block via alpha-1 adrenergic vasoconstriction (reducing vascular uptake of LA) and potentially via direct alpha-2 agonist analgesia at spinal cord receptors.",
   "rationale":"Reduced systemic absorption maintains higher CSF LA concentration for longer; the alpha-2 mechanism contributes additional intrinsic analgesia.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":326}],"confusable_with":"Phenylephrine added to epidural (used to treat hypotension, not prolong block)"}
]

# ── Topic 9: Spinal Cord Injury Acute Anesthetic Considerations ──────────────
kps += [
  {"id":"spinal-cord-injury-anesthesia-1","topic":"Spinal Cord Injury: Acute Anesthetic Considerations","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"A patient with acute SCI below T6 develops sudden hypertension, bradycardia, and diaphoresis during bladder catheterization. What syndrome is this?",
   "answer":"Autonomic dysreflexia (hyperreflexia): a life-threatening exaggerated sympathetic response to noxious stimulation below the level of injury, occurring in SCI at or above T6.",
   "rationale":"Loss of supraspinal inhibition of sympathetic outflow allows uninhibited reflex vasoconstriction below the lesion; the resulting hypertension can cause stroke, seizure, or cardiac arrest.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1012}],"confusable_with":"Neurogenic shock (hypotension + bradycardia from acute SCI; opposite hemodynamics)"},
  {"id":"spinal-cord-injury-anesthesia-2","topic":"Spinal Cord Injury: Acute Anesthetic Considerations","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"In the acute phase of spinal cord injury (neurogenic shock), what triad characterizes the hemodynamic presentation?",
   "answer":"Neurogenic shock: hypotension + bradycardia + peripheral vasodilation (from loss of sympathetic tone below the injury level); treat with isotonic fluids, vasopressors, and inotropes; maintain MAP >=85 mmHg.",
   "rationale":"Complete sympathectomy below the injury level removes vasomotor tone and cardiac chronotropy; fluids alone are insufficient and vasopressors are required.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":810}],"confusable_with":"Hypovolemic shock (tachycardia + hypotension; absent in neurogenic shock)"},
  {"id":"spinal-cord-injury-anesthesia-3","topic":"Spinal Cord Injury: Acute Anesthetic Considerations","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"What MAP target is recommended for patients with acute SCI to optimize spinal cord perfusion?",
   "answer":"MAP should be maintained at >=85 mmHg in acute SCI to support spinal cord perfusion pressure and limit secondary injury.",
   "rationale":"Secondary ischemic injury from hypoperfusion worsens neurological outcomes; aggressive MAP targets reduce ischemia in the penumbra around the injury.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":810}],"confusable_with":"TBI MAP target (also >=65-70 mmHg minimum, but SCI-specific guidelines recommend >=85)"},
  {"id":"spinal-cord-injury-anesthesia-4","topic":"Spinal Cord Injury: Acute Anesthetic Considerations","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"A patient with Guillain-Barre syndrome (GBS) presents for urgent surgery. What anesthetic concern about autonomic function is present?",
   "answer":"GBS causes autonomic instability with exaggerated responses to stimulation (hypertension, tachycardia) or sympatholytic drugs (profound hypotension); careful titration of all vasoactive drugs is required.",
   "rationale":"GBS involves acute demyelinating polyneuropathy with variable autonomic involvement; the denervated cardiovascular system shows exaggerated and unpredictable hemodynamic responses.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1010}],"confusable_with":"Myasthenia gravis (NMJ disorder without autonomic instability)"},
  {"id":"spinal-cord-injury-anesthesia-5","topic":"Spinal Cord Injury: Acute Anesthetic Considerations","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"Why must succinylcholine be avoided in patients with SCI beyond the acute phase?",
   "answer":"SCI causes upregulation of extrajunctional acetylcholine receptors; succinylcholine causes exaggerated, potentially lethal hyperkalemia in these patients starting 24-72 h post-injury.",
   "rationale":"Denervation supersensitivity leads to proliferation of fetal-type acetylcholine receptors throughout the muscle; depolarization by succinylcholine causes massive K+ efflux.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1012}],"confusable_with":"Burns, immobilization (same mechanism of extrajunctional receptor upregulation and hyperkalemia)"}
]
kps += [{"_type":"illness_script","topic":"Spinal Cord Injury: Acute Anesthetic Considerations","discipline":"anesthesia",
  "enabling_conditions":"Trauma (MVA, falls, assault); most common mechanism is fracture-dislocation",
  "pathophysiology":"Primary mechanical injury to cord followed by secondary ischemia, edema, inflammation; loss of descending sympathetic control causes neurogenic shock; denervation causes receptor upregulation",
  "time_course":"Acute: neurogenic shock + flaccid paralysis; subacute/chronic: spastic paralysis, autonomic dysreflexia risk starts 2-3 weeks post-injury",
  "key_features":"Neurogenic shock (hypotension + bradycardia), level-dependent deficits, succinylcholine contraindicated after 24-72h, autonomic dysreflexia at/above T6",
  "consequence_if_missed":"Failure to recognize autonomic dysreflexia triggers can cause hypertensive emergency, stroke; succinylcholine use causes cardiac arrest from hyperkalemia"}]

# ── Topic 10: Spinal and epidural complications ───────────────────────────────
kps += [
  {"id":"spinal-epidural-complications-1","topic":"Spinal and epidural complications: recognition and management","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"What is the estimated incidence of epidural hematoma after epidural block, and what anticoagulant significantly increased this risk when first introduced in the US?",
   "answer":"Epidural hematoma incidence is approximately 1 in 150,000 for epidural block and 1 in 220,000 for spinal; low-molecular-weight heparin (LMWH) introduced in Europe without significant problems but caused cases when introduced to the US.",
   "rationale":"LMWH's introduction in the US at higher doses and without adequate washout intervals revealed the spinal hematoma risk, leading to ASRA guidelines on timing.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":751}],"confusable_with":"Spinal cord compression from other causes (disc herniation, abscess)"},
  {"id":"spinal-epidural-complications-2","topic":"Spinal and epidural complications: recognition and management","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"Post-dural puncture headache (PDPH) typically begins within how many days, and what is the natural history?",
   "answer":"PDPH begins within 3 days of the procedure (approximately two-thirds within 48 hours); spontaneous resolution occurs within 7 days in most patients, but a minority have symptoms at 6 months.",
   "rationale":"CSF leak from the dural puncture reduces intracranial CSF pressure; compensatory meningeal vessel dilation causes the positional headache; most leaks seal spontaneously.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":336}],"confusable_with":"Meningitis (non-positional, fever; PDPH is positional and afebrile)"},
  {"id":"spinal-epidural-complications-3","topic":"Spinal and epidural complications: recognition and management","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"Intrathecal opioids cause pruritus. What drugs can be used for treatment?",
   "answer":"Naloxone, naltrexone, or the partial agonist/antagonist nalbuphine can treat intrathecal opioid-induced pruritus; reducing the opioid dose reduces likelihood.",
   "rationale":"Neuraxial opioid pruritus is mediated by spinal opioid receptor activation, not histamine release; mu-receptor antagonism or mixed agonist-antagonism relieves it.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":338}],"confusable_with":"Histamine-mediated pruritus (treated with antihistamines; neuraxial opioid pruritus does not respond to diphenhydramine)"},
  {"id":"spinal-epidural-complications-4","topic":"Spinal and epidural complications: recognition and management","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"Transient neurological symptoms (TNS) after spinal anesthesia are characterized by what clinical presentation and associated drug?",
   "answer":"TNS presents as back pain radiating to the legs starting after recovery from spinal anesthesia; most strongly associated with intrathecal lidocaine (especially with lithotomy position).",
   "rationale":"TNS (also called transient radicular irritation) likely results from direct neurotoxicity of concentrated lidocaine pooling in dependent sacral nerve roots; no permanent neurologic deficit.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1603}],"confusable_with":"Cauda equina syndrome (permanent neurologic deficit; associated with concentrated hyperbaric lidocaine via continuous spinal)"},
  {"id":"spinal-epidural-complications-5","topic":"Spinal and epidural complications: recognition and management","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"The consequence of untreated spinal cord compression from any source is what, and how quickly does it develop?",
   "answer":"Untreated spinal cord compression leads to irreversible neurologic deficit including paralysis, gait impairment, sensory loss, and bladder/bowel dysfunction; permanent deficits can develop rapidly.",
   "rationale":"Spinal cord ischemia from compression causes irreversible infarction if not decompressed emergently; time to treatment is the critical determinant of outcome.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Spinal Cord Compression  Non Traumatic","page":11}],"confusable_with":""}
]
kps += [{"_type":"confusable_pair","topic_a":"Transient Neurological Symptoms (TNS)","topic_b":"Cauda Equina Syndrome","discriminator":"TNS: back/leg pain after spinal recovery, resolves completely within days, no motor deficit; Cauda Equina: permanent bladder/bowel/sexual dysfunction + motor weakness, requires emergency decompression"}]

print('Topics 0-10 done:', len(kps))
with open('data/kp_part26_batch1.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print('Batch 1 written')
