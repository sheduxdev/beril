---
id: host-header-poisoning-reaches-reset-links-and-caches
title: Host header poisoning reaches reset links and caches
tags: web, host-header, reset
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/web-host-header-reset.md, references/techniques.md
status: active
---
# Host header poisoning reaches reset links and caches

## Claim

When the app builds absolute URLs from the Host header, an attacker host lands in the reset mail or the cache.

## Test

Send a reset with a custom Host and with X-Forwarded-Host. Compare the link in the mail.

## Proof

The reset link points at the attacker host.

## Failure modes

A configured canonical host blocks it. A proxy can rewrite Host.
