---
id: input-validation-and-output-encoding-are-two-layers
title: Input validation and output encoding are two layers
tags: design, input, output
confidence: high
updated: 2026-11-26
uses: 0
sources: references/techniques.md
status: active
---
# Input validation and output encoding are two layers

## Claim

A validator on input cannot cover every output context. A value can be safe in JSON and dangerous in HTML or a shell.

## Test

Send a value with markup and metacharacters. Read it in HTML, an attribute, a URL, a shell and a log.

## Proof

One context where the value changes meaning.

## Failure modes

A context aware encoder closes the output side. A parser can normalize the input.
