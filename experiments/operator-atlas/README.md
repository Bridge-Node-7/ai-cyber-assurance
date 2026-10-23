# Operator Atlas — Procedure Compass (research prototype v0.2)

**The right knowledge. The right action. The proof that is still missing.**

A search-first, local-only web experiment in the AI Cyber Assurance reference repository. It explores whether task-shaped, source-linked operator guidance can reduce the time between a practical question and an honest, human-reviewable record.

The product is inspired by the **purpose** of cross-disciplinary technical field references, including NETMUX's *Operator Handbook*, but contains entirely original procedures and presentation. No text, diagrams, commands, branding, or content from the handbook are reproduced.

## Try it

Open [index.html](index.html) in a browser. Search for *contractor*, *CVE*, or *agent*, select a procedure, provide synthetic/nonsensitive review labels, and record observations. JSON export is manual and contains only user-declared information.

No backend, credentials, third-party scripts, analytics, network requests, persistent browser storage, or live-system integrations. External source sites are opened only when a user clicks a link. It works as a static file without a server; static HTTPS hosting can be evaluated separately.

## What exists (implemented)

- Plain-language search over **three** curated, original procedures
- Procedure metadata: audience, applicability, editorial review date, risk, external source links
- **180-day editorial review reminder**, not automatic determination of technical obsolescence
- Authorization, bounded scope, owner, named reviewer
- Per-check **Observed / Tested / Reported / Inferred / Unknown** evidence declarations
- Three explicit output states: **SAFE STOP**, **WAIT**, **READY FOR HUMAN REVIEW**
- JSON export of unverified user declarations; reset removes this tab's in-memory record
- Responsive, keyboard-usable interface built with DOM text rather than untrusted HTML insertion

## Procedure catalog

1. Contractor offboarding access review — NIST 800-63-4 identity/session guidance.
2. Vulnerable dependency triage — CISA KEV, OSV and EPSS provenance distinctions.
3. AI agent permission review — NIST AI RMF and OWASP GenAI threat/authority context.

**Do not put secrets, passwords, tokens, PII, client-sensitive records, or live-system evidence in this prototype.** An ordinary browser and JSON downloads are not a confidential evidence vault.

## Decision semantics

- **SAFE STOP** — no user-declared authorization.
- **WAIT** — scope/owner/reviewer missing, or any check lacks an Observed/Tested declaration, dated observation, and reference.
- **READY FOR HUMAN REVIEW** — only means all required user-declared fields are present. It does *not* imply evidence authenticity, factual correctness, remediation completion, configuration validity, safety, conformity, effectiveness, certification, final sign-off, or permission to operate.

A checkbox or user-selected "Tested" class cannot prove a real test happened. All final actions remain human-governed. No cross-repository import, change of FMA/AI Cyber Assurance semantics, or promotion into canonical institutional evidence occurs.

## Run validation

```bash
node tests/engine.test.cjs
```

This tests deterministic logic only. See [acceptance scenarios](tests/ACCEPTANCE.md) for human browser verification, including responsive layout. No GitHub Pages deployment has been enabled or verified as part of this experiment.

## Architecture / future steps

`index.html` (view) → `ui.js` (in-memory controls/export) → `engine.js` (fixed original catalog and structural decision gates). There are deliberately no cross-repository runtime dependencies.

Before any public promotion: browser tests, accessibility audit, provenance review, threat model, license check, evidence privacy design, content-maintenance owner, pilot task-success measurement, and product-home decision. The research prototype can be moved to a dedicated repository only when independent public purpose, rights boundary, or release cadence justifies it under the BN7 architecture rule.

## Intellectual property

Copyright (c) 2026 Bridge Node 7. This directory follows the host repository's MIT License. Third-party sources are linked, not incorporated. Product value and novelty are hypotheses requiring customer testing and prior-art assessment.
