---
id: root-detection-is-a-set-of-checks
title: Root detection is a set of checks
tags: android, root, detection
confidence: high
updated: 2026-11-26
uses: 0
sources: references/mobile-reverse.md
status: active
---
# Root detection is a set of checks

## Claim

A root check looks for su, Magisk, build tags and mount state. A single hook or a denylist defeats one check.

## Test

List the checks with strings and API calls. Hide each artifact. Run the app after each change.

## Proof

The app reaches the protected screen on a rooted device.

## Failure modes

A hardware backed check is harder. A Play Integrity verdict can override the local checks.
