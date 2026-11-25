---
id: tls-dtor-is-a-per-thread-function-pointer
title: TLS dtor is a per thread function pointer
tags: pwn, tls, dtor
confidence: low
updated: 2026-11-26
uses: 0
sources: references/exploit-development.md
status: active
---
# TLS dtor is a per thread function pointer

## Claim

The TLS destructor list runs on thread exit and can be overwritten with a controlled function and argument.

## Test

Find the dtv. Write a pair. Exit the thread. Watch the call.

## Proof

The function runs with the argument.

## Failure modes

A static binary or a different TLS layout blocks it. A process exit can differ from a thread exit.
