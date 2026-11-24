---
id: ai-rag-tenant-filter
title: RAG leaks when retrieval ignores the tenant
tags: ai, llm, rag
confidence: high
updated: 2026-11-24
uses: 0
sources: labs/llm, references/techniques.md
status: active
---
# RAG leaks when retrieval ignores the tenant

## Claim

The retriever ranks chunks across users and filters after generation, or not at all.

## Test

Create two users with distinct documents. Query as A and inspect the retrieved sources and the answer.

## Proof

A document from user B appears in A's answer or source list.

## Failure modes

A shared public doc is not a leak. A model hallucination is not retrieval.
