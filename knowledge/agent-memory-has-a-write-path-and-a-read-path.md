---
id: agent-memory-has-a-write-path-and-a-read-path
title: Agent memory has a write path and a read path
tags: ai, memory, poison
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/ai-memory-poison.md
status: active
---
# Agent memory has a write path and a read path

## Claim

Long term memory is a store the model writes from untrusted content and reads later. A poisoned write survives the session.

## Test

Teach the agent a false fact through a document. Start a new session. Ask a question that uses the memory.

## Proof

The false fact returns in a later session.

## Failure modes

A memory with a source label and a TTL limits it. A summary step can drop the poison.
