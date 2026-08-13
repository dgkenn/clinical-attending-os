r"""
fetch_statpearls.py
====================
Bulk-fetch StatPearls articles from NCBI Bookshelf (open-access, CC BY-NC-ND 4.0).

Access method (confirmed June 2026):
  - ESearch: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi
              db=books, term=<topic>[Title] AND StatPearls[Book]
  - ESummary: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi
              db=books — returns accessionid (NBK ID), rtype, title per uid
  - Bookshelf HTML: https://www.ncbi.nlm.nih.gov/books/<NBK_ID>/
              Full chapter text, fetched and stripped with BeautifulSoup.

Rate limit: <=3 req/sec without API key (NCBI_API_KEY env var optional for 10/sec).
Writes ONLY to D:\corpus_staging\statpearls\.
Filenames: "StatPearls - <Article Title>.txt" for ingest pipeline source tagging.
Resumable: skips already-downloaded files.
Disk-aware: aborts if D: free < 5 GB.

Usage:
    python scripts/fetch_statpearls.py [--limit N] [--tier {1,2,3,all}] [--dry-run]

    --limit N      Process only first N medicine topics (default: all 555)
    --tier         Filter by priority_tier (1=highest). Default: all.
    --dry-run      Search only, don't download. Shows what would be fetched.
    --delay SECS   Override per-request delay (default: 0.34s = ~3/sec)

Full run command:
    python scripts/fetch_statpearls.py
"""

import argparse
import json
import os
import re
import shutil
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
BLUEPRINT_PATH = Path("C:/Users/Dean/anesthesia_attending/data/curriculum_blueprint.json")
OUTPUT_DIR = Path("D:/corpus_staging/statpearls")
MIN_FREE_GB = 5.0

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
BOOKSHELF_URL = "https://www.ncbi.nlm.nih.gov/books/"

# NCBI API key speeds up to 10 req/sec; without it, stay <=3/sec
NCBI_API_KEY = os.environ.get("NCBI_API_KEY", "")
if NCBI_API_KEY:
    REQUEST_DELAY = 0.11   # ~9/sec, safe with key
    print(f"[config] NCBI_API_KEY found — using 10 req/sec mode")
else:
    REQUEST_DELAY = 0.34   # ~3/sec, no key

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; anesthesia_attending corpus fetcher; "
        "contact: dgkenn@bu.edu; NCBI E-utils academic use)"
    ),
    "Accept": "text/html,application/json,application/xml",
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def check_disk():
    """Abort if D: has less than MIN_FREE_GB free."""
    usage = shutil.disk_usage("D:/")
    free_gb = usage.free / (1024 ** 3)
    if free_gb < MIN_FREE_GB:
        sys.exit(f"[ABORT] D: drive only {free_gb:.1f} GB free (need >={MIN_FREE_GB} GB)")
    return free_gb


def safe_filename(title: str) -> str:
    """Sanitize a title for use as a filename (Windows-safe)."""
    # Remove / replace chars that are illegal on Windows filesystems
    title = re.sub(r'[\\/:*?"<>|]', "-", title)
    title = re.sub(r"\s+", " ", title).strip()
    # Truncate to avoid hitting 260-char path limit
    if len(title) > 180:
        title = title[:177] + "..."
    return f"StatPearls - {title}.txt"


def ncbi_get(endpoint: str, params: dict, delay: float) -> dict | str | None:
    """
    GET an NCBI E-utilities endpoint. Returns parsed JSON dict for ?retmode=json,
    or raw bytes string for HTML. Returns None on error.
    """
    if NCBI_API_KEY:
        params["api_key"] = NCBI_API_KEY
    qs = urllib.parse.urlencode(params)
    url = f"{BASE_URL}{endpoint}?{qs}"
    time.sleep(delay)
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read()
        if params.get("retmode") == "json":
            return json.loads(raw.decode("utf-8"))
        return raw.decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  [warn] NCBI request failed: {e} — url: {url}")
        return None


def bookshelf_html(nbk_id: str, delay: float) -> str | None:
    """Fetch the Bookshelf HTML page for an NBK chapter ID."""
    url = f"{BOOKSHELF_URL}{nbk_id}/"
    time.sleep(delay)
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=45) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  [warn] HTML fetch failed for {nbk_id}: {e}")
        return None


def extract_text_from_html(html: str, nbk_id: str) -> str:
    """
    Parse StatPearls Bookshelf HTML and extract clean article text.
    Uses BeautifulSoup when available; falls back to regex stripping.
    """
    try:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")

        # Remove script, style, nav, header, footer, aside
        for tag in soup.find_all(["script", "style", "nav", "header",
                                   "footer", "aside", "noscript"]):
            tag.decompose()

        # The main article content lives in <div class="book-part"> or
        # <article> or <div id="maincontent">
        content_tags = (
            soup.find("article")
            or soup.find("div", id="maincontent")
            or soup.find("div", class_="book-part")
            or soup.find("main")
            or soup.find("body")
        )
        if content_tags is None:
            return ""

        # Extract paragraphs, headings, list items
        parts = []
        for elem in content_tags.find_all(
            ["h1", "h2", "h3", "h4", "p", "li", "td", "th"]
        ):
            txt = elem.get_text(" ", strip=True)
            if txt and len(txt) > 20:   # skip stub labels
                parts.append(txt)

        text = "\n\n".join(parts)
        return text

    except ImportError:
        # Regex fallback: strip all HTML tags
        text = re.sub(r"<script[^>]*>.*?</script>", "", html,
                      flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r"<style[^>]*>.*?</style>", "", text,
                      flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r"<[^>]+>", " ", text)
        text = re.sub(r"&amp;", "&", text)
        text = re.sub(r"&lt;", "<", text)
        text = re.sub(r"&gt;", ">", text)
        text = re.sub(r"&nbsp;", " ", text)
        text = re.sub(r"&#\d+;", " ", text)
        text = re.sub(r"\s{3,}", "\n\n", text)
        return text.strip()


def search_statpearls_chapters(topic: str, delay: float) -> list[dict]:
    """
    Search StatPearls for articles matching the given topic title.
    Returns a list of {'uid', 'nbk_id', 'title'} dicts for rtype=chapter entries.
    Prefers exact title match; falls back to first chapter result.
    """
    # Build a cascade of search terms from most to least specific.
    # StatPearls article titles often differ from blueprint topic titles in:
    #   - Subtitles (after colon): "STEMI: Diagnosis..." -> "STEMI"
    #   - Conjunctions: "AFib and Flutter" -> "Atrial Fibrillation"
    #   - Parenthetical qualifiers: "HFpEF" stem only
    #   - Abbreviation expansion: "NSTEMI" -> search abbreviation directly
    #   - Plural vs singular: "Arrhythmias" -> "Arrhythmia" etc.
    short_topic = topic.split(":")[0].split("(")[0].strip()
    # Try first component before "and" / "or" connector
    and_split = short_topic.split(" and ")[0].split(" or ")[0].strip()
    # Try parenthetical abbreviation if present (e.g. "HFrEF" from "(HFrEF)")
    paren_match = re.search(r"\(([A-Za-z0-9\-]+)\)", topic)
    abbrev = paren_match.group(1) if paren_match else None

    # Also try de-pluralizing the last word (e.g. "Tachycardias" -> "Tachycardia")
    def desingularize(s):
        """Strip trailing 's' from the last word if it likely makes it singular."""
        words = s.split()
        if words and words[-1].endswith("s") and len(words[-1]) > 4:
            words[-1] = words[-1][:-1]
            return " ".join(words)
        return s

    and_split_desing = desingularize(and_split)
    short_topic_desing = desingularize(short_topic)

    seen = set()
    search_terms = []
    candidates = [
        f'"{topic}"[Title] AND StatPearls[Book]',
        f'{topic}[Title] AND StatPearls[Book]',
        f'"{short_topic}"[Title] AND StatPearls[Book]' if short_topic != topic else None,
        f'{short_topic}[Title] AND StatPearls[Book]' if short_topic != topic else None,
        f'"{and_split}"[Title] AND StatPearls[Book]' if and_split not in (topic, short_topic) else None,
        f'{and_split}[Title] AND StatPearls[Book]' if and_split not in (topic, short_topic) else None,
        # De-pluralized variants
        f'"{short_topic_desing}"[Title] AND StatPearls[Book]' if short_topic_desing != short_topic else None,
        f'{short_topic_desing}[Title] AND StatPearls[Book]' if short_topic_desing != short_topic else None,
        f'"{and_split_desing}"[Title] AND StatPearls[Book]' if and_split_desing != and_split else None,
        f'{and_split_desing}[Title] AND StatPearls[Book]' if and_split_desing != and_split else None,
        # Abbreviation from parenthetical
        f'"{abbrev}"[Title] AND StatPearls[Book]' if abbrev else None,
        f'{abbrev}[Title] AND StatPearls[Book]' if abbrev else None,
    ]
    for term in candidates:
        if term and term not in seen:
            seen.add(term)
            search_terms.append(term)

    ids = []
    for search_term in search_terms:
        result = ncbi_get("esearch.fcgi", {
            "db": "books",
            "term": search_term,
            "retmax": "10",
            "retmode": "json",
        }, delay)
        if not result:
            continue
        ids = result.get("esearchresult", {}).get("idlist", [])
        if ids:
            break

    if not ids:
        return []

    if not ids:
        return []

    # ESummary to get accession IDs and rtypes
    summary = ncbi_get("esummary.fcgi", {
        "db": "books",
        "id": ",".join(ids),
        "retmode": "json",
    }, delay)
    if not summary:
        return []

    result_map = summary.get("result", {})
    uids = result_map.get("uids", [])

    chapters = []
    fallback_nbk_ids = {}  # chapteraccessionid -> title from non-chapter hits

    for uid in uids:
        entry = result_map.get(uid, {})
        rtype = entry.get("rtype", "")
        nbk_id = entry.get("chapteraccessionid") or entry.get("accessionid", "")
        title = entry.get("title", "")
        if rtype == "chapter" and nbk_id:
            chapters.append({"uid": uid, "nbk_id": nbk_id, "title": title})
        elif nbk_id and rtype not in ("book",):
            # Non-chapter result (section, figure, table) — save its parent chapter NBK
            if nbk_id not in fallback_nbk_ids:
                fallback_nbk_ids[nbk_id] = title

    # If no direct chapter hits, use parent-chapter NBK IDs from non-chapter results
    if not chapters and fallback_nbk_ids:
        for nbk_id, title in fallback_nbk_ids.items():
            chapters.append({"uid": "fallback", "nbk_id": nbk_id, "title": topic})

    # Sort chapters so the one whose title best matches the topic comes first.
    # Scoring: exact match > title contains topic words > anything
    topic_words = set(re.sub(r"[^a-z0-9\s]", "", topic.lower()).split())

    def match_score(ch):
        ctitle = re.sub(r"[^a-z0-9\s]", "", ch["title"].lower())
        ctitle_words = set(ctitle.split())
        if ctitle == re.sub(r"[^a-z0-9\s]", "", topic.lower()):
            return 100  # exact
        overlap = len(topic_words & ctitle_words)
        return overlap

    chapters.sort(key=match_score, reverse=True)
    return chapters


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Fetch StatPearls IM articles from NCBI Bookshelf")
    parser.add_argument("--limit", type=int, default=None,
                        help="Process only first N medicine topics")
    parser.add_argument("--tier", type=str, default="all",
                        choices=["1", "2", "3", "all"],
                        help="Filter by priority_tier (1=highest)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Search only; do not download")
    parser.add_argument("--delay", type=float, default=None,
                        help="Per-request delay seconds (default: auto)")
    args = parser.parse_args()

    delay = args.delay if args.delay is not None else REQUEST_DELAY

    # Disk check
    free_gb = check_disk()
    print(f"[disk] D: free: {free_gb:.1f} GB")

    # Ensure output dir exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Load blueprint
    with open(BLUEPRINT_PATH, encoding="utf-8") as f:
        blueprint = json.load(f)

    # Filter to medicine topics
    topics = [t for t in blueprint if t.get("discipline") == "medicine"]
    if args.tier != "all":
        tier_n = int(args.tier)
        topics = [t for t in topics if t.get("priority_tier") == tier_n]
    if args.limit:
        topics = topics[:args.limit]

    print(f"[plan] {len(topics)} medicine topics to process")
    print(f"[plan] Output dir: {OUTPUT_DIR}")
    print(f"[plan] Request delay: {delay:.2f}s")

    # Log file for this run
    log_path = OUTPUT_DIR / "fetch_log.jsonl"
    stats = {"found": 0, "downloaded": 0, "skipped_existing": 0,
             "not_found": 0, "error": 0}

    not_found = []

    for idx, topic_entry in enumerate(topics):
        topic_title = topic_entry["topic"]
        print(f"\n[{idx+1}/{len(topics)}] '{topic_title}'")

        # Disk check every 50 topics
        if idx % 50 == 0 and idx > 0:
            free_gb = check_disk()
            print(f"  [disk] D: free: {free_gb:.1f} GB")

        # Search for StatPearls chapters
        chapters = search_statpearls_chapters(topic_title, delay)

        if not chapters:
            print(f"  [miss] No StatPearls chapter found")
            stats["not_found"] += 1
            not_found.append(topic_title)
            with open(log_path, "a", encoding="utf-8") as lf:
                lf.write(json.dumps({
                    "topic": topic_title, "status": "not_found"
                }) + "\n")
            continue

        # Use first chapter result (best match from title search)
        chapter = chapters[0]
        nbk_id = chapter["nbk_id"]
        article_title = chapter["title"] or topic_title
        print(f"  [hit] {nbk_id}: '{article_title}'")
        stats["found"] += 1

        # Build output filename using the topic title (for consistency with blueprint)
        out_filename = safe_filename(topic_title)
        out_path = OUTPUT_DIR / out_filename

        # Resumable: skip if already downloaded
        if out_path.exists() and out_path.stat().st_size > 500:
            print(f"  [skip] Already exists ({out_path.stat().st_size:,} bytes)")
            stats["skipped_existing"] += 1
            with open(log_path, "a", encoding="utf-8") as lf:
                lf.write(json.dumps({
                    "topic": topic_title, "status": "existing",
                    "nbk_id": nbk_id, "file": out_filename
                }) + "\n")
            continue

        if args.dry_run:
            print(f"  [dry-run] Would download → {out_filename}")
            continue

        # Fetch HTML from Bookshelf
        html = bookshelf_html(nbk_id, delay)
        if not html:
            print(f"  [err] Failed to fetch HTML for {nbk_id}")
            stats["error"] += 1
            with open(log_path, "a", encoding="utf-8") as lf:
                lf.write(json.dumps({
                    "topic": topic_title, "status": "fetch_error", "nbk_id": nbk_id
                }) + "\n")
            continue

        # Extract clean text
        text = extract_text_from_html(html, nbk_id)

        # Validate we got real content (not an error page)
        if len(text) < 300:
            print(f"  [err] Too little text ({len(text)} chars) — possible error page")
            stats["error"] += 1
            with open(log_path, "a", encoding="utf-8") as lf:
                lf.write(json.dumps({
                    "topic": topic_title, "status": "short_content",
                    "nbk_id": nbk_id, "chars": len(text)
                }) + "\n")
            continue

        # Prepend source header for ingest pipeline tagging
        header = (
            f"Source: StatPearls\n"
            f"NCBI Bookshelf NBK ID: {nbk_id}\n"
            f"URL: {BOOKSHELF_URL}{nbk_id}/\n"
            f"Topic: {topic_title}\n"
            f"Article Title: {article_title}\n"
            f"License: CC BY-NC-ND 4.0\n"
            f"{'='*60}\n\n"
        )

        out_path.write_text(header + text, encoding="utf-8")
        print(f"  [ok] Saved {out_path.stat().st_size:,} bytes -> {out_filename}")
        stats["downloaded"] += 1

        with open(log_path, "a", encoding="utf-8") as lf:
            lf.write(json.dumps({
                "topic": topic_title, "status": "ok", "nbk_id": nbk_id,
                "file": out_filename, "bytes": out_path.stat().st_size,
                "chars": len(text)
            }) + "\n")

    # Final summary
    print(f"\n{'='*60}")
    print(f"DONE: {len(topics)} topics processed")
    print(f"  Found:            {stats['found']}")
    print(f"  Downloaded:       {stats['downloaded']}")
    print(f"  Skipped (exist):  {stats['skipped_existing']}")
    print(f"  Not found:        {stats['not_found']}")
    print(f"  Errors:           {stats['error']}")
    print(f"  Log:              {log_path}")

    if not_found:
        print(f"\nTopics with no StatPearls chapter found ({len(not_found)}):")
        for t in not_found[:20]:
            print(f"  - {t}")
        if len(not_found) > 20:
            print(f"  ... and {len(not_found)-20} more (see log)")


if __name__ == "__main__":
    main()
