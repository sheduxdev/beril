---
id: jni-is-a-native-boundary-with-a-type-contract
title: JNI is a native boundary with a type contract
tags: android, jni, native
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/re-android-native.md
status: active
---
# JNI is a native boundary with a type contract

## Claim

A JNI function trusts the Java types and the array length. A length or a null from Java can become a native memory bug.

## Test

List the native methods. Read the JNI code. Send a null, a short array and a negative length.

## Proof

A native crash or a corrupted value.

## Failure modes

A checked wrapper closes it. A Java exception can stop the call early.
