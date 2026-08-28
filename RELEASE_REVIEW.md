# Release Validation: AI Cyber Assurance v0.4.0

AI Cyber Assurance v0.4.0 adds a bounded Assurance Intelligence kernel while preserving the toolkit's defensive assurance boundaries and human decision authority.

## User-facing scope

The release:

- adds one canonical machine-readable Assurance Case representation;
- adds a standard-library assurance-case validator for structural and relationship invariants;
- adds deterministic rendering of a Decision Receipt, Assurance Passport, and Executive Summary from the same case;
- adds one fully synthetic AI-agent assurance example with corrective action and successful retest;
- adds partner guidance that keeps real evidence in private or access-controlled workspaces;
- preserves the existing Quick Review and Full Assurance Lifecycle paths;
- preserves the evidence classes Observed, Tested, Reported, Inferred, and Unknown;
- extends the existing regression suite without requiring a new CI architecture;
- updates selected 2026 cybersecurity supply-chain references.

## Validation boundary

Assurance Case validation checks structural consistency, reference integrity, evidence-class discipline, required authority fields, and closure preconditions.

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
- assurance-case positive and negative tests;
- deterministic rendering checks;
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

## Release condition

The v0.4.0 release candidate is not complete until the pull-request diff receives human review and required hosted validation passes.

## Limitations

Assurance Intelligence supports bounded review consistency and decision communication. It is not a certification engine, autonomous decision maker, production authorization service, GRC replacement, SIEM, SOC platform, or proof that a real system is secure.
