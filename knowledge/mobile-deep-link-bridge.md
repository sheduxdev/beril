---
id: mobile-deep-link-bridge
title: A deep link plus a JS bridge is a chain
tags: mobile, android, deep-link
confidence: high
updated: 2026-11-24
uses: 0
sources: references/mobile-reverse.md, labs/mobile
status: active
---
# A deep link plus a JS bridge is a chain

## Claim

An exported activity loads an attacker URL into a WebView that exposes a JavaScript bridge. The page can call native methods.

## Test

Read the manifest. Start the deep link with an attacker URL. From the page, call each bridge method and log the result.

## Proof

A token or native action triggered from the attacker page.

## Failure modes

An exported launcher activity is normal. The bug needs a valuable method or data.
