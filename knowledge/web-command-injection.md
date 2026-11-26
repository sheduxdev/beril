---
id: web-command-injection
title: Command injection is a string reaching a shell
tags: web, rce, command-injection
confidence: high
updated: 2026-11-26
uses: 0
sources: https://cwe.mitre.org/data/definitions/78.html, https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html, https://portswigger.net/web-security/os-command-injection
status: active
---
# Command injection is a string reaching a shell

## Claim

User input is joined into a command line that a shell parses: `system`, `exec`, `popen`, backticks, `shell=True`, `Runtime.exec("sh -c ...")`.

## Test

Find the sink in source first. Trace one input to it. In a lab, send a harmless separator and a time delay or an out-of-band DNS callback to your own host.

## Proof

A delay, callback or file write that only a second command could cause.

## Failure modes

An argv array with no shell is not this bug, but option injection (`--output=`) still is. Escaping by blocklist fails; the fix is no shell, an allowlist and `--` before arguments.
