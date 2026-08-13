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

# ── 0: Distributive Shock (Non-septic) ──────────────────────────────
top = T(0); dom = D(0); dis = DI(0)
kps += [
    kp("distributive-shock-nonseptic-1", top, dom, dis,
       "A patient with anaphylaxis has warm extremities, wide pulse pressure, and hypotension; what hemodynamic pattern is present?",
       "Low SVR, high/normal CO (distributive pattern): vasodilation causes relative hypovolemia despite adequate cardiac output",
       "Mast-cell mediators cause profound vasodilation, pooling venous blood and lowering afterload.",
       "recall", "Marino ICU Book", 153),
    kp("distributive-shock-nonseptic-2", top, dom, dis,
       "Blood lactate >4 mEq/L in a shock patient carries what prognostic significance?",
       "Strongly predicts increased mortality; lactate >= 4 mEq/L is the threshold most strongly correlated with mortality in severe sepsis/distributive shock",
       "Tissue O2 delivery fails; anaerobic metabolism generates lactate as a marker of impaired perfusion.",
       "recall", "Marino ICU Book", 153),
    kp("distributive-shock-nonseptic-3", top, dom, dis,
       "Thyroid storm causes distributive physiology; what initial fluid strategy is required alongside antithyroid therapy?",
       "Aggressive volume infusion to replace losses from vomiting, diarrhea, and heightened metabolic state",
       "Thyroid storm dramatically raises metabolic rate with concurrent GI fluid losses, producing relative intravascular depletion.",
       "apply", "Marino ICU Book", 628),
    kp("distributive-shock-nonseptic-4", top, dom, dis,
       "Why is ranitidine-based stress ulcer prophylaxis in ICU patients associated with net harm?",
       "Gastric acid suppression with ranitidine may cause more deaths from pneumonia than lives saved from fewer GI bleeds",
       "Reducing gastric acidity allows gram-negative colonization and aspiration pneumonia.",
       "apply", "Marino ICU Book", 45),
    kp("distributive-shock-nonseptic-5", top, dom, dis,
       "In anaphylaxis-mediated distributive shock, which vasopressor is first-line and what receptors does it target?",
       "Epinephrine: alpha-1 (vasoconstriction) + beta-1/2 (bronchodilation, cardiac support)",
       "Anaphylaxis causes mast-cell histamine release; epinephrine simultaneously reverses vasodilation, bronchospasm, and negative inotropy.",
       "recall", "Morgan & Mikhail", 2162),
]
kps.append(script(top, dis,
    "Anaphylaxis, neurogenic injury (spinal cord), adrenal crisis, thyroid storm; no bacterial infection required",
    "Extreme vasodilation lowers SVR; venous pooling causes relative hypovolemia; CO may be elevated initially",
    "Acute (anaphylaxis: minutes; neurogenic: immediate; thyroid storm: hours to days)",
    "Warm skin, bounding pulse, wide PP, hypotension, elevated/normal CO, low SVR",
    "Cardiovascular collapse and death if vasodilation and precipitant not urgently treated"))

# ── 1: Diverticular Bleeding ────────────────────────────────────────
top = T(1); dom = D(1); dis = DI(1)
kps += [
    kp("diverticular-bleeding-1", top, dom, dis,
       "A patient presents with painless, brisk bright-red or maroon rectal bleeding; what is the most common lower GI source in adults?",
       "Diverticular disease is the most common cause of lower GI bleeding",
       "Diverticular walls erode into perforating arterioles at the diverticular neck, causing sudden arterial hemorrhage.",
       "recall", "Morgan & Mikhail", 2157),
    kp("diverticular-bleeding-2", top, dom, dis,
       "What proportion of patients with diverticulosis develop symptomatic diverticulitis?",
       "10-20% of patients with diverticulosis develop diverticulitis (inflammation/microperforation)",
       "Low-fiber diet leads to increased intraluminal pressure promoting mucosal outpouching, predominantly in the sigmoid colon.",
       "recall", "Curated Units", 0),
    kp("diverticular-bleeding-3", top, dom, dis,
       "What clinical features distinguish diverticular bleeding from diverticulitis?",
       "Bleeding: painless, brisk, usually self-limited; Diverticulitis: LLQ pain, fever, leukocytosis, diarrhea",
       "Bleeding arises from vascular erosion without inflammation; diverticulitis reflects microperforation with local infection.",
       "analyze", "Curated Units", 0),
    kp("diverticular-bleeding-4", top, dom, dis,
       "When is surgery or interventional radiology generally indicated for severe peptic ulcer or lower GI hemorrhage?",
       "Severe hemorrhage (>5 units transfused) and recurrent bleeding are indications; H2-blockers and PPIs do not stop active hemorrhage",
       "Medical acid suppression reduces rebleeding risk but mechanical hemostasis is required for ongoing arterial bleeding.",
       "apply", "Morgan & Mikhail", 2157),
    kp("diverticular-bleeding-5", top, dom, dis,
       "What nuclear medicine test using radiolabeled RBCs detects slow lower GI bleeding rates?",
       "99mTc-labeled RBC scintigraphy; in-vivo method: 1 mg stannous pyrophosphate then IV 99mTc-pertechnetate",
       "Labeled RBCs pool at the bleeding site over serial images, detecting hemorrhage rates too slow for angiography.",
       "recall", "StatPearls: StatPearls   Gastrointestinal bleeding", 2),
]
kps.append(script(top, dis,
    "Age >50, low-fiber diet, NSAIDs/aspirin use, pre-existing diverticulosis",
    "Erosion of perforating arteriole at diverticular neck; no inflammation unlike diverticulitis",
    "Abrupt onset; 75-80% stops spontaneously; 25% rebleed within 1 year",
    "Painless hematochezia (bright red or maroon), hemodynamic compromise if massive; colonoscopy confirms",
    "Delayed diagnosis delays hemostasis; ongoing hemorrhage causes hemodynamic instability and death"))
kps.append(pair("Diverticular Bleeding", "Diverticulitis",
    "Bleeding: painless, brisk hemorrhage, no fever; Diverticulitis: LLQ pain, fever, leukocytosis, no significant hematochezia"))

# ── 2: Drug-induced lupus ─────────────────────────────────────────
top = T(2); dom = D(2); dis = DI(2)
kps += [
    kp("drug-induced-lupus-1", top, dom, dis,
       "A patient on long-term procainamide develops arthralgia, fever, and myalgia; what autoantibody is most characteristic?",
       "Anti-histone antibodies are characteristic of drug-induced lupus erythematosus (DIL)",
       "Drug metabolites haptenize nuclear histones, triggering IgG autoantibody formation against histone-DNA complexes.",
       "recall", "MGH Housestaff Manual", 192),
    kp("drug-induced-lupus-2", top, dom, dis,
       "What antiarrhythmic agent has drug-induced lupus listed as a side effect of long-term use?",
       "Procainamide (long-term use) causes drug-induced lupus",
       "Procainamide and its metabolite N-acetylprocainamide modify nuclear antigens, inducing loss of self-tolerance.",
       "recall", "MGH Housestaff Manual", 44),
    kp("drug-induced-lupus-3", top, dom, dis,
       "How does organ involvement in drug-induced lupus differ from idiopathic SLE?",
       "DIL: renal, neurologic, and vasculitic involvement uncommon; constitutional and musculoskeletal symptoms (arthralgia, fever, myalgia, fatigue) dominate",
       "DIL autoantibodies target histones (not dsDNA) and do not activate complement-mediated glomerulonephritis as in SLE.",
       "analyze", "StatPearls: StatPearls   Drug induced lupus", 5),
    kp("drug-induced-lupus-4", top, dom, dis,
       "Which cutaneous manifestation appears more frequently in drug-induced lupus than in idiopathic SLE?",
       "Subacute cutaneous lupus erythematosus (SCLE) is more frequent in DIL",
       "Certain drugs preferentially trigger anti-Ro/SS-A pathway that mediates SCLE.",
       "recall", "StatPearls: StatPearls   Drug induced lupus", 5),
    kp("drug-induced-lupus-5", top, dom, dis,
       "What lab test distinguishes drug-induced lupus from idiopathic SLE?",
       "Anti-histone Abs support DIL; anti-dsDNA Abs favor idiopathic SLE (anti-dsDNA rare in DIL)",
       "Anti-dsDNA requires loss of tolerance to native DNA, which does not occur in drug-hapten mechanism.",
       "analyze", "MGH Housestaff Manual", 192),
]
kps.append(script(top, dis,
    "Chronic use of procainamide, hydralazine, isoniazid, minocycline, anti-TNF agents",
    "Drug metabolite modifies nuclear histones; loss of tolerance generates anti-histone IgG; complement activation causes systemic inflammation",
    "Weeks to years after drug initiation; resolves within weeks to months after drug discontinuation",
    "Arthralgia, fever, myalgia, fatigue, pleuritis; anti-histone Ab+; rare renal/CNS involvement",
    "Continued exposure worsens disease; misdiagnosis as idiopathic SLE leads to unnecessary immunosuppression"))
kps.append(pair("Drug-Induced Lupus", "Idiopathic SLE",
    "DIL: anti-histone Abs, no anti-dsDNA, rare renal/CNS, resolves with drug discontinuation; SLE: anti-dsDNA, frequent nephritis, chronic course"))

# ── 3: Glycemic Control in ICU ────────────────────────────────────
top = T(3); dom = D(3); dis = DI(3)
kps += [
    kp("glycemic-icu-1", top, dom, dis,
       "Intensive insulin therapy (target 80-110 mg/dL) vs conventional therapy (180-200 mg/dL) in ICU sepsis: what was the mortality outcome in a large RCT?",
       "No significant difference in 28-day or 90-day mortality; intensive insulin therapy significantly increased hypoglycemia",
       "Tight glycemic control increases hypoglycemia events, which cause neuronal injury and may offset metabolic benefits.",
       "analyze", "Society Guideline: Guideline   KDIGO 2012 AKI", 47),
    kp("glycemic-icu-2", top, dom, dis,
       "Blood glucose <40 mg/dL in an ICU patient represents what dangerous complication of intensive insulin therapy?",
       "Severe hypoglycemia (BG <40 mg/dL) is a key harm of intensive insulin therapy (IIT) in the ICU",
       "Neurons are entirely glucose-dependent; brief hypoglycemia causes irreversible neuronal injury.",
       "recall", "Society Guideline: Guideline   KDIGO 2012 AKI", 47),
    kp("glycemic-icu-3", top, dom, dis,
       "What hemodynamic feature of sepsis complicates reliable medication titration including insulin dosing?",
       "Systemic blood pooling and fluid transudation cause relative hypovolemia, altering volume of distribution and drug pharmacokinetics",
       "Vasodilation in sepsis redistributes circulating volume, making standard dosing protocols unreliable.",
       "apply", "Morgan & Mikhail", 2126),
]

# ── 4: Gout: urate-lowering therapy & long-term management ──────────
top = T(4); dom = D(4); dis = DI(4)
kps += [
    kp("gout-ult-1", top, dom, dis,
       "A serum uric acid >6.8 mg/dL is found incidentally; does this confirm a diagnosis of gout?",
       "No; elevated uric acid supports but neither confirms nor is required for gout diagnosis; asymptomatic hyperuricemia is common",
       "Urate crystals precipitate at >6.8 mg/dL (saturation point) but many hyperuricemic individuals never develop gout.",
       "recall", "StatPearls: StatPearls   Gout  acute management", 14),
    kp("gout-ult-2", top, dom, dis,
       "What are the two mechanisms causing hyperuricemia in gout, and which is more common?",
       "Underexcretion (most common, ~90%) or overproduction of uric acid; overproduction causes include Lesch-Nyhan, tumor lysis, myeloproliferative disorders",
       "Most gout results from impaired renal urate excretion; a minority overproduce urate via purine metabolism defects.",
       "recall", "StatPearls: StatPearls   Gout  acute management", 24),
    kp("gout-ult-3", top, dom, dis,
       "What is the mechanism of action of colchicine in acute gout?",
       "Colchicine inhibits microtubule formation and neutrophil chemotaxis, reducing crystal-induced inflammation",
       "Urate crystals activate the NLRP3 inflammasome and recruit neutrophils; colchicine blocks tubulin polymerization required for neutrophil migration.",
       "recall", "StatPearls: StatPearls   Gout  acute management", 24),
    kp("gout-ult-4", top, dom, dis,
       "Pegloticase is reserved for which gout patients, and why must standard ULT be stopped when starting it?",
       "Refractory gout with high tophaceous burden; standard ULT must be discontinued because antibodies to pegloticase develop when urate falls, increasing infusion reactions and loss of efficacy",
       "PEGylated uricase degrades urate to allantoin; concomitant ULT lowers urate and masks antibody formation that predicts loss of response.",
       "apply", "StatPearls: StatPearls   Gout  acute management", 22),
    kp("gout-ult-5", top, dom, dis,
       "What modifiable dietary/lifestyle factors should be addressed in chronic gout management?",
       "Obesity, alcohol use, excessive red meat and shellfish consumption are modifiable risk factors",
       "Purines from animal proteins increase urate synthesis; alcohol increases urate production and decreases renal excretion.",
       "recall", "StatPearls: StatPearls   Gout  acute management", 24),
    kp("gout-ult-6", top, dom, dis,
       "What diagnoses must be urgently excluded in a patient presenting with acute monoarthritis before treating as gout?",
       "Exclude septic arthritis (requires urgent drainage and antibiotics), CPPD (pseudogout), and basic calcium phosphate disease",
       "Treating septic arthritis as gout delays definitive care and risks irreversible joint destruction.",
       "analyze", "StatPearls: StatPearls   Gout  acute management", 23, "Septic arthritis"),
]
kps.append(pair("Gout", "Pseudogout (CPPD)",
    "Gout: monosodium urate crystals (negatively birefringent, needle-shaped), often 1st MTP; Pseudogout: calcium pyrophosphate (positively birefringent, rhomboid), often knee/wrist"))

print(f"Batch1 items: {len(kps)}")
with open('data/_kp_batch1.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("OK")
