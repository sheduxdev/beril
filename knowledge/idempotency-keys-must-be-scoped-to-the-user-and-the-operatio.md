---
id: idempotency-keys-must-be-scoped-to-the-user-and-the-operatio
title: Idempotency keys must be scoped to the user and the operation
tags: api, idempotency, race
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/api-idempotency.md
status: active
---
# Idempotency keys must be scoped to the user and the operation

## Claim

A global key cache lets one user replay another user's request or read the stored response.

## Test

Send a key on user A. Repeat the same key on user B with a different body. Compare the response.

## Proof

User B receives user A's stored response or the operation is skipped.

## Failure modes

A key namespaced by user and route is safe. Server generated keys close it.
