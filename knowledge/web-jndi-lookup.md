---
id: web-jndi-lookup
title: A JNDI lookup in a log line is remote class loading
tags: web, rce, java, log4j
confidence: high
updated: 2026-11-26
uses: 0
sources: https://logging.apache.org/log4j/2.x/security.html, https://www.cisa.gov/news-events/news/apache-log4j-vulnerability-guidance, https://nvd.nist.gov/vuln/detail/CVE-2021-44228
status: active
---
# A JNDI lookup in a log line is remote class loading

## Claim

A logger expands `${jndi:...}` in logged data, fetches an LDAP or RMI reference and loads a remote object (Log4Shell, CVE-2021-44228).

## Test

Inventory log4j-core versions, including shaded and nested jars. In a lab, log a lookup that points to your own DNS canary.

## Proof

A DNS or LDAP callback from the server, tied to the request.

## Failure modes

log4j-api alone is not vulnerable. A DNS hit without class loading proves the lookup, not RCE. The fix is 2.17.1 or later; WAF rules are a stopgap that obfuscation bypasses.
