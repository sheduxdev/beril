---
id: clipboard-read-needs-a-gesture-and-a-permission
title: Clipboard read needs a gesture and a permission
tags: browser, clipboard, api
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# Clipboard read needs a gesture and a permission

## Claim

A page can read the clipboard after a user gesture or with a granted permission, which exposes copied secrets.

## Test

Copy a marker. Focus the page and call `navigator.clipboard.readText` from a click. Repeat without a gesture.

## Proof

The marker is read.

## Failure modes

A browser prompt and a strict permission block it. A paste event is narrower than a read.
