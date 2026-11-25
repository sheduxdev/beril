---
id: app-links-verification-is-not-a-custom-scheme
title: App Links verification is not a custom scheme
tags: mobile, deeplink, applinks
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/mobile-deep-link-bridge.md
status: active
---
# App Links verification is not a custom scheme

## Claim

A verified https App Link belongs to one app through asset links. A custom scheme can be registered by any app.

## Test

Read the intent filter and the autoVerify flag. Fetch the assetlinks file. Register the same scheme in a helper app.

## Proof

The helper app receives the link or the asset link is missing or wrong.

## Failure modes

The OS chooser can still show both apps. A verified link with a correct file is bound.
