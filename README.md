# AI Cyber Defense OS

**Open-source cyber governance, verification, and secure-by-design templates for AI-enabled systems, agentic workflows, emerging technology, and high-impact environments.**

**Bridge Node 7 — Verification & Validation Layer for AI-Era Cyber Governance**

## Mission

AI and autonomous systems are becoming operational infrastructure. Cybersecurity must now govern not only networks and applications, but also agents, prompts, tools, models, data flows, software supply chains, identity systems, and human decision loops.

**AI Cyber Defense OS** provides public-safe, defensive templates and workflows that help teams:

- Map cybersecurity controls to real operational decisions
- Review AI-agent and LLM risks before deployment
- Document verifiable evidence for review and audit
- Verify secure-by-design practices
- Prepare Zero Trust readiness packages
- Reduce unsafe automation and excessive agency
- Keep humans accountable for high-impact decisions
- Support trustworthy AI and emerging-technology governance

**Tagline:** Cybersecurity for the age of AI automation: verified, explainable, human-governed.

## What This Is

A defensive cybersecurity and governance toolkit for builders, operators, founders, students, auditors, product teams, and reviewers who need practical, auditable cyber documentation for AI-enabled and emerging-technology systems.

This repository focuses on **verification, validation, evidence, and governance**. It helps teams move from static security language to operationally usable cyber readiness.

## What This Is Not

This repository does **not** provide offensive exploit instructions, malware, credential theft methods, unauthorized access techniques, or sensitive operational procedures. Everything here is public-safe and focused on defensive cybersecurity, secure design, review workflows, and accountable deployment.

This repository does **not** claim certification, formal authorization, production deployment maturity, or endorsement by any external organization.

## How to Use This Repository

Start with the system, asset, or workflow you want to review. The numbered folders are **not** a mandatory sequence; they are independent modules you can use as needed.

**First action for most users:** open `02-evidence-manifests/evidence-manifest-template.md` and fill it out for your system. Then use the other modules as needed.

1. **Define the asset.** Name the system, owner, purpose, boundary, connected systems, and data handled.
2. **Choose the relevant modules.** Use AI Agent Security for tool-using agents, Evidence Manifests for review packages, Zero Trust for access assumptions, LLM Risk for model-enabled workflows, and High-Impact Systems for sensitive or operational workflows.
3. **Apply the shared decision rubric.** Use [`DECISION_RUBRIC.md`](DECISION_RUBRIC.md) to keep Green, Amber, Red, and More Evidence Required decisions consistent.
4. **Capture evidence.** Record what was reviewed, what is known, what is assumed, what remains open, and who owns each action.
5. **Make the smallest defensible decision.** Proceed, proceed with constraints, stop, or request more evidence.

Recommended first three modules for any new AI-enabled system or workflow:

```text
02-evidence-manifests/evidence-manifest-template.md
01-ai-agent-security/ai-agent-security-checklist.md
04-llm-risk/llm-risk-register.md
```

Recommended starter path for a fuller review:

```text
02-evidence-manifests/evidence-manifest-template.md
01-ai-agent-security/ai-agent-security-checklist.md
04-llm-risk/llm-risk-register.md
03-zero-trust/zero-trust-readiness-map.md
05-secure-by-design/secure-by-design-product-review.md
```

For public release, also review:

```text
06-software-supply-chain/sbom-readiness.md
07-cyber-survivability/cyber-survivability-review.md
09-incident-review/incident-review-template.md
RELEASE_REVIEW.md
```

## Core Philosophy

- Judgment stays human.
- Evidence leads.
- Security becomes understandable.
- AI becomes governable.
- Trust becomes verifiable.

## Framework Alignment

This toolkit is designed to support mapping and readiness work related to:

- NIST Cybersecurity Framework 2.0
- NIST Secure Software Development Framework (SSDF)
- CISA Secure by Design guidance
- OWASP Top 10 for LLM Applications and Generative AI
- Zero Trust principles: continuous verification, least privilege, assume breach
- Cyber survivability and resilience concepts
- Evidence-based readiness workflows for AI-enabled and high-impact systems

See [`REFERENCES.md`](REFERENCES.md) for public framework references.

## Repository Structure

```text
ai-cyber-defense-os/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── DECISION_RUBRIC.md
├── RELEASE_REVIEW.md
├── REFERENCES.md
├── REPO_MANIFEST.json
│
├── 01-ai-agent-security/
│   ├── ai-agent-security-checklist.md
│   └── human-approval-gates.md
├── 02-evidence-manifests/
│   ├── evidence-manifest-template.md
│   └── review-decision-template.md
├── 03-zero-trust/
│   └── zero-trust-readiness-map.md
├── 04-llm-risk/
│   └── llm-risk-register.md
├── 05-secure-by-design/
│   └── secure-by-design-product-review.md
├── 06-software-supply-chain/
│   └── sbom-readiness.md
├── 07-cyber-survivability/
│   └── cyber-survivability-review.md
├── 08-high-impact-systems/
│   └── high-impact-system-readiness.md
├── 09-incident-review/
│   └── incident-review-template.md
└── 10-examples/
    └── example-ai-workflow-cyber-review.md
```

## Core Modules

### 1. AI Agent Security

Checklist-based review for agents, copilots, workflow automations, and tool-using AI systems. Covers identity, tool permissions, prompt-injection risk, sensitive data exposure, human approval gates, logging, and deployment decision status.

### 2. Evidence Manifests

Structured evidence packages that define system boundaries, connected systems, data handled, control status, risks, assumptions, and decision gates. Useful for audits, readiness reviews, internal governance, release preparation, and product reviews.

### 3. Zero Trust Readiness

A practical mapping template for identity, devices/workloads, applications, tools, data, visibility, and automation governance. Designed to help teams identify where trust is assumed and where continuous verification is needed. Use the scoring anchors in `DECISION_RUBRIC.md` for repeatable 0–5 scoring.

### 4. LLM Risk Register

A public-safe risk register for LLM-enabled systems. Tracks OWASP-aligned risks such as prompt injection, sensitive information disclosure, supply-chain exposure, data/model poisoning, improper output handling, excessive agency, system prompt leakage, vector/embedding weakness, misinformation, and unbounded consumption.

### 5. Secure-by-Design Product Review

A review workflow for product teams to document secure defaults, transparency, vulnerability handling, AI-specific design constraints, and release-readiness decisions.

### 6. Software Supply Chain Review

Templates for dependency review, SBOM readiness, release security, provenance checks, and open-source hygiene.

### 7. Cyber Survivability Review

A resilience-oriented review template for preventing, mitigating, and recovering from cyber disruption without exposing sensitive implementation details.

### 8. High-Impact Systems Readiness

A starter template for sensitive or operational workflows where reliability, access control, data integrity, rollback, recovery, and human approval gates matter.

### 9. Incident Review

A structured incident and near-miss review template for documenting impact, timeline, contributing factors, response, recovery, lessons learned, and control improvements.

### 10. Examples

Synthetic, public-safe examples showing how the templates can be applied without exposing real customer, employer, proprietary, or operational data.

## Technology Readiness

This repository is a documentation and workflow foundation. It is not a validated operational system, a certified control set, or a production security product.

Before making stronger maturity claims, create a validation artifact with reviewer, date, environment, scope, test method, findings, and evidence trail.

## Release Evidence

This release includes [`RELEASE_REVIEW.md`](RELEASE_REVIEW.md), a self-review using the repository's public-safety, secure-by-design, and release-readiness criteria.

The review is a self-assessment, not an independent audit. It exists to make the release decision traceable.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Contributions should improve clarity, evidence quality, public safety, repeatability, and defensive value. Contributions must not add offensive exploit content, credential theft workflows, malware behavior, or sensitive operational procedures.

## License

MIT License — use, fork, adapt, and deploy these templates responsibly.

---

**Bridge Node 7 — a verification layer for AI-era cyber governance.**
