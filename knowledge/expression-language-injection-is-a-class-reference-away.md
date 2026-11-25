---
id: expression-language-injection-is-a-class-reference-away
title: Expression language injection is a class reference away
tags: rce, spel, ognl
confidence: high
updated: 2026-11-26
uses: 0
sources: references/rce-mastery.md
status: active
---
# Expression language injection is a class reference away

## Claim

SpEL and OGNL evaluate type references. A literal expression proves evaluation, a T() or @class@ reference proves reach into the runtime.

## Test

Send the arithmetic form first, then a Runtime getRuntime exec with id. Check both the body and the body parameter path.

## Proof

Class reference evaluation and command output.

## Failure modes

The parameter is not the expression source. A WAF blocks T or Runtime. Double evaluation changes the quoting.
