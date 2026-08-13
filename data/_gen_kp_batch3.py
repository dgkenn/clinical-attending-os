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

# ── 11: Hypothermia ───────────────────────────────────────────────
top = T(11); dom = D(11); dis = DI(11)
kps += [
    kp("hypothermia-1", top, dom, dis,
       "What is the definition of hypothermia in anesthetic practice?",
       "Core body temperature less than 36 degrees Celsius",
       "Below 36C, peripheral vasodilation from anesthetic agents redistributes core heat to the periphery.",
       "recall", "Stanford CA-1", 63),
    kp("hypothermia-2", top, dom, dis,
       "By how much does metabolic rate decrease per 1C drop in core temperature?",
       "Metabolic rate decreases approximately 8% per 1C decrease in temperature",
       "Reduced metabolic demand lowers O2 consumption, confers myocardial and CNS protection during surgical cooling.",
       "recall", "Stanford CA-1", 64),
    kp("hypothermia-3", top, dom, dis,
       "What is the rationale for targeted temperature management (TTM) after cardiac arrest?",
       "Fever worsens neurological outcomes and neuronal damage via inflammatory cascades after ischemia-reperfusion; TTM prevents fever for neuroprotection",
       "Reperfusion injury generates reactive oxygen species and inflammatory mediators; normothermia/mild cooling limits secondary neuronal death.",
       "apply", "MGH Housestaff Manual", 5),
    kp("hypothermia-4", top, dom, dis,
       "What is the single most effective intervention to reduce redistribution hypothermia in the first 30 minutes after anesthetic induction?",
       "Preoperative forced-air warming of torso and legs for 30 minutes before induction",
       "Preinduction warming elevates peripheral tissue temperature, minimizing the core-to-periphery gradient that drives redistribution heat loss.",
       "apply", "Stanford CA-1", 65),
    kp("hypothermia-5", top, dom, dis,
       "What site provides the gold standard core temperature measurement using a catheter?",
       "Thermistor of a pulmonary artery catheter is the gold standard core temperature measurement site",
       "The PAC thermistor sits in the central pulmonary artery, directly sampling mixed venous blood temperature.",
       "recall", "Stanford CA-1", 63),
]

# ── 12: ICU Procedures & Vascular Access (chunks mostly off-topic) ───
top = T(12); dom = D(12); dis = DI(12)
kps += [
    kp("icu-procedures-1", top, dom, dis,
       "What catheter allows simultaneous right-heart pressure measurement and cardiac output determination via thermodilution?",
       "Pulmonary artery catheter (PAC): 110-cm balloon-tipped catheter advanced from RA to RV to wedge position in pulmonary artery",
       "Following pressure waveforms from RA to RV to PA confirms correct placement; PCWP approximates LA pressure.",
       "recall", "Miller/Baby Miller", 397),
    kp("icu-procedures-2", top, dom, dis,
       "What is a major concern when placing an introducer sheath for a PAC regarding fluid resuscitation?",
       "Catheter placement into an introducer sheath can significantly reduce fluid flow rate through the sheath",
       "The PAC occupies most of the sheath lumen, restricting the cross-sectional area available for rapid fluid infusion.",
       "apply", "Miller/Baby Miller", 397),
    kp("icu-procedures-3", top, dom, dis,
       "What family-centered ICU care practices have been shown to reduce patient anxiety, confusion, and agitation?",
       "Patient/family inclusion on rounds, extended visiting hours, and family presence during procedures reduce anxiety and agitation",
       "ICU-acquired delirium and anxiety are worsened by isolation; family presence maintains orientation and reduces fear.",
       "apply", "Miller/Baby Miller", 775),
]

# ── 13: ICU Sedation ──────────────────────────────────────────────
top = T(13); dom = D(13); dis = DI(13)
kps += [
    kp("icu-sedation-1", top, dom, dis,
       "Why is etomidate avoided for prolonged ICU sedation, particularly in septic patients?",
       "Etomidate infusion causes consistent adrenocortical suppression and was associated with increased mortality in critically ill (especially septic) patients",
       "Etomidate irreversibly inhibits 11-beta-hydroxylase, blocking cortisol synthesis; adrenal insufficiency worsens septic shock.",
       "recall", "Morgan & Mikhail", 290),
    kp("icu-sedation-2", top, dom, dis,
       "Why is propofol not recommended for prolonged sedation in critically ill pediatric patients?",
       "Propofol is associated with mortality in critically ill pediatric patients (propofol infusion syndrome)",
       "Propofol infusion syndrome causes metabolic acidosis, rhabdomyolysis, cardiac failure, and renal failure in children on prolonged infusions.",
       "recall", "Morgan & Mikhail", 1456),
    kp("icu-sedation-3", top, dom, dis,
       "What is the rationale for moving away from mechanical restraints and sedative/paralytic drugs for ICU delirium management?",
       "Restraints are inhumane and all such approaches (restraints, heavy sedation, paralysis) are associated with adverse consequences",
       "Over-sedation prolongs ICU stay, increases delirium, and delays weaning; goal-directed light sedation improves outcomes.",
       "apply", "Morgan & Mikhail", 2158),
    kp("icu-sedation-4", top, dom, dis,
       "What is the typical total dose of flumazenil for benzodiazepine reversal, and why must repeat doses be considered?",
       "Flumazenil 0.2 mg/min IV to desired reversal, usual total dose 0.6-1.0 mg; repeat doses needed due to rapid hepatic clearance",
       "Flumazenil has a short half-life (~1 hour) compared with most benzodiazepines, so resedation can occur.",
       "apply", "Morgan & Mikhail", 467),
    kp("icu-sedation-5", top, dom, dis,
       "What effect does etomidate have on cerebral blood flow and ICP, making it useful in neurosurgical patients?",
       "Etomidate decreases cerebral metabolic rate, cerebral blood flow, and ICP while maintaining cerebral perfusion pressure",
       "Because etomidate has minimal cardiovascular effects, MAP is preserved, maintaining CPP = MAP - ICP.",
       "recall", "Morgan & Mikhail", 290),
]

# ── 14: Immunodeficiency: primary antibody deficiencies ──────────────
top = T(14); dom = D(14); dis = DI(14)
kps += [
    kp("prim-immunodef-1", top, dom, dis,
       "What is the most prevalent primary antibody deficiency?",
       "Secondary antibody deficiency (from HIV) is most common overall; among primary deficiencies, antibody deficiency (41%) is most prevalent; IgA deficiency is the most common selective immunoglobulin deficiency",
       "B-cell development defects prevent immunoglobulin production; IgA deficiency is often asymptomatic but increases infection risk.",
       "recall", "StatPearls: StatPearls   Immunodeficiency  primary", 6),
    kp("prim-immunodef-2", top, dom, dis,
       "At what age does X-linked agammaglobulinemia typically present and why?",
       "Around 5-6 months of age when maternal IgG disappears; male infants present with recurrent bacterial infections",
       "Maternal IgG transferred transplacentally provides passive immunity for the first months; once depleted, lack of BTK-mediated B-cell maturation becomes apparent.",
       "recall", "StatPearls: StatPearls   Immunodeficiency  primary", 10),
    kp("prim-immunodef-3", top, dom, dis,
       "What defect causes DiGeorge anomaly and what immune cell is primarily affected?",
       "Defect in the 3rd and 4th pharyngeal pouches causes abnormal thymic development; T-cell deficiency results (variable severity based on thymic lesion)",
       "The thymus is derived from the 3rd pharyngeal pouch; absent or hypoplastic thymus prevents T-cell maturation.",
       "recall", "StatPearls: StatPearls   Immunodeficiency  primary", 5),
    kp("prim-immunodef-4", top, dom, dis,
       "What genetic defect causes autosomal recessive SCID?",
       "Mutations in RAG1 or RAG2 genes cause autosomal recessive SCID by preventing V(D)J recombination of immunoglobulin/T-cell receptor genes",
       "RAG1/2 enzymes initiate V(D)J recombination required for antigen receptor diversity; deficiency prevents both B- and T-cell development.",
       "recall", "StatPearls: StatPearls   Immunodeficiency  primary", 5),
    kp("prim-immunodef-5", top, dom, dis,
       "What workup specimens should be collected in suspected primary immunodeficiency?",
       "CBC, sputum culture + Pneumocystis PCR, stool for viral/bacterial/parasitic infection, CSF culture/chemistry/histopathology, serum immunoglobulin levels",
       "Comprehensive microbiologic workup reveals the pattern of susceptibility (encapsulated bacteria = antibody deficiency; fungal/viral = T-cell defect).",
       "apply", "StatPearls: StatPearls   Immunodeficiency  primary", 9),
]

# ── 15: Infective Endocarditis: Diagnosis ──────────────────────────
top = T(15); dom = D(15); dis = DI(15)
kps += [
    kp("ie-diagnosis-1", top, dom, dis,
       "What are the sources of bloodstream infection (BSI) that must be considered when evaluating positive blood cultures?",
       "Lines, procedures, meningitis, endocarditis, osteomyelitis, septic arthritis, pneumonia, UTI, SSTI, abscesses",
       "Blood cultures must trigger systematic source evaluation; endocarditis requires echocardiography to confirm valvular vegetation.",
       "apply", "MGH Housestaff Manual", 122),
    kp("ie-diagnosis-2", top, dom, dis,
       "In infective endocarditis affecting the mitral valve with extensive tissue destruction, is repair or replacement preferred?",
       "Mitral valve replacement is preferred over repair when there is extensive tissue destruction from infective endocarditis",
       "Destroyed leaflet tissue cannot hold sutures reliably; replacement provides durable hemostasis.",
       "apply", "StatPearls: StatPearls   Mitral Regurgitation", 10),
    kp("ie-diagnosis-3", top, dom, dis,
       "What is the most common structural cardiac substrate for mitral valve endocarditis (myxomatous)?",
       "Mitral valve prolapse with myxomatous degeneration is the most common structural substrate for mitral IE in developed countries",
       "Redundant, degenerated leaflets create turbulent flow and platelet-fibrin nidi that bacteria can colonize.",
       "recall", "Morgan & Mikhail", 672),
]

# ── 16: Infective Endocarditis: Treatment & Surgery ─────────────────
# Chunks for this topic are about Mohs surgery prophylaxis, not IE treatment — extremely limited usable content
top = T(16); dom = D(16); dis = DI(16)
kps += [
    kp("ie-treatment-1", top, dom, dis,
       "In cutaneous surgery (including Mohs), what three categories does antibiotic prophylaxis address?",
       "Prophylaxis addresses: surgical site infection (SSI), endocarditis, and prosthetic joint infection",
       "Skin surgery carries low SSI risk; prophylaxis is reserved for high-risk cardiac conditions or prosthetic joints per AHA advisory.",
       "recall", "StatPearls: StatPearls   Infective Endocarditis  T", 3),
    kp("ie-treatment-2", top, dom, dis,
       "Which patients undergoing bloodstream-infection workup should be evaluated for endocarditis?",
       "Patients with persistent bacteremia, new murmur, embolic phenomena, or high-risk cardiac anatomy (prosthetic valve, prior IE, congenital heart disease)",
       "Persistent bacteremia despite source control is a key trigger for echocardiography to rule out valvular vegetation.",
       "apply", "MGH Housestaff Manual", 122),
    kp("ie-treatment-3", top, dom, dis,
       "What significant tricuspid valve complication is most commonly due to right ventricular dilation from pulmonary hypertension?",
       "Clinically significant tricuspid regurgitation is most commonly caused by dilation of the right ventricle from pulmonary hypertension (not primary valve disease)",
       "RV dilation displaces the papillary muscles, causing functional TR rather than structural leaflet disease.",
       "recall", "Morgan & Mikhail", 679),
]

print(f"Batch3 items: {len(kps)}")
with open('data/_kp_batch3.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("OK")
