---
id: selinux-is-the-android-mandatory-control
title: SELinux is the Android mandatory control
tags: android, selinux, policy
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# SELinux is the Android mandatory control

## Claim

A domain transition and a context label decide file and socket access. A permissive domain logs and allows.

## Test

Read the mode. Check the context of the target file. Trigger a denial and read `dmesg` or the audit log.

## Proof

A denied action in enforcing mode.

## Failure modes

A permissive build hides it. A vendor policy can allow the path.
