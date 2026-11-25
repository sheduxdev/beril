---
id: npm-lifecycle-scripts-are-the-install-surface
title: npm lifecycle scripts are the install surface
tags: pkg, npm, postinstall
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/supply-lockfile.md
status: active
---
# npm lifecycle scripts are the install surface

## Claim

`preinstall`, `install` and `postinstall` run with the developer user. A package can execute before an import.

## Test

Read the scripts block. Install with `--ignore-scripts` and without. Compare the network and the file writes.

## Proof

A script side effect during install.

## Failure modes

A lockfile and a script policy block it. A package can add the script later.
