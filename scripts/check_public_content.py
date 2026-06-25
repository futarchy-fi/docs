#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOTS = [Path("content")]
FILES = [Path("mkdocs.yml")]

BLOCKED_PATTERNS = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in [
        r"\bfollow-up questions\b",
        r"\bintentionally a stub\b",
        r"\buseful additions would include\b",
        r"\bapproved for public\b",
        r"\bapproved for external\b",
        r"\bcurrent fundraising status\b",
        r"\bgrant programs being targeted\b",
        r"\bbudget by workstream\b",
        r"\bteam bios\b",
        r"\bTODO\b",
        r"\bTBD\b",
    ]
]


def iter_files():
    for root in ROOTS:
        for path in root.rglob("*"):
            if path.is_file() and path.suffix in {".md", ".yml", ".yaml"}:
                yield path
    for path in FILES:
        if path.exists():
            yield path


findings = []

for path in iter_files():
    text = path.read_text(encoding="utf-8")
    for lineno, line in enumerate(text.splitlines(), start=1):
        for pattern in BLOCKED_PATTERNS:
            if pattern.search(line):
                findings.append(f"{path}:{lineno}: {line.strip()}")
                break

if findings:
    print("Public content check failed:")
    for finding in findings:
        print(f"  {finding}")
    sys.exit(1)

print("Public content check OK")
