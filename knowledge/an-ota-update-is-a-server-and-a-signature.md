---
id: an-ota-update-is-a-server-and-a-signature
title: An OTA update is a server and a signature
tags: auto, ota, update
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-update-sign.md
status: active
---
# An OTA update is a server and a signature

## Claim

The update path has a server, a transport, a package and a verify step. The weakest of the four is the target.

## Test

Read the update client and the server trust. Check the signature and the rollback. Try an old package.

## Proof

A downgrade or a package from the wrong server.

## Failure modes

A pinned TLS and a counter hold. A recovery mode can allow a signed old image.
