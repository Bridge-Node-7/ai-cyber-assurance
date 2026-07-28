# Secure-by-Design Product Review
> **Artifact type:** TEMPLATE  
> **Completion status:** Blank for reuse  
> **Required for:** Conditional: product design or release review

## Purpose

Review whether a product or system makes safe and secure operation the default, keeps limitations visible, supports vulnerability handling, and preserves human authority over consequential actions.

## Use with

- [Evidence Manifest](../02-evidence-manifests/evidence-manifest-template.md)
- [Security Policy and Target](../11-assurance-lifecycle/security-policy-and-target-template.md)
- [Control Validation Record](../11-assurance-lifecycle/control-validation-record.md)
- [Supply Chain Review](../06-software-supply-chain/sbom-readiness.md)

## Product identity

- **Product / system:**
- **Version / configuration:**
- **Review date:**
- **Security owner:**
- **Release owner:**
- **Intended users and outcome:**

## Default security posture

| Check | Status | Evidence ID | Gap / condition | Owner |
|---|---|---|---|---|
| Secure defaults are enabled | | | | |
| Weak or dangerous settings are not the default | | | | |
| Logging needed for review is enabled | | | | |
| Sensitive and privileged features require explicit authorization | | | | |
| Administrative functions are protected and separated | | | | |
| Unnecessary services, tools, and access are disabled | | | | |
| Default credentials and shared privileged identities are not used | | | | |
| Access is least privilege and time-bounded where feasible | | | | |
| Safe failure, rollback, and recovery are supported | | | | |

## Transparency and responsibility

- [ ] Intended use and prohibited use are documented.
- [ ] Known limitations, assumptions, and unresolved risks are visible.
- [ ] Security and data responsibilities are allocated between producer, operator, supplier, and user.
- [ ] Dependencies, models, providers, tools, and external services are listed.
- [ ] AI limitations, evidence expectations, and human authority are disclosed.
- [ ] Risk acceptance decisions identify the authorized owner and expiration.
- [ ] Public claims do not exceed the available evidence.

## Vulnerability handling

- [ ] A private vulnerability-reporting path exists and is verified.
- [ ] Triage, severity, ownership, and response-time expectations are documented.
- [ ] Patch, mitigation, rollback, and communication paths exist.
- [ ] Release notes include relevant security changes and limitations.
- [ ] Vulnerability fixes are prioritized by risk and mission impact.
- [ ] Corrective action and retest evidence are retained.

## AI-specific secure design

- [ ] Agent identity and permissions are bounded.
- [ ] Prompt injection, data poisoning, disclosure, excessive agency, and output handling are addressed.
- [ ] Tools and APIs are allowlisted and policy-controlled.
- [ ] Sensitive data exposure is minimized and monitored.
- [ ] Human approval gates exist for consequential actions.
- [ ] Models, prompts, retrieval sources, policies, and tools are change-controlled.
- [ ] Outputs are validated before high-impact use.
- [ ] Disable, revoke, rollback, and manual fallback paths are tested.

## Validation summary

| Control / requirement | Expected result | Observed result | Evidence ID | Status | Corrective action |
|---|---|---|---|---|---|

## Release decision

- [ ] Ready for stated scope and stage
- [ ] Ready with conditions
- [ ] Not ready
- [ ] More evidence required

Reviewer:

Decision maker:

Date:

Conditions:

Next review:

Notes:
