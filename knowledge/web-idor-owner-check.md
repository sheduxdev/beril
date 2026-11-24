---
id: web-idor-owner-check
title: IDOR is a missing owner check, not a hidden id
tags: web, idor, access-control
confidence: high
updated: 2026-11-24
uses: 1
sources: references/techniques.md, docs/break-my-app.md
status: active
---
# IDOR is a missing owner check, not a hidden id

## Claim

An object id from the request is used without comparing the object owner to the session user. Hiding the id in a UUID does not add a check.

## Test

Create two accounts at the same role. Capture an object id from A. Request it with B. Repeat for read, update, delete and export.

## Proof

B receives or changes A's object, with both sessions and the ids in the log.

## Failure modes

A public object, a 200 with an empty body, or an admin bypass is not the same bug. Check the data, not the status.
