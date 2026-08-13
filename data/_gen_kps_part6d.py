import json

with open('C:/Users/Dean/anesthesia_attending/data/_kps_batch3.json', 'r', encoding='utf-8') as f:
    kps = json.load(f)

# ============================================================
# [18] Femoral nerve and adductor canal blocks
# ============================================================
t = "Femoral nerve and adductor canal blocks"
dom = "Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)"
disc = "anesthesia"
s = "femoral-acb"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the key difference between femoral nerve block and adductor canal block regarding motor function after knee surgery?",
 "answer":"Adductor canal block spares quadriceps strength more than femoral nerve block; patients with adductor canal catheters ambulate further on postoperative day 1 after total knee arthroplasty than femoral block patients",
 "rationale":"The adductor canal contains primarily the saphenous nerve (sensory) and motor branches to the vastus medialis; femoral block blocks all quadriceps branches causing weakness that limits ambulation.",
 "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1667}],"confusable_with":"Femoral nerve block (better motor block for surgical use, worse for rehab)"},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What nerves and sensory territories are covered by the adductor canal block?",
 "answer":"Adductor canal block covers anterior thigh, medial leg, and medial ankle sensory territory (saphenous nerve); subsartorial nerves lie just lateral to the superficial femoral artery",
 "rationale":"The saphenous nerve (terminal sensory branch of femoral) runs with the superficial femoral artery under the sartorius in the adductor canal, providing medial leg anesthesia.",
 "bloom":"recall","source":[{"book":"Stanford CA-1","page":98},{"book":"Miller/Baby Miller","page":353}],"confusable_with":"Femoral nerve block (covers anterior thigh, medial leg, AND quadriceps motor)"},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"What ultrasound landmarks guide needle placement for the adductor canal block?",
 "answer":"High-frequency linear transducer positioned transverse over medial thigh at midpoint between ASIS and superior patellar pole; identify femoral artery/vein deep to sartorius; saphenous nerve lies anterior to artery; inject 15-20 mL under sartorius fascia",
 "rationale":"The subsartorial position of the saphenous nerve requires injection deep to the sartorius muscle fascia to achieve reliable nerve contact.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1668}],"confusable_with":"Femoral nerve block (proximal to adductor canal, anterior approach)"},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the fascia iliaca block and which nerves does it typically affect?",
 "answer":"Fascia iliaca block: two 'pops' through fascia lata and fascia iliaca proximal to femoral artery bifurcation; typically affects femoral nerve AND lateral femoral cutaneous nerve",
 "rationale":"Injecting under the fascia iliaca proximal to the femoral nerve allows spread to cover both the femoral nerve and the lateral femoral cutaneous nerve, providing hip and anterior thigh analgesia.",
 "bloom":"recall","source":[{"book":"Stanford CA-1","page":98}],"confusable_with":"Femoral nerve block (more targeted, may miss LFCN)"},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"Why is obturator nerve block often added to femoral and sciatic nerve blocks for complete knee anesthesia?",
 "answer":"Obturator nerve block is usually required for complete anesthesia of the knee; also prevents adductor muscle spasms during transurethral bladder resection",
 "rationale":"The obturator nerve innervates the medial aspect of the knee joint capsule; without obturator block, patients may experience medial knee pain despite femoral + sciatic coverage.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1660}],"confusable_with":""},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the posterior lumbar plexus (psoas compartment) block used for and what nerves does it block?",
 "answer":"Posterior lumbar plexus block used for hip, knee, and anterior thigh procedures; blocks femoral, lateral femoral cutaneous, AND obturator nerves (complete lumbar plexus)",
 "rationale":"Psoas compartment injection surrounds the lumbar plexus within the psoas muscle, blocking all three major branches in a single injection.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1662}],"confusable_with":"Femoral nerve block (only one branch of the lumbar plexus)"},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What perineural adjuvant prolongs regional nerve blocks, and what systemic side effect is reduced by its perineural administration?",
 "answer":"Perineural dexamethasone (preservative-free) prolongs regional nerve blocks; reduces systemic absorption of local anesthetic, lowering peak plasma levels",
 "rationale":"Perineural dexamethasone acts locally on nerve membrane and reduces local inflammation; epinephrine also reduces peak plasma LA levels via vasoconstriction.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":343}],"confusable_with":""},
]

kps.append({"_type":"confusable_pair","topic_a":"Adductor canal block","topic_b":"Femoral nerve block",
 "discriminator":"Adductor canal: primarily sensory (saphenous nerve), spares quadriceps, better for TKA rehabilitation; femoral nerve block: complete quadriceps motor block, better for surgical anesthesia but impairs ambulation"})

# ============================================================
# [19] Fentanyl, sufentanil, alfentanil: comparative pharmacology
# Chunks mostly off-topic; use available opioid pharmacology content
# ============================================================
t = "Fentanyl, sufentanil, alfentanil: comparative pharmacology"
dom = "Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)"
disc = "anesthesia"
s = "fentanyl-sufentanil"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"Why is fentanyl preferred over morphine for labor analgesia when systemic opioids are used?",
 "answer":"Fentanyl has short duration of action and no active metabolites; in small IV bolus doses (50-100 mcg/hour), no significant differences in neonatal Apgar scores or respiratory effort versus non-opioid-exposed newborns",
 "rationale":"Morphine has active metabolites that accumulate and cause prolonged neonatal depression; fentanyl's rapid redistribution limits neonatal exposure.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":609}],"confusable_with":"Morphine (active metabolites, prolonged neonatal effects)"},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the context-sensitive half-time of remifentanil and how does it differ from fentanyl/sufentanil/alfentanil?",
 "answer":"Remifentanil has a very short, infusion-duration-INDEPENDENT context-sensitive half-time (not context-sensitive); fentanyl/sufentanil/alfentanil have context-SENSITIVE half-times that increase with prolonged infusion",
 "rationale":"Remifentanil is hydrolyzed by nonspecific esterases in blood and tissues, independent of hepatic/renal function, making offset predictable regardless of duration.",
 "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":307}],"confusable_with":"Alfentanil (short duration but context-sensitive)"},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"What dose of fentanyl or sufentanil is added to intrathecal local anesthetic to significantly potentiate the block for cesarean delivery?",
 "answer":"Fentanyl 12.5-25 mcg or sufentanil 5-7.5 mcg added intrathecally significantly potentiates the block",
 "rationale":"Intrathecal opioids act synergistically with local anesthetics at the dorsal horn, reducing the required local anesthetic dose and extending block quality.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1402}],"confusable_with":""},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"In elderly patients, what change in fentanyl sensitivity is observed and what is the pharmacokinetic basis?",
 "answer":"Enhanced sensitivity to fentanyl, alfentanil, and sufentanil in elderly; both pharmacokinetic and pharmacodynamic factors responsible; older patients require approximately 50% lower blood levels of propofol for anesthesia",
 "rationale":"Reduced clearance, smaller distribution volumes, and increased receptor sensitivity in elderly patients mean lower doses produce equivalent or greater effect.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1507}],"confusable_with":""},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the rapid IV chest wall rigidity complication associated with large doses of opioids, and which opioids are most implicated?",
 "answer":"Rapid administration of larger doses of fentanyl, sufentanil, remifentanil, and alfentanil can induce chest wall rigidity severe enough to prevent bag-mask ventilation",
 "rationale":"High-dose rapid opioid administration causes glottic and thoracic muscle rigidity via central mu receptor activation; can be treated with succinylcholine or NMBAs.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":299}],"confusable_with":"Laryngospasm (different mechanism, different treatment)"},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is remifentanil's mechanism of metabolism and what does this imply for patients with hepatic or renal failure?",
 "answer":"Remifentanil is biotransformed by nonspecific blood and tissue esterases (not hepatic or renal); minimally affected by hepatic or renal failure",
 "rationale":"Ester hydrolysis by ubiquitous tissue esterases produces an inactive metabolite; this organ-independent clearance makes remifentanil ideal for critically ill patients.",
 "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":307}],"confusable_with":"Morphine (renally excreted active metabolites, contraindicated in renal failure)"},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What clinical caution applies to the use of meperidine in patients with kidney disease?",
 "answer":"Meperidine should be avoided in kidney failure because normeperidine (an active metabolite) accumulates and causes CNS excitability, seizures",
 "rationale":"Normeperidine is excreted by the kidney; accumulation lowers the seizure threshold and causes dysphoria; no reversal agent is available for normeperidine toxicity.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1116}],"confusable_with":"Morphine-6-glucuronide accumulation (causes narcosis, not seizures)"},
]

# ============================================================
# [20] Fetal physiology and assessment
# ============================================================
t = "Fetal physiology and assessment"
dom = "Obstetric anesthesia (maternal physiology, labor analgesia, cesarean anesthesia, preeclampsia/eclampsia, obstetric hemorrhage, emergencies, fetal considerations)"
disc = "anesthesia"
s = "fetal-physiology"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What maternal respiratory changes during pregnancy reduce oxygen reserve and predispose to rapid desaturation?",
 "answer":"Decreased FRC (reduced ERV), increased O2 consumption, elevated diaphragm; FRC returns to baseline by 48 hours postpartum; NO change in vital capacity",
 "rationale":"Decreased FRC with increased O2 consumption creates minimal apnea-to-desaturation time; preoxygenation is critical before any anticipated apnea.",
 "bloom":"recall","source":[{"book":"Stanford CA-1","page":100}],"confusable_with":""},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What preoxygenation protocol is recommended before general anesthesia in the parturient?",
 "answer":"Breathe 100% oxygen for 3 minutes before anticipated apnea; OR four maximal breaths over 30 seconds if emergent GA is needed",
 "rationale":"Decreased FRC and increased O2 consumption mean standard preoxygenation intervals from non-pregnant patients are insufficient; nitrogen washout is accelerated by the physiologic changes.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":605}],"confusable_with":"Non-pregnant preoxygenation (3 min sufficient but FRC is larger)"},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"What cardiovascular change peaks during active labor and immediately postpartum?",
 "answer":"Peak cardiac output occurs during active labor and immediately after delivery (autotransfusion from uterine contraction); pregnancy increases CO by 40% and SV by 30%",
 "rationale":"Uterine contraction during labor expels blood into maternal circulation (auto-transfusion effect), further increasing already elevated CO.",
 "bloom":"recall","source":[{"book":"Stanford CA-1","page":100}],"confusable_with":""},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"All opioids readily cross the placenta. What are the key neonatal effects?",
 "answer":"All opioids cross placenta and can cause: decreased fetal heart rate variability and neonatal dose-related respiratory depression; maternal side effects include nausea, vomiting, pruritus, delayed gastric emptying",
 "rationale":"Fetal opioid exposure depends on maternal dose, timing relative to delivery, and drug lipophilicity; all current clinical opioids achieve fetal plasma concentrations.",
 "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":609}],"confusable_with":""},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the respiratory alkalosis compensation of pregnancy and what is its clinical implication for epidural/spinal dosing?",
 "answer":"Pregnancy causes hyperventilation -> respiratory alkalosis -> compensatory lower bicarbonate; PaCO2 decreases (~30 mmHg); affects local anesthetic pKa equilibrium favoring more un-ionized drug",
 "rationale":"The lower maternal PaCO2 shifts LA equilibrium toward un-ionized form, enhancing nerve penetration; also affects pH-based drug calculations for epidural dosing.",
 "bloom":"analyze","source":[{"book":"Stanford CA-1","page":100}],"confusable_with":""},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What cardiac structural immaturity makes the neonatal heart dependent on a different mechanism for contractility compared to adults?",
 "answer":"Neonatal myocardium has poorly organized myocytes with fewer contractile elements and immature sarcoplasmic reticulum; depends heavily on FREE IONIZED CALCIUM concentration for contractility (not SR calcium release)",
 "rationale":"Immature T-tubules and SR mean neonates rely more on extracellular calcium influx; blood transfusion-related hypocalcemia can cause significant neonatal cardiac depression.",
 "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":639}],"confusable_with":"Adult myocardium (relies on SR calcium cycling)"},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What emergency obstetric guideline applies if a pregnant patient suffers cardiac arrest and cannot be resuscitated?",
 "answer":"Emergent cesarean delivery should be performed within 5 minutes of maternal cardiac arrest if mother is not resuscitated; improves survival chances for both mother and neonate",
 "rationale":"Aortocaval compression by the gravid uterus reduces cardiac output during CPR; delivery relieves compression and may allow successful resuscitation of the mother.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":615}],"confusable_with":""},
]

print(f"KPs so far: {len(kps)}")

with open('C:/Users/Dean/anesthesia_attending/data/_kps_batch4.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Batch 4 saved OK")
