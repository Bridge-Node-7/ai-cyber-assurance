#!/usr/bin/env python3
"""Render safe, deterministic assurance views from one canonical Assurance Case."""

from __future__ import annotations

import argparse
import html
import importlib.util
import re
import unicodedata
from datetime import date
from pathlib import Path
from typing import Any

TARGET_FILES = ("DECISION_RECEIPT.md", "ASSURANCE_PASSPORT.md", "EXECUTIVE_SUMMARY.md")
MARKDOWN_META = re.compile(r"([\\`*_{}\[\]()#+.!|>\-])")


def load_validator():
    path = Path(__file__).with_name("validate_assurance_case.py")
    spec = importlib.util.spec_from_file_location("aca_assurance_validator", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load assurance-case validator.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validator = load_validator()


def _visible_control(char: str) -> str:
    return f"[U+{ord(char):04X}]"


def safe_text(value: Any) -> str:
    """Escape case-controlled text so it cannot create Markdown structure or raw HTML."""
    text = str(value)
    cleaned: list[str] = []
    for char in text:
        category = unicodedata.category(char)
        if category == "Cf" or (category == "Cc" and char not in {"\n", "\r", "\t"}):
            cleaned.append(_visible_control(char))
        else:
            cleaned.append(char)
    escaped_lines: list[str] = []
    for line in "".join(cleaned).replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        escaped = html.escape(line, quote=False)
        escaped = MARKDOWN_META.sub(r"\\\1", escaped)
        escaped_lines.append(escaped)
    return "<br>\n".join(escaped_lines)


def _lines(values: list[str], empty_text: str) -> str:
    return "\n".join(f"- {safe_text(value)}" for value in values) if values else f"- {empty_text}"


def _stateful_lines(decision: dict[str, Any], field: str, state_field: str) -> str:
    values = decision[field]
    state = decision[state_field]
    if state == "items_recorded":
        return _lines(values, "Items were expected but not recorded")
    labels = {
        "none_identified": "None identified in the bounded review",
        "not_assessed": "Not assessed by this review",
        "not_applicable": "Not applicable to this bounded decision",
        "unknown": "Unknown / not established",
    }
    return f"- {labels[state]}"


def _decision(data: dict[str, Any]) -> dict[str, Any]:
    return data["decisions"][0]


def _currency(data: dict[str, Any], as_of: date) -> str:
    return validator.currency_status(data, as_of)


def render_decision_receipt(data: dict[str, Any], as_of: date) -> str:
    case = data["case"]
    decision = _decision(data)
    evidence = data.get("evidence", [])
    by_class = {
        name: [item["id"] for item in evidence if item.get("evidence_class") == name]
        for name in ("Observed", "Tested", "Reported", "Inferred", "Unknown")
    }
    actions = [f'{item["id"]}: {item["action"]}' for item in data.get("corrective_actions", [])]
    return f"""# Decision Receipt — {safe_text(decision["id"])}

> **Artifact type:** GENERATED VIEW  
> **Operational authority:** None  
> **Source of truth:** `{safe_text(case["id"])}` canonical Assurance Case  
> **Currency as of {as_of.isoformat()}:** {_currency(data, as_of)}

## Decision question

{safe_text(case["decision_question"])}

## Scope

{safe_text(case["scope"])}

## Evidence considered

### Observed
{_lines(by_class["Observed"], "None identified in the canonical evidence set")}

### Tested
{_lines(by_class["Tested"], "None identified in the canonical evidence set")}

### Reported
{_lines(by_class["Reported"], "None identified in the canonical evidence set")}

### Inferred
{_lines(by_class["Inferred"], "None identified in the canonical evidence set")}

### Unknown
{_lines(by_class["Unknown"], "None identified in the canonical evidence set")}

## Missing evidence

{_stateful_lines(decision, "missing_evidence", "missing_evidence_state")}

## Human decision

**Status:** {safe_text(decision["decision_status"])}

**Disposition:** {safe_text(decision["disposition"])}

**Authorized human decision owner:** {safe_text(decision["authority"]["name"])} — {safe_text(decision["authority"]["role"])}

**Confidence:** {safe_text(decision.get("confidence", "not stated"))}

**Confidence basis:** {safe_text(decision.get("confidence_basis", "not stated"))}

## Conditions

{_stateful_lines(decision, "conditions", "conditions_state")}

## Corrective actions

{_lines(actions, "No corrective actions recorded for this bounded case")}

## Reversal trigger

{safe_text(decision["reversal_trigger"])}

## Review

- Decision date: {safe_text(decision["decided_at"])}
- Review date / evidence cutoff: {safe_text(case["reviewed_at"])}
- Expiration: {safe_text(case["expires_at"])}
- Currency as of {as_of.isoformat()}: {_currency(data, as_of)}

This receipt communicates the bounded human decision recorded in the canonical case. It does not independently certify, authorize, or establish the security of a real system.
"""


def render_passport(data: dict[str, Any], as_of: date) -> str:
    case = data["case"]
    decision = _decision(data)
    open_findings = [x["id"] for x in data.get("findings", []) if x.get("status") != "closed"]
    identities = [f'{x["id"]}: {x["purpose"]}' for x in data.get("identities", [])]
    return f"""# Assurance Passport — {safe_text(case["id"])}

> **Artifact type:** GENERATED VIEW  
> **Operational authority:** None  
> **Currency as of {as_of.isoformat()}:** {_currency(data, as_of)}

## System or review subject

**Name:** {safe_text(case["title"])}

**Purpose and scope:** {safe_text(case["scope"])}

## Accountable identities

{_lines(identities, "No identities recorded")}

## Bounded assurance status

**Decision status:** {safe_text(decision["decision_status"])}

**Human decision recorded:** {safe_text(decision["disposition"])}

**Decision authority:** {safe_text(decision["authority"]["name"])} — {safe_text(decision["authority"]["role"])}

**Open findings:** {len(open_findings)}

{_lines(open_findings, "None identified as open in the canonical case")}

## Review boundary

- Evidence cutoff / review date: {safe_text(case["reviewed_at"])}
- Review expires: {safe_text(case["expires_at"])}
- Currency as of {as_of.isoformat()}: {_currency(data, as_of)}
- Reversal trigger: {safe_text(decision["reversal_trigger"])}

This passport is a bounded communication view of a recorded human decision. It is not a certification, compliance statement, or claim of indefinite trust.
"""


def render_executive_summary(data: dict[str, Any], as_of: date) -> str:
    case = data["case"]
    decision = _decision(data)
    risks = [f'{x["id"]}: {x["statement"]}' for x in data.get("risks", [])]
    findings = [f'{x["id"]}: {x["statement"]}' for x in data.get("findings", [])]
    unknown = [f'{x["id"]}: {x["source"]}' for x in data.get("evidence", []) if x.get("evidence_class") == "Unknown"]
    return f"""# Executive Summary — {safe_text(case["id"])}

> **Artifact type:** GENERATED VIEW  
> **Operational authority:** None  
> **Currency as of {as_of.isoformat()}:** {_currency(data, as_of)}

## Decision question

{safe_text(case["decision_question"])}

## Scope

{safe_text(case["scope"])}

## Material risks

{_lines(risks, "None identified in the canonical risk set")}

## Material findings

{_lines(findings, "None identified in the canonical finding set")}

## Important Unknowns

{_lines(unknown, "None identified in the canonical evidence set")}

## Human decision

**Status:** {safe_text(decision["decision_status"])}

**Disposition:** {safe_text(decision["disposition"])}

**Decision authority:** {safe_text(decision["authority"]["name"])} — {safe_text(decision["authority"]["role"])}

## Conditions

{_stateful_lines(decision, "conditions", "conditions_state")}

## Next review

- Expiration: {safe_text(case["expires_at"])}
- Currency as of {as_of.isoformat()}: {_currency(data, as_of)}
- Reversal trigger: {safe_text(decision["reversal_trigger"])}

This summary translates the canonical case without inventing additional facts. It does not establish financial loss, probability, certification, compliance, authorization, or real-world control effectiveness.
"""


def _check_output_fidelity(files: dict[str, str]) -> None:
    for name, content in files.items():
        if "<script" in content.lower():
            raise ValueError(f"Unsafe raw HTML survived rendering in {name}.")
    for name in ("DECISION_RECEIPT.md", "EXECUTIVE_SUMMARY.md"):
        if files[name].count("## Human decision") != 1:
            raise ValueError(f"{name} must contain exactly one Human decision section.")


def render_all(data: dict[str, Any], output_dir: Path, *, as_of: date, overwrite: bool = False) -> None:
    errors = validator.validate_case(data)
    if errors:
        raise ValueError("Case validation failed: " + "; ".join(errors))
    files = {
        "DECISION_RECEIPT.md": render_decision_receipt(data, as_of),
        "ASSURANCE_PASSPORT.md": render_passport(data, as_of),
        "EXECUTIVE_SUMMARY.md": render_executive_summary(data, as_of),
    }
    _check_output_fidelity(files)
    output_dir.mkdir(parents=True, exist_ok=True)
    existing = [name for name in TARGET_FILES if (output_dir / name).exists()]
    if existing and not overwrite:
        raise FileExistsError(
            "Refusing to overwrite existing generated outputs without --force: " + ", ".join(existing)
        )
    for name, content in files.items():
        (output_dir / name).write_text(content, encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Validate one Assurance Case and render a Decision Receipt, Assurance Passport, "
            "and Executive Summary with Markdown/HTML injection defenses."
        )
    )
    parser.add_argument("case", type=Path, help="Path to assurance-case.json")
    parser.add_argument("--output-dir", type=Path, help="Destination directory (default: <case>/generated)")
    parser.add_argument(
        "--as-of",
        type=date.fromisoformat,
        default=date.today(),
        help="Date used to label review currency (YYYY-MM-DD; default: today)",
    )
    parser.add_argument("--force", action="store_true", help="Permit overwriting existing generated views")
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
    try:
        render_all(data, output_dir, as_of=args.as_of, overwrite=args.force)
    except (ValueError, FileExistsError, OSError) as exc:
        print(f"FAIL - assurance outputs: {exc}")
        return 1
    print(f"PASS - rendered assurance outputs to {output_dir}")
    print(f"  currency_as_of_{args.as_of.isoformat()}: {validator.currency_status(data, args.as_of)}")
    print("  boundary: generated views communicate the canonical case; human authority remains final")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
