
import json

with open('data/kp_part10_b1.json', 'r', encoding='utf-8') as f:
    b1 = json.load(f)

with open('data/kp_part10_b2.json', 'r', encoding='utf-8') as f:
    b2 = json.load(f)

combined = b1 + b2

# Validate: check for duplicate ids
ids = [x.get('id', x.get('topic','')) for x in combined]
kps = [x for x in combined if '_type' not in x]
scripts = [x for x in combined if x.get('_type') == 'illness_script']
pairs = [x for x in combined if x.get('_type') == 'confusable_pair']

kp_ids = [x['id'] for x in kps]
dupes = [x for x in kp_ids if kp_ids.count(x) > 1]
if dupes:
    print(f"DUPLICATE IDs: {set(dupes)}")
else:
    print("No duplicate IDs")

# Count topics covered
topics = sorted(set(x['topic'] for x in combined))
print(f"Topics covered: {len(topics)}")
print(f"Total items: {len(combined)}")
print(f"KPs: {len(kps)}, Scripts: {len(scripts)}, Pairs: {len(pairs)}")

with open('data/kp_redeep_part_10.json', 'w', encoding='utf-8') as f:
    json.dump(combined, f, ensure_ascii=False, indent=2)

# Verify it parses
with open('data/kp_redeep_part_10.json', 'r', encoding='utf-8') as f:
    check = json.load(f)
print(f"Parse OK: {len(check)} items")
