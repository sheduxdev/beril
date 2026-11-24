---
id: detection-sigma
title: A Sigma rule needs a logsource, a selection and a false-positive note
tags: detection, sigma, log
confidence: high
updated: 2026-11-24
uses: 0
sources: labs/detection
status: active
---
# A Sigma rule needs a logsource, a selection and a false-positive note

## Claim

The rule matches a behavior, not a product string, and states the expected noise.

## Test

Write the logsource and fields. Test against one true positive and one normal day. Add a condition that narrows it.

## Proof

A rule that fires on the true positive and not the baseline.

## Failure modes

A rule that fires on everything is a report. A rule with no logsource cannot deploy.
