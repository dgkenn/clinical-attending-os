#!/usr/bin/env python3
"""Verify and report on kp_full_part_29.json"""
import json

# Load and verify
with open('data/kp_full_part_29.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Count types
kps = [x for x in data if 'id' in x and '_type' not in x]
illness_scripts = [x for x in data if x.get('_type') == 'illness_script']
confusable_pairs = [x for x in data if x.get('_type') == 'confusable_pair']

print(f"Total entries: {len(data)}")
print(f"  KPs: {len(kps)}")
print(f"  Illness scripts: {len(illness_scripts)}")
print(f"  Confusable pairs: {len(confusable_pairs)}")

# Sample a few KPs
print("\nSample KPs:")
for i, kp in enumerate(kps[:3]):
    print(f"\n{i+1}. Topic: {kp.get('topic')}")
    print(f"   ID: {kp.get('id')}")
    print(f"   Stem: {kp.get('stem')}")
    print(f"   Answer: {kp.get('answer')[:80]}...")
    print(f"   Bloom: {kp.get('bloom')}")

# Verify all have required fields
required = ['id', 'topic', 'domain', 'discipline', 'stem', 'answer', 'rationale', 'bloom', 'source', 'confusable_with']
missing = []
for kp in kps:
    for field in required:
        if field not in kp:
            missing.append((kp.get('id'), field))

if missing:
    print(f"\nMissing fields: {missing[:5]}")
else:
    print("\nAll KPs have required fields: OK")

# Check source validity
bad_sources = []
for kp in kps:
    src = kp.get('source', [])
    if not isinstance(src, list):
        bad_sources.append(kp.get('id'))
    elif len(src) == 0:
        bad_sources.append(kp.get('id'))

if bad_sources:
    print(f"KPs with invalid sources: {len(bad_sources)}")
else:
    print("All KPs have valid sources: OK")

# Final parse test
test_str = json.dumps(data, ensure_ascii=False)
json.loads(test_str)
print(f"\nFinal JSON parses OK: {len(test_str)} characters")

# Get unique topics
topics = set(kp.get('topic') for kp in kps)
print(f"Unique topics: {len(topics)}")

# Topics list
print("\nTopics covered:")
for topic in sorted(topics)[:10]:
    count = len([k for k in kps if k.get('topic') == topic])
    print(f"  {topic}: {count} KPs")
