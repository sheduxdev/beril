---
id: an-implicit-intent-can-be-redirected
title: An implicit intent can be redirected
tags: mobile, android, intent
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/mobile-deep-link-bridge.md
status: active
---
# An implicit intent can be redirected

## Claim

An implicit intent with a URL or an action can be caught by a malicious app that registers the same filter.

## Test

Find the send call. Register the filter in a helper app. Trigger the feature and read the extras.

## Proof

The helper receives the payload.

## Failure modes

An explicit package or a chooser limits it. A custom action only the app uses is narrow.
