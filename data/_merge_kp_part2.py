import json, os

batches = [
    'data/_kp_part2_batch1.json',
    'data/_kp_part2_batch2.json',
    'data/_kp_part2_batch3.json',
    'data/_kp_part2_batch4.json',
    'data/_kp_part2_batch5.json',
    'data/_kp_part2_batch6.json',
    'data/_kp_part2_batch7.json',
    'data/_kp_part2_batch8.json',
    'data/_kp_part2_batch9.json',
    'data/_kp_part2_batch10.json',
    'data/_kp_part2_batch11.json',
]

all_kps = []
for b in batches:
    with open(b, 'r', encoding='utf-8') as f:
        items = json.load(f)
    all_kps.extend(items)

# Count types
kp_entries = [x for x in all_kps if not x.get('_type')]
illness_scripts = [x for x in all_kps if x.get('_type') == 'illness_script']
confusable_pairs = [x for x in all_kps if x.get('_type') == 'confusable_pair']

print(f'Total entries: {len(all_kps)}')
print(f'KP entries: {len(kp_entries)}')
print(f'Illness scripts: {len(illness_scripts)}')
print(f'Confusable pairs: {len(confusable_pairs)}')

# Topics covered
topics = sorted(set(x.get('topic', '') for x in kp_entries))
print(f'Topics covered: {len(topics)}')
for t in topics:
    count = sum(1 for x in kp_entries if x.get('topic') == t)
    print(f'  {t}: {count} KPs')

# Write final file
output_path = 'data/kp_catalog_part_2.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_kps, f, ensure_ascii=False, indent=2)

# Verify it parses
with open(output_path, 'r', encoding='utf-8') as f:
    verify = json.load(f)
print(f'\nOutput file: {output_path}')
print(f'Parses OK: {len(verify)} entries')
print(f'File size: {os.path.getsize(output_path):,} bytes')
