import json

kps = []

def kp(id_, topic, domain, discipline, stem, answer, rationale, bloom, book, page, confusable=""):
    return {"id": id_, "topic": topic, "domain": domain, "discipline": discipline,
            "stem": stem, "answer": answer, "rationale": rationale,
            "bloom": bloom, "source": [{"book": book, "page": page}],
            "confusable_with": confusable}

def script(topic, discipline, ec, patho, tc, kf, consequence):
    return {"_type": "illness_script", "topic": topic, "discipline": discipline,
            "enabling_conditions": ec, "pathophysiology": patho,
            "time_course": tc, "key_features": kf, "consequence_if_missed": consequence}

def pair(a, b, discriminator):
    return {"_type": "confusable_pair", "topic_a": a, "topic_b": b, "discriminator": discriminator}

with open('data/_kp_retrieval_full.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
sliced = data[33:66]
D = lambda idx: sliced[idx]["domain"]
DI = lambda idx: sliced[idx]["discipline"]
T = lambda idx: sliced[idx]["topic"]

# ── 22: Ischemic Stroke: Pathophysiology & Classification ─────────────
top = T(22); dom = D(22); dis = DI(22)
kps += [
    kp("stroke-patho-1", top, dom, dis,
       "What are the major etiologic categories of ischemic stroke?",
       "Large artery atherosclerosis, cardioembolic (e.g., AF), small vessel occlusion (lacunar), cryptogenic, other determined causes",
       "Etiology determines prognosis, outcomes, and secondary prevention strategy.",
       "recall", "StatPearls", 3),
    kp("stroke-patho-2", top, dom, dis,
       "In AF, what is the recommended approach to stroke risk reduction therapy selection?",
       "Guided by stroke risk (CHA2DS2-VASc), bleeding risk, and patient preferences; DOACs preferred in non-valvular AF",
       "Higher CHA2DS2-VASc score predicts greater annual stroke risk; anticoagulation benefit outweighs bleeding risk above threshold scores.",
       "apply", "Society Guideline: Guideline   ACC AHA 2023 Atrial", 32),
    kp("stroke-patho-3", top, dom, dis,
       "What right-to-left cardiac shunt can allow venous emboli to enter the cerebral arterial system?",
       "Patent foramen ovale (PFO): emboli arising from venous circulation cross into the left heart via the PFO to cause paradoxical embolism",
       "PFO is present in ~25% of adults; cryptogenic stroke in young patients warrants bubble echocardiography to assess for PFO.",
       "recall", "StatPearls", 3),
    kp("stroke-patho-4", top, dom, dis,
       "What is the mechanism of fever-related neuronal damage in the periischemic period?",
       "Fever triggers inflammatory cascades and biochemical reactions following ischemia-reperfusion injury, worsening neuronal damage and outcomes",
       "Hyperthermia increases metabolic demand and excitotoxic neurotransmitter release in ischemic penumbra, accelerating infarct growth.",
       "analyze", "Marino ICU Book", 667),
]

# ── 23: Ischemic Stroke: Secondary Prevention ──────────────────────
top = T(23); dom = D(23); dis = DI(23)
kps += [
    kp("stroke-secondary-1", top, dom, dis,
       "What pharmacologic class is the primary anticoagulation choice for stroke prevention in patients with AF and prosthetic heart valves?",
       "Vitamin K antagonists (VKAs, warfarin) are required for prosthetic mechanical heart valves; DOACs are inferior in this setting",
       "Prosthetic mechanical valves generate higher thrombogenicity; DOACs have not shown non-inferiority to warfarin for mechanical valves.",
       "recall", "Society Guideline: Guideline   ACC AHA 2023 Atrial", 49),
    kp("stroke-secondary-2", top, dom, dis,
       "For patients with prior ischemic stroke, what antiplatelet or anticoagulant therapy is continued perioperatively?",
       "Patients with prior ischemic stroke may be receiving antiplatelet or anticoagulant therapy for secondary prevention; this should be maintained through the perioperative period unless bleeding risk prohibits it",
       "Discontinuing secondary prevention therapy risks thrombotic stroke recurrence, especially in the perioperative hypercoagulable state.",
       "apply", "Miller/Baby Miller", 222),
    kp("stroke-secondary-3", top, dom, dis,
       "What statin strategy is recommended for secondary stroke prevention in patients with atherosclerotic disease?",
       "Intensive LDL-lowering with statin therapy; evidence supports safety of intensive LDL lowering with low cost (fire-and-forget strategy)",
       "Statins reduce plaque instability, endothelial dysfunction, and stroke risk; intensive therapy provides greater LDL reduction.",
       "apply", "Society Guideline: Guideline   KDIGO 2024 CKD", 121),
    kp("stroke-secondary-4", top, dom, dis,
       "What is the outcome prognosis for patients who receive IV tPA for ischemic stroke vs those who do not?",
       "Prognosis generally favorable with tPA; more guarded for those who do not receive thrombolytic therapy",
       "tPA restores perfusion to the penumbra before irreversible infarction; delayed treatment increases disability.",
       "recall", "StatPearls", 19),
]

# ── 24: Large-vessel vasculitis: Giant Cell Arteritis ──────────────
top = T(24); dom = D(24); dis = DI(24)
kps += [
    kp("gca-1", top, dom, dis,
       "What are the cardinal features prompting suspicion of giant cell arteritis?",
       "Age >50 with new/altered headaches, jaw claudication, fever, visual disturbances, or vascular abnormalities",
       "GCA affects medium-to-large arteries in elderly patients; cranial ischemia causes jaw claudication and vision loss from ophthalmic artery involvement.",
       "recall", "StatPearls: StatPearls   Large vessel vasculitis  ", 1),
    kp("gca-2", top, dom, dis,
       "GCA predominantly affects which age group and which vessel sizes?",
       "Individuals older than 50 years; affects large- and medium-sized arteries",
       "Chronic granulomatous inflammation affects the aorta and its branches; temporal artery is the classically involved vessel.",
       "recall", "StatPearls: StatPearls   Large vessel vasculitis  ", 2),
    kp("gca-3", top, dom, dis,
       "What is the initial treatment for GCA with evidence of cranial ischemia (vision threat)?",
       "IV methylprednisolone pulse (high-dose IV steroids for 3 days); if unavailable, oral prednisone 1 mg/kg/day",
       "Prompt high-dose glucocorticoids suppress granulomatous inflammation and prevent irreversible visual loss.",
       "apply", "StatPearls: StatPearls   Large vessel vasculitis  ", 10),
    kp("gca-4", top, dom, dis,
       "How is GCA classified among the vasculitides?",
       "GCA is a large-vessel vasculitis; classified by size and type of blood vessel involved",
       "Large-vessel vasculitides include GCA and Takayasu; medium-vessel includes PAN and Kawasaki; small-vessel includes ANCA-associated vasculitis.",
       "recall", "MGH Housestaff Manual", 176),
    kp("gca-5", top, dom, dis,
       "What associated rheumatologic condition occurs in ~50% of GCA patients and presents with shoulder/hip girdle stiffness?",
       "Polymyalgia rheumatica (PMR) occurs in ~50% of GCA patients; shoulder and hip girdle pain and stiffness without weakness",
       "PMR and GCA share the same granulomatous inflammatory mechanism in elderly patients; PMR can precede, accompany, or follow GCA.",
       "recall", "StatPearls: StatPearls   Large vessel vasculitis  ", 2, "Polymyalgia rheumatica"),
]
kps.append(script(top, dis,
    "Age >50, female sex, Northern European ancestry, prior PMR",
    "Granulomatous transmural inflammation of medium-to-large arteries; intimal hyperplasia causes luminal stenosis and ischemia",
    "Weeks to months of headache, jaw claudication, scalp tenderness; vision loss can be sudden and permanent",
    "New headache, tender temporal artery, jaw claudication, elevated ESR/CRP, visual symptoms; temporal artery biopsy confirms",
    "Untreated vision loss (anterior ischemic optic neuropathy) is permanent; aortic aneurysm in late disease"))
kps.append(pair("Giant Cell Arteritis", "Polymyalgia Rheumatica",
    "GCA: cranial ischemia symptoms (headache, jaw claudication, vision loss), temporal artery tenderness; PMR: proximal girdle pain/stiffness, no cranial ischemia"))

# ── 25: Lung-Protective Ventilation & ARDS ──────────────────────────
top = T(25); dom = D(25); dis = DI(25)
kps += [
    kp("ards-lpv-1", top, dom, dis,
       "What tidal volume strategy defines lung-protective (ARDSnet) ventilation?",
       "Tidal volume 6 mL/kg ideal body weight (low-stretch ventilation) to prevent volutrauma and barotrauma",
       "High tidal volumes overdistend alveoli and cause ventilator-induced lung injury (VILI); 6 mL/kg reduces cyclic stretch.",
       "recall", "Miller/Baby Miller", 766),
    kp("ards-lpv-2", top, dom, dis,
       "What pulmonary complication results from prolonged exposure to high FiO2 in mechanically ventilated patients?",
       "Oxygen toxicity: lung damage that is dependent on both partial pressure and duration of hyperoxia",
       "Reactive oxygen species generated at high FiO2 cause alveolar epithelial and endothelial damage, worsening the ARDS injury.",
       "apply", "Morgan & Mikhail", 2176),
    kp("ards-lpv-3", top, dom, dis,
       "What pathophysiology underlies pulmonary venous hypertension causing pulmonary edema?",
       "Left ventricular failure or mitral valve disease raises pulmonary venous pressure, increasing pulmonary capillary pressure and driving fluid into alveoli",
       "Starling forces: elevated Pc' drives filtration exceeding lymphatic drainage; hydrostatic (cardiogenic) pulmonary edema results.",
       "analyze", "Morgan & Mikhail", 2130),
    kp("ards-lpv-4", top, dom, dis,
       "What FEV1 threshold is a general extubation criterion for patients with restrictive pulmonary disease or post-thoracotomy?",
       "FEV1 >1 L is a general minimum criterion associated with adequate reserve for extubation; absence of significant hypercapnia/acidosis also required",
       "Insufficient FEV1 means the patient cannot generate adequate expiratory flow to clear secretions and resist airway closure.",
       "apply", "Morgan & Mikhail", 874),
    kp("ards-lpv-5", top, dom, dis,
       "What is the goal of formal ARDS management guidelines regarding ventilator settings beyond tidal volume?",
       "Lung-protective ventilation: low TV (6 mL/kg IBW), limit plateau pressure, apply PEEP to maintain alveolar recruitment, minimize FiO2",
       "Combining low TV with adequate PEEP prevents both overdistension and cyclic atelectrauma (alveolar opening/closing).",
       "apply", "Society Guideline", 37),
]

print(f"Batch5 items: {len(kps)}")
with open('data/_kp_batch5.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("OK")
