# Incident case library

Five published cases, one rule each, one lab each. The point is the chain:
event, root cause, detection, fix, rule, lab. A case that does not produce a
rule is reading, not practice.

```bash
./beril incidents list
./beril incidents show log4shell
./beril incidents lab log4shell
./beril incidents run log4shell
./beril incidents run --all
```

Rules live in `data/incidents.jsonl` and load into `source_audit` as
`src.incident-<id>`. The lab has one line that must match and one noise line
that must not.

## Cases

| ID | Year | Publisher | Lesson |
|---|---:|---|---|
| `log4shell` | 2021 | CISA AA21-356A | A parser reached the network |
| `papercut-bl00dy` | 2023 | CISA AA23-144A | Unauthenticated setup and a child process |
| `mssql-bluesky` | 2023 | The DFIR Report | Public database, weak password, xp_cmdshell |
| `barracuda-esg` | 2023 | Mandiant | Attachment parsing to shell |
| `volt-typhoon` | 2024 | CISA AA24-060B | Built-in tools, no malware |

## Source policy

- Only published analysis is used: vendor advisory, DFIR writeup, framework.
- The link is the source of record. The JSONL keeps a short summary, not the
  article text.
- No leaked data, no victim file, no stolen credential is stored.
- No leaked source tree or tool is run. A case cites the public writeup.
- Numbers that change (victim counts, ransom figures) stay in the link unless
  the publisher states them as final.

## Method

1. Read the case and write the event from memory.
2. Name the root cause without the tool name.
3. Write one detection line that a log would carry.
4. Run the lab. The rule must match the incident and not the noise.
5. Write the fix in the order an operator can apply it.
6. Add the rule to your own pipeline and keep the false positive note.

The rule is a teaching aid. A real deployment needs a parser, a field mapping
and a backtest against a week of logs.
