# RCE, intrusion prevention and pentest reading list

Where to read about finding RCE, closing it, and stopping intrusions. Primary sources first. Use a lab or a scope you own.

Snapshot 2026-11-26.

## Standards and taxonomies

| Source | Endpoint | Use |
|---|---|---|
| CWE-78 OS command injection | `https://cwe.mitre.org/data/definitions/78.html` | Root cause and examples |
| CWE-94 code injection | `https://cwe.mitre.org/data/definitions/94.html` | eval-class RCE |
| CWE-502 deserialization | `https://cwe.mitre.org/data/definitions/502.html` | Gadget-chain RCE |
| CWE-917 expression language | `https://cwe.mitre.org/data/definitions/917.html` | SpEL, OGNL, EL |
| CWE-1336 template injection | `https://cwe.mitre.org/data/definitions/1336.html` | SSTI |
| CWE-434 unrestricted upload | `https://cwe.mitre.org/data/definitions/434.html` | Upload to execution |
| CWE Top 25 | `https://cwe.mitre.org/top25/` | Yearly ranking |
| OWASP Top 10 | `https://owasp.org/www-project-top-ten/` | A03 Injection, A08 Integrity |
| MITRE ATT&CK T1190 | `https://attack.mitre.org/techniques/T1190/` | Exploit public-facing app |
| MITRE ATT&CK T1059 | `https://attack.mitre.org/techniques/T1059/` | Command interpreter, detections |
| MITRE D3FEND | `https://d3fend.mitre.org/` | Defensive technique map |
| CAPEC | `https://capec.mitre.org/` | Attack patterns per CWE |

## Pentest methodology

| Source | Endpoint | Use |
|---|---|---|
| NIST SP 800-115 | `https://csrc.nist.gov/pubs/sp/800/115/final` | Test planning and rules of engagement |
| OWASP WSTG | `https://owasp.org/www-project-web-security-testing-guide/` | Web test cases, INPV section for injection |
| OWASP ASVS | `https://owasp.org/www-project-application-security-verification-standard/` | Verification levels, fix checklist |
| OWASP MASTG | `https://mas.owasp.org/MASTG/` | Mobile testing |
| PTES | `http://www.pentest-standard.org/` | Engagement phases |
| OSSTMM | `https://www.isecom.org/OSSTMM.3.pdf` | Operational testing |
| HackTricks | `https://book.hacktricks.wiki/` | Community methodology notes |
| PayloadsAllTheThings | `https://github.com/swisskyrepo/PayloadsAllTheThings` | Probe memory aid; confirm the parser |

## RCE classes to learn and fix

| Class | Learn | Fix guidance | Card |
|---|---|---|---|
| OS command injection | `https://portswigger.net/web-security/os-command-injection` | `https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html` | `web-command-injection` |
| SSTI | `https://portswigger.net/web-security/server-side-template-injection` | Same page, prevention section | `web-ssti-sandbox` |
| Deserialization | `https://portswigger.net/web-security/deserialization` | `https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html` | `web-deserialization-gadget` |
| Expression language | `https://owasp.org/www-community/vulnerabilities/Expression_Language_Injection` | Spring `SimpleEvaluationContext` docs | `web-expression-injection` |
| JNDI / Log4Shell | `https://logging.apache.org/log4j/2.x/security.html` | `https://www.cisa.gov/news-events/news/apache-log4j-vulnerability-guidance` | `web-jndi-lookup` |
| File upload | `https://portswigger.net/web-security/file-upload` | `https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html` | `web-upload-validation` |
| Image and document parsers | `https://imagemagick.org/script/security-policy.php` | Policy file, sandboxed worker | `web-imagemagick-delegate` |
| Prototype pollution to RCE | `https://portswigger.net/web-security/prototype-pollution/server-side` | Null-prototype objects, schema validation | `web-prototype-pollution` |
| XXE | `https://portswigger.net/web-security/xxe` | `https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html` | `web-xxe-parser` |
| SSRF to internal RCE | `https://portswigger.net/web-security/ssrf` | `https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html` | `web-ssrf-parser-differential` |
| Memory corruption | `https://github.com/shellphish/how2heap` | Compiler hardening flags, sanitizers | `references/exploit-development.md` |

## Finding RCE in code you own

| Tool | Endpoint | Use |
|---|---|---|
| Semgrep rules | `https://semgrep.dev/r` | Sink rules for exec, eval, templates |
| CodeQL queries | `https://codeql.github.com/codeql-query-help/` | Taint paths, `cwe-078`, `cwe-094` |
| Bandit | `https://bandit.readthedocs.io/` | Python `subprocess` and `pickle` checks |
| gosec | `https://github.com/securego/gosec` | Go `exec.Command` checks |
| Brakeman | `https://brakemanscanner.org/` | Rails command and eval checks |
| OSV-Scanner | `https://google.github.io/osv-scanner/` | Vulnerable dependencies |
| Trivy | `https://trivy.dev/` | Images, SBOM and IaC |
| Nuclei templates | `https://github.com/projectdiscovery/nuclei-templates` | Known-CVE checks on your own hosts |
| OWASP ZAP | `https://www.zaproxy.org/docs/` | DAST on a staging app |
| Burp Suite docs | `https://portswigger.net/burp/documentation` | Manual testing |

## Patch priority and advisories

| Source | Endpoint | Use |
|---|---|---|
| CISA KEV | `https://www.cisa.gov/known-exploited-vulnerabilities-catalog` | Exploited in the wild; JSON feed available |
| FIRST EPSS | `https://www.first.org/epss/` | Exploitation probability |
| FIRST CVSS | `https://www.first.org/cvss/` | Severity vector |
| NVD | `https://nvd.nist.gov/` | CVE records and CPE |
| OSV | `https://osv.dev/` | Ecosystem advisories |
| GitHub Advisory DB | `https://github.com/advisories` | Package advisories |
| USOM | `https://www.usom.gov.tr/` | Turkish national CERT alerts |
| Vendor PSIRTs | Microsoft MSRC, Cisco, Fortinet, Ivanti, Citrix | Edge devices are frequent KEV entries |

## Intrusion prevention and detection

| Source | Endpoint | Use | Card |
|---|---|---|---|
| NIST SP 800-94 | `https://csrc.nist.gov/pubs/sp/800/94/final` | IDPS classes | `defense-ips-inline-tuning` |
| Suricata docs | `https://docs.suricata.io/` | IDS/IPS rules, eve.json | `defense-ips-inline-tuning` |
| Snort 3 docs | `https://www.snort.org/documents` | Rules and inline mode | `defense-ips-inline-tuning` |
| Emerging Threats Open | `https://rules.emergingthreats.net/` | Free ruleset | |
| OWASP CRS | `https://coreruleset.org/docs/` | WAF anomaly scoring | `defense-waf-anomaly-score` |
| Coraza | `https://coraza.io/docs/` | CRS-compatible WAF in Go | `defense-waf-anomaly-score` |
| ModSecurity | `https://github.com/owasp-modsecurity/ModSecurity` | Reference WAF engine | `defense-waf-anomaly-score` |
| Zeek | `https://docs.zeek.org/` | Network logs for hunting | |
| Wazuh | `https://documentation.wazuh.com/` | HIDS, FIM, SIEM | |
| Falco | `https://falco.org/docs/` | Runtime syscall rules, shell in container | `defense-rce-blast-radius` |
| Sigma rules | `https://github.com/SigmaHQ/sigma` | Web shell and child-process detections | `detection-sigma` |
| CrowdSec | `https://docs.crowdsec.net/` | Behavior-based IP blocking | |
| fail2ban | `https://github.com/fail2ban/fail2ban` | Log-driven bans | |
| CISA CPGs | `https://www.cisa.gov/cybersecurity-performance-goals-cpgs` | Baseline controls | |
| NIST SP 800-61r3 | `https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-61r3.pdf` | Incident response after RCE | |

## Hardening after the fix

| Source | Endpoint | Use |
|---|---|---|
| CIS Benchmarks | `https://www.cisecurity.org/cis-benchmarks` | OS and service baselines |
| Docker seccomp | `https://docs.docker.com/engine/security/seccomp/` | Syscall filter |
| Kubernetes Pod Security Standards | `https://kubernetes.io/docs/concepts/security/pod-security-standards/` | Restricted profile |
| AppArmor | `https://apparmor.net/` | Mandatory access control |
| OpenSSF Compiler Hardening Guide | `https://best.openssf.org/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++` | C and C++ flags |

## Labs (local or legal)

| Lab | Endpoint | Covers |
|---|---|---|
| PortSwigger Web Security Academy | `https://portswigger.net/web-security/all-labs` | Every web RCE class, free |
| OWASP Juice Shop | `https://owasp.org/www-project-juice-shop/` | Broad web app |
| DVWA | `https://github.com/digininja/DVWA` | Command injection, upload |
| WebGoat | `https://owasp.org/www-project-webgoat/` | Java, deserialization |
| Vulhub | `https://github.com/vulhub/vulhub` | Docker images of real CVEs, test patch and detection |
| TryHackMe | `https://tryhackme.com/` | Guided rooms, blue and red |
| Hack The Box | `https://www.hackthebox.com/` | Machines and Academy |
| Detection labs | `labs/` in this repo | Local Beril labs |

## Disclosed reports and research

| Source | Endpoint | Use |
|---|---|---|
| HackerOne Hacktivity | `https://hackerone.com/hacktivity` | Disclosed RCE reports and fixes |
| PortSwigger Research | `https://portswigger.net/research` | New primitives |
| Google Project Zero | `https://googleprojectzero.blogspot.com/` | Root-cause analyses |
| Project Zero 0day RCA | `https://googleprojectzero.github.io/0days-in-the-wild/` | In-the-wild exploit analyses |
| Assetnote research | `https://www.assetnote.io/resources/research` | Edge device RCE, patch diffs |
| watchTowr Labs | `https://labs.watchtowr.com/` | Patch diffing of KEV bugs |
| Trail of Bits blog | `https://blog.trailofbits.com/` | Audits and tooling |

Rule. A blog post is a lead. A claim enters a card only with a CVE, an advisory, a vendor fix or a reproducible lab.
