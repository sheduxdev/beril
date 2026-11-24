---
id: secrets-verified
title: A secret is a finding only after a read-only proof
tags: supply-chain, secret, verification
confidence: high
updated: 2026-11-24
uses: 0
sources: references/tooling.md
status: active
---
# A secret is a finding only after a read-only proof

## Claim

A key or token is in the repo, but its scope and liveness are unknown.

## Test

Identify the provider. Call a read-only identity or list endpoint. Check the scope and expiry.

## Proof

A successful read-only API response with the key's permissions.

## Failure modes

A public client key may be intended. A revoked key is a false positive.
