---
id: a-guardrail-can-be-bypassed-by-encoding
title: A guardrail can be bypassed by encoding
tags: ai, guardrail, encoding
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/ai-guardrail.md
status: active
---
# A guardrail can be bypassed by encoding

## Claim

A regex or classifier guard checks the surface string. Base64, leetspeak, Unicode homoglyphs and translation move the payload past it.

## Test

Take a blocked prompt. Encode it four ways. Send each and check the tool call or the answer.

## Proof

A blocked action succeeds through an encoded form.

## Failure modes

A decoder in the pipeline normalizes it. A model guard can still catch the intent.
