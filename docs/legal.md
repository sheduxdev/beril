# Responsible use and legal frame

This is not legal advice. Get a short opinion from a lawyer who works with
computer law in Turkey before a public release.

## Turkey

- **TCK 243:** Unlawful entry into a computer system and staying there. The
  fourth paragraph covers watching data traffic with technical tools without
  entering.
- **TCK 244:** Blocking, breaking or destroying a system or data. Every active
  check that can be disruptive sits near this article.
- **Cybersecurity Law 7545 (2025):** Article 16 defines nine offences. 16/4
  punishes opening, sharing or selling leaked personal or critical public
  service data without permission (3 to 5 years). Case law is young.
- **KVKK:** A data controller notifies a breach within 72 hours. Beril counts as
  a processor when it sees personal data and minimises it in the report.

## Design rules

1. **Passive default.** A browser-like GET against a public page.
2. **Proof for active work.** DNS TXT, file or meta verification is enforced in
   code.
3. **Non-destructive.** GET, one quote, one marker, one redirect, one traversal.
   No writes. 2 requests per second, 250 request budget.
4. **Secret masking.** No full key in the report. Personal data is counted, not
   quoted.
5. **No leaked data corpus.** Beril does not search, download or store someone
   else's breach dump.
6. **Adapters inherit the gate.** `beril run` asks for an ownership record before
   Nuclei or testssl. Ingested results are marked as imports.
7. **Responsible reporting.** A user who finds a bug on someone else's system
   reports it to the security channel. Verify the USOM path before publishing.
8. **Clear terms.** README and first run say "systems you own or have written
   permission to test".
9. **Cautious wording.** "Indicator, needs confirmation" rather than "breach".

## Risk by check type

| Type | Risk | Gate |
|---|---|---|
| GET on a public page | Low, grey area | None |
| Path and file probes | Low | Treated as passive |
| Quote and marker | Low | Ownership record |
| Port connection | Low | Ownership record |
| Authenticated IDOR | Medium | Manual, two accounts |
| Write and delete | Medium | Separate approval |
| Fuzz and load | High | Separate window |

## Program rules

The bug bounty rule comes before Beril's default. If the program says "GET only",
turn active off. If it limits automated scanning, lower the rate.

## Evidence and retention

- Requests and responses stay under `scans/`.
- Secrets are masked.
- Personal data excerpts stay under 1200 characters.
- The program decides retention. Without a rule, delete after publication.

## False alarms

Beril never says "you are secure". It says "no finding in these checks". The
scope list is mandatory in every report. A wrong finding carries a
`false_positive` field and human confirmation.

## Beril's own safety

- Collected text is data. `guard.py` marks risk.
- The agent runs only allowlisted commands directly.
- The sandbox has no network.
- The dashboard binds loopback.
- No key is written to disk.

Detail: `docs/prompt-injection.md`, `SECURITY.md`.
