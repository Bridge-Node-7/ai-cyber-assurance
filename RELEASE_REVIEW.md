# Release Validation: AI Cyber Assurance v0.6.1

AI Cyber Assurance v0.6.1 is the final schema-authoring-parity patch over the v0.6.0 output-integrity hardening release.

## Scope carried forward from v0.6.0

The current release retains all v0.6.0 controls and UX corrections:

- Assurance Case schema version `0.3`;
- exactly one bounded human decision;
- typed cross-object references;
- accountable-human linkage for nonhuman identities;
- material statements for claims, risks, controls, and findings;
- Green / Amber / Red / More evidence required decision status;
- complete Amber condition package;
- explicit recorded / none identified / not assessed / not applicable / unknown states;
- chronology and review-currency checks;
- Markdown/HTML output escaping and Unicode-control rejection;
- output-fidelity checks against forged `Human decision` sections;
- no generated-output overwrite without explicit `--force`;
- partner confidentiality/intake routing;
- workflow navigation and narrow-screen authoring guidance;
- adversarial regression coverage.

## v0.6.1 closure additions

This patch closes the final verification gaps found during post-release audit:

1. **Schema authoring parity.** Local conditional requirements are now encoded in the JSON Schema for:
   - nonhuman identity accountability;
   - confidence basis when confidence is supplied;
   - required closure fields for closed findings;
   - Amber decision conditions and bounded operating fields;
   - More-evidence-required cases;
   - completed corrective-action dates; and
   - rationale for non-independent retests.

2. **Committed generated-output parity.** The regression suite again proves that the committed synthetic AI-agent Decision Receipt, Assurance Passport, and Executive Summary match the current safe renderer byte-for-byte for the fixed example review date.

Cross-object ID typing, chronology, closure semantics, and other repository-specific relational invariants remain the responsibility of the standard-library executable validator; JSON Schema does not resolve those relationships by itself.

## Validation boundary

Assurance Case validation checks structural consistency, typed reference integrity, evidence-class discipline, required human authority fields, material statement presence, decision-state semantics, date/chronology fields, currency status, and closure preconditions.

Safe rendering checks presentation fidelity after structural validation.

These checks do not establish:

- factual truth or evidence authenticity;
- evidence sufficiency;
- real-world control effectiveness;
- certification or compliance;
- deployment or operational authorization;
- independent validation of a real partner system;
- successful partner outcomes.

## Repository validation

Release validation covers:

- the full standard-library regression suite;
- Assurance Case positive and adversarial negative tests;
- Markdown/HTML and Unicode-control injection tests;
- deterministic safe rendering across two distinct synthetic domains;
- committed generated-output parity;
- schema/validator material-field and local-conditional parity checks;
- chronology and currency tests;
- navigation regression tests;
- deterministic metadata, manifest, SHA-256 integrity, links, public-safety declarations, and repository identity;
- hosted Ubuntu and Windows GitHub Actions.

## Public/private boundary

The repository contains reusable public methodology, validation logic, templates, and synthetic examples only.

Real partner architecture, evidence, telemetry, supplier information, credentials, vulnerabilities, regulated data, proprietary material, and decision records belong in private or access-controlled workspaces unless deliberately approved for unrestricted release.

## Release-state semantics

`REPO_MANIFEST.json` describes a validation-gated public release channel. The authoritative evidence that a specific version was actually published is the corresponding GitHub Release and tag.

## Release gate

v0.6.1 is complete only after:

1. the human-authorized pull request is merged through protected `main`;
2. required Ubuntu and Windows validation passes on the merged commit; and
3. the versioned GitHub Release is published for that exact commit.

## Human UAT boundary

The repository incorporates adversarial simulated UAT and deterministic regression tests. It does not claim that representative partner users have been observed completing real cases, that assistive-technology testing has been completed, or that real partner outcomes have been established.

Those are evidence to collect during controlled private pilots, not unfinished public-repository engineering claims.

## Limitations

Assurance Intelligence supports bounded review consistency, safer decision communication, and traceable closure. It is not a certification engine, autonomous decision maker, production authorization service, GRC replacement, SIEM, SOC platform, or proof that a real system is secure.
