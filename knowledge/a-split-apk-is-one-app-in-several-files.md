---
id: a-split-apk-is-one-app-in-several-files
title: A split APK is one app in several files
tags: android, split, packaging
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/re-android-native.md
status: active
---
# A split APK is one app in several files

## Claim

The base and the config splits are installed together. A patch to one split without the others can break the signature or the load.

## Test

List the splits. Check the signature scheme. Patch one split and reinstall all. Verify the app.

## Proof

A patched split that loads with the matching base.

## Failure modes

A v2 signature covers the whole set. A v3 rotation can change the key.
