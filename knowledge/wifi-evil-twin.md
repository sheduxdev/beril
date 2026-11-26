---
id: wifi-evil-twin
title: An evil twin wins when the client does not verify the network
tags: wifi, evil-twin, eap-tls, wpa3
confidence: medium
updated: 2026-11-26
uses: 0
sources: https://www.cisa.gov/news-events/news/securing-enterprise-wireless-networks, https://attack.mitre.org/techniques/T1557/004/
status: active
---
# An evil twin wins when the client does not verify the network

## Claim

A rogue AP broadcasts a real SSID, often at higher power, and clients reconnect to it (MITRE T1557.004). WPA2-Enterprise without server-certificate validation hands credentials to the twin. WPA3 transition mode keeps the WPA2 attack surface.

## Test

On your own network, check that clients are configured to validate the RADIUS server certificate and CA, and to refuse an unknown one. Confirm Protected Management Frames are required and transition mode is understood.

## Proof

A client that refuses to associate when the server certificate does not match, and management frames that cannot be forged to deauth.

## Failure modes

EAP methods without mutual auth, or clients set to not validate the cert, defeat WPA3's promise. Transition mode downgrades silently. Headless IoT often cannot do EAP-TLS, so segment it.
