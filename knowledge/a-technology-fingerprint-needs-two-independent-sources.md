---
id: a-technology-fingerprint-needs-two-independent-sources
title: A technology fingerprint needs two independent sources
tags: recon, fingerprint, tech
confidence: high
updated: 2026-11-25
uses: 0
sources: references/artex-flask.md
status: active
---
# A technology fingerprint needs two independent sources

## Claim

One header, cookie or body string is weak. A stack claim needs two independent markers, and a version claim needs a version string in the same product context.

## Test

Match header, cookie, meta and body separately. Require two categories before naming the stack. Confirm the version in the banner, not in a changelog link.

## Proof

Two markers from different response parts, or a banner with product and version.

## Failure modes

Shared hosts and reverse proxies copy headers. A stock 404 page carries the framework name. A CDN adds its own cookies.
