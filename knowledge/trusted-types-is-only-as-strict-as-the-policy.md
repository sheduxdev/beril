---
id: trusted-types-is-only-as-strict-as-the-policy
title: Trusted Types is only as strict as the policy
tags: browser, trusted-types, xss
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/web-csp-bypass.md
status: active
---
# Trusted Types is only as strict as the policy

## Claim

A policy that passes strings through or a sink that accepts both types keeps the injection path.

## Test

Read the policy functions. Find a sink that accepts a string. Inject a payload through it.

## Proof

The payload reaches the DOM without a violation.

## Failure modes

A default policy that sanitizes and required sinks close it. A partial rollout leaves old paths.
