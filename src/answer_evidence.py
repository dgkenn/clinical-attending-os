"""Decide what an answer actually PROVES, rather than what it was graded.

Four recording failures found by diffing the 2026-08-18 session transcript
against the database. All four share a root cause: the system stored a verdict
without the evidence for the verdict, so nothing could be audited and wrong
states persisted invisibly. Each function here reconstructs the missing
evidence check.

1. PARTIAL ANSWERS CREDITED NOTHING. Grading is per-answer; knowledge is
   per-fact. On 5 of 7 partials only the corrected material was carded — the
   tutor said "your transfusion threshold knowledge is solid", "dose range is
   right", "epinephrine confirmed correct", and none of it was recorded
   anywhere. Demonstrated knowledge evaporated, so the fact stayed in the queue
   and came back. That is the "quizzing me on things I already know" problem,
   and it is structural. `evidence_supports` lets a per-fact verdict be checked
   against the user's own words instead of collapsing to one impression.

2. PARROTING SCORED AS KNOWLEDGE. Tutor: "...6 mL/kg of ideal body weight,
   since lung size tracks height." User, 47 seconds later: "You just told me
   since because lung size tracks height, not fat." Graded correct; the fact
   advanced to 3-of-5 on a three-day interval. He flagged it himself and the
   grader took it at face value. `detect_parroting` catches this mechanically,
   because the tutor cannot be trusted to self-report — it recorded
   teach_back_quality=0.5 on that same answer while still grading it correct.

3. TUTOR REPLIES STORED AS SUMMARIES. Two turns recorded "Rationale corrected
   to receptor mechanism rather than renal protection" instead of the actual
   teaching. The clinical content is simply gone from the audit trail.
   `looks_like_meta_summary` flags it while the session is still running.

4. FACTS WRITTEN BEFORE THEY WERE TAUGHT. A BiPAP mechanism card was created a
   minute BEFORE the BiPAP question was asked; likewise post-obstructive
   diuresis. The tutor batch-writes topic content rather than recording what was
   demonstrated, manufacturing cards nobody was tested on and then scheduling
   them as though they had been failed. `fact_was_covered` requires a fact to
   appear somewhere in the turn that supposedly taught it.

Everything is deterministic string work: no model call, no network, cheap
enough to run on every answer.
"""
from __future__ import annotations

import re
from typing import Iterable

# Words too common to carry evidence. Kept deliberately small — clinical text
# is dense with meaningful short tokens ("peep", "map", "iv") and an aggressive
# stopword list would strip the very terms that prove a fact.
_STOP = frozenset("""
a an and are as at be been but by can could do does for from had has have he
her him his how i if in into is it its me my no not of on or our out she so
than that the their them then there these they this those to too us was we
were what when where which who why will with would you your yours am been
being here just like get got very really much also then now non
""".split())

_WORD = re.compile(r"[a-z0-9][a-z0-9./%-]*")

# Said out loud by the user when restating something they were just handed.
# The observed case ("You just told me since because lung size tracks height")
# is caught by the first alternative. These are near-conclusive on their own.
_PARROT_PHRASES = re.compile(
    r"\b(you just (told|said|explained|mentioned)|as you (just )?said|"
    r"like you said|you (just )?told me|per what you said|"
    r"based on what you (just )?said|going off what you said)\b",
    re.I,
)


def content_words(text: str) -> set[str]:
    # The token pattern deliberately admits '.', '/', '-' and '%' INSIDE a word
    # so clinical quantities survive intact ("0.9%", "6ml/kg", "bun/cr",
    # "p/f"). That also swallows sentence-ending punctuation, which silently
    # broke matching: the tutor's "...tracks height." and the user's "tracks
    # height," tokenized to different strings, so a verbatim echo scored only
    # 50% overlap and slipped past detection. Strip trailing separators only —
    # never internal ones.
    out = set()
    for w in _WORD.findall((text or "").lower()):
        w = w.rstrip("./-%")
        if len(w) > 2 and w not in _STOP:
            out.add(w)
    return out


def _overlap(sub: Iterable[str], sup: Iterable[str]) -> float:
    """Share of `sub` present in `sup`. 0.0 when sub is empty."""
    sub, sup = set(sub), set(sup)
    return len(sub & sup) / len(sub) if sub else 0.0


def evidence_supports(evidence: str, verbatim: str, threshold: float = 0.6) -> bool:
    """True when `evidence` plausibly comes from what the user actually said.

    Token overlap rather than substring match, so a grader may lightly
    paraphrase ("hemoglobin of 7" for "a hemoglobin of seven") without failing,
    while evidence invented wholesale — the real risk, since an inventing
    grader is exactly how unearned credit gets written — does not pass.
    """
    ev = content_words(evidence)
    if not ev:
        return False
    return _overlap(ev, content_words(verbatim)) >= threshold


def detect_parroting(
    verbatim: str,
    prior_tutor_response: str,
    *,
    overlap_threshold: float = 0.65,
    max_content_words: int = 40,
) -> tuple[bool, str]:
    """Is this answer a restatement of what the tutor just said?

    Returns (is_parroted, reason). Two independent detectors:

    - An explicit admission ("you just told me"). Near-conclusive, and the
      case actually observed. Note the user volunteered it and was still
      graded correct, which is why this cannot be left to the grader.
    - High content-word overlap with the immediately preceding tutor turn on a
      SHORT answer. Length matters: a long answer that happens to reuse the
      tutor's vocabulary is usually genuine elaboration, whereas a one-line
      answer made almost entirely of the tutor's own words is an echo.

    Exposure is not knowledge. Crediting it is worse than not asking at all,
    because it moves the fact out of the queue while the user still cannot
    produce it unaided.
    """
    v = (verbatim or "").strip()
    if not v:
        return False, ""
    if _PARROT_PHRASES.search(v):
        return True, "user said outright that the tutor had just supplied this"
    prior = (prior_tutor_response or "").strip()
    if not prior:
        return False, ""
    vw = content_words(v)
    if not vw or len(vw) > max_content_words:
        return False, ""
    ov = _overlap(vw, content_words(prior))
    if ov >= overlap_threshold:
        return True, (f"{ov:.0%} of the answer's content words came straight "
                      f"from the tutor's immediately preceding reply")
    return False, ""


# A real teaching reply speaks TO the user and carries clinical substance. A
# meta-summary describes the exchange from outside it, in the past tense, the
# way a grading log would: "Rationale corrected to receptor mechanism",
# "Workup elements reasonable, sequencing corrected".
_META_LEAD = re.compile(
    r"^\s*(confirmed|corrected|taught|explained|clarified|reviewed|noted|"
    r"reinforced|discussed|covered|addressed)\b", re.I)
_META_PATTERN = re.compile(
    r"\b(rationale|definition|sequencing|dose range|elements|criteria|answer)\s+"
    r"\w*\s*(corrected|confirmed|clarified|reinforced)\b", re.I)
_META_TAIL = re.compile(
    r"\b(corrected to|confirmed correct|marked correct|graded|"
    r"as (the )?next step confirmed)\b", re.I)


def looks_like_meta_summary(tutor_response: str) -> tuple[bool, str]:
    """Flag a tutor_response that describes the teaching instead of being it.

    Two turns in the audited session stored exactly this, losing the clinical
    content permanently. Advisory: returned as a warning so the tutor can
    resend, never used to reject the write — a summary is still better than
    silence, and the attempt itself must not fail.
    """
    t = (tutor_response or "").strip()
    if not t:
        return False, ""
    addresses_user = re.search(r"\b(you|your|you're|let's|we)\b", t, re.I)
    signals = sum(bool(p.search(t)) for p in (_META_LEAD, _META_PATTERN, _META_TAIL))
    if signals and not addresses_user:
        return True, ("reads as a summary of the exchange rather than the reply "
                      "itself — store the actual words said to the user")
    if signals >= 2:
        return True, ("contains grading commentary in place of teaching content")
    return False, ""


# A citation has to name something OUTSIDE the system. These phrases name the
# system's own fact table, which is not a source — the facts in it are exactly
# what needs corroborating.
_SELF_REFERENTIAL = re.compile(
    r"knowledge[ _-]?point[s]?[ _-]?bank|knowledge[ _-]?base|fact[ _-]?bank|"
    r"fact[ _-]?table|prior session|previous session|earlier session|"
    r"session context|from memory|internal|my training|the database", re.I)
# A real citation names a document, and usually a location in it.
_CITATION_MARKERS = re.compile(
    r"\bp\.?\s?\d|\bpage\s?\d|\bch(?:apter)?\.?\s?\d|manual|guideline|"
    r"marino|miller|morgan|mikhail|stanford|statpearls|mgh|kdigo|surviving|"
    r"acc[/ ]aha|gold|idsa|uptodate|nejm|jama|lancet|handbook|textbook|"
    r"survival guide|housestaff", re.I)


def citation_quality(grounded_in: str) -> tuple[str, str]:
    """Classify a `grounded_in` value: 'real' | 'self_referential' | 'vague' | 'empty'.

    Grounding had quietly become a rubber stamp. In one audited session 11 of 17
    answers cited "<Topic> knowledge point bank" — a restatement of "I used the
    fact table", not a source — and every automated check counted the session as
    fully grounded because the field was non-empty.

    Worse, the answers that DID carry a real-looking citation were the dangerous
    ones. A question about vasopressor escalation cited "Surviving Sepsis
    Campaign 2021, p.7, p.30" for dose thresholds the guideline does not
    contain. The maintainer checked the source himself and found nothing. A
    citation nobody verifies does not add rigour, it launders invention — so an
    unverifiable stamp is worse than an empty field, which at least reports its
    own absence honestly.
    """
    g = (grounded_in or "").strip()
    if not g:
        return "empty", "no source declared"
    if _SELF_REFERENTIAL.search(g):
        return "self_referential", (
            "names the system's own fact table rather than a source — the facts "
            "there are what needs corroborating. Cite the book/guideline and "
            "location the passage came from, or leave it empty")
    if _CITATION_MARKERS.search(g):
        return "real", ""
    return "vague", ("does not name a document or location — cite the source and "
                     "page you built the question from")


# Units whose presence or absence changes a dose by orders of magnitude.
_PER_KG = re.compile(r"\b(?:per\s*kg|/\s*kg|mg\s*/\s*kg|mcg\s*/\s*kg|µg\s*/\s*kg|"
                     r"per\s*kilo(?:gram)?)\b", re.I)
_PER_DOSE = re.compile(r"\b(?:per\s*dose|each\s*dose|a\s*dose|flat\s*dose)\b", re.I)


def summary_contradicts_verbatim(user_answer: str, verbatim: str) -> tuple[bool, str]:
    """Catch a graded summary that has quietly corrected what the user said.

    The worst recording failure yet observed. The user said "point one to point
    three mgs PER KG" of naloxone. The graded summary recorded "0.1 to 0.3 mg
    PER DOSE" — silently swapping the unit — and the answer was then graded
    against the rewritten version and called "a touch conservative". For a 70 kg
    adult 0.1-0.3 mg/kg is 7-21 mg against a correct flat dose of 0.4 mg: 18 to
    52 times too high, and the kind of error that precipitates violent
    withdrawal. The day before, the same answer had been recorded correctly as
    "per kg ... incorrect, should be a flat 0.4 mg".

    A summary that edits the error out does not merely mis-grade one answer; it
    removes the mistake from the record, so no later audit can find it and the
    user is told he was nearly right. Weight-based versus flat dosing is the
    highest-yield instance, so it is checked explicitly.
    """
    v, s = (verbatim or ""), (user_answer or "")
    if not v.strip() or not s.strip():
        return False, ""
    if _PER_KG.search(v) and not _PER_KG.search(s):
        detail = ("the user said a WEIGHT-BASED dose (per kg) and the summary "
                  "dropped it")
        if _PER_DOSE.search(s):
            detail = ("the user said PER KG and the summary recorded PER DOSE — "
                      "an order-of-magnitude difference")
        return True, (f"user_answer contradicts user_answer_verbatim: {detail}. "
                      f"Record what was said and grade THAT; a per-kg answer to a "
                      f"flat-dose question is wrong, not approximately right.")
    return False, ""


def fact_was_covered(point: str, *turn_texts: str, threshold: float = 0.35) -> bool:
    """Did this turn actually cover the fact being carded?

    A fact whose content appears nowhere in the question, the user's answer, or
    the tutor's reply was not taught in this exchange — it was batch-written
    about the topic. That is how a BiPAP mechanism card came to exist a minute
    before the BiPAP question was asked. Such facts are real content but
    untested, so they belong in the new-material pool, never in the review
    queue as though they had been failed.

    The threshold is deliberately loose: carded facts are compressed
    restatements, so demanding tight overlap with conversational prose would
    reject genuine ones. This only needs to separate "discussed here" from
    "about a different part of the topic entirely".
    """
    pw = content_words(point)
    if not pw:
        return False
    return _overlap(pw, content_words(" ".join(t or "" for t in turn_texts))) >= threshold
