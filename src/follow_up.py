"""Server-side iterative follow-up question handler.

The Custom GPT calls a single `/follow_up` endpoint with the user's literal
question + the current lesson topic. The backend:

1. Builds 1-3 query variants (direct + topic-prefixed + synonym-expanded +
   broader-mode fallback).
2. Calls hybrid_search per variant; stops as soon as a variant returns
   high/medium confidence.
3. Extracts the sentences from the top chunks that actually contain answer-
   bearing tokens (numbers, drug names from the question, condition names).
4. Returns a focused payload: top chunks + extracted answer sentences +
   the queries it tried + the modes it tried + a confidence band.

The GPT then narrates the extracted sentences in the user's framing and
cites the source. One round-trip per follow-up, regardless of how many
internal search rounds were needed.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable

from .retrieval import hybrid_search, retrieval_confidence
from .schemas import SourceChunk
from .synonyms import expand_with_synonyms


_QUESTION_STOPWORDS = {
    "the", "a", "an", "is", "are", "was", "were", "be", "do", "does", "did",
    "what", "which", "who", "whom", "why", "how", "when", "where",
    "of", "to", "in", "on", "at", "by", "for", "with", "from", "as",
    "and", "or", "but", "not", "no", "yes", "than", "then",
    "this", "that", "these", "those", "it", "its", "if",
    "you", "your", "i", "me", "my", "we", "our", "us",
    "any", "all", "every", "some", "such",
    "based", "give", "given", "use", "used", "going", "still",
}


def _terms(text: str) -> list[str]:
    return [t for t in re.findall(r"[a-zA-Z][a-zA-Z0-9-]{1,}", text)]


def _content_terms(question: str) -> list[str]:
    out = []
    for t in _terms(question):
        low = t.lower()
        if low in _QUESTION_STOPWORDS or len(low) < 3:
            continue
        out.append(low)
    return out


def _topic_label(lesson_topic: str | None) -> str:
    if not lesson_topic:
        return ""
    return re.sub(r"\s+", " ", lesson_topic).strip()


@dataclass
class AnswerSentence:
    text: str
    book: str
    page: int | None
    matched_terms: list[str]


# Terms that, when present in the query, indicate the user is asking *about* that
# specific drug/agent.  When a sentence also contains that exact term, it is more
# likely to be the direct answer than a sentence that only matches generic context
# words (e.g. "septic shock").  List is intentionally broad so the boost
# generalises to any explicitly-named pharmacological agent.
_NAMED_AGENT_TERMS: frozenset[str] = frozenset({
    "norepinephrine", "vasopressin", "phenylephrine", "dopamine",
    "epinephrine", "dobutamine", "milrinone", "rocuronium",
    "succinylcholine", "dantrolene", "metoprolol", "labetalol",
    "nitroglycerin", "nitroprusside", "furosemide", "albumin",
    "ketamine", "propofol", "midazolam", "fentanyl", "morphine",
    "hydromorphone", "naloxone", "neostigmine", "sugammadex",
    "vancomycin", "piperacillin", "meropenem", "ceftriaxone",
    "heparin", "warfarin", "enoxaparin", "alteplase",
    "dexamethasone", "methylprednisolone", "hydrocortisone",
    "insulin", "glucagon", "atropine", "adenosine", "amiodarone",
})


def _extract_answer_sentences(
    chunks: list[SourceChunk],
    question_terms: list[str],
    max_sentences: int = 4,
) -> list[AnswerSentence]:
    if not chunks or not question_terms:
        return []
    # Identify which question terms are explicitly-named pharmacological agents.
    # Sentences that contain one of these terms receive a priority bonus so they
    # rank above generic context sentences with more total term matches.
    named_drug_hits = _NAMED_AGENT_TERMS.intersection(question_terms)
    out: list[AnswerSentence] = []
    seen_keys: set[tuple[str, str]] = set()
    for chunk in chunks:
        text = chunk.text or ""
        if not text:
            continue
        # Split on sentence boundaries
        sentences = re.split(r"(?<=[.!?])\s+|(?<=\.)\s+(?=[A-Z])", text)
        for sent in sentences:
            sent_clean = re.sub(r"\s+", " ", sent).strip()
            if len(sent_clean) < 20 or len(sent_clean) > 400:
                continue
            sent_low = sent_clean.lower()
            matched = [t for t in question_terms if t in sent_low]
            if not matched:
                continue
            key = (chunk.book, sent_clean[:60])
            if key in seen_keys:
                continue
            seen_keys.add(key)
            out.append(
                AnswerSentence(
                    text=sent_clean,
                    book=chunk.book,
                    page=chunk.page,
                    matched_terms=matched,
                )
            )
    # Sort: primary key = number of matched terms + bonus for containing a
    # query-named drug (generalises to any agent in _NAMED_AGENT_TERMS);
    # secondary key = shorter sentences preferred (more focused).
    def _sort_key(a: AnswerSentence) -> tuple:
        drug_bonus = 2 if named_drug_hits and any(d in a.text.lower() for d in named_drug_hits) else 0
        return (-(len(a.matched_terms) + drug_bonus), len(a.text))

    out.sort(key=_sort_key)
    return out[:max_sentences]


def _build_query_variants(question: str, lesson_topic: str, mode_hint: str | None) -> list[tuple[str, str]]:
    """Produce ordered (query, mode) variants for up to 3 search rounds."""
    topic = _topic_label(lesson_topic)
    base_terms = " ".join(_content_terms(question))
    base = (topic + " " + base_terms).strip() if topic else base_terms or question
    variants: list[tuple[str, str]] = []
    primary_mode = mode_hint or "broad_explain"

    # Round 1: topic + question content terms, primary mode
    variants.append((expand_with_synonyms(base), primary_mode))

    # Round 2: question only, broader mode
    secondary_mode = "broad_explain" if primary_mode != "broad_explain" else "intern_teach"
    variants.append((expand_with_synonyms(base_terms or question), secondary_mode))

    # Round 3: heavy synonym expansion + a tertiary mode (anesthesia / ICU)
    if primary_mode in ("intern_teach", "cross_cover"):
        tertiary = "ICU_teach"
    elif primary_mode == "ICU_teach":
        tertiary = "anesthesia_boards"
    elif primary_mode in ("anesthesia_boards", "drug", "crisis"):
        tertiary = "intern_teach"
    else:
        tertiary = "anesthesia_boards"
    expanded = expand_with_synonyms(base) + " " + " ".join(_content_terms(topic))
    variants.append((expanded.strip(), tertiary))

    # Dedupe identical variants
    seen = set()
    deduped = []
    for q, m in variants:
        key = (q, m)
        if key in seen:
            continue
        seen.add(key)
        deduped.append((q, m))
    return deduped


def answer_follow_up(
    question: str,
    lesson_topic: str | None = None,
    mode_hint: str | None = None,
    max_rounds: int = 3,
    max_results_per_round: int = 5,
) -> dict:
    if not question or not question.strip():
        return {
            "question": question,
            "lesson_topic": lesson_topic or "",
            "queries_tried": [],
            "modes_tried": [],
            "answer_sentences": [],
            "top_chunks": [],
            "confidence": "low",
            "insufficient_context": True,
        }

    q_terms = _content_terms(question)
    if lesson_topic:
        q_terms.extend(_content_terms(lesson_topic))
    q_terms = list(dict.fromkeys(q_terms))  # de-dupe preserving order

    variants = _build_query_variants(question, lesson_topic or "", mode_hint)[:max_rounds]
    queries_tried: list[str] = []
    modes_tried: list[str] = []
    best_chunks: list[SourceChunk] = []
    best_confidence = "low"
    best_round_score = -1

    for query, mode in variants:
        queries_tried.append(query)
        modes_tried.append(mode)
        results, insufficient = hybrid_search(
            query,
            mode=mode,
            max_results=max_results_per_round,
            use_cross_encoder=False,
        )
        if not results:
            continue
        confidence = retrieval_confidence(results)
        # Score the round: prefer chunks whose text contains question terms
        text_blob = " ".join(r.text.lower() for r in results[:3])
        term_hits = sum(1 for t in q_terms if t in text_blob)
        round_score = term_hits * 10 + {"high": 3, "medium": 2, "low": 0}.get(confidence, 0)
        if round_score > best_round_score:
            best_round_score = round_score
            best_chunks = results
            best_confidence = confidence
        # Early stop: if we've hit medium+ confidence AND have at least 2 question-term hits, done
        if confidence in ("high", "medium") and term_hits >= max(2, min(3, len(q_terms))):
            break

    answers = _extract_answer_sentences(best_chunks[:5], q_terms, max_sentences=4)
    return {
        "question": question,
        "lesson_topic": lesson_topic or "",
        "queries_tried": queries_tried,
        "modes_tried": modes_tried,
        "answer_sentences": [
            {
                "text": a.text,
                "book": a.book,
                "page": a.page,
                "matched_terms": a.matched_terms,
            }
            for a in answers
        ],
        "top_chunks": [c for c in best_chunks[:5]],
        "confidence": best_confidence,
        "insufficient_context": (best_confidence == "low" and not answers),
    }
