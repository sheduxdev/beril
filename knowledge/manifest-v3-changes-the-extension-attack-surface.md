---
id: manifest-v3-changes-the-extension-attack-surface
title: Manifest V3 changes the extension attack surface
tags: browser, extension, mv3
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/browser-extension-permissions.md
status: active
---
# Manifest V3 changes the extension attack surface

## Claim

A service worker replaces the background page, host permissions are narrower and remote code is restricted. The content script bridge remains.

## Test

Read the manifest permissions and the content scripts. Check `externally_connectable` and the message handlers.

## Proof

A web page reaches an extension API or a content script bridge.

## Failure modes

A strict sender check and a narrow match pattern close it. MV2 extensions have a different model.
