---
id: web-csp-bypass
title: CSP is bypassed by a trusted script source, not by a weak directive alone
tags: web, csp, xss
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# CSP is bypassed by a trusted script source, not by a weak directive alone

## Claim

A JSONP endpoint, an allowlisted CDN with a gadget, a base tag, or a reusable nonce gives the attacker script under the policy.

## Test

Read the policy. List every allowed host and scheme. Look for JSONP, Angular, script gadgets and base-uri. Inject a script from an allowed source.

## Proof

Script execution while the CSP header stays unchanged.

## Failure modes

A report-only policy does not block. A missing CSP is a different finding.
