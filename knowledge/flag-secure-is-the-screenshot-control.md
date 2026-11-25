---
id: flag-secure-is-the-screenshot-control
title: FLAG_SECURE is the screenshot control
tags: mobile, android, screen
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# FLAG_SECURE is the screenshot control

## Claim

Without FLAG_SECURE, a sensitive screen appears in the recents thumbnail, screenshots and screen recording.

## Test

Open the sensitive screen. Take a screenshot and open recents. Check the window flags in a hook.

## Proof

The secret is visible in the capture.

## Failure modes

The app can mask only part of the screen. A secure flag on one activity does not cover another.
