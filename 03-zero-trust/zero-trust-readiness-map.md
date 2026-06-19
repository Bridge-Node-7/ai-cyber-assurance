# Zero Trust Readiness Map

## Purpose

This template helps teams review whether an AI-enabled, mission-critical, or emerging-technology system is moving toward Zero Trust principles.

## Core Question

Does the system continuously verify access instead of assuming trust?

## Identity

- [ ] Every user has a unique identity.
- [ ] Every service or workload has a unique identity where applicable.
- [ ] Privileged access is separated.
- [ ] MFA is enforced where appropriate.
- [ ] Access is reviewed regularly.
- [ ] Break-glass access is documented and monitored.

## Device / Workload

- [ ] Devices are inventoried.
- [ ] Workloads are inventoried.
- [ ] Unknown devices are blocked or limited.
- [ ] Workload permissions are documented.
- [ ] Configuration state is monitored.
- [ ] Unsupported systems are tracked as risk.

## Network / Environment

- [ ] Network access is segmented.
- [ ] Sensitive services are not broadly reachable.
- [ ] Access paths are documented.
- [ ] Remote access is monitored.
- [ ] High-risk paths are approval-gated.
- [ ] External connections are reviewed.

## Application / Tool Access

- [ ] Tools are approved.
- [ ] Tool permissions are scoped.
- [ ] APIs are authenticated.
- [ ] Destructive actions require approval.
- [ ] Tool outputs are validated.
- [ ] AI agents cannot call arbitrary tools.

## Data

- [ ] Sensitive data is identified.
- [ ] Data access is logged.
- [ ] Data sharing is controlled.
- [ ] AI systems are restricted from unnecessary sensitive data.
- [ ] Data retention expectations are documented.
- [ ] Data release decisions are approval-gated.

## Visibility

- [ ] Security logs exist.
- [ ] Logs are reviewed.
- [ ] Anomalies are escalated.
- [ ] Evidence is preserved.
- [ ] Automated actions are traceable.
- [ ] Operators can understand system state.

## Automation Governance

- [ ] Automated actions are bounded.
- [ ] AI agent actions are logged.
- [ ] Human approval gates exist.
- [ ] A disable path or kill switch exists.
- [ ] High-impact decisions remain human-accountable.
- [ ] Model and tool changes are reviewed.

## Readiness Score

Use the 0–5 scoring anchors in [`../DECISION_RUBRIC.md`](../DECISION_RUBRIC.md).

| Domain | Score 0-5 | Notes |
|---|---:|---|
| Identity | | |
| Device / workload | | |
| Network / environment | | |
| Application / tools | | |
| Data | | |
| Visibility | | |
| Automation governance | | |

## Overall Status

Use [`../DECISION_RUBRIC.md`](../DECISION_RUBRIC.md) to keep decision thresholds consistent.

- [ ] Green
- [ ] Amber
- [ ] Red
- [ ] More evidence required

Reviewer:

Date:

Notes:
