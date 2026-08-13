import json, sys
sys.stdout.reconfigure(encoding='utf-8')

all_kps = []
for batch in ['data/kp_part26_batch1.json', 'data/kp_part26_batch2.json',
              'data/kp_part26_batch3.json', 'data/kp_part26_batch4.json']:
    with open(batch, 'r', encoding='utf-8') as f:
        all_kps.extend(json.load(f))

# Verify JSON parses correctly and count types
topics_seen = set()
kps_count = 0
scripts_count = 0
pairs_count = 0
ids_seen = set()
dupe_ids = []

for item in all_kps:
    if item.get('_type') == 'illness_script':
        scripts_count += 1
    elif item.get('_type') == 'confusable_pair':
        pairs_count += 1
    else:
        kps_count += 1
        topics_seen.add(item.get('topic', ''))
        kid = item.get('id', '')
        if kid in ids_seen:
            dupe_ids.append(kid)
        ids_seen.add(kid)

print(f'Total items: {len(all_kps)}')
print(f'KPs: {kps_count}')
print(f'Illness scripts: {scripts_count}')
print(f'Confusable pairs: {pairs_count}')
print(f'Unique topics: {len(topics_seen)}')
print(f'Duplicate IDs: {dupe_ids}')

# Write final output
with open('data/kp_full_part_26.json', 'w', encoding='utf-8') as f:
    json.dump(all_kps, f, ensure_ascii=False, indent=2)

# Verify written file parses correctly
with open('data/kp_full_part_26.json', 'r', encoding='utf-8') as f:
    verify = json.load(f)
print(f'Final file verified: {len(verify)} items')
print(f'Parses OK: True')
