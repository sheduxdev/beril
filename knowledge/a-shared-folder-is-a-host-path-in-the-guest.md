---
id: a-shared-folder-is-a-host-path-in-the-guest
title: A shared folder is a host path in the guest
tags: hv, shared-folder, path
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# A shared folder is a host path in the guest

## Claim

A shared folder maps a host directory into the guest. A traversal or a symlink in the guest reaches the host path.

## Test

List the shares and the mount options. Create a symlink to a host path. Read through it in the guest.

## Proof

A host file read from the guest.

## Failure modes

A read only share blocks the write but not the read. A mount option can allow symlinks.
