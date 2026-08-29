# Software and AI Supply Chain Readiness
> **Artifact type:** TEMPLATE  
> **Completion status:** Blank for reuse  
> **Required for:** Conditional: third-party code, models, data, or services

## What this document is

A public-safe review record for software dependencies, build provenance, external services, AI models, retrieval sources, and release integrity.

## Who should complete it

Product owners, security reviewers, software maintainers, AI-system owners, and release managers.

## When to use it

Use before a release, supplier decision, major dependency change, model/provider change, or high-impact deployment.

## Decision supported

Whether the reviewed software or AI supply chain has enough evidence to proceed, proceed with conditions, stop, or require more evidence.

## System / Product

## Version or Release

## Owner

## Review Date

## 1. Dependency Inventory

| Dependency ID | Name | Version | Direct or Transitive | Source | Purpose | Owner | Support Status | Evidence ID |
|---|---|---|---|---|---|---|---|---|

Review:

- [ ] Direct dependencies are identified.
- [ ] Transitive dependencies are identified where feasible.
- [ ] Unsupported or unmaintained dependencies are flagged.
- [ ] High-impact dependencies have named owners.
- [ ] Dependency sources and expected integrity mechanisms are documented.

## 2. SBOM Status

| Question | Answer | Evidence ID | Gap / Action |
|---|---|---|---|
| Does an SBOM exist? | | | |
| What format is used? | | | |
| How is it generated? | | | |
| Is generation repeatable? | | | |
| Is it updated for each release? | | | |
| Is it retained with release evidence? | | | |

## 3. Source and Build Provenance

| Control Area | Expected State | Observed State | Evidence ID | Decision |
|---|---|---|---|---|
| Authoritative source repository | | | | |
| Maintainer access | | | | |
| Build environment | | | | |
| Dependency resolution | | | | |
| Review and approval | | | | |
| Artifact signing or attestation | | | | |
| Release archive | | | | |
| Rollback artifact | | | | |

## 4. AI and Model Supply Chain

| Item | Provider / Source | Version | Data or Tool Access | Change Detection | Exit / Replacement Path | Evidence ID |
|---|---|---|---|---|---|---|
| Model | | | | | | |
| Embedding model | | | | | | |
| Retrieval source | | | | | | |
| Dataset | | | | | | |
| Plugin / tool | | | | | | |
| External API | | | | | | |
| Hosted platform | | | | | | |

Review:

- [ ] Model and provider changes are detectable.
- [ ] Retrieval and dataset provenance is documented where applicable.
- [ ] Tool and plugin permissions are bounded.
- [ ] External API dependencies have fallback or exit considerations.
- [ ] Untrusted third-party content is treated as data, not authority.
- [ ] Human approval remains required for consequential release decisions.

## 5. Vulnerability and Change Handling

| Event | Detection Source | Owner | Required Action | Time Expectation | Evidence ID |
|---|---|---|---|---|---|
| Critical dependency vulnerability | | | | | |
| Malicious package or source compromise | | | | | |
| Model/provider change | | | | | |
| Build-system compromise | | | | | |
| Signing-key concern | | | | | |
| Unsupported dependency | | | | | |

## 6. Release Integrity

- [ ] Release-controlled files are enumerated.
- [ ] Release hashes are generated after content freeze.
- [ ] The manifest can be verified from a clean checkout.
- [ ] Release notes distinguish implemented, tested, and unproven claims.
- [ ] Rollback artifacts and ownership are documented.
- [ ] No private keys, credentials, or sensitive operational details are included.

## 7. Findings and Corrective Actions

| Finding ID | Finding | Severity | Evidence ID | Owner | Due Date | Retest Required? | Status |
|---|---|---|---|---|---|---:|---|

## 8. Decision

- [ ] Green — sufficient evidence for the current stage
- [ ] Amber — proceed only with documented conditions
- [ ] Red — do not proceed
- [ ] More evidence required

Decision owner:

Reviewer:

Conditions:

Residual risk:

Next review date:

## Limitations

Completion of this template does not certify a product, prove that a dependency is trustworthy, authorize deployment, or replace system-specific engineering, legal, contractual, or compliance review.

## Navigation

- Evidence source: [Evidence Manifest](../02-evidence-manifests/evidence-manifest-template.md)
- Related specialist path: [Cryptographic Change Assurance](../12-cryptographic-change-assurance/README.md)
- Decision semantics: [Decision Rubric](../DECISION_RUBRIC.md)
- Back to toolkit: [START_HERE.md](../START_HERE.md)
