---
id: shellcode-needs-the-loader-contract
title: Shellcode needs the loader contract
tags: malware, shellcode, loader
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/exploit-development.md
status: active
---
# Shellcode needs the loader contract

## Claim

A blob is only shellcode if something allocates, writes and calls it. The contract is the allocation flags and the entry state.

## Test

Disassemble with a raw arch. Identify the PEB walk or the hash resolver. Emulate the first instructions.

## Proof

A resolver loop and a syscall table walk.

## Failure modes

Position independent data can look like code. A decoder needs the right key.
