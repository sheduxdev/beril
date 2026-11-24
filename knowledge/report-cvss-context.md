---
id: report-cvss-context
title: CVSS without business context misranks the bug
tags: process, report, cvss
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/scoring.md
status: active
---
# CVSS without business context misranks the bug

## Claim

The vector scores the mechanism, not the asset value or the attacker position.

## Test

Write the impact first. Set the vector from the real precondition. Explain the business asset in one sentence.

## Proof

A score a triager accepts because the narrative matches it.

## Failure modes

A high score on a staging host oversells. A low score on production data undersells.
