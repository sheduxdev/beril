---
id: electron-with-nodeintegration-is-a-browser-and-a-shell
title: Electron with nodeIntegration is a browser and a shell
tags: browser, electron, rce
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# Electron with nodeIntegration is a browser and a shell

## Claim

A renderer with Node integration gives any script `require` and child process access on the desktop.

## Test

Read the BrowserWindow options. Open DevTools in the app. Run `require('child_process').exec('id')`.

## Proof

A shell command runs from the renderer.

## Failure modes

Context isolation and a preload bridge reduce it. A sandboxed renderer with no bridge is strong.
