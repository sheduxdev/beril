---
id: web-ssrf-parser-differential
title: SSRF hides in URL parser disagreement
tags: web, ssrf, parser
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md, references/rust-reverse.md
status: active
---
# SSRF hides in URL parser disagreement

## Claim

One component validates a URL and another fetches it. Different parsers disagree about host, scheme, userinfo or path.

## Test

Use a listener to confirm the fetch. Test http:///host, backslashes, userinfo, encoded delimiters, IPv4-mapped IPv6, decimal IPs, redirects and DNS rebinding.

## Proof

A callback from the target, or a response body from an internal service.

## Failure modes

DNS-only SSRF is weak without exfiltration. A hit on your listener does not prove the response reaches the attacker.
