---
id: rust-unsafe-is-a-contract-not-a-bug
title: Rust unsafe is a contract, not a bug
tags: lang, rust, unsafe
confidence: high
updated: 2026-11-26
uses: 0
sources: references/rust-reverse.md
status: active
---
# Rust unsafe is a contract, not a bug

## Claim

An `unsafe` block is a promise the compiler cannot check. The bug is a broken invariant, not the keyword.

## Test

List the unsafe blocks. Read each safety comment. Look for a length, a lifetime or an aliasing break.

## Proof

An input that breaks the invariant.

## Failure modes

A safe wrapper around the block contains it. A dependency can hide the unsafe code.
