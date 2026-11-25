---
id: an-audit-policy-with-no-data-plane-is-blind
title: An audit policy with no data plane is blind
tags: k8s, audit, detection
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/ir-container.md
status: active
---
# An audit policy with no data plane is blind

## Claim

An audit policy that omits secrets, exec or token requests hides the credential access and the shell.

## Test

Read the policy rules and the level. Perform an exec and a secret read. Check the audit log.

## Proof

An action with no audit event.

## Failure modes

A metadata level still records the verb. A short retention hides it later.
