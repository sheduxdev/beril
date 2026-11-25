---
id: a-javascript-bridge-is-a-native-api-in-the-page
title: A JavaScript bridge is a native API in the page
tags: mobile, webview, bridge
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/mobile-deep-link-bridge.md, labs/mobile
status: active
---
# A JavaScript bridge is a native API in the page

## Claim

`addJavascriptInterface` exposes annotated methods to every page loaded in the WebView, including a page that navigates away.

## Test

List the bridge name and methods. Call them from the page console. Navigate to an attacker page and call again.

## Proof

A native method runs from a page you control.

## Failure modes

A strict allowlist and a navigation guard limit it. A bridge with only safe getters has low impact.
