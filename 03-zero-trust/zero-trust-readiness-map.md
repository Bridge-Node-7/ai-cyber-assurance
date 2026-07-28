# Zero Trust Readiness Map
> **Artifact type:** TEMPLATE  
> **Completion status:** Blank for reuse  
> **Required for:** Conditional: identity, access, or trust-boundary review

## Purpose

Review whether access to an AI-enabled, mission-critical, or emerging-technology system is explicitly verified, least-privileged, observable, and continuously reassessed instead of assumed trustworthy.

## Use with

- [Evidence Manifest](../02-evidence-manifests/evidence-manifest-template.md)
- [Identity and Authority Register](../11-assurance-lifecycle/identity-and-authority-register.md)
- [Human Approval Gates](../01-ai-agent-security/human-approval-gates.md)

## Review identity

- **System:**
- **Owner:**
- **Reviewer:**
- **Date:**
- **Scope:**

## Core question

Does every request for access or action have a known identity, authorized purpose, bounded scope, relevant context, evidence, and revocation path?

## Identity

- [ ] Every human has a unique identity.
- [ ] Every service, workload, supplier integration, and AI agent has a unique identity where applicable.
- [ ] Identity proofing and authoritative sources are documented.
- [ ] Privileged access is separated from routine access.
- [ ] MFA or phishing-resistant authentication is used where appropriate.
- [ ] Access is reviewed on a defined schedule.
- [ ] Joiner, mover, leaver, expiration, and revocation processes are documented.
- [ ] Break-glass access is time-limited, monitored, and reviewed.

## Device and workload

- [ ] Devices and workloads are inventoried and owned.
- [ ] Unknown or noncompliant devices are blocked or constrained.
- [ ] Workload permissions and service identities are documented.
- [ ] Configuration, software, and integrity state influence access decisions where relevant.
- [ ] Unsupported systems are tracked as risk.

## Network and environment

- [ ] Access paths and trust boundaries are documented.
- [ ] Sensitive services are not broadly reachable.
- [ ] Segmentation limits lateral movement and blast radius.
- [ ] Remote and third-party access is monitored.
- [ ] High-risk paths are approval-gated.
- [ ] External connections have owners, purpose, evidence, and termination paths.

## Application, API, and tool access

- [ ] Applications, APIs, and tools authenticate the calling identity.
- [ ] Permissions are scoped to purpose and resource.
- [ ] Destructive or consequential actions require approval.
- [ ] AI agents cannot call arbitrary or unapproved tools.
- [ ] Tool outputs and external results are treated as untrusted until validated.
- [ ] Tokens and sessions have appropriate audience, scope, lifetime, and revocation.

## Data

- [ ] Sensitive data is identified and owned.
- [ ] Data access is authorized, logged, and reviewable.
- [ ] Data sharing and export are controlled.
- [ ] AI systems are restricted from unnecessary data.
- [ ] Retention, deletion, correction, and release expectations are documented.
- [ ] Data provenance and integrity are evaluated where decisions depend on content.

## Visibility and policy enforcement

- [ ] Security and access logs exist.
- [ ] Time, identity, action, resource, result, and policy decision are traceable.
- [ ] Logs are reviewed and protected from unauthorized alteration.
- [ ] Anomalies and policy violations have escalation thresholds.
- [ ] Automated actions are attributable and explainable enough for review.
- [ ] Operators can understand current state and safely terminate access.

## Automation governance

- [ ] Automated actions are bounded by policy.
- [ ] Human approval gates exist for high-impact actions.
- [ ] The system prevents self-approval by the requesting agent or operator.
- [ ] A disable, revoke, or containment path exists and is tested.
- [ ] Model, tool, policy, and identity changes are reviewed.
- [ ] Decisions can fail closed when identity, policy, or evidence is unknown.

## Readiness score

Use the 0–5 anchors in [DECISION_RUBRIC.md](../DECISION_RUBRIC.md).

| Domain | Score 0–5 | Evidence ID | Gap | Owner |
|---|---:|---|---|---|
| Identity | | | | |
| Device / workload | | | | |
| Network / environment | | | | |
| Application / API / tools | | | | |
| Data | | | | |
| Visibility / policy enforcement | | | | |
| Automation governance | | | | |

## Overall status

- [ ] Green
- [ ] Amber
- [ ] Red
- [ ] More evidence required

Reviewer:

Date:

Conditions:

Next review:

Notes:
