---
id: a-threat-model-names-one-boundary-and-one-control
title: A threat model names one boundary and one control
tags: design, threat-model, control
confidence: high
updated: 2026-11-26
uses: 0
sources: references/senior-bar.md
status: active
---
# A threat model names one boundary and one control

## Claim

A model that maps every box hides the boundary that matters. One actor, one asset and one missing control drive the test plan.

## Test

Draw the data flow. Pick the boundary with the highest value and the weakest check. Name the control that should exist.

## Proof

A one page model with the chosen boundary and the test.

## Failure modes

A system can have several equal boundaries. A model goes stale after a design change.
