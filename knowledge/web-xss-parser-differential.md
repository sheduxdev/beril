---
id: web-xss-parser-differential
title: XSS survives when two parsers disagree
tags: web, xss, parser
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md, references/ghidra-ecosystem.md
status: active
---
# XSS survives when two parsers disagree

## Claim

A sanitizer, template engine or WAF reads the input with a different parser than the browser. The gap is the payload space.

## Test

Map the sanitizer and the sink. Try mXSS, namespace changes, comment tricks, attribute boundaries and encoding that normalizes late.

## Proof

Script execution in the target origin, with the exact input and browser.

## Failure modes

A payload that fires in an innerHTML test may not fire in the page. A CSP report without execution is not a finding.
