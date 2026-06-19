# Human Approval Gates

## Purpose

Define where AI or automation must stop and request human review before acting.

## Approval Gate Categories

| Gate | Example Action | Approval Required? | Approver Role | Evidence Required |
|---|---|---:|---|---|
| Financial | Payment, invoice, purchase, budget commitment | Yes | Owner / finance | Amount, vendor, purpose |
| Legal / contractual | Contract edits, terms, public claims | Yes | Legal / counsel | Draft, source, risk notes |
| Security | Permission changes, firewall change, identity change | Yes | Security owner | Change request, rollback |
| Production | Deployment, deletion, irreversible configuration | Yes | System owner | Test evidence, rollback |
| Mission-impacting | Command, workflow change, data release | Yes | Mission owner | Risk review, authorization |
| Public release | GitHub publish, website update, press language | Yes | Project owner | Public-safety review |

## Approval Decision

- [ ] Approved
- [ ] Approved with conditions
- [ ] Rejected
- [ ] More evidence required

Decision maker:

Date:

Conditions:

Rollback path:

Notes:
