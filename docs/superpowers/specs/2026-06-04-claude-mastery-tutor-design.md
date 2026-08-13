# Claude Mastery Tutor for Medical Learning
## Complete Design Specification

**Date:** 2026-06-04  
**Author:** Claude Code  
**Status:** Design Review (awaiting user approval)  
**Target User:** Dean Kennedy, MD — Intern Year Medicine + Future Anesthesia

---

## 1. EXECUTIVE SUMMARY

This system is a **persistent, evidence-based mastery learning tutor** accessible via Claude (MCP server), replacing the current Custom GPT interface while maintaining the existing backend (retrieval + FSRS + session memory).

**Core promise:** Guide the user to 100% mastery of core medical knowledge through adaptive, spaced retrieval practice over 1-2 years, starting with bread-and-butter intern medicine (80%), then ICU (10%), then anesthesia depth (10%).

**Key innovation:** Dual-interface (Claude + Custom GPT) backed by a single MCP server + SQLite state, so learning persists across all entry points.

---

## 2. LEARNING OUTCOMES & MASTERY CRITERIA

### 2.1 Three-Tier Mastery Model

**Tier 1: Bread & Butter (Intern Year Focus, 60-80 topics)**  
High-frequency, high-mortality conditions appearing in 80% of overnight calls:
- Sepsis/infection (pneumonia, UTI, meningitis, endocarditis)
- Cardiovascular (ACS, arrhythmias, heart failure, hypertensive urgency/emergency)
- Respiratory (dyspnea, hypoxia, asthma/COPD exacerbation, PNA)
- GI (upper/lower GI bleed, acute abdomen, pancreatitis, cholecystitis)
- Renal (AKI, hyperkalemia, hyponatremia, fluid management)
- Neuro (altered mental status, seizure, stroke/TIA, meningitis)
- Endocrine (DKA, HHS, hypoglycemia, thyroid storm)
- Toxicology (overdose, poisoning, reversal agents)
- Procedures (central lines, intubation, thoracentesis, LP)

**Tier 2: Important but Infrequent (6-12 months, 40-60 topics)**  
Specialty topics, chronic disease management, preventive medicine:
- Rheumatology, oncology, endocrinology depth, sleep medicine, etc.

**Tier 3: Esoteric (Post-Intern, 60+ topics)**  
Rare zebras, edge cases, deep-dive reading.

### 2.2 Mastery Criteria (Multi-Dimensional)

A topic is mastered when student demonstrates:

1. **Accuracy on in-distribution cases** — ≥85% accuracy on textbook-style questions
2. **Transfer to novel cases** — ≥80% AUC on out-of-distribution scenarios (different patient, same diagnosis)
3. **Mechanistic reasoning** — Can explain **why** (not just "what"); teach-back rubric ≥3/4
4. **Calibration** — Reported confidence accuracy ICC ≥0.70 (knows what they don't know)
5. **Retention over time** — ≥80% accuracy at 6-month follow-up quiz
6. **Integration & synthesis** — Can integrate across domains (e.g., "young woman with seizure + hypertension + headache → pre-eclampsia")

**Operational thresholds:**
- **Baseline (new topic):** 70% accuracy on 3 attempts + confidence accuracy ≥0.60 + mechanism articulated
- **Intermediate (drilling):** 80% accuracy on 5 recent attempts + <2 overconfident errors in last 10 + near-transfer success
- **Advanced (mastery):** 90% accuracy on 8 recent attempts + overconfidence rate <0.15 + far-transfer success + teach-back ≥95%

---

## 3. CURRICULUM STRUCTURE (THREE PHASES)

### 3.1 Phase 1: Foundation (Weeks 1-4, ~50-65 hours ingestion)

**Goal:** Establish frameworks that unlock all downstream learning

**Topics to master:**
- H&P methodology & differential diagnosis templates
- Evidence-based medicine basics (study design, p-values, GRADE)
- NIHSS scoring (stroke)
- Status epilepticus recognition & benzodiazepine dosing
- Meningitis CSF interpretation & empiric antibiotics (age-stratified)

**Learning outcomes:**
- Generate differentials for dyspnea, chest pain, AMS, fever
- Score NIHSS correctly on stroke scenarios
- Recognize seizure emergencies, order appropriate therapy
- Interpret CSF, select empiric antibiotics

**Sources (free online):**
- Washington Manual H&P chapter + AHA/ASA Stroke Guidelines 2024 (PDF, free)
- IDSA Meningitis Guidelines (free PDF)
- UpToDate "Clinical Approach to..." modules (if institutional access)
- Guyatt's Users' Guides to Medical Literature (BMJ Learning, free via BU/institutional access)

**Cumulative units:** 550-750

### 3.2 Phase 2: High-Frequency Diagnoses (Weeks 5-12, ~65-75 hours ingestion)

**Goal:** Master 80% of overnight call scenarios

**Bread-and-butter topics:**
- Pneumonia (CAP/HAP) + antibiotic stewardship
- ACS / Valvular heart disease
- PE/DVT
- GI bleeding (upper & lower)
- COPD/asthma exacerbation
- Diabetes (type 1 & 2, chronic management)
- Thyroid disease (hypo, hyper, thyroid storm)
- Renal (AKI, hyperkalemia, hyponatremia)
- Sepsis management

**Learning outcomes:**
- Use CURB-65 + select pneumonia antibiotics by local resistance
- Interpret ECG in ACS, order troponin kinetics
- Stratify PE risk (Wells score), interpret D-dimer
- Manage GI bleeding (transfusion thresholds, PPI dosing)
- Calculate insulin regimen, A1C targets
- Manage electrolyte disturbances with mechanism understanding

**Sources (free online):**
- IDSA Pneumonia Guidelines (IDSA.org)
- NAEPP Asthma, GOLD COPD guidelines (free)
- AHA/ACC CAD Guidelines (free)
- CHEST PE/DVT Guidelines (free)
- ADA Standards of Care (free)
- AACE Thyroid Guidelines (free)
- UpToDate modules (if available)
- Free cardiology tutorials (StatPearls, NEJM Journal Watch)

**Cumulative units:** 1,550-1,950

### 3.3 Phase 3: Breadth & Integration (Weeks 13-20, ~65-77 hours ingestion)

**Goal:** Complete core medicine knowledge; prepare for rotations beyond intern year

**Additional topics:**
- Hematology (anemia, bleeding disorders, HIT, thrombocytopenia)
- Hepatic failure, cirrhosis, hepatitis
- Pancreatitis & cholecystitis
- Substance abuse & withdrawal (CIWA-Ar scoring)
- Psychiatry basics (depression, anxiety, suicide risk)
- Patient communication & palliative care
- Quality improvement & patient safety

**Learning outcomes:**
- Differentiate microcytic/macrocytic/normocytic anemia
- Manage alcohol withdrawal with CIWA-Ar
- Calculate Child-Pugh score
- Communicate advance directives appropriately

**Sources (free online):**
- AASLD Cirrhosis Guidelines (free)
- ASGE GI Bleeding Guidelines (free)
- Addiction Medicine UpToDate (if subscribed)
- Stanford Serious Illness Conversation Guide (free online modules)
- IHI Open School (free quality improvement modules)
- Free psychiatry resources (MoodGYM, SAMHSA)

**Cumulative units:** 2,478-3,078 (final)

---

## 4. KNOWLEDGE BASE ACQUISITION & INGESTION

### 4.1 Current Inventory

| Source | Chunks | Coverage | Status |
|--------|--------|----------|--------|
| MGH Housestaff Manual | 6,503 | 95% medicine | ✓ Active |
| Marino ICU | 7,134 | 95% ICU | ✓ Active (re-phase as ICU-specific) |
| Morgan & Mikhail | 29,609 | 98% anesthesia | ✓ Active |
| Miller Basics | 18,636 | 100% CA-1 anesthesia | ✓ Active |
| Stanford CA-1 | 1,237 | 100% CA-1 anesthesia | ✓ Active |
| Intern Survival (fragmented) | 1,508 | 100% medicine | ✓ Active (consolidate 3 PDFs) |
| **Personal Notes** | 0 | — | Planned |
| **Missed Questions** | 0 | — | Planned (auto-populate from logs) |

### 4.2 Gap-Filling Strategy: Free Online Sources

**Phase 1 sources** (free, high-authority):
1. **AHA/ASA Stroke Guidelines 2024** (PDF, americanheart.org) → NIHSS, imaging gates
2. **IDSA Meningitis Guidelines** (PDF, IDSA.org) → CSF, empiric antibiotics
3. **Washington Manual H&P chapter** (used book $20-40, or library) → methodology
4. **Guyatt's Guide chapters 1-4** (BMJ Learning free via BU institutional access) → EBM

**Phase 2 sources** (free, authoritative):
1. **IDSA Pneumonia Guidelines 2023** (PDF, IDSA.org)
2. **NAEPP Asthma Guidelines 2024** (PDF, naepp.asthma.edu)
3. **GOLD COPD Guidelines 2024** (PDF, goldcopd.org)
4. **AHA/ACC CAD Guidelines 2023** (PDF, americanheart.org)
5. **CHEST PE/DVT Guidelines 2023** (PDF, chestjournal.org)
6. **ADA Standards of Care 2024** (PDF, diabetes.org)
7. **AACE Thyroid Guidelines 2016** (PDF, aace.com)
8. **UpToDate "Clinical Approach to..." modules** (if institutional access, ~$0)
9. **Free StatPearls** (NIH repository, free) — cardiology, GI, nephrology chapters

**Phase 3 sources** (free, supplemental):
1. **AASLD Cirrhosis Guidelines** (PDF, aasld.org)
2. **ASGE GI Bleeding Guidelines** (PDF, asge.org)
3. **Stanford Serious Illness Conversation Guide** (free online, stanford.edu)
4. **IHI Open School** (free modules, ihi.org) — quality improvement
5. **Addiction Medicine UpToDate** (if subscribed)
6. **Free psychiatry** (MoodGYM, SAMHSA materials)

**Cost:** ~$20-60 (Washington Manual used copy) + ~$0 for guideline PDFs (all public domain or institutional UpToDate) = **minimal outlay**

### 4.3 Ingestion Plan

**Week 1-4 (Phase 1):**
- Download 4 free PDFs + secure Washington Manual
- Extract facts + chunks for H&P, differential, NIHSS, seizures, meningitis
- Create 550-750 curriculum units
- Run `/ingest --force` and validate retrieval quality

**Week 5-12 (Phase 2):**
- Download 8 guideline PDFs + UpToDate access (if available)
- Parallel ingestion: pneumonia + cardiology + pulmonary + GI + renal + endocrinology
- Create 1,000-1,200 curriculum units
- Deduplicate against existing Marino/Morgan content; resolve any conflicts

**Week 13-20 (Phase 3):**
- Ingest hematology + hepatology + psychiatry + communication modules
- Create 800-1,000 curriculum units
- Final deduplication + quality audit

---

## 5. MCP SERVER ARCHITECTURE

### 5.1 New MCP Endpoints

The backend will expose these tools to Claude:

```
retrieval(query: str, mode: str, max_results: int)
  → Returns chunks + citations from ingested sources
  → Modes: "intern_teach", "icu_teach", "anesthesia_boards"
  → Used by: Claude to fetch source material for explanations

get_session_state()
  → Returns current student state: FSRS due dates, weak topics, mastery matrix
  → Used by: Claude on session start to load context

get_next_topic()
  → Returns what should be studied next (FSRS-prioritized + coverage gaps)
  → Considers: phase (medicine/ICU/anesthesia), weak topics, unmastered concepts
  → Used by: Claude to guide lesson selection

submit_answer(topic, result, mastery_signals)
  → Logs student attempt; updates FSRS, mastery vector, weak flags
  → Takes: answer correctness, confidence, teach-back quality, transfer success
  → Used by: Claude after each lesson to persist learning

get_coverage_gaps()
  → Returns topics from curriculum that haven't been studied yet
  → Used by: Claude to identify "what's left to master"

mark_topic_mastered(topic, confidence)
  → Final mastery gate; removes from active rotation (moves to maintenance review)
  → Used by: Claude when all mastery criteria met

get_weak_patterns()
  → Returns repeat-offender (topic, mistake_type) pairs
  → Used by: Claude to detect patterns & recommend focused drilling

get_progress()
  → Returns % mastery by band (intern_core / icu / anesthesia), % complete overall
  → Used by: Claude to show student progress & motivation
```

### 5.2 Session Flow (Claude via MCP)

```
1. User opens Claude chat → "Start a lesson"
   ↓
2. Claude calls MCP: get_session_state() 
   → Loads FSRS due dates, weak topics, mastery progress
   ↓
3. Claude calls MCP: get_next_topic()
   → Decides: which topic to teach next (due date? weak? coverage gap?)
   ↓
4. Claude calls MCP: retrieval("hyperkalemia mechanism", mode="intern_teach")
   → Gets textbook chunks + citations for explanation
   ↓
5. Claude teaches the lesson:
   - Warm-up: cloze card or quick recall
   - Drilling: active-recall questions + mechanism focus
   - New material: case presentation
   - Case application: "what would you do first?"
   - Teach-back: "explain this to an MS3"
   ↓
6. Student answers → Claude evaluates (correct? confidence? mechanism sound?)
   ↓
7. Claude calls MCP: submit_answer(
     topic="hyperkalemia",
     result="correct",
     confidence_reported=4,
     teach_back_quality="strong",
     transfer_success=true
   )
   → FSRS updates interval, mastery vector updates, weak flags clear
   ↓
8. Claude asks if student wants another topic or break
   ↓
9. Session ends → State persisted in SQLite
   ↓
10. Next session: Claude auto-loads updated state, continues from where left off
```

### 5.3 Integration with Existing Backend

**No breaking changes to FastAPI:**
- Existing `/next_lesson`, `/submit_answer` endpoints remain unchanged (for Custom GPT)
- MCP server is a **new interface** exposing the same SQLite state + retrieval layer
- Both Claude (MCP) and Custom GPT can write to the same SQLite database
- State is **bidirectional**: learning in Claude persists when switching to Custom GPT and vice versa

---

## 6. CLAUDE-SPECIFIC PEDAGOGY

### 6.1 Session Structure (Adaptive, 30-60 min)

Each session Claude will:

1. **Load state** (5 sec)
   - Current FSRS queue, weak topics, phase (intern/ICU/anesthesia)

2. **Pick topic** (30 sec)
   - If FSRS due date exists: review that first
   - Else if weak topic flag: drilling on weak area
   - Else: new material from curriculum
   - Else: cross-topic integration (stretch goal)

3. **Teach using 5-phase pedagogy** (25-45 min):
   - **Warm-up** (2 min): Cloze card recall or quick "what's the mechanism?"
   - **Drilling** (8 min, if mastery <85%): 3 active-recall questions targeting weak mechanism
   - **New material** (8 min, if new): Textbook explanation + worked example case
   - **Case application** (5 min): "What would you do first?" clinical scenario
   - **Teach-back** (2 min): "Explain this to a colleague" without notes

4. **Evaluate understanding** (2 min):
   - Accuracy: correct/partial/incorrect
   - Confidence: 1-5 scale
   - Mechanism articulation: does teach-back include causal language?
   - Transfer: can student apply to novel case?

5. **Submit to backend** (10 sec)
   - Log answer + signals → FSRS updates

6. **Offer next action** (30 sec):
   - "Ready for another? Or take a break?" (enforce 40-50 min max)
   - If fatigue detected: suggest break or lighter phase

### 6.2 Mastery-Gated Phase Skipping

Claude learns the student's mastery level via MCP and **adapts the lesson flow**:

- **If accuracy ≥90%** → Skip warm-up & drilling → Jump to cases + teach-back (saves 15 min)
- **If accuracy 85-89%** → Skip warm-up → Go to drilling (saves 5 min)
- **If accuracy <70%** → Do full 5-phase (normal)

This respects the student's time while preventing boredom.

### 6.3 Confidence-Weighted FSRS

Claude will **amplify review for overconfident errors**:

- Confident + correct → Normal FSRS interval (e.g., day 3, day 10, day 30)
- Confident + wrong → **3.5× boost** (e.g., day 1.4, day 3, day 10) — Dunning-Kruger risk
- Uncertain + correct → Slight boost (×1.2) — learner is calibrated, reward
- Uncertain + wrong → Normal interval (mistake is expected; learner knows it)

This prevents false confidence from masking gaps.

### 6.4 Session Pacing & Fatigue Detection

Claude will monitor:
- **Time-on-task per question** — If >90 sec, offer break or re-teach
- **Accuracy slope** — If trending down over 5 questions, suggest fatigue
- **Session duration** — Cap at 40-50 min (enforce with soft warnings at 35 min)

If fatigue detected: "Take 30 seconds — I'll wait" or "Switch to a lighter phase?"

---

## 7. TIMELINE & MASTERY TARGETS

### 7.1 Year 1: Foundation & High-Frequency Diagnoses

**Target:** 400 core intern medicine concepts at mastery level  
**Time investment:** 2 hours/day × 6 days/week = ~600 hours/year  
**Expected progression:**
- **Months 1-3:** Tier 1 bread-and-butter (60-80 topics) → 85% mastery
- **Months 4-8:** Additional Tier 1 coverage + integration
- **Months 9-12:** Consolidation via spaced retrieval + maintenance

**Success metrics:**
- End of month 3: Student scores ≥85% on ABIM-style intern medicine questions
- End of month 6: ≥80% transfer AUC (novel cases)
- End of year: Passing score on self-administered ABIM intern-level questions

### 7.2 Year 2: Breadth, Advanced Medicine, & Anesthesia Foundation

**Target:** 600-800 additional concepts (Tier 2 + ICU + early anesthesia)  
**Time investment:** 1-1.5 hours/day, lower frequency (spacing wins over new material)

**Expected progression:**
- **Months 1-6:** ICU rotations; Marino content becomes primary
- **Months 7-12:** Anesthesia rotation; Morgan & Mikhail + Miller content accelerates

**Success metrics:**
- ICU rotation end: Can manage sepsis, ARDS, shock with independent reasoning
- Anesthesia rotation end: Passes CA-1 milestones; prepared for BASIC exam

### 7.3 Spacing Schedule (Evidence-Based)

**For Tier 1 topics (highest priority):**
- Day 1: Warm-up review (same-day)
- Day 3: Drilling phase (active recall)
- Day 7: Case application
- Day 14: Teach-back + confidence recalibration
- Day 30: Maintenance review (spaced)
- Day 60-90: Monthly maintenance (if mastery ≥90%)

**Overconfidence penalty:** ×0.7 multiplier (return earlier if confident but wrong)  
**Mastery bonus:** ×1.3 multiplier (push out if teach-back success ≥3 times)

**For Tier 2 topics (secondary):**
- Longer intervals (day 5, 14, 30, 60+)
- Less frequent drilling; more synthesis

---

## 8. KNOWLEDGE MANAGEMENT & VERSIONING

### 8.1 Medical Knowledge Evolution

This system will acknowledge that medical guidelines change:

- **Quarterly knowledge audit** (vs. UpToDate, current AHA/ACC/IDSA guidelines)
- **Version-stamped facts** — All ingested chunks include source + date
- **Uncertainty labeling** — "High certainty" vs. "Evolving" vs. "Expert disagreement"
- **Mechanism for teaching disagreement** — When evidence conflicts, explain why experts disagree

**Example:** Sepsis bundle evolution:
- Fact v1 (2015): "Sepsis = lactate → cultures → fluids → antibiotics → pressors"
- Fact v2 (2021): "Randomized trials showed some sepsis subgroups harmed by aggressive fluids"
- Fact v3 (2026): "Lactate clearance is prognostic but not necessarily a treatment target"
- **Teaching approach:** Teach the evolution; student learns that medicine is a moving target

### 8.2 Personal Notes & Missed Questions

Two high-rank libraries remain to be populated:

1. **Personal Notes** — User can drop PDFs of their own notes; system chunks them with rank=105 (highest priority in retrieval)
2. **Missed Questions** — Auto-populated from `/submit_answer` failures; system logs all incorrect attempts, chunks them with rank=110 (highest), resurfaces them at T+1d, T+3d, T+10d

---

## 9. SUCCESS METRICS & VALIDATION

### 9.1 Learning Gain Validation

**Pre/post assessments:**
- **Baseline:** User takes 20-question ABIM-style quiz on Tier 1 topics (day 1)
- **Month 3 check:** Same difficulty quiz → Compare accuracy (target: +25% improvement)
- **Month 6 check:** ABIM-style + transfer questions (novel cases) → Target: +30% improvement, ≥80% transfer AUC
- **Month 12 check:** Comprehensive Tier 1 quiz + integration questions → Target: ≥85% accuracy

**Retention validation:**
- **Month 6 follow-up:** Re-quiz on topics from months 1-2 → Target: ≥80% accuracy (no >10% decay)
- **Month 12 follow-up:** Same

**Calibration validation:**
- **Monthly:** Compare reported confidence vs. actual accuracy → Target: ICC ≥0.70 (well-calibrated)

### 9.2 Engagement & Compliance

- **Session frequency:** Target 5-6 sessions/week, 45 min average
- **Completion rate:** ≥90% of scheduled lessons started
- **Dropout risk:** If <2 sessions/week for 2 weeks, system sends check-in

### 9.3 Clinical Validation (Post-Intern Year)

- **Board exam performance:** Track ABIM exam scores; compare to peer cohort
- **Attendings feedback:** Collect qualitative feedback on preparedness, confidence, reasoning
- **Error tracking:** Monitor clinical error rates (medication, diagnosis) vs. baseline

---

## 10. SAFETY & LIMITATIONS

### 10.1 This System is NOT a Substitute for

- Real clinical supervision and feedback from attending physicians
- Live patient interaction and procedural practice
- Real-time decision-making under time pressure
- Ethics consultation for difficult cases

### 10.2 Design Assumptions & Limitations

- **Internet/local server required:** MCP server must run on local machine; assumes consistent network access
- **Learner autonomy:** System works best for self-motivated learners; cannot enforce compliance
- **Knowledge limits:** System is only as good as ingested sources; if a guideline is missing or outdated, system will reflect that
- **Mechanism teaching is hard:** Explaining "why" is more challenging than drilling "what"; Claude may oversimplify

### 10.3 When to Escalate to Human Teachers

System will recommend human consultation for:
- Topics with >3 failed mastery attempts (possible knowledge gap requiring re-teaching)
- Ethical dilemmas or cases with conflicting expert opinion
- Procedural skills (intubation, lines) — system can teach mechanics but cannot grade proficiency

---

## 11. IMPLEMENTATION ROADMAP (AT A GLANCE)

| Phase | Duration | Effort | Deliverable | Gate |
|-------|----------|--------|-------------|------|
| **Design & Gap-Fill** | Weeks 1-4 | 50-65h ingestion | 550-750 intern units | User approves this spec |
| **Phase 1 Launch** | Weeks 1-4 | (above) | MCP server live, Claude tutor works | 3/4 Phase 1 validation tests pass |
| **Phase 2 Expansion** | Weeks 5-12 | 65-75h ingestion | 1,000-1,200 additional units | 4/5 Phase 2 validation tests pass |
| **Phase 3 Breadth** | Weeks 13-20 | 65-77h ingestion | 800-1,000 final units | 4/5 Phase 3 validation tests pass |
| **Post-Launch Iteration** | Ongoing | Maintenance | Quarterly knowledge audits, missed-question logging | User feedback drives improvements |

---

## 12. FINAL DESIGN CHECKLIST

- ✅ **Curriculum:** 80% medicine (intern focus) / 10% ICU / 10% anesthesia depth
- ✅ **Mastery model:** 6-dimensional (accuracy, transfer, mechanism, calibration, retention, integration)
- ✅ **Pedagogy:** 5-phase adaptive (warm-up → drilling → new → cases → teach-back)
- ✅ **Spacing:** FSRS + phase-aware + confidence-weighted
- ✅ **MCP server:** 6 core endpoints exposing retrieval + FSRS + session management to Claude
- ✅ **Session structure:** 30-60 min adaptive lessons, fatigue-aware, phase-gating
- ✅ **Knowledge base:** 64,627 existing chunks + 2,350-2,950 new units from free online sources
- ✅ **Timeline:** 20 weeks ingestion, 1-2 year mastery arc
- ✅ **Success metrics:** Pre/post assessments, monthly calibration checks, board exam correlation
- ✅ **Safety:** Clear scope limitations, escalation paths for complex cases

---

## NEXT STEPS

1. **User reviews this spec** — Check for accuracy, gaps, concerns
2. **User approves** — If changes needed, I revise and re-present
3. **Invoke writing-plans skill** — Creates detailed implementation plan with step-by-step task breakdown
4. **Execute implementation** — Ingest sources, build MCP server, integrate with Claude

**Ready to proceed?**
