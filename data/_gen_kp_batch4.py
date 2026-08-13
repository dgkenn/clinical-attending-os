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

# ── 17: Inotropes ────────────────────────────────────────────────
top = T(17); dom = D(17); dis = DI(17)
kps += [
    kp("inotropes-1", top, dom, dis,
       "What intracellular signaling cascade do dopamine, dobutamine, and norepinephrine share to increase cardiac contractility?",
       "Beta-1 adrenergic receptor -> G protein Gas -> adenylyl cyclase -> ATP to cAMP -> PKA phosphorylation of myocardial proteins",
       "cAMP-dependent PKA phosphorylates L-type Ca2+ channels and troponin I, increasing cytosolic Ca2+ and myofilament sensitivity.",
       "recall", "Morgan & Mikhail", 570),
    kp("inotropes-2", top, dom, dis,
       "How does dobutamine differ from dopamine regarding filling pressures and blood pressure effects?",
       "Dobutamine does not increase filling pressures and may cause less tachycardia than dopamine; however, CO often increases without significant BP change",
       "Dobutamine has predominantly beta-1/beta-2 activity with weak alpha; dopamine also activates alpha receptors, increasing SVR and BP.",
       "analyze", "Morgan & Mikhail", 752),
    kp("inotropes-3", top, dom, dis,
       "When drug therapies fail in post-CPB cardiogenic shock, what mechanical support device may be initiated?",
       "Intra-aortic balloon pump (IABP) counterpulsation; efficacy depends on proper timing of balloon inflation and deflation",
       "IABP inflates in diastole (augments coronary perfusion) and deflates before systole (reduces afterload), improving CO in refractory failure.",
       "apply", "Morgan & Mikhail", 751),
    kp("inotropes-4", top, dom, dis,
       "What EF threshold and NYHA class define intractable heart failure requiring mechanical circulatory support?",
       "EF <20% with NYHA class IV (heart failure class D) defines intractable heart failure",
       "At this severity, cardiac output cannot sustain end-organ perfusion and pharmacologic escalation is insufficient.",
       "recall", "Morgan & Mikhail", 765),
    kp("inotropes-5", top, dom, dis,
       "What is the mechanism by which dopamine increases BP at medium-to-high doses compared with low doses?",
       "At high doses dopamine activates alpha-1 receptors, increasing SVR; at low doses it acts primarily on dopaminergic (D1) receptors causing renal/splanchnic vasodilation",
       "Dose-dependent receptor selectivity: low = D1; medium = beta-1; high = alpha-1 dominates, raising SVR and BP.",
       "recall", "Morgan & Mikhail", 752),
]

# ── 18: Intra-Abdominal Infections (chunks mostly off-topic) ─────────
top = T(18); dom = D(18); dis = DI(18)
kps += [
    kp("intra-abdominal-inf-1", top, dom, dis,
       "What AmpC beta-lactamase mechanism renders organisms resistant to third-generation cephalosporins?",
       "AmpC beta-lactamase (cephalosporinase) inactivates 3rd-gen cephalosporins and pip-tazo; can be constitutive or inducible by beta-lactam exposure",
       "Inducible AmpC is triggered by cephalosporin-induced accumulation of cell wall fragments that de-repress the AmpC gene.",
       "recall", "MGH Housestaff Manual", 115),
    kp("intra-abdominal-inf-2", top, dom, dis,
       "What is the definition of an organ/space surgical site infection after abdominal surgery?",
       "Organ or space SSI involves any area beyond skin/muscle/subcutaneous tissue, including intra-abdominal cavities, joints, or body compartments",
       "Deep infections after abdominal surgery may initially be subtle and require CT imaging or re-exploration for diagnosis.",
       "recall", "StatPearls", 13),
    kp("intra-abdominal-inf-3", top, dom, dis,
       "For how long must SSI surveillance be maintained after operations involving prosthetic material?",
       "1 year of surveillance after operations with prosthetic material; 30 days for operations without prosthesis",
       "Prosthetic-related infections can develop months later due to biofilm formation and slow bacterial growth.",
       "recall", "Society Guideline: Guideline   IDSA 2014 SSTI", 18),
]

# ── 19: Intracranial Pressure & Herniation ───────────────────────────
top = T(19); dom = D(19); dis = DI(19)
kps += [
    kp("icp-herniation-1", top, dom, dis,
       "What anesthetic technique modification is required in patients with elevated ICP and marginal cerebral perfusion?",
       "Anesthetic techniques must be modified to maintain CPP; avoid agents that increase ICP (e.g., ketamine, N2O at high ICP); consider osmotic diuresis or CSF drainage before induction",
       "CPP = MAP - ICP; falling MAP or rising ICP during induction can precipitate cerebral ischemia in the vulnerable patient.",
       "apply", "Morgan & Mikhail", 967),
    kp("icp-herniation-2", top, dom, dis,
       "What interventions improve intracranial compliance before anesthesia induction in a patient with elevated ICP?",
       "Osmotic diuresis (mannitol) or removal of small CSF volumes via ventriculostomy drain",
       "Reducing brain water (osmotic therapy) or CSF volume shifts the Monro-Kellie curve to a lower-pressure operating point.",
       "apply", "Morgan & Mikhail", 971),
    kp("icp-herniation-3", top, dom, dis,
       "What happens to intracranial compliance when tonsillar herniation occurs through the foramen magnum?",
       "Tonsillar herniation causes loss of intracranial compliance; further pressure rises become catastrophic",
       "At this stage the brain has exhausted all compensatory mechanisms; small volume increases cause exponential ICP rises.",
       "analyze", "StatPearls: StatPearls   Intracranial Pressure & H", 3),
    kp("icp-herniation-4", top, dom, dis,
       "What types of cerebral edema can result in intracranial hypertension?",
       "Vasogenic (BBB disruption), cytotoxic (cellular swelling), interstitial (obstructive hydrocephalus), and osmotic (hypo-osmolality/water intoxication)",
       "Each type reflects a distinct mechanism of water entry into brain parenchyma; treatment differs based on type.",
       "recall", "Morgan & Mikhail", 968),
    kp("icp-herniation-5", top, dom, dis,
       "What effect does PaCO2 have on ICP and why is mild hyperventilation used acutely?",
       "Hypocapnia (PaCO2 lowering) causes cerebral vasoconstriction, reducing CBF and acutely lowering ICP",
       "CO2 is a potent regulator of cerebrovascular tone; cerebral arterioles constrict as pH rises with hypocapnia.",
       "apply", "Morgan & Mikhail", 946),
    kp("icp-herniation-6", top, dom, dis,
       "What effect does a cerebellar hemorrhage have on intracranial compliance?",
       "Cerebellar hemorrhage can cause rapid herniation of cerebellar tonsils through the foramen magnum, with sudden loss of compliance and fatal brainstem compression",
       "The posterior fossa is a rigid, tightly constrained compartment; even small hemorrhages rapidly exhaust compliance.",
       "analyze", "StatPearls: StatPearls   Intracranial Pressure & H", 3),
]
kps.append(script(top, dis,
    "TBI, mass lesion (tumor, hematoma), hydrocephalus, stroke with edema, hyponatremia",
    "Monro-Kellie doctrine: fixed cranial volume means any volume increase (blood, CSF, brain water) raises ICP; cerebral herniation when ICP exceeds compensatory capacity",
    "Minutes (traumatic hemorrhage) to days (vasogenic edema); tonsillar herniation is terminal event",
    "Headache, nausea/vomiting, papilledema, Cushing triad (hypertension+bradycardia+irregular breathing), altered consciousness, herniation syndromes",
    "Brainstem compression causes respiratory arrest; death or permanent neurological injury"))

# ── 20: Ischemic Stroke: Clinical Syndromes & Localization ───────────
top = T(20); dom = D(20); dis = DI(20)
kps += [
    kp("stroke-syndromes-1", top, dom, dis,
       "In ischemic stroke, what happens to cerebral autoregulation and how does reduced CPP affect CBF?",
       "Cerebral autoregulation becomes impaired; as CPP decreases, cerebral vessels dilate maximally then CBF falls passively with further CPP drop",
       "Loss of autoregulation means CBF becomes pressure-passive; ischemia occurs when perfusion falls below the penumbra threshold.",
       "analyze", "StatPearls", 6),
    kp("stroke-syndromes-2", top, dom, dis,
       "What is the mechanism of cardioembolic stroke and which cardiac condition is a major risk factor?",
       "Emboli from the heart (e.g., AF with left atrial thrombus, prosthetic valve) travel to cerebral arteries causing occlusion; occasionally emboli cross via PFO",
       "Left atrial stasis in AF promotes thrombus formation; clot fragments embolize to middle cerebral artery territory.",
       "recall", "StatPearls", 3),
    kp("stroke-syndromes-3", top, dom, dis,
       "What is the stroke risk reduction strategy for patients with AF according to the ACC/AHA 2023 guideline?",
       "Stroke risk reduction therapy selection guided by patient's risk of stroke, risk of bleeding with therapy, and individual preferences; DOACs preferred over warfarin in non-valvular AF",
       "DOACs reduce stroke risk with fewer intracranial hemorrhages than warfarin in non-valvular AF.",
       "apply", "Society Guideline: Guideline   ACC AHA 2023 Atrial", 32),
    kp("stroke-syndromes-4", top, dom, dis,
       "What ischemic penumbra concept drives the rationale for time-sensitive reperfusion in acute stroke?",
       "The penumbra is electrically silent but metabolically viable brain surrounding the core infarct; it is salvageable if reperfusion occurs before irreversible infarction",
       "Neurons in the penumbra have reduced but non-zero perfusion; time-to-treatment determines how much penumbra converts to infarct.",
       "analyze", "StatPearls", 6),
]

# ── 21: Ischemic Stroke: Endovascular Thrombectomy ──────────────────
top = T(21); dom = D(21); dis = DI(21)
kps += [
    kp("stroke-evt-1", top, dom, dis,
       "What is the standard IV tPA dose for acute ischemic stroke and what is the maximum dose?",
       "IV tPA 0.9 mg/kg, maximum 90 mg; first 10% as bolus over 1 minute, remaining 90% over 60 minutes",
       "Weight-based dosing minimizes hemorrhagic transformation; the 4.5-hour window allows extended treatment in selected candidates.",
       "recall", "StatPearls", 12),
    kp("stroke-evt-2", top, dom, dis,
       "What major trials in 2015 established endovascular thrombectomy (EVT) as standard of care for large vessel occlusion stroke?",
       "Multiple 2015 trials (MR CLEAN, ESCAPE, SWIFT PRIME, EXTEND-IA) demonstrated EVT superiority for large vessel occlusion; EVT is now standard for eligible patients",
       "These trials showed dramatic functional outcome improvement with mechanical thrombectomy in proximal LVO; number needed to treat was low.",
       "recall", "StatPearls", 13),
    kp("stroke-evt-3", top, dom, dis,
       "What is the extended EVT time window when perfusion imaging is used?",
       "EVT can be performed up to 16-24 hours after stroke onset when perfusion imaging demonstrates salvageable penumbra",
       "DAWN and DEFUSE-3 trials showed that perfusion mismatch (penumbra > core) predicts EVT benefit beyond 6 hours.",
       "recall", "StatPearls", 13),
    kp("stroke-evt-4", top, dom, dis,
       "What ASPECTS threshold indicates a large infarct core that reduces EVT benefit?",
       "ASPECTS <6 indicates large infarct core (>1/3 MCA territory) on CT; lower score = larger infarct, reduced EVT benefit",
       "ASPECTS scores the caudate, putamen, internal capsule, insula, and 6 MCA cortical regions; each affected area subtracts 1 from 10.",
       "recall", "StatPearls", 14),
    kp("stroke-evt-5", top, dom, dis,
       "What metabolic abnormality should be corrected early in acute stroke to avoid confounding neurological assessment?",
       "Electrolyte imbalances (especially glucose, Na) should be corrected; BUN/Cr monitored if contrast imaging planned",
       "Hypoglycemia and hyperglycemia mimic stroke; contrast nephropathy risk requires renal function monitoring before angiography.",
       "apply", "StatPearls", 11),
]

print(f"Batch4 items: {len(kps)}")
with open('data/_kp_batch4.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("OK")
