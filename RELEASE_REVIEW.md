# Release Review: AI Cyber Assurance v0.2.1

> **Artifact type:** RELEASE ASSURANCE RECORD
> **Decision status:** GREEN, conditionally approved for public release
> **Public release authority:** Granted only after PR-head validation, merged-main validation, release-asset checksum verification, and logged-out review

## Scope

This maintenance review covers checksum-manifest portability only. The v0.2.0 assurance content, user paths, synthetic examples, public-safety boundaries, and limitations remain unchanged.

It does not evaluate a production deployment, real-system control effectiveness, certification, legal sufficiency, compliance, or independent validation.

## Defect and correction

A Windows Git Bash fresh clone showed two portability hazards: `MANIFEST.sha256` could retain CRLF line endings, and `core.autocrlf=true` could change the checked-out bytes of other hashed text files. Either condition prevents portable byte-for-byte checksum verification even when the source content is logically unchanged.

The v0.2.1 candidate:

- enforces LF checkout for checksum files and every hashed text format;
- writes generated checksum manifests with explicit LF newlines;
- adds direct GNU `sha256sum -c` verification to GitHub Actions;
- updates version and release-control records without changing product content.

## Validation evidence required

| Check | Required result |
|---|---|
| Repository validator | Pass |
| Manifest parity | Pass |
| SHA-256 verification | Pass in Git Bash and GitHub Actions |
| Python syntax | Pass |
| JSON syntax | Pass |
| Relative Markdown links | Pass through repository validator |
| Secret and personal-information scans | Pass through repository validator |
| Fresh Windows-style clone | Pass with LF checksum manifest |
| GitHub Actions | Pass on PR head and merged main |
| Private vulnerability reporting | Remains enabled |
| Human release approver | Required before publication |

## Internal usability walkthroughs

The maintenance patch does not change navigation, templates, examples, or user-facing assurance content. The completed v0.2.0 walkthrough evidence remains applicable to the unchanged experience.

## Integrity scope

`MANIFEST.sha256` provides deterministic file-change detection but is not an independent attestation. Public-release integrity depends on the approved commit, tag, GitHub release record, externally recorded archive checksum, and human approval.

## Final decision

**GREEN, conditionally approved for v0.2.1 public release after all listed gates pass.**

Proceed through one reviewed pull request. Stop before merge, tag, release, deployment, or settings changes unless separately authorized. This decision does not claim independent validation, operational validation, production authorization, certification, compliance, or real-system effectiveness.
