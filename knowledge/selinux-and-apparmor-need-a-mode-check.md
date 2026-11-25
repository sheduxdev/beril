---
id: selinux-and-apparmor-need-a-mode-check
title: SELinux and AppArmor need a mode check
tags: linux, selinux, apparmor
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# SELinux and AppArmor need a mode check

## Claim

A permissive or complaining profile logs but does not block. The enforcement mode decides the value of the label.

## Test

Read the mode and the profile. Run a denied action. Check the audit log for the denial.

## Proof

The action is blocked in enforcing mode.

## Failure modes

A disabled module makes the check moot. A broad profile allows most paths.
