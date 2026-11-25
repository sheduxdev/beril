---
id: a-rag-citation-is-not-a-verified-source
title: A RAG citation is not a verified source
tags: ai, rag, citation
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# A RAG citation is not a verified source

## Claim

The model can cite a document it did not use or misquote one it did. The citation field proves a link, not the claim.

## Test

Ask for a claim with a citation. Open the cited chunk and compare. Repeat with a distractor document.

## Proof

A citation that does not contain the claim or a quote that is absent.

## Failure modes

A reranker with a quote check helps. A short chunk can be ambiguous.
