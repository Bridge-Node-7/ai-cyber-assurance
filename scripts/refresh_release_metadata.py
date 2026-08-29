#!/usr/bin/env python3
"""Refresh or verify deterministic AI Cyber Assurance release metadata."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from validate_repo import check_hashes, generate_hashes, read_version, release_files


def load_manifest(root: Path) -> dict[str, object]:
    path = root / "REPO_MANIFEST.json"
    if not path.exists():
        raise ValueError("REPO_MANIFEST.json is missing.")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("REPO_MANIFEST.json must contain a JSON object.")
    return data


def expected_fields(root: Path) -> dict[str, object]:
    files = [rel.as_posix() for rel in release_files(root)]
    return {
        "version": f"v{read_version(root)}",
        "file_count": len(files),
        "files": files,
    }


def expected_hash_lines(root: Path) -> list[str]:
    lines: list[str] = []
    for rel in release_files(root):
        if rel.as_posix() == "MANIFEST.sha256":
            continue
        digest = hashlib.sha256((root / rel).read_bytes()).hexdigest()
        lines.append(f"{digest}  {rel.as_posix()}")
    return lines


def check_metadata(root: Path) -> list[str]:
    findings: list[str] = []
    try:
        manifest = load_manifest(root)
        expected = expected_fields(root)
    except (ValueError, json.JSONDecodeError, OSError) as exc:
        return [str(exc)]

    for key, value in expected.items():
        if manifest.get(key) != value:
            findings.append(f"REPO_MANIFEST.json field {key!r} is out of date.")

    hash_result = check_hashes(root, release_files(root))
    if not hash_result.passed:
        findings.extend(hash_result.details)

    return findings


def write_metadata(root: Path) -> None:
    manifest = load_manifest(root)
    manifest.update(expected_fields(root))
    (root / "REPO_MANIFEST.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    generate_hashes(root)


def main() -> int:
    parser = argparse.ArgumentParser(description="Refresh or verify deterministic release metadata and SHA-256 inventory.")
    parser.add_argument("--root", type=Path, default=Path("."))
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Verify metadata without modifying files")
    mode.add_argument("--write", action="store_true", help="Refresh manifest fields and SHA-256 inventory")
    args = parser.parse_args()

    root = args.root.resolve()

    if args.write:
        write_metadata(root)

    findings = check_metadata(root)
    if findings:
        print("FAIL - release metadata")
        for finding in findings:
            print(f"  - {finding}")
        print("EXPECTED-MANIFEST-SHA256-BEGIN")
        for line in expected_hash_lines(root):
            print(line)
        print("EXPECTED-MANIFEST-SHA256-END")
        return 1

    print("PASS - release metadata")
    return 0


if __name__ == "__main__":
    sys.exit(main())
