---
id: shell-is-a-quoting-language-first
title: Shell is a quoting language first
tags: lang, shell, quoting
confidence: high
updated: 2026-11-26
uses: 0
sources: references/techniques.md
status: active
---
# Shell is a quoting language first

## Claim

Every unquoted expansion is a word split and a glob. A variable in a command is not an argument.

## Test

Put a space, a star, a semicolon and a newline in the value. Compare a quoted and an unquoted call.

## Proof

An extra argument or a second command.

## Failure modes

An argv call from a script language avoids the shell. A strict allowlist limits the value.
