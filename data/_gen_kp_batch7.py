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

# ── 29: Mesenteric Ischemia ──────────────────────────────────────
top = T(29); dom = D(29); dis = DI(29)
kps += [
    kp("mesenteric-ischemia-1", top, dom, dis,
       "What are the three clinical types of mesenteric ischemia?",
       "Acute mesenteric ischemia, chronic mesenteric ischemia, and colonic ischemia",
       "Each has distinct pathophysiology: acute is embolic/thrombotic; chronic is stenotic (postprandial pain); colonic is low-flow.",
       "recall", "MGH Housestaff Manual", 83),
    kp("mesenteric-ischemia-2", top, dom, dis,
       "What are symptoms of constitutional vasculitic involvement including mesenteric ischemia in a patient with polyarteritis nodosa?",
       "Constitutional symptoms (fever, fatigue, weight loss), mononeuritis multiplex, GI distress (mesenteric ischemia), myalgias, AKI",
       "PAN is a medium-vessel vasculitis; mesenteric artery involvement causes ischemia and GI bleeding.",
       "apply", "MGH Housestaff Manual", 177),
    kp("mesenteric-ischemia-3", top, dom, dis,
       "What contraindications to terlipressin in hepatorenal syndrome include vascular ischemia?",
       "Terlipressin is contraindicated in: Cr >5 mg/dL, SpO2 <90%, pregnancy, active mesenteric or peripheral ischemia",
       "Terlipressin is a vasopressin analog; splanchnic vasoconstriction can worsen mesenteric and peripheral ischemia.",
       "apply", "MGH Housestaff Manual", 97),
    kp("mesenteric-ischemia-4", top, dom, dis,
       "In evaluation of acute abdominal pain, what features suggest mesenteric ischemia vs small bowel obstruction?",
       "Mesenteric ischemia: pain out of proportion to exam, older patient, AF or atherosclerosis risk factors, metabolic acidosis; SBO: colicky pain, distension, vomiting, air-fluid levels",
       "Mesenteric ischemia often presents deceptively benign early; SBO causes mechanical obstruction with distension.",
       "analyze", "MGH Housestaff Manual", 72, "Small Bowel Obstruction"),
    kp("mesenteric-ischemia-5", top, dom, dis,
       "What lower GI bleeding cause specifically involves the ischemic segment of colon?",
       "Ischemic colitis is a cause of lower GI bleeding, distinct from diverticular and angiodysplastic sources",
       "Low-flow states (shock, aortic surgery) reduce mesenteric perfusion; watershed areas (splenic flexure, sigmoid) are most vulnerable.",
       "recall", "MGH Housestaff Manual", 71),
]
kps.append(script(top, dis,
    "AF (embolic), atherosclerosis (thrombotic/stenotic), hypercoagulable states, vasculitis, low-flow states (shock)",
    "SMA occlusion (embolus or thrombus) or non-occlusive ischemia causes bowel infarction; colonic ischemia via low-flow at watershed zones",
    "Acute: sudden severe pain, rapid progression to infarction/peritonitis within hours; chronic: postprandial angina",
    "Pain out of proportion to exam, lactic acidosis, bloody diarrhea (colonic); CT angiography confirms",
    "Full-thickness bowel necrosis, perforation, peritonitis, septic shock, death"))

# ── 30: Migraine: Acute & Preventive Treatment ──────────────────────
top = T(30); dom = D(30); dis = DI(30)
kps += [
    kp("migraine-1", top, dom, dis,
       "What is the combination oral therapy that exploits synergy between a triptan and an NSAID for acute migraine?",
       "Sumatriptan 85 mg + naproxen sodium 500 mg in a single tablet; combination more effective than either drug alone",
       "Triptans act on 5-HT1B/1D receptors to cause vasoconstriction and inhibit CGRP release; NSAIDs reduce neurogenic inflammation.",
       "apply", "StatPearls: StatPearls   Migraine  Acute & Prevent", 11),
    kp("migraine-2", top, dom, dis,
       "What ICHD-3 criterion defines the headache character in migraine without aura?",
       "Criterion B1a: headache with >=2 of: unilateral, pulsating, moderate-severe intensity, aggravated by routine activity; >=1 of: nausea/vomiting, photophobia/phonophobia",
       "Trigeminal activation and cortical spreading depression drive migraine pain; photophobia reflects thalamic hypersensitivity.",
       "recall", "StatPearls: StatPearls   Migraine  Acute & Prevent", 8),
    kp("migraine-3", top, dom, dis,
       "What are the indications for initiating preventive migraine therapy?",
       "Frequent or long-lasting headaches causing significant disability; contraindications/failure of acute therapies; significant adverse effects from abortive therapy",
       "Preventive treatment reduces attack frequency and severity; prophylaxis is warranted when acute therapy burden is high.",
       "apply", "StatPearls: StatPearls   Migraine  Acute & Prevent", 12),
    kp("migraine-4", top, dom, dis,
       "What red flag differentials must be considered when evaluating a patient with migraine-like headache?",
       "Tension-type headache, chronic paroxysmal hemicrania, subarachnoid/intracranial hemorrhage, temporal/giant cell arteritis",
       "SAH and GCA are life- and vision-threatening; must be excluded before labeling headache as primary migraine.",
       "analyze", "StatPearls: StatPearls   Migraine  Acute & Prevent", 13, "Subarachnoid hemorrhage"),
    kp("migraine-5", top, dom, dis,
       "What is the SNOOP4 screening tool used for in headache evaluation?",
       "SNOOP4 screens for secondary headache red flags: Systemic symptoms, Neurological signs, Onset sudden (thunderclap), Older >50, Position-dependent, Prior pattern change, Papilledema/pregnancy",
       "Secondary causes (meningitis, SAH, mass) require urgent investigation; SNOOP4 systematically identifies these red flags.",
       "apply", "StatPearls: StatPearls   Headache  Primary Disorde", 7),
]

# ── 31: Mixed connective tissue disease & overlap syndromes ──────────
top = T(31); dom = D(31); dis = DI(31)
kps += [
    kp("mctd-overlap-1", top, dom, dis,
       "What antibody profile is associated with limited cutaneous systemic sclerosis overlap with mixed connective tissue disease?",
       "Anti-U1 RNP antibodies are associated with overlap syndrome and mixed connective tissue disease; linked to limited cutaneous involvement and increased risk of inflammatory arthritis",
       "Anti-U1 RNP is the hallmark antibody of MCTD; it defines the overlap of SLE, myositis, and scleroderma features.",
       "recall", "StatPearls: StatPearls   Systemic sclerosis (scler", 14),
    kp("mctd-overlap-2", top, dom, dis,
       "What joint and extra-articular manifestations does azathioprine effectively treat in undifferentiated CTD?",
       "Azathioprine is typically effective for joint and extra-articular symptoms in undifferentiated connective tissue disease",
       "Azathioprine inhibits purine synthesis, reducing lymphocyte proliferation and autoantibody production.",
       "apply", "StatPearls", 6),
    kp("mctd-overlap-3", top, dom, dis,
       "What features define undifferentiated connective tissue disease (UCTD)?",
       "Symptoms of inflammation associated with UCTD that do not meet criteria for any single defined CTD (SLE, MCTD, Sjogren, systemic sclerosis, PM/DM, RA)",
       "UCTD represents early or limited autoimmune disease; some patients evolve to a defined CTD over time.",
       "recall", "StatPearls", 6),
    kp("mctd-overlap-4", top, dom, dis,
       "What clinical features characterize MCTD per the MGH clinical presentation pattern?",
       "Female > Male, age 15-40, Afro/Latino/Asian > White; constitutional sx (fever, fatigue, myalgia), inflammatory polyarthritis, Raynaud phenomenon",
       "MCTD is defined by high-titer anti-U1 RNP with overlapping features of SLE, myositis, and scleroderma.",
       "recall", "MGH Housestaff Manual", 175),
    kp("mctd-overlap-5", top, dom, dis,
       "What serious vascular complication is associated with connective tissue diseases and should be evaluated with right heart catheterization?",
       "Pulmonary arterial hypertension (PAH): RHC is the gold standard diagnosis; associated with MCTD, SSc, SLE",
       "CTD-associated PAH results from endothelial injury and vascular remodeling; early detection prevents right heart failure.",
       "apply", "MGH Housestaff Manual", 56),
]

# ── 32: Multidrug-Resistant Organisms (MDROs) ───────────────────────
top = T(32); dom = D(32); dis = DI(32)
kps += [
    kp("mdro-1", top, dom, dis,
       "What conditions in the ICU predispose patients to colonization with multidrug-resistant organisms?",
       "Chemotherapy, prolonged use of invasive devices, respiratory failure, kidney failure, head trauma, burns; also prior broad-spectrum antibiotics",
       "Altered host defenses and antibiotic pressure select for resistant organisms; invasive devices breach mucosal barriers.",
       "recall", "Morgan & Mikhail", 2152),
    kp("mdro-2", top, dom, dis,
       "What is the mechanism of AmpC beta-lactamase resistance and which antibiotics does it affect?",
       "AmpC inactivates 3rd-gen cephalosporins and piperacillin-tazobactam; can be constitutive or inducible by beta-lactam exposure",
       "Inducible AmpC is de-repressed by cephalosporin accumulation of cell wall fragments (muropeptides), making initial susceptibility unreliable.",
       "recall", "MGH Housestaff Manual", 115),
    kp("mdro-3", top, dom, dis,
       "What are target trough concentrations for vancomycin in severe MDRO infections?",
       "Vancomycin trough concentrations of 15-20 mcg/mL are targeted in severe infections",
       "Higher troughs improve tissue penetration and bactericidal activity against MRSA and other resistant gram-positive organisms.",
       "recall", "Society Guideline: Guideline   IDSA 2014 SSTI", 33),
    kp("mdro-4", top, dom, dis,
       "What is a recognized consequence of long-term unnecessary antibiotic use beyond selecting for resistance?",
       "Toxicity and colonization with multidrug-resistant organisms are recognized consequences of prolonged unnecessary antibiotic use",
       "Dysbiosis from broad-spectrum antibiotics eliminates commensal flora, creating ecologic niches for resistant pathogens.",
       "apply", "StatPearls: StatPearls   MEN Syndromes (Multiple E", 26),
    kp("mdro-5", top, dom, dis,
       "What are absolute contraindications to hematopoietic stem cell transplant related to infection?",
       "Pretransplant infection with multidrug-resistant organisms, active sepsis, and profound leukopenia (<500/mm3) are absolute contraindications",
       "Active MDR infections or sepsis at time of transplant would be amplified by the profound immunosuppression required for conditioning.",
       "recall", "StatPearls", 5),
    kp("mdro-6", top, dom, dis,
       "Why does preservation of gastric acidity matter in the ICU regarding MDRO colonization?",
       "Gastric acidity inhibits overgrowth of gram-negative organisms in the stomach; suppression allows colonization and aspiration risk",
       "Acid-suppressing medications reduce gastric pH, enabling gram-negative bacterial overgrowth that can be aspirated into the lungs.",
       "apply", "Morgan & Mikhail", 2152),
]

print(f"Batch7 items: {len(kps)}")
with open('data/_kp_batch7.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("OK")
