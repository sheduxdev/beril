---
id: nfs-no-root-squash-is-a-root-write
title: NFS no_root_squash is a root write
tags: linux, nfs, root
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# NFS no_root_squash is a root write

## Claim

An export with `no_root_squash` lets a root client create a SUID root file on the share and run it on the server.

## Test

Read the export options. Mount from a root client. Create a SUID shell. Run it on the server.

## Proof

A root shell on the server.

## Failure modes

`root_squash` blocks it. A read only export stops the write.
