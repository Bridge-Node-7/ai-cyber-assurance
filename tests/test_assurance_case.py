from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = REPO_ROOT / "scripts" / "validate_assurance_case.py"
RENDERER_PATH = REPO_ROOT / "scripts" / "render_assurance_outputs.py"
CASE_PATH = REPO_ROOT / "10-examples" / "synthetic-ai-agent-assurance" / "assurance-case.json"

spec = importlib.util.spec_from_file_location("aca_assurance_validator_test", VALIDATOR_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("Unable to load assurance-case validator.")
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)

render_spec = importlib.util.spec_from_file_location("aca_assurance_renderer_test", RENDERER_PATH)
if render_spec is None or render_spec.loader is None:
    raise RuntimeError("Unable to load assurance renderer.")
renderer = importlib.util.module_from_spec(render_spec)
sys.modules[render_spec.name] = renderer
render_spec.loader.exec_module(renderer)


def load_fixture() -> dict:
    return json.loads(CASE_PATH.read_text(encoding="utf-8"))


class AssuranceCaseTests(unittest.TestCase):
    def test_valid_completed_case_passes(self) -> None:
        self.assertEqual(validator.validate_case(load_fixture()), [])

    def test_duplicate_id_fails(self) -> None:
        data = load_fixture()
        data["controls"][0]["id"] = data["identities"][0]["id"]
        self.assertTrue(any("Duplicate object ID" in x for x in validator.validate_case(data)))

    def test_dangling_evidence_reference_fails(self) -> None:
        data = load_fixture()
        data["claims"][0]["evidence_refs"].append("EVID-MISSING")
        self.assertTrue(any("unresolved reference" in x for x in validator.validate_case(data)))

    def test_finding_without_owner_fails(self) -> None:
        data = load_fixture()
        data["findings"][0]["owner"] = ""
        self.assertTrue(any("FIND-001.owner is required" in x for x in validator.validate_case(data)))

    def test_invalid_evidence_class_fails(self) -> None:
        data = load_fixture()
        data["evidence"][0]["evidence_class"] = "Recommended"
        self.assertTrue(any("evidence_class" in x for x in validator.validate_case(data)))

    def test_missing_human_authority_fails(self) -> None:
        data = load_fixture()
        data["decisions"][0]["authority"]["type"] = "agent"
        self.assertTrue(any("authority.type" in x for x in validator.validate_case(data)))

    def test_corrective_action_without_finding_fails(self) -> None:
        data = load_fixture()
        data["corrective_actions"][0]["finding_ref"] = ""
        errors = validator.validate_case(data)
        self.assertTrue(any("finding_ref is required" in x for x in errors))

    def test_closed_finding_without_retest_fails(self) -> None:
        data = load_fixture()
        data["findings"][0]["retest_ref"] = ""
        errors = validator.validate_case(data)
        self.assertTrue(any("closed but has no retest_ref" in x for x in errors))

    def test_failed_retest_cannot_close_finding(self) -> None:
        data = load_fixture()
        data["retests"][0]["result"] = "fail"
        errors = validator.validate_case(data)
        self.assertTrue(any("did not pass" in x for x in errors))

    def test_unknown_cannot_support_closure(self) -> None:
        data = load_fixture()
        data["findings"][0]["closure_evidence_refs"] = ["EVID-003"]
        errors = validator.validate_case(data)
        self.assertTrue(any("uses Unknown evidence" in x for x in errors))

    def test_unknown_cannot_be_retest_evidence(self) -> None:
        data = load_fixture()
        data["retests"][0]["evidence_refs"] = ["EVID-003"]
        errors = validator.validate_case(data)
        self.assertTrue(any("cannot use Unknown evidence" in x for x in errors))

    def test_renderer_is_deterministic_and_consistent(self) -> None:
        data = load_fixture()
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            renderer.render_all(data, Path(first))
            renderer.render_all(data, Path(second))
            for name in ("DECISION_RECEIPT.md", "ASSURANCE_PASSPORT.md", "EXECUTIVE_SUMMARY.md"):
                one = (Path(first) / name).read_text(encoding="utf-8")
                two = (Path(second) / name).read_text(encoding="utf-8")
                self.assertEqual(one, two)
                self.assertIn(data["case"]["id"], one)
                self.assertIn(data["decisions"][0]["disposition"], one)


if __name__ == "__main__":
    unittest.main()
