---
id: web-traversal-canonical-path
title: Traversal is a join before canonicalization
tags: web, file, traversal
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md, references/firmware-iot.md
status: active
---
# Traversal is a join before canonicalization

## Claim

The app joins a user path to a root without resolving and checking the result. Encoded separators and absolute second arguments bypass naive filters.

## Test

Try ../, ..%2f, double encoding, absolute paths, null bytes and Windows separators. Compare the served file with the intended root.

## Proof

A file outside the intended directory is returned or written.

## Failure modes

Reflected filenames are not traversal. A 404 with the path in the body proves nothing.
