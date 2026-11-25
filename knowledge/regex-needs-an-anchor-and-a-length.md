---
id: regex-needs-an-anchor-and-a-length
title: Regex needs an anchor and a length
tags: lang, regex, validation
confidence: high
updated: 2026-11-26
uses: 0
sources: references/techniques.md
status: active
---
# Regex needs an anchor and a length

## Claim

An unanchored pattern matches a substring. A nested quantifier can backtrack to a timeout.

## Test

Put a valid value before and after garbage. Send a long near miss. Time the match.

## Proof

A match on the garbage or a timeout.

## Failure modes

An anchored pattern and a length cap hold. A linear time engine avoids the timeout.
