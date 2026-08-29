#!/usr/bin/env python3
"""Validate a bounded AI Cyber Assurance Case.

Standard-library only. This validator checks structural consistency,
typed relationship integrity, evidence-class discipline, human authority
fields, date fields, and closure preconditions. It does not establish
factual truth, evidence authenticity or sufficiency, real-world control
effectiveness, certification, compliance, deployment approval, or
operational authorization.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

EVIDENCE_CLASSES = {"Observed", "Tested", "Reported", "Inferred", "Unknown"}
CASE_VERSION = "0.2"
REVIEW_PATHS = {"Quick Review", "Full Assurance Lifecycle"}

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
    "review_history",
)

REFERENCE_FIELDS: dict[str, str] = {
    "subject_refs": "identities",
    "identity_refs": "identities",
    "claim_refs": "claims",
    "risk_refs": "risks",
    "control_refs": "controls",
    "evidence_refs": "evidence",
    "finding_refs": "findings",
    "decision_refs": "decisions",
    "corrective_action_refs": "corrective_actions",
    "closure_evidence_refs": "evidence",
}

SINGLE_REFERENCE_FIELDS: dict[str, str] = {
    "owner_identity_ref": "identities",
    "accountable_human_ref": "identities",
    "decision_ref": "decisions",
    "finding_ref": "findings",
    "corrective_action_ref": "corrective_actions",
    "retest_ref": "retests",
}


def load_case(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Assurance Case root must be a JSON object.")
    return data


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _parse_date(value: Any, label: str, errors: list[str]) -> date | None:
    if not _nonempty(value):
        errors.append(f"{label} is required.")
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        errors.append(f"{label} must be an ISO date (YYYY-MM-DD).")
        return None


def validate_case(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    if data.get("case_version") != CASE_VERSION:
        errors.append(f"case_version must be {CASE_VERSION!r}.")

    case = data.get("case")
    if not isinstance(case, dict):
        errors.append("case must be an object.")
        case = {}
    for field in ("id", "title", "scope", "decision_question"):
        if not _nonempty(case.get(field)):
            errors.append(f"case.{field} is required.")
    if case.get("review_path") not in REVIEW_PATHS:
        errors.append("case.review_path must be Quick Review or Full Assurance Lifecycle.")
    if not isinstance(case.get("public_synthetic"), bool):
        errors.append("case.public_synthetic must be true or false.")
    reviewed = _parse_date(case.get("reviewed_at"), "case.reviewed_at", errors)
    expires = _parse_date(case.get("expires_at"), "case.expires_at", errors)
    if reviewed and expires and expires < reviewed:
        errors.append("case.expires_at must not precede case.reviewed_at.")

    objects: list[tuple[str, dict[str, Any]]] = []
    ids: dict[str, str] = {}
    by_collection: dict[str, dict[str, dict[str, Any]]] = {name: {} for name in COLLECTIONS}
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
                by_collection[collection][object_id] = item
            objects.append((collection, item))

    decisions = data.get("decisions", [])
    if isinstance(decisions, list) and len(decisions) != 1:
        errors.append("decisions must contain exactly one bounded decision.")

    for _collection, item in objects:
        object_id = item.get("id", "<unknown>")
        for field, expected_collection in REFERENCE_FIELDS.items():
            refs = item.get(field)
            if refs is None:
                continue
            if not isinstance(refs, list):
                errors.append(f"{object_id}.{field} must be an array.")
                continue
            for ref in refs:
                if not _nonempty(ref) or ref not in ids:
                    errors.append(f"{object_id}.{field} contains unresolved reference {ref!r}.")
                elif ids[ref] != expected_collection:
                    errors.append(
                        f"{object_id}.{field} reference {ref!r} must target {expected_collection}, not {ids[ref]}."
                    )
        for field, expected_collection in SINGLE_REFERENCE_FIELDS.items():
            ref = item.get(field)
            if ref is None:
                continue
            if not _nonempty(ref) or ref not in ids:
                errors.append(f"{object_id}.{field} has unresolved reference {ref!r}.")
            elif ids[ref] != expected_collection:
                errors.append(
                    f"{object_id}.{field} reference {ref!r} must target {expected_collection}, not {ids[ref]}."
                )

    identities = by_collection["identities"]
    for identity_id, identity in identities.items():
        identity_type = str(identity.get("type", "")).strip().lower()
        if not identity_type:
            errors.append(f"{identity_id}.type is required.")
            continue
        if identity_type != "human":
            accountable_ref = identity.get("accountable_human_ref")
            if not _nonempty(accountable_ref):
                errors.append(f"{identity_id}.accountable_human_ref is required for a nonhuman identity.")
            else:
                target = identities.get(accountable_ref)
                if target and str(target.get("type", "")).strip().lower() != "human":
                    errors.append(
                        f"{identity_id}.accountable_human_ref must reference an identity with type 'human'."
                    )

    evidence_by_id = by_collection["evidence"]
    for eid, item in evidence_by_id.items():
        evidence_class = item.get("evidence_class")
        if evidence_class not in EVIDENCE_CLASSES:
            errors.append(
                f"{eid}.evidence_class must be one of: {', '.join(sorted(EVIDENCE_CLASSES))}."
            )
        for field in ("source", "owner"):
            if not _nonempty(item.get(field)):
                errors.append(f"{eid}.{field} is required.")
        _parse_date(item.get("collected_at"), f"{eid}.collected_at", errors)
        if not isinstance(item.get("limitations"), list):
            errors.append(f"{eid}.limitations must be an array.")
        if item.get("confidence") is not None and not _nonempty(item.get("confidence_basis")):
            errors.append(f"{eid}.confidence_basis is required when confidence is stated.")

    finding_by_id = by_collection["findings"]
    ca_by_id = by_collection["corrective_actions"]
    retest_by_id = by_collection["retests"]
    decision_by_id = by_collection["decisions"]

    for did, decision in decision_by_id.items():
        if not _nonempty(decision.get("disposition")):
            errors.append(f"{did}.disposition is required.")
        authority = decision.get("authority")
        if not isinstance(authority, dict):
            errors.append(f"{did}.authority is required for the bounded human decision.")
        else:
            if str(authority.get("type", "")).strip().lower() != "human":
                errors.append(f"{did}.authority.type must be 'human'.")
            for field in ("name", "role"):
                if not _nonempty(authority.get(field)):
                    errors.append(f"{did}.authority.{field} is required.")
        if decision.get("confidence") is not None and not _nonempty(decision.get("confidence_basis")):
            errors.append(f"{did}.confidence_basis is required when confidence is stated.")

    sole_decision_id = next(iter(decision_by_id), None) if len(decision_by_id) == 1 else None

    for cid, ca in ca_by_id.items():
        if not _nonempty(ca.get("finding_ref")):
            errors.append(f"{cid}.finding_ref is required.")
        if not _nonempty(ca.get("owner")):
            errors.append(f"{cid}.owner is required.")
        if ca.get("status") not in {"proposed", "approved", "in_progress", "complete"}:
            errors.append(f"{cid}.status has an invalid value.")
        if not _nonempty(ca.get("decision_ref")):
            errors.append(f"{cid}.decision_ref is required to preserve human decision linkage.")
        elif sole_decision_id and ca.get("decision_ref") != sole_decision_id:
            errors.append(f"{cid}.decision_ref must reference the case's bounded decision {sole_decision_id}.")

    for rid, retest in retest_by_id.items():
        for field in ("tester", "method"):
            if not _nonempty(retest.get(field)):
                errors.append(f"{rid}.{field} is required.")
        _parse_date(retest.get("tested_at"), f"{rid}.tested_at", errors)
        if retest.get("result") not in {"pass", "fail"}:
            errors.append(f"{rid}.result must be pass or fail.")
        if not isinstance(retest.get("independent"), bool):
            errors.append(f"{rid}.independent must be true or false.")
        elif retest.get("independent") is False and not _nonempty(retest.get("independence_rationale")):
            errors.append(f"{rid}.independence_rationale is required when independent is false.")
        for ref in retest.get("evidence_refs", []):
            ev = evidence_by_id.get(ref)
            if ev and ev.get("evidence_class") == "Unknown":
                errors.append(f"{rid} cannot use Unknown evidence {ref} as retest evidence.")

    for fid, finding in finding_by_id.items():
        if not _nonempty(finding.get("owner")):
            errors.append(f"{fid}.owner is required.")
        status = finding.get("status")
        if status not in {"open", "in_progress", "closed"}:
            errors.append(f"{fid}.status must be open, in_progress, or closed.")

        if status == "closed":
            retest_ref = finding.get("retest_ref")
            closure_refs = finding.get("closure_evidence_refs")
            ca_refs = finding.get("corrective_action_refs")
            if not _nonempty(retest_ref):
                errors.append(f"{fid} is closed but has no retest_ref.")
            if not isinstance(closure_refs, list) or not closure_refs:
                errors.append(f"{fid} is closed but has no closure_evidence_refs.")
            else:
                for ref in closure_refs:
                    ev = evidence_by_id.get(ref)
                    if ev and ev.get("evidence_class") == "Unknown":
                        errors.append(f"{fid} uses Unknown evidence {ref} for verified closure.")
            if not isinstance(ca_refs, list) or not ca_refs:
                errors.append(f"{fid} is closed but has no corrective_action_refs.")
            retest = retest_by_id.get(retest_ref) if isinstance(retest_ref, str) else None
            if retest and retest.get("result") != "pass":
                errors.append(f"{fid} is closed but retest {retest_ref} did not pass.")
            if retest and retest.get("finding_ref") != fid:
                errors.append(f"{fid} retest {retest_ref} must reference the same finding.")
            for ca_ref in ca_refs if isinstance(ca_refs, list) else []:
                ca = ca_by_id.get(ca_ref)
                if ca and ca.get("status") != "complete":
                    errors.append(f"{fid} is closed but corrective action {ca_ref} is not complete.")
                if ca and ca.get("finding_ref") != fid:
                    errors.append(f"{fid} corrective action {ca_ref} must reference the same finding.")
                if ca and sole_decision_id and ca.get("decision_ref") != sole_decision_id:
                    errors.append(f"{fid} corrective action {ca_ref} is not linked to the bounded decision.")

    for hid, history in by_collection["review_history"].items():
        for field in ("actor", "summary"):
            if not _nonempty(history.get(field)):
                errors.append(f"{hid}.{field} is required.")
        _parse_date(history.get("date"), f"{hid}.date", errors)

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
