---
id: defense-kev-patch-order
title: Patch order follows exploitation evidence, not CVSS alone
tags: defense, patch, kev, epss
confidence: high
updated: 2026-11-26
uses: 0
sources: https://www.cisa.gov/known-exploited-vulnerabilities-catalog, https://www.first.org/epss/, https://www.first.org/cvss/
status: active
---
# Patch order follows exploitation evidence, not CVSS alone

## Claim

CVSS measures severity. CISA KEV lists bugs exploited in the wild, and EPSS estimates exploitation likelihood. Exposure and asset value decide the rest.

## Test

Join the asset inventory to CVEs. Mark KEV entries, then high EPSS, then internet-facing. Compare with a CVSS-only order.

## Proof

A ranked list where every top item is exposed and has exploitation evidence.

## Failure modes

No CVE does not mean no risk. EPSS is a probability, not a guarantee. A missing inventory makes every ranking wrong.
