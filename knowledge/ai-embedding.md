---
id: ai-embedding
title: An embedding is not anonymized data
tags: ai, embedding, rag
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# An embedding is not anonymized data

## Claim

Vectors can be inverted or used to match documents, and a shared vector store can leak membership.

## Test

Get vectors through an API. Invert or nearest-neighbor. Test cross-user retrieval.

## Proof

A reconstructed phrase or a matching private document.

## Failure modes

A low-dimensional vector may lose detail. A public corpus match is not private.
