import json

kps = []

# TOPIC 14: Hemodynamic Monitoring: Invasive
kps += [
  {"id":"hdinvasive-1","topic":"Hemodynamic Monitoring: Invasive","domain":"Anesthesia monitoring & equipment (anesthesia machine & circuits, ventilators, capnography & gas analysis, pulse oximetry, depth of anesthesia, neuromuscular monitoring, alarms & safety checks)","discipline":"anesthesia",
   "stem":"What is the safety rule for the tip position of a central venous pressure catheter?",
   "answer":"CVP catheter tip must not be allowed to migrate into the heart chambers",
   "rationale":"An intracardiac catheter tip causes arrhythmias, perforation, and tamponade; optimal position is at the SVC-RA junction confirmed by CXR.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":132}],"confusable_with":"Catheter tip in subclavian vein being adequate for CVP measurement"},
  {"id":"hdinvasive-2","topic":"Hemodynamic Monitoring: Invasive","domain":"Anesthesia monitoring & equipment (anesthesia machine & circuits, ventilators, capnography & gas analysis, pulse oximetry, depth of anesthesia, neuromuscular monitoring, alarms & safety checks)","discipline":"anesthesia",
   "stem":"What clinical finding on ultrasonography indicates a severely hypovolemic state secondary to acute blood loss?",
   "answer":"Nearly collapsed inferior vena cava on ultrasonography indicates severe hypovolemia from acute blood loss",
   "rationale":"Acute hemorrhage reduces intravascular volume faster than compensatory extravascular fluid shifts can restore it, causing IVC collapse.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1946}],"confusable_with":"Respiratory variation in IVC diameter only indicating fluid responsiveness (different measure)"},
  {"id":"hdinvasive-3","topic":"Hemodynamic Monitoring: Invasive","domain":"Anesthesia monitoring & equipment (anesthesia machine & circuits, ventilators, capnography & gas analysis, pulse oximetry, depth of anesthesia, neuromuscular monitoring, alarms & safety checks)","discipline":"anesthesia",
   "stem":"In patients with severe hypertension, pulmonary edema, or refractory oliguria, what monitoring is indicated?",
   "answer":"Invasive arterial and central venous monitoring are indicated in severe hypertension, pulmonary edema, or refractory oliguria",
   "rationale":"These conditions require beat-to-beat blood pressure measurement and central venous access for drug infusion and CVP monitoring.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1422}],"confusable_with":"Non-invasive BP cuff adequate for all severe hypertension cases"},
  {"id":"hdinvasive-4","topic":"Hemodynamic Monitoring: Invasive","domain":"Anesthesia monitoring & equipment (anesthesia machine & circuits, ventilators, capnography & gas analysis, pulse oximetry, depth of anesthesia, neuromuscular monitoring, alarms & safety checks)","discipline":"anesthesia",
   "stem":"In major blood loss and hemodynamic instability in the trauma patient, what specific challenge does hypovolemia create?",
   "answer":"Major blood loss and hemodynamic instability create a dangerous situation for both the conscious trauma patient and a challenge for invasive monitoring placement",
   "rationale":"Coagulopathy, vasoconstriction, and patient movement make arterial and central venous line placement technically difficult under emergency conditions.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1334}],"confusable_with":"Waiting for monitoring before resuscitation"},
  {"id":"hdinvasive-5","topic":"Hemodynamic Monitoring: Invasive","domain":"Anesthesia monitoring & equipment (anesthesia machine & circuits, ventilators, capnography & gas analysis, pulse oximetry, depth of anesthesia, neuromuscular monitoring, alarms & safety checks)","discipline":"anesthesia",
   "stem":"What does the PA catheter enable beyond PCWP measurement that guides hemodynamic therapy?",
   "answer":"PA catheter measures cardiac output (CO) and mixed venous oxygen saturation in addition to filling pressures",
   "rationale":"CO and SvO2 provide information about oxygen delivery and consumption that pressure measurements alone cannot supply.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":157}],"confusable_with":"PCWP alone being sufficient for all hemodynamic decision-making"},
]

# TOPIC 15: Hemodynamic Monitoring: Noninvasive and Minimally Invasive
kps += [
  {"id":"hdnoninv-1","topic":"Hemodynamic Monitoring: Noninvasive and Minimally Invasive","domain":"Anesthesia monitoring & equipment (anesthesia machine & circuits, ventilators, capnography & gas analysis, pulse oximetry, depth of anesthesia, neuromuscular monitoring, alarms & safety checks)","discipline":"anesthesia",
   "stem":"What goal-directed hemodynamic monitoring devices can guide fluid replacement using arterial pulse wave contour analysis?",
   "answer":"Arterial pulse wave contour analysis devices (LiDCO, PiCCO, FloTrac) and echocardiography guide fluid replacement non-invasively or minimally invasively",
   "rationale":"These devices derive CO and fluid responsiveness parameters from the arterial waveform without requiring PA catheter insertion.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1422}],"confusable_with":"PA catheter being the only valid CO monitoring tool"},
  {"id":"hdnoninv-2","topic":"Hemodynamic Monitoring: Noninvasive and Minimally Invasive","domain":"Anesthesia monitoring & equipment (anesthesia machine & circuits, ventilators, capnography & gas analysis, pulse oximetry, depth of anesthesia, neuromuscular monitoring, alarms & safety checks)","discipline":"anesthesia",
   "stem":"What non-invasive cardiac function monitor is increasingly used alongside or instead of PAC in cardiac ICU?",
   "answer":"Minimally invasive cardiac output monitoring (pulse-contour analysis, transpulmonary thermodilution) in cardiac surgery ICU",
   "rationale":"Less invasive devices reduce procedural risk while providing continuous CO trends useful for hemodynamic management post-cardiac surgery.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":186}],"confusable_with":"CVP alone as adequate ICU cardiac monitoring"},
  {"id":"hdnoninv-3","topic":"Hemodynamic Monitoring: Noninvasive and Minimally Invasive","domain":"Anesthesia monitoring & equipment (anesthesia machine & circuits, ventilators, capnography & gas analysis, pulse oximetry, depth of anesthesia, neuromuscular monitoring, alarms & safety checks)","discipline":"anesthesia",
   "stem":"What echocardiographic finding indicates the patient is unlikely to be fluid responsive?",
   "answer":"Plethoric non-collapsing IVC and right heart distension on echocardiography indicate fluid overload not fluid responsiveness",
   "rationale":"A distended non-collapsing IVC reflects elevated right atrial pressure; further fluid administration would not increase preload.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1946}],"confusable_with":"All tachycardic ICU patients being fluid-responsive"},
  {"id":"hdnoninv-4","topic":"Hemodynamic Monitoring: Noninvasive and Minimally Invasive","domain":"Anesthesia monitoring & equipment (anesthesia machine & circuits, ventilators, capnography & gas analysis, pulse oximetry, depth of anesthesia, neuromuscular monitoring, alarms & safety checks)","discipline":"anesthesia",
   "stem":"In a patient with moderate mitral stenosis at high risk of emboli (age over 40, large atrium, chronic AF), what perioperative management is indicated?",
   "answer":"Anticoagulation for high-risk mitral stenosis patients (age >40, large atrium, chronic AF) plus careful hemodynamic management",
   "rationale":"Left atrial enlargement and AF create high thromboembolic risk; anticoagulation reduces stroke risk perioperatively.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":666}],"confusable_with":"Anticoagulation only for mechanical valve patients"},
]

# TOPIC 16: Hemodynamic management during thoracic surgery
kps += [
  {"id":"thorachd-1","topic":"Hemodynamic management during thoracic surgery","domain":"Thoracic anesthesia (one-lung ventilation, thoracic epidural, hypoxia during OLV, pneumonectomy/lobectomy, mediastinal mass, HPV)","discipline":"anesthesia",
   "stem":"What positioning protection is required for the brachial plexus during lateral decubitus positioning for thoracic surgery?",
   "answer":"Axillary roll placed beneath dependent upper chest to protect the brachial plexus and avoid compression injury",
   "rationale":"Without an axillary roll, pressure on the axilla occludes the axillary artery and stretches the brachial plexus, risking nerve injury.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":911}],"confusable_with":"Shoulder roll (placed under shoulder, different structure)"},
  {"id":"thorachd-2","topic":"Hemodynamic management during thoracic surgery","domain":"Thoracic anesthesia (one-lung ventilation, thoracic epidural, hypoxia during OLV, pneumonectomy/lobectomy, mediastinal mass, HPV)","discipline":"anesthesia",
   "stem":"What monitoring and vascular access are recommended for thoracic surgery where major hemodynamic instability is possible?",
   "answer":"Central venous catheter allowing vasoactive agents; arterial line for beat-to-beat monitoring in major thoracic cases",
   "rationale":"Intrathoracic surgical manipulation can cause sudden hypotension from cardiac compression or major vessel injury requiring immediate vasoactive response.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":516}],"confusable_with":"Peripheral IV only for minor thoracic procedures"},
  {"id":"thorachd-3","topic":"Hemodynamic management during thoracic surgery","domain":"Thoracic anesthesia (one-lung ventilation, thoracic epidural, hypoxia during OLV, pneumonectomy/lobectomy, mediastinal mass, HPV)","discipline":"anesthesia",
   "stem":"During thoracic surgery, patients with severe pulmonary hypertension are at risk for what hemodynamic catastrophe with positive-pressure ventilation?",
   "answer":"Positive-pressure ventilation reduces venous return and worsens hemodynamic instability in severe pulmonary hypertension, risking acute RV failure",
   "rationale":"Elevated pulmonary vascular resistance leaves RV function marginal; added preload reduction from PPV can precipitate RV failure.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":692}],"confusable_with":"PPV being uniformly beneficial for oxygenation in all thoracic cases"},
  {"id":"thorachd-4","topic":"Hemodynamic management during thoracic surgery","domain":"Thoracic anesthesia (one-lung ventilation, thoracic epidural, hypoxia during OLV, pneumonectomy/lobectomy, mediastinal mass, HPV)","discipline":"anesthesia",
   "stem":"What balanced crystalloid is preferred over normal saline for trauma resuscitation based on clinical trials?",
   "answer":"Plasma-Lyte or similar balanced crystalloids are preferred over normal saline in trauma resuscitation based on trial data",
   "rationale":"Balanced crystalloids have a chloride concentration near physiological levels, avoiding hyperchloremic metabolic acidosis seen with large-volume NS.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":467}],"confusable_with":"Normal saline being equivalent to balanced crystalloids in all trauma situations"},
]

print(f"Batch E: {len(kps)} entries")
with open('C:/Users/Dean/anesthesia_attending/data/kp_batch6e_out.json','w',encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("OK")
