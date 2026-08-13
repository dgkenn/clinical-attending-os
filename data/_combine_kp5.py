import json, sys, importlib.util, os
sys.stdout.reconfigure(encoding='utf-8')

# Execute each build script and collect kps list
all_kps = []

for script in ['data/_build_kp5.py', 'data/_build_kp5b.py', 'data/_build_kp5c.py']:
    with open(script, 'r', encoding='utf-8') as f:
        code = f.read()
    # Remove the print statement at the end
    code = code.rsplit('\nprint(', 1)[0]
    ns = {'json': json, 'sys': sys}
    exec(code, ns)
    all_kps.extend(ns['kps'])

print(f"Total KPs before dedup: {len(all_kps)}", file=sys.stderr)

# Check for duplicate IDs
ids = [k['id'] for k in all_kps if 'id' in k]
dupes = [i for i in ids if ids.count(i) > 1]
if dupes:
    print(f"DUPLICATE IDs: {set(dupes)}", file=sys.stderr)

# Count by type
scripts = [k for k in all_kps if k.get('_type') == 'illness_script']
pairs = [k for k in all_kps if k.get('_type') == 'confusable_pair']
kps_only = [k for k in all_kps if 'id' in k and '_type' not in k]

print(f"KPs: {len(kps_only)}, illness_scripts: {len(scripts)}, confusable_pairs: {len(pairs)}", file=sys.stderr)
print(f"TOTAL items: {len(all_kps)}", file=sys.stderr)

# Count unique topics
topics = set(k.get('topic','') for k in all_kps)
print(f"Unique topics covered: {len(topics)}", file=sys.stderr)

# Write output
out_path = 'data/kp_full_part_5.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(all_kps, f, ensure_ascii=False, indent=2)

print(f"Written to {out_path}", file=sys.stderr)

# Verify it parses back
with open(out_path, 'r', encoding='utf-8') as f:
    check = json.load(f)
assert len(check) == len(all_kps), "Parse mismatch!"
print("parses OK", file=sys.stderr)

# Print summary for final message
print(f"SUMMARY|topics={len(topics)}|kps={len(kps_only)}|scripts={len(scripts)}|pairs={len(pairs)}|total={len(all_kps)}")
