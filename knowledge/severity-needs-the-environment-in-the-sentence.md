---
id: severity-needs-the-environment-in-the-sentence
title: Severity needs the environment in the sentence
tags: consulting, severity, context
confidence: high
updated: 2026-11-26
uses: 0
sources: references/senior-bar.md, references/scoring.md
status: active
---
# Severity needs the environment in the sentence

## Claim

The same bug is critical on an internet facing admin and low on an isolated lab. A severity without the environment is a guess.

## Test

Name the actor position, the reachable asset and the consequence. Compare two deployments before the score.

## Proof

A severity sentence with all three.

## Failure modes

A CVSS base score hides the environment. A theoretical actor inflates it.
