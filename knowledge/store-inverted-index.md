---
id: store-inverted-index
title: An inverted index maps a term to postings
tags: search, index, postings
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# An inverted index maps a term to postings

## Claim

The postings list holds document ids and positions. Ranking combines term frequency, rarity and length.

## Test

Index three documents. Query a term. Check the postings and the ranking order.

## Proof

A ranked result that matches the term statistics.

## Failure modes

A stop word list changes recall. A position-less index cannot answer a phrase.
