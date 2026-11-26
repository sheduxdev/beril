# OSINT

Public records and posts answer questions packets cannot. `references/osint-toolkit.md`
is the method and tool shelf. This page is the short path.

## Start

One question, two source classes, a date on every fact.

```bash
./beril recon --target example.com
dig +short TXT example.com
curl -s https://rdap.org/domain/example.com
```

Map the domain first. Then read certificates, registries, code and archives in
that order.

## Rules

- Public is not permission. Read the terms and the scope.
- A lead needs two independent sources before it enters a report.
- Archive before you quote.
- Name the date, the source and the confidence.
- Keep personal data to the minimum the question needs.
- A login wall and an API key are separate terms.
- A dead source stays with its archive link.

## Order

1. `recon` for the host inventory.
2. RDAP and DNS for registration and records.
3. Certificate transparency for names.
4. Registry and corporate records for the owner.
5. Code and package search for leaks and stack.
6. Archive for deleted and changed pages.
7. Images for place and time only with two cues.

## Output

Use the lead block in `references/osint-toolkit.md`. A lead without two sources
stays a lead.

## Limits

- Free APIs rate limit.
- A certificate name is not a live host.
- A favicon hash is not proof of ownership.
- A social profile is self reported.
- An image cue can match several places.

Check the host with `scan` after the map. OSINT finds the door. It does not
prove it opens.
