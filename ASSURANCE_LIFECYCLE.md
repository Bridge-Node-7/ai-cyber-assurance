# Assurance Lifecycle

> **Artifact type:** NAVIGATOR  
> **Completion status:** Reference document  
> **Required for:** Full Assurance Lifecycle

## Purpose

This file is the navigator for a full AI Cyber Assurance review. It explains the lifecycle and routes each step to the record that captures the work. It is not a duplicate template.

Use the full lifecycle when a system is high-impact, operational, multi-party, dependent on external services, able to change external state, or expected to support consequential decisions.

Begin with [Start Here](START_HERE.md) and create the [Review Package Index](02-evidence-manifests/review-package-index-template.md). For a focused review, use the Quick Review path. AI assistants should also follow [AGENTS.md](AGENTS.md).

## Lifecycle

```text
Mission
→ Boundary
→ Assets and Dependencies
→ Identities and Authority
→ Threats and Failure Modes
→ Risk
→ Security Requirements
→ Controls
→ Evidence
→ Validation
→ Human Decision
→ Monitoring and Incident Response
→ Recovery
→ Corrective Action
→ Retest
→ Assurance
```

## Step-by-step routing

| Step | Core question | Primary record | Supporting modules | Exit condition |
|---|---|---|---|---|
| Mission | What outcome matters, to whom, and why? | [Evidence Manifest](02-evidence-manifests/evidence-manifest-template.md) | [High-Impact Readiness](08-high-impact-systems/high-impact-system-readiness.md) | Mission, owner, users, and consequences are stated |
| Boundary | What people, systems, data, tools, facilities, suppliers, and dependencies are in scope? | [Evidence Manifest](02-evidence-manifests/evidence-manifest-template.md) | [High-Impact Readiness](08-high-impact-systems/high-impact-system-readiness.md) | In-scope, out-of-scope, interfaces, assumptions, and dependencies are recorded |
| Assets and dependencies | What must remain confidential, accurate, available, authentic, and recoverable? | [Evidence Manifest](02-evidence-manifests/evidence-manifest-template.md) | [Supply Chain Review](06-software-supply-chain/sbom-readiness.md) | Critical assets and external dependencies have owners |
| Identities and authority | Who or what may act, on which resources, for what purpose, and for how long? | [Identity and Authority Register](11-assurance-lifecycle/identity-and-authority-register.md) | [Agent Security](01-ai-agent-security/ai-agent-security-checklist.md), [Zero Trust](03-zero-trust/zero-trust-readiness-map.md) | Human, service, workload, supplier, and agent identities have bounded authority and revocation paths |
| Threats and failure modes | What malicious, accidental, environmental, supplier, and automation failures could matter? | [Threat-Control-Evidence Map](11-assurance-lifecycle/threat-control-evidence-map.md) | [LLM Risk](04-llm-risk/llm-risk-register.md), [Incident Review](09-incident-review/incident-review-template.md) | Material threats and failure modes are connected to consequences |
| Risk | What is the likelihood, impact, uncertainty, and risk owner? | [Threat-Control-Evidence Map](11-assurance-lifecycle/threat-control-evidence-map.md) | [Decision Rubric](DECISION_RUBRIC.md) | Risks are prioritized and assigned |
| Security requirements | What protection outcomes must the system satisfy? | [Security Policy and Target](11-assurance-lifecycle/security-policy-and-target-template.md) | [Secure by Design](05-secure-by-design/secure-by-design-product-review.md) | Requirements are testable and linked to threats and mission outcomes |
| Controls | What preventive, detective, corrective, and recovery mechanisms address each requirement? | [Threat-Control-Evidence Map](11-assurance-lifecycle/threat-control-evidence-map.md) | All specialist modules | Control owners and intended outcomes are documented |
| Evidence | What supports implementation, operation, and review? | [Evidence Manifest](02-evidence-manifests/evidence-manifest-template.md) | [Supply Chain Review](06-software-supply-chain/sbom-readiness.md) | Evidence has identifiers, provenance, dates, owners, integrity, and limitations |
| Validation | Was the control implemented, observed, tested, and found effective for the stated scope? | [Control Validation Record](11-assurance-lifecycle/control-validation-record.md) | [Secure by Design](05-secure-by-design/secure-by-design-product-review.md) | Expected and observed results are compared; gaps are recorded |
| Human decision | What may proceed, under which constraints, and who owns residual risk? | [Review Decision](02-evidence-manifests/review-decision-template.md) | [Human Approval Gates](01-ai-agent-security/human-approval-gates.md) | Authorized reviewer records Green, Amber, Red, or More Evidence Required |
| Monitoring and incident response | What telemetry, thresholds, escalation, and investigation paths exist? | [Incident Review](09-incident-review/incident-review-template.md) | [Agent Security](01-ai-agent-security/ai-agent-security-checklist.md), [Zero Trust](03-zero-trust/zero-trust-readiness-map.md) | Detection, triage, evidence preservation, and escalation are defined |
| Recovery | Can the system restore required outcomes within defined constraints? | [Recovery Assurance Record](11-assurance-lifecycle/recovery-assurance-record.md) | [Cyber Survivability](07-cyber-survivability/cyber-survivability-review.md) | Recovery objectives are tested and evidence is reviewed |
| Corrective action | What must change, who owns it, and by when? | [Review Decision](02-evidence-manifests/review-decision-template.md) | [Incident Review](09-incident-review/incident-review-template.md) | Actions have owners, due dates, evidence requirements, and priority |
| Retest | Did the corrective action resolve the observed gap without unacceptable side effects? | [Control Validation Record](11-assurance-lifecycle/control-validation-record.md) | [Recovery Assurance Record](11-assurance-lifecycle/recovery-assurance-record.md) | Retest result and reviewer disposition are recorded |
| Assurance | What confidence is justified, for which scope, until when, and with what limitations? | [Review Decision](02-evidence-manifests/review-decision-template.md) | [Control Validation](11-assurance-lifecycle/control-validation-record.md), [Recovery Assurance](11-assurance-lifecycle/recovery-assurance-record.md), [Decision Rubric](DECISION_RUBRIC.md) | Confidence, limitations, expiration, and next review are explicit |

## Worked example

The [Synthetic Supplier Assurance](10-examples/synthetic-supplier-assurance/) example demonstrates part of this lifecycle. It is explicitly a partial profile, not a completed Full Assurance Lifecycle package.

## Human authority boundary

AI and automation may assist with:

- Inventory and classification
- Threat and control mapping
- Evidence summarization
- Drafting test cases
- Building timelines
- Identifying missing evidence
- Preparing corrective-action options

Authorized humans retain decision authority for:

- Granting or removing privileges
- Disabling identities or services
- Blocking or isolating production systems
- Deleting data
- Rotating production keys
- Accepting residual risk
- Declaring an incident
- Making attribution, legal, compliance, or public claims
- Approving supplier, material, product, or mission status
- Releasing consequential outputs

Use [Human Approval Gates](01-ai-agent-security/human-approval-gates.md) to define each boundary.

## Decision hierarchy

Use one decision hierarchy across the package:

1. **Module assessment:** a local conclusion within a specialist record.
2. **Assurance recommendation:** the package-level recommendation prepared by the review team, with AI assistance where appropriate.
3. **Final assurance decision:** the bounded decision made by the authorized human decision owner.

A module assessment or assurance recommendation does not replace the final assurance decision.

## Minimum completion package

Track completion in the [Review Package Index](02-evidence-manifests/review-package-index-template.md).

A full lifecycle review is not complete until it has:

- [ ] Evidence Manifest
- [ ] Security Policy and Target
- [ ] Identity and Authority Register
- [ ] Threat-Control-Evidence Map
- [ ] Applicable specialist-module reviews
- [ ] Control Validation Record for critical controls
- [ ] Human Approval Gates
- [ ] Recovery Assurance Record where recovery is material
- [ ] Review Decision
- [ ] Corrective actions and retest status

## Decision rule

Use [DECISION_RUBRIC.md](DECISION_RUBRIC.md):

- **Green:** evidence is sufficient for the current scope and stage.
- **Amber:** proceed only with explicit constraints, owners, dates, and evidence needed to reach Green.
- **Red:** do not proceed because a safe constraint set is not available.
- **More Evidence Required:** a defensible decision cannot yet be made.

Assurance is time-bounded. Record an expiration or review date whenever evidence, dependencies, identities, threats, or operating conditions can change.
