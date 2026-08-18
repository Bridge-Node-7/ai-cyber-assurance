# AI Cyber Assurance

**AI Cyber Assurance helps teams organize evidence and make accountable human decisions about AI-enabled and high-impact systems.**

[Start here](START_HERE.md) to choose a review path, create a safe working package, and identify the records that apply.

- **Use it when:** reviewing a workflow, pilot, release, supplier, incident, AI agent, or high-impact system.
- **Use it with:** system owners, engineers, security reviewers, operators, governance teams, auditors, and authorized decision owners.
- **AI may help with:** organizing, drafting, mapping, questioning, summarizing, and checking.
- **Humans remain responsible for:** evidence access, fact validation, consequential actions, risk acceptance, and the final assurance decision.

> **Start safely:** Create a private or access-controlled working package outside this public repository before adding real evidence. Publish only material deliberately approved for unrestricted release.

AI assistants and coding agents should read [`AGENTS.md`](AGENTS.md) before applying or modifying this repository.

## What this is

AI Cyber Assurance is a defensive documentation and workflow toolkit for builders, operators, security reviewers, governance teams, auditors, founders, and system owners.

It helps teams connect:

```text
Mission
→ Boundary
→ Assets and Dependencies
→ Identities and Authority
→ Threats and Failure Modes
→ Risk
→ Security Requirements
→ Controls
→ Evidence
→ Validation
→ Human Decision
→ Monitoring and Incident Response
→ Recovery
→ Corrective Action
→ Retest
→ Assurance
```

The result is a traceable review package with named owners, bounded claims, visible evidence gaps, accountable decisions, and next actions.

## What this produces

A completed review can include:

- A defined system boundary
- A review package index
- An identity and authority record
- A threat-control-evidence map
- Control validation results
- Human approval gates
- Recovery evidence
- A bounded review decision
- Corrective actions and retest status

## What this does not do

This repository does **not**:

- Certify a system
- Authorize deployment or operation
- Replace legal, compliance, privacy, safety, or engineering review
- Prove that a control is effective without supporting evidence
- Provide offensive exploit instructions, malware code, credential-theft workflows, or unauthorized-access procedures
- Claim production maturity, independent validation, or external endorsement

## Five-minute orientation

This is an orientation, not a completion-time estimate.

1. Open [`START_HERE.md`](START_HERE.md).
2. Create a private or access-controlled working package.
3. Copy the [Review Package Index](02-evidence-manifests/review-package-index-template.md).
4. Choose Quick Review or Full Assurance Lifecycle.
5. Copy only the applicable records.
6. Record evidence, gaps, owners, limitations, and required human decisions.
7. Apply the [Decision Rubric](DECISION_RUBRIC.md) and complete the [Review Decision](02-evidence-manifests/review-decision-template.md).

## Choose your path

### Quick Review

Use this path for one workflow, product, pilot, or release:

```text
Review Package Index
→ Evidence Manifest
→ Relevant Specialist Module
→ Decision Rubric
→ Review Decision
```

Start here:

1. [Start Here](START_HERE.md)
2. [Review Package Index](02-evidence-manifests/review-package-index-template.md)
3. [Evidence Manifest](02-evidence-manifests/evidence-manifest-template.md)
4. [Decision Rubric](DECISION_RUBRIC.md)
5. [Review Decision](02-evidence-manifests/review-decision-template.md)

### Full Assurance Lifecycle

Use this path for high-impact, operational, multi-party, or deeply integrated systems:

1. Open [Start Here](START_HERE.md) and create the [Review Package Index](02-evidence-manifests/review-package-index-template.md).
2. Follow the [Assurance Lifecycle](ASSURANCE_LIFECYCLE.md).
3. Define mission, boundary, assets, dependencies, and evidence.
4. Record identities and authority.
5. Identify threats, failure modes, risk, and uncertainty.
6. Establish the security policy, target, and requirements.
7. Map controls to evidence.
8. Validate controls, monitoring, response, and recovery.
9. Make an accountable human decision.
10. Track corrective action and retest.

## Which artifacts apply?

```text
Does the system use tool-performing AI or automation?
→ Use AI Agent Security and Human Approval Gates.

Does it use an LLM, retrieval, model, or generated output?
→ Use the LLM and Generative AI Risk Register.

Does it depend on third-party code, models, data, or services?
→ Use Software and AI Supply Chain Readiness.

Could loss, corruption, or interruption create material harm?
→ Use Cyber Survivability and Recovery Assurance.

Does approved cryptography need to be replaced, withdrawn, or revalidated?
→ Use Cryptographic Change Assurance.

Is the system high-impact, multi-party, operational, or deeply integrated?
→ Use the Full Assurance Lifecycle.
```

## Expected effort

Effort depends on scope and evidence availability:

- **Quick Review:** one bounded workflow, product change, pilot, or release.
- **Specialist Module:** one control family or risk area.
- **Full Assurance Lifecycle:** a multi-stakeholder review across the system lifecycle.

These are relative effort bands, not measured completion-time promises.

## Core doctrine

- **Judgment stays human.** AI may assist analysis, drafting, mapping, and evidence review. Accountable people retain authority over consequential decisions.
- **Evidence leads.** A policy statement is not operating evidence. A configuration is not test evidence. An alert is not an incident determination.
- **Boundaries are explicit.** Systems include people, identities, data, tools, suppliers, infrastructure, facilities, and dependencies.
- **Controls are traceable.** Requirements connect to controls, evidence, validation, decisions, and corrective action.
- **Recovery is engineered.** A backup, rollback path, or disable mechanism is not trusted until it is tested and reviewed.
- **Claims remain bounded.** Templates support assurance work; they do not establish certification or operational effectiveness by themselves.

## Specialist modules

| Module | Use it to | Primary output |
|---|---|---|
| [AI Agent Security](01-ai-agent-security/ai-agent-security-checklist.md) | Review tool-using agents and human approval boundaries | Agent checklist and approval gates |
| [Evidence Manifests](02-evidence-manifests/evidence-manifest-template.md) | Define the system, evidence, gaps, package status, and decision | Package index, evidence manifest, and review decision |
| [Zero Trust](03-zero-trust/zero-trust-readiness-map.md) | Review identity, access, trust assumptions, and visibility | Zero Trust readiness map |
| [LLM Risk](04-llm-risk/llm-risk-register.md) | Track LLM and generative AI security risks | LLM risk register |
| [Secure by Design](05-secure-by-design/secure-by-design-product-review.md) | Review secure defaults and release design | Secure-by-design review |
| [Software Supply Chain](06-software-supply-chain/sbom-readiness.md) | Review dependencies, provenance, models, and release integrity | Supply-chain readiness review |
| [Cyber Survivability](07-cyber-survivability/cyber-survivability-review.md) | Review prevention, degradation, recovery, and adaptation | Survivability review |
| [Cryptographic Change Assurance](12-cryptographic-change-assurance/README.md) | Review bounded cryptographic replacement, withdrawal, and revalidation | Cryptographic Change Decision Pack |
| [High-Impact Systems](08-high-impact-systems/high-impact-system-readiness.md) | Organize deeper evidence for sensitive systems | High-impact readiness package |
| [Incident Review](09-incident-review/incident-review-template.md) | Document incidents, near misses, response, and lessons | Incident review |
| [Examples](10-examples/) | Learn from completed synthetic examples | Example review packages |
| [Assurance Lifecycle Records](11-assurance-lifecycle/) | Complete an end-to-end assurance package | Policy, authority, mapping, validation, and recovery records |

## Examples

- [Synthetic AI Workflow Cyber Review](10-examples/example-ai-workflow-cyber-review.md) demonstrates a completed Quick Review.
- [Synthetic Supplier Assurance](10-examples/synthetic-supplier-assurance/) is a concise partial profile demonstrating AI-assisted evidence review, integrity checking, corrective action, and a human Amber decision. It is not a completed Full Assurance Lifecycle package.
- [Synthetic Cryptographic Withdrawal](10-examples/synthetic-cryptographic-withdrawal/) demonstrates evidence gating, dependency mapping, persistent-state classification, fail-closed Unknown handling, substitution readiness, and a bounded withdrawal exercise.

## Framework alignment

The toolkit can support mapping and readiness work informed by:

- NIST Cybersecurity Framework 2.0
- NIST systems security engineering and cyber-resilience guidance
- NIST cryptographic agility and post-quantum migration guidance
- NIST Zero Trust Architecture
- NIST incident-response guidance
- NIST Secure Software Development Framework and AI profile
- NIST AI Risk Management Framework and Generative AI Profile
- CISA Secure by Design
- OWASP Top 10 for LLM Applications and Generative AI

See [REFERENCES.md](REFERENCES.md) for exact publication titles, versions, statuses, and relevance.

## Repository validation

The repository includes a standard-library-only validator, a small regression suite, and a GitHub Actions workflow.

Run locally:

```bash
python -m unittest discover -s tests -p "test_*.py"
python scripts/refresh_release_metadata.py --root . --check
python scripts/validate_repo.py --root .
sha256sum -c MANIFEST.sha256
```

The validator checks the structural manifest, hashes, internal links, current identity, required template fields, onboarding and AI-assistance guidance, synthetic-example labels, common secret patterns, and public-safety declarations.

Validation confirms the controlled public toolkit structure. It does **not** prove that a private completed review is factually correct, that evidence is sufficient, that a control works in a real environment, or that a system is authorized.

## Scope and limitations

The repository provides reusable documentation, examples, and validation tooling. It does not demonstrate control effectiveness in a real system, production deployment, certification, formal authorization, or independent assessment.

Quick Review is designed for self-guided use. Full Assurance Lifecycle remains expert-led.

See [RELEASE_REVIEW.md](RELEASE_REVIEW.md) for release-specific validation scope and remaining conditions.

## Public-safety boundary

Contributions must be appropriate for public defensive use. Do not post sensitive security details publicly.

High-level defensive analysis may be included when necessary for prevention, detection, investigation, response, recovery, or assurance.

## Contributing and security

- Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes.
- Read [AGENTS.md](AGENTS.md) before using an AI assistant or coding agent.
- Report vulnerabilities through the private reporting process in [SECURITY.md](SECURITY.md).
- Use [DECISION_RUBRIC.md](DECISION_RUBRIC.md) for consistent Green, Amber, Red, and More Evidence Required decisions.

## License

MIT License. Use, adapt, and improve the templates responsibly.

Maintained by Bridge Node 7.
