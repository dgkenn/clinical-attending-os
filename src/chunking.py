from __future__ import annotations

import re
from collections.abc import Iterable


NOISE_PATTERNS = [
    re.compile(r"^copyright\b", re.I),
    re.compile(r"^©"),
    re.compile(r"^\d+\s*$"),
    re.compile(r"^page\s+\d+(\s+of\s+\d+)?$", re.I),
    re.compile(r"^downloaded\s+from\b", re.I),
    re.compile(r"^licensed\s+to\b", re.I),
]


def normalize_line(line: str) -> str:
    line = re.sub(r"(\w)-\s+(\w)", r"\1\2", line)
    return re.sub(r"\s+", " ", line).strip()


def clean_page_text(text: str, repeated_lines: Iterable[str] | None = None) -> str:
    repeated = {line.lower() for line in repeated_lines or []}
    lines = [normalize_line(line) for line in text.splitlines()]
    kept = []
    for line in lines:
        low = line.lower()
        if not line or len(line) < 2:
            continue
        if low in repeated and len(line) < 140:
            continue
        if any(pattern.search(line) for pattern in NOISE_PATTERNS):
            continue
        kept.append(line)
    return "\n".join(kept)


def tokenish_count(text: str) -> int:
    return max(1, len(re.findall(r"\S+", text)))


def detect_section(text: str) -> str:
    for line in text.splitlines()[:14]:
        line = normalize_line(line)
        if not 4 <= len(line) <= 100 or line.endswith("."):
            continue
        alpha = [c for c in line if c.isalpha()]
        uppercase_ratio = sum(c.isupper() for c in alpha) / max(1, len(alpha))
        titleish = len(line.split()) <= 12 and line[:1].isupper()
        numbered = bool(re.match(r"^(\d+(\.\d+)*|[A-Z])[\).:-]\s+\w+", line))
        if uppercase_ratio >= 0.55 or numbered or titleish:
            return line[:90]
    return ""


def _is_heading(line: str) -> bool:
    line = normalize_line(line)
    if not 3 <= len(line) <= 100 or line.endswith("."):
        return False
    words = line.split()
    if len(words) > 14:
        return False
    alpha = [c for c in line if c.isalpha()]
    uppercase_ratio = sum(c.isupper() for c in alpha) / max(1, len(alpha))
    return uppercase_ratio >= 0.55 or bool(re.match(r"^(\d+(\.\d+)*|[A-Z])[\).:-]\s+\w+", line)) or (len(words) <= 8 and line[:1].isupper())


def _blockify(text: str) -> list[str]:
    blocks: list[str] = []
    current: list[str] = []
    for raw_line in text.splitlines():
        line = normalize_line(raw_line)
        if not line:
            if current:
                blocks.append(" ".join(current).strip())
                current = []
            continue
        bullet_or_table = bool(re.match(r"^(\u2022|-|\*|\d+[\).])\s+", line)) or line.count("  ") >= 2 or "\t" in raw_line
        if _is_heading(line):
            if current:
                blocks.append(" ".join(current).strip())
                current = []
            blocks.append(line)
        elif bullet_or_table:
            if current:
                blocks.append(" ".join(current).strip())
                current = []
            blocks.append(line)
        else:
            current.append(line)
    if current:
        blocks.append(" ".join(current).strip())
    return [b for b in blocks if tokenish_count(b) >= 2]


def _split_long_block(block: str, target_tokens: int) -> list[str]:
    words = re.findall(r"\S+", block)
    if len(words) <= target_tokens:
        return [block]
    chunks = []
    for start in range(0, len(words), target_tokens):
        part = " ".join(words[start : start + target_tokens]).strip()
        if part:
            chunks.append(part)
    return chunks


def chunk_page_text(text: str, target_tokens: int = 1000, overlap_tokens: int = 180) -> list[str]:
    if tokenish_count(text) < 40:
        return []
    chunks: list[str] = []
    current: list[str] = []
    current_tokens = 0
    active_heading = detect_section(text)

    for block in _blockify(text):
        if _is_heading(block):
            active_heading = block[:100]
        for part in _split_long_block(block, max(200, target_tokens // 2)):
            part_tokens = tokenish_count(part)
            if current and current_tokens + part_tokens > target_tokens:
                chunk = " ".join(current).strip()
                if tokenish_count(chunk) >= 60:
                    chunks.append(chunk)
                overlap = " ".join(re.findall(r"\S+", chunk)[-overlap_tokens:])
                current = [f"Section: {active_heading}.", overlap] if overlap else [f"Section: {active_heading}."]
                current_tokens = tokenish_count(" ".join(current))
            if active_heading and (not current or not current[0].startswith("Section:")):
                current.append(f"Section: {active_heading}.")
                current_tokens += tokenish_count(current[-1])
            current.append(part)
            current_tokens += part_tokens
    if current:
        chunk = " ".join(current).strip()
        if tokenish_count(chunk) >= 60:
            chunks.append(chunk)
    return chunks
