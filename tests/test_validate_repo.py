from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = REPO_ROOT / "scripts" / "validate_repo.py"

spec = importlib.util.spec_from_file_location("aca_validate_repo", VALIDATOR_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("Unable to load repository validator.")
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def minimal_guidance(root: Path) -> None:
    write(
        root / "README.md",
        """# AI Cyber Assurance

[Start here](START_HERE.md)
[Automated Review Guide](AUTOMATED_REVIEW_GUIDE.md)
Create a private or access-controlled working package.
The final assurance decision remains human.
""",
    )
    write(
        root / "START_HERE.md",
        """# Start Here

[Automated review](AUTOMATED_REVIEW_GUIDE.md)
[Package](02-evidence-manifests/review-package-index-template.md)
[Evidence](02-evidence-manifests/evidence-manifest-template.md)
[Lifecycle](ASSURANCE_LIFECYCLE.md)
[Rubric](DECISION_RUBRIC.md)
[Decision](02-evidence-manifests/review-decision-template.md)

Do not place evidence in a public repository.
Quick Review
Full Assurance Lifecycle
Module assessment
Assurance recommendation
Final assurance decision
The validator does not prove review truth.
""",
    )
    write(
        root / "AUTOMATED_REVIEW_GUIDE.md",
        """# AI Assistance Instructions

## Scope
## Human Authority
## Evidence Classes
## Automated Assistance May
## Automated Assistance Must
## Automated Assistance Must Not
## Required Output
## Stop Conditions
## Validation Boundary
""",
    )
    write(
        root / "02-evidence-manifests/review-package-index-template.md",
        """# Review Package Index

> **Artifact type:** TEMPLATE
> **Completion status:** Blank for reuse
> **Required for:** Review packages

Required
Conditional
Not Applicable
Not Started
Draft
Blocked
Ready for Review
Complete
Module assessment
Assurance recommendation
Final assurance decision
## Package Completion Rule
""",
    )


class VersionTests(unittest.TestCase):
    def test_version_is_read_from_version_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write(root / "VERSION", "9.8.7\n")
            self.assertEqual(validator.read_version(root), "9.8.7")

    def test_release_requires_explicit_main_dispatch(self) -> None:
        workflow = (REPO_ROOT / ".github" / "workflows" / "validate.yml").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "if: github.event_name == 'workflow_dispatch' && "
            "github.ref == 'refs/heads/main'",
            workflow,
        )
        self.assertNotIn("if: github.event_name == 'push' &&", workflow)

    def test_manifest_comparison_uses_version_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write(root / "VERSION", "9.8.7\n")
            manifest = {
                "repository": "ai-cyber-assurance",
                "target_url": "https://github.com/Bridge-Node-7/ai-cyber-assurance",
                "version": "v9.8.7",
                "file_count": 2,
                "files": ["REPO_MANIFEST.json", "VERSION"],
            }
            write(root / "REPO_MANIFEST.json", json.dumps(manifest) + "\n")
            result = validator.check_manifest(
                root, [Path("REPO_MANIFEST.json"), Path("VERSION")]
            )
            self.assertTrue(result.passed, result.details)

    def test_report_uses_version_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write(root / "VERSION", "9.8.7\n")
            report = validator.build_report(
                root, [validator.CheckResult("sample", True, ["ok"])]
            )
            self.assertEqual(report["version"], "v9.8.7")


class GuidanceTests(unittest.TestCase):
    def test_controlled_repository_guidance_passes(self) -> None:
        result = validator.check_onboarding_and_agent_guidance(REPO_ROOT)
        self.assertTrue(result.passed, result.details)

    def test_missing_start_here_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            minimal_guidance(root)
            (root / "START_HERE.md").unlink()
            result = validator.check_onboarding_and_agent_guidance(root)
            self.assertFalse(result.passed)
            self.assertTrue(any("START_HERE.md" in item for item in result.details))

    def test_missing_agents_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            minimal_guidance(root)
            (root / "AUTOMATED_REVIEW_GUIDE.md").unlink()
            result = validator.check_onboarding_and_agent_guidance(root)
            self.assertFalse(result.passed)
            self.assertTrue(any("AUTOMATED_REVIEW_GUIDE.md" in item for item in result.details))

    def test_missing_readme_start_link_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            minimal_guidance(root)
            write(
                root / "README.md",
                """# AI Cyber Assurance

[Automated review](AUTOMATED_REVIEW_GUIDE.md)
Create a private or access-controlled working package.
The final assurance decision remains human.
""",
            )
            result = validator.check_onboarding_and_agent_guidance(root)
            self.assertFalse(result.passed)
            self.assertTrue(any("START_HERE.md" in item for item in result.details))

    def test_missing_private_workspace_warning_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            minimal_guidance(root)
            write(
                root / "README.md",
                """# AI Cyber Assurance

[Start here](START_HERE.md)
[Automated review](AUTOMATED_REVIEW_GUIDE.md)
The final assurance decision remains human.
""",
            )
            result = validator.check_onboarding_and_agent_guidance(root)
            self.assertFalse(result.passed)
            self.assertTrue(
                any("private or access-controlled" in item for item in result.details)
            )

    def test_missing_decision_hierarchy_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            minimal_guidance(root)
            path = root / "02-evidence-manifests/review-package-index-template.md"
            text = path.read_text(encoding="utf-8").replace("Module assessment\n", "")
            write(path, text)
            result = validator.check_onboarding_and_agent_guidance(root)
            self.assertFalse(result.passed)
            self.assertTrue(any("Module assessment" in item for item in result.details))


if __name__ == "__main__":
    unittest.main()
