---
id: webhook-urls-are-ssrf-and-secret-theft-at-once
title: Webhook URLs are SSRF and secret theft at once
tags: api, webhook, ssrf
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/api-webhook-signature.md, references/techniques.md
status: active
---
# Webhook URLs are SSRF and secret theft at once

## Claim

A customer supplied webhook URL is fetched by the server. It can reach metadata, internal APIs and the signing secret.

## Test

Register a webhook to a callback you own. Watch headers and body. Then point it at an internal address.

## Proof

The internal response or the signing secret arrives at your listener.

## Failure modes

An allowlist can block internal targets. A queue worker can delay the request.
