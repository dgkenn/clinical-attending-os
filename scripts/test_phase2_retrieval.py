#!/usr/bin/env python3
"""
Test Phase 2 retrieval quality with spot-check queries.
Verify knowledge base is searchable and relevant.
"""

import json
from pathlib import Path
from collections import defaultdict

def test_phase2_queries():
    """Run spot-check queries on cumulative knowledge base."""
    data_dir = Path("C:/Users/Dean/anesthesia_attending/data")
    cumulative_file = data_dir / "cumulative_chunks.jsonl"

    # Load all units into memory for simple text search
    units = []
    with open(cumulative_file, 'r') as f:
        for line in f:
            if line.strip():
                units.append(json.loads(line))

    # Test queries covering all 8 Phase 2 modules
    test_queries = [
        ("pneumonia CURB-65 severity", "pneumonia_severity"),
        ("ACS troponin STEMI diagnosis", "acs_stemi"),
        ("PE Wells score D-dimer", "pe_diagnosis"),
        ("GI bleeding PPI dosing variceal", "ugib_varices"),
        ("COPD exacerbation bronchodilator", "copd_exacerbation"),
        ("diabetes DKA treatment ketoacidosis", "diabetes_dka"),
        ("hypothyroidism levothyroxine dosing", "thyroid_treatment"),
        ("AKI prerenal intrinsic postrenal", "aki_types"),
        ("hyperkalemia EKG peaked T waves", "hyperkalemia"),
        ("hyponatremia SIADH correction", "hyponatremia"),
    ]

    print("=" * 70)
    print("PHASE 2 RETRIEVAL QUALITY TEST")
    print("=" * 70)
    print(f"Total units in knowledge base: {len(units)}")
    print(f"\nRunning {len(test_queries)} spot-check queries...\n")

    all_passed = True
    results_summary = []

    for query_text, expected_subtopic in test_queries:
        # Simple keyword-based search (in production would use vector similarity)
        query_terms = query_text.lower().split()
        matching_units = []

        for unit in units:
            text = unit["text"].lower()
            metadata = unit["metadata"]
            # Count matching keywords in text and metadata
            match_count = sum(1 for term in query_terms if term in text)
            subtopic = metadata.get("subtopic", "")

            if match_count >= 1:  # At least one keyword match
                matching_units.append({
                    "id": unit["id"],
                    "topic": metadata["topic"],
                    "subtopic": subtopic,
                    "match_count": match_count
                })

        # Sort by match count
        matching_units.sort(key=lambda x: -x["match_count"])

        # Check if expected subtopic present in top results
        expected_found = any(u["subtopic"] == expected_subtopic for u in matching_units[:3])
        status = "PASS" if expected_found and len(matching_units) >= 1 else "FAIL"

        if status == "FAIL":
            all_passed = False

        result = {
            "query": query_text,
            "expected_subtopic": expected_subtopic,
            "results_count": len(matching_units),
            "status": status,
            "top_result": matching_units[0] if matching_units else None
        }
        results_summary.append(result)

        print(f"Query: '{query_text}'")
        print(f"  Expected subtopic: {expected_subtopic}")
        print(f"  Results found: {len(matching_units)}")
        print(f"  Status: {status}")
        if matching_units:
            top = matching_units[0]
            print(f"  Top result: {top['topic']} (subtopic: {top['subtopic']})")
        print()

    # Summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    passed = sum(1 for r in results_summary if r["status"] == "PASS")
    failed = sum(1 for r in results_summary if r["status"] == "FAIL")
    print(f"Passed: {passed}/{len(test_queries)}")
    print(f"Failed: {failed}/{len(test_queries)}")

    if all_passed:
        print("\nRESULT: All tests PASSED")
        print("Knowledge base retrieval quality is adequate for Phase 2.")
    else:
        print("\nRESULT: Some tests FAILED")
        print("Review query patterns and knowledge base coverage.")

    # Module statistics
    print("\nPhase 2 Module Statistics:")
    module_stats = defaultdict(int)
    for unit in units:
        if unit["id"].startswith("phase2"):
            subtopic = unit["metadata"].get("subtopic", "unknown")
            # Extract module from subtopic (e.g., "pneumonia_severity" -> "pneumonia")
            module = subtopic.split("_")[0]
            module_stats[module] += 1

    for module in sorted(module_stats.keys()):
        print(f"  {module}: {module_stats[module]} units")

    return all_passed

if __name__ == "__main__":
    success = test_phase2_queries()
    exit(0 if success else 1)
