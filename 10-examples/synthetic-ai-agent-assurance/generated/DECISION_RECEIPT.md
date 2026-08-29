# Decision Receipt — DEC\-001

> **Artifact type:** GENERATED VIEW  
> **Operational authority:** None  
> **Source of truth:** `CASE\-AI\-001` canonical Assurance Case  
> **Currency as of 2026-08-28:** CURRENT

## Decision question

May the synthetic AI agent continue operating with bounded supplier\-information access after remediation and retest?

## Scope

Fictional AI agent access to synthetic supplier\-information records and associated authority controls\.

## Evidence considered

### Observed
- EVID\-001

### Tested
- EVID\-004
- EVID\-005

### Reported
- EVID\-002

### Inferred
- None identified in the canonical evidence set

### Unknown
- EVID\-003

## Missing evidence

- No production evidence exists because the example is entirely synthetic\.

## Human decision

**Status:** Amber

**Disposition:** Proceed with bounded authority after successful retest

**Authorized human decision owner:** Fictional Security Owner — Authorized Human Decision Owner

**Confidence:** high

**Confidence basis:** Synthetic Observed and Tested records support the bounded fictional disposition while limitations remain explicit\.

## Conditions

- Read\-only scope
- Bounded credential lifetime
- Revocation path
- Audit logging
- Successful retest

## Corrective actions

- CA\-001: Remove write authority and retain only read access required by the stated purpose\.
- CA\-002: Replace the persistent credential with a bounded\-lifetime credential and preserve revocation capability\.
- CA\-003: Enable required synthetic audit events and verify their generation\.

## Reversal trigger

Unauthorized action, material scope change, failed future retest, or loss of required logging\.

## Review

- Decision date: 2026\-08\-28
- Review date / evidence cutoff: 2026\-08\-28
- Expiration: 2026\-11\-26
- Currency as of 2026-08-28: CURRENT

This receipt communicates the bounded human decision recorded in the canonical case. It does not independently certify, authorize, or establish the security of a real system.
