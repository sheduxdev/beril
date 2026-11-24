---
id: electron-context-isolation
title: Electron is Node with a browser attached
tags: electron, desktop, context-isolation
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# Electron is Node with a browser attached

## Claim

nodeIntegration is on, contextIsolation is off, or the preload exposes a broad bridge.

## Test

Read BrowserWindow options and the preload. Load an attacker page. Call the exposed API.

## Proof

A Node or file action from a remote page.

## Failure modes

A sandboxed renderer with a narrow preload is safer. A local file page is a different origin.
