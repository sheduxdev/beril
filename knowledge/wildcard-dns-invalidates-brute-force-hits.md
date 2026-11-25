---
id: wildcard-dns-invalidates-brute-force-hits
title: Wildcard DNS invalidates brute-force hits
tags: recon, dns, wildcard
confidence: high
updated: 2026-11-25
uses: 0
sources: references/artex-flask.md
status: active
---
# Wildcard DNS invalidates brute-force hits

## Claim

When a random label resolves, every wordlist hit also resolves. A hit counts only after an HTTP or content check separates the default app from a real host.

## Test

Resolve a random 12 character label first. If it answers, compare the address and body of each wordlist hit with the wildcard baseline.

## Proof

A different address or a clearly different body and title.

## Failure modes

A catch-all app can serve unique content per name. The wildcard check then produces false negatives, not false positives.
