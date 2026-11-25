---
description: Run Beril from a natural sentence
allowed-tools: Bash, Read, Grep, Glob
---

The user said: "$ARGUMENTS"

Act now. Do not ask the four-question intake when the target is in the sentence.

1. Classify the target: URL, domain, directory, file, image, CIDR or nothing.
2. Classify the intent: assess ("kır", "açık bul", "break", "find a bug"), map
   ("harita", "recon", "subdomain"), secrets, artifact, source review, hunt,
   config, dependency or report.
3. Run the first command from this table:

| Target and intent | Command |
|---|---|
| URL, assess | `./beril scan --target <url> --out scans/scan` |
| Domain, map | `./beril recon --target <domain>` |
| Domain, assess | `./beril scan --target <domain> --out scans/scan` |
| Directory, review | `./beril scan --target <dir> --tools --vibe` |
| Repository, find a bug | `./beril hunt --target <repo> --sandbox` |
| File, artifact | `./beril scan --target <file> --deep` |
| Secret leak | `./beril secrets --target <dir> --history` |
| MCP config | `./beril mcp --target <dir>` |

4. Read the output, then answer with the top three evidence-backed items, one
   next manual test, and what was not tested. Save the report path.

If the intent is "kır" and the next step needs a payload, check the gate. An
explicit "benim" or "my app" allows `--owned`. Without a record and without a
claim, stay passive and ask one permission question.

Answer in the user's language. A scanner hit is a lead, not a finding.
