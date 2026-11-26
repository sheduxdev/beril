---
id: web-ssti-sandbox
title: SSTI is input parsed as a template, not rendered into one
tags: web, rce, ssti
confidence: high
updated: 2026-11-26
uses: 0
sources: references/techniques.md, https://portswigger.net/web-security/server-side-template-injection, https://cwe.mitre.org/data/definitions/1336.html
status: active
---
# SSTI is input parsed as a template, not rendered into one

## Claim

The app builds the template source from user input (`render_template_string(user)`, `Template(user)`) instead of passing it as a variable.

## Test

Send an arithmetic probe such as `{{7*7}}` and engine variants. Fingerprint the engine from errors and output. Read whether a sandbox is on.

## Proof

Evaluated output, then engine identity. In your own lab, object traversal to a command.

## Failure modes

Client-side template output is XSS, not SSTI. A sandboxed engine may only leak config. The fix is a fixed template with data in the context.
