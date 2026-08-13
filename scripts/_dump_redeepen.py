import sys, json
sys.path.insert(0, '.')
from src.student_model import conn, initialize_database
from src.retrieval import hybrid_search
initialize_database()
with conn() as db:
    # thin topics: <3 KPs in catalog; enrich with curriculum priority
    rows = db.execute('''
        SELECT c.topic, c.domain, c.discipline, c.priority_tier, c.category, c.is_critical_care,
               COUNT(k.id) AS nkp
        FROM curriculum c
        LEFT JOIN kp_catalog k ON k.topic = c.topic
        GROUP BY c.topic
        HAVING nkp < 3
        ORDER BY (CASE WHEN c.category='presentation' THEN 0 ELSE 1 END),
                 c.is_critical_care DESC, c.priority_tier ASC,
                 (CASE WHEN c.discipline='medicine' THEN 0 ELSE 1 END), c.topic
    ''').fetchall()
topics = [dict(r) for r in rows]
print(f'[redeepen] {len(topics)} thin topics to re-author', flush=True)
out = []
for i, r in enumerate(topics):
    try:
        s, _ = hybrid_search(r['topic'], max_results=10)
        chunks = [{'book': x.book or x.filename or '?', 'page': x.page or 0, 'text': (x.text or '')[:900]} for x in s]
    except Exception as e:
        chunks = []; print(f'[redeepen] err {r["topic"]}: {e}', flush=True)
    out.append({'topic': r['topic'], 'domain': r['domain'], 'discipline': r['discipline'],
                'priority_tier': r['priority_tier'], 'category': r['category'],
                'is_critical_care': r['is_critical_care'], 'existing_kps': r['nkp'], 'chunks': chunks})
    if (i + 1) % 50 == 0: print(f'[redeepen] {i+1}/{len(topics)}', flush=True)
json.dump(out, open('data/_kp_redeepen.json', 'w', encoding='utf-8'), ensure_ascii=False)
print(f'[redeepen] DONE -> data/_kp_redeepen.json ({len(out)} topics)', flush=True)
