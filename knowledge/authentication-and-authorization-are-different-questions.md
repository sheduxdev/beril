---
id: authentication-and-authorization-are-different-questions
title: Authentication and authorization are different questions
tags: design, authn, authz
confidence: high
updated: 2026-11-26
uses: 0
sources: references/techniques.md
status: active
---
# Authentication and authorization are different questions

## Claim

A valid session says who the caller is. It says nothing about the object. Every object access needs the owner or role check.

## Test

With one valid account, request a foreign object by id. Repeat for read, write and delete.

## Proof

A foreign object returned or changed.

## Failure modes

A global object can be public. A tenant wide role can be intended.
