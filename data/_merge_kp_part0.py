import json
import sys

batches = [
    "C:/Users/Dean/anesthesia_attending/data/_kp_batch1.json",
    "C:/Users/Dean/anesthesia_attending/data/_kp_batch2.json",
    "C:/Users/Dean/anesthesia_attending/data/_kp_batch3.json",
    "C:/Users/Dean/anesthesia_attending/data/_kp_batch4.json",
    "C:/Users/Dean/anesthesia_attending/data/_kp_batch5.json",
    "C:/Users/Dean/anesthesia_attending/data/_kp_batch6.json",
    "C:/Users/Dean/anesthesia_attending/data/_kp_batch7.json",
]

merged = []
for path in batches:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    merged.extend(data)

# Count by type
kps_count = sum(1 for e in merged if "_type" not in e)
scripts_count = sum(1 for e in merged if e.get("_type") == "illness_script")
pairs_count = sum(1 for e in merged if e.get("_type") == "confusable_pair")

# Count unique topics from KP entries
topics = set()
for e in merged:
    if "_type" not in e:
        topics.add(e.get("topic", ""))
    elif e.get("_type") in ("illness_script", "confusable_pair"):
        topics.add(e.get("topic", "") or e.get("topic_a", ""))

print(f"Total entries: {len(merged)}")
print(f"KPs: {kps_count}")
print(f"Illness scripts: {scripts_count}")
print(f"Confusable pairs: {pairs_count}")
print(f"Unique topics: {len(topics)}")

# Write output
out_path = "C:/Users/Dean/anesthesia_attending/data/kp_full_part_0.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(merged, f, ensure_ascii=False, indent=2)

# Verify it parses back
with open(out_path, encoding="utf-8") as f:
    verify = json.load(f)
print(f"Verification: parsed {len(verify)} entries OK")
print(f"\nFINAL: part 0: {len(topics)} topics, {kps_count} KPs, {scripts_count} scripts, {pairs_count} pairs, parses OK")
