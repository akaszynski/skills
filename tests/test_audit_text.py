#!/usr/bin/env python3
"""Tests for the de-ai-ify audit helper."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "de-ai-ify" / "scripts" / "audit_text.py"
SPEC = importlib.util.spec_from_file_location("audit_text", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class AuditTextTests(unittest.TestCase):
    def test_reports_multiple_pattern_families(self) -> None:
        text = "Great question. Here's the key point - in order to proceed."
        findings = MODULE.audit_text(text)
        categories = {finding.category for finding in findings}
        self.assertEqual(categories, {"sycophancy", "signposting", "filler"})

    def test_skips_fenced_code(self) -> None:
        text = "Before.\n```text\nGreat question - as an AI.\n```\nAfter."
        self.assertEqual(MODULE.audit_text(text), [])

    def test_reports_unicode_dash(self) -> None:
        text = f"Measured value {chr(0x2014)} final value."
        findings = MODULE.audit_text(text)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].category, "unicode-dash")

    def test_keeps_isolated_common_words(self) -> None:
        self.assertEqual(
            MODULE.audit_text("The robust estimator reduced the residual."), []
        )


if __name__ == "__main__":
    unittest.main()
