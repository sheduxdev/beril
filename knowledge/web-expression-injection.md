---
id: web-expression-injection
title: Expression language injection is eval under a framework name
tags: web, rce, java, el
confidence: high
updated: 2026-11-26
uses: 0
sources: https://cwe.mitre.org/data/definitions/917.html, https://owasp.org/www-community/vulnerabilities/Expression_Language_Injection
status: active
---
# Expression language injection is eval under a framework name

## Claim

User input reaches a SpEL, OGNL, MVEL, JEXL or Jakarta EL evaluator, which can call methods and reach the runtime.

## Test

Grep for `parseExpression`, `ValueStack`, `ELProcessor` and `@Value` built from input. Send an arithmetic probe in a lab.

## Proof

Evaluated arithmetic, then a method call that the context should not allow.

## Failure modes

A `SimpleEvaluationContext` limits SpEL to property access. Struts OGNL bugs are often in the framework, so check the version before the code.
