---
id: recon-attack-surface
title: Your attack surface is what enumeration finds, not what you deployed
tags: recon, asm, subdomain, osint
confidence: high
updated: 2026-11-26
uses: 0
sources: https://owasp.org/www-project-amass/, https://github.com/owasp-amass/amass, https://attack.mitre.org/techniques/T1595/
status: active
---
# Your attack surface is what enumeration finds, not what you deployed

## Claim

An attacker maps internet-facing assets from passive sources: certificate transparency logs, DNS, WHOIS, reverse IP and public OSINT. Forgotten subdomains such as old or test hosts are frequent entry points, including subdomain takeover.

## Test

Run passive enumeration on your own domains (Amass, Subfinder, CT log search). Diff the result against the official inventory. Flag dangling CNAMEs that point to deprovisioned cloud resources.

## Proof

A live asset the inventory did not list, or a CNAME pointing at an unclaimed cloud endpoint that can be registered.

## Failure modes

Passive data goes stale, so re-run on a schedule. Active scanning needs written scope. Finding an asset is not a finding; it is the start of one.
