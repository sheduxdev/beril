---
id: a-rule-needs-a-clean-day-baseline
title: A rule needs a clean day baseline
tags: detection, false-positive, baseline
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/detection-sigma.md, references/senior-bar.md
status: active
---
# A rule needs a clean day baseline

## Claim

False positive rate is measured against normal activity. Without a clean day the rule is untested for noise.

## Test

Run the rule on seven normal days. Count alerts. Sample ten and label each.

## Proof

A measured rate and a tuning change that lowers it.

## Failure modes

A quiet week misses the noisy event. A test environment differs from production.
