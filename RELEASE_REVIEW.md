# Release Validation: AI Cyber Assurance v0.5.0

AI Cyber Assurance v0.5.0 hardens the Assurance Intelligence kernel for generic bounded partner use while preserving defensive assurance boundaries and human decision authority.

## User-facing scope

The release:

- advances the Assurance Case contract to schema version `0.2`;
- requires exactly one bounded human decision per Assurance Case;
- enforces typed cross-object references rather than existence-only references;
- requires an accountable human identity for nonhuman identities;
- requires corrective actions to preserve decision linkage;
- requires retest independence metadata or a rationale when retest is not independent;
- validates review-history and ISO date fields;
- removes AI-agent-specific assumptions from generated Executive Summaries and other views;
- adds a second, distinct synthetic cryptographic Assurance Case to prove cross-domain rendering;
- expands adversarial regression coverage for decision cardinality, typed references, authority, dates, review history, retest independence, and multi-domain rendering;
- records that repository version 0.3.0 was not separately published as a GitHub Release/tag.

## Validation boundary

Assurance Case validation checks structural consistency, typed reference integrity, evidence-class discipline, required human authority fields, date fields, and closure preconditions.

It does not establish:

- factual truth or evidence authenticity;
- evidence sufficiency;
- real-world control effectiveness;
- certification or compliance;
- deployment or operational authorization;
- independent validation of a real system.

## Repository validation

Release validation covers:

- the regression suite;
- Assurance Case positive and adversarial negative tests;
- deterministic rendering across two distinct synthetic domains;
- schema/validator parity checks for core invariants;
- repository structure;
- deterministic metadata;
- manifest and checksum integrity;
- internal links;
- common secret and personal-information patterns;
- public-safety declarations;
- hosted Ubuntu and Windows GitHub Actions.

## Public/private boundary

The repository contains only reusable public methodology, validation logic, templates, and synthetic examples.

Real partner architecture, evidence, telemetry, supplier information, credentials, vulnerabilities, regulated data, proprietary material, and decision records belong in private or access-controlled workspaces unless deliberately approved for unrestricted release.

## Security reports

Security concerns should use the private reporting path described in [`SECURITY.md`](SECURITY.md).

## Release gate

v0.5.0 is complete only after the human-authorized pull request is merged, required Ubuntu and Windows validation passes on protected `main`, and the versioned GitHub Release is published.

Versioned GitHub Release publication is gated behind successful validation on protected `main`. Publication is idempotent: if the current `VERSION` release already exists, the release job makes no change.

## Limitations

Assurance Intelligence supports bounded review consistency and decision communication. It is not a certification engine, autonomous decision maker, production authorization service, GRC replacement, SIEM, SOC platform, or proof that a real system is secure.
