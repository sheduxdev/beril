---
id: web-upload-validation
title: Upload validation is four separate checks
tags: web, upload, file
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# Upload validation is four separate checks

## Claim

Extension, MIME, magic bytes and the serving path are checked inconsistently, or the stored file is executable.

## Test

Test each check alone. Use a polyglot, double extension, case change, null byte and a traversal filename. Fetch the stored file.

## Proof

A file stored outside the intended type or path, or code execution from it.

## Failure modes

A reflected filename is not traversal. A file served as attachment may not execute.
