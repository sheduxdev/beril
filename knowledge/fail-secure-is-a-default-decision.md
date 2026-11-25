---
id: fail-secure-is-a-default-decision
title: Fail secure is a default decision
tags: design, fail-secure, default
confidence: high
updated: 2026-11-26
uses: 0
sources: references/senior-bar.md
status: active
---
# Fail secure is a default decision

## Claim

A check that errors open on a timeout or a missing config grants access by accident.

## Test

Break the policy service, the cache and the config. Call a protected action. Compare with the healthy state.

## Proof

The action is denied when the check is unavailable.

## Failure modes

A degraded read can be acceptable. A fail open logout path can be intended.
