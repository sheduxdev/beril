---
id: npm-lifecycle-scripts-run-on-install
title: npm lifecycle scripts run on install
tags: supply, npm, postinstall
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/supply-lockfile.md
status: active
---
# npm lifecycle scripts run on install

## Claim

A `preinstall` or `postinstall` script executes with the developer user before any import, so review of the code is not enough.

## Test

Read the scripts block. Install in a disposable container. Watch network and file changes.

## Proof

The script calls out or writes a file during install.

## Failure modes

A lockfile with `ignore-scripts` blocks it. A package can be clean today and change tomorrow.
