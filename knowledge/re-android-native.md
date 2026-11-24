---
id: re-android-native
title: JNI is the bridge between Java and native code
tags: re, android, jni
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/mobile-reverse.md
status: active
---
# JNI is the bridge between Java and native code

## Claim

Native methods are registered by name or JNI_OnLoad. The signature ties a Java method to a C function.

## Test

Find RegisterNatives and JNI exports. Map the signatures. Hook the native side.

## Proof

A recovered native function and a working hook.

## Failure modes

A stripped library hides names. Static registration still leaves exports.
