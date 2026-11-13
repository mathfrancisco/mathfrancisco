#!/usr/bin/env python3
"""Static checks for a GitHub profile README; no external network dependencies."""
import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / 'README.md'
MAX_SVG_BYTES = 80_000
errors = []
md = README.read_text(encoding='utf-8')

# Local refs in Markdown image syntax and HTML img/srcset attributes.
refs = re.findall(r'!\[[^\]]*\]\(([^)\s]+)', md)
refs += re.findall(r'\b(?:src|srcset)="([^"]+)"', md)
refs += re.findall(r'\]\((docs/[^)]+)\)', md)
for ref in refs:
    path = ref.split('#', 1)[0]
    if not path or path.startswith(('https://', 'http://', 'mailto:', '#')):
        continue
    candidate = (ROOT / path).resolve()
    try:
        candidate.relative_to(ROOT)
    except ValueError:
        errors.append(f'unsafe relative path: {ref}')
        continue
    if not candidate.exists():
        errors.append(f'missing local asset: {ref}')

svgs = sorted((ROOT / 'assets').rglob('*.svg'))
if len(svgs) < 5:
    errors.append(f'expected five or more local SVGs; got {len(svgs)}')
for svg in svgs:
    size = svg.stat().st_size
    if size > MAX_SVG_BYTES:
        errors.append(f'{svg.relative_to(ROOT)} is too large ({size} B)')
    try:
        tree = ET.parse(svg)
        if not tree.getroot().tag.endswith('svg'):
            errors.append(f'not an SVG root: {svg}')
    except ET.ParseError as exc:
        errors.append(f'XML parse error in {svg}: {exc}')
    data = svg.read_text(encoding='utf-8')
    if re.search(r'<script\b|<foreignObject\b|https?://(?!www\.w3\.org/2000/svg)', data, re.I):
        errors.append(f'potential active/external content in {svg}')

# External dynamic images are deliberately banned for performance/reliability.
if re.search(r'<img[^>]+src="https?://|!\[[^\]]*\]\(https?://', md):
    errors.append('external image found in profile README')

if errors:
    print('PROFILE VALIDATION FAILED:')
    for e in errors:
        print(' - ' + e)
    sys.exit(1)
print(f'OK — {len(svgs)} SVG assets parsed, paths resolved, no external images.')
