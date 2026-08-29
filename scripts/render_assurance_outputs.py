#!/usr/bin/env python3
"""Render deterministic assurance views from one canonical Assurance Case."""

from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path
from typing import Any


def load_validator():
    path = Path(__file__).with_name("validate_assurance_case.py")
    spec = importlib.util.spec_from_file_location("aca_assurance_validator", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load assurance-case validator.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validator = load_validator()


def _lines(values: list[str]) -> str:
    return "\n".join(f"- {value}" for value in values) if values else "- None recorded"


def _decision(data: dict[str, Any]) -> dict[str, Any]:
    return data["decisions"][0]


def render_decision_receipt(data: dict[str, Any]) -> str:
    case = data["case"]
    decision = _decision(data)
    evidence = data.get("evidence", [])
    by_class = {
        name: [item["id"] for item in evidence if item.get("evidence_class") == name]
        for name in ("Observed", "Tested", "Reported", "Inferred", "Unknown")
    }
    actions = [f'{item["id"]}: {item.get("action", "action not recorded")}' for item in data.get("corrective_actions", [])]
    missing = decision.get("missing_evidence", [])
    conditions = decision.get("conditions", [])
    return f"""# Decision Receipt — {decision["id"]}

> **Artifact type:** GENERATED VIEW  
> **Operational authority:** None  
> **Source of truth:** `{case["id"]}` canonical Assurance Case

## Decision question

{case["decision_question"]}

## Scope

{case["scope"]}

## Evidence considered

### Observed
{_lines(by_class["Observed"])}

### Tested
{_lines(by_class["Tested"])}

### Reported
{_lines(by_class["Reported"])}

### Inferred
{_lines(by_class["Inferred"])}

### Unknown
{_lines(by_class["Unknown"])}

## Missing evidence

{_lines(missing)}

## Human decision

**Disposition:** {decision["disposition"]}

**Authorized human decision owner:** {decision["authority"]["name"]} — {decision["authority"]["role"]}

**Confidence:** {decision.get("confidence", "not stated")}

**Confidence basis:** {decision.get("confidence_basis", "not stated")}

## Conditions

{_lines(conditions)}

## Corrective actions

{_lines(actions)}

## Reversal trigger

{decision.get("reversal_trigger", "None recorded")}

## Review

- Review date: {case["reviewed_at"]}
- Expiration: {case["expires_at"]}

This receipt communicates the bounded human decision recorded in the canonical case. It does not independently certify, authorize, or establish the security of a real system.
"""


def render_passport(data: dict[str, Any]) -> str:
    case = data["case"]
    decision = _decision(data)
    open_findings = [x["id"] for x in data.get("findings", []) if x.get("status") != "closed"]
    identities = [f'{x["id"]}: {x.get("purpose", "purpose not recorded")}' for x in data.get("identities", [])]
    return f"""# Assurance Passport — {case["id"]}

> **Artifact type:** GENERATED VIEW  
> **Operational authority:** None

## System or review subject

**Name:** {case["title"]}

**Purpose and scope:** {case["scope"]}

## Accountable identities

{_lines(identities)}

## Bounded assurance status

**Human decision recorded:** {decision["disposition"]}

**Decision authority:** {decision["authority"]["name"]} — {decision["authority"]["role"]}

**Open findings:** {len(open_findings)}

{_lines(open_findings)}

## Review boundary

- Evidence cutoff / review date: {case["reviewed_at"]}
- Review expires: {case["expires_at"]}
- Reversal trigger: {decision.get("reversal_trigger", "None recorded")}

This passport is a bounded communication view of a recorded human decision. It is not a certification, compliance statement, or claim of indefinite trust.
"""


def render_executive_summary(data: dict[str, Any]) -> str:
    case = data["case"]
    decision = _decision(data)
    risks = [f'{x["id"]}: {x.get("statement", "risk statement not recorded")}' for x in data.get("risks", [])]
    findings = [f'{x["id"]}: {x.get("statement", "finding statement not recorded")}' for x in data.get("findings", [])]
    unknown = [f'{x["id"]}: {x.get("source", "source not recorded")}' for x in data.get("evidence", []) if x.get("evidence_class") == "Unknown"]
    conditions = decision.get("conditions", [])
    return f"""# Executive Summary — {case["id"]}

> **Artifact type:** GENERATED VIEW  
> **Operational authority:** None

## Decision question

{case["decision_question"]}

## Scope

{case["scope"]}

## Material risks

{_lines(risks)}

## Material findings

{_lines(findings)}

## Important Unknowns

{_lines(unknown)}

## Human decision

**{decision["disposition"]}**

**Decision authority:** {decision["authority"]["name"]} — {decision["authority"]["role"]}

## Conditions

{_lines(conditions)}

## Next review

- Expiration: {case["expires_at"]}
- Reversal trigger: {decision.get("reversal_trigger", "None recorded")}

This summary translates the canonical case without inventing additional facts. It does not establish financial loss, probability, certification, compliance, authorization, or real-world control effectiveness.
"""


def render_all(data: dict[str, Any], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    files = {
        "DECISION_RECEIPT.md": render_decision_receipt(data),
        "ASSURANCE_PASSPORT.md": render_passport(data),
        "EXECUTIVE_SUMMARY.md": render_executive_summary(data),
    }
    for name, content in files.items():
        (output_dir / name).write_text(content, encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("case", type=Path)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()

    try:
        data = validator.load_case(args.case)
    except Exception as exc:
        print(f"FAIL - assurance outputs: {exc}")
        return 1

    errors = validator.validate_case(data)
    if errors:
        print("FAIL - assurance outputs: case validation failed")
        for error in errors:
            print(f"  - {error}")
        return 1

    output_dir = args.output_dir or (args.case.parent / "generated")
    render_all(data, output_dir)
    print(f"PASS - rendered assurance outputs to {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
