"""Merge parts 3a, 3b, 3c into kp_redeep_part_3.json and validate."""
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

parts = []
for fname in ['data/_kps_part3a.json', 'data/_kps_part3b.json', 'data/_kps_part3c.json']:
    with open(fname, 'r', encoding='utf-8') as f:
        parts.extend(json.load(f))

# Count by type
kp_count = sum(1 for x in parts if '_type' not in x)
script_count = sum(1 for x in parts if x.get('_type') == 'illness_script')
pair_count = sum(1 for x in parts if x.get('_type') == 'confusable_pair')

# Validate unique IDs among KPs
ids = [x['id'] for x in parts if '_type' not in x]
assert len(ids) == len(set(ids)), f"Duplicate IDs found: {set(i for i in ids if ids.count(i)>1)}"

# Validate required fields in KPs
required = ['id','topic','domain','discipline','stem','answer','rationale','bloom','source','confusable_with']
for item in parts:
    if '_type' not in item:
        for field in required:
            assert field in item, f"Missing field {field} in {item.get('id','?')}"
        assert item['bloom'] in ('recall','apply','analyze'), f"Bad bloom: {item['id']}"
        assert isinstance(item['source'], list) and len(item['source']) > 0, f"Empty source: {item['id']}"

# Validate illness scripts
for item in parts:
    if item.get('_type') == 'illness_script':
        for f in ['topic','discipline','enabling_conditions','pathophysiology','time_course','key_features','consequence_if_missed']:
            assert f in item, f"Missing {f} in illness_script for {item.get('topic','?')}"

# Validate confusable pairs
for item in parts:
    if item.get('_type') == 'confusable_pair':
        for f in ['topic_a','topic_b','discriminator']:
            assert f in item, f"Missing {f} in confusable_pair"

# Count topics (unique)
topics = list(dict.fromkeys([x['topic'] for x in parts if '_type' not in x]))
topic_count = len(topics)

print(f"Total objects: {len(parts)}")
print(f"Topics: {topic_count}")
print(f"KPs: {kp_count}")
print(f"Illness scripts: {script_count}")
print(f"Confusable pairs: {pair_count}")
print(f"Unique KP IDs: {len(set(ids))}")
print("All validations passed.")

# Write output
with open('data/kp_redeep_part_3.json', 'w', encoding='utf-8') as f:
    json.dump(parts, f, ensure_ascii=False, indent=2)
print(f"Written to data/kp_redeep_part_3.json ({len(parts)} objects)")

# Final summary line
print(f"\npart 3: {topic_count} topics, {kp_count} KPs, {script_count} scripts, {pair_count} pairs, parses OK")
