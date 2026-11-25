---
id: a-fix-must-close-the-class-not-the-string
title: A fix must close the class, not the string
tags: senior, fix, verification
confidence: high
updated: 2026-11-26
uses: 0
sources: references/senior-bar.md, docs/defending.md
status: active
---
# A fix must close the class, not the string

## Claim

Blocking one payload is a filter. A class level fix changes the sink, the parser or the trust boundary. Test the old payload and two variants after the fix.

## Test

Read the patch. Ask which transform changed. Send the original, a variant and a bypass attempt. Check the regression test.

## Proof

A patch at the sink or boundary and a passing regression test.

## Failure modes

A deny list. A WAF rule with no code change. A fix only on the tested endpoint.
