---
id: uploaded-svg-is-active-content-when-served-inline
title: Uploaded SVG is active content when served inline
tags: web, upload, xss
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/web-upload-validation.md, references/techniques.md
status: active
---
# Uploaded SVG is active content when served inline

## Claim

An SVG with a script, served as image/svg+xml without attachment, executes on the app origin.

## Test

Upload an SVG with a script and an onload. Fetch it directly and check Content-Type and disposition.

## Proof

The script runs on the target origin.

## Failure modes

Attachment headers or a separate asset domain stop it. A sanitizer strips the script.
