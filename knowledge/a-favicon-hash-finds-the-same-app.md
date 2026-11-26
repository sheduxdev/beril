---
id: a-favicon-hash-finds-the-same-app
title: A favicon hash finds the same app
tags: osint, favicon, shodan
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/osint-toolkit.md
status: active
---
# A favicon hash finds the same app

## Claim

The favicon hash is stable across hosts that serve the same product. It is a pivot, not an ownership proof.

## Test

Fetch the favicon. Hash it with the Shodan mmh3 recipe. Search the hash. Compare the title and the cert.

## Proof

A second host with the same hash and a related certificate.

## Failure modes

A default product favicon matches every install. A CDN can rewrite the icon.
