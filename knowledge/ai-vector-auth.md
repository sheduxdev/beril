---
id: ai-vector-auth
title: A vector query still needs an ACL
tags: ai, rag, vector
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# A vector query still needs an ACL

## Claim

Embedding search returns nearest chunks, not authorized chunks. Metadata filtering is the authorization layer.

## Test

Create two users with separate documents. Query as A. Inspect source ids and metadata. Test a filter bypass with a crafted query.

## Proof

A chunk from user B appears in A's sources.

## Failure modes

A shared public corpus is not a leak. A filter without a tenant field is decorative.
