---
id: dicom-is-a-medical-image-and-a-network-protocol
title: DICOM is a medical image and a network protocol
tags: med, dicom, pacs
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/network-protection.md
status: active
---
# DICOM is a medical image and a network protocol

## Claim

DICOM has a header with patient data and a network service with a calling and a called AE title. A PACS often accepts any caller.

## Test

Read the AE titles. Query with a C-FIND. Retrieve one image with a C-MOVE or a C-GET.

## Proof

An image and a patient header from the PACS.

## Failure modes

An AE allowlist blocks it. A TLS only endpoint needs a certificate.
