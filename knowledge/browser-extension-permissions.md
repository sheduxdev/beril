---
id: browser-extension-permissions
title: An extension is a trusted page with broad APIs
tags: browser, extension, permissions
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# An extension is a trusted page with broad APIs

## Claim

The extension has host permissions, content scripts and message passing. A web page or another extension can send messages.

## Test

Read the manifest. List permissions. Send messages from a page and from another extension. Check externally_connectable.

## Proof

A privileged action or data read from an untrusted sender.

## Failure modes

A permission that is never used is not a finding. Content script isolation matters.
