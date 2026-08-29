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
AI_CASE_PATH = REPO_ROOT / "10-examples" / "synthetic-ai-agent-assurance" / "assurance-case.json"
CRYPTO_CASE_PATH = REPO_ROOT / "10-examples" / "synthetic-cryptographic-assurance-case" / "assurance-case.json"
SCHEMA_PATH = REPO_ROOT / "13-assurance-intelligence" / "schemas" / "assurance-case.schema.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {path}.")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


validator = load_module("aca_assurance_validator_test", VALIDATOR_PATH)
renderer = load_module("aca_assurance_renderer_test", RENDERER_PATH)


def load_fixture(path: Path = AI_CASE_PATH) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class AssuranceCaseTests(unittest.TestCase):
    def test_valid_ai_case_passes(self) -> None:
        self.assertEqual(validator.validate_case(load_fixture()), [])

    def test_valid_second_domain_case_passes(self) -> None:
        self.assertEqual(validator.validate_case(load_fixture(CRYPTO_CASE_PATH)), [])

    def test_duplicate_id_fails(self) -> None:
        data = load_fixture(); data["controls"][0]["id"] = data["identities"][0]["id"]
        self.assertTrue(any("Duplicate object ID" in x for x in validator.validate_case(data)))

    def test_dangling_reference_fails(self) -> None:
        data = load_fixture(); data["claims"][0]["evidence_refs"].append("EVID-MISSING")
        self.assertTrue(any("unresolved reference" in x for x in validator.validate_case(data)))

    def test_wrong_type_reference_fails(self) -> None:
        data = load_fixture(); data["claims"][0]["evidence_refs"] = ["CTRL-001"]
        self.assertTrue(any("must target evidence" in x for x in validator.validate_case(data)))

    def test_invalid_evidence_class_fails(self) -> None:
        data = load_fixture(); data["evidence"][0]["evidence_class"] = "Recommended"
        self.assertTrue(any("evidence_class" in x for x in validator.validate_case(data)))

    def test_empty_decision_array_fails(self) -> None:
        data = load_fixture(); data["decisions"] = []
        self.assertTrue(any("exactly one bounded decision" in x for x in validator.validate_case(data)))

    def test_multiple_decisions_fail(self) -> None:
        data = load_fixture(); data["decisions"].append(dict(data["decisions"][0], id="DEC-002"))
        self.assertTrue(any("exactly one bounded decision" in x for x in validator.validate_case(data)))

    def test_nonhuman_identity_requires_accountable_human(self) -> None:
        data = load_fixture(); data["identities"][1].pop("accountable_human_ref")
        self.assertTrue(any("accountable_human_ref is required" in x for x in validator.validate_case(data)))

    def test_accountable_human_must_be_human(self) -> None:
        data = load_fixture(); data["identities"][1]["accountable_human_ref"] = "ID-AI-001"
        self.assertTrue(any("must reference an identity with type 'human'" in x for x in validator.validate_case(data)))

    def test_missing_human_authority_fails(self) -> None:
        data = load_fixture(); data["decisions"][0]["authority"]["type"] = "agent"
        self.assertTrue(any("authority.type" in x for x in validator.validate_case(data)))

    def test_corrective_action_requires_decision_link(self) -> None:
        data = load_fixture(); data["corrective_actions"][0]["decision_ref"] = ""
        self.assertTrue(any("decision_ref is required" in x for x in validator.validate_case(data)))

    def test_closed_finding_without_retest_fails(self) -> None:
        data = load_fixture(); data["findings"][0]["retest_ref"] = ""
        self.assertTrue(any("closed but has no retest_ref" in x for x in validator.validate_case(data)))

    def test_failed_retest_cannot_close_finding(self) -> None:
        data = load_fixture(); data["retests"][0]["result"] = "fail"
        self.assertTrue(any("did not pass" in x for x in validator.validate_case(data)))

    def test_retest_must_reference_same_finding(self) -> None:
        data = load_fixture(); data["retests"][0]["finding_ref"] = "FIND-002"
        self.assertTrue(any("must reference the same finding" in x for x in validator.validate_case(data)))

    def test_unknown_cannot_support_closure(self) -> None:
        data = load_fixture(); data["findings"][0]["closure_evidence_refs"] = ["EVID-003"]
        self.assertTrue(any("uses Unknown evidence" in x for x in validator.validate_case(data)))

    def test_unknown_cannot_be_retest_evidence(self) -> None:
        data = load_fixture(); data["retests"][0]["evidence_refs"] = ["EVID-003"]
        self.assertTrue(any("cannot use Unknown evidence" in x for x in validator.validate_case(data)))

    def test_nonindependent_retest_requires_rationale(self) -> None:
        data = load_fixture(); data["retests"][0]["independent"] = False
        self.assertTrue(any("independence_rationale is required" in x for x in validator.validate_case(data)))

    def test_invalid_date_fails(self) -> None:
        data = load_fixture(); data["case"]["reviewed_at"] = "08/28/2026"
        self.assertTrue(any("ISO date" in x for x in validator.validate_case(data)))

    def test_expiration_before_review_fails(self) -> None:
        data = load_fixture(); data["case"]["expires_at"] = "2026-01-01"
        self.assertTrue(any("must not precede" in x for x in validator.validate_case(data)))

    def test_review_history_is_validated(self) -> None:
        data = load_fixture(); data["review_history"][0]["actor"] = ""
        self.assertTrue(any("REV-001.actor is required" in x for x in validator.validate_case(data)))

    def test_schema_contract_matches_core_validator_constants(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.assertEqual(schema["properties"]["case_version"]["const"], validator.CASE_VERSION)
        self.assertEqual(schema["properties"]["decisions"]["minItems"], 1)
        self.assertEqual(schema["properties"]["decisions"]["maxItems"], 1)
        classes = set(schema["properties"]["evidence"]["items"]["properties"]["evidence_class"]["enum"])
        self.assertEqual(classes, validator.EVIDENCE_CLASSES)

    def test_renderer_is_deterministic_for_both_domains(self) -> None:
        for path in (AI_CASE_PATH, CRYPTO_CASE_PATH):
            data = load_fixture(path)
            with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
                renderer.render_all(data, Path(first)); renderer.render_all(data, Path(second))
                for name in ("DECISION_RECEIPT.md", "ASSURANCE_PASSPORT.md", "EXECUTIVE_SUMMARY.md"):
                    one = (Path(first) / name).read_text(encoding="utf-8")
                    two = (Path(second) / name).read_text(encoding="utf-8")
                    self.assertEqual(one, two)
                    self.assertIn(data["case"]["id"], one)
                    self.assertIn(data["decisions"][0]["disposition"], one)

    def test_committed_ai_outputs_match_renderer(self) -> None:
        data = load_fixture(AI_CASE_PATH)
        with tempfile.TemporaryDirectory() as temp:
            renderer.render_all(data, Path(temp))
            committed = AI_CASE_PATH.parent / "generated"
            for name in ("DECISION_RECEIPT.md", "ASSURANCE_PASSPORT.md", "EXECUTIVE_SUMMARY.md"):
                self.assertEqual(
                    (Path(temp) / name).read_text(encoding="utf-8"),
                    (committed / name).read_text(encoding="utf-8"),
                )

    def test_crypto_executive_summary_has_no_ai_supplier_invention(self) -> None:
        text = renderer.render_executive_summary(load_fixture(CRYPTO_CASE_PATH))
        self.assertNotIn("AI agent", text)
        self.assertNotIn("supplier-information", text)
        self.assertIn("cryptographic dependency", text.lower())


if __name__ == "__main__":
    unittest.main()
