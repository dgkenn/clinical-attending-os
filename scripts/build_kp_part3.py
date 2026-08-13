import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open("C:/Users/Dean/anesthesia_attending/scripts/kp_batch2.json", "r", encoding="utf-8") as f:
    kps = json.load(f)

print("Loaded", len(kps), "from batch2")

# ============================================================
# ITEM 13: Pulmonary Hypertension in ICU
# CHUNKS are thin (COPD, OSA, index content)
# ============================================================
topic = "Pulmonary Hypertension in ICU"
domain = "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)"
disc = "medicine"

kps += [
  {"id":"pulm-htn-icu-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Pulmonary artery systolic pressure can be estimated non-invasively by what echocardiographic technique when a specific valvular lesion is present?",
   "answer":"Tricuspid regurgitation (TR) jet velocity with the Bernoulli equation: PASP = 4v^2 + RAP; assumes no pulmonic valve disease so RVSP = PASP.",
   "rationale":"TR creates a pressure gradient between RV and RA measurable by Doppler; adding known (or estimated) RAP gives PASP without invasive catheterization.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":182}],"confusable_with":""},
  {"id":"pulm-htn-icu-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In the ICU management of COPD, what finding on pulmonary function testing indicates very high risk for dyspnea with minimal activity?",
   "answer":"FEV1 <25% predicted (<1 L in men) indicates dyspnea with minimal activity; FEV1 <50% (1.2-1.5 L) typically causes dyspnea on exertion.",
   "rationale":"FEV1 reflects airflow obstruction severity; very low FEV1 indicates near-total obstruction limiting even low-level exertion and predicts pulmonary hypertension from chronic hypoxia.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":872}],"confusable_with":""},
  {"id":"pulm-htn-icu-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In patients with pulmonary hypertension and right heart failure, what hemodynamic approach avoids worsening right ventricular afterload during anesthesia?",
   "answer":"Avoid hypoxia (pulmonary vasoconstriction), hypercarbia (acidosis increases PVR), high airway pressures (impedes RV outflow), and agents that cause systemic hypotension (uncouples RV from pulmonary vasculature); use pulmonary vasodilators (inhaled nitric oxide, inhaled prostacyclin) when needed.",
   "rationale":"The RV in pulmonary HTN is pressure-overloaded and afterload-sensitive; any increase in PVR or decrease in systemic pressure reduces coronary perfusion pressure and precipitates acute RV failure.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":186}],"confusable_with":""},
  {"id":"pulm-htn-icu-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Pulmonic stenosis obstructs what outflow tract and causes what adaptive cardiac change?",
   "answer":"Pulmonic stenosis obstructs right ventricular outflow and causes concentric right ventricular hypertrophy (pressure-overload hypertrophy).",
   "rationale":"Sustained outflow obstruction forces the RV to generate higher systolic pressure; concentric hypertrophy is the adaptive response but reduces RV compliance and eventually leads to failure.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":686}],"confusable_with":""},
  {"id":"pulm-htn-icu-d5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In COPD patients with pulmonary hypertension being managed with bronchodilators, what volatile anesthetic agent should be avoided due to bronchoconstriction?",
   "answer":"Desflurane should be avoided; all other volatile agents (sevoflurane, isoflurane) reduce bronchomotor tone and produce bronchodilation helpful in obstructive lung disease.",
   "rationale":"Desflurane causes airway irritation and reflex bronchoconstriction; sevoflurane is the preferred volatile agent in reactive airway/obstructive lung disease.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":504}],"confusable_with":""},
]

# ============================================================
# ITEM 14: Reactive arthritis
# ============================================================
topic = "Reactive arthritis"
domain = "Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)"
disc = "medicine"

kps += [
  {"id":"reactive-arthritis-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the classic triad of reactive arthritis ('Reiter syndrome') and following what type of infection does it typically arise?",
   "answer":"Classic triad: arthritis + urethritis/cervicitis + conjunctivitis/uveitis ('can't pee, can't see, can't climb a tree'); follows genitourinary (Chlamydia trachomatis) or gastrointestinal (Salmonella, Shigella, Yersinia, Campylobacter) infection.",
   "rationale":"Reactive arthritis is a post-infectious sterile inflammatory arthritis; the immune response to infection triggers molecular mimicry with joint antigens.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Reactive arthritis","page":2}],"confusable_with":"Septic arthritis"},
  {"id":"reactive-arthritis-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"HLA-B27 testing supports the diagnosis of reactive arthritis — if absent, does this rule out the disease?",
   "answer":"No — HLA-B27 supports the diagnosis but its absence does NOT rule out reactive arthritis; the diagnosis is primarily clinical, and HLA-B27 is neither required nor definitively diagnostic.",
   "rationale":"HLA-B27 increases susceptibility to spondyloarthropathies including reactive arthritis but is present in only ~50-75% of cases; negative testing does not exclude the diagnosis.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Reactive arthritis","page":6}],"confusable_with":""},
  {"id":"reactive-arthritis-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What synovial fluid finding is essential to exclude when evaluating a patient with suspected reactive arthritis?",
   "answer":"Septic arthritis must be excluded — reactive arthritis typically shows sterile inflammatory synovial fluid; synovial fluid culture/Gram stain is mandatory.",
   "rationale":"Reactive arthritis is sterile inflammation; failure to exclude septic arthritis risks joint destruction from untreated infection.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Reactive arthritis","page":6}],"confusable_with":"Septic arthritis"},
  {"id":"reactive-arthritis-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What immune mechanisms drive synovial inflammation in reactive arthritis?",
   "answer":"Robust Th1 and Th17 activity with cytokines TNF-alpha, IL-17, and IL-23 driving synovial inflammation; persistent microbial antigens in the joint promote chronic inflammation through molecular mimicry.",
   "rationale":"Th17-mediated IL-17/IL-23 axis is central to spondyloarthropathy pathogenesis; this explains the efficacy of IL-17 and TNF inhibitors in refractory disease.",
   "bloom":"analyze","source":[{"book":"StatPearls: StatPearls   Reactive arthritis","page":4}],"confusable_with":""},
  {"id":"reactive-arthritis-d5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What two skin manifestations are pathognomonic or highly characteristic of reactive arthritis?",
   "answer":"Keratoderma blennorrhagicum (hyperkeratotic papules/plaques on soles and palms, resembling pustular psoriasis) and circinate balanitis (painless shallow ulcers on glans penis).",
   "rationale":"These dermatologic lesions are specific to reactive arthritis/Reiter syndrome and when present alongside arthritis and urethritis clinch the diagnosis.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Reactive arthritis","page":5}],"confusable_with":"Psoriatic arthritis"},
  {"id":"reactive-arthritis-d6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the prognosis of reactive arthritis and which organism-associated subtype is most prone to relapse?",
   "answer":"Most cases resolve within 3-6 months; Chlamydia-associated reactive arthritis tends to have more frequent relapses than enteric-triggered disease; ~15-20% develop severe long-term consequences such as joint deformity.",
   "rationale":"Chlamydia can persist intracellularly in the joint, maintaining chronic antigen stimulation; enteric organisms are more rapidly cleared, allowing immune resolution.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Reactive arthritis","page":8}],"confusable_with":""},
  {"id":"reactive-arthritis-d7","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the first-line treatment for reactive arthritis and when are DMARDs or biologics needed?",
   "answer":"NSAIDs are first-line; DMARDs (sulfasalazine, MTX) for persistent disease; TNF inhibitors, IL-17 inhibitors, or JAK inhibitors (tofacitinib) for severe/refractory cases including refractory skin and nail changes.",
   "rationale":"Reactive arthritis is often self-limited so aggressive DMARD therapy is reserved for refractory or severe cases; biologics target the Th17/TNF pathways central to spondyloarthropathy.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Reactive arthritis","page":7}],"confusable_with":""},
]
kps.append({"_type":"illness_script","topic":topic,"discipline":disc,
  "enabling_conditions":"Young adults; follows GI infection (Salmonella, Shigella, Yersinia, Campylobacter) or GU infection (Chlamydia trachomatis); HLA-B27 positive in ~50-75%",
  "pathophysiology":"Post-infectious sterile inflammatory arthritis; Th1/Th17 with TNF-alpha/IL-17/IL-23; persistent microbial antigens -> molecular mimicry -> joint inflammation",
  "time_course":"Onset 1-6 weeks after infection; most resolve in 3-6 months; Chlamydia-associated more prone to relapse",
  "key_features":"Asymmetric oligoarthritis (lower extremities), urethritis, conjunctivitis/uveitis, keratoderma blennorrhagicum, circinate balanitis; sterile synovial fluid; HLA-B27 supportive but not required",
  "consequence_if_missed":"Missed septic arthritis (must exclude), undiagnosed spondyloarthropathy with joint deformity in 15-20%"})

# ============================================================
# ITEM 15: Seronegative spondyloarthropathies - overview
# CHUNKS are thin (reactive arthritis, anesthesia machine, mitral regurg)
# ============================================================
topic = "Seronegative spondyloarthropathies - overview & shared features"
domain = "Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)"
disc = "medicine"

kps += [
  {"id":"spondyloarthropathy-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What entheseal and axial radiological features are shared across the seronegative spondyloarthropathies?",
   "answer":"Enthesitis and new bone formation are characteristic of all spondyloarthropathies; axial features include sacroiliitis and spondylitis with syndesmophyte formation (ossification of annulus fibrosus).",
   "rationale":"Enthesitis (inflammation at tendon/ligament insertion) drives new bone formation unique to spondyloarthropathies versus RA, which is purely erosive.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Psoriatic arthritis","page":8}],"confusable_with":"Rheumatoid arthritis"},
  {"id":"spondyloarthropathy-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What distinguishes the sacroiliitis and syndesmophytes of psoriatic arthritis from those of ankylosing spondylitis?",
   "answer":"Psoriatic arthritis: asymmetric, often unilateral sacroiliitis; nonmarginal, bulky, asymmetric, discontinuous syndesmophytes. Ankylosing spondylitis: bilateral symmetric sacroiliitis; marginal, thin, symmetric syndesmophytes bridging vertebral bodies.",
   "rationale":"These radiological differences reflect distinct patterns of axial inflammation and new bone formation between the two spondyloarthropathies.",
   "bloom":"analyze","source":[{"book":"StatPearls: StatPearls   Psoriatic arthritis","page":8}],"confusable_with":"Ankylosing spondylitis"},
  {"id":"spondyloarthropathy-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What extrajoint features are common across the seronegative spondyloarthropathies?",
   "answer":"Eye involvement (uveitis/conjunctivitis), skin changes (psoriasis, keratoderma blennorrhagicum), genitourinary symptoms (urethritis/cervicitis), oral ulcers, and enthesitis with dactylitis ('sausage digit').",
   "rationale":"The seronegative spondyloarthropathies share an HLA-B27-associated inflammatory process targeting entheses, axial joints, and mucocutaneous sites.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Reactive arthritis","page":5}],"confusable_with":""},
  {"id":"spondyloarthropathy-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Anti-TNF therapy is used in patients with seronegative spondyloarthropathy — when is an IL-17 inhibitor preferred over a TNF inhibitor?",
   "answer":"When there is relevant skin involvement (psoriasis), an IL-17 inhibitor may be preferred because IL-17 inhibitors have superior efficacy for both skin and joint disease versus TNF inhibitors alone.",
   "rationale":"Psoriatic skin disease is driven predominantly by IL-23/Th17/IL-17; IL-17 blockade addresses both joint and skin pathology more comprehensively in psoriatic arthritis.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Psoriatic arthritis","page":11}],"confusable_with":""},
  {"id":"spondyloarthropathy-d5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Anti-TNF agents used for ankylosing spondylitis carry what specific infectious risk that should be screened for pre-treatment?",
   "answer":"Increased risk of infection (particularly TB reactivation, opportunistic infections) and development of lymphoma with anti-TNF agents; TB screening (IGRA or TST) is required before initiating therapy.",
   "rationale":"TNF is essential for granuloma formation and maintenance; TNF blockade impairs containment of latent TB, Listeria, and fungal infections.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1745}],"confusable_with":""},
]

# ============================================================
# ITEM 16: Sexually Transmitted Infections (STIs)
# CHUNKS are almost entirely metadata/boilerplate — very thin
# Produce 4 KPs from the minimal clinical content
# ============================================================
topic = "Sexually Transmitted Infections (STIs)"
domain = "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)"
disc = "medicine"

kps += [
  {"id":"stis-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"HIV targets cells with CD4+ receptors — without treatment, what happens to the clinical course?",
   "answer":"HIV targets CD4+ T-cells and macrophages; without treatment, progressive CD4 depletion leads to AIDS-defining conditions and death, typically over 8-10 years.",
   "rationale":"CD4 cell depletion impairs cell-mediated immunity; the rate of progression varies but untreated HIV uniformly leads to immunodeficiency.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Sexually Transmitted Infections (STIs)","page":1}],"confusable_with":""},
  {"id":"stis-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is PrEP and what STI screening should accompany its use?",
   "answer":"Pre-exposure prophylaxis (tenofovir/emtricitabine) prevents HIV acquisition in high-risk individuals; routine STI testing (gonorrhea, chlamydia, syphilis, hepatitis) accompanies PrEP initiation and every 3 months during use.",
   "rationale":"PrEP users may have increased sexual risk behavior; regular STI screening is mandatory to detect treatable bacterial STIs that increase HIV susceptibility.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":129}],"confusable_with":""},
  {"id":"stis-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What STI screening is recommended for MSM (men who sex with men) beyond standard heterosexual screening?",
   "answer":"Rectal HPV screening (anal Pap + anoscopy), HPV vaccine series, hepatitis B vaccination, HIV testing, gonorrhea/chlamydia at rectal and pharyngeal sites (not just urogenital).",
   "rationale":"Rectal and pharyngeal sites are primary transmission locations in MSM; site-specific sampling is required because urogenital-only testing misses majority of infections in this population.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":129}],"confusable_with":""},
  {"id":"stis-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What are the common malaria, dengue, and tick-borne infections that must be considered in returned travelers presenting with fever and constitutional symptoms?",
   "answer":"Returned traveler febrile illness differential: malaria, dengue, EBV/CMV, tick-borne infections, typhoid fever, respiratory viruses, TB, STIs, typical bacterial infections (CAP/UTI); approach systematically by exposure history and region.",
   "rationale":"Travel medicine requires a broad syndromic approach; many tropical infections present with non-specific fever and constitutional symptoms that overlap with STIs.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":129}],"confusable_with":""},
]

# ============================================================
# ITEM 17: Small-vessel vasculitis: IgA vasculitis (HSP)
# ============================================================
topic = "Small-vessel vasculitis: IgA vasculitis (Henoch-Schonlein purpura)"
domain = "Internal medicine: rheumatology, immunology & allergy (gout & crystal arthropathy, SLE, RA, vasculitides, anaphylaxis & angioedema, drug reactions)"
disc = "medicine"

kps += [
  {"id":"iga-vasculitis-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the classic tetrad of IgA vasculitis (Henoch-Schonlein purpura) and what is its typical demographic?",
   "answer":"Classic tetrad: palpable purpura (lower extremities) + arthritis/arthralgia + abdominal pain (colicky GI involvement) + nephritis/hematuria; predominantly in children (90%), male predominance, often following URI ~10 days prior.",
   "rationale":"IgA deposition in small vessels drives multi-organ involvement; the tetrad reflects skin, joint, GI, and renal small-vessel leukocytoclastic vasculitis.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":177}],"confusable_with":"Anaphylactic purpura"},
  {"id":"iga-vasculitis-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"How does the severity and prognosis of IgA vasculitis differ between children and adults?",
   "answer":"Adults have increased severity — greater nephropathy and renal involvement; adult cases are more frequently associated with medications or underlying malignancy (unlike predominantly idiopathic/post-viral in children).",
   "rationale":"IgA vasculitis in adults is rarer but more serious; renal involvement determines long-term prognosis and adults require more aggressive nephrology follow-up.",
   "bloom":"analyze","source":[{"book":"MGH Housestaff Manual","page":177}],"confusable_with":""},
  {"id":"iga-vasculitis-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"IgA vasculitis is classified as what size vessel disease and how is it distinguished from IgA nephropathy (Berger disease)?",
   "answer":"Small-vessel vasculitis; IgA vasculitis has systemic vasculitic features (purpura, arthritis, abdominal pain, nephritis) while IgA nephropathy is confined to the kidney with mesangial IgA deposits and no systemic vasculitis.",
   "rationale":"Both involve IgA immune complexes but IgA nephropathy is organ-limited while IgA vasculitis is a systemic small-vessel vasculitis; treatment and prognosis differ.",
   "bloom":"analyze","source":[{"book":"StatPearls: StatPearls   Microscopic Colitis","page":16}],"confusable_with":"IgA nephropathy"},
  {"id":"iga-vasculitis-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What other forms of small-vessel vasculitis are listed in the differential diagnosis of IgA vasculitis?",
   "answer":"ANCA-associated vasculitis (GPA, MPA, EGPA), drug-induced small-vessel vasculitis, infection-associated vasculitis (post-streptococcal, endocarditis), cryoglobulinemic vasculitis, rheumatoid vasculitis.",
   "rationale":"All small-vessel vasculitides can present with palpable purpura; distinguishing features include ANCA status, cryoglobulins, complement, infection history, and biopsy immunofluorescence.",
   "bloom":"analyze","source":[{"book":"StatPearls: StatPearls   Cryoglobulinemic vasculitis","page":10}],"confusable_with":""},
  {"id":"iga-vasculitis-d5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Renal involvement in IgA vasculitis affects what percentage of children and how does it most commonly manifest?",
   "answer":"Renal manifestations occur in 20-50% of children; hematuria (most common) following an infection, with episodes of gross hematuria; rare progression to ESRD in children but higher in adults.",
   "rationale":"IgA deposition in glomerular mesangium causes mesangial proliferative GN with hematuria; the milder IgA vasculitis nephritis rarely progresses to ESRD in children unlike adult onset.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Microscopic Colitis","page":16}],"confusable_with":""},
  {"id":"iga-vasculitis-d6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What features on differential of palpable purpura help distinguish IgA vasculitis from rickettsial infection or antiphospholipid syndrome?",
   "answer":"Rickettsial infections and babesiosis may present with overlapping purpuric rash but have tick exposure history, fever, thrombocytopenia, and elevated LFTs; antiphospholipid syndrome causes thrombotic rather than inflammatory purpura, with APLA antibodies.",
   "rationale":"Non-blanching purpura has a broad differential including infectious, thrombotic, and vasculitic causes; careful history, exposure, and serologic testing differentiate.",
   "bloom":"analyze","source":[{"book":"StatPearls: StatPearls   Cryoglobulinemic vasculitis","page":10}],"confusable_with":""},
]
kps.append({"_type":"illness_script","topic":topic,"discipline":disc,
  "enabling_conditions":"Children (90%), male predominance, 4-15 years, often follows URI ~10 days prior; adults: associated with medications or malignancy",
  "pathophysiology":"IgA immune complex deposition in small-vessel walls -> leukocytoclastic vasculitis of skin, gut, joints, and glomeruli",
  "time_course":"Acute over days-weeks following trigger; most children recover fully in 4-6 weeks; adults more severe and prolonged",
  "key_features":"Tetrad: palpable purpura (lower extremity + buttocks) + arthritis + colicky abdominal pain + nephritis; IgA deposits on skin biopsy",
  "consequence_if_missed":"Undiagnosed nephritis progressing to ESRD in adults; intussusception from GI involvement in children"})

print("Total KPs:", len(kps))
with open("C:/Users/Dean/anesthesia_attending/scripts/kp_batch3.json", "w", encoding="utf-8") as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Saved batch3")
