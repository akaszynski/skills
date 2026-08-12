#!/usr/bin/env python3
"""Report likely machine-written prose patterns without rewriting the source."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    category: str
    match: str


PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("unicode-dash", re.compile(r"[\u2013\u2014\u2015\u2212]")),
    (
        "decorative-contrast",
        re.compile(r"\b(?:not only\b.{0,80}\bbut also|not\s+\w+\s*[;,]\s*(?:it(?:'s| is)|but)\s+\w+)", re.I),
    ),
    (
        "sycophancy",
        re.compile(r"\b(?:great|excellent|brilliant)\s+(?:question|point|idea)\b", re.I),
    ),
    (
        "signposting",
        re.compile(r"\b(?:here(?:'s| is) the (?:key|important) (?:point|thing)|let(?:'s| us) break (?:it|this) down)\b", re.I),
    ),
    (
        "filler",
        re.compile(r"\b(?:it is important to note that|it should be noted that|in order to)\b", re.I),
    ),
    (
        "chatbot-artifact",
        re.compile(r"\b(?:as an ai|knowledge cutoff|feel free to ask|let me know if you(?:'d| would) like)\b", re.I),
    ),
    (
        "promotional",
        re.compile(r"\b(?:groundbreaking|game-changing|revolutionary|must-see|world-class)\b", re.I),
    ),
    (
        "stock-vocabulary",
        re.compile(r"\b(?:delve|tapestry|testament|pivotal|multifaceted|seamless)\b", re.I),
    ),
    (
        "vague-attribution",
        re.compile(r"\b(?:experts|observers|industry leaders|many people)\s+(?:say|note|believe|agree)\b", re.I),
    ),
    (
        "generic-conclusion",
        re.compile(r"\b(?:in conclusion|the future (?:looks|is) (?:bright|promising))\b", re.I),
    ),
)


def iter_prose_lines(text: str) -> Iterable[tuple[int, str]]:
    """Yield lines outside fenced code blocks."""
    fenced = False
    for number, line in enumerate(text.splitlines(), start=1):
        if re.match(r"^\s*(```|~~~)", line):
            fenced = not fenced
            continue
        if not fenced:
            yield number, line


def audit_text(text: str, path: str = "<stdin>") -> list[Finding]:
    findings: list[Finding] = []
    for number, line in iter_prose_lines(text):
        for category, pattern in PATTERNS:
            for match in pattern.finditer(line):
                findings.append(Finding(path, number, category, match.group(0)))
    return findings


def audit_paths(paths: Sequence[Path]) -> list[Finding]:
    findings: list[Finding] = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        findings.extend(audit_text(text, str(path)))
    return findings


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--json", action="store_true", help="emit JSON findings")
    parser.add_argument(
        "--summary", action="store_true", help="emit counts by category"
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    findings = audit_paths(args.paths)
    if args.json:
        print(json.dumps([asdict(finding) for finding in findings], indent=2))
    else:
        for finding in findings:
            print(
                f"{finding.path}:{finding.line}: "
                f"{finding.category}: {finding.match}"
            )
        if args.summary:
            counts = Counter(finding.category for finding in findings)
            for category, count in sorted(counts.items()):
                print(f"{category}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
