---
id: a-sudoers-rule-needs-the-argument-check
title: A sudoers rule needs the argument check
tags: linux, sudo, sudoers
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# A sudoers rule needs the argument check

## Claim

A sudo rule for a binary with a shell escape, a wildcard argument or an editor is root if the argument is not pinned.

## Test

Run `sudo -l`. Compare each rule with GTFOBins. Try a shell flag, a file argument and a wildcard match.

## Proof

A root shell or a root file write.

## Failure modes

A fixed argument and a noexec option can hold. A timestamp timeout limits the window.
