# Synthetic Cryptographic Withdrawal

> **Artifact type:** COMPLETED SYNTHETIC EXAMPLE
> **Completion status:** Completed reference example
> **Operational authority:** None

This example is fully synthetic and fictional. It demonstrates a bounded Cryptographic Change Assurance review without describing a real organization, system, vulnerability, cryptographic product, or operational environment.

The identifiers, timings, systems, and cryptographic names below are illustrative test data, not benchmarks or real-world claims.

## Scenario

A fictional records service uses synthetic primitive `SYN-ALG-A` in several trust and data-protection paths.

Synthetic policy evidence `SYN-CR-E-001` states that `SYN-ALG-A` must be withdrawn from the fictional service boundary. The approved candidate replacement is `SYN-ALG-B`.

The initial review contains one deliberately Unknown dependency so the method can demonstrate fail-closed behavior.

## Evidence Gate

| Field | Entry |
|---|---|
| Claim ID | SYN-CR-C-001 |
| Evidence ID | SYN-CR-E-001 |
| Claim | SYN-ALG-A is disallowed for this fictional boundary |
| Current state | ACTIONABLE |
| Scope | Synthetic records service only |
| Explicit limit | No claim is made about any real algorithm or implementation |
| Human authority | SYN-OWNER-001 |

Synthetic transition history:

```text
QUARANTINED
→ REPRODUCED
→ CORROBORATED
→ IMPACT-MAPPED
→ HUMAN-AUTHORIZED
→ ACTIONABLE
```

## Dependency and State Review

| Usage ID | Asset | Function | Current primitive | State class | Status |
|---|---|---|---|---|---|
| SYN-CR-U-001 | API session | Session protection | SYN-ALG-A | SM-0 | Mapped |
| SYN-CR-U-002 | Service credential | Renewable trust material | SYN-ALG-A | SM-1 | Mapped |
| SYN-CR-U-003 | Database key hierarchy | Stored-data protection | SYN-ALG-A | SM-2 | Mapped |
| SYN-CR-U-004 | Reporting database | Stored-data protection | SYN-ALG-A | SM-3 | Mapped |
| SYN-CR-U-005 | Evidence archive | Long-lived archive | SYN-ALG-A | SM-4 | Mapped after corrective action |
| SYN-CR-U-006 | Archive import job | Dependency | SYN-ALG-A | Unknown initially | Resolved before retest |

### Initial result

`SYN-CR-U-006` was not mapped during the first pass.

Because a critical dependency remained Unknown, the initial module assessment was:

**More Evidence Required**

The review did not infer that the missing dependency was safe.

## Corrective Action

The fictional review owner mapped `SYN-CR-U-006`, established its relationship to the evidence archive, and classified the affected archive as `SM-4`.

The transition plan was then updated so the archive received a separate preservation and verification treatment instead of being silently grouped with ordinary re-encryptable data.

## Blast-Radius View

No aggregate blast-radius score is used.

| Dimension | Synthetic finding |
|---|---|
| Mission consequence | Reporting remains available only if session, credential, database, and archive paths remain valid |
| Affected assets | Six mapped usages |
| Persistent-state burden | SM-2, SM-3, and SM-4 state require distinct treatments |
| Dependency depth | Archive import path was the limiting dependency |
| Policy constraints | SYN-ALG-A may not return through fallback |
| Replacement availability | SYN-ALG-B is available in the fictional test boundary |
| Unknowns | No critical unknown remains after corrective action |

## Substitution Readiness

The fictional nonproduction exercise confirmed:

- session state could be recreated under `SYN-ALG-B`;
- renewable trust material could be replaced through the synthetic renewal path;
- the database key hierarchy had a bounded rewrap path;
- bulk reporting data had a bounded migration and integrity-check path;
- archival evidence required a separate long-term treatment;
- the archive import dependency was included in verification;
- the fallback test did not restore `SYN-ALG-A`.

## Time to Safe Substitution

Illustrative exercise durations:

| Stage | Duration |
|---|---:|
| Evidence intake | 1 unit |
| Validation | 2 units |
| Decision and authorization | 1 unit |
| Preparation | 3 units |
| Staging | 2 units |
| Cutover | 1 unit |
| Persistent-state migration | 6 units |
| Verification | 2 units |
| **TSS** | **18 units** |

These synthetic units demonstrate the calculation only. They are not performance targets or real-world timing claims.

## Withdrawal Exercise Result

| Check | Result |
|---|---|
| Critical dependencies mapped | PASS |
| Persistent state classified | PASS |
| Candidate substitution path bounded | PASS |
| Pre-cutover checks completed | PASS |
| Silent fallback blocked | PASS |
| Recovery path reviewed | PASS |
| Verification evidence recorded | PASS |

## Final Module Assessment

**Amber**

The synthetic evidence supports a bounded transition exercise, with one continuing condition: the `SM-4` archive must remain under its approved preservation treatment and reassessment schedule.

This is a module assessment only. It does not authorize a real cryptographic change, establish certification, or demonstrate the safety of any real algorithm, product, or system.
