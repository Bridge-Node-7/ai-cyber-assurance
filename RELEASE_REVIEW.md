# Release Review: AI Cyber Assurance v0.2.2

> **Artifact type:** RELEASE ASSURANCE RECORD
> **Decision status:** GREEN, conditionally approved for public release
> **Public release authority:** Granted only after exact PR-head review, merged-main validation, hosted-asset verification, human and AI walkthroughs, and logged-out public review

## Scope

This review covers one focused UX and validator-maintenance release.

The release:

- Adds a safe and obvious starting point
- Adds a review-package status authority
- Consolidates AI-assistance rules and human authority boundaries
- Makes `VERSION` the validator's release-version authority
- Adds a small standard-library regression suite
- Adds Ubuntu and Windows hosted validation
- Preserves all existing specialist records, synthetic examples, public-safety boundaries, and assurance limitations

It does not evaluate a production deployment, real-system control effectiveness, certification, legal sufficiency, compliance, or independent validation.

## User experience intent

A first-time human or AI assistant should be able to identify:

1. What the repository does
2. When it applies
3. Where real evidence belongs
4. Which review path to use
5. Which records apply
6. What AI may and may not do
7. What evidence classes mean
8. Which decision is controlling
9. What validation checks
10. What validation does not prove

## Validation evidence required

| Check | Required result |
|---|---|
| Standard-library regression tests | Pass |
| Repository validator | Pass |
| Manifest parity | Pass |
| SHA-256 verification | Pass in local Git Bash and hosted validation |
| Python syntax | Pass |
| JSON syntax | Pass |
| Relative Markdown links | Pass through repository validator |
| Secret and personal-information scans | Pass through repository validator |
| Ubuntu GitHub Actions | Pass on PR head and merged main |
| Windows GitHub Actions | Pass on PR head and merged main |
| Fresh Windows-style clone | Pass |
| Private vulnerability reporting | Remains enabled |
| Human release approver | Required before publication |

## Internal usability walkthroughs

### Human walkthrough

One uninvolved reviewer must be able to:

- Explain the repository's purpose and limitations
- Create a safe private package
- Select Quick Review or Full Assurance Lifecycle
- Complete the Review Package Index
- Identify the final assurance decision owner
- Explain what validation does not prove

Record assistance, blockers, and misunderstandings. Do not claim broad usability from one walkthrough.

### AI-assistant walkthrough

Using only the public candidate, one AI assistant must correctly identify:

- The correct first file
- The five evidence classes
- Allowed and prohibited activities
- Stop conditions
- Required output structure
- The distinction between module assessment, assurance recommendation, and final assurance decision
- The human authority boundary

The assistant must not claim autonomous authorization.

## Integrity scope

`MANIFEST.sha256` provides deterministic file-change detection but is not an independent attestation. Public-release integrity depends on the approved commit, annotated tag, GitHub release record, externally recorded archive checksum, hosted-asset verification, and human approval.

## Accepted limitations

- Quick Review is designed for self-guided use.
- Full Assurance Lifecycle remains expert-led.
- The validator checks the public toolkit, not the semantic truth or sufficiency of a completed private review.
- No autonomous approval, certification, compliance, or operational-effectiveness claim is introduced.

## Final decision

**GREEN, conditionally approved for v0.2.2 public release after all listed gates pass.**

Proceed through one reviewed pull request. Stop before merge, tag, release, deployment, or settings changes unless separately authorized. This decision does not claim independent validation, operational validation, production authorization, certification, compliance, or real-system effectiveness.
