---
id: java-deserialization-needs-a-classpath-gadget
title: Java deserialization needs a classpath gadget
tags: lang, java, deser
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/re-jvm.md
status: active
---
# Java deserialization needs a classpath gadget

## Claim

An ObjectInputStream read is only RCE when a gadget chain and a trigger exist on the classpath.

## Test

Identify the stream. Enumerate the libraries and versions. Try a matching ysoserial chain with a DNS callback.

## Proof

A callback or a command from the object.

## Failure modes

A serialization filter can block the classes. A missing trigger breaks the chain.
