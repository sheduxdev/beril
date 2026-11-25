---
id: a-sigma-rule-dies-on-the-wrong-logsource
title: A Sigma rule dies on the wrong logsource
tags: detection, sigma, logsource
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/detection-sigma.md, labs/detection
status: active
---
# A Sigma rule dies on the wrong logsource

## Claim

A rule with a service or category the pipeline never fills produces no alert, even when the logic is correct.

## Test

Read the logsource. Compare with the fields the collector emits. Run the rule against a stored sample.

## Proof

The rule fires on a sample and the logsource maps to a real feed.

## Failure modes

A backend can map aliases. A broad category can be expensive but works.
