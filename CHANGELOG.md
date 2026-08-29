# Changelog

## [0.6.1] - 2026-08-28

### Improved

- Encoded local conditional authoring rules directly in the Assurance Case JSON Schema for nonhuman accountability, confidence basis, closed-finding closure fields, Amber decision requirements, More-evidence-required cases, completed corrective actions, and non-independent retests.
- Restored an explicit regression test proving the committed synthetic AI-agent generated views match the current safe renderer byte-for-byte for the fixed review date.
- Expanded schema/validator parity coverage to require the material conditional rules as part of the published authoring contract.

### Limitations

- Cross-object typed-reference, chronology, and other relational invariants remain the responsibility of the standard-library executable validator because JSON Schema does not resolve repository-specific object relationships by itself.
- Structural and presentation-integrity validation still does not establish evidence authenticity or sufficiency, real-world control effectiveness, certification, compliance, deployment approval, operational authorization, or partner outcomes.

## [0.6.0] - 2026-08-28

### Added

- Assurance Case schema version `0.3` with material renderer-consumed and validator-enforced fields documented in the public contract.
- Controlled decision-status vocabulary: Green, Amber, Red, and More evidence required.
- Explicit absence states for conditions and missing evidence so `none_identified`, `not_assessed`, `not_applicable`, `unknown`, and recorded items remain distinct.
- Review-currency reporting with `CURRENT`, `EXPIRED`, and `NOT_YET_CURRENT`, plus an optional `--require-current` gate.
- Chronology checks across evidence collection, findings, human decision, corrective action, retest, closure, review history, and the review cutoff.
- Adversarial regression tests for Markdown/HTML injection, Unicode formatting controls, silent material-field blanking, Amber decision completeness, stale review currency, chronology, output overwrite protection, and CLI help.
- Navigation regression tests for partner onboarding and reusable lifecycle/specialist records identified by UX review.
- A narrow-screen/editor authoring alternative that preserves wide-table field semantics without creating a second assurance model.

### Fixed

- Escaped case-controlled Markdown and raw HTML before generated views are produced, preventing supplied text from creating a forged `Human decision` section.
- Required material statements for claims, risks, controls, and findings so a structurally valid case cannot silently render blank executive content.
- Required Amber decisions to carry explicit bounded scope, conditions, due date, prohibited actions, monitoring requirements, required retests, and expiration/review context.
- Replaced ambiguous `None recorded` output with explicit state-aware language.
- Prevented the renderer from silently overwriting existing generated views unless `--force` is supplied.
- Linked the partner confidentiality boundary and intake template directly into the intended partner workflow.
- Added return/next-step navigation to the reusable LLM-risk, software-supply-chain, survivability, high-impact, incident, and assurance-lifecycle records identified as workflow dead ends.
- Added `.pytest_cache/` to ignored local Python artifacts.

### Improved

- Added output-fidelity checks after rendering and direct-library fail-closed validation before files are written.
- Expanded CLI help for both Assurance Case validation and rendering.
- Clarified that historical cases may remain structurally valid after expiry while a current decision can require current review status explicitly.
- Clarified that Markdown templates remain sufficient for many reviews and Assurance Intelligence is an optional structured layer.
- Replaced time-sensitive manifest release-candidate state with durable validation-gated release-policy metadata; GitHub Releases and tags are the publication source of truth.

### Limitations

- Structural and presentation-integrity validation still does not establish evidence authenticity or sufficiency, real-world control effectiveness, certification, compliance, deployment approval, operational authorization, or partner outcomes.
- Private cases created against Assurance Case schema v0.2 or earlier require migration before validation under schema v0.3.
- Human usability and accessibility in real partner environments require observation during controlled pilots; the public repository does not claim those outcomes in advance.

## [0.5.0] - 2026-08-28

### Added

- Assurance Case schema version `0.2` for generic bounded partner use.
- Typed cross-object reference validation for identities, claims, risks, controls, evidence, findings, decisions, corrective actions, and retests.
- Accountable-human linkage for nonhuman identities.
- Required retest-independence metadata, with rationale required when retest is not independent.
- ISO date and review-history validation.
- A second completed synthetic Assurance Case in a distinct cryptographic-change domain.
- Adversarial regression tests for decision cardinality, wrong-type references, authority, dates, review history, retest independence, and cross-domain rendering.

### Fixed

- Removed AI-agent and supplier-information assumptions from the generic Executive Summary renderer.
- Prevented structurally valid cases with zero or multiple decisions from reaching a renderer that expects one bounded decision.
- Prevented references from resolving merely because an ID exists in the wrong object collection.
- Strengthened closure linkage between findings, corrective actions, retests, evidence, and the bounded human decision.

### Improved

- Clarified that the JSON Schema documents the envelope and local field constraints while the standard-library validator is authoritative for cross-object relational invariants.
- Added schema/validator parity tests for the case version, decision cardinality, and evidence classes.
- Documented the historical 0.3.0 repository-version milestone as not separately published as a GitHub Release/tag.

### Limitations

- Structural validation still does not establish evidence authenticity or sufficiency, real-world control effectiveness, certification, compliance, deployment approval, or operational authorization.
- The v0.2 Assurance Case contract is stricter than v0.1; private cases created against v0.1 require migration before validation under this release.

## [0.4.0] - 2026-08-28

### Added

- Assurance Intelligence as an optional structured layer over the existing assurance methodology.
- A canonical machine-readable Assurance Case schema.
- A standard-library assurance-case validator with fail-closed relationship and closure checks.
- Deterministic Decision Receipt, Assurance Passport, and Executive Summary rendering from one canonical case.
- A completed synthetic AI-agent assurance case demonstrating excessive initial authority, human decision ownership, corrective action, retest, and structural closure.
- A minimal partner starter kit with explicit public/private evidence boundaries.
- Regression tests covering valid cases, duplicate IDs, dangling references, invalid evidence classes, missing human authority, invalid closure, Unknown evidence misuse, and output determinism.
- Validated-main GitHub Release publication after required hosted checks succeed.

### Improved

- Added Assurance Intelligence routing to README and Start Here without replacing Quick Review or Full Assurance Lifecycle.
- Added a structured-case example to the example index.
- Strengthened partner-pilot entry, outputs, completion criteria, and real-use boundaries.
- Refreshed selected 2026 cybersecurity supply-chain references.

### Limitations

- Assurance Case validation checks structure and relationships only. It does not establish evidence authenticity or sufficiency, real-world control effectiveness, certification, compliance, deployment approval, or operational authorization.
- This release does not add a database, graph backend, API, dashboard, customer portal, autonomous remediation, autonomous risk acceptance, or numerical trust score.

## [0.3.0] - 2026-08-17

> Repository version milestone. This version was not separately published as a GitHub Release or `v0.3.0` tag.

### Added

- Cryptographic Change Assurance as a bounded specialist review for cryptographic replacement, withdrawal, and revalidation.
- A cryptographic evidence gate with explicit progression from Quarantined through Actionable.
- Dependency, state-mobility, blast-radius, substitution-readiness, and Time to Safe Substitution review.
- A bounded withdrawal-exercise template and Cryptographic Change Decision Pack.
- A completed synthetic cryptographic-withdrawal example.
- Deterministic release-metadata refresh and drift checking.

### Improved

- Added cryptographic-change routing to the repository onboarding and assurance lifecycle.
- Extended validation and regression coverage for the new specialist module.
- Added current public references for cryptographic agility and post-quantum migration.

### Limitations

- This version does not implement cryptography, authorize live changes, establish certification or compliance, or prove that a real system can complete a cryptographic transition.

## [0.2.2] - 2026-08-06

### Added

- A single `START_HERE.md` navigator for safe package creation and review-path selection.
- An `AGENTS.md` operating contract for evidence classification, AI-assistance boundaries, stop conditions, and required outputs.
- A Review Package Index for applicability, status, blockers, recommendation, and final-decision control.
- Standard-library regression tests for the UX contract and version authority.
- Ubuntu and Windows hosted validation.

### Improved

- Made the README opening outcome-led, safe, and immediately actionable.
- Established `VERSION` as the validator's release-version authority.
- Added validator checks for onboarding, AI-assistance guidance, package vocabulary, and decision hierarchy.
- Replaced time-sensitive release-state and security-policy wording with durable language.

### Limitations

- Validation confirms the controlled public toolkit structure. It does not prove the truth or sufficiency of evidence in a private review, establish control effectiveness, authorize a system, or replace accountable human judgment.

## [0.2.1] - 2026-08-06

### Fixed

- Enforced LF checkout for checksum files and all hashed text formats across operating systems.
- Added GNU `sha256sum -c` to hosted validation so checksum portability is tested directly.
- Preserved the v0.2.0 assurance content and evidence boundaries without product-scope changes.

## [0.2.0] - 2026-07-27

### Added

- Two explicit user paths: Quick Review and Full Assurance Lifecycle.
- A top-level assurance lifecycle navigator.
- Security policy and target, identity and authority, threat-control-evidence, control validation, and recovery assurance records.
- A completed synthetic supplier-assurance profile.
- Repository validation, manifest verification, and GitHub Actions checks.
- Standardized template and example labels.

### Improved

- Human approval gates.
- Evidence provenance and integrity fields.
- High-impact system routing.
- Public-safety wording.
- Reference precision and publication-status labeling.
- README onboarding, artifact selection, and effort guidance.

### Limitations

- The repository does not certify systems, authorize deployment, prove control effectiveness in a real environment, or claim independent validation.
