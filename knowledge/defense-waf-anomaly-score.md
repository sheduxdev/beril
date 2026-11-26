---
id: defense-waf-anomaly-score
title: A CRS WAF blocks a score, not an attack
tags: defense, waf, modsecurity, crs
confidence: high
updated: 2026-11-26
uses: 0
sources: https://coreruleset.org/docs/, https://github.com/coreruleset/coreruleset, https://coraza.io/docs/
status: active
---
# A CRS WAF blocks a score, not an attack

## Claim

OWASP CRS adds points per matched rule. A request is blocked when the inbound score passes the threshold (default 5). Paranoia levels 1 to 4 add stricter rules.

## Test

Run in detection-only mode. Collect a week of traffic. Write exclusions per path and parameter, then raise the paranoia level one step.

## Proof

Lab attacks blocked and the baseline passing, at a recorded level and threshold.

## Failure modes

A global exclusion is a hole. A WAF does not fix the sink; it buys time until the patch.
