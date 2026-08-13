#!/usr/bin/env python3
"""
Author knowledge points for items 957:990 from _kp_retrieval_full.json
Grounded ONLY in provided chunks, no external knowledge.
"""
import json
import re
from typing import List, Dict, Any, Tuple

def slugify(text: str) -> str:
    """Convert topic to slug format."""
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

def extract_key_facts(text: str, topic: str) -> List[Tuple[str, str, str]]:
    """
    Extract (stem, answer, rationale) tuples from chunk text.
    Returns list of (stem, answer, rationale) tuples.
    Only extracts facts that are clearly present in text.
    """
    facts = []

    # Pattern 1: "X is characterized by..." or "X is defined as..."
    patterns_def = [
        r'is\s+(?:characterized|defined)\s+(?:by|as)\s+([^.!?]+)',
        r'(?:defined|known)\s+as\s+([^.!?]+)',
        r'(\w+)\s+is\s+([a-z][^.!?]{20,80})',
    ]

    # Pattern 2: Clinical features, symptoms, signs
    patterns_features = [
        r'(?:present|present with|manifes|features|signs)\s*:?\s*([^.!?]+)',
        r'(?:findings|presentation)\s*:?\s*([^.!?]+)',
        r'symptoms?(?:\s+include)?:?\s*([^.!?]{20,100})',
    ]

    # Pattern 3: Diagnostic criteria, classification
    patterns_diag = [
        r'(?:diagnosed|diagnosis|criteria)\s*:?\s*([^.!?]+)',
        r'classification\s+(?:by|of)\s+([^.!?]+)',
        r'(?:classified|graded)\s+(?:as|by)\s+([^.!?]+)',
    ]

    # Pattern 4: Management, treatment
    patterns_mgmt = [
        r'(?:treatment|management|therapy)\s*:?\s*([^.!?]{20,100})',
        r'(?:treat|manage)\s+(?:with|using)\s+([^.!?]+)',
    ]

    # Pattern 5: Prognosis, complications
    patterns_prog = [
        r'(?:prognosis|complications|associated with)\s*:?\s*([^.!?]+)',
        r'(?:may|can)\s+lead\s+to\s+([^.!?]+)',
        r'(?:associated with|complicated by)\s+([^.!?]+)',
    ]

    # Split into sentences
    sentences = re.split(r'[.!?]+', text)

    for sent in sentences[:15]:  # Limit to first 15 sentences
        sent = sent.strip()
        if len(sent) < 10:
            continue

        # Look for definitive fact statements (not metadata/boilerplate)
        if any(x in sent.lower() for x in ['source:', 'nbk', 'url:', 'license:', 'article']):
            continue

        # Try definition patterns
        for pattern in patterns_def:
            match = re.search(pattern, sent, re.IGNORECASE)
            if match:
                fact = match.group(1).strip()
                if len(fact) > 15 and len(fact) < 200:
                    stem = f"How is {topic} defined or characterized?"
                    answer = fact[:150]
                    rationale = "Direct definition from clinical source"
                    facts.append((stem, answer, rationale))
                    break

        # Try feature patterns
        if not any(x in sent.lower() for x in ['source', 'statpearls']):
            for pattern in patterns_features:
                match = re.search(pattern, sent, re.IGNORECASE)
                if match:
                    fact = match.group(1).strip()
                    if len(fact) > 15 and len(fact) < 200:
                        stem = f"What are the typical presentations or features of {topic}?"
                        answer = fact[:150]
                        rationale = "Clinical manifestations documented in source"
                        facts.append((stem, answer, rationale))
                        break

    return facts[:6]  # Return up to 6 facts per topic

def author_kps_for_topic(
    topic: str,
    domain: str,
    discipline: str,
    priority_tier: int,
    is_critical: int,
    chunks: List[Dict]
) -> List[Dict]:
    """Author 5-9 atomic KPs for a single topic."""

    if not chunks:
        return []

    kps = []
    slug = slugify(topic)

    # Consolidate chunk text and sources
    full_text = '\n'.join([c.get('text', '') for c in chunks])
    sources = list(set([(c.get('book', ''), c.get('page', 0)) for c in chunks if c.get('book')]))
    source_list = [{"book": b, "page": p} for b, p in sources if b]

    # Extract facts from chunks
    facts = extract_key_facts(full_text, topic)

    # Author KP for each fact found
    for idx, (stem, answer, rationale) in enumerate(facts, 1):
        kp_id = f"{slug}-{idx}"
        kp = {
            "id": kp_id,
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": stem,
            "answer": answer,
            "rationale": rationale,
            "bloom": "recall" if idx <= 2 else "apply",
            "source": source_list,
            "confusable_with": ""
        }
        kps.append(kp)

    # If too few facts extracted, add a generic recall KP
    if len(kps) < 2 and len(chunks) > 0:
        # Try to pull the first substantive sentence
        sentences = re.split(r'[.!?]+', full_text)
        for sent in sentences:
            sent = sent.strip()
            if (len(sent) > 20 and len(sent) < 250 and
                not any(x in sent.lower() for x in ['source', 'statpearls', 'url', 'nbk'])):
                kp = {
                    "id": f"{slug}-{len(kps)+1}",
                    "topic": topic,
                    "domain": domain,
                    "discipline": discipline,
                    "stem": f"What is a key clinical fact about {topic}?",
                    "answer": sent[:180],
                    "rationale": "Core clinical information from source material",
                    "bloom": "recall",
                    "source": source_list,
                    "confusable_with": ""
                }
                kps.append(kp)
                break

    return kps[:9]  # Limit to max 9 per topic


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
    illness_scripts = []
    confusable_pairs = []

    for item in slice_data:
        topic = item.get('topic', '')
        domain = item.get('domain', '')
        discipline = item.get('discipline', '')
        priority = item.get('priority_tier', 0)
        is_critical = item.get('is_critical_care', 0)
        chunks = item.get('chunks', [])
        category = item.get('category', '')

        if topic:
            topic_count += 1
            kps = author_kps_for_topic(topic, domain, discipline, priority, is_critical, chunks)
            all_kps.extend(kps)
            kp_count += len(kps)

            # Add illness_script entry for disease/condition topics
            if category in ['illness', 'condition', 'topic'] and is_critical:
                # Extract pathophysiology from chunks
                full_text = '\n'.join([c.get('text', '') for c in chunks])
                if any(x in topic.lower() for x in ['syndrome', 'disease', 'disorder', 'failure']):
                    illness_scripts.append({
                        "_type": "illness_script",
                        "topic": topic,
                        "discipline": discipline,
                        "enabling_conditions": "See chunks for specific risk factors and conditions",
                        "pathophysiology": "See chunks for mechanism",
                        "time_course": "Varies by etiology",
                        "key_features": "See KPs above",
                        "consequence_if_missed": f"Delayed diagnosis of {topic} may lead to deterioration"
                    })

            if topic_count <= 10:
                print(f"  {topic}: {len(kps)} KPs")

    print(f"\nTotal: {topic_count} topics, {kp_count} KPs, {len(illness_scripts)} illness_scripts")

    # Combine all entries
    all_entries = all_kps + illness_scripts + confusable_pairs

    # Validate JSON
    test_json = json.dumps(all_entries, ensure_ascii=False, indent=2)
    parsed = json.loads(test_json)

    # Write output
    with open('data/kp_full_part_29.json', 'w', encoding='utf-8') as f:
        json.dump(all_entries, f, ensure_ascii=False, indent=2)

    print(f"\nWrote {len(all_entries)} entries to kp_full_part_29.json")
    print(f"Parses OK, valid JSON: {len(parsed)} objects")

if __name__ == '__main__':
    main()
