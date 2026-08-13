import json, pathlib

entries = []

# ──────────────────────────────────────────────────────────────────────────────
# TOPIC 122: Acute Pancreatitis
# ──────────────────────────────────────────────────────────────────────────────
t = "Acute Pancreatitis"
dom = "Internal medicine: gastroenterology"
disc = "Gastroenterology"

entries += [
    {
        "id": "acute-pancreatitis-1",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "A patient presents with severe epigastric pain radiating to the back. Which category of acute pain mechanism does this represent, and what is the shared pathophysiology with renal colic?",
        "answer": "Nociceptive acute pain; both are caused by visceral distension and tissue injury activating somatic nociceptors.",
        "rationale": "Pancreatitis and renal calculi both generate nociceptive pain via tissue injury and inflammation stimulating afferent pain fibers.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 1708}],
        "confusable_with": ""
    },
    {
        "id": "acute-pancreatitis-2",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "Three days after an episode of severe abdominal inflammation with elevated lipase, a patient develops tetany and QTc prolongation. Which electrolyte disturbance explains this, and what is its mechanism?",
        "answer": "Hypocalcemia; calcium precipitates with free fatty acids (saponification) released by pancreatic lipolytic enzymes and fat necrosis.",
        "rationale": "Lipolytic enzymes released during pancreatic necrosis hydrolyze peripancreatic fat, and the resulting free fatty acids chelate ionized calcium.",
        "bloom": "analyze",
        "source": [{"book": "Morgan & Mikhail", "page": 1892}],
        "confusable_with": "hypomagnesemia (also causes tetany)"
    },
    {
        "id": "acute-pancreatitis-3",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "Among the listed causes of hypocalcemia — kidney failure, hypomagnesemia, vitamin D deficiency, and acute pancreatitis — which mechanism is unique to pancreatitis?",
        "answer": "Saponification of peripancreatic fat sequesters calcium; this mechanism is unique to pancreatitis among common hypocalcemia causes.",
        "rationale": "All other listed causes reduce calcium availability via impaired synthesis, absorption, or renal handling, not via direct chemical precipitation.",
        "bloom": "analyze",
        "source": [{"book": "Morgan & Mikhail", "page": 1232}],
        "confusable_with": ""
    },
    {
        "id": "acute-pancreatitis-4",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "A patient with severe abdominal inflammation and ileus cannot tolerate oral feeds. What is the current preferred nutritional strategy compared to historical practice?",
        "answer": "Enteral nutrition via nasojejunal or nasogastric tube is now preferred over TPN when feasible.",
        "rationale": "Enteral feeding maintains gut mucosal integrity, reduces infection risk, and avoids TPN-associated complications such as line infection and hepatic dysfunction.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 1999}],
        "confusable_with": "TPN (historical practice, still used if enteral route not tolerated)"
    },
    {
        "id": "acute-pancreatitis-5",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "Which five conditions are grouped together as common causes of acute nociceptive pain in the hospitalized patient?",
        "answer": "Trauma, surgery, labor, pancreatitis, and renal calculi.",
        "rationale": "All generate acute nociceptive pain through direct tissue injury or visceral distension activating peripheral nociceptors.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 1708}],
        "confusable_with": ""
    },
    {
        "id": "acute-pancreatitis-6",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "In a patient with acute abdominal inflammation requiring nutritional support, why was TPN historically used, and when does current practice still favor it?",
        "answer": "TPN was used because gut rest was thought beneficial; current practice still uses TPN when enteral access is not feasible or enteral feeding is not tolerated.",
        "rationale": "Gut rest dogma has been largely disproven; enteral nutrition is preferred, but TPN remains appropriate when the GI tract cannot be used safely.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 1999}],
        "confusable_with": ""
    },
    {
        "_type": "illness_script",
        "topic": t,
        "discipline": disc,
        "enabling_conditions": "Gallstones (most common), alcohol use, hypertriglyceridemia, ERCP, medications (azathioprine, thiazides), trauma.",
        "pathophysiology": "Premature activation of pancreatic enzymes within acinar cells causes autodigestion; lipases released into peripancreatic tissue hydrolyze fat, free fatty acids chelate calcium (saponification), causing hypocalcemia; systemic inflammatory response can progress to SIRS/ARDS.",
        "time_course": "Acute onset over hours; pain peaks quickly and may persist days; complications (necrosis, pseudocyst) develop over days to weeks.",
        "key_features": "Epigastric pain radiating to back, nausea/vomiting, elevated lipase/amylase (lipase more specific), hypocalcemia, tetany in severe cases.",
        "consequence_if_missed": "Progression to necrotizing pancreatitis, infected necrosis, sepsis, ARDS, multi-organ failure, and death."
    }
]

# ──────────────────────────────────────────────────────────────────────────────
# TOPIC 123: Acute Kidney Injury
# ──────────────────────────────────────────────────────────────────────────────
t = "Acute kidney injury"
dom = "General internal medicine"
disc = "General internal medicine"

entries += [
    {
        "id": "aki-1",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What three criteria define AKI, and what are the three etiologic categories used in the initial differential?",
        "answer": "AKI: Cr rise ≥0.3 mg/dL in <48 h, OR Cr ≥50% above baseline, OR UO <0.5 mL/kg/h for >6 h. Categories: prerenal, intrinsic renal, postrenal.",
        "rationale": "KDIGO criteria standardize AKI diagnosis; the prerenal/intrinsic/postrenal framework directs targeted workup and management.",
        "bloom": "recall",
        "source": [{"book": "Intern Notes / Survival Guide", "page": 43}],
        "confusable_with": ""
    },
    {
        "id": "aki-2",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "In a patient with AKI, when is FEUrea preferred over FENa for distinguishing prerenal from intrinsic causes?",
        "answer": "FEUrea is preferred when the patient is on diuretics, because diuretics artificially increase urinary sodium excretion and falsely elevate FENa.",
        "rationale": "Diuretics inhibit tubular sodium reabsorption, making FENa unreliable; urea handling is independent of loop diuretic effect.",
        "bloom": "apply",
        "source": [{"book": "Intern Notes / Survival Guide", "page": 43}],
        "confusable_with": "FENa (unreliable on diuretics)"
    },
    {
        "id": "aki-3",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What is the central principle of AKI fluid management, and why are IV fluids not always the answer?",
        "answer": "Goal is euvolemia ('a euvolemic kidney is a happy kidney'); IVF only if hypovolemic; diuretics if hypervolemic — excess fluid causes venous congestion and worsens renal perfusion.",
        "rationale": "Volume overload increases renal venous pressure, reducing the arteriovenous gradient and GFR; fluid should be titrated to euvolemia, not given reflexively.",
        "bloom": "analyze",
        "source": [{"book": "MGH Housestaff Manual", "page": 100}],
        "confusable_with": ""
    },
    {
        "id": "aki-4",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "Which four drug classes should be held or stopped in a patient with new AKI?",
        "answer": "NSAIDs, ACE inhibitors, ARBs, and IV contrast agents (also avoid high glucose).",
        "rationale": "NSAIDs and RAS inhibitors impair renal autoregulation; contrast is directly nephrotoxic; hyperglycemia exacerbates tubular injury.",
        "bloom": "recall",
        "source": [{"book": "MGH Housestaff Manual", "page": 100}],
        "confusable_with": ""
    },
    {
        "id": "aki-5",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "A patient recovering from ATN has urine specific gravity of 1.006. What does this indicate about tubular function?",
        "answer": "SG <1.010 suggests a post-ATN concentrating defect — the recovering tubules cannot yet maximally concentrate urine.",
        "rationale": "Maximal urinary concentration requires intact tubular function; SG <1.010 indicates persistent tubular dysfunction even as filtration recovers.",
        "bloom": "analyze",
        "source": [{"book": "MGH Housestaff Manual", "page": 111}],
        "confusable_with": "diabetes insipidus, diuretic effect (both also give dilute urine)"
    },
    {
        "id": "aki-6",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What five components constitute the initial evaluation of a patient with suspected AKI?",
        "answer": "History (medications, volume losses), volume status assessment, renal function panel, urinalysis, and urine microscopy (plus FENa or FEUrea).",
        "rationale": "The combination identifies the AKI category (prerenal: bland UA + low FENa; intrinsic: casts on microscopy; postrenal: hydronephrosis on imaging).",
        "bloom": "recall",
        "source": [{"book": "Intern Notes / Survival Guide", "page": 43}],
        "confusable_with": ""
    }
]

# ──────────────────────────────────────────────────────────────────────────────
# TOPIC 124: Anemia of Chronic Disease / Inflammation
# ──────────────────────────────────────────────────────────────────────────────
t = "Anemia of chronic disease / inflammation"
dom = "Internal medicine: hematology & oncology"
disc = "Hematology"

entries += [
    {
        "id": "aci-1",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "A patient with rheumatoid arthritis has a normocytic anemia with low serum iron and low TIBC but elevated ferritin. What is the diagnosis and what does 'functional iron deficiency' mean in this context?",
        "answer": "Anemia of inflammation (ACI); functional iron deficiency means sufficient total body iron exists but is unavailable for erythropoiesis due to sequestration (hepcidin-mediated).",
        "rationale": "Inflammatory cytokines upregulate hepcidin, which blocks ferroportin-mediated iron release from macrophages and enterocytes, restricting iron supply to erythroid precursors.",
        "bloom": "analyze",
        "source": [{"book": "Miller/Baby Miller", "page": 780}],
        "confusable_with": "iron deficiency anemia (low ferritin, high TIBC)"
    },
    {
        "id": "aci-2",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "Can absolute iron deficiency coexist with anemia of inflammation, and how does this complicate interpretation of iron studies?",
        "answer": "Yes; absolute iron deficiency can coexist with ACI. Ferritin may be falsely elevated by inflammation, masking true iron depletion.",
        "rationale": "Ferritin is an acute-phase reactant; inflammation raises ferritin even when iron stores are depleted, so ferritin alone is unreliable in inflammatory states.",
        "bloom": "analyze",
        "source": [{"book": "Miller/Baby Miller", "page": 780}],
        "confusable_with": "isolated IDA"
    },
    {
        "id": "aci-3",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What are the three main causes of iron deficiency anemia by mechanism category?",
        "answer": "Increased loss (chronic GI bleeding, menses, hemolysis), increased demand (pregnancy, EPO therapy, blood donation), and decreased intake/absorption.",
        "rationale": "IDA requires a negative iron balance from any combination of these three mechanisms; identifying the category guides treatment.",
        "bloom": "recall",
        "source": [{"book": "MGH Housestaff Manual", "page": 137}],
        "confusable_with": "ACI (sequestration, not loss)"
    },
    {
        "id": "aci-4",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "A patient with a chronic systemic inflammatory disease develops anemia. What iron study pattern distinguishes ACI from coexisting absolute iron deficiency?",
        "answer": "ACI: low serum iron, low TIBC, ferritin normal or high. Absolute IDA superimposed on ACI: very low ferritin (<30 ng/mL) or soluble transferrin receptor elevation despite elevated ferritin.",
        "rationale": "TIBC falls in ACI (inflammation reduces transferrin synthesis) but rises in IDA; soluble transferrin receptor is not an acute-phase reactant and rises with true iron depletion.",
        "bloom": "analyze",
        "source": [{"book": "Miller/Baby Miller", "page": 780}],
        "confusable_with": "IDA alone"
    },
    {
        "id": "aci-5",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "A patient with anemia has pancytopenia. What four disease categories must be considered in the differential?",
        "answer": "Viral infections, bone marrow infiltration (leukemia, MPN, MDS, metastases), bone marrow failure (B12/folate deficiency), and aplastic anemia.",
        "rationale": "Pancytopenia implies a global marrow process or suppression; targeted evaluation distinguishes inflammatory causes from primary marrow pathology.",
        "bloom": "recall",
        "source": [{"book": "MGH Housestaff Manual", "page": 136}],
        "confusable_with": ""
    },
    {
        "id": "aci-6",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "Why is ACI also called 'anemia of chronic disease', and what distinguishes its erythrocyte morphology from that of IDA?",
        "answer": "It is called anemia of chronic disease because it arises in the setting of chronic inflammatory, infectious, or neoplastic conditions; morphology is normocytic/normochromic (vs. microcytic/hypochromic in IDA).",
        "rationale": "Hepcidin-mediated iron restriction reduces hemoglobin synthesis only modestly in ACI, producing normochromic cells, unlike the severe iron restriction in IDA.",
        "bloom": "apply",
        "source": [{"book": "Miller/Baby Miller", "page": 780}],
        "confusable_with": "IDA (microcytic/hypochromic)"
    },
    {
        "_type": "illness_script",
        "topic": t,
        "discipline": disc,
        "enabling_conditions": "Chronic inflammation (RA, SLE, IBD, CKD), chronic infection (TB, endocarditis), malignancy.",
        "pathophysiology": "Inflammatory cytokines (IL-6) upregulate hepatic hepcidin → blocks ferroportin → iron sequestered in macrophages and enterocytes → functional iron deficiency → reduced erythropoiesis; EPO production also blunted by cytokines.",
        "time_course": "Develops weeks to months after onset of underlying inflammatory condition; slowly progressive.",
        "key_features": "Normocytic/normochromic anemia, low serum iron, low TIBC, normal or elevated ferritin, elevated inflammatory markers (ESR, CRP).",
        "consequence_if_missed": "Untreated underlying disease worsens anemia; unnecessary iron supplementation may cause iron overload if absolute IDA not confirmed."
    },
    {
        "_type": "confusable_pair",
        "topic_a": "Anemia of chronic disease / inflammation",
        "topic_b": "Iron deficiency anemia",
        "discriminator": "ACI: low serum iron + low TIBC + normal/high ferritin + normocytic cells. IDA: low serum iron + HIGH TIBC + LOW ferritin + microcytic/hypochromic cells. Both can coexist — soluble transferrin receptor elevated in IDA but not ACI alone."
    }
]

# ──────────────────────────────────────────────────────────────────────────────
# TOPIC 125: Anticoagulants: mechanisms, dosing, and monitoring
# ──────────────────────────────────────────────────────────────────────────────
t = "Anticoagulants: mechanisms, dosing, and monitoring"
dom = "Internal medicine: hematology & oncology"
disc = "Hematology"

entries += [
    {
        "id": "anticoag-mech-1",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What is the recommended anticoagulant agent and route for DVT prophylaxis in a patient with normal bleeding risk who cannot receive oral anticoagulation?",
        "answer": "Low-dose subcutaneous unfractionated heparin.",
        "rationale": "Subcutaneous UFH at prophylactic doses inhibits thrombin and factor Xa indirectly via antithrombin without requiring laboratory monitoring in most patients.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 1299}],
        "confusable_with": "therapeutic heparin (requires monitoring)"
    },
    {
        "id": "anticoag-mech-2",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "A patient on argatroban (a direct thrombin inhibitor) requires bridging to warfarin. Why is the INR unreliable in this setting?",
        "answer": "All DTIs interfere with INR measurement; argatroban specifically prolongs the PT/INR, making it impossible to distinguish DTI effect from warfarin anticoagulation by INR alone.",
        "rationale": "Direct thrombin inhibition affects the extrinsic pathway, which is the basis of PT/INR measurement, creating a false elevation above the true warfarin effect.",
        "bloom": "analyze",
        "source": [{"book": "Miller/Baby Miller", "page": 454}],
        "confusable_with": "warfarin supratherapeutic effect"
    },
    {
        "id": "anticoag-mech-3",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "A patient on a direct thrombin inhibitor develops major bleeding. What is the reversal strategy?",
        "answer": "There are no specific antidotes for DTIs; reversal depends on clearance of the drug (hold the agent, support with time).",
        "rationale": "Unlike heparin (protamine) or warfarin (vitamin K/FFP/4F-PCC), DTIs lack approved reversal agents and must be cleared renally or hepatically.",
        "bloom": "recall",
        "source": [{"book": "Miller/Baby Miller", "page": 454}],
        "confusable_with": "factor Xa inhibitor (andexanet alfa available)"
    },
    {
        "id": "anticoag-mech-4",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "Which two cardiac conditions mandate warfarin (VKA) and CANNOT be anticoagulated with DOACs in AF?",
        "answer": "AF with moderate-to-severe rheumatic mitral stenosis and AF with mechanical heart valves.",
        "rationale": "Randomized trial (RE-ALIGN) showed dabigatran inferior to warfarin in mechanical valves; rheumatic mitral stenosis was excluded from DOAC AF trials.",
        "bloom": "recall",
        "source": [{"book": "ACC AHA 2023 AF", "page": 33}],
        "confusable_with": "non-valvular AF (DOACs preferred)"
    },
    {
        "id": "anticoag-mech-5",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What target INR range is used for warfarin therapy in AF with rheumatic mitral stenosis, and above what INR does bleeding risk increase significantly?",
        "answer": "Target INR 2–3; bleeding risk increases significantly above INR 3.",
        "rationale": "The therapeutic window balances stroke prevention (INR ≥2) against hemorrhagic risk (INR >3); values outside 2–3 sharply shift the risk-benefit ratio.",
        "bloom": "recall",
        "source": [{"book": "ACC AHA 2023 AF", "page": 33}],
        "confusable_with": "mechanical valve targets (some require INR 2.5–3.5)"
    },
    {
        "id": "anticoag-mech-6",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "How does the PT/INR interference of argatroban differ from that of other DTIs, and what practical consequence does this have when transitioning to warfarin?",
        "answer": "Argatroban prolongs INR more than other DTIs; the transition to warfarin requires a specific correction formula or chromogenic factor X assay to estimate true warfarin effect.",
        "rationale": "Without correction, the inflated INR may cause premature discontinuation of argatroban before adequate warfarin anticoagulation is achieved, risking thrombosis.",
        "bloom": "analyze",
        "source": [{"book": "Miller/Baby Miller", "page": 454}],
        "confusable_with": ""
    },
    {
        "_type": "confusable_pair",
        "topic_a": "Direct thrombin inhibitor (DTI) monitoring",
        "topic_b": "Factor Xa inhibitor monitoring",
        "discriminator": "DTIs: no approved reversal agents; all interfere with INR; monitored by aPTT or ECT. Factor Xa inhibitors: andexanet alfa is the reversal agent; do NOT significantly interfere with INR; can be measured by anti-Xa activity assay."
    }
]

# ──────────────────────────────────────────────────────────────────────────────
# TOPIC 126: Anticoagulation Reversal
# ──────────────────────────────────────────────────────────────────────────────
t = "Anticoagulation reversal"
dom = "Internal medicine: hematology & oncology"
disc = "Hematology"

entries += [
    {
        "id": "anticoag-reversal-1",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What laboratory test monitors heparin anticoagulation during cardiopulmonary bypass, and what does it measure?",
        "answer": "Activated clotting time (ACT); it is plotted against heparin dose to establish the dose-response curve for each patient.",
        "rationale": "ACT provides real-time point-of-care measurement of total anticoagulation effect during CPB, where standard aPTT is too slow and impractical.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 744}],
        "confusable_with": "aPTT (used for heparin monitoring outside CPB)"
    },
    {
        "id": "anticoag-reversal-2",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "After CPB, if unwashed pump reservoir blood is administered, what supplemental dose of protamine may be considered?",
        "answer": "Supplemental protamine 50–100 mg.",
        "rationale": "Pump reservoir blood contains residual heparin; additional protamine is needed to neutralize this heparin and avoid post-bypass coagulopathy.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 755}],
        "confusable_with": "initial protamine dose (weight-based, given post-bypass)"
    },
    {
        "id": "anticoag-reversal-3",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "Why must heparin be administered before initiating cardiopulmonary bypass?",
        "answer": "To prevent acute DIC; contact of blood with the CPB circuit without adequate anticoagulation triggers the coagulation cascade and consumes clotting factors.",
        "rationale": "Exposure of blood to the artificial CPB circuit surface activates the extrinsic and contact pathways; without heparin, widespread fibrin formation rapidly depletes clotting factors.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 707}],
        "confusable_with": ""
    },
    {
        "id": "anticoag-reversal-4",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What is the relationship between the ACT value and the heparin dose-response curve, and why is an individualized curve preferred over a fixed dose?",
        "answer": "ACT is plotted against heparin dose for each patient; individual variation in response means a fixed dose may be inadequate or excessive without the curve.",
        "rationale": "Heparin sensitivity varies due to antithrombin III levels, acute-phase protein binding, and other factors; the curve identifies the minimum dose to reach target ACT.",
        "bloom": "analyze",
        "source": [{"book": "Morgan & Mikhail", "page": 744}],
        "confusable_with": ""
    },
    {
        "id": "anticoag-reversal-5",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What is the consequence of inadequate heparin anticoagulation at the start of CPB, and what specific coagulopathy results?",
        "answer": "Acute disseminated intravascular coagulation (DIC) with consumption of clotting factors and platelets.",
        "rationale": "Uncontrolled thrombin generation within the circuit triggers systemic fibrin deposition and factor consumption, leading to simultaneous thrombosis and bleeding.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 707}],
        "confusable_with": ""
    }
]

# ──────────────────────────────────────────────────────────────────────────────
# TOPIC 127: Antithrombotic Therapy and Management of Bleeding
# ──────────────────────────────────────────────────────────────────────────────
t = "Antithrombotic Therapy and Management of Bleeding"
dom = "Internal medicine: cardiology"
disc = "Cardiology"

entries += [
    {
        "id": "antithrombotic-1",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "When planning anticoagulation cessation before a procedure, what two drug properties must guide the duration of interruption?",
        "answer": "Both pharmacokinetics (half-life, clearance) AND pharmacodynamics (residual anticoagulant effect at target organ) must be considered.",
        "rationale": "A drug may have a short half-life but residual platelet or coagulation factor inhibition beyond what PK alone predicts; ignoring PD leads to either underirrigation of the clot or excess procedural bleeding.",
        "bloom": "analyze",
        "source": [{"book": "ACC AHA 2023 AF", "page": 52}],
        "confusable_with": ""
    },
    {
        "id": "antithrombotic-2",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "In AF patients post-PCI who require both anticoagulation and antiplatelet therapy, which regimen reduces clinically relevant bleeding compared to triple therapy?",
        "answer": "Dual therapy (OAC + P2Y12 inhibitor alone, without aspirin) significantly lowers clinically relevant bleeding risk versus triple therapy.",
        "rationale": "Adding aspirin to OAC + P2Y12 provides minimal additional thrombotic protection after stenting but substantially increases major bleeding events.",
        "bloom": "recall",
        "source": [{"book": "ACC AHA 2023 AF", "page": 53}],
        "confusable_with": "triple therapy (OAC + aspirin + P2Y12)"
    },
    {
        "id": "antithrombotic-3",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What is the reversal agent for major bleeding associated with factor Xa inhibitors (e.g., rivaroxaban, apixaban)?",
        "answer": "Andexanet alfa.",
        "rationale": "Andexanet alfa is a modified factor Xa decoy that binds and sequesters factor Xa inhibitors, rapidly reversing anticoagulant activity.",
        "bloom": "recall",
        "source": [{"book": "ACC AHA 2023 AF", "page": 127}],
        "confusable_with": "idarucizumab (reversal for dabigatran, a DTI)"
    },
    {
        "id": "antithrombotic-4",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What is the reversal strategy for major bleeding with a direct thrombin inhibitor such as dabigatran vs. a factor Xa inhibitor?",
        "answer": "DTIs (e.g., dabigatran): idarucizumab is the specific reversal agent. Factor Xa inhibitors: andexanet alfa. Older DTIs (argatroban, bivalirudin): no specific antidote, rely on drug clearance.",
        "rationale": "Each anticoagulant class has a distinct mechanism requiring class-specific reversal; DTIs bind thrombin directly, and idarucizumab is a monoclonal antibody fragment that sequesters dabigatran.",
        "bloom": "apply",
        "source": [{"book": "Miller/Baby Miller", "page": 454}, {"book": "ACC AHA 2023 AF", "page": 127}],
        "confusable_with": "andexanet alfa (only for factor Xa inhibitors)"
    },
    {
        "id": "antithrombotic-5",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "Why does perioperative antithrombotic management require a multidisciplinary team approach?",
        "answer": "Decisions require integrating thrombotic risk (indication for anticoagulation), bleeding risk (surgery type), drug pharmacology, and patient comorbidities — expertise spanning hematology, cardiology, and surgery.",
        "rationale": "No single specialist has full domain over all these dimensions; bridging decisions, timing of restart, and choice of agent require coordinated input to prevent both thrombosis and major bleeding.",
        "bloom": "apply",
        "source": [{"book": "Miller/Baby Miller", "page": 456}],
        "confusable_with": ""
    },
    {
        "id": "antithrombotic-6",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What does 'clinically relevant bleeding' include in trials comparing dual vs. triple antithrombotic therapy?",
        "answer": "Major bleeding plus minor non-TIMI-major bleeding that requires medical attention (e.g., GI bleeding, access site complications, significant bruising requiring evaluation).",
        "rationale": "Regulatory and trial definitions use 'clinically relevant non-major bleeding' to capture events below the threshold of ISTH major bleeding that still impact patient outcomes and require intervention.",
        "bloom": "recall",
        "source": [{"book": "ACC AHA 2023 AF", "page": 53}],
        "confusable_with": "TIMI major bleeding (narrower definition)"
    },
    {
        "id": "antithrombotic-7",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "When stopping an anticoagulant before surgery, is it sufficient to simply calculate five half-lives?",
        "answer": "No; the duration must account for both pharmacokinetics AND pharmacodynamics — residual anticoagulant effect may persist beyond what the half-life alone predicts.",
        "rationale": "Some anticoagulants have pharmacodynamic effects (e.g., irreversible platelet inhibition or residual anti-Xa activity) that outlast their measured plasma half-life.",
        "bloom": "analyze",
        "source": [{"book": "ACC AHA 2023 AF", "page": 52}],
        "confusable_with": ""
    }
]

# ──────────────────────────────────────────────────────────────────────────────
# TOPIC 128: Ascites in Cirrhosis
# ──────────────────────────────────────────────────────────────────────────────
t = "Ascites in Cirrhosis"
dom = "Internal medicine: gastroenterology"
disc = "Gastroenterology"

entries += [
    {
        "id": "ascites-cirrhosis-1",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What is the 1-year and 5-year mortality after first development of ascites in a cirrhotic patient?",
        "answer": "Approximately 15% at 1 year and 44% at 5 years.",
        "rationale": "Development of ascites marks the transition from compensated to decompensated cirrhosis and dramatically worsens prognosis.",
        "bloom": "recall",
        "source": [{"book": "MGH Housestaff Manual", "page": 94}],
        "confusable_with": ""
    },
    {
        "id": "ascites-cirrhosis-2",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What portal pressure threshold triggers splanchnic vasodilation in cirrhosis, and which two vasodilatory mediators are principally involved?",
        "answer": "Portal pressure >12 mmHg; mediators: nitric oxide (NO) and prostaglandins.",
        "rationale": "Portal hypertension ≥12 mmHg activates local production of NO and prostaglandins in the splanchnic bed, causing vasodilation, hyperdynamic circulation, and sodium/water retention.",
        "bloom": "analyze",
        "source": [{"book": "MGH Housestaff Manual", "page": 94}],
        "confusable_with": ""
    },
    {
        "id": "ascites-cirrhosis-3",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What four clinical features define compensated cirrhosis, and why is the distinction from decompensated disease prognostically important?",
        "answer": "Compensated cirrhosis = absence of ascites, hepatic encephalopathy, jaundice, and GI bleeding. Decompensation marks significantly worse survival and guides management urgency.",
        "rationale": "Compensated patients have better-preserved hepatic function and lower portal pressures; each decompensating event (especially ascites) marks a step-wise worsening of prognosis.",
        "bloom": "recall",
        "source": [{"book": "MGH Housestaff Manual", "page": 93}],
        "confusable_with": ""
    },
    {
        "id": "ascites-cirrhosis-4",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What is the first-line medical management of uncomplicated cirrhotic ascites?",
        "answer": "Sodium restriction plus diuretics (typically spironolactone ± furosemide).",
        "rationale": "Sodium retention drives ascites formation; aldosterone antagonism (spironolactone) targets the primary mechanism, augmented by loop diuretics for additional sodium excretion.",
        "bloom": "recall",
        "source": [{"book": "Miller/Baby Miller", "page": 533}],
        "confusable_with": ""
    },
    {
        "id": "ascites-cirrhosis-5",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "When is abdominal paracentesis indicated in the management of cirrhotic ascites?",
        "answer": "For tense or refractory ascites not controlled by sodium restriction and diuretics.",
        "rationale": "Large-volume paracentesis rapidly relieves respiratory compromise and abdominal pain; albumin replacement is given for large-volume taps (>5L) to prevent paracentesis-induced circulatory dysfunction.",
        "bloom": "recall",
        "source": [{"book": "Miller/Baby Miller", "page": 533}],
        "confusable_with": ""
    },
    {
        "id": "ascites-cirrhosis-6",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What scoring system predicts 90-day mortality in cirrhosis and guides liver transplant listing priority?",
        "answer": "MELD score (Model for End-stage Liver Disease).",
        "rationale": "MELD uses bilirubin, creatinine, and INR to objectively quantify hepatic synthetic and renal function; higher scores predict greater 90-day mortality and priority for transplantation.",
        "bloom": "recall",
        "source": [{"book": "Miller/Baby Miller", "page": 534}],
        "confusable_with": "Child-Pugh score (used for surgical risk stratification)"
    },
    {
        "id": "ascites-cirrhosis-7",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "In which Child-Pugh class is elective surgery generally avoided, and why?",
        "answer": "Decompensated Child-Pugh class C; perioperative mortality is prohibitively high (>50%) due to severely impaired synthetic function, coagulopathy, and inability to tolerate the metabolic stress of surgery.",
        "rationale": "Child-Pugh C indicates severe hepatic dysfunction; anesthesia and surgical stress further reduce hepatic blood flow and synthetic capacity, precipitating liver failure.",
        "bloom": "apply",
        "source": [{"book": "Miller/Baby Miller", "page": 534}],
        "confusable_with": "Child-Pugh B (intermediate risk, case-by-case)"
    },
    {
        "_type": "illness_script",
        "topic": t,
        "discipline": disc,
        "enabling_conditions": "Advanced cirrhosis (any etiology: alcohol, NASH, viral hepatitis); portal pressure >12 mmHg.",
        "pathophysiology": "Portal hypertension → splanchnic NO/prostaglandin-mediated vasodilation → effective arterial underfilling → RAAS and SNS activation → renal sodium and water retention → fluid accumulates in peritoneal cavity.",
        "time_course": "Develops over months to years in compensated cirrhosis; acute decompensation can occur with precipitants (GI bleed, infection, alcohol binge).",
        "key_features": "Abdominal distension, shifting dullness, fluid wave, low serum albumin, elevated bilirubin, coagulopathy; SAAG ≥1.1 g/dL confirms portal hypertension.",
        "consequence_if_missed": "Spontaneous bacterial peritonitis (SBP), hepatorenal syndrome, respiratory compromise, sepsis, and death."
    }
]

# ──────────────────────────────────────────────────────────────────────────────
# TOPIC 129: Atrial Fibrillation and Atrial Flutter
# ──────────────────────────────────────────────────────────────────────────────
t = "Atrial Fibrillation and Atrial Flutter"
dom = "Internal medicine: cardiology"
disc = "Cardiology"

entries += [
    {
        "id": "af-1",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "List six modifiable and non-modifiable risk factors for atrial fibrillation.",
        "answer": "Age (non-modifiable), obesity, hypertension, smoking, alcohol use, diabetes mellitus, prior MI, heart failure, and obstructive sleep apnea.",
        "rationale": "These risk factors cause atrial structural and electrical remodeling (fibrosis, stretch) that creates the substrate for AF initiation and maintenance.",
        "bloom": "recall",
        "source": [{"book": "MGH Housestaff Manual", "page": 13}],
        "confusable_with": ""
    },
    {
        "id": "af-2",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "A patient has a second episode of AF after successful cardioversion. Which non-cardiac precipitants should be investigated to reduce recurrence?",
        "answer": "Surgery, systemic infection, and acute MI — AF recurs in the majority of patients due to identifiable secondary precipitants.",
        "rationale": "Treating the underlying precipitant reduces arrhythmia burden; persistent AF despite treating precipitants indicates structural or electrical substrate requiring long-term therapy.",
        "bloom": "apply",
        "source": [{"book": "MGH Housestaff Manual", "page": 13}],
        "confusable_with": ""
    },
    {
        "id": "af-3",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "Which two valvular/structural cardiac conditions require VKA (warfarin) for AF anticoagulation rather than DOACs?",
        "answer": "AF with moderate-to-severe rheumatic mitral stenosis and AF in patients with mechanical heart valves.",
        "rationale": "DOACs have not been validated in these conditions; randomized evidence shows inferiority in mechanical valves (RE-ALIGN trial), and rheumatic MS was excluded from all major DOAC AF trials.",
        "bloom": "recall",
        "source": [{"book": "ACC AHA 2023 AF", "page": 33}],
        "confusable_with": "non-valvular AF (DOACs preferred)"
    },
    {
        "id": "af-4",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "In a patient with AF who has undergone PCI, what antiplatelet regimen combined with OAC minimizes bleeding while preserving ischemic protection?",
        "answer": "Dual therapy: OAC + single P2Y12 inhibitor (without aspirin) — significantly lower clinically relevant bleeding than triple therapy.",
        "rationale": "Aspirin adds minimal thrombotic benefit post-stenting in patients already on OAC + P2Y12 inhibitor but substantially increases GI and other major bleeding.",
        "bloom": "apply",
        "source": [{"book": "ACC AHA 2023 AF", "page": 53}],
        "confusable_with": "triple therapy (higher bleeding risk)"
    },
    {
        "id": "af-5",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What is the mortality risk associated with sotalol use for AF rhythm control based on meta-analysis data?",
        "answer": "Sotalol is associated with increased all-cause mortality (relative risk 2.23) compared to placebo in Cochrane meta-analysis.",
        "rationale": "Sotalol's class III effects (QTc prolongation) and class II (beta-blockade) combined with proarrhythmic risk (torsades de pointes) drive excess mortality in AF rhythm control.",
        "bloom": "recall",
        "source": [{"book": "ACC AHA 2023 AF", "page": 77}],
        "confusable_with": "amiodarone (higher efficacy, different risk profile)"
    },
    {
        "id": "af-6",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What INR range is targeted for warfarin anticoagulation in AF with rheumatic mitral stenosis, and what clinical event risk rises sharply above this range?",
        "answer": "Target INR 2–3; bleeding risk increases significantly above INR 3.",
        "rationale": "Values below 2 risk cardioembolic stroke; values above 3 risk intracranial and major systemic hemorrhage, narrowing the therapeutic window.",
        "bloom": "recall",
        "source": [{"book": "ACC AHA 2023 AF", "page": 33}],
        "confusable_with": ""
    },
    {
        "id": "af-7",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "A patient with persistent AF has a history of moderate rheumatic mitral stenosis. Her physician considers switching to apixaban. Is this appropriate, and why?",
        "answer": "No; rheumatic mitral stenosis with AF requires warfarin (VKA). DOACs are not approved or proven safe in this condition.",
        "rationale": "Moderate-to-severe rheumatic MS with AF carries high thromboembolic risk driven by stasis in the obstructed left atrium; only VKA has evidence and regulatory approval.",
        "bloom": "apply",
        "source": [{"book": "ACC AHA 2023 AF", "page": 33}],
        "confusable_with": "non-valvular AF (DOACs are first-line)"
    },
    {
        "_type": "illness_script",
        "topic": t,
        "discipline": disc,
        "enabling_conditions": "Age, hypertension, obesity, OSA, diabetes, prior MI, heart failure, alcohol use, surgery, infection, hyperthyroidism.",
        "pathophysiology": "Disorganized rapid atrial electrical activity (>350 bpm) → loss of coordinated atrial contraction → blood stasis in left atrial appendage → thrombus formation → cardioembolism; rapid ventricular rate → tachycardia-mediated cardiomyopathy if untreated.",
        "time_course": "Paroxysmal (<7 days, self-terminating), persistent (>7 days), or permanent; each episode increases structural remodeling risk.",
        "key_features": "Irregular irregular pulse, palpitations, dyspnea, fatigue; ECG shows absent P waves with irregularly irregular RR intervals.",
        "consequence_if_missed": "Ischemic stroke (5× baseline risk), systemic embolism, tachycardia-mediated cardiomyopathy, hemodynamic compromise."
    }
]

# ──────────────────────────────────────────────────────────────────────────────
# TOPIC 130: Atrial Fibrillation: Inpatient Management
# ──────────────────────────────────────────────────────────────────────────────
t = "Atrial fibrillation: inpatient management"
dom = "General internal medicine"
disc = "General internal medicine"

entries += [
    {
        "id": "af-inpatient-1",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "A patient develops new AF on post-operative day 1. What three secondary precipitants should be evaluated and corrected before escalating rhythm control therapy?",
        "answer": "Surgery/pain, systemic infection, and myocardial ischemia (MI) — addressing these precipitants alone often terminates the arrhythmia.",
        "rationale": "Secondary precipitants are responsible for the majority of inpatient AF episodes; treating the cause avoids unnecessary antiarrhythmic drug exposure.",
        "bloom": "apply",
        "source": [{"book": "MGH Housestaff Manual", "page": 13}],
        "confusable_with": ""
    },
    {
        "id": "af-inpatient-2",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What biomarker level helps distinguish cardiac from non-cardiac causes of acute dyspnea when a patient with new AF presents in respiratory distress?",
        "answer": "BNP (B-type natriuretic peptide); elevation distinguishes heart failure from other causes of dyspnea.",
        "rationale": "BNP is released from ventricular myocytes in response to volume overload and wall stress; elevation points to a cardiac cause (HF or tachycardia-mediated cardiomyopathy) rather than pulmonary or other etiologies.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 659}],
        "confusable_with": "troponin (myocardial injury, not volume overload)"
    },
    {
        "id": "af-inpatient-3",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "In inpatient AF management associated with heart failure, what special considerations affect rate and rhythm control decisions?",
        "answer": "HF reduces tolerance for negative inotropes; rate control agents with negative inotropy (beta-blockers, non-dihydropyridine CCBs) may worsen HF; amiodarone is often preferred for rhythm control in HF with reduced EF.",
        "rationale": "HFrEF already has impaired contractility; adding negative inotropes precipitates acute decompensation; amiodarone has minimal negative inotropy compared to other antiarrhythmics.",
        "bloom": "analyze",
        "source": [{"book": "ACC AHA 2023 AF", "page": 92}],
        "confusable_with": ""
    },
    {
        "id": "af-inpatient-4",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "A patient in the ICU with new AF is found to have an elevated BNP and worsening respiratory status. How does BNP elevation change the immediate management priority?",
        "answer": "Elevated BNP suggests volume overload/HF as precipitant or consequence; diuresis should be added to rate control, and aggressive volume resuscitation should be avoided.",
        "rationale": "BNP-guided management prevents the error of attributing dyspnea to the AF alone while missing underlying HF requiring diuresis.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 659}],
        "confusable_with": ""
    },
    {
        "id": "af-inpatient-5",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What is the expected recurrence rate of AF in hospitalized patients who convert to sinus rhythm, and what is the implication for discharge planning?",
        "answer": "AF recurs in the majority of patients; most require ongoing rate or rhythm control therapy and anticoagulation planning at discharge.",
        "rationale": "The high recurrence rate reflects persistent substrate (structural remodeling, ongoing precipitants); single-episode cardioversion without long-term management leads to predictable relapse.",
        "bloom": "recall",
        "source": [{"book": "MGH Housestaff Manual", "page": 13}],
        "confusable_with": ""
    }
]

# ──────────────────────────────────────────────────────────────────────────────
# TOPIC 131: COPD: Acute Exacerbations
# ──────────────────────────────────────────────────────────────────────────────
t = "COPD: Acute Exacerbations"
dom = "Internal medicine: pulmonology"
disc = "Pulmonology"

entries += [
    {
        "id": "copd-aecopd-1",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "In an acute COPD exacerbation, is a nebulizer superior to a pressurized metered-dose inhaler with spacer for bronchodilator delivery?",
        "answer": "No; nebulizer and pMDI with spacer have equivalent efficacy for bronchodilator delivery in acute COPD exacerbations.",
        "rationale": "Randomized trials show equivalent bronchodilation and clinical outcomes; pMDI + spacer is preferred when feasible due to lower infection risk and cost.",
        "bloom": "recall",
        "source": [{"book": "GOLD 2024 COPD", "page": 200}],
        "confusable_with": ""
    },
    {
        "id": "copd-aecopd-2",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What level of evidence supports early NIV use for acute COPD exacerbations on general respiratory wards, and what outcome benefit was demonstrated?",
        "answer": "Multicenter RCT evidence (Plant et al.) supports early NIV on general respiratory wards; benefit: reduced mortality.",
        "rationale": "NIV reduces the work of breathing, improves gas exchange, and avoids intubation; randomized evidence from general ward settings shows mortality benefit, not just ICU benefit.",
        "bloom": "recall",
        "source": [{"book": "GOLD 2024 COPD", "page": 203}],
        "confusable_with": "invasive mechanical ventilation (higher morbidity, last resort)"
    },
    {
        "id": "copd-aecopd-3",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What rare opportunistic fungal infection should be considered in a COPD patient with acute exacerbation who fails to respond to standard antibiotics and steroids?",
        "answer": "Invasive pulmonary aspergillosis (IPA).",
        "rationale": "COPD patients are at risk for IPA due to impaired airway defenses and frequent systemic corticosteroid use; failure of standard AECOPD treatment should prompt bronchoscopy and galactomannan testing.",
        "bloom": "apply",
        "source": [{"book": "GOLD 2024 COPD", "page": 199}],
        "confusable_with": "bacterial pneumonia (most common AECOPD precipitant)"
    },
    {
        "id": "copd-aecopd-4",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "For a COPD exacerbation patient in respiratory distress, what are the two key clinical criteria indicating a need to escalate to NIV?",
        "answer": "Acute hypercapnic respiratory failure (elevated PaCO2 with acidosis, pH <7.35) and increased work of breathing (accessory muscle use, respiratory rate >25/min) despite maximal medical therapy.",
        "rationale": "NIV is most beneficial in hypercapnic AECOPD with respiratory acidosis; it offloads respiratory muscles and improves CO2 clearance without the risks of intubation.",
        "bloom": "apply",
        "source": [{"book": "GOLD 2024 COPD", "page": 203}],
        "confusable_with": ""
    },
    {
        "id": "copd-aecopd-5",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "In terms of bronchodilator delivery during an acute COPD exacerbation requiring hospitalization, when is a nebulizer preferred over pMDI + spacer?",
        "answer": "When the patient cannot coordinate pMDI technique due to severe dyspnea, altered mental status, or inability to use an inhaler device correctly.",
        "rationale": "Both devices are therapeutically equivalent when used correctly; the nebulizer removes the coordination barrier, making it preferable in patients unable to use pMDI appropriately.",
        "bloom": "apply",
        "source": [{"book": "GOLD 2024 COPD", "page": 200}],
        "confusable_with": ""
    }
]

# ──────────────────────────────────────────────────────────────────────────────
# TOPIC 132: Cardiac Biomarkers and Diagnostic Testing
# ──────────────────────────────────────────────────────────────────────────────
t = "Cardiac Biomarkers and Diagnostic Testing"
dom = "Internal medicine: cardiology"
disc = "Cardiology"

entries += [
    {
        "id": "cardiac-biomarkers-1",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What are the detection window, peak, and main limitation of myoglobin as a cardiac biomarker after myocardial infarction?",
        "answer": "Detected 1 hour after MI, peaks 4–12 hours, returns to baseline quickly; main limitation is lack of cardiac specificity.",
        "rationale": "Myoglobin rises early but is also released from skeletal muscle, producing false positives in muscle trauma, renal failure, or intense exercise.",
        "bloom": "recall",
        "source": [{"book": "StatPearls Cardiac Biomarkers", "page": 3}],
        "confusable_with": "troponin (cardiac-specific, slower rise)"
    },
    {
        "id": "cardiac-biomarkers-2",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "According to the 2007 World Task Force definition, what constitutes a positive troponin result for AMI diagnosis?",
        "answer": "At least one troponin value above the 99th percentile of a healthy reference population, supported by signs or symptoms of ischemia.",
        "rationale": "The 99th percentile threshold distinguishes AMI from incidental troponin release; clinical context (symptoms, ECG) must accompany the biomarker for AMI diagnosis.",
        "bloom": "recall",
        "source": [{"book": "StatPearls Cardiac Biomarkers", "page": 4}],
        "confusable_with": "any troponin elevation (many non-ischemic causes also elevate troponin)"
    },
    {
        "id": "cardiac-biomarkers-3",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "Why are cardiac troponins (I and T) preferred over CK-MB and myoglobin for AMI evaluation?",
        "answer": "Cardiac troponins are the most specific and sensitive biomarkers for AMI, providing superior cardiac specificity and a wider diagnostic window.",
        "rationale": "Cardiac-specific troponin isoforms are not present in non-cardiac muscle, conferring high specificity; high-sensitivity assays detect myocardial injury within 1–3 hours of onset.",
        "bloom": "recall",
        "source": [{"book": "StatPearls Cardiac Biomarkers", "page": 6}],
        "confusable_with": "CK-MB (less cardiac-specific, shorter window)"
    },
    {
        "id": "cardiac-biomarkers-4",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What is the role of elevated natriuretic peptide levels (BNP or NT-proBNP) in the diagnosis of heart failure?",
        "answer": "Elevated BNP/NT-proBNP corroborates the clinical diagnosis of heart failure; they support but do not replace clinical assessment.",
        "rationale": "Natriuretic peptides are released from ventricular myocytes in response to increased wall stress and volume overload; they have high negative predictive value (low levels effectively rule out HF).",
        "bloom": "recall",
        "source": [{"book": "Miller/Baby Miller", "page": 493}],
        "confusable_with": "troponin (myocardial injury, not volume overload)"
    },
    {
        "id": "cardiac-biomarkers-5",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What does NT-proBNP reduction during hospitalization for acute decompensated heart failure predict?",
        "answer": "Reduction in NT-proBNP during the ADHF admission predicts lower long-term cardiovascular mortality.",
        "rationale": "NT-proBNP trajectory reflects the degree of decongestion achieved; failure to reduce NT-proBNP signals inadequate treatment and predicts poor outcomes.",
        "bloom": "apply",
        "source": [{"book": "ACC AHA 2022 HF", "page": 113}],
        "confusable_with": ""
    },
    {
        "id": "cardiac-biomarkers-6",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "A patient with chest pain has troponin above the 99th percentile but no ischemic symptoms, ECG changes, or wall motion abnormality. Does this meet the 2007 AMI definition?",
        "answer": "No; the 2007 definition requires troponin elevation PLUS supporting clinical signs/symptoms of ischemia — biomarker alone is insufficient.",
        "rationale": "Troponin can be elevated in many non-ischemic conditions (myocarditis, PE, renal failure, sepsis); the AMI diagnosis requires the clinical-biomarker combination.",
        "bloom": "analyze",
        "source": [{"book": "StatPearls Cardiac Biomarkers", "page": 4}],
        "confusable_with": "myocardial injury (troponin elevation without acute ischemia)"
    },
    {
        "id": "cardiac-biomarkers-7",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "Why does myoglobin return to baseline quickly after MI, and how does this affect its clinical utility for late presenters?",
        "answer": "Myoglobin has a small molecular size and is rapidly renally cleared; it returns to baseline within 24 hours, making it useless for late presenters (>12–24h) where troponin remains elevated for days.",
        "rationale": "Troponin's slower clearance and structural binding within cardiomyocytes allows detection up to 5–14 days post-MI, while myoglobin's rapid clearance limits its window.",
        "bloom": "analyze",
        "source": [{"book": "StatPearls Cardiac Biomarkers", "page": 3}],
        "confusable_with": ""
    }
]

# ──────────────────────────────────────────────────────────────────────────────
# TOPIC 133: Chest Pain Evaluation & Acute Coronary Syndromes
# ──────────────────────────────────────────────────────────────────────────────
t = "Chest pain evaluation & acute coronary syndromes"
dom = "General internal medicine"
disc = "General internal medicine"

entries += [
    {
        "id": "acs-1",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "Within what timeframe do interventions for ACS typically need to occur, and what does this imply for initial evaluation speed?",
        "answer": "Timely interventions within hours of symptom onset are required; initial evaluation must be rapid (ECG within 10 minutes, biomarkers immediately).",
        "rationale": "Myocardial salvage is time-dependent — every hour of delay in reperfusion increases infarct size and mortality.",
        "bloom": "recall",
        "source": [{"book": "Marino ICU Book", "page": 226}],
        "confusable_with": ""
    },
    {
        "id": "acs-2",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "Beta-blockers are recommended in most ACS patients. What are the two specific contraindications or exceptions where they must be withheld?",
        "answer": "Bradycardia (relative contraindication to all beta-blockers in ACS), and cocaine-induced MI (risk of unopposed alpha-mediated coronary vasoconstriction).",
        "rationale": "In cocaine-induced MI, non-selective beta-blockade leaves alpha-adrenergic vasoconstriction unopposed, potentially worsening coronary spasm; benzodiazepines and nitrates are preferred.",
        "bloom": "apply",
        "source": [{"book": "Marino ICU Book", "page": 230}],
        "confusable_with": "standard ACS (beta-blockers beneficial)"
    },
    {
        "id": "acs-3",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What ECG finding appears within minutes of MI onset and represents the earliest ischemic change?",
        "answer": "Hyperacute symmetric (peaked) T waves — appear within minutes of onset, before ST elevation develops.",
        "rationale": "Hyperacute T waves reflect acute transmural ischemia causing localized hyperkalemia and altered repolarization; they are analyzed along vectors of ventricular depolarization and repolarization.",
        "bloom": "recall",
        "source": [{"book": "MGH Housestaff Manual", "page": 10}],
        "confusable_with": "hyperkalemia T waves (symmetric but in absence of ischemic context)"
    },
    {
        "id": "acs-4",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What is Step 1 of the perioperative cardiac assessment for patients with CAD risk factors requiring surgery?",
        "answer": "Determine the urgency of surgery — emergent surgery proceeds regardless of cardiac risk; non-urgent surgery proceeds to stepwise risk assessment.",
        "rationale": "Surgical urgency overrides pre-operative cardiac workup in life-threatening emergencies; risk stratification only applies when surgery can be safely deferred.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 622}],
        "confusable_with": ""
    },
    {
        "id": "acs-5",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "In cocaine-induced chest pain with ST elevation, why is nitroglycerin preferred over beta-blockers, and what additional medication class is also used?",
        "answer": "Nitroglycerin directly vasodilates coronary arteries; benzodiazepines are also used to reduce sympathomimetic drive. Beta-blockers risk unopposed alpha-mediated coronary vasoconstriction.",
        "rationale": "Cocaine causes sympathomimetic coronary spasm via alpha-adrenergic and dopaminergic stimulation; beta-blockade removes the beta-vasodilatory component while leaving alpha-vasoconstriction unopposed.",
        "bloom": "analyze",
        "source": [{"book": "Marino ICU Book", "page": 230}],
        "confusable_with": ""
    },
    {
        "id": "acs-6",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "How should hyperacute T waves be distinguished from normal T wave variants on a 12-lead ECG?",
        "answer": "Hyperacute T waves are symmetric, peaked, and analyzed in the context of vectors of ventricular depolarization/repolarization in at least two contiguous leads suggesting a territory of ischemia.",
        "rationale": "Normal T waves are asymmetric with a gradual upstroke; symmetry and peaking in a coronary territory distribution distinguishes ischemia from normal variant or hyperkalemia.",
        "bloom": "analyze",
        "source": [{"book": "MGH Housestaff Manual", "page": 10}],
        "confusable_with": "hyperkalemia (symmetric T waves without territorial distribution)"
    },
    {
        "id": "acs-7",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What is the implication of a very short symptom-to-door time in STEMI for the priority of initial interventions?",
        "answer": "Very early presenters may still show only hyperacute T waves without ST elevation; serial ECGs every 15–30 minutes are mandatory since ST changes evolve rapidly and interventional activation must not wait.",
        "rationale": "Earliest ECG may be non-diagnostic; dynamic evolution confirms MI and triggers cath lab activation — serial ECGs preserve the time-to-treatment window.",
        "bloom": "apply",
        "source": [{"book": "Marino ICU Book", "page": 226}],
        "confusable_with": ""
    },
    {
        "_type": "illness_script",
        "topic": t,
        "discipline": disc,
        "enabling_conditions": "CAD risk factors: smoking, hypertension, diabetes, hyperlipidemia, family history, age, male sex; cocaine use; prior MI.",
        "pathophysiology": "Atherosclerotic plaque rupture → platelet aggregation → acute coronary thrombus → partial (NSTEMI/UA) or complete (STEMI) coronary occlusion → ischemic myocardial injury → troponin release.",
        "time_course": "Symptoms begin acutely; ECG evolves over minutes (hyperacute T) → hours (ST elevation) → days (Q waves); troponin detectable 1–4h, peaks 12–24h.",
        "key_features": "Chest pain/pressure radiating to arm/jaw, diaphoresis, nausea; ECG changes (ST elevation/depression, hyperacute T waves, new LBBB); troponin elevation above 99th percentile.",
        "consequence_if_missed": "Complete infarction, ventricular fibrillation, cardiogenic shock, mechanical complications (free wall rupture, VSD, papillary muscle rupture), death."
    }
]

# ──────────────────────────────────────────────────────────────────────────────
# TOPIC 134: Cirrhosis: Diagnosis & Staging (minimal chunks — 3 KPs only)
# ──────────────────────────────────────────────────────────────────────────────
t = "Cirrhosis: Diagnosis & Staging"
dom = "Internal medicine: gastroenterology"
disc = "Gastroenterology"

entries += [
    {
        "id": "cirrhosis-staging-1",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What five components are used to calculate a Child-Pugh score in cirrhosis?",
        "answer": "Serum bilirubin, serum albumin, prothrombin time (or INR), degree of ascites, and degree of hepatic encephalopathy.",
        "rationale": "Child-Pugh integrates synthetic function (albumin, PT), excretory function (bilirubin), and clinical complications (ascites, encephalopathy) to grade hepatic reserve as A, B, or C.",
        "bloom": "recall",
        "source": [{"book": "StatPearls NBK585060", "page": 1}],
        "confusable_with": "MELD score (uses different variables: bilirubin, creatinine, INR)"
    },
    {
        "id": "cirrhosis-staging-2",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What is the primary clinical use of the MELD score in cirrhosis, and which three laboratory values does it incorporate?",
        "answer": "MELD predicts 90-day mortality and guides liver transplant allocation priority; it incorporates bilirubin, creatinine, and INR.",
        "rationale": "MELD was originally developed to predict short-term mortality after TIPS; it replaced Child-Pugh for transplant listing due to objective, reproducible laboratory inputs without subjective clinical grading.",
        "bloom": "recall",
        "source": [{"book": "StatPearls NBK585060", "page": 1}],
        "confusable_with": "Child-Pugh (includes subjective ascites/encephalopathy grades)"
    },
    {
        "id": "cirrhosis-staging-3",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What is the gold standard for definitive diagnosis and staging of cirrhosis?",
        "answer": "Liver biopsy.",
        "rationale": "Liver biopsy with histologic assessment (Metavir or Ishak staging) directly visualizes fibrosis architecture and degree; non-invasive methods (elastography, serum markers) provide estimates but cannot fully replace biopsy for staging.",
        "bloom": "recall",
        "source": [{"book": "StatPearls NBK585060", "page": 1}],
        "confusable_with": "transient elastography (non-invasive alternative, not gold standard)"
    }
]

# ──────────────────────────────────────────────────────────────────────────────
# TOPIC 135: Community-Acquired Pneumonia
# ──────────────────────────────────────────────────────────────────────────────
t = "Community-Acquired Pneumonia"
dom = "Internal medicine: pulmonology"
disc = "Pulmonology"

entries += [
    {
        "id": "cap-1",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "A patient with confirmed CAP is admitted to the medical ward but deteriorates and requires ICU transfer 48 hours later. How does late ICU admission affect prognosis?",
        "answer": "Late ICU admission in CAP is associated with higher mortality compared to direct ICU admission.",
        "rationale": "Delayed escalation of care allows progressive respiratory failure and septic shock to worsen without the intensity of organ support available in the ICU.",
        "bloom": "apply",
        "source": [{"book": "IDSA ATS 2019 CAP", "page": 12}],
        "confusable_with": ""
    },
    {
        "id": "cap-2",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "Which class of organisms causes the majority of infection-related SIRS in critically ill patients, and what happens when the inflammatory response is marked and prolonged?",
        "answer": "Gram-negative organisms; marked/prolonged response → widespread organ dysfunction (multi-organ failure).",
        "rationale": "Gram-negative bacterial cell wall lipopolysaccharide (endotoxin) is a potent trigger of systemic inflammatory cytokine release; excessive response overwhelms regulatory mechanisms.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 2148}],
        "confusable_with": ""
    },
    {
        "id": "cap-3",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "Why does advanced age strongly correlate with aspiration pneumonia, even in patients without overt dysphagia?",
        "answer": "Silent microaspiration in older adults — impaired swallowing reflexes and reduced cough response allow small volumes of oropharyngeal secretions to enter the lower airway without triggering protective mechanisms.",
        "rationale": "Age-related neurologic degeneration reduces the sensitivity of pharyngeal and laryngeal reflexes; silent aspiration may go unrecognized until pneumonia develops.",
        "bloom": "analyze",
        "source": [{"book": "StatPearls Aspiration Pneumonia", "page": 3}],
        "confusable_with": "classic aspiration (large volume, witnessed event)"
    },
    {
        "id": "cap-4",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What clinical and severity criteria should prompt consideration of direct ICU admission rather than ward admission for CAP?",
        "answer": "Major criteria: need for invasive mechanical ventilation or vasopressors. Minor criteria (3 of 9): RR ≥30, PaO2/FiO2 ≤250, multilobar infiltrates, confusion, BUN ≥20, WBC <4,000, platelets <100,000, temp <36°C, hypotension requiring aggressive resuscitation.",
        "rationale": "IDSA/ATS severe CAP criteria identify patients at high risk of deterioration who benefit from direct ICU-level care rather than delayed escalation.",
        "bloom": "apply",
        "source": [{"book": "IDSA ATS 2019 CAP", "page": 12}],
        "confusable_with": ""
    },
    {
        "id": "cap-5",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "In an elderly patient with CAP who was not witnessed coughing or choking while eating, how does the mechanism differ from classic aspiration pneumonia?",
        "answer": "Silent microaspiration of colonized oropharyngeal secretions during sleep or during swallowing without triggering a cough reflex; this is distinct from large-volume aspiration events.",
        "rationale": "The distinction matters because silent aspiration is preventable with oral care and positioning interventions, whereas witnessed aspiration events require immediate airway management.",
        "bloom": "analyze",
        "source": [{"book": "StatPearls Aspiration Pneumonia", "page": 3}],
        "confusable_with": "community-acquired pneumonia from exogenous pathogen (different prevention strategy)"
    },
    {
        "_type": "illness_script",
        "topic": t,
        "discipline": disc,
        "enabling_conditions": "Advanced age, smoking, immunosuppression, aspiration risk (dysphagia, altered consciousness), COPD, heart failure.",
        "pathophysiology": "Inhalation or microaspiration of pathogens (most commonly Streptococcus pneumoniae, atypicals, gram-negatives in elderly) → alveolar infection → neutrophil influx → consolidation → impaired gas exchange; gram-negative organisms trigger robust SIRS that can progress to septic shock.",
        "time_course": "Prodrome 1–3 days; hospitalization typically 3–7 days; late ICU transfer associated with worse mortality than early recognition.",
        "key_features": "Fever, productive cough, pleuritic chest pain, lobar infiltrate on CXR, leukocytosis; elderly may present with confusion or functional decline without classic symptoms.",
        "consequence_if_missed": "Respiratory failure, septic shock, empyema, lung abscess, ARDS, death; late ICU transfer worsens outcome."
    }
]

# ──────────────────────────────────────────────────────────────────────────────
# TOPIC 136: Deep Vein Thrombosis
# ──────────────────────────────────────────────────────────────────────────────
t = "Deep vein thrombosis: diagnosis and treatment"
dom = "Internal medicine: hematology & oncology"
disc = "Hematology"

entries += [
    {
        "id": "dvt-1",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "Where do deep vein thrombi most commonly form, and what local hemodynamic features predispose these sites?",
        "answer": "Soleal sinuses and behind venous valve pockets — low-flow zones where blood stasis allows thrombus formation.",
        "rationale": "Virchow's triad requires stasis, endothelial injury, and hypercoagulability; valve pockets and soleal sinuses are low-shear zones where platelet aggregation initiates thrombosis.",
        "bloom": "recall",
        "source": [{"book": "StatPearls DVT", "page": 4}],
        "confusable_with": ""
    },
    {
        "id": "dvt-2",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What role does endothelial dysfunction play in DVT pathophysiology?",
        "answer": "Endothelial dysfunction impairs natural anticoagulant mechanisms (protein C activation, tissue factor pathway inhibitor, thrombomodulin expression), promoting a prothrombotic state.",
        "rationale": "Intact endothelium suppresses coagulation via multiple pathways; dysfunction from immobility, hypoxia, or prior trauma removes these protective mechanisms.",
        "bloom": "analyze",
        "source": [{"book": "StatPearls DVT", "page": 4}],
        "confusable_with": ""
    },
    {
        "id": "dvt-3",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "For pelvic or abdominal oncology surgery patients, what extended prophylaxis consideration is supported by evidence, and what is the tradeoff?",
        "answer": "Extended outpatient VTE prophylaxis is beneficial; however, it approximately doubles bleeding risk compared to standard in-hospital prophylaxis alone.",
        "rationale": "Cancer surgery patients have prolonged hypercoagulable states due to tumor procoagulant factors; the ENOXACAN II and FAME trials showed VTE reduction with extended prophylaxis at cost of doubled bleeding.",
        "bloom": "analyze",
        "source": [{"book": "StatPearls DVT", "page": 9}],
        "confusable_with": ""
    },
    {
        "id": "dvt-4",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What is fat embolism syndrome, and what are its four classic clinical signs?",
        "answer": "Fat embolism syndrome: fat globules enter circulation (usually after long bone fracture). Classic signs: petechiae on chest, upper extremities, axillae, and conjunctiva; fat globules in retina and urine.",
        "rationale": "Bone marrow fat released by fracture lodges in pulmonary capillaries and systemic microvasculature; hydrolysis of fat produces free fatty acids causing endothelial injury and the petechial rash.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 1298}],
        "confusable_with": "PE (no petechiae, different embolism type)"
    },
    {
        "id": "dvt-5",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What did the PADIS-DVT trial demonstrate about anticoagulation duration after unprovoked DVT?",
        "answer": "6 months of anticoagulation after unprovoked DVT was compared to extended anticoagulation; the trial addressed optimal duration of therapy in this clinical scenario.",
        "rationale": "Unprovoked DVT has a high recurrence risk; PADIS-DVT evaluated whether extended anticoagulation beyond 6 months reduces recurrence, balancing against long-term bleeding risk.",
        "bloom": "recall",
        "source": [{"book": "CHEST 2021 VTE", "page": 64}],
        "confusable_with": "provoked DVT (shorter duration standard)"
    },
    {
        "id": "dvt-6",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "How does extended VTE prophylaxis for pelvic oncology surgery patients change the risk-benefit calculation compared to standard in-hospital prophylaxis?",
        "answer": "Extended prophylaxis lowers VTE incidence in high-risk surgical oncology patients but approximately doubles the risk of clinically significant bleeding events.",
        "rationale": "The risk-benefit balance shifts favorably for extended prophylaxis in pelvic/abdominal oncology surgery due to very high baseline VTE risk from tumor procoagulants and venous injury during surgery.",
        "bloom": "analyze",
        "source": [{"book": "StatPearls DVT", "page": 9}],
        "confusable_with": ""
    },
    {
        "_type": "illness_script",
        "topic": t,
        "discipline": disc,
        "enabling_conditions": "Immobility (hospitalization, long-haul travel), prior VTE, cancer, pregnancy, thrombophilia, major surgery (especially orthopedic, pelvic), OCP/hormone therapy.",
        "pathophysiology": "Venous stasis + endothelial dysfunction + hypercoagulability (Virchow's triad) → thrombus initiation at soleal sinuses/valve pockets → propagation → proximal DVT → PE risk if clot fragments.",
        "time_course": "Develops over days to weeks of risk exposure; symptoms may be absent (50% asymptomatic); PE risk highest in first weeks.",
        "key_features": "Unilateral leg swelling, calf tenderness, warmth; Wells score guides pre-test probability; confirmed by compression ultrasound.",
        "consequence_if_missed": "Pulmonary embolism (potentially fatal), post-thrombotic syndrome (chronic venous insufficiency), recurrent DVT."
    }
]

# ──────────────────────────────────────────────────────────────────────────────
# TOPIC 137: Delirium Prevention Programs & Hospital-Acquired Complications
# ──────────────────────────────────────────────────────────────────────────────
t = "Delirium prevention programs & hospital-acquired complications"
dom = "General internal medicine"
disc = "General internal medicine"

entries += [
    {
        "id": "delirium-hac-1",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What are the five major hospital-acquired complications (HACs), and what single shared risk factor underlies most of them?",
        "answer": "Falls, pressure ulcers, hospital-acquired infections (CLABSI, CAUTI, SSI, pneumonia), delirium, and deconditioning. Shared risk factor: immobility (due to pain, sedation, or weakness).",
        "rationale": "Immobility is the common denominator — it impairs skin perfusion (ulcers), reduces gait stability (falls), promotes aspiration and line retention (HAI), and drives delirium and functional decline.",
        "bloom": "recall",
        "source": [{"book": "Curated Units", "page": 0}],
        "confusable_with": ""
    },
    {
        "id": "delirium-hac-2",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What is the approximate incidence of inpatient falls and pressure ulcers during hospitalization?",
        "answer": "Falls: 1–5% of admissions (majority preventable). Pressure ulcers: 5–15% of admissions (stage 3+ are rare).",
        "rationale": "These rates reflect modifiable risk factors; prevention programs targeting mobility, skin inspection, and nutrition substantially reduce both outcomes.",
        "bloom": "recall",
        "source": [{"book": "Curated Units", "page": 0}],
        "confusable_with": ""
    },
    {
        "id": "delirium-hac-3",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "According to AGS guidelines, what analgesic strategy in older postoperative patients reduces the likelihood of delirium?",
        "answer": "Nonopioid analgesia techniques (e.g., regional anesthesia, NSAIDs if safe, acetaminophen) reduce delirium likelihood in older adults.",
        "rationale": "Opioids impair cholinergic neurotransmission and cause sedation, both of which are independent delirium risk factors; nonopioid multimodal analgesia reduces the anticholinergic and sedating burden.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 1504}],
        "confusable_with": ""
    },
    {
        "id": "delirium-hac-4",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What comprehensive program addresses fall prevention in patients undergoing lower extremity arthroplasty?",
        "answer": "Comprehensive fall prevention programs specifically addressing post-arthroplasty patients are recommended — these include early physical therapy, environmental modification, medication review, and patient education.",
        "rationale": "Lower extremity arthroplasty patients have impaired proprioception, pain, and weakness immediately post-operatively, placing them at high fall risk during the early mobilization phase.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 1313}],
        "confusable_with": ""
    },
    {
        "id": "delirium-hac-5",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "Beyond immobility, what two patient-level factors are shared risk factors across the major HAC categories?",
        "answer": "Cognitive impairment and pain/sedation.",
        "rationale": "Cognitive impairment reduces ability to call for help, cooperate with repositioning, or report early signs of HACs; sedation and pain both promote immobility and reduce protective reflexes.",
        "bloom": "recall",
        "source": [{"book": "Curated Units", "page": 0}],
        "confusable_with": ""
    },
    {
        "id": "delirium-hac-6",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "In opioid-treated postoperative older adults, what specific mechanism links opioid use to delirium development?",
        "answer": "Opioids impair central cholinergic neurotransmission and cause sedation — both independent risk factors for delirium — by acting on opioid receptors in the brainstem and limbic system.",
        "rationale": "The AGS Beers Criteria identify opioids as delirium-precipitating agents in older adults; multimodal nonopioid analgesia reduces this cholinergic deficit.",
        "bloom": "analyze",
        "source": [{"book": "Morgan & Mikhail", "page": 1504}],
        "confusable_with": ""
    }
]

# ──────────────────────────────────────────────────────────────────────────────
# TOPIC 138: Diabetic Ketoacidosis (DKA)
# ──────────────────────────────────────────────────────────────────────────────
t = "Diabetic Ketoacidosis (DKA)"
dom = "Internal medicine: endocrinology"
disc = "Endocrinology"

entries += [
    {
        "id": "dka-1",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What are the three life-threatening acute complications of diabetes?",
        "answer": "Diabetic ketoacidosis (DKA), hyperosmolar hyperglycemic state (HHS), and hypoglycemia.",
        "rationale": "All three represent extremes of glucose dysregulation requiring urgent treatment; DKA involves insulin deficiency with ketosis, HHS involves hyperosmolarity without significant ketosis, and hypoglycemia involves excess insulin effect.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 1218}],
        "confusable_with": ""
    },
    {
        "id": "dka-2",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "A patient with type 2 diabetes starts empagliflozin and is admitted 2 days post-surgery with anion gap metabolic acidosis but glucose only mildly elevated (180 mg/dL). What diagnosis must be considered?",
        "answer": "Euglycemic DKA due to SGLT2 inhibitor; SGLT2 inhibitors provoke DKA with near-normal glucose by increasing glucagon and promoting ketogenesis, particularly when fluid and hormonal changes occur perioperatively.",
        "rationale": "SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin) are associated with euglycemic DKA especially around surgery; the glucose may be misleadingly near-normal.",
        "bloom": "analyze",
        "source": [{"book": "Morgan & Mikhail", "page": 1223}],
        "confusable_with": "standard hyperglycemic DKA, starvation ketosis"
    },
    {
        "id": "dka-3",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "Which four SGLT2 inhibitors are associated with increased DKA risk including euglycemic DKA?",
        "answer": "Canagliflozin, dapagliflozin, empagliflozin, and ertugliflozin.",
        "rationale": "All SGLT2 inhibitors increase urinary glucose excretion and lower the renal threshold for glucose, leading to a relative decrease in insulin-to-glucagon ratio and ketone body accumulation.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 1223}],
        "confusable_with": ""
    },
    {
        "id": "dka-4",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What is the primary treatment goal for fluid replacement in DKA, and what specific therapy is given?",
        "answer": "Replace the existing fluid deficit with IV crystalloid (typically normal saline initially); fluid replacement restores circulating volume and renal perfusion, enabling insulin to work.",
        "rationale": "DKA causes profound dehydration from osmotic diuresis; insulin therapy without adequate fluid resuscitation risks cardiovascular collapse and does not adequately lower glucose.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 1931}],
        "confusable_with": ""
    },
    {
        "id": "dka-5",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "Why have alternative alkali agents (Carbicarb, THAM) not replaced bicarbonate in DKA treatment, despite theoretical advantages?",
        "answer": "Although theoretically preferable (e.g., Carbicarb does not generate CO2, THAM buffers without sodium load), they remain unproven in clinical trials compared to standard bicarbonate use.",
        "rationale": "Clinical evidence for routine bicarbonate use in DKA itself is also controversial, but alternative agents lack the evidence base to displace established standard-of-care therapy.",
        "bloom": "analyze",
        "source": [{"book": "Morgan & Mikhail", "page": 1931}],
        "confusable_with": ""
    },
    {
        "id": "dka-6",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What fluid and hormonal changes associated with SGLT2 inhibitors trigger DKA even without marked hyperglycemia?",
        "answer": "Perioperative fasting, volume depletion, and stress-induced changes in the insulin-to-glucagon ratio shift metabolism toward ketogenesis; SGLT2 inhibitor-induced glucagon elevation amplifies this.",
        "rationale": "SGLT2 inhibitors directly increase glucagon secretion and suppress insulin; fasting and surgical stress further suppress insulin and stimulate counterregulatory hormones, promoting ketone body production.",
        "bloom": "analyze",
        "source": [{"book": "Morgan & Mikhail", "page": 1223}],
        "confusable_with": ""
    },
    {
        "id": "dka-7",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "How does DKA differ from HHS in terms of the presence of ketosis and the degree of glucose elevation?",
        "answer": "DKA: prominent ketosis (anion gap metabolic acidosis), glucose typically 250–600 mg/dL (but can be euglycemic on SGLT2i). HHS: minimal or absent ketosis, glucose often >600 mg/dL with extreme hyperosmolarity.",
        "rationale": "In DKA, absolute insulin deficiency drives unrestrained lipolysis and ketogenesis; in HHS, residual insulin is sufficient to suppress ketogenesis but insufficient to control glucose.",
        "bloom": "analyze",
        "source": [{"book": "Morgan & Mikhail", "page": 1218}],
        "confusable_with": "HHS (no significant ketosis)"
    },
    {
        "_type": "illness_script",
        "topic": t,
        "discipline": disc,
        "enabling_conditions": "Type 1 DM most common; also type 2 with precipitating illness; SGLT2 inhibitor use (euglycemic variant); infection, medication non-adherence, new onset T1DM, surgery.",
        "pathophysiology": "Insulin deficiency → unrestrained glucagon → hyperglycemia + lipolysis → free fatty acid oxidation → ketone bodies (acetoacetate, beta-hydroxybutyrate) → anion gap metabolic acidosis → osmotic diuresis → dehydration and electrolyte depletion.",
        "time_course": "Develops over hours to days; rapid deterioration without treatment.",
        "key_features": "Polyuria, polydipsia, nausea/vomiting, abdominal pain, Kussmaul breathing, fruity breath, anion gap metabolic acidosis, ketonemia/ketonuria, glucose typically >250 mg/dL (may be near-normal in SGLT2i DKA).",
        "consequence_if_missed": "Cerebral edema (especially children), severe hypokalemia with insulin treatment (must replete K+ before insulin if K+ <3.5), respiratory arrest, death."
    },
    {
        "_type": "confusable_pair",
        "topic_a": "Diabetic Ketoacidosis (DKA)",
        "topic_b": "Hyperosmolar Hyperglycemic State (HHS)",
        "discriminator": "DKA: anion gap metabolic acidosis + ketosis + glucose often 250–600 (but can be euglycemic on SGLT2i). HHS: glucose >600 + plasma osmolality >320 + minimal or NO ketosis. Both: dehydration, polyuria; HHS predominates in type 2 DM with enough residual insulin to suppress ketogenesis."
    }
]

# ──────────────────────────────────────────────────────────────────────────────
# TOPIC 139: Dyspnea & Acute Decompensated Heart Failure
# ──────────────────────────────────────────────────────────────────────────────
t = "Dyspnea & acute decompensated heart failure"
dom = "General internal medicine"
disc = "General internal medicine"

entries += [
    {
        "id": "adhf-1",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What initially maintains cardiac output in early heart failure, and why does this compensation ultimately cause harm?",
        "answer": "Sympathetic activation with norepinephrine release initially maintains cardiac output via tachycardia and increased contractility; long-term it drives adverse cardiac remodeling (hypertrophy, fibrosis, apoptosis).",
        "rationale": "Neurohormonal activation (RAAS, SNS) is initially adaptive but becomes maladaptive — chronic catecholamine exposure downregulates beta-receptors and promotes ventricular dilation and failure.",
        "bloom": "analyze",
        "source": [{"book": "Morgan & Mikhail", "page": 603}],
        "confusable_with": ""
    },
    {
        "id": "adhf-2",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "What initial diagnostic tests are recommended in a patient presenting with suspected new heart failure?",
        "answer": "Elevated BNP or NT-proBNP corroborates HF diagnosis; initial laboratory panel (metabolic panel, CBC, TSH) and 12-lead ECG.",
        "rationale": "BNP/NT-proBNP have high sensitivity for HF and help distinguish it from pulmonary causes of dyspnea; ECG identifies arrhythmias, ischemia, or LVH as underlying cause.",
        "bloom": "recall",
        "source": [{"book": "ACC AHA 2022 HF", "page": 112}],
        "confusable_with": ""
    },
    {
        "id": "adhf-3",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "How does the trajectory of NT-proBNP during hospitalization for ADHF guide prognosis and discharge planning?",
        "answer": "Reduction of NT-proBNP during hospitalization predicts lower long-term cardiovascular mortality; failure to achieve NT-proBNP reduction before discharge signals inadequate decongestion and high rehospitalization risk.",
        "rationale": "NT-proBNP tracks filling pressures; persistent elevation indicates ongoing congestion and elevated wall stress — a surrogate for decompensated state despite apparent clinical improvement.",
        "bloom": "analyze",
        "source": [{"book": "ACC AHA 2022 HF", "page": 113}],
        "confusable_with": ""
    },
    {
        "id": "adhf-4",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "In HFpEF patients not acutely decompensated, what physical exam finding is present in approximately 10–20% and what does it indicate?",
        "answer": "Jugular venous distension (JVD) in ~10–20% of non-acutely-decompensated HFpEF patients, indicating elevated central venous and right-sided filling pressures.",
        "rationale": "HFpEF may have elevated filling pressures at rest even when not dramatically decompensated; JVD is an objective sign of volume overload not always captured by symptoms alone.",
        "bloom": "recall",
        "source": [{"book": "StatPearls", "page": 9}],
        "confusable_with": "HFrEF (more commonly decompensated at presentation)"
    },
    {
        "id": "adhf-5",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "In a patient with dyspnea, how does BNP help distinguish heart failure from a primary pulmonary etiology?",
        "answer": "Elevated BNP indicates cardiac origin (volume overload/wall stress); normal BNP effectively rules out HF as the cause of dyspnea (high negative predictive value).",
        "rationale": "BNP released from stretched ventricular myocytes is sensitive for HF; a low BNP redirects evaluation to pulmonary (PE, COPD exacerbation) or other causes of dyspnea.",
        "bloom": "apply",
        "source": [{"book": "Morgan & Mikhail", "page": 603}],
        "confusable_with": "troponin elevation (myocardial injury, not volume overload)"
    },
    {
        "id": "adhf-6",
        "topic": t, "domain": dom, "discipline": disc,
        "stem": "In mildly hypertensive, non-acutely-decompensated HFpEF, what is the significance of JVD being absent in approximately 80–90% of such patients?",
        "answer": "Absence of JVD in HFpEF does not exclude elevated filling pressures — many HFpEF patients have elevated PCWP only with exertion or during fluid challenge, not at rest, limiting sensitivity of JVD as a screening sign.",
        "rationale": "HFpEF's stiff left ventricle raises filling pressures with minimal volume changes; resting JVD appears only when volume overload is significant, making exercise testing or right heart catheterization necessary in equivocal cases.",
        "bloom": "analyze",
        "source": [{"book": "StatPearls", "page": 9}],
        "confusable_with": ""
    }
]

# ──────────────────────────────────────────────────────────────────────────────
# Write output
# ──────────────────────────────────────────────────────────────────────────────
out_path = pathlib.Path(__file__).parent / "kp_catalog_part4b.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)

# Summary
kp_count = sum(1 for e in entries if "_type" not in e)
illness_count = sum(1 for e in entries if e.get("_type") == "illness_script")
confusable_count = sum(1 for e in entries if e.get("_type") == "confusable_pair")

print(f"Total entries: {len(entries)}")
print(f"  Knowledge points (KPs): {kp_count}")
print(f"  Illness scripts:        {illness_count}")
print(f"  Confusable pairs:       {confusable_count}")
print(f"Output written to: {out_path}")
