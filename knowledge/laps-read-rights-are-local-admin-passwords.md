---
id: laps-read-rights-are-local-admin-passwords
title: LAPS read rights are local admin passwords
tags: ad, laps, password
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# LAPS read rights are local admin passwords

## Claim

Read access to the LAPS password attribute on a computer object is the local administrator password for that host.

## Test

Check the extended right on the computer. Read `ms-Mcs-AdmPwd` or the Windows LAPS attribute. Log in locally.

## Proof

A local admin session on the host.

## Failure modes

The password can be rotated. A host with unique local admin and no shared reuse limits the spread.
