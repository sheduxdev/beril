---
id: a-lolbin-is-a-signed-loader
title: A LOLBin is a signed loader
tags: red, lolbin, execution
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/detection-lolbins.md
status: active
---
# A LOLBin is a signed loader

## Claim

A signed system binary with a download or a script flag runs code without a dropped tool, and the parent is the detection.

## Test

Pick a binary with a download or a script flag. Run a callback. Check the parent and the command line in the log.

## Proof

A callback and the log line.

## Failure modes

An application allowlist can block the binary. A proxy can inspect the download.
