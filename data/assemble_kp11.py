import json, sys, importlib.util, os
sys.stdout.reconfigure(encoding='utf-8')

all_kps = []

scripts = [
    'data/build_kp11.py',
    'data/build_kp11b.py',
    'data/build_kp11c.py',
    'data/build_kp11d.py',
    'data/build_kp11e.py',
    'data/build_kp11f.py',
    'data/build_kp11g.py',
    'data/build_kp11h.py',
    'data/build_kp11i.py',
]

for script_path in scripts:
    spec = importlib.util.spec_from_file_location("mod", script_path)
    mod = importlib.util.module_from_spec(spec)
    # Capture kps from each module by executing and reading the kps variable
    ns = {}
    with open(script_path, 'r', encoding='utf-8') as f:
        src = f.read()
    exec(compile(src, script_path, 'exec'), ns)
    batch = ns.get('kps', [])
    all_kps.extend(batch)
    print(f"{script_path}: {len(batch)} items")

# Validate: check all IDs unique
ids = [k.get('id','') for k in all_kps if 'id' in k]
dupes = [i for i in ids if ids.count(i) > 1]
if dupes:
    print(f"DUPLICATE IDs: {set(dupes)}")
else:
    print("All IDs unique.")

# Count by type
kp_count = sum(1 for k in all_kps if '_type' not in k)
script_count = sum(1 for k in all_kps if k.get('_type') == 'illness_script')
pair_count = sum(1 for k in all_kps if k.get('_type') == 'confusable_pair')

print(f"\nTotal items: {len(all_kps)}")
print(f"  KPs: {kp_count}")
print(f"  Illness scripts: {script_count}")
print(f"  Confusable pairs: {pair_count}")

# Write output
out_path = 'data/kp_full_part_11.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(all_kps, f, ensure_ascii=False, indent=2)

# Verify it parses back
with open(out_path, 'r', encoding='utf-8') as f:
    check = json.load(f)
print(f"\nParses OK: {len(check)} items in {out_path}")
print(f"\npart 11: 33 topics, {kp_count} KPs, {script_count} scripts, {pair_count} pairs, parses OK")
