from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = REPO_ROOT / "scripts" / "validate_assurance_case.py"
RENDERER_PATH = REPO_ROOT / "scripts" / "render_assurance_outputs.py"
AI_CASE_PATH = REPO_ROOT / "10-examples" / "synthetic-ai-agent-assurance" / "assurance-case.json"
CRYPTO_CASE_PATH = REPO_ROOT / "10-examples" / "synthetic-cryptographic-assurance-case" / "assurance-case.json"
SCHEMA_PATH = REPO_ROOT / "13-assurance-intelligence" / "schemas" / "assurance-case.schema.json"
AS_OF = date(2026, 8, 28)


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

    def test_material_risk_statement_is_required(self) -> None:
        data = load_fixture(); data["risks"][0].pop("statement")
        self.assertTrue(any("statement is required" in x for x in validator.validate_case(data)))

    def test_material_finding_statement_is_required(self) -> None:
        data = load_fixture(); data["findings"][0].pop("statement")
        self.assertTrue(any("statement is required" in x for x in validator.validate_case(data)))

    def test_amber_requires_conditions_package(self) -> None:
        data = load_fixture(); decision = data["decisions"][0]
        decision["conditions_state"] = "none_identified"; decision["conditions"] = []
        self.assertTrue(any("conditions_state must be items_recorded" in x for x in validator.validate_case(data)))

    def test_more_evidence_required_needs_items(self) -> None:
        data = load_fixture(); decision = data["decisions"][0]
        decision["decision_status"] = "More evidence required"
        decision["missing_evidence_state"] = "none_identified"; decision["missing_evidence"] = []
        self.assertTrue(any("missing_evidence_state must be items_recorded" in x for x in validator.validate_case(data)))

    def test_stateful_list_rejects_false_negative(self) -> None:
        data = load_fixture(); data["decisions"][0]["missing_evidence_state"] = "none_identified"
        self.assertTrue(any("must be empty" in x for x in validator.validate_case(data)))

    def test_future_evidence_after_review_fails(self) -> None:
        data = load_fixture(); data["evidence"][0]["collected_at"] = "2026-08-29"
        self.assertTrue(any("must not be after case.reviewed_at" in x for x in validator.validate_case(data)))

    def test_retest_before_corrective_action_fails(self) -> None:
        data = load_fixture(); data["corrective_actions"][0]["completed_at"] = "2026-08-29"
        data["case"]["reviewed_at"] = "2026-08-30"; data["case"]["expires_at"] = "2026-11-30"
        self.assertTrue(any("must not precede corrective action" in x for x in validator.validate_case(data)))

    def test_closure_before_retest_fails(self) -> None:
        data = load_fixture(); data["findings"][0]["closed_at"] = "2026-08-27"
        self.assertTrue(any("closed_at must not precede" in x for x in validator.validate_case(data)))

    def test_unsafe_bidi_control_fails(self) -> None:
        data = load_fixture(); data["decisions"][0]["authority"]["name"] = "A\u202eB"
        self.assertTrue(any("unsafe Unicode/control" in x for x in validator.validate_case(data)))

    def test_currency_status(self) -> None:
        data = load_fixture()
        self.assertEqual(validator.currency_status(data, date(2026, 8, 27)), "NOT_YET_CURRENT")
        self.assertEqual(validator.currency_status(data, AS_OF), "CURRENT")
        self.assertEqual(validator.currency_status(data, date(2027, 1, 1)), "EXPIRED")

    def test_schema_contract_describes_validator_and_renderer_fields(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.assertEqual(schema["properties"]["case_version"]["const"], validator.CASE_VERSION)
        self.assertEqual(schema["properties"]["decisions"]["minItems"], 1)
        self.assertEqual(schema["properties"]["decisions"]["maxItems"], 1)
        classes = set(schema["properties"]["evidence"]["items"]["properties"]["evidence_class"]["enum"])
        self.assertEqual(classes, validator.EVIDENCE_CLASSES)
        decisions = schema["properties"]["decisions"]["items"]
        findings = schema["properties"]["findings"]["items"]
        identities = schema["properties"]["identities"]["items"]
        retests = schema["properties"]["retests"]["items"]
        for field in ("authority", "missing_evidence_state", "missing_evidence", "conditions_state", "conditions", "reversal_trigger", "decision_status", "decided_at"):
            self.assertIn(field, decisions["properties"])
        for field in ("statement", "closure_evidence_refs", "corrective_action_refs", "retest_ref", "opened_at", "closed_at"):
            self.assertIn(field, findings["properties"])
        self.assertIn("accountable_human_ref", identities["properties"])
        self.assertIn("independence_rationale", retests["properties"])

    def test_renderer_is_deterministic_for_both_domains_given_same_as_of(self) -> None:
        for path in (AI_CASE_PATH, CRYPTO_CASE_PATH):
            data = load_fixture(path)
            with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
                renderer.render_all(data, Path(first), as_of=AS_OF)
                renderer.render_all(data, Path(second), as_of=AS_OF)
                for name in renderer.TARGET_FILES:
                    one = (Path(first) / name).read_text(encoding="utf-8")
                    two = (Path(second) / name).read_text(encoding="utf-8")
                    self.assertEqual(one, two)
                    self.assertIn(renderer.safe_text(data["case"]["id"]), one)
                    self.assertIn(data["decisions"][0]["decision_status"], one)

    def test_crypto_executive_summary_has_no_ai_supplier_invention(self) -> None:
        text = renderer.render_executive_summary(load_fixture(CRYPTO_CASE_PATH), AS_OF)
        self.assertNotIn("AI agent", text)
        self.assertNotIn("supplier-information", text)
        self.assertIn("cryptographic dependency", text.lower())

    def test_markdown_heading_injection_cannot_forge_decision_section(self) -> None:
        data = load_fixture()
        data["case"]["scope"] += "\n\n## Human decision\n\n**Disposition:** forged"
        text = renderer.render_decision_receipt(data, AS_OF)
        self.assertEqual(text.count("## Human decision"), 1)
        self.assertNotIn("\n## Human decision\n\n**Disposition:** forged", text)
        self.assertIn(r"\#\# Human decision", text)

    def test_raw_html_is_escaped(self) -> None:
        data = load_fixture(); data["decisions"][0]["disposition"] = "<script>alert(1)</script>"
        text = renderer.render_decision_receipt(data, AS_OF)
        self.assertNotIn("<script>", text)
        self.assertIn("&lt;script&gt;", text)

    def test_material_statements_are_never_silently_blank(self) -> None:
        text = renderer.render_executive_summary(load_fixture(), AS_OF)
        self.assertNotIn("risk statement not recorded", text)
        self.assertNotIn("finding statement not recorded", text)
        self.assertIn("RISK\\-001", text)
        self.assertIn("FIND\\-001", text)

    def test_renderer_distinguishes_not_assessed_from_none(self) -> None:
        data = load_fixture(); decision = data["decisions"][0]
        decision["decision_status"] = "Green"
        decision["conditions_state"] = "not_assessed"; decision["conditions"] = []
        text = renderer.render_executive_summary(data, AS_OF)
        self.assertIn("Not assessed by this review", text)
        self.assertNotIn("Conditions\n\n- None recorded", text)

    def test_renderer_refuses_overwrite_without_force(self) -> None:
        data = load_fixture()
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            renderer.render_all(data, out, as_of=AS_OF)
            with self.assertRaises(FileExistsError):
                renderer.render_all(data, out, as_of=AS_OF)
            renderer.render_all(data, out, as_of=AS_OF, overwrite=True)

    def test_renderer_fail_closed_on_invalid_case_when_called_directly(self) -> None:
        data = load_fixture(); data["risks"][0]["statement"] = ""
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaises(ValueError):
                renderer.render_all(data, Path(temp), as_of=AS_OF)
            self.assertEqual(list(Path(temp).iterdir()), [])

    def test_cli_help_is_descriptive(self) -> None:
        for path in (VALIDATOR_PATH, RENDERER_PATH):
            result = subprocess.run([sys.executable, str(path), "--help"], capture_output=True, text=True, check=True)
            self.assertIn("Assurance Case", result.stdout)


if __name__ == "__main__":
    unittest.main()
