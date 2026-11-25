---
id: tso-is-an-interactive-mainframe-session
title: TSO is an interactive mainframe session
tags: mf, tso, session
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# TSO is an interactive mainframe session

## Claim

A TSO session runs commands and REXX with the user rights. A command or a CLIST is the first surface.

## Test

Log in to a lab. List the authorized commands. Run a REXX to read a dataset.

## Proof

A dataset read from a REXX.

## Failure modes

A command can be restricted. A session can be read only.
