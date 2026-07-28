# Human Approval Gates
> **Artifact type:** TEMPLATE  
> **Completion status:** Blank for reuse  
> **Required for:** Conditional: systems with consequential automated actions

## What this document is

A record of where AI or automation must stop and request authorized human review before an action is approved or executed.

## Who should complete it

The system owner, security owner, process owner, and each role authorized to approve consequential actions.

## When to use it

Use whenever an AI or automated workflow can change external state, create commitments, expose data, alter access, affect production, publish content, or influence high-impact decisions.

## Related records

- [Identity and Authority Register](../11-assurance-lifecycle/identity-and-authority-register.md)
- [Evidence Manifest](../02-evidence-manifests/evidence-manifest-template.md)
- [Control Validation Record](../11-assurance-lifecycle/control-validation-record.md)
- [Review Decision](../02-evidence-manifests/review-decision-template.md)

## Approval-gate register

| Gate ID | Trigger condition | Example action | Initiating human identity | Agent / automation identity | Required approver | Prohibited self-approval | Required evidence package | Approval scope and expiration | Execution authority | Execution confirmation | Rollback owner | Emergency override | Post-action validation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HAG-01 | Financial commitment | Payment, invoice, purchase, budget commitment | | | Owner / finance | Yes | Amount, counterparty, purpose, source, fraud checks | | | | | | |
| HAG-02 | Legal or contractual effect | Contract edit, term acceptance, external legal statement | | | Authorized legal / counsel role | Yes | Draft, source text, risk notes, affected parties | | | | | | |
| HAG-03 | Security or identity change | Permission, firewall, key, token, account, or policy change | | | Security owner | Yes | Change request, impact, test evidence, rollback | | | | | | |
| HAG-04 | Production or irreversible change | Deployment, deletion, isolation, destructive configuration | | | System owner | Yes | Test evidence, affected scope, rollback, recovery | | | | | | |
| HAG-05 | Mission or safety impact | Command, workflow change, high-impact data release | | | Mission / safety owner | Yes | Risk review, authority, constraints, contingency | | | | | | |
| HAG-06 | Public release | GitHub publication, website update, public claim | | | Project / release owner | Yes | Public-safety review, evidence, limitations, attribution | | | | | | |
| HAG-07 | Supplier or qualification decision | Approve, suspend, reject, or condition supplier/material status | | | Authorized qualification owner | Yes | Identity, provenance, evidence, validation, conflict review | | | | | | |
| HAG-08 | Incident declaration or external notification | Declare incident, attribution, customer or law-enforcement notice | | | Incident authority / counsel as applicable | Yes | Timeline, evidence, confidence, impact, obligations | | | | | | |

## Decision record

Gate ID:

Requested action:

- [ ] Approved
- [ ] Approved with conditions
- [ ] Rejected
- [ ] More evidence required

Decision maker:

Authority basis:

Decision date and time:

Expiration / revisit date:

Conditions:

Evidence reviewed:

Execution confirmation:

Rollback result:

Post-action validation result:

Notes:
