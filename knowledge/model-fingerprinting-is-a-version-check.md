---
id: model-fingerprinting-is-a-version-check
title: Model fingerprinting is a version check
tags: ai, model, fingerprint
confidence: low
updated: 2026-11-26
uses: 0
sources: knowledge/ai-model-extraction.md
status: active
---
# Model fingerprinting is a version check

## Claim

Token timing, refusal shape and a fixed probe set can separate model families and sometimes versions without an API field.

## Test

Send a fixed probe set. Record latency, logprobs and answer style. Compare with two known models.

## Proof

A stable profile that matches one family.

## Failure modes

A proxy can mix models. A temperature change moves the style.
