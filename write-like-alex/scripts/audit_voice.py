#!/usr/bin/env python3
"""Measure prose against register-specific Alex voice anchors."""

from __future__ import annotations

import argparse
import json
import re
import statistics
from collections.abc import Sequence
from dataclasses import asdict, dataclass
from pathlib import Path

WORD = re.compile(r"\b[A-Za-z][A-Za-z'-]*\b")
SENTENCE = re.compile(r"(?<=[.!?])(?:[\"')\]]+)?\s+")
FENCE = re.compile(r"```.*?```|~~~.*?~~~", re.DOTALL)
UNICODE_DASH = re.compile(r"[\u2013\u2014\u2015\u2212]")
GENERIC = re.compile(
    r"\b(?:delve|tapestry|testament|game-changing|groundbreaking|seamless|"
    r"it is important to note that|in today's fast-paced|in conclusion)\b",
    re.IGNORECASE,
)

RANGES = {
    "message": (7, 19),
    "issue": (8, 21),
    "pr": (8, 21),
    "review": (6, 18),
    "commit": (2, 9),
    "docs": (10, 25),
    "paper": (15, 34),
    "report": (12, 30),
    "slides": (2, 18),
}


@dataclass(frozen=True)
class Audit:
    path: str
    mode: str
    words: int
    sentences: int
    median_sentence_words: float
    first_paragraph_words: int
    unicode_dashes: int
    generic_phrases: int
    notes: tuple[str, ...]


def prose(text: str) -> str:
    return FENCE.sub(" ", text)


def audit_text(text: str, mode: str, path: str = "<stdin>") -> Audit:
    cleaned = prose(text)
    words = WORD.findall(cleaned)
    lengths = [
        len(WORD.findall(sentence))
        for sentence in SENTENCE.split(cleaned)
        if len(WORD.findall(sentence)) >= 2
    ]
    median = float(statistics.median(lengths)) if lengths else 0.0
    first_paragraph = re.split(r"\n\s*\n", cleaned.strip(), maxsplit=1)[0]
    first_words = len(WORD.findall(first_paragraph))
    dashes = len(UNICODE_DASH.findall(cleaned))
    generic = len(GENERIC.findall(cleaned))
    low, high = RANGES[mode]
    notes: list[str] = []
    if median and median < low:
        notes.append(
            f"median sentence length {median:g} is below the {mode} anchor {low}-{high}"
        )
    if median > high:
        notes.append(
            f"median sentence length {median:g} is above the {mode} anchor {low}-{high}"
        )
    if first_words > (140 if mode == "paper" else 80):
        notes.append("the opening paragraph may delay the result or request")
    if dashes:
        notes.append("replace Unicode dash punctuation")
    if generic:
        notes.append("review generic or promotional phrasing")
    if mode in {"commit", "issue", "pr"}:
        first_line = cleaned.strip().splitlines()[0] if cleaned.strip() else ""
        title_words = len(WORD.findall(first_line))
        if title_words > 10:
            notes.append("the title is longer than Alex's usual verb-led title")
        if first_line.endswith("."):
            notes.append("remove the title's terminal period")
    return Audit(
        path=path,
        mode=mode,
        words=len(words),
        sentences=len(lengths),
        median_sentence_words=median,
        first_paragraph_words=first_words,
        unicode_dashes=dashes,
        generic_phrases=generic,
        notes=tuple(notes),
    )


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--mode", choices=tuple(RANGES), required=True)
    parser.add_argument("--json", action="store_true")
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail only on hard punctuation violations, not cadence suggestions",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    audits = [
        audit_text(path.read_text(encoding="utf-8"), args.mode, str(path))
        for path in args.paths
    ]
    if args.json:
        print(json.dumps([asdict(audit) for audit in audits], indent=2))
    else:
        for audit in audits:
            print(
                f"{audit.path}: mode={audit.mode} words={audit.words} "
                f"sentences={audit.sentences} median={audit.median_sentence_words:g}"
            )
            for note in audit.notes:
                print(f"  - {note}")
    return int(args.check and any(audit.unicode_dashes for audit in audits))


if __name__ == "__main__":
    raise SystemExit(main())
