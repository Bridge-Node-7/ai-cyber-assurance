# AI Cyber Assurance

**Public-safe assurance templates and validation workflows for AI-enabled systems, agentic operations, emerging technology, and high-impact environments.**

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

1. Copy the [Evidence Manifest](02-evidence-manifests/evidence-manifest-template.md).
2. Define the system, scope, owner, and decision to be made.
3. Select one or more [specialist modules](#specialist-modules).
4. Record the evidence supporting each material control.
5. Apply the [Decision Rubric](DECISION_RUBRIC.md) and complete the [Review Decision](02-evidence-manifests/review-decision-template.md).

## Choose your path

### Quick Review

Use this path for one workflow, product, pilot, or release:

```text
Evidence Manifest
→ Relevant Specialist Module
→ Decision Rubric
→ Review Decision
```

Start here:

1. [Evidence Manifest](02-evidence-manifests/evidence-manifest-template.md)
2. [Decision Rubric](DECISION_RUBRIC.md)
3. [Review Decision](02-evidence-manifests/review-decision-template.md)

### Full Assurance Lifecycle

Use this path for high-impact, operational, multi-party, or deeply integrated systems:

1. Open the [Assurance Lifecycle](ASSURANCE_LIFECYCLE.md).
2. Define mission, boundary, assets, dependencies, and evidence.
3. Record identities and authority.
4. Identify threats, failure modes, risk, and uncertainty.
5. Establish the security policy, target, and requirements.
6. Map controls to evidence.
7. Validate controls, monitoring, response, and recovery.
8. Make an accountable human decision.
9. Track corrective action and retest.

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
| [Evidence Manifests](02-evidence-manifests/evidence-manifest-template.md) | Define the system, evidence, gaps, and decision | Evidence manifest and review decision |
| [Zero Trust](03-zero-trust/zero-trust-readiness-map.md) | Review identity, access, trust assumptions, and visibility | Zero Trust readiness map |
| [LLM Risk](04-llm-risk/llm-risk-register.md) | Track LLM and generative AI security risks | LLM risk register |
| [Secure by Design](05-secure-by-design/secure-by-design-product-review.md) | Review secure defaults and release design | Secure-by-design review |
| [Software Supply Chain](06-software-supply-chain/sbom-readiness.md) | Review dependencies, provenance, models, and release integrity | Supply-chain readiness review |
| [Cyber Survivability](07-cyber-survivability/cyber-survivability-review.md) | Review prevention, degradation, recovery, and adaptation | Survivability review |
| [High-Impact Systems](08-high-impact-systems/high-impact-system-readiness.md) | Organize deeper evidence for sensitive systems | High-impact readiness package |
| [Incident Review](09-incident-review/incident-review-template.md) | Document incidents, near misses, response, and lessons | Incident review |
| [Examples](10-examples/) | Learn from completed synthetic examples | Example review packages |
| [Assurance Lifecycle Records](11-assurance-lifecycle/) | Complete an end-to-end assurance package | Policy, authority, mapping, validation, and recovery records |

## Examples

- [Synthetic AI Workflow Cyber Review](10-examples/example-ai-workflow-cyber-review.md) demonstrates a completed Quick Review.
- [Synthetic Supplier Assurance](10-examples/synthetic-supplier-assurance/) is a concise partial profile demonstrating AI-assisted evidence review, integrity checking, corrective action, and a human Amber decision. It is not a completed Full Assurance Lifecycle package.

## Framework alignment

The toolkit can support mapping and readiness work informed by:

- NIST Cybersecurity Framework 2.0
- NIST systems security engineering and cyber-resilience guidance
- NIST Zero Trust Architecture
- NIST incident-response guidance
- NIST Secure Software Development Framework and AI profile
- NIST AI Risk Management Framework and Generative AI Profile
- CISA Secure by Design
- OWASP Top 10 for LLM Applications and Generative AI

See [REFERENCES.md](REFERENCES.md) for exact publication titles, versions, statuses, and relevance.

## Repository validation

The repository includes a standard-library-only validator and a GitHub Actions workflow.

Run locally:

```bash
python scripts/validate_repo.py --root .
```

The validator checks the structural manifest, hashes, internal links, current identity, required template fields, synthetic-example labels, common secret patterns, and public-safety declarations.

## Scope and limitations

The repository provides reusable documentation, examples, and validation tooling. It does not demonstrate control effectiveness in a real system, production deployment, certification, formal authorization, or independent assessment.

See [RELEASE_REVIEW.md](RELEASE_REVIEW.md) for release-specific validation scope and remaining conditions.

## Public-safety boundary

Contributions must not include malware code, weaponization instructions, harmful deployment procedures, persistence or evasion guidance, credential-theft workflows, exploit-enabling operational details, secrets, private keys, customer data, proprietary material, or sensitive infrastructure information.

High-level defensive analysis may be included when necessary for prevention, detection, investigation, response, recovery, or assurance.

## Contributing and security

- Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes.
- Report vulnerabilities through the private reporting process in [SECURITY.md](SECURITY.md).
- Use [DECISION_RUBRIC.md](DECISION_RUBRIC.md) for consistent Green, Amber, Red, and More Evidence Required decisions.

## License

MIT License. Use, adapt, and improve the templates responsibly.

Maintained by Bridge Node 7.
