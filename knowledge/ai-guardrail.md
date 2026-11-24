---
id: ai-guardrail
title: A guardrail is a classifier with an input distribution
tags: ai, guardrail, bypass
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/techniques.md
status: active
---
# A guardrail is a classifier with an input distribution

## Claim

Encoding, length, language or context shifts the input outside the classifier's training distribution.

## Test

Test base64, leetspeak, another language, long context and a benign wrapper. Compare the model output.

## Proof

A policy violation with the guardrail still enabled.

## Failure modes

A refusal is not a bypass. A safe completion is not a violation.
