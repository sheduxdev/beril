---
id: runtime-tls
title: Thread-local storage has a model and a destructor order
tags: runtime, tls, threads
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Thread-local storage has a model and a destructor order

## Claim

The TLS model decides the lookup cost. The destructor runs at thread exit, and the order is not yours to choose.

## Test

Read the TLS model in the binary. Start and stop a thread. Check the destructor.

## Proof

A correct per-thread value and a clean destructor.

## Failure modes

A dynamic TLS in a dlopen library has a slow path. A destructor that touches freed state crashes.
