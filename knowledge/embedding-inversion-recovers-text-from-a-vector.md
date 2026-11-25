---
id: embedding-inversion-recovers-text-from-a-vector
title: Embedding inversion recovers text from a vector
tags: ai, embedding, privacy
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/ai-embedding.md
status: active
---
# Embedding inversion recovers text from a vector

## Claim

A stored vector keeps enough signal to reconstruct words and names, so a vector store is personal data under many regimes.

## Test

Embed a sentence with a known model. Run an inversion method or compare nearest neighbors. Recover the topic and a name.

## Proof

A reconstructed phrase from the vector alone.

## Failure modes

A short or generic sentence is hard. A model change invalidates the inversion.
