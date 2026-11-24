---
id: proto-versioning
title: Version negotiation needs a downgrade policy
tags: protocol, versioning, downgrade
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Version negotiation needs a downgrade policy

## Claim

The version is chosen in the handshake. A downgrade to an old version can drop a security feature.

## Test

Offer only an old version. Check the negotiated version and the protected fields.

## Proof

A downgrade that is explicit and logged.

## Failure modes

A silent fallback hides an attack. A version field outside the transcript can be rewritten.
