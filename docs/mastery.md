# Mastery map

The 25-week curriculum gets you to competent. This map is the longer climb. Pick one primary track, keep one secondary, and measure by artifacts, not courses. `references/specialist-program.md` turns each track into four week blocks. `references/senior-bar.md` is the review rubric.

## Milestones

| Stage | Evidence | Typical time |
|---|---|---|
| Beginner | 20 solved labs, 5 writeups, a clean report | 0 to 6 months |
| Operator | 3 real findings, one chain, one tool built | 6 to 18 months |
| Specialist | 10 findings in one class, a talk or a CVE | 18 to 36 months |
| Researcher | Novel primitive or a named technique | 3 to 6 years |
| Teacher | Others reproduce your work, you review theirs | after research |

Certifications help at gates. They do not replace artifacts. OSCP, OSWE, OSED, CRTO, CISSP and cloud certs each signal a different thing. Pick for the job you want, not for the badge.

## Tracks

### Web and API

- Deep: auth, OAuth, SAML, request parsing, cache, race, GraphQL, business logic.
- RCE specialization: command injection, template and expression engines, deserialization, LFI, upload, SQLi and SSRF to execution.
- Build: a proxy plugin, a parser diff tool, a fuzzer for a spec.
- Read: PortSwigger research, Bugcrowd VRT, OWASP WSTG, disclosed reports.
- Proof: a chain with a clean reproduction and a fix.
- Ceiling: novel parser or protocol research.
- Track: `references/rce-curriculum.md`.

### Binary and RE

- Deep: C/C++, mitigations, heap internals, kernel, hypervisor, firmware.
- Build: a Ghidra script, a harness, a crash triage pipeline.
- Read: POA, Practical Malware Analysis, how2heap, Project Zero.
- Proof: a PoC with reliability, a patch diff, a CVE.
- Ceiling: novel exploitation primitive or a full chain on a hardened target.

### Network defense

- Deep: flow and packet analysis, DNS, TLS and ECH, IDS tuning, segmentation, egress, DDoS, zero trust, BGP and RPKI.
- Build: a beacon scorer, a Sigma rule set, a segmented lab, a honeypot with alerting.
- Read: NIST SP 800-94 and 800-61r3, CISA CPGs, SANS flow and metadata papers, ATT&CK and D3FEND.
- Proof: a segmentation test with a closed bypass, a tuned rule with measured false positives, an incident timeline.
- Ceiling: detection engineering at scale or protocol visibility research.
- Track: `references/network-curriculum.md`.

### Cloud and AD

- Deep: IAM, trust policies, ADCS, delegation, Kubernetes, CI identity.
- Build: a cloud attack-path graph, a misconfig scanner, a detection rule.
- Read: HackTricks cloud, BloodHound docs, cloud provider docs, ATT&CK.
- Proof: a read-only escalation path with a clear blast radius.
- Ceiling: identity research across providers.

### Mobile and firmware

- Deep: Android internals, iOS, ARM, bootloaders, update signing, radio.
- Build: a Frida harness, an emulation rig, a firmware diff tool.
- Read: MASTG, Android Internals, EMBA docs, vendor advisories.
- Proof: a component chain or a root shell with recovery steps.
- Ceiling: baseband and secure boot research.

## Research habits

1. Keep a question log. One question per week.
2. Read one primary paper or advisory a day.
3. Rebuild one technique from scratch each month.
4. Diff one patched project each month.
5. Write down what failed. Failures are the map.
6. Present at a local meetup before a conference.
7. Review someone else's report every month.

## Portfolio

- Three writeups with a reproduction and a fix.
- One tool with a README and tests.
- One talk or workshop.
- One disclosed report or CVE.
- One detection rule with a false-positive analysis.
- A one-page CV that names the artifacts.

## Anti-patterns

| Pattern | Cost |
|---|---|
| Tutorial completion without a lab | False confidence |
| Tool collection | Choice paralysis |
| Wide but shallow | Duplicate reports and triage misses |
| No notes | Every lesson resets |
| Only CTFs | Weak business impact |
| Only real targets | Missing fundamentals |
| No writing | Invisible work |

## Weekly maintenance

- Two labs from an old phase.
- One new primary source.
- One review of a peer's work.
- One hour on the weakest track.
- One paragraph on what changed in your model.

## Teaching

Teach a topic when you can predict the three mistakes a learner will make. Teaching exposes the gaps faster than another course.

Use `agents/mentor.md` to run a session. Grade against `references/curriculum.md`. Keep the evidence rule for the learner too.
