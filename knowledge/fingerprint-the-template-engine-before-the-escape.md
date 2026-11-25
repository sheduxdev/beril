---
id: fingerprint-the-template-engine-before-the-escape
title: Fingerprint the template engine before the escape
tags: rce, ssti, template
confidence: high
updated: 2026-11-26
uses: 0
sources: references/rce-mastery.md
status: active
---
# Fingerprint the template engine before the escape

## Claim

Arithmetic tells you an engine family, not the engine. String multiplication, division by zero and error text separate Jinja2 from Twig and expose the version.

## Test

Send two expression families. Jinja2 turns 7 times string 7 into 7777777, Twig returns 49. Read the error page for the engine name.

## Proof

Two evaluated expressions and an engine version.

## Failure modes

Client side rendering. A page value that happens to be 49. A sandbox blocks attributes per version.
