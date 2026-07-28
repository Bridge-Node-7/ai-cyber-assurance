# Assurance Lifecycle Records
> **Artifact type:** RECORD INDEX  
> **Completion status:** Reference document  
> **Required for:** Full Assurance Lifecycle

## Purpose

This folder contains the records used by the **Full Assurance Lifecycle** path.

Start with the top-level [`ASSURANCE_LIFECYCLE.md`](../ASSURANCE_LIFECYCLE.md) navigator. Use these records to connect protection requirements, identities, threats, controls, evidence, validation, human decisions, recovery, corrective action, and retesting.

## Records

| Record | Purpose | Primary Output |
|---|---|---|
| [`security-policy-and-target-template.md`](security-policy-and-target-template.md) | Define the required protection outcome and how it applies to the reviewed system | Approved protection objective and scoped implementation target |
| [`identity-and-authority-register.md`](identity-and-authority-register.md) | Identify human and nonhuman actors, ownership, privileges, approvals, expiration, and revocation | Traceable authority inventory |
| [`threat-control-evidence-map.md`](threat-control-evidence-map.md) | Connect threats and failure modes to requirements, controls, evidence, owners, and decisions | Traceable assurance map |
| [`control-validation-record.md`](control-validation-record.md) | Distinguish documented, implemented, observed, tested, and effective control states | Bounded validation result |
| [`recovery-assurance-record.md`](recovery-assurance-record.md) | Record executed recovery tests, mismatches, corrective action, and retest | Evidence-backed recovery decision |

## Recommended Order

```text
Evidence Manifest
→ Identity and Authority
→ Threat and Risk Identification
→ Security Policy and Target
→ Complete Threat-Control-Evidence Mapping
→ Control Validation
→ Recovery Assurance
→ Review Decision
```

The lifecycle is iterative. Record threats and risk before finalizing security requirements, then return to the map to connect controls, evidence, validation, and decisions.

The Evidence Manifest should identify the reviewed system and evidence package before these records are completed.

## Completion Rule

A record is not complete merely because every field contains text. Completion requires:

- Named owner
- Defined scope
- Evidence references
- Review date
- Bounded decision
- Documented gaps
- Corrective action where required
- Retest where a failed or changed control requires it

## Public-Safety Boundary

Use fictional or authorized information only. Do not include credentials, private keys, customer data, private infrastructure, real vulnerabilities, controlled technical information, or sensitive operational details in a public example.

## Limitations

These records support assurance work. They do not certify a system, authorize deployment, replace legal or compliance review, or prove control effectiveness without appropriate evidence and validation.
