---
id: web-imagemagick-delegate
title: An image converter is a parser zoo with shell delegates
tags: web, rce, upload, imagemagick
confidence: medium
updated: 2026-11-26
uses: 0
sources: https://imagemagick.org/script/security-policy.php, https://nvd.nist.gov/vuln/detail/CVE-2016-3714
status: active
---
# An image converter is a parser zoo with shell delegates

## Claim

ImageMagick, Ghostscript, ExifTool or ffmpeg pick a decoder by content, not extension. Some coders call external programs (ImageTragick, CVE-2016-3714).

## Test

List the tools the upload path calls and their versions. Read `policy.xml` for disabled coders: PS, EPS, PDF, XPS, MVG, MSL, URL.

## Proof

A policy that allows a dangerous coder on untrusted input, or a lab file that triggers a delegate.

## Failure modes

An extension check does not stop content sniffing. The fix is a strict policy, a sandboxed worker without network, and re-encoding to one known format.
