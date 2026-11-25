---
id: certificate-pinning-is-bypassed-at-the-trust-call
title: Certificate pinning is bypassed at the trust call
tags: mobile, pinning, frida
confidence: high
updated: 2026-11-26
uses: 0
sources: references/mobile-reverse.md, scripts/frida_hook.js
status: active
---
# Certificate pinning is bypassed at the trust call

## Claim

Pinning fails closed only if every client uses the same pin store. A hook on the trust manager or the pin comparison removes it at runtime.

## Test

Proxy the app. Find the pin failure. Hook the trust manager, the OkHttp pinner or the SHA comparison.

## Proof

The proxy sees decrypted traffic.

## Failure modes

Native pinning and multiple clients need several hooks. A network security config can pin declaratively.
