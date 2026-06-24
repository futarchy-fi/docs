#!/usr/bin/env python3
from pathlib import Path
import re
import sys
from urllib.parse import unquote

root = Path("content")
link_re = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
missing = []

for path in root.rglob("*.md"):
    text = path.read_text(encoding="utf-8")
    for match in link_re.finditer(text):
        href = match.group(1).strip()
        if not href or href.startswith(("#", "http://", "https://", "mailto:")):
            continue
        target = unquote(href.split("#", 1)[0])
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        candidates = [
            resolved,
            resolved.with_suffix(".md") if not resolved.suffix else resolved,
            resolved / "README.md",
            resolved / "index.md",
        ]
        if not any(candidate.exists() for candidate in candidates):
            missing.append(f"{path}: {href}")

if missing:
    print("Broken internal links:")
    for item in missing:
        print(f"  {item}")
    sys.exit(1)

print("Internal markdown links OK")
