---
id: length-extension-breaks-secret-prefix-hashes
title: Length extension breaks secret prefix hashes
tags: crypto, hash, mac
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# Length extension breaks secret prefix hashes

## Claim

A MAC built as hash(secret + message) with MD5 or SHA1 can be extended without the secret.

## Test

Take a valid message and MAC. Use hash_extender or hashpumpy to append data and a new MAC.

## Proof

The server accepts the extended message.

## Failure modes

HMAC or SHA3 prevents it. A server that checks the full length can still be fooled by the right padding.
