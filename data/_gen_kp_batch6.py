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

# ── 26: Lupus nephritis ──────────────────────────────────────────
top = T(26); dom = D(26); dis = DI(26)
kps += [
    kp("lupus-nephritis-1", top, dom, dis,
       "What proportion of SLE patients develop lupus nephritis, and within what timeframe?",
       "Approximately 40% of SLE patients develop lupus nephritis, often within 5 years of SLE diagnosis",
       "Immune complex deposition in the glomerulus activates complement and inflammatory cascades causing nephritis.",
       "recall", "StatPearls: StatPearls   Lupus nephritis", 6),
    kp("lupus-nephritis-2", top, dom, dis,
       "What percentage of lupus nephritis patients progress to end-stage renal disease?",
       "Approximately 10-30% of lupus nephritis patients progress to ESRD",
       "Proliferative classes (III/IV) carry the highest risk of progression; early aggressive treatment reduces ESRD risk.",
       "recall", "StatPearls: StatPearls   Lupus nephritis", 6),
    kp("lupus-nephritis-3", top, dom, dis,
       "What is the cornerstone diagnostic test that guides treatment class selection in lupus nephritis?",
       "Renal biopsy is the cornerstone for diagnosing lupus nephritis and classifying pathological lesion to guide treatment",
       "Different ISN/RPS histologic classes (I-VI) have distinct prognoses and require different intensities of immunosuppression.",
       "recall", "StatPearls: StatPearls   Lupus nephritis", 10),
    kp("lupus-nephritis-4", top, dom, dis,
       "What is the treatment approach for Class V (membranous) lupus nephritis?",
       "Pulse steroids (IV methylprednisolone) then prednisone taper; pulse steroids with each cyclophosphamide dose linked to improved outcomes",
       "Class V involves immune complex deposition on the subepithelial surface; high-dose steroids suppress antibody production.",
       "apply", "StatPearls: StatPearls   Lupus nephritis", 12),
    kp("lupus-nephritis-5", top, dom, dis,
       "What significantly increased cardiovascular risk is associated with lupus nephritis?",
       "Lupus nephritis substantially increases coronary artery disease risk via atherosclerosis, vasculitis, thrombosis, and dyslipidemia mechanisms",
       "Chronic inflammation and antiphospholipid antibodies accelerate atherosclerosis; renal disease adds hypertension and dyslipidemia.",
       "recall", "StatPearls: StatPearls   Lupus nephritis", 7),
    kp("lupus-nephritis-6", top, dom, dis,
       "What pathophysiologic mechanism drives anti-dsDNA-mediated kidney injury in lupus nephritis?",
       "Anti-dsDNA antibodies activate neutrophil extracellular traps (NETs); cell apoptosis releases nuclear antigens fueling further autoantibody production",
       "NETs expose nuclear chromatin to the immune system; anti-dsDNA/complement complex deposition in glomeruli drives nephritis.",
       "analyze", "StatPearls: StatPearls   Lupus nephritis", 5),
]
kps.append(script(top, dis,
    "Established SLE, often within 5 years; female sex, Afro-Caribbean/Hispanic ancestry",
    "Immune complex (anti-dsDNA + complement) deposition in glomeruli; complement activation, neutrophil/macrophage recruitment cause glomerular injury",
    "Weeks to months; can be acute nephritic (hematuria, HTN, AKI) or insidious proteinuria",
    "Proteinuria, hematuria, HTN, rising creatinine; ANA+, anti-dsDNA+, low complement (C3/C4); biopsy confirms class",
    "Untreated proliferative nephritis (Class III/IV) rapidly progresses to ESRD"))

# ── 27: Mechanical Ventilation (anesthesia-focused chunks) ───────────
top = T(27); dom = D(27); dis = DI(27)
kps += [
    kp("mech-vent-1", top, dom, dis,
       "What extubation criteria regarding tidal volume and vital capacity must be met?",
       "TV >5 mL/kg and VC >15 mL/kg; SpO2 >90% on FiO2 <0.4; RR >6 and <30; EtCO2 <50-60",
       "Adequate TV and VC ensure the patient can sustain spontaneous breathing and clear secretions after extubation.",
       "recall", "Stanford CA-1", 70),
    kp("mech-vent-2", top, dom, dis,
       "What are the causes of failed extubation related to ventilatory failure?",
       "Failure to oxygenate (TV <5 mL/kg, VC <15 mL/kg, SpO2 <90% on FiO2 >0.4) or failure to ventilate (excessive hypercapnia, inadequate NMB reversal)",
       "Extubation failure is more likely from NMB residual, secretions, or airway edema than from hypoxemia alone.",
       "apply", "Stanford CA-1", 70),
    kp("mech-vent-3", top, dom, dis,
       "What does an upsloping capnography trace indicate in a mechanically ventilated patient?",
       "Upsloping capnogram indicates bronchospasm; significant hypotension is associated with a drop in EtCO2",
       "Bronchospasm slows alveolar emptying, creating phase III slope; reduced CO causes less CO2 delivery to lungs.",
       "analyze", "Stanford CA-1", 16),
    kp("mech-vent-4", top, dom, dis,
       "What non-invasive ventilatory support options precede intubation for a hypoxic patient?",
       "Supplemental O2 via nasal cannula/Venturi mask; high-flow nasal cannula (HFNC); CPAP/BiPAP (non-invasive positive pressure ventilation)",
       "HFNC provides high FiO2 and modest PEEP; NIV (CPAP/BiPAP) unloads respiratory muscles and prevents atelectasis.",
       "apply", "MGH Housestaff Manual", 48),
    kp("mech-vent-5", top, dom, dis,
       "What is TRALI and when does it typically occur?",
       "TRALI (Transfusion-Related Acute Lung Injury): non-cardiogenic pulmonary edema occurring 4-6 hours after transfusion; due to plasma-containing products (platelets, FFP > pRBCs)",
       "Donor anti-HLA or anti-neutrophil antibodies activate recipient neutrophils in pulmonary vasculature, causing capillary leak.",
       "recall", "Stanford CA-1", 52),
]

# ── 28: Mechanical Ventilation: Physiology & Modes ──────────────────
top = T(28); dom = D(28); dis = DI(28)
kps += [
    kp("vent-modes-1", top, dom, dis,
       "What is the difference between volume-targeted and pressure-targeted ventilation modes?",
       "Volume-targeted: set TV delivered regardless of pressure generated; Pressure-targeted: set pressure maintained, TV varies with compliance",
       "Volume control ensures consistent minute ventilation; pressure control limits peak airway pressure but TV varies with lung mechanics.",
       "recall", "Miller/Baby Miller", 768),
    kp("vent-modes-2", top, dom, dis,
       "In pressure-cycled ventilation, what characteristic flow pattern is produced?",
       "Constant-pressure generators maintain airway pressure constant; flow decelerates as the alveolus fills (decelerating flow pattern)",
       "Pressure-controlled breaths deliver flow until alveolar pressure equals set Pcontrol; flow naturally decreases as lung fills.",
       "recall", "Morgan & Mikhail", 2190),
    kp("vent-modes-3", top, dom, dis,
       "What rapid shallow breathing index (RSBI) threshold predicts successful weaning from mechanical ventilation?",
       "RSBI <105 breaths/min/L predicts success; RSBI >105 breaths/min/L is better at identifying patients who will fail",
       "RSBI = RR/TV; high frequency with low TV indicates increased work of breathing and respiratory muscle fatigue.",
       "recall", "Miller/Baby Miller", 770),
    kp("vent-modes-4", top, dom, dis,
       "What causes increased peak airway pressure with unchanged plateau pressure on a ventilator?",
       "Increased airway resistance (e.g., bronchospasm, secretions, kinked ETT); plateau pressure reflects alveolar/compliance pressure",
       "Peak Paw - Plateau Paw = resistive pressure; if only peak rises, the problem is airway resistance, not alveolar compliance.",
       "analyze", "Miller/Baby Miller", 380),
    kp("vent-modes-5", top, dom, dis,
       "What are the two key concerns regarding retinopathy of prematurity (ROP) in neonatal ventilator management?",
       "Hyperoxia and hypoxia are both risk factors for ROP but are not the primary causes; titrate SpO2 targets carefully",
       "Excessive O2 causes vasoconstriction then pathologic neovascularization; hypoxia also triggers aberrant vessel growth.",
       "apply", "Morgan & Mikhail", 2164),
]

print(f"Batch6 items: {len(kps)}")
with open('data/_kp_batch6.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("OK")
