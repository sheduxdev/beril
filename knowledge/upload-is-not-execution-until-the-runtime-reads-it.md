---
id: upload-is-not-execution-until-the-runtime-reads-it
title: Upload is not execution until the runtime reads it
tags: rce, upload, execution
confidence: high
updated: 2026-11-26
uses: 0
sources: references/rce-mastery.md, labs/rce
status: active
---
# Upload is not execution until the runtime reads it

## Claim

Extension, MIME, magic byte and serving path are separate checks. Execution needs the stored file in a path the runtime compiles or includes.

## Test

Upload text and find the stored URL. Test each check alone. Try a polyglot, double extension, case change and htaccess or web config. Fetch the file and compare served type with execution.

## Proof

Command output or callback from the stored file.

## Failure modes

A CDN serves the file as static. A resize strips code. The upload path is outside the web root.
