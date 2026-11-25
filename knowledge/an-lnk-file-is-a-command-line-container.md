---
id: an-lnk-file-is-a-command-line-container
title: An LNK file is a command line container
tags: malware, lnk, delivery
confidence: high
updated: 2026-11-26
uses: 0
sources: references/reverse-engineering.md
status: active
---
# An LNK file is a command line container

## Claim

A shortcut stores arguments, an icon and a working directory. The target can be a LOLBin with a remote payload.

## Test

Read the LNK target and arguments with a parser. Check the icon and the working directory. Run it in a sandbox.

## Proof

The stored command line and the child process.

## Failure modes

A LNK can point to a local script. A Mark of the Web can change the behavior.
