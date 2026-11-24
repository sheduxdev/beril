---
id: eng-slo
title: An SLO is a budget for unreliability
tags: engineering, sre, slo
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# An SLO is a budget for unreliability

## Claim

An SLO names the indicator, the target and the window. The error budget decides how fast to ship.

## Test

Define the SLI. Measure. Set the alert on burn rate, not a raw threshold.

## Proof

An alert that fires before the budget is gone.

## Failure modes

A 100% target leaves no room to deploy.
