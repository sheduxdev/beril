---
id: feed-dedup-needs-the-canonical-indicator
title: Feed dedup needs the canonical indicator
tags: ti, feed, dedup
confidence: high
updated: 2026-11-26
uses: 0
sources: references/scoring.md
status: active
---
# Feed dedup needs the canonical indicator

## Claim

The same domain appears with a trailing dot, a case change and a URL. Canonicalize before the dedup or the feed doubles.

## Test

Normalize case, trailing dot, scheme and path. Hash the canonical form. Compare the counts.

## Proof

A stable canonical key and a lower duplicate count.

## Failure modes

A path can be significant. A wildcard can change the meaning.
