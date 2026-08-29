from __future__ import annotations

import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

ACTIONABLE_RECORDS = (
    "04-llm-risk/llm-risk-register.md",
    "06-software-supply-chain/sbom-readiness.md",
    "07-cyber-survivability/cyber-survivability-review.md",
    "08-high-impact-systems/high-impact-system-readiness.md",
    "09-incident-review/incident-review-template.md",
    "11-assurance-lifecycle/security-policy-and-target-template.md",
    "11-assurance-lifecycle/identity-and-authority-register.md",
    "11-assurance-lifecycle/threat-control-evidence-map.md",
    "11-assurance-lifecycle/control-validation-record.md",
    "11-assurance-lifecycle/recovery-assurance-record.md",
    "13-assurance-intelligence/partner-kit/START_HERE.md",
    "13-assurance-intelligence/partner-kit/intake-template.md",
    "13-assurance-intelligence/partner-kit/confidentiality-boundary.md",
)


class NavigationTests(unittest.TestCase):
    def test_actionable_records_have_navigation_spine(self) -> None:
        for rel in ACTIONABLE_RECORDS:
            text = (REPO_ROOT / rel).read_text(encoding="utf-8")
            with self.subTest(rel=rel):
                self.assertIn("## Navigation", text)
                self.assertIn("START_HERE.md", text)

    def test_partner_start_links_intake_and_confidentiality_first(self) -> None:
        text = (REPO_ROOT / "13-assurance-intelligence/partner-kit/START_HERE.md").read_text(encoding="utf-8")
        self.assertIn("[Confidentiality Boundary](confidentiality-boundary.md)", text)
        self.assertIn("[Assurance Case Intake Template](intake-template.md)", text)
        self.assertLess(text.index("confidentiality-boundary.md"), text.index("## Pilot fit gate"))

    def test_partner_documents_cross_link(self) -> None:
        intake = (REPO_ROOT / "13-assurance-intelligence/partner-kit/intake-template.md").read_text(encoding="utf-8")
        boundary = (REPO_ROOT / "13-assurance-intelligence/partner-kit/confidentiality-boundary.md").read_text(encoding="utf-8")
        self.assertIn("confidentiality-boundary.md", intake)
        self.assertIn("intake-template.md", boundary)


if __name__ == "__main__":
    unittest.main()
