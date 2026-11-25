---
id: userfaultfd-moves-a-page-fault-to-user-space
title: userfaultfd moves a page fault to user space
tags: link, userfaultfd, fault
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/os-page-fault.md
status: active
---
# userfaultfd moves a page fault to user space

## Claim

A registered range delivers the fault to a handler. A race between the handler and the kernel can expose a stale page.

## Test

Register a range. Fault a page. Delay the reply. Read the page from another path.

## Proof

A stale or an attacker supplied page.

## Failure modes

A disabled sysctl blocks it. A different mapping can avoid the handler.
