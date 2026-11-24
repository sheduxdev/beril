---
id: api-grpc-reflection
title: gRPC reflection is a map, per-method auth is the bug
tags: api, grpc, reflection
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# gRPC reflection is a map, per-method auth is the bug

## Claim

The server exposes reflection and descriptors, but individual methods lack authorization or validate only the transport.

## Test

Call reflection, list services, call every method with and without a token. Compare a low-privilege caller.

## Proof

A method returns data or performs an action for the wrong role.

## Failure modes

Reflection enabled is not a finding. A method that is public by design is not either.
