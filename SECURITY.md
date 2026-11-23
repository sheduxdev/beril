# Security policy

## Supported versions

The latest tag on `main` gets fixes. Older tags are snapshots and are not patched.

## Report a vulnerability

Use GitHub private advisories:

https://github.com/sheduxdev/beril/security/advisories/new

Include the version from `git describe --tags --always`, the affected file or
command, the smallest reproduction, and the impact. Do not paste a live token.
Say where it lives and mask it.

You can expect a first reply within seven days. If the report is valid, the fix
lands on `main` and the advisory is published after the fix.

## Scope

In scope:

- the Python scripts, shell wrappers, dashboard and installer;
- the finding model, scope matching and ownership gate;
- a bypass of the active gate or the request budget;
- a scan check that produces a false positive or a false negative with a clear
  reproduction;
- a path, command or template injection in Beril itself;
- a secret that reaches an output file unmasked;
- a sandbox escape from `scripts/sandbox.sh`;
- prompt injection that makes an agent run an unlisted command.

Out of scope:

- the security posture of a host you scanned with Beril;
- an upstream tool or source site;
- a lab target that is meant to be vulnerable;
- a finding that the scanner correctly labeled `low` confidence.

The passive scanner, the artifact scanner and the hunt line are separate
stages. A finding in a target is not a Beril bug unless the scanner reported it
wrong.

## Beril's own controls

| Control | Where |
|---|---|
| Passive by default | `scan_app.py`, `mode` |
| Ownership record with expiry | `authz.py` |
| Scope allowlist | `authz.in_scope` |
| Request budget and rate | `web_checks.Fetcher` |
| Masked secrets | `secrets.mask` |
| Static artifact handling | `scan_artifact.py` |
| Networkless sandbox | `scripts/sandbox.sh` |
| Prompt guard | `guard.py`, `prompt_risk` in `extract.py` |
| Loopback dashboard | `dashboard.py` |

## Testing a fix

```bash
./install.sh --dev
python -m pytest -q
./beril validate
```

A regression test is expected with a gate, masking or false-positive fix.
