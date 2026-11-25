---
id: lfi-becomes-rce-only-through-an-executor
title: LFI becomes RCE only through an executor
tags: rce, lfi, php
confidence: high
updated: 2026-11-26
uses: 0
sources: references/rce-mastery.md
status: active
---
# LFI becomes RCE only through an executor

## Claim

Reading a file is disclosure. Execution needs an include that compiles, a wrapper that runs, a poisoned log that is included, or an upload that is executed.

## Test

Identify include versus read. For PHP try php filter for source, then data or phar, then session and access log poisoning. Chain upload plus include when available.

## Proof

Command output from the included file.

## Failure modes

php filter alone is disclosure. The log path differs by distro. Log encoding breaks the syntax.
