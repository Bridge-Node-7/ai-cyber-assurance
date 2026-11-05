# AI Cyber Assurance

**Organize evidence and make accountable human decisions about AI-enabled and high-impact systems.**

AI Cyber Assurance is a defensive documentation, workflow, and bounded assurance-intelligence toolkit for builders, operators, security reviewers, governance teams, auditors, founders, and system owners. It produces a traceable review package with named owners, bounded claims, visible evidence gaps, accountable decisions, and next actions.

[Latest release](https://github.com/Bridge-Node-7/ai-cyber-assurance/releases/latest) · [START_HERE.md](START_HERE.md) · [Partner](https://bridgenode7.com/partner/)

- **Use it when:** reviewing a workflow, pilot, release, supplier, incident, AI agent, or high-impact system
- **Use it with:** system owners, engineers, security reviewers, operators, governance teams, auditors, founders, and authorized decision owners
- **AI may help with:** organizing, drafting, mapping, questioning, summarizing, checking, and validating structure
- **Humans remain responsible for:** evidence access, fact validation, consequential actions, risk acceptance, and the final assurance decision

> Create a private or access-controlled working package in the environment authorized for your review evidence. Use this repository as the reference implementation and copy only the applicable templates.

## Layout

Numbered directories (`01-` … `13-`) are specialist modules and examples. Start with [`START_HERE.md`](START_HERE.md) to pick Quick Review or Full Assurance Lifecycle, then copy only the templates you need. `scripts/` and `tests/` provide standard-library validators.

## What this connects

```text
Mission → Boundary → Assets and Dependencies → Identities and Authority
→ Threats and Failure Modes → Risk → Security Requirements → Controls
→ Evidence → Validation → Human Decision → Monitoring and Incident Response
→ Recovery → Corrective Action → Retest → Assurance
```

## Assurance Intelligence

[`13-assurance-intelligence/`](13-assurance-intelligence/) adds an optional machine-readable layer for a bounded Assurance Case. One canonical case can be structurally validated and used to generate three consistent views:

```text
Assurance Case
   ├── Decision Receipt
   ├── Assurance Passport
   └── Executive Summary
```

See the [completed synthetic AI-agent assurance case](10-examples/synthetic-ai-agent-assurance/).

## What this produces

- Defined system boundary; review package index; identity and authority record
- Threat-control-evidence map; control validation results; human approval gates
- Recovery evidence; bounded review decision; corrective actions and retest status
- Optionally, one machine-readable Assurance Case and generated communication views

## Five-minute orientation

1. Open [`START_HERE.md`](START_HERE.md)
2. Create a working package where review evidence is authorized to be handled
3. Copy the [Review Package Index](02-evidence-manifests/review-package-index-template.md)
4. Choose Quick Review or Full Assurance Lifecycle; copy only applicable records
5. Record evidence, gaps, owners, and required human decisions
6. Apply the [Decision Rubric](DECISION_RUBRIC.md) and complete the [Review Decision](02-evidence-manifests/review-decision-template.md)
7. Optionally represent the review as an [Assurance Case](13-assurance-intelligence/README.md)

## Choose your path

### Quick Review

One workflow, product, pilot, supplier decision, incident, or release:

```text
Review Package Index → Evidence Manifest → Specialist Module → Decision Rubric → Review Decision
```

1. [Start Here](START_HERE.md)
2. [Review Package Index](02-evidence-manifests/review-package-index-template.md)
3. [Evidence Manifest](02-evidence-manifests/evidence-manifest-template.md)
4. [Decision Rubric](DECISION_RUBRIC.md)
5. [Review Decision](02-evidence-manifests/review-decision-template.md)

### Full Assurance Lifecycle

High-impact, operational, multi-party, or deeply integrated systems: follow [ASSURANCE_LIFECYCLE.md](ASSURANCE_LIFECYCLE.md) after creating the Review Package Index—mission and boundary through validation, accountable decision, corrective action, and retest.

### Structured Assurance Case

Optional representation after scope and path are understood: [Assurance Intelligence](13-assurance-intelligence/README.md).

## Which artifacts apply?

```text
Tool-performing AI or automation?     → AI Agent Security and Human Approval Gates
LLM, retrieval, model, or generation? → LLM and Generative AI Risk Register
Third-party code, models, data, services? → Software and AI Supply Chain Readiness
Material harm from loss or interruption? → Cyber Survivability and Recovery Assurance
Cryptography to replace or revalidate? → Cryptographic Change Assurance
High-impact / multi-party / operational? → Full Assurance Lifecycle
Need one structured evidence-to-decision record? → Assurance Case after path selection
```

## Core doctrine

- Judgment stays human; evidence leads; evidence classes stay explicit (Observed, Tested, Reported, Inferred, Unknown)
- Boundaries are explicit; controls are traceable; recovery is engineered; claims remain bounded

## Specialist modules

| Module | Use it to | Primary output |
|---|---|---|
| [AI Agent Security](01-ai-agent-security/ai-agent-security-checklist.md) | Tool-using agents and human approval boundaries | Agent checklist and approval gates |
| [Evidence Manifests](02-evidence-manifests/evidence-manifest-template.md) | System, evidence, gaps, package status, decision | Package index, evidence manifest, review decision |
| [Zero Trust](03-zero-trust/zero-trust-readiness-map.md) | Identity, access, trust assumptions, visibility | Zero Trust readiness map |
| [LLM Risk](04-llm-risk/llm-risk-register.md) | LLM and generative AI security risks | LLM risk register |
| [Secure by Design](05-secure-by-design/secure-by-design-product-review.md) | Secure defaults and release design | Secure-by-design review |
| [Software Supply Chain](06-software-supply-chain/sbom-readiness.md) | Dependencies, provenance, models, release integrity | Supply-chain readiness review |
| [Cyber Survivability](07-cyber-survivability/cyber-survivability-review.md) | Prevention, degradation, recovery, adaptation | Survivability review |
| [High-Impact Systems](08-high-impact-systems/high-impact-system-readiness.md) | Deeper evidence for sensitive systems | High-impact readiness package |
| [Incident Review](09-incident-review/incident-review-template.md) | Incidents, near misses, response, lessons | Incident review |
| [Examples](10-examples/) | Completed synthetic examples | Example review packages |
| [Assurance Lifecycle Records](11-assurance-lifecycle/) | End-to-end assurance package | Policy, authority, mapping, validation, recovery |
| [Cryptographic Change Assurance](12-cryptographic-change-assurance/README.md) | Cryptographic replacement, withdrawal, revalidation | Cryptographic Change Decision Pack |
| [Assurance Intelligence](13-assurance-intelligence/) | Structured evidence-to-decision case and views | Assurance Case, Decision Receipt, Passport, Summary |

## Examples

- [Synthetic AI Workflow Cyber Review](10-examples/example-ai-workflow-cyber-review.md)
- [Synthetic Supplier Assurance](10-examples/synthetic-supplier-assurance/)
- [Synthetic Cryptographic Withdrawal](10-examples/synthetic-cryptographic-withdrawal/)
- [Synthetic AI Agent Assurance](10-examples/synthetic-ai-agent-assurance/)

## Framework alignment

Mapping and readiness work may be informed by NIST CSF 2.0, NIST systems security engineering and cyber-resilience guidance, NIST C-SCRM, cryptographic agility and post-quantum migration guidance, Zero Trust Architecture, incident-response guidance, SSDF and AI profile, AI RMF and Generative AI Profile, CISA Secure by Design, and OWASP Top 10 for LLM Applications. Exact titles and versions: [REFERENCES.md](REFERENCES.md).

## Validation

```bash
python3 -m unittest discover -s tests -p "test_*.py"
python3 scripts/refresh_release_metadata.py --root . --check
python3 scripts/validate_repo.py --root .
sha256sum -c MANIFEST.sha256
python scripts/validate_assurance_case.py 10-examples/synthetic-ai-agent-assurance/assurance-case.json
```

Use `python3` (3.11+). Validators are standard-library-only for the core gate.

## Assurance boundary

Use the Assurance Case and generated views to organize bounded review evidence and identify unanswered questions. Automated review assistance must follow [`AUTOMATED_REVIEW_GUIDE.md`](AUTOMATED_REVIEW_GUIDE.md).

System certification, deployment authorization, and legal, compliance, privacy, safety, and engineering determinations remain with the qualified processes responsible for them. Control effectiveness rests on supporting evidence. Defensive scope only. See [RELEASE_REVIEW.md](RELEASE_REVIEW.md).

## Contributing and security

- [CONTRIBUTING.md](CONTRIBUTING.md) · [AUTOMATED_REVIEW_GUIDE.md](AUTOMATED_REVIEW_GUIDE.md)
- Private vulnerability reporting: [SECURITY.md](SECURITY.md)
- Decisions: [DECISION_RUBRIC.md](DECISION_RUBRIC.md)

## License

MIT License. Maintained by Bridge Node 7.

## Release

`main` is the current reviewed source. Distribution identity lives on Releases and in CHANGELOG.
