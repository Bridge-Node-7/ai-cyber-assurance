#!/usr/bin/env python3
"""Validate the AI Cyber Assurance release package.

Standard-library only. The validator checks structural inventory, byte
integrity, internal links, repository identity, portfolio separation,
artifact labels, required content, common secret and personal-information
patterns, public-safety language, and workflow safety.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    "dist",
    "build",
}
EXCLUDED_FILES = {"validation-report.json", "VALIDATION_REPORT.json"}
ALLOWED_SUFFIXES = {".md", ".json", ".yml", ".yaml", ".py", ".sha256"}
ALLOWED_EXTENSIONLESS = {"LICENSE", "VERSION", ".gitignore", ".gitattributes"}
VALIDATOR_EXEMPT_FILES = {"scripts/validate_repo.py"}

SECRET_PATTERNS = {
    "private key header": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "GitHub classic token": re.compile(r"\bghp_[A-Za-z0-9]{36}\b"),
    "GitHub fine-grained token": re.compile(r"\bgithub_pat_[A-Za-z0-9_]{50,}\b"),
    "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
}
PERSONAL_INFO_PATTERNS = {
    "email address": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "phone number": re.compile(
        r"(?<!\d)(?:\+?1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}(?!\d)"
    ),
    "IPv4 address": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
}
PLACEHOLDER_PATTERN = re.compile(r"\b(?:TODO|FIXME|TBD)\b", re.IGNORECASE)
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
REPOSITORY_SLUG_PATTERN = re.compile(r"\bai-cyber-[a-z0-9-]+\b")
ORG_REPOSITORY_URL_PATTERN = re.compile(
    r"https://github\.com/Bridge-Node-7/([A-Za-z0-9_.-]+)"
)
LEGACY_VERSION_PATTERN = re.compile(r"\bv0\.(?:0|1)\.\d+\b")
TRANSITION_LANGUAGE_PATTERN = re.compile(
    r"\b(?:renamed|former|previous|retired|legacy)\s+"
    r"(?:project|repository|identity|name)\b",
    re.IGNORECASE,
)


@dataclass
class CheckResult:
    name: str
    passed: bool
    details: list[str]


def release_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if any(part in EXCLUDED_DIRS for part in rel.parts):
            continue
        if rel.as_posix() in EXCLUDED_FILES:
            continue
        files.append(rel)
    return sorted(files, key=lambda item: item.as_posix())


def read_text(root: Path, rel: Path) -> str:
    return (root / rel).read_text(encoding="utf-8")


def read_version(root: Path) -> str:
    path = root / "VERSION"
    if not path.exists():
        raise ValueError("VERSION is missing.")
    version = path.read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][A-Za-z0-9.-]+)?", version):
        raise ValueError(f"VERSION has an invalid value: {version!r}")
    return version


def text_files(files: Iterable[Path]) -> list[Path]:
    return [
        rel
        for rel in files
        if rel.suffix.lower() in {".md", ".json", ".yml", ".yaml", ".py"}
    ]


def check_allowed_file_types(files: Iterable[Path]) -> CheckResult:
    bad: list[str] = []
    for rel in files:
        if rel.name in ALLOWED_EXTENSIONLESS:
            continue
        if rel.suffix.lower() not in ALLOWED_SUFFIXES:
            bad.append(rel.as_posix())
    return CheckResult(
        "allowed_file_types",
        not bad,
        bad or ["All release files use approved types."],
    )


def check_nonempty_files(root: Path, files: Iterable[Path]) -> CheckResult:
    empty = [rel.as_posix() for rel in files if (root / rel).stat().st_size == 0]
    return CheckResult(
        "nonempty_files",
        not empty,
        empty or ["No empty release files found."],
    )


def check_manifest(root: Path, files: list[Path]) -> CheckResult:
    path = root / "REPO_MANIFEST.json"
    details: list[str] = []
    if not path.exists():
        return CheckResult("manifest", False, ["REPO_MANIFEST.json is missing."])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        return CheckResult("manifest", False, [f"Manifest parse error: {exc}"])

    listed = data.get("files")
    if not isinstance(listed, list):
        return CheckResult("manifest", False, ["Manifest field 'files' must be a list."])

    actual = [rel.as_posix() for rel in files]
    listed_sorted = sorted(str(item) for item in listed)
    actual_sorted = sorted(actual)

    missing = sorted(set(actual_sorted) - set(listed_sorted))
    extra = sorted(set(listed_sorted) - set(actual_sorted))
    if missing:
        details.append("Missing from manifest: " + ", ".join(missing))
    if extra:
        details.append("Listed but absent: " + ", ".join(extra))
    if data.get("file_count") != len(actual_sorted):
        details.append(f"file_count={data.get('file_count')!r}, actual={len(actual_sorted)}")
    if data.get("repository") != "ai-cyber-assurance":
        details.append("Manifest repository field is not 'ai-cyber-assurance'.")
    expected_url = "https://github.com/Bridge-Node-7/ai-cyber-assurance"
    if data.get("target_url") != expected_url:
        details.append("Manifest target_url is not the canonical repository URL.")
    try:
        expected_version = f"v{read_version(root)}"
    except ValueError as exc:
        details.append(str(exc))
    else:
        if data.get("version") != expected_version:
            details.append(
                f"Manifest version is {data.get('version')!r}; expected {expected_version!r} from VERSION."
            )

    return CheckResult(
        "manifest",
        not details,
        details or ["Manifest matches the release tree."],
    )


def parse_hash_manifest(path: Path) -> tuple[dict[str, str], list[str]]:
    hashes: dict[str, str] = {}
    errors: list[str] = []
    if not path.exists():
        return hashes, ["MANIFEST.sha256 is missing."]
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if not match:
            errors.append(f"Invalid hash line {number}: {raw!r}")
            continue
        digest, rel = match.groups()
        if rel in hashes:
            errors.append(f"Duplicate hash path: {rel}")
        hashes[rel] = digest
    return hashes, errors


def check_hashes(root: Path, files: list[Path]) -> CheckResult:
    expected_files = sorted(
        rel.as_posix() for rel in files if rel.as_posix() != "MANIFEST.sha256"
    )
    hashes, details = parse_hash_manifest(root / "MANIFEST.sha256")
    actual_paths = sorted(hashes)

    missing = sorted(set(expected_files) - set(actual_paths))
    extra = sorted(set(actual_paths) - set(expected_files))
    if missing:
        details.append("Missing hashes: " + ", ".join(missing))
    if extra:
        details.append("Unexpected hashes: " + ", ".join(extra))

    for rel in sorted(set(expected_files) & set(actual_paths)):
        digest = hashlib.sha256((root / rel).read_bytes()).hexdigest()
        if digest != hashes[rel]:
            details.append(f"Hash mismatch: {rel}")

    if "MANIFEST.sha256" in hashes:
        details.append("MANIFEST.sha256 must exclude itself.")

    return CheckResult(
        "hashes",
        not details,
        details or ["All release hashes validate."],
    )


def check_markdown_links(root: Path, files: list[Path]) -> CheckResult:
    broken: list[str] = []
    for rel in files:
        if rel.suffix.lower() != ".md":
            continue
        text = read_text(root, rel)
        for target in MARKDOWN_LINK_PATTERN.findall(text):
            target = target.strip().split()[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target_path = target.split("#", 1)[0]
            if not target_path:
                continue
            resolved = (root / rel.parent / target_path).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                broken.append(f"{rel.as_posix()}: link escapes repository: {target}")
                continue
            if not resolved.exists():
                broken.append(f"{rel.as_posix()}: missing target {target}")
    return CheckResult(
        "markdown_links",
        not broken,
        broken or ["All relative Markdown links resolve."],
    )


def check_identity(root: Path, files: list[Path]) -> CheckResult:
    findings: list[str] = []
    readme = (root / "README.md").read_text(encoding="utf-8")
    if not readme.startswith("# AI Cyber Assurance\n"):
        findings.append("README title is not '# AI Cyber Assurance'.")

    for rel in text_files(files):
        if rel.as_posix() in VALIDATOR_EXEMPT_FILES:
            continue
        text = read_text(root, rel)
        for match in REPOSITORY_SLUG_PATTERN.findall(text):
            if match != "ai-cyber-assurance" and not match.startswith("ai-cyber-assurance-"):
                findings.append(f"Unexpected repository identity {match!r} in {rel.as_posix()}")
        if re.search(r"\bAI Cyber [A-Za-z ]+ OS\b", text):
            findings.append(f"Unexpected OS-style project identity in {rel.as_posix()}")

    return CheckResult(
        "current_identity",
        not findings,
        findings or ["Current repository identity is consistent."],
    )


def check_portfolio_separation(root: Path, files: list[Path]) -> CheckResult:
    findings: list[str] = []
    for rel in text_files(files):
        text = read_text(root, rel)
        for repository in ORG_REPOSITORY_URL_PATTERN.findall(text):
            if repository != "ai-cyber-assurance":
                findings.append(
                    f"{rel.as_posix()}: references another Bridge Node 7 repository: {repository}"
                )
    return CheckResult(
        "portfolio_separation",
        not findings,
        findings or ["No links to unrelated organization repositories found."],
    )


def check_content_minimization(root: Path, files: list[Path]) -> CheckResult:
    findings: list[str] = []
    for rel in text_files(files):
        if rel.as_posix() in VALIDATOR_EXEMPT_FILES:
            continue
        text = read_text(root, rel)
        if LEGACY_VERSION_PATTERN.search(text):
            findings.append(f"{rel.as_posix()}: older pre-baseline version reference")
        if TRANSITION_LANGUAGE_PATTERN.search(text):
            findings.append(f"{rel.as_posix()}: repository-transition language")
    return CheckResult(
        "content_minimization",
        not findings,
        findings or ["No retired-version or repository-transition content found."],
    )


def check_artifact_labels(root: Path) -> CheckResult:
    template_files = [
        "01-ai-agent-security/ai-agent-security-checklist.md",
        "01-ai-agent-security/human-approval-gates.md",
        "02-evidence-manifests/evidence-manifest-template.md",
        "02-evidence-manifests/review-package-index-template.md",
        "02-evidence-manifests/review-decision-template.md",
        "03-zero-trust/zero-trust-readiness-map.md",
        "04-llm-risk/llm-risk-register.md",
        "05-secure-by-design/secure-by-design-product-review.md",
        "06-software-supply-chain/sbom-readiness.md",
        "07-cyber-survivability/cyber-survivability-review.md",
        "08-high-impact-systems/high-impact-system-readiness.md",
        "09-incident-review/incident-review-template.md",
        "11-assurance-lifecycle/security-policy-and-target-template.md",
        "11-assurance-lifecycle/identity-and-authority-register.md",
        "11-assurance-lifecycle/threat-control-evidence-map.md",
        "11-assurance-lifecycle/control-validation-record.md",
        "11-assurance-lifecycle/recovery-assurance-record.md",
    ]
    example_files = [
        "10-examples/example-ai-workflow-cyber-review.md",
        "10-examples/synthetic-supplier-assurance/README.md",
        "10-examples/synthetic-supplier-assurance/completed-evidence-manifest.md",
        "10-examples/synthetic-supplier-assurance/completed-review-decision.md",
        "10-examples/synthetic-supplier-assurance/completed-threat-control-evidence-map.md",
    ]
    findings: list[str] = []

    for rel in template_files:
        path = root / rel
        if not path.exists():
            findings.append(f"{rel}: missing template file")
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in ("Artifact type:** TEMPLATE", "Completion status:** Blank for reuse", "Required for:"):
            if phrase.lower() not in text.lower():
                findings.append(f"{rel}: missing artifact-label phrase {phrase!r}")

    navigator = (root / "ASSURANCE_LIFECYCLE.md").read_text(encoding="utf-8")
    if "Artifact type:** NAVIGATOR".lower() not in navigator.lower():
        findings.append("ASSURANCE_LIFECYCLE.md: missing NAVIGATOR label")

    for rel in example_files:
        text = (root / rel).read_text(encoding="utf-8").lower()
        for phrase in (
            "artifact type:** completed synthetic example",
            "operational authority:** none",
            "synthetic",
            "fictional",
        ):
            if phrase not in text:
                findings.append(f"{rel}: missing example-label phrase {phrase!r}")

    for rel in example_files[1:]:
        text = (root / rel).read_text(encoding="utf-8").lower()
        if "partial assurance profile" not in text:
            findings.append(f"{rel}: supplier example must be labeled partial")

    return CheckResult(
        "artifact_labels",
        not findings,
        findings or ["Templates, navigator, and examples are clearly labeled."],
    )


def check_required_content(root: Path) -> CheckResult:
    required: dict[str, list[str]] = {
        "README.md": [
            "Five-minute orientation",
            "Quick Review",
            "Full Assurance Lifecycle",
            "Which artifacts apply?",
            "Expected effort",
            "What this does not do",
        ],
        "ASSURANCE_LIFECYCLE.md": [
            "This file is the navigator",
            "Human authority",
            "Retest",
        ],
        "01-ai-agent-security/human-approval-gates.md": [
            "Prohibited self-approval",
            "Approval scope and expiration",
            "Post-action validation",
        ],
        "02-evidence-manifests/evidence-manifest-template.md": [
            "Evidence ID",
            "Integrity method",
            "Supersedes",
        ],
        "08-high-impact-systems/high-impact-system-readiness.md": [
            "Lifecycle Record Map",
            "Recovery Assurance Record",
            "Unproven claims",
        ],
        "11-assurance-lifecycle/security-policy-and-target-template.md": [
            "Security policy",
            "Security target",
            "Decision owner",
        ],
        "11-assurance-lifecycle/identity-and-authority-register.md": [
            "Revocation Path",
            "Last Observed Use",
            "Evidence ID",
        ],
        "11-assurance-lifecycle/threat-control-evidence-map.md": [
            "Preventive Control",
            "Detective Control",
            "Recovery Control",
        ],
        "11-assurance-lifecycle/control-validation-record.md": [
            "Documented",
            "Observed operating",
            "Retest",
        ],
        "11-assurance-lifecycle/recovery-assurance-record.md": [
            "Expected Result",
            "Observed Result",
            "Next test date",
        ],
        "RELEASE_REVIEW.md": [
            "Repository validation",
            "GitHub Actions",
            "Security reports",
            "Limitations",
        ],
    }
    findings: list[str] = []
    for rel, phrases in required.items():
        path = root / rel
        if not path.exists():
            findings.append(f"Missing required file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase.lower() not in text.lower():
                findings.append(f"{rel}: missing required phrase {phrase!r}")
    return CheckResult(
        "required_content",
        not findings,
        findings or ["Required assurance and release content is present."],
    )



def check_onboarding_and_agent_guidance(root: Path) -> CheckResult:
    requirements: dict[str, list[str]] = {
        "README.md": [
            "(START_HERE.md)",
            "(AGENTS.md)",
            "private or access-controlled working package",
            "final assurance decision",
        ],
        "START_HERE.md": [
            "(AGENTS.md)",
            "review-package-index-template.md",
            "evidence-manifest-template.md",
            "(ASSURANCE_LIFECYCLE.md)",
            "(DECISION_RUBRIC.md)",
            "review-decision-template.md",
            "public repository",
            "Quick Review",
            "Full Assurance Lifecycle",
            "Module assessment",
            "Assurance recommendation",
            "Final assurance decision",
            "does not prove",
        ],
        "AGENTS.md": [
            "## Scope",
            "## Human Authority",
            "## Evidence Classes",
            "## Agent May",
            "## Agent Must",
            "## Agent Must Not",
            "## Required Output",
            "## Stop Conditions",
            "## Validation Boundary",
        ],
        "02-evidence-manifests/review-package-index-template.md": [
            "Artifact type:** TEMPLATE",
            "Completion status:** Blank for reuse",
            "Required",
            "Conditional",
            "Not Applicable",
            "Not Started",
            "Draft",
            "Blocked",
            "Ready for Review",
            "Complete",
            "Module assessment",
            "Assurance recommendation",
            "Final assurance decision",
            "Package Completion Rule",
        ],
    }
    findings: list[str] = []
    for rel, phrases in requirements.items():
        path = root / rel
        if not path.exists():
            findings.append(f"Missing UX guidance file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        lower = text.lower()
        for phrase in phrases:
            if phrase.lower() not in lower:
                findings.append(f"{rel}: missing UX guidance phrase {phrase!r}")
    return CheckResult(
        "onboarding_and_agent_guidance",
        not findings,
        findings or ["Onboarding, package control, and AI-assistance guidance are present."],
    )


def check_secrets_and_placeholders(root: Path, files: list[Path]) -> CheckResult:
    findings: list[str] = []
    for rel in text_files(files):
        text = read_text(root, rel)
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                findings.append(f"{rel.as_posix()}: possible {label}")
        if rel.as_posix() not in VALIDATOR_EXEMPT_FILES and PLACEHOLDER_PATTERN.search(text):
            findings.append(f"{rel.as_posix()}: unresolved placeholder marker")
    return CheckResult(
        "secrets_and_placeholders",
        not findings,
        findings or ["No common secret patterns or unresolved markers found."],
    )


def check_personal_information(root: Path, files: list[Path]) -> CheckResult:
    findings: list[str] = []
    for rel in text_files(files):
        if rel.as_posix() in VALIDATOR_EXEMPT_FILES:
            continue
        text = read_text(root, rel)
        for label, pattern in PERSONAL_INFO_PATTERNS.items():
            if pattern.search(text):
                findings.append(f"{rel.as_posix()}: possible {label}")
    return CheckResult(
        "personal_information",
        not findings,
        findings or ["No configured personal-information patterns found."],
    )



def check_example_traceability(root: Path) -> CheckResult:
    example_root = root / "10-examples/synthetic-supplier-assurance"
    manifest_text = (example_root / "completed-evidence-manifest.md").read_text(encoding="utf-8")
    map_text = (example_root / "completed-threat-control-evidence-map.md").read_text(encoding="utf-8")
    decision_text = (example_root / "completed-review-decision.md").read_text(encoding="utf-8")
    findings: list[str] = []

    requirement_ids = {f"SYN-R-{number:03d}" for number in range(1, 6)}
    control_ids = {f"SYN-C-{number:03d}" for number in range(1, 6)}
    evidence_ids = {f"SYN-E-{number:03d}" for number in range(1, 6)}

    for identifier in sorted(requirement_ids | control_ids):
        if identifier not in manifest_text:
            findings.append(f"Evidence manifest missing {identifier}")
        if identifier not in map_text:
            findings.append(f"Threat-control-evidence map missing {identifier}")

    for identifier in sorted(evidence_ids):
        if identifier not in manifest_text:
            findings.append(f"Evidence manifest missing {identifier}")
        if identifier not in map_text:
            findings.append(f"Threat-control-evidence map missing {identifier}")
        if identifier not in decision_text:
            findings.append(f"Review decision missing {identifier}")

    for identifier in ("SYN-R-005", "SYN-C-005"):
        if identifier not in decision_text:
            findings.append(f"Review decision does not identify unresolved {identifier}")

    return CheckResult(
        "example_traceability",
        not findings,
        findings or ["Synthetic supplier identifiers trace across manifest, map, and decision."],
    )


def check_public_safety_language(root: Path) -> CheckResult:
    required = {
        "README.md": ["does not", "offensive", "certify"],
        "SECURITY.md": ["malware code", "private", "defensive"],
        "CONTRIBUTING.md": [
            "weaponization instructions",
            "high-level defensive analysis",
            "private keys",
        ],
        "DECISION_RUBRIC.md": [
            "exploit-enabling operational detail",
            "public release",
            "residual risk",
        ],
    }
    findings: list[str] = []
    for rel, phrases in required.items():
        path = root / rel
        if not path.exists():
            findings.append(f"Missing public-safety file: {rel}")
            continue
        lower = path.read_text(encoding="utf-8").lower()
        for phrase in phrases:
            if phrase.lower() not in lower:
                findings.append(f"{rel}: missing public-safety phrase {phrase!r}")
    return CheckResult(
        "public_safety_language",
        not findings,
        findings or ["Required public-safety language is present."],
    )


def check_workflow_safety(root: Path) -> CheckResult:
    path = root / ".github/workflows/validate.yml"
    if not path.exists():
        return CheckResult("workflow_safety", False, ["Validation workflow is missing."])
    text = path.read_text(encoding="utf-8")
    findings: list[str] = []
    if "contents: read" not in text:
        findings.append("Workflow must declare read-only contents permission.")
    if "python scripts/validate_repo.py" not in text or "--root ." not in text:
        findings.append("Workflow does not run the repository validator.")
    if "pull_request:" not in text or "push:" not in text:
        findings.append("Workflow must run on pull requests and pushes.")
    if "python -m unittest discover" not in text:
        findings.append("Workflow must run the standard-library regression suite.")
    if "ubuntu-latest" not in text or "windows-latest" not in text:
        findings.append("Workflow must validate on Ubuntu and Windows.")
    if "sha256sum -c MANIFEST.sha256" not in text:
        findings.append("Workflow must run direct GNU checksum verification.")
    return CheckResult(
        "workflow_safety",
        not findings,
        findings or ["Validation workflow uses the expected read-only baseline."],
    )


def run_checks(root: Path) -> list[CheckResult]:
    files = release_files(root)
    return [
        check_allowed_file_types(files),
        check_nonempty_files(root, files),
        check_manifest(root, files),
        check_hashes(root, files),
        check_markdown_links(root, files),
        check_identity(root, files),
        check_portfolio_separation(root, files),
        check_content_minimization(root, files),
        check_artifact_labels(root),
        check_required_content(root),
        check_onboarding_and_agent_guidance(root),
        check_secrets_and_placeholders(root, files),
        check_personal_information(root, files),
        check_example_traceability(root),
        check_public_safety_language(root),
        check_workflow_safety(root),
    ]


def generate_hashes(root: Path) -> None:
    files = release_files(root)
    lines: list[str] = []
    for rel in files:
        if rel.as_posix() == "MANIFEST.sha256":
            continue
        digest = hashlib.sha256((root / rel).read_bytes()).hexdigest()
        lines.append(f"{digest}  {rel.as_posix()}")
    (root / "MANIFEST.sha256").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
        newline="\n",
    )



def build_report(root: Path, results: list[CheckResult]) -> dict[str, object]:
    passed = all(result.passed for result in results)
    return {
        "repository": "ai-cyber-assurance",
        "version": f"v{read_version(root)}",
        "status": "PASS" if passed else "FAIL",
        "checks": [asdict(result) for result in results],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--generate-hashes", action="store_true")
    parser.add_argument("--json-output", type=Path)
    args = parser.parse_args()

    root = args.root.resolve()
    if args.generate_hashes:
        generate_hashes(root)

    results = run_checks(root)
    passed = all(result.passed for result in results)
    report = build_report(root, results)

    for result in results:
        mark = "PASS" if result.passed else "FAIL"
        print(f"[{mark}] {result.name}")
        for detail in result.details:
            print(f"  - {detail}")

    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(
            json.dumps(report, indent=2) + "\n",
            encoding="utf-8",
        )

    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
