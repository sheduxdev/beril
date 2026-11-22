# Security policy

## Supported versions

The latest tag on `main` gets fixes. Older tags are snapshots and are not patched.

## Report a vulnerability

Use GitHub private advisories:

https://github.com/sheduxdev/beril/security/advisories/new

Include the version from `git describe --tags --always`, the affected file or command, the smallest reproduction, and the impact. Do not paste a live token. Say where it lives and mask it.

You can expect a first reply within seven days. If the report is valid, the fix lands on `main` and the advisory is published after the fix.

## Scope

In scope:

- the Python scripts, shell wrappers, dashboard and installer;
- the schema and parsing logic;
- a scan check that produces a false positive or a false negative with a clear reproduction;
- a path or command injection in Beril itself.

Out of scope:

- the security posture of a host you scanned with Beril;
- an upstream tool or source site;
- a lab target that is meant to be vulnerable.

The read-only scanner and the artifact scanner are separate products. A finding in a target is not a Beril bug unless the scanner reported it wrong.
