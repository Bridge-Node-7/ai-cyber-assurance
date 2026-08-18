# Cryptographic Change Assurance

> **Artifact type:** NAVIGATOR
> **Completion status:** Reference document
> **Required for:** Reviews where approved cryptography may need to be replaced, withdrawn, or revalidated

Cryptographic Change Assurance helps teams determine what is affected when a cryptographic primitive, protocol profile, implementation, provider, key or trust configuration, or governing policy changes.

Use this module to connect a bounded change trigger to evidence, dependencies, persistent state, substitution readiness, verification, and an accountable human decision.

## Start Here

1. Create or update the [Review Package Index](../02-evidence-manifests/review-package-index-template.md).
2. Record the triggering evidence in the [Evidence Manifest](../02-evidence-manifests/evidence-manifest-template.md).
3. Apply the [Cryptographic Evidence Gate](cryptographic-evidence-gate.md).
4. Complete the [Cryptographic Change Review](cryptographic-change-review.md).
5. Run a bounded [Withdrawal Exercise](withdrawal-exercise.md).
6. Assemble the [Cryptographic Change Decision Pack](cryptographic-change-decision-pack.md).
7. Apply the repository [Decision Rubric](../DECISION_RUBRIC.md) and record the final decision in the [Review Decision](../02-evidence-manifests/review-decision-template.md).

## Core Flow

```text
Change trigger
→ Evidence gate
→ Cryptographic dependencies
→ State mobility
→ Blast radius
→ Substitution readiness
→ Time to Safe Substitution
→ Pre-cutover review
→ Withdrawal exercise
→ Verification
→ Decision Pack
→ Human decision
→ Reassessment
```

## Use It When

Use the module when one or more of these conditions can materially affect the approved cryptographic state:

- an algorithm, parameter set, protocol profile, implementation, or provider is deprecated or withdrawn;
- a cryptographic finding requires scoped technical review;
- a key, certificate, trust store, trust anchor, or signing configuration changes;
- a standards, policy, support, or architecture change requires migration;
- a system must demonstrate that a replacement path is testable and recoverable.

## Key Rules

- **Evidence is scoped.** A finding about one construction, parameter set, implementation, or test condition does not automatically apply to another.
- **Unknown stays unknown.** Missing dependency or state information does not become favorable evidence.
- **Persistent state is explicit.** Affected data must have a state-mobility class or remain an open blocker.
- **No aggregate blast-radius score.** Report material dimensions separately so one favorable area cannot hide a critical weakness.
- **Time to Safe Substitution is defender-controlled.** Use measured or bounded change stages; do not present an adversary timeline as a known fact.
- **No silent fallback.** A proposed transition must not silently restore cryptography that the approved policy disallows.
- **Judgment stays human.** AI and automation may assist review and validation but do not authorize production cryptographic changes.

## Time to Safe Substitution

Time to Safe Substitution, or **TSS**, is the total defender-controlled time needed to move from a validated change trigger to a verified acceptable state:

```text
TSS =
  evidence intake
+ validation
+ decision and authorization
+ preparation
+ staging
+ cutover
+ persistent-state migration
+ verification
```

If a material stage cannot be measured or bounded, report TSS as **Unknown** rather than inventing precision.

## Public-Safety Boundary

This public module is a defensive review method. It does not authorize scanning, exploitation, key rotation, trust-store modification, production cutover, or any other live-system change.

Keep real keys, credentials, customer data, sensitive architecture, nonpublic vulnerabilities, proprietary evidence, and operational details in an approved private or access-controlled environment.
