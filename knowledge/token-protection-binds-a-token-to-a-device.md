---
id: token-protection-binds-a-token-to-a-device
title: Token protection binds a token to a device
tags: idp, token-protection, binding
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# Token protection binds a token to a device

## Claim

A bound token needs the device key and fails on a replay from another host. An unbound token is a bearer secret.

## Test

Read the token binding and the policy. Replay the token from a second host. Compare with the bound state.

## Proof

A token failure on the second host.

## Failure modes

A policy in report only mode allows it. A stolen device key defeats the binding.
