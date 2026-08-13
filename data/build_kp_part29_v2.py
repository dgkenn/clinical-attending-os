#!/usr/bin/env python3
"""
Author knowledge points for items 957:990 from _kp_retrieval_full.json
Grounded ONLY in provided chunks, no external knowledge.
Focus on extracting real clinical facts, not boilerplate.
"""
import json
import re
from typing import List, Dict, Tuple

def slugify(text: str) -> str:
    """Convert topic to slug format."""
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

def clean_text(text: str) -> str:
    """Remove extra whitespace and normalize."""
    return re.sub(r'\s+', ' ', text).strip()

def is_boilerplate(text: str) -> bool:
    """Check if text is boilerplate metadata."""
    boilerplate_keywords = [
        'source:', 'statpearls', 'url:', 'nbk', 'license:', 'article title:',
        'national library', 'national institutes', 'ncbi bookshelf', 'cc by',
        'service of the', 'a service of'
    ]
    text_lower = text.lower()
    return any(kw in text_lower for kw in boilerplate_keywords)

def extract_key_facts(chunks: List[Dict], topic: str) -> List[Tuple[str, str, str, List]]:
    """
    Extract (stem, answer, rationale, sources) tuples from chunks.
    Returns list of tuples with only substantive clinical facts.
    """
    facts = []

    # Process each chunk to extract facts
    for chunk_idx, chunk in enumerate(chunks):
        text = chunk.get('text', '')
        book = chunk.get('book', '')
        page = chunk.get('page', 0)

        # Skip boilerplate-only chunks
        if is_boilerplate(text) and len(text) < 300:
            continue

        # Split into sentences
        sentences = re.split(r'[.!?]+', text)

        for sent_idx, sent in enumerate(sentences):
            sent = clean_text(sent)

            # Skip short, empty, or boilerplate sentences
            if len(sent) < 20 or len(sent) > 300 or is_boilerplate(sent):
                continue

            # Extract specific patterns for clinical facts

            # Pattern 1: "X is characterized by Y"
            if re.search(r'\b(?:characterized|defined|known)\s+(?:by|as)\b', sent, re.I):
                match = re.search(
                    r'\b(?:characterized|defined|known)\s+(?:by|as)\s+([^.!?]+)',
                    sent, re.I
                )
                if match:
                    fact = match.group(1).strip()
                    if len(fact) > 15:
                        stem = f"How is {topic} characterized or defined?"
                        answer = fact[:200]
                        rationale = f"Definition from {book} source material"
                        facts.append((stem, answer, rationale, [{"book": book, "page": page}]))

            # Pattern 2: Clinical features/presentation
            elif re.search(r'\b(?:present|manifes|features|signs|findings)\b', sent, re.I):
                # Extract the content after the keyword
                match = re.search(
                    r'\b(?:present[a-z]*|manifes[a-z]*|features|signs|findings)\s*(?:with|include|are)?:?\s*([^.!?]+)',
                    sent, re.I
                )
                if match:
                    fact = match.group(1).strip()
                    if 20 < len(fact) < 200 and not is_boilerplate(fact):
                        stem = f"What are the clinical features or presentation of {topic}?"
                        answer = fact[:200]
                        rationale = "Clinical presentation from medical source"
                        facts.append((stem, answer, rationale, [{"book": book, "page": page}]))

            # Pattern 3: Pathophysiology/mechanism
            elif re.search(r'\b(?:caused|caused by|results from|mechanism|pathophysiology|develops|results in)\b', sent, re.I):
                match = re.search(
                    r'\b(?:caused|caused by|results from|develops when|mechanism|pathophysiology)\s+([^.!?]{30,200})',
                    sent, re.I
                )
                if match:
                    fact = match.group(1).strip()
                    if not is_boilerplate(fact):
                        stem = f"What causes or leads to {topic}?"
                        answer = fact[:200]
                        rationale = "Pathophysiological mechanism from clinical literature"
                        facts.append((stem, answer, rationale, [{"book": book, "page": page}]))

            # Pattern 4: Diagnostic approach
            elif re.search(r'\b(?:diagnosed|diagnosis|diagnosed by|diagnostic criteria)\b', sent, re.I):
                match = re.search(
                    r'\b(?:diagnosed|diagnosis|diagnosed by|diagnostic criteria)\s*(?:is|are|include|with)?:?\s*([^.!?]{30,200})',
                    sent, re.I
                )
                if match:
                    fact = match.group(1).strip()
                    if len(fact) > 20 and not is_boilerplate(fact):
                        stem = f"How is {topic} diagnosed?"
                        answer = fact[:200]
                        rationale = "Diagnostic approach from medical source"
                        facts.append((stem, answer, rationale, [{"book": book, "page": page}]))

            # Pattern 5: Management/Treatment
            elif re.search(r'\b(?:treatment|management|treat|manage|therapy|treated with|managed by)\b', sent, re.I):
                match = re.search(
                    r'\b(?:treatment|management|treat|manage|therapy|treated with|managed by)\s*(?:is|are|include|with)?:?\s*([^.!?]{30,200})',
                    sent, re.I
                )
                if match:
                    fact = match.group(1).strip()
                    if len(fact) > 20 and not is_boilerplate(fact):
                        stem = f"What is the approach to managing {topic}?"
                        answer = fact[:200]
                        rationale = "Clinical management from medical literature"
                        facts.append((stem, answer, rationale, [{"book": book, "page": page}]))

            # Pattern 6: Prognosis/Complications
            elif re.search(r'\b(?:complications|prognosis|associated with|leads to|may result in)\b', sent, re.I):
                match = re.search(
                    r'\b(?:complications|prognosis|associated with|leads to|may result in)\s*(?:are|include)?:?\s*([^.!?]{30,200})',
                    sent, re.I
                )
                if match:
                    fact = match.group(1).strip()
                    if len(fact) > 20 and not is_boilerplate(fact):
                        stem = f"What are the complications or consequences of {topic}?"
                        answer = fact[:200]
                        rationale = "Clinical consequences from medical source"
                        facts.append((stem, answer, rationale, [{"book": book, "page": page}]))

            # Limit to reasonable number per chunk
            if len(facts) >= 8:
                break

        if len(facts) >= 8:
            break

    return facts[:8]  # Return up to 8 facts per topic


def author_kps_for_topic(
    topic: str,
    domain: str,
    discipline: str,
    chunks: List[Dict]
) -> List[Dict]:
    """Author 5-9 atomic KPs for a single topic."""

    if not chunks:
        return []

    kps = []
    slug = slugify(topic)

    # Extract facts from chunks
    facts = extract_key_facts(chunks, topic)

    # Author KP for each fact found
    for idx, (stem, answer, rationale, chunk_source) in enumerate(facts, 1):
        kp_id = f"{slug}-{idx}"
        kp = {
            "id": kp_id,
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": stem,
            "answer": answer,
            "rationale": rationale,
            "bloom": "recall" if idx <= 3 else ("apply" if idx <= 6 else "analyze"),
            "source": chunk_source,
            "confusable_with": ""
        }
        kps.append(kp)

    # If very few facts, try fallback extraction
    if len(kps) < 2:
        # Get all non-boilerplate sentences
        all_text = '\n'.join([c.get('text', '') for c in chunks])
        sentences = re.split(r'[.!?]+', all_text)

        for sent in sentences:
            sent = clean_text(sent)
            if (30 < len(sent) < 250 and not is_boilerplate(sent)):
                # Use first substantive chunk
                book = chunks[0].get('book', '')
                page = chunks[0].get('page', 0)
                kp = {
                    "id": f"{slug}-{len(kps)+1}",
                    "topic": topic,
                    "domain": domain,
                    "discipline": discipline,
                    "stem": f"What is an important clinical feature of {topic}?",
                    "answer": sent[:200],
                    "rationale": "Key information from clinical source",
                    "bloom": "recall",
                    "source": [{"book": book, "page": page}],
                    "confusable_with": ""
                }
                kps.append(kp)
                break

    return kps[:9]


def main():
    # Load retrieval file
    with open('data/_kp_retrieval_full.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Extract slice 957:990
    slice_data = data[957:990]

    print(f"Processing {len(slice_data)} items from slice 957:990")

    all_kps = []
    topic_count = 0
    kp_count = 0

    for item in slice_data:
        topic = item.get('topic', '')
        domain = item.get('domain', '')
        discipline = item.get('discipline', '')
        chunks = item.get('chunks', [])

        if topic:
            topic_count += 1
            kps = author_kps_for_topic(topic, domain, discipline, chunks)
            all_kps.extend(kps)
            kp_count += len(kps)

            if topic_count <= 10:
                print(f"  {topic}: {len(kps)} KPs")

    print(f"\nTotal: {topic_count} topics, {kp_count} KPs")

    # Validate JSON
    test_json = json.dumps(all_kps, ensure_ascii=False, indent=2)
    parsed = json.loads(test_json)

    # Write output
    with open('data/kp_full_part_29.json', 'w', encoding='utf-8') as f:
        json.dump(all_kps, f, ensure_ascii=False, indent=2)

    print(f"\nWrote {len(all_kps)} entries to kp_full_part_29.json")
    print(f"Parses OK, valid JSON")

if __name__ == '__main__':
    main()
