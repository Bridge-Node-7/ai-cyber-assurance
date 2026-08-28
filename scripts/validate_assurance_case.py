#!/usr/bin/env python3
"""Validate a bounded AI Cyber Assurance Case.

Standard-library only. This validator checks structural consistency,
relationship integrity, evidence-class discipline, human authority fields,
and closure preconditions. It does not establish factual truth, evidence
authenticity or sufficiency, real-world control effectiveness, certification,
compliance, deployment approval, or operational authorization.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

EVIDENCE_CLASSES = {"Observed", "Tested", "Reported", "Inferred", "Unknown"}
COLLECTIONS = (
    "identities",
    "claims",
    "risks",
    "controls",
    "evidence",
    "findings",
    "decisions",
    "corrective_actions",
    "retests",
)
REFERENCE_FIELDS = {
    "subject_refs",
    "identity_refs",
    "claim_refs",
    "risk_refs",
    "control_refs",
    "evidence_refs",
    "finding_refs",
    "decision_refs",
    "corrective_action_refs",
    "closure_evidence_refs",
}
SINGLE_REFERENCE_FIELDS = {
    "owner_identity_ref",
    "decision_ref",
    "finding_ref",
    "corrective_action_ref",
    "retest_ref",
}


def load_case(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Assurance Case root must be a JSON object.")
    return data


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_case(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    if data.get("case_version") != "0.1":
        errors.append("case_version must be '0.1'.")

    case = data.get("case")
    if not isinstance(case, dict):
        errors.append("case must be an object.")
        case = {}
    for field in ("id", "title", "scope", "decision_question", "review_path", "reviewed_at", "expires_at"):
        if not _nonempty(case.get(field)):
            errors.append(f"case.{field} is required.")
    if case.get("review_path") not in {"Quick Review", "Full Assurance Lifecycle"}:
        errors.append("case.review_path must be Quick Review or Full Assurance Lifecycle.")
    if not isinstance(case.get("public_synthetic"), bool):
        errors.append("case.public_synthetic must be true or false.")

    objects: list[tuple[str, dict[str, Any]]] = []
    ids: dict[str, str] = {}
    for collection in COLLECTIONS:
        value = data.get(collection)
        if not isinstance(value, list):
            errors.append(f"{collection} must be an array.")
            continue
        for index, item in enumerate(value):
            if not isinstance(item, dict):
                errors.append(f"{collection}[{index}] must be an object.")
                continue
            object_id = item.get("id")
            if not _nonempty(object_id):
                errors.append(f"{collection}[{index}].id is required.")
                continue
            if object_id in ids:
                errors.append(
                    f"Duplicate object ID {object_id!r} in {collection}; first seen in {ids[object_id]}."
                )
            else:
                ids[object_id] = collection
            objects.append((collection, item))

    for collection, item in objects:
        object_id = item.get("id", "<unknown>")
        for field in REFERENCE_FIELDS:
            refs = item.get(field)
            if refs is None:
                continue
            if not isinstance(refs, list):
                errors.append(f"{object_id}.{field} must be an array.")
                continue
            for ref in refs:
                if not _nonempty(ref) or ref not in ids:
                    errors.append(f"{object_id}.{field} contains unresolved reference {ref!r}.")
        for field in SINGLE_REFERENCE_FIELDS:
            ref = item.get(field)
            if ref is None:
                continue
            if not _nonempty(ref) or ref not in ids:
                errors.append(f"{object_id}.{field} has unresolved reference {ref!r}.")

    evidence_by_id: dict[str, dict[str, Any]] = {}
    for item in data.get("evidence", []):
        if not isinstance(item, dict) or not _nonempty(item.get("id")):
            continue
        eid = item["id"]
        evidence_by_id[eid] = item
        evidence_class = item.get("evidence_class")
        if evidence_class not in EVIDENCE_CLASSES:
            errors.append(
                f"{eid}.evidence_class must be one of: {', '.join(sorted(EVIDENCE_CLASSES))}."
            )
        for field in ("source", "owner", "collected_at"):
            if not _nonempty(item.get(field)):
                errors.append(f"{eid}.{field} is required.")
        if not isinstance(item.get("limitations"), list):
            errors.append(f"{eid}.limitations must be an array.")
        if item.get("confidence") is not None and not _nonempty(item.get("confidence_basis")):
            errors.append(f"{eid}.confidence_basis is required when confidence is stated.")

    finding_by_id = {
        item["id"]: item
        for item in data.get("findings", [])
        if isinstance(item, dict) and _nonempty(item.get("id"))
    }
    ca_by_id = {
        item["id"]: item
        for item in data.get("corrective_actions", [])
        if isinstance(item, dict) and _nonempty(item.get("id"))
    }
    retest_by_id = {
        item["id"]: item
        for item in data.get("retests", [])
        if isinstance(item, dict) and _nonempty(item.get("id"))
    }

    for fid, finding in finding_by_id.items():
        if not _nonempty(finding.get("owner")):
            errors.append(f"{fid}.owner is required.")
        status = finding.get("status")
        if status not in {"open", "in_progress", "closed"}:
            errors.append(f"{fid}.status must be open, in_progress, or closed.")

        if status == "closed":
            retest_ref = finding.get("retest_ref")
            closure_refs = finding.get("closure_evidence_refs")
            if not _nonempty(retest_ref):
                errors.append(f"{fid} is closed but has no retest_ref.")
            if not isinstance(closure_refs, list) or not closure_refs:
                errors.append(f"{fid} is closed but has no closure_evidence_refs.")
            else:
                for ref in closure_refs:
                    ev = evidence_by_id.get(ref)
                    if ev and ev.get("evidence_class") == "Unknown":
                        errors.append(f"{fid} uses Unknown evidence {ref} for verified closure.")
            retest = retest_by_id.get(retest_ref) if isinstance(retest_ref, str) else None
            if retest and retest.get("result") != "pass":
                errors.append(f"{fid} is closed but retest {retest_ref} did not pass.")
            for ca_ref in finding.get("corrective_action_refs", []):
                ca = ca_by_id.get(ca_ref)
                if ca and ca.get("status") != "complete":
                    errors.append(f"{fid} is closed but corrective action {ca_ref} is not complete.")

    for decision in data.get("decisions", []):
        if not isinstance(decision, dict) or not _nonempty(decision.get("id")):
            continue
        did = decision["id"]
        if decision.get("consequential") is True:
            authority = decision.get("authority")
            if not isinstance(authority, dict):
                errors.append(f"{did}.authority is required for a consequential decision.")
            else:
                if authority.get("type") != "human":
                    errors.append(f"{did}.authority.type must be 'human'.")
                for field in ("name", "role"):
                    if not _nonempty(authority.get(field)):
                        errors.append(f"{did}.authority.{field} is required.")
        if decision.get("confidence") is not None and not _nonempty(decision.get("confidence_basis")):
            errors.append(f"{did}.confidence_basis is required when confidence is stated.")

    for ca in data.get("corrective_actions", []):
        if not isinstance(ca, dict) or not _nonempty(ca.get("id")):
            continue
        cid = ca["id"]
        if not _nonempty(ca.get("finding_ref")):
            errors.append(f"{cid}.finding_ref is required.")
        if not _nonempty(ca.get("owner")):
            errors.append(f"{cid}.owner is required.")
        if ca.get("status") not in {"proposed", "approved", "in_progress", "complete"}:
            errors.append(f"{cid}.status has an invalid value.")

    for retest in data.get("retests", []):
        if not isinstance(retest, dict) or not _nonempty(retest.get("id")):
            continue
        rid = retest["id"]
        for field in ("tester", "method", "tested_at"):
            if not _nonempty(retest.get(field)):
                errors.append(f"{rid}.{field} is required.")
        if retest.get("result") not in {"pass", "fail"}:
            errors.append(f"{rid}.result must be pass or fail.")
        for ref in retest.get("evidence_refs", []):
            ev = evidence_by_id.get(ref)
            if ev and ev.get("evidence_class") == "Unknown":
                errors.append(f"{rid} cannot use Unknown evidence {ref} as retest evidence.")

    return sorted(set(errors))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("case", type=Path)
    args = parser.parse_args()

    try:
        data = load_case(args.case)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"FAIL - assurance case: {exc}")
        return 1

    errors = validate_case(data)
    if errors:
        print("FAIL - assurance case")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("PASS - assurance case")
    print(f"  case: {data['case']['id']}")
    print(f"  claims: {len(data.get('claims', []))}")
    print(f"  evidence: {len(data.get('evidence', []))}")
    print(f"  findings: {len(data.get('findings', []))}")
    print(f"  corrective_actions: {len(data.get('corrective_actions', []))}")
    print(f"  retests: {len(data.get('retests', []))}")
    print("  boundary: structural validation only; human authority remains final")
    return 0


if __name__ == "__main__":
    sys.exit(main())
