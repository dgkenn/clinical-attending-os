# Clinical value audit — all 178 knowledge points

Read every point and judged it against the actual goal: a transitional-year
intern doing general medicine for one year, then anesthesiology, who needs
applied ward/ICU knowledge with critical-care depth — not internal-medicine-
resident breadth.

**Headline: the content is good.** Nearly every point is decision-relevant and
actionable — "give calcium first, it stabilises the membrane and does NOT lower
K", "aortic dissection: beta-blocker BEFORE vasodilator to reduce dP/dt". That
is the right grain. The problems below are not about bad medicine; they are
contradictions, redundancy, and a handful of items that are not knowledge at all.

---

## 1. SAFETY — contradictory numbers being drilled simultaneously

**DKA: hold insulin below what potassium?** Three cards, two different numbers:

| id | threshold | status |
|----|-----------|--------|
| 14 | K+ < **3.5** | learning |
| 38 | K+ < **3.5** | learning |
| 245 | K+ < **3.3** | learning |

The ADA standard is **3.3 mEq/L**. Cards 14 and 38 teach 3.5. Spaced repetition
is currently reinforcing both, which is worse than teaching neither — on a real
patient you would hesitate at exactly the wrong moment.

This is the one finding I would not defer. **Recommend: correct 14 and 38 to
3.3, or delete them and keep 245.** Flagging rather than auto-editing because
if your institution's protocol genuinely uses 3.5, you should be the one to say so.

**Hyponatremia correction rate** (id 248): "max 12 mEq/L in 24 hours (some say
10)". Current practice has moved toward **8 mEq/L/24h in high-risk patients**
(malnutrition, alcoholism, hypokalemia, Na <105) with 10–12 as an outer bound.
The card is not wrong but sits at the aggressive end without naming the
high-risk caveat. **Recommend: add the 8 mEq/L high-risk qualifier.**

---

## 2. NOT KNOWLEDGE — learning objectives stored as facts

Four cards are question stems or objectives, not testable facts. These are
artifacts of the derived-knowledge-point fallback, which names a fact after the
question that produced it:

| id | text | problem |
|----|------|---------|
| 185 | "**State** the immediate next management priority for suspected high-risk PE" | an instruction, not a fact |
| 184 | "**Recognize** hemodynamic instability/shock as the immediate threat..." | an objective |
| 201 | "**Use** a structured pretest probability tool such as Wells criteria" | too vague to test |
| 199 | "**Use** D-dimer in low pretest probability suspected PE" | borderline — real content, weak phrasing |

184/185/201 can never be graded meaningfully: there is no specific answer they
test. **Recommend: delete 184, 185, 201.** The underlying content is already
covered properly by ids 145, 150, 151.

---

## 3. REDUNDANCY — ~29% of the review load is the same concept re-carded

This is the direct cause of the review-time problem, and it is bigger than the
exact-duplicate merge already done (those were textual near-copies; these are
the *same idea* worded differently enough that no matcher should merge them
automatically).

| cards | concept |
|-------|---------|
| 8 | hypoglycemia treatment (PO vs IV, dose, recheck interval) |
| 7 | Wells score / D-dimer usage |
| 6 | FeNa prerenal vs intrinsic |
| 6 | variceal bleed ceftriaxone |
| 6 | delirium: avoid benzos/Benadryl |
| 5 | STEMI beta-blocker holds |
| 4 | ARDS tidal volume |
| 4 | NSTEMI TIMI risk stratification |
| 4 | HE lactulose/rifaximin |
| 3 | shunt vs V/Q O2 response |
| 3 | muddy brown casts / ATN |

**~51 excess cards. 178 → ~127.**

The STEMI beta-blocker cluster shows the mechanism clearly: ids 7, 8, 9, 10 are
four separate cards each holding ONE contraindication (bradycardia, hypotension,
bronchospasm, decompensated HF), plus id 13 listing all four. That came from one
bundled question being decomposed per-fact. **Over-decomposition:** a four-item
list should be ONE card testing the list, not four cards plus a summary — you
will never be asked "name the third contraindication."

**Recommend: consolidate each cluster to one well-worded card, preserving the
combined review history** (the merge script already does this safely).

---

## 4. LOW YIELD for this specific path — small, judgment calls

Not wrong, just poor value for a TY intern → anesthesia:

- **id 85** — nephrotic syndrome fatty casts / Maltese crosses under polarised
  light. Classic exam trivia; you will not act on it this year.
- **id 34** — G6PD deficiency trigger list. Low frequency; the anesthesia-relevant
  piece (avoid in specific drugs) is thin here.
- **id 149** — Wells PE component point values (+1.5, +3...). Memorising the
  weights is low-yield; using the score is what matters, and id 150 covers that.

Keeping is defensible — none is harmful. Listed for your call.

**Explicitly NOT flagged** (checked and worth keeping despite looking niche):
DDAVP for uremic platelet dysfunction (id 36 — genuinely pre-procedure
relevant), succinylcholine subacute SCI window (25, 26 — core anesthesia
safety), LEMON (23), CURB-65 (159).

---

## 5. STRUCTURAL — topic fragmentation

- **"GI bleed" (7 cards) and "Gastrointestinal bleeding" (3 cards)** are the same
  topic under two names. Splits the schedule and the coverage map.
- **"PE" (9) and "DVT/PE" (8)** overlap heavily.
- **id 77** — a delirium fact ("avoid benzos and opioids") filed under
  **Electrolytes**. Misfiled.

**Recommend: merge the GI bleed pair; merge id 77 into Delirium.** PE vs DVT/PE
is arguable — they are genuinely adjacent but distinct workups — so left alone.

---

## Suggested order

1. **DKA potassium contradiction** (safety, today)
2. Delete the three non-facts (free, no judgement needed)
3. Merge GI bleed topics + refile id 77 (structural, safe)
4. Consolidate the redundancy clusters (~29% review-time reduction)
5. Low-yield items — your call, no urgency

---

## RESOLVED — 2026-08-18

**DKA potassium threshold.** User confirmed 3.3 mEq/L. The three contradictory
cards were consolidated into one, teaching 3.3, with the combined review
history preserved. Zero cards now teach 3.5.

**Redundancy consolidation.** 14 near-duplicate cards folded away after
per-pair clinical judgement, not a blanket similarity rule. Two contrasts were
preserved by rewriting rather than discarding: the ARDS card now carries BOTH
"ideal not actual body weight" and "not high PEEP", and the D-dimer card
carries both the low- and high-probability halves of the rule.

**Deliberately NOT merged** — related but clinically distinct, where merging
would have destroyed knowledge:

- "FeNa unreliable on diuretics, use FeUrea" vs the <1% / >2% thresholds. The
  first is the caveat that the number cannot be trusted at all; losing it means
  misreading a FeNa in exactly the patient where it misleads.
- "Norepinephrine first-line over dopamine" (the choice) vs "dopamine's
  arrhythmia risk is beta-1 mediated" (the mechanism). Different questions.

**Original 29% estimate was wrong** and is corrected in the commit history: it
came from a keyword regex that lumped the AEIOU-TIPS mnemonic and DKA D5 cards
into a "hypoglycemia treatment" cluster. Measured with the fact-matcher, the
real figure was 21 near-duplicate pairs, and consolidation removed 14 cards.

**Structural fixes so this does not regrow** (see commit history): the tutor now
receives `existing_facts` for a topic so it reinforces rather than re-cards,
instructions forbid splitting one list into per-item cards, and
record_knowledge_point fuzzy-dedupes at the write layer for every caller.
