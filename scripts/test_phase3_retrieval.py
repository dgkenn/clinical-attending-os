#!/usr/bin/env python3
"""
Test Phase 3 retrieval quality with spot-check queries.

Verifies that Phase 3 units are retrievable via keyword search.
"""

import json
import re

def test_phase3_retrieval():
    """Test retrieval of Phase 3 units by keyword search."""

    # Load Phase 3 chunks
    with open("data/phase3_chunks_chroma.jsonl", 'r', encoding='utf-8') as f:
        units = [json.loads(line) for line in f]

    # Test queries covering all Phase 3 modules
    test_queries = [
        ("sepsis qSOFA score early recognition", ["sepsis", "qsofa", "recognition"]),
        ("ARDS lung-protective ventilation PEEP", ["ards", "ventilation", "peep"]),
        ("acute heart failure decompensation treatment", ["heart", "failure", "decompensation"]),
        ("hypertensive emergency end-organ damage", ["hypertensive", "emergency", "organ"]),
        ("DIC disseminated intravascular coagulation", ["dic", "coagulation", "thrombosis"]),
        ("acute liver failure encephalopathy management", ["liver", "failure", "encephalopathy"]),
        ("acute pancreatitis necrosis complications", ["pancreatitis", "necrosis"]),
        ("intracranial hypertension cerebral edema osmotic therapy", ["icp", "edema", "osmotic"]),
        ("status epilepticus first-line treatment", ["status", "epilepticus", "seizure"]),
        ("MOF multiple organ failure SOFA", ["organ", "failure", "sofa"]),
    ]

    print("=" * 80)
    print("PHASE 3 RETRIEVAL QUALITY TEST")
    print("=" * 80)

    results_summary = []

    for query, keywords in test_queries:
        # Simple keyword-based retrieval
        matching_units = []
        for unit in units:
            text = (unit.get('text', '') + " " + unit.get('metadata', {}).get('topic', '') + " " +
                   " ".join(unit.get('metadata', {}).get('topic_tags', []))).lower()

            # Count how many keywords match
            keyword_matches = sum(1 for kw in keywords if kw.lower() in text)

            if keyword_matches >= 2:  # At least 2 keywords must match
                matching_units.append({
                    'id': unit.get('id'),
                    'topic': unit.get('metadata', {}).get('topic', ''),
                    'matches': keyword_matches
                })

        # Sort by match count
        matching_units.sort(key=lambda x: -x['matches'])

        print(f"\nQuery: {query}")
        print(f"  Keywords: {', '.join(keywords)}")
        print(f"  Matches found: {len(matching_units)}")

        if len(matching_units) >= 3:
            print(f"  [PASS] (found {len(matching_units)} results)")
            for i, unit in enumerate(matching_units[:3]):
                print(f"    {i+1}. [{unit['id']}] {unit['topic'][:60]}")
        else:
            print(f"  [FAIL] (found only {len(matching_units)} results, need >=3)")
            for i, unit in enumerate(matching_units):
                print(f"    {i+1}. [{unit['id']}] {unit['topic'][:60]}")

        results_summary.append({
            'query': query,
            'matches': len(matching_units),
            'passed': len(matching_units) >= 3
        })

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    passed = sum(1 for r in results_summary if r['passed'])
    total = len(results_summary)
    print(f"Queries passed: {passed}/{total}")
    print(f"Success rate: {100*passed/total:.0f}%")

    if passed == total:
        print("\n[PASS] All retrieval tests PASSED")
    else:
        print(f"\n[FAIL] {total - passed} retrieval tests FAILED")
        for result in results_summary:
            if not result['passed']:
                print(f"  - {result['query']} ({result['matches']} matches)")

    # Statistics
    print("\n" + "=" * 80)
    print("PHASE 3 STATISTICS")
    print("=" * 80)
    print(f"Total Phase 3 units: {len(units)}")

    subtopics = {}
    libraries = {}
    for unit in units:
        meta = unit.get('metadata', {})
        subtopic = meta.get('subtopic', 'UNKNOWN')
        library = meta.get('library', 'UNKNOWN')
        subtopics[subtopic] = subtopics.get(subtopic, 0) + 1
        libraries[library] = libraries.get(library, 0) + 1

    print(f"\nLibrary distribution:")
    for lib, count in sorted(libraries.items(), key=lambda x: -x[1]):
        print(f"  {lib}: {count}")

    print(f"\nSubtopic count: {len(subtopics)} unique subtopics")
    print(f"Top 10 subtopics:")
    for subtopic, count in sorted(subtopics.items(), key=lambda x: -x[1])[:10]:
        print(f"  {subtopic}: {count}")

if __name__ == "__main__":
    test_phase3_retrieval()
