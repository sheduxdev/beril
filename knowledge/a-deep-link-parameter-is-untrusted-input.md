---
id: a-deep-link-parameter-is-untrusted-input
title: A deep link parameter is untrusted input
tags: mobile, deeplink, input
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/mobile-deep-link-bridge.md, labs/mobile
status: active
---
# A deep link parameter is untrusted input

## Claim

A query value from a link can reach a file path, a URL fetch or a WebView load without encoding.

## Test

Trace each link parameter to its sink. Send traversal, an external URL and a javascript URL.

## Proof

A file is read, a fetch is made or script runs in the WebView.

## Failure modes

A parser and an allowlist close it. A parameter that is only displayed has low impact.
