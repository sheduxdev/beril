---
id: dynamic-code-loading-needs-a-write-path-and-a-loader
title: Dynamic code loading needs a write path and a loader
tags: android, dynamic-code, loader
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/mobile-reverse.md
status: active
---
# Dynamic code loading needs a write path and a loader

## Claim

A dex or a native library from a writable path is code. A path in the app data or the external storage is a drop point.

## Test

Find the loader call and the path. Place a test dex or so. Trigger the load.

## Proof

A class or a symbol from the dropped file.

## Failure modes

A signature check on the file closes it. A scoped storage path can hide the drop.
