# Maintainer report template

Use this only for a finding that reached `reproduced` or `verified`. A candidate
without a line number and a reproduction stays in the local notes.

```markdown
Subject: [security] <class> in <component>, <one line impact>

## Summary

<Two sentences. What is wrong, what an attacker gets.>

This was found with an AI assisted static and sandboxed review (Beril). The
reproduction below was run locally.

## CRA fields

For a product under the EU Cyber Resilience Act, add: product name, affected
version, fixed version, support period, CVSS, CWE, the report date and the
planned disclosure date. `./beril report --profile cra` lays these out; fill the
`meta` values first.

## Affected

- Version: <tag or commit>
- File: <path>:<line>
- Component: <parser, endpoint, CLI>
- Configuration: <flags, defaults>

## Reproduction

```bash
<smallest build and run commands>
```

Input:

```
<smallest input or request>
```

Observed:

```
<sanitizer output, crash, wrong response>
```

Expected: <the correct behavior>.

## Impact

<Who can trigger it, from where, with what prerequisites. State DoS vs RCE only
if proven.>

## Root cause

<The missing check and the line. One paragraph.>

## Suggested fix

```diff
<smallest patch>
```

## Notes

- CWE: <id>
- Confidence: reproduced / verified
- Raw log: <path or attachment>
- Not tested: <list>
```

## Sending

1. Check `SECURITY.md`, `GOVERNANCE.md` and the GitHub security tab.
2. Prefer the project's private channel.
3. If the project has a policy, follow its timeline. Otherwise propose 90 days.
4. Send one finding per report unless two share a root cause.
5. Do not attach a weaponised exploit. A crash input is enough.
6. If the maintainer asks for a CVE, help with the request but do not assign one
   yourself.

## Quality gate

- Build command works from a clean clone.
- Input is attached and minimal.
- Sanitizer or response proves the behavior.
- The fix compiles or is obviously correct.
- The report says what was not tested.
- No full secret and no personal data in the body.
