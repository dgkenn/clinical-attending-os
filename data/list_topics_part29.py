#!/usr/bin/env python3
"""List all topics in part 29."""
import json

with open('data/kp_full_part_29.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

kps = [x for x in data if 'id' in x and '_type' not in x]
topics = {}
for kp in kps:
    topic = kp.get('topic')
    if topic not in topics:
        topics[topic] = 0
    topics[topic] += 1

print("All topics and KP counts:")
for i, (topic, count) in enumerate(sorted(topics.items()), 1):
    print(f"{i:2d}. {topic}: {count} KPs")
