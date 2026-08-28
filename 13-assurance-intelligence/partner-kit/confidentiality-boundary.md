# Confidentiality Boundary

> **Artifact type:** PARTNER GUIDE  
> **Completion status:** Reference document  
> **Operational authority:** None

AI Cyber Assurance is a public defensive toolkit. Real partner assurance work should use a separate private or access-controlled workspace.

## Appropriate for the public repository

- methodology;
- schemas;
- validation logic;
- rendering logic;
- blank templates;
- fictional synthetic examples;
- public references.

## Keep in the private partner workspace

- real system architecture;
- customer or partner identities;
- private supplier information;
- bills of materials;
- private telemetry or logs;
- vulnerabilities not approved for disclosure;
- credentials or secrets;
- regulated or personal data;
- proprietary evidence;
- real decision records unless deliberately approved for public release.

## Reference pattern

A public or reusable case structure may reference controlled evidence by stable identifier and bounded metadata, but should not copy the sensitive evidence itself.

## Publication gate

Publication is a consequential action. Material must be explicitly approved for unrestricted release before it enters this repository.
