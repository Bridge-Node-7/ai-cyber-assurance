# Release Validation: AI Cyber Assurance v0.6.0

AI Cyber Assurance v0.6.0 closes the generated-view trust-boundary and authoring-contract findings identified during adversarial V&V of v0.5.0 while preserving defensive assurance boundaries and human decision authority.

## User-facing scope

The release:

- advances the Assurance Case contract to schema version `0.3`;
- preserves exactly one bounded human decision per Assurance Case;
- keeps typed cross-object references and accountable-human linkage for nonhuman identities;
- requires material statements for claims, risks, controls, and findings before a case can render;
- adds controlled decision status: Green, Amber, Red, or More evidence required;
- requires a complete bounded condition package for Amber decisions;
- distinguishes recorded items, none identified, not assessed, not applicable, and unknown for conditions and missing evidence;
- validates chronology across evidence, findings, decisions, corrective actions, retests, closure, and review history;
- reports case currency as CURRENT, EXPIRED, or NOT_YET_CURRENT without rewriting historical records;
- escapes case-controlled Markdown and raw HTML before generated views are produced;
- rejects unsafe Unicode formatting/control characters in the canonical case;
- performs output-fidelity checks so supplied content cannot create a second generated `Human decision` section;
- refuses to overwrite existing generated views unless a human explicitly supplies `--force`;
- links the partner confidentiality boundary and intake template into the intended partner workflow;
- adds workflow navigation to reusable specialist and lifecycle records identified as dead ends;
- adds a narrow-screen/editor authoring alternative for wide traceability tables;
- expands adversarial regression coverage for view injection, material-field omissions, conditional-decision semantics, currency, chronology, schema parity, safe overwrite, CLI help, and navigation.

## V&V findings closed by this release

The corrective scope directly addresses:

- generated-view Markdown/HTML structure injection;
- schema omissions for material validator/renderer fields;
- silent blanking of material risk/finding statements;
- Amber decisions without explicit conditions and bounded operating context;
- stale-review ambiguity;
- incomplete chronology between remediation and retest/closure;
- ambiguous `None recorded` presentation;
- partner confidentiality/intake documents outside the intended navigation path;
- reusable workflow records with no return/next-step path;
- accidental overwriting of generated views;
- minimal CLI help;
- `.pytest_cache/` local hygiene.

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
- schema/validator parity checks for the material contract;
- chronology and currency tests;
- navigation regression tests;
- repository structure;
- deterministic metadata;
- manifest and checksum integrity;
- internal links;
- common secret and personal-information patterns;
- public-safety declarations;
- hosted Ubuntu and Windows GitHub Actions.

## Public/private boundary

The repository contains reusable public methodology, validation logic, templates, and synthetic examples only.

Real partner architecture, evidence, telemetry, supplier information, credentials, vulnerabilities, regulated data, proprietary material, and decision records belong in private or access-controlled workspaces unless deliberately approved for unrestricted release.

The partner path links the confidentiality boundary before real evidence intake.

## Release-state semantics

`REPO_MANIFEST.json` describes a **validation-gated public release channel**, not a time-sensitive publication state. The authoritative evidence that a specific version was actually published is the corresponding GitHub Release and tag.

This avoids a manifest becoming stale after the protected-main release job publishes an otherwise identical validated tree.

## Security reports

Security concerns should use the private reporting path described in [`SECURITY.md`](SECURITY.md).

## Release gate

v0.6.0 is complete only after:

1. the human-authorized pull request is merged through protected `main`;
2. required Ubuntu and Windows validation passes on the merged commit; and
3. the versioned GitHub Release is published for that exact commit.

Versioned GitHub Release publication is gated behind successful validation on protected `main`. Publication is idempotent: if the current `VERSION` release already exists, the release job makes no change.

## Human UAT boundary

The repository incorporates adversarial simulated UAT and deterministic regression tests. It does not claim that representative partner users have been observed completing real cases, that assistive-technology testing has been completed, or that real partner outcomes have been established.

Those are evidence to collect during controlled private pilots, not facts to invent in the public repository.

## Limitations

Assurance Intelligence supports bounded review consistency, safer decision communication, and traceable closure. It is not a certification engine, autonomous decision maker, production authorization service, GRC replacement, SIEM, SOC platform, or proof that a real system is secure.
