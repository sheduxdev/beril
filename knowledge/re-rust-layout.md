---
id: re-rust-layout
title: Rust types are not C types
tags: re, rust, layout
confidence: high
updated: 2026-11-24
uses: 0
sources: references/rust-reverse.md
status: active
---
# Rust types are not C types

## Claim

A slice is pointer plus length. A trait object is data plus vtable. Option uses a null niche. Async is a state machine.

## Test

Before reading a method, name the two-field structs and the function-pointer pairs. Map the state enum for async.

## Proof

A recovered prototype or struct that explains the call site.

## Failure modes

A C-string view truncates a &str. Monomorphized copies are not separate features.
