# Synthetic AI Workflow Cyber Review
> **Artifact type:** COMPLETED SYNTHETIC EXAMPLE  
> **Operational authority:** None  
> **Coverage:** Completed Quick Review

## Example Status

**Synthetic / fictional example.**

This example does not describe a real person, customer, employer, system, repository, provider, deployment, or security finding. It demonstrates the **Quick Review** path.

## System / Workflow

A fictional AI-assisted document review workflow retrieves documents from a controlled repository, summarizes selected content, proposes classifications, and sends outputs to a human approval queue.

## Mission

Reduce repetitive review time while preserving data boundaries, traceability, and accountable human decisions.

## Quick Review Path

```text
Evidence Manifest
→ AI Agent Security
→ LLM Risk
→ Human Approval Gates
→ Review Decision
```

## System Boundary

### In Scope

- User authentication
- AI-agent identity
- Document retrieval
- Prompt and retrieval handling
- Tool permissions
- Output review
- Human approval
- Logging and evidence retention

### Out of Scope

- Real customer information
- Production infrastructure
- Real credentials
- Proprietary prompts
- External legal or compliance conclusions

## Identities and Authority

| Identity | Class | Permitted Authority | Prohibited Authority | Owner |
|---|---|---|---|---|
| Fictional reviewer | Human | Select source documents; approve or reject output | Self-approve privileged access changes | Review lead |
| Fictional AI review agent | Nonhuman workload | Read approved documents; draft summaries and classifications | Publish, delete, grant access, or change source records | Product owner |
| Fictional repository service | Service identity | Return authorized documents | Expand access based on AI output | Platform owner |

## Key Risks

| Risk | Consequence | Preventive Control | Detective Control | Corrective / Recovery Control | Evidence ID |
|---|---|---|---|---|---|
| Prompt injection in retrieved content | Agent follows untrusted instructions | Separate instructions from retrieved data; restrict tools | Log prompt, retrieval, and tool activity | Stop session; quarantine source; review output | E-001 |
| Sensitive information disclosure | Unauthorized exposure | Data minimization and access control | Output and access review | Revoke session; remove output; investigate | E-002 |
| Excessive agency | Unauthorized external action | Read-only tool scope; no publication authority | Tool-call monitoring | Disable agent identity; revert workflow | E-003 |
| Unsupported classification | Incorrect decision support | Require source citation and reviewer approval | Sample review and disagreement tracking | Correct result; update instructions; retest | E-004 |
| Provider or dependency change | Unexpected behavior | Version inventory and change control | Change detection | Roll back approved configuration | E-005 |

## Evidence Summary

| Evidence ID | Evidence | Status | Limitation |
|---|---|---|---|
| E-001 | Synthetic prompt and retrieval log sample | Available | Demonstrates format, not production operation |
| E-002 | Fictional access-control review | Available | Self-reviewed |
| E-003 | Fictional read-only tool manifest | Available | Not independently tested |
| E-004 | Synthetic reviewer comparison | Available | Small demonstration sample |
| E-005 | Fictional version record and rollback note | Partial | Recovery not executed |

## Human Approval Gates

Human approval is required before:

- Publishing or externally distributing output
- Expanding document access
- Changing agent tools or privileges
- Accepting residual risk
- Declaring a security incident
- Making legal, compliance, attribution, or customer-notification decisions

## Review Decision

**Amber — proceed only as a controlled pilot with conditions.**

Conditions:

1. Maintain read-only agent tools.
2. Require human approval before output leaves the review queue.
3. Complete an executed rollback test.
4. Retain logs for the agreed review period.
5. Reassess after any model, provider, retrieval, or tool change.

## What This Example Proves

It proves only that the repository templates can organize a fictional review into traceable risks, controls, evidence, conditions, and human authority.

It does not prove system security, control effectiveness, production readiness, certification, or independent validation.
