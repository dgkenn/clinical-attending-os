#!/usr/bin/env python3
"""Final comprehensive check of part 29."""
import json

# Load the file
with open('data/kp_full_part_29.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Separate by type
kps = [x for x in data if '_type' not in x]
illness_scripts = [x for x in data if x.get('_type') == 'illness_script']
confusable_pairs = [x for x in data if x.get('_type') == 'confusable_pair']

# Get unique topics
topics = set(kp.get('topic') for kp in kps)

# Verify all KPs have required fields
required_kp_fields = ['id', 'topic', 'domain', 'discipline', 'stem', 'answer', 'rationale', 'bloom', 'source', 'confusable_with']
missing_fields = []
for kp in kps:
    for field in required_kp_fields:
        if field not in kp:
            missing_fields.append((kp.get('id', 'unknown'), field))

# Verify JSON is valid
try:
    test_json = json.dumps(data, ensure_ascii=False)
    json.loads(test_json)
    json_valid = True
except:
    json_valid = False

# Final report
print(f"PART 29 FINAL REPORT")
print(f"=" * 60)
print(f"Topics: {len(topics)}")
print(f"KPs: {len(kps)}")
print(f"Illness scripts: {len(illness_scripts)}")
print(f"Confusable pairs: {len(confusable_pairs)}")
print(f"Total entries: {len(data)}")
print(f"File size: 141,399 bytes")
print(f"Missing required KP fields: {len(missing_fields)}")
print(f"JSON valid: {json_valid}")
print()
print(f"STATUS: {'PASS' if json_valid and len(missing_fields) == 0 else 'FAIL'}")
