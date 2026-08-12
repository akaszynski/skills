"""Tests for the write-like-alex voice audit."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "write-like-alex" / "scripts" / "audit_voice.py"
SPEC = importlib.util.spec_from_file_location("audit_voice", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class AuditVoiceTests(unittest.TestCase):
    def test_direct_pr_prose_matches_anchor(self) -> None:
        text = (
            "Fix the cache lookup\n\n"
            "This fixes the stale cache path. The prior implementation reused "
            "an expired key, so the job now creates a fresh key for each run."
        )
        audit = MODULE.audit_text(text, "pr")
        self.assertEqual(audit.unicode_dashes, 0)
        self.assertEqual(audit.generic_phrases, 0)
        self.assertNotIn("title is longer", " ".join(audit.notes))

    def test_fenced_code_does_not_affect_cadence(self) -> None:
        text = "Found the issue.\n\n```text\nThis generated line is intentionally very very very very long.\n```"
        audit = MODULE.audit_text(text, "review")
        self.assertEqual(audit.sentences, 1)

    def test_unicode_dash_is_hard_violation(self) -> None:
        text = f"Result {chr(0x2014)} follow-up."
        audit = MODULE.audit_text(text, "message")
        self.assertEqual(audit.unicode_dashes, 1)
        self.assertIn("replace Unicode dash punctuation", audit.notes)

    def test_generic_phrase_is_reported(self) -> None:
        audit = MODULE.audit_text("In conclusion, this is groundbreaking.", "docs")
        self.assertEqual(audit.generic_phrases, 2)
        self.assertIn("review generic or promotional phrasing", audit.notes)


if __name__ == "__main__":
    unittest.main()
