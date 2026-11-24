---
id: mobile-flutter
title: Flutter hides logic in libapp.so and pins in Dart
tags: mobile, flutter, dart
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/mobile-reverse.md
status: active
---
# Flutter hides logic in libapp.so and pins in Dart

## Claim

The Dart snapshot is not readable Java, and pinning can live in Dart or native code. Standard Java hooks miss it.

## Test

Use reFlutter or Blutter. Hook BoringSSL and the Dart socket layer. Compare with a Java-only bypass.

## Proof

A decrypted request or a recovered Dart symbol.

## Failure modes

A successful pinning bypass on a rooted device does not prove a server-side issue.
