---
id: ai-data-poison
title: Poisoned data changes the model or the retrieval set
tags: ai, data, poisoning
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# Poisoned data changes the model or the retrieval set

## Claim

An attacker can add documents, feedback or training samples that later influence an answer or a tool call.

## Test

Add a document with a unique claim or instruction. Ask a related question. Check whether retrieval or training picks it up.

## Proof

A later answer repeats the planted claim or follows the instruction.

## Failure modes

A one-off prompt is not poisoning. The data must persist and be retrieved.
