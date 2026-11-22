# Cyber intelligence dossier

Collected 2026-11-22. Every entry links to its public source. Counts describe this snapshot, not the whole internet.

## Coverage

| Layer | Rows | Sources |
|---|---:|---|
| Threads and reports | 311 | 11 |
| Experts | 94 | 4 |
| Tools | 139 | 1 |
| Methods and research | 42 | 8 |

## High-signal threads

- [Unauthenticated remote process termination of Arc RPC nodes via custom JS tracer (Boa engine) leads to sustained node DoS](https://hackerone.com/reports/3966160)
  program Arc, weakness Uncontrolled Resource Consumption, severity High, bounty $10,000 (HackerOne Hacktivity)
- [A disabled account's API key still works on BMO's Mojolicious /rest/ routes, including for security-group bugs filed after the disable](https://hackerone.com/reports/4000084)
  program Mozilla, weakness Improper Authentication - Generic, severity High, bounty $4,000 (HackerOne Hacktivity)
- [Unauthenticated access to Checkout Blocks employee-only endpoints exposed merchant metadata](https://hackerone.com/reports/3954327)
  program Shopify, weakness Missing Authentication for Critical Function, severity Medium, bounty $3,100 (HackerOne Hacktivity)
- [Evernote(WindowsApp) XSS to RCE](https://hackerone.com/reports/2119149)
  program Evernote, weakness Code Injection, severity High, bounty $2,000 (HackerOne Hacktivity)
- [Revoked deployment collaborator regains access to private comments after active collaborator interaction](https://hackerone.com/reports/3852102)
  program Vercel, weakness Access Control Check Implemented After Asset is Accessed, severity Medium, bounty $1,026 (HackerOne Hacktivity)
- [Burp Community OpenAPI site-map action reads a local schema example through $id rebasing](https://hackerone.com/reports/4000535)
  program PortSwigger Web Security, weakness Path Traversal, severity Medium, bounty $1,000 (HackerOne Hacktivity)
- [Public shares remain accessible via alternate endpoints after owner account is disabled](https://hackerone.com/reports/3620539)
  program Nextcloud, weakness Improper Access Control - Generic, severity Medium, bounty $270 (HackerOne Hacktivity)
- [SSRF on Nextcloud Whiteboard Application via Recordings to Unauthorised Access to Whiteboards](https://hackerone.com/reports/3576823)
  program Nextcloud, weakness Server-Side Request Forgery (SSRF), severity Medium, bounty $250 (HackerOne Hacktivity)

## Experts worth reading

- [fg0x0](https://hackerone.com/fg0x0?type=user) - disclosed HackerOne reports
  - [Connector/ODBC: MADB_Stmt::ArrayOffset is not reset when an exception unwinds out of MADB_StmtExecute, so the next paramset reads out of bounds](https://hackerone.com/reports/3920647)
  - [Connector/ODBC: SqlwcsOctetLen sizes UTF-16 with a byte-oriented helper, reading past the caller's buffer and sending client memory to the server](https://hackerone.com/reports/3920633)
- [James Kettle](https://portswigger.net/research/james-kettle) - HTTP desync, request smuggling, cache poisoning, research automation
  - [HTTP desync attacks](https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn)
  - [hunting unknown vulnerability classes](https://portswigger.net/research/backslash-powered-scanning-hunting-unknown-vulnerability-classes)
- [sumit-sabhaya](https://hackerone.com/sumit-sabhaya?type=user) - disclosed HackerOne reports
  - [Billion laughs entity expansion in Qt .ts discovery: a crafted ~950 KB file forces ~55 MB of XML expansion per parse, cost scales with crafted file c](https://hackerone.com/reports/4094236)
  - [Incomplete VCS metadata exclusion: `.svn` / `.bzr` bypass CVE-2026-61792 due to missing `VCS_METADATA_DIRS` entries.](https://hackerone.com/reports/4037976)
- [Zakhar Fedotkin](https://portswigger.net/research/zakhar-fedotkin) - SAML, cookie prefixes, WebSocket testing, client-side parser tricks
  - [The Fragile Lock: Novel Bypasses For SAML Authentication](https://portswigger.net/research/the-fragile-lock)
  - [WebSocket Turbo Intruder: Unearthing the WebSocket Goldmine](https://portswigger.net/research/websocket-turbo-intruder-unearthing-the-websocket-goldmine)
- [Gareth Heyes](https://portswigger.net/research/gareth-heyes) - XSS, parser differentials, CSP bypass, client-side exfiltration
  - [CSS:the bomb inside your inbox](https://portswigger.net/research/css-the-bomb-inside-your-inbox)
  - [Splitting the email atom: exploiting parsers to bypass access controls](https://portswigger.net/research/splitting-the-email-atom)
- [0xbs0d27](https://hackerone.com/0xbs0d27?type=user) - disclosed HackerOne reports
  - [WordCamp Meta gpre: password-protected event RSVP list readable without password via /gpre/v1/.../rsvp-responses](https://hackerone.com/reports/4029867)
  - [wordpress.org Rosetta: invite stores unvalidated role — Editor can assign site Administrator despite editable_roles](https://hackerone.com/reports/3942522)
- [stze](https://hackerone.com/stze?type=user) - disclosed HackerOne reports
  - [wolfSSL TLS sessions retain native-CA trust after the application narrows trust](https://hackerone.com/reports/4122227)
  - [OpenSSL `--cert-status` accepts indefinitely stale GOOD OCSP staples](https://hackerone.com/reports/4125601)
- [matty69v](https://hackerone.com/matty69v?type=user) - disclosed HackerOne reports
  - [Unauthenticated arbitrary local file read via ABCpdf on www.████████](https://hackerone.com/reports/4191812)
  - [Cross-account stored XSS on app.basecamp.com leads to persistent administrator takeover](https://hackerone.com/reports/4175245)

## Tool shelf

### agentic

- [usestrix/strix](https://github.com/usestrix/strix) - 76933 stars. Open-source AI penetration testing tool to find and fix your app’s vulnerabilities. - usestrix/strix
- [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) - 52166 stars. Shannon is an AI pentester for web applications and APIs. It analyzes your source code, identifies attack vectors, and e
- [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) - 34751 stars. Fully autonomous AI Agents system capable of performing complex penetration testing tasks - vxcontrol/pentagi
- [GreyDGL/PentestGPT](https://github.com/GreyDGL/PentestGPT) - 16543 stars. Automated Penetration Testing Agentic Framework Powered by Large Language Models - GreyDGL/PentestGPT
- [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) - 16076 stars. A Claude Code skill bundle for bug hunting and external red-team work - 82 skills, 15 slash commands, 681 disclosed-repo
- [CyberStrikeus/CyberStrike](https://github.com/CyberStrikeus/CyberStrike) - 3672 stars. Open-source AI-powered offensive security harness for automated penetration testing. - CyberStrikeus/CyberStrike
- [Armur-Ai/Pentest-Swarm-AI](https://github.com/Armur-Ai/Pentest-Swarm-AI) - 3277 stars. Autonomous penetration testing using a swarm of AI agents. Orchestrates recon, classification, exploitation, and reporti
- [xalgorix/xalgorix](https://github.com/xalgorix/xalgorix) - 1381 stars. Open-source AI penetration testing agent that exploit-verifies every finding. Autonomous 22-phase pentests of web apps &

### audit defense

- [aquasecurity/trivy](https://github.com/aquasecurity/trivy) - 39601 stars. Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds and more - a
- [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks) - 31246 stars. Find secrets with Gitleaks 🔑. Contribute to gitleaks/gitleaks development by creating an account on GitHub.
- [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog) - 29565 stars. Find, verify, and analyze leaked credentials. Contribute to trufflesecurity/trufflehog development by creating an accoun
- [returntocorp/semgrep](https://github.com/returntocorp/semgrep) - 17880 stars. Lightweight static analysis for many languages. Find bug variants with patterns that look like source code. - semgrep/se
- [CISOfy/lynis](https://github.com/CISOfy/lynis) - 16738 stars. Lynis - Security auditing tool for Linux, macOS, and UNIX-based systems. Assists with compliance testing (HIPAA/ISO27001
- [anchore/grype](https://github.com/anchore/grype) - 13319 stars. A vulnerability scanner for container images and filesystems - anchore/grype
- [fuzzdb-project/fuzzdb](https://github.com/fuzzdb-project/fuzzdb) - 9010 stars. Dictionary of attack patterns and primitives for black-box application fault injection and resource discovery. - fuzzdb-

### cloud ad

- [jpillora/chisel](https://github.com/jpillora/chisel) - 16803 stars. A fast TCP/UDP tunnel over HTTP. Contribute to jpillora/chisel development by creating an account on GitHub.
- [fortra/impacket](https://github.com/fortra/impacket) - 16293 stars. Impacket is a collection of Python classes for working with network protocols. - fortra/impacket
- [BishopFox/sliver](https://github.com/BishopFox/sliver) - 12393 stars. Adversary Emulation Framework. Contribute to BishopFox/sliver development by creating an account on GitHub.
- [BloodHoundAD/BloodHound](https://github.com/BloodHoundAD/BloodHound) - 10631 stars. Six Degrees of Domain Admin. Contribute to SpecterOps/BloodHound-Legacy development by creating an account on GitHub.
- [HavocFramework/Havoc](https://github.com/HavocFramework/Havoc) - 8505 stars. The Havoc Framework. Contribute to HavocFramework/Havoc development by creating an account on GitHub.
- [lgandx/Responder](https://github.com/lgandx/Responder) - 6689 stars. Responder is a LLMNR, NBT-NS and MDNS poisoner, with built-in HTTP/SMB/MSSQL/FTP/LDAP rogue authentication server suppor
- [GhostPack/Rubeus](https://github.com/GhostPack/Rubeus) - 5238 stars. Trying to tame the three-headed dog. Contribute to GhostPack/Rubeus development by creating an account on GitHub.
- [nicocha30/ligolo-ng](https://github.com/nicocha30/ligolo-ng) - 5198 stars. An advanced, yet simple, tunneling/pivoting tool that uses a TUN interface. - nicocha30/ligolo-ng

### mobile binary

- [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) - 100895 stars. Ghidra is a software reverse engineering (SRE) framework - NationalSecurityAgency/ghidra
- [skylot/jadx](https://github.com/skylot/jadx) - 51929 stars. Dex to Java decompiler. Contribute to skylot/jadx development by creating an account on GitHub.
- [iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool) - 27322 stars. A tool for reverse engineering Android apk files. Contribute to iBotPeaches/Apktool development by creating an account o
- [radareorg/radare2](https://github.com/radareorg/radare2) - 25478 stars. UNIX-like reverse engineering framework and command-line toolset - radareorg/radare2
- [frida/frida](https://github.com/frida/frida) - 22885 stars. Main repo for hosting release binaries. Contribute to frida/frida development by creating an account on GitHub.
- [MobSF/Mobile-Security-Framework-MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) - 22290 stars. Mobile Security Framework (MobSF) is an automated, all-in-one mobile application (Android/iOS/Windows) pen-testing, malw
- [Gallopsled/pwntools](https://github.com/Gallopsled/pwntools) - 13882 stars. CTF framework and exploit development library. Contribute to Gallopsled/pwntools development by creating an account on G
- [sensepost/objection](https://github.com/sensepost/objection) - 9530 stars. 📱 objection - runtime mobile exploration. Contribute to sensepost/objection development by creating an account on GitHub

### osint surface

- [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) - 115488 stars. Hunt down social media accounts by username across social networks - sherlock-project/sherlock
- [soxoj/maigret](https://github.com/soxoj/maigret) - 41134 stars. 🕵️‍♂️ Collect a dossier on a person by username from 6K websites - soxoj/maigret
- [lissy93/web-check](https://github.com/lissy93/web-check) - 35560 stars. 🕵️‍♂️ All-in-one OSINT tool for analysing any website - lissy93/web-check
- [smicallef/spiderfoot](https://github.com/smicallef/spiderfoot) - 24815 stars. SpiderFoot automates OSINT for threat intelligence and mapping your attack surface. - smicallef/spiderfoot
- [mxrch/GHunt](https://github.com/mxrch/GHunt) - 19886 stars. 🕵️‍♂️ Offensive Google framework. Contribute to mxrch/GHunt development by creating an account on GitHub.
- [sundowndev/phoneinfoga](https://github.com/sundowndev/phoneinfoga) - 18647 stars. Information gathering framework for phone numbers. Contribute to sundowndev/phoneinfoga development by creating an accou
- [laramies/theHarvester](https://github.com/laramies/theHarvester) - 18379 stars. E-mails, subdomains and names Harvester - OSINT . Contribute to laramies/theHarvester development by creating an account
- [yogeshojha/rengine](https://github.com/yogeshojha/rengine) - 8956 stars. reNgine is an automated reconnaissance framework for web applications with a focus on highly configurable streamlined re

### re-binary

- [lief](lief-project/LIEF) - ? stars. Parse and modify ELF, PE, and Mach-O.
- [pefile](erocarrera/pefile) - ? stars. Python PE parser.
- [pyelftools](eliben/pyelftools) - ? stars. Python ELF and DWARF parser.
- [capstone](capstone-engine/capstone) - ? stars. Disassembly framework.

### re-capability

- [capa](mandiant/capa) - ? stars. Identify capabilities from imports and structure.
- [floss](mandiant/flare-floss) - ? stars. Extract obfuscated and stack strings.

### re-debugger

- [x64dbg](x64dbg/x64dbg) - ? stars. Windows user-mode debugger.
- [windbg](Microsoft WinDbg) - ? stars. Windows kernel and user-mode debugger with TTD.
- [pwndbg](pwndbg/pwndbg) - ? stars. GDB plugin for exploit development and heap inspection.
- [gef](hugsy/gef) - ? stars. GDB plugin with exploit-oriented views.
- [rr](rr-debugger/rr) - ? stars. Record and replay execution for Linux.

### re-diff

- [bindiff](google/bindiff) - ? stars. Binary similarity for patch analysis.
- [diaphora](joxeankoret/diaphora) - ? stars. IDA plugin for binary diffing.
- [ghidriff](clearbluejar/ghidriff) - ? stars. Ghidra headless patch diffing.

### re-disassembler

- [ghidra](NationalSecurityAgency/ghidra) - ? stars. NSA reverse-engineering framework with decompiler and headless mode.
- [binaryninja](Vector35/binaryninja-api) - ? stars. Commercial reverse-engineering platform with BNIL and Python API. Headless needs a license.
- [ida](hex-rays/ida) - ? stars. Industry decompiler and plugin ecosystem. IDA Free is limited.
- [rizin](rizinorg/rizin) - ? stars. Command-first binary analysis framework and radare2 fork.
- [radare2](radareorg/radare2) - ? stars. Long-running command-line reverse-engineering framework.

### re-dynamic

- [frida](frida/frida) - ? stars. Dynamic instrumentation toolkit for native and managed code.
- [objection](sensepost/objection) - ? stars. Frida-powered mobile runtime exploration.
- [dynamorio](DynamoRIO/dynamorio) - ? stars. Dynamic binary instrumentation framework.
- [pin](intel/pin) - ? stars. Intel dynamic instrumentation.

### re-firmware

- [unblob](onekey-sec/unblob) - ? stars. Recursive extractor for 78+ container formats.
- [binwalk](ReFirmLabs/binwalk) - ? stars. Firmware signature scanner and extractor.
- [emba](e-m-b-a/emba) - ? stars. Firmware security analyzer.
- [firmae](pr0v3rbs/FirmAE) - ? stars. Full-system firmware emulation.
- [qemu](qemu/qemu) - ? stars. Emulator and virtual machine.

### re-fuzzing

- [aflpp](AFLplusplus/AFLplusplus) - ? stars. Coverage-guided fuzzer.
- [libfuzzer](llvm/llvm-project) - ? stars. In-process coverage-guided fuzzer.
- [honggfuzz](google/honggfuzz) - ? stars. Coverage-guided fuzzer with hardware feedback.
- [syzkaller](google/syzkaller) - ? stars. Kernel syscall fuzzer.
- [casr](ispras/casr) - ? stars. Crash report collection, deduplication, and severity.
- [nyx](nyx-fuzz/Nyx) - ? stars. Snapshot fuzzing engine for AFL++.
- [snapchange](awslabs/snapchange) - ? stars. Snapshot fuzzing for Linux kernel targets.

### re-gui

- [cutter](rizinorg/cutter) - ? stars. Qt GUI for rizin.

### re-mobile

- [mobsf](MobSF/Mobile-Security-Framework-MobSF) - ? stars. Static and dynamic mobile app analysis.
- [jadx](skylot/jadx) - ? stars. DEX to Java decompiler.
- [apktool](iBotPeaches/Apktool) - ? stars. APK resource and smali unpacker.

### re-network

- [wireshark](wireshark/wireshark) - ? stars. Protocol analyzer.
- [mitmproxy](mitmproxy/mitmproxy) - ? stars. Interactive HTTPS proxy.

### re-signature

- [yara](VirusTotal/yara) - ? stars. Pattern matching for malware families and packers.

### re-source

- [codeql](github/codeql) - ? stars. Semantic code query engine with data flow.
- [joern](joernio/joern) - ? stars. Code property graph query engine.
- [semgrep](semgrep/semgrep) - ? stars. Fast rule-based static analysis.
- [weggli](weggli/weggli) - ? stars. Fast C/C++ syntax query tool.
- [cppcheck](danmar/cppcheck) - ? stars. C/C++ static analyzer.
- [infer](facebook/infer) - ? stars. Static analyzer for Java, C, C++, and Objective-C.

### re-symbolic

- [angr](angr/angr) - ? stars. Python symbolic execution and binary analysis.
- [triton](JonathanSalwan/Triton) - ? stars. Dynamic symbolic execution library.
- [miasm](cea-sec/miasm) - ? stars. Reverse-engineering and symbolic execution framework.
- [klee](klee/klee) - ? stars. Symbolic execution on LLVM bitcode.

### recon

- [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei) - 33181 stars. Nuclei is a fast, customizable vulnerability scanner powered by the global security community and built on a simple YAML
- [projectdiscovery/katana](https://github.com/projectdiscovery/katana) - 17880 stars. A next-generation crawling and spidering framework. - projectdiscovery/katana
- [ffuf/ffuf](https://github.com/ffuf/ffuf) - 17096 stars. Fast web fuzzer written in Go. Contribute to ffuf/ffuf development by creating an account on GitHub.
- [owasp-amass/amass](https://github.com/owasp-amass/amass) - 15546 stars. In-depth attack surface mapping and asset discovery - owasp-amass/amass
- [maurosoria/dirsearch](https://github.com/maurosoria/dirsearch) - 15106 stars. Web path scanner. Contribute to maurosoria/dirsearch development by creating an account on GitHub.
- [projectdiscovery/subfinder](https://github.com/projectdiscovery/subfinder) - 14845 stars. Fast passive subdomain enumeration tool. Contribute to projectdiscovery/subfinder development by creating an account on 
- [OJ/gobuster](https://github.com/OJ/gobuster) - 14342 stars. Directory/File, DNS and VHost busting tool written in Go - OJ/gobuster
- [aboul3la/Sublist3r](https://github.com/aboul3la/Sublist3r) - 11099 stars. Fast subdomains enumeration tool for penetration testers - aboul3la/Sublist3r

### web

- [swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) - 82844 stars. A list of useful payloads and bypass for Web Application Security and Pentest/CTF - swisskyrepo/PayloadsAllTheThings
- [danielmiessler/SecLists](https://github.com/danielmiessler/SecLists) - 74877 stars. SecLists is the security tester's companion. It's a collection of multiple types of lists used during security assessmen
- [sqlmapproject/sqlmap](https://github.com/sqlmapproject/sqlmap) - 39010 stars. Automatic SQL injection and database takeover tool - sqlmapproject/sqlmap
- [s0md3v/XSStrike](https://github.com/s0md3v/XSStrike) - 15277 stars. Most advanced XSS scanner. Contribute to s0md3v/XSStrike development by creating an account on GitHub.
- [projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates) - 13383 stars. Community curated list of templates for the nuclei engine to find security vulnerabilities. - projectdiscovery/nuclei-te
- [chaitin/xray](https://github.com/chaitin/xray) - 11798 stars. 一款长亭自研的完善的安全评估工具，支持常见 web 安全问题扫描和自定义 poc \| 使用之前务必先阅读文档 - chaitin/xray
- [sullo/nikto](https://github.com/sullo/nikto) - 10870 stars. Nikto web server scanner. Contribute to sullo/nikto development by creating an account on GitHub.
- [wpscanteam/wpscan](https://github.com/wpscanteam/wpscan) - 9862 stars. WPScan WordPress security scanner. Written for security professionals and blog maintainers to test the security of their

## Method index

- [HTTP Request Smuggling Research](https://portswigger.net/research/request-smuggling) - PortSwigger Research
- [Template Injection Research](https://portswigger.net/research/template-injection) - PortSwigger Research
- [Top 10 Web Hacking Techniques](https://portswigger.net/research/top-10-web-hacking-techniques) - PortSwigger Research
- [CSS:the bomb inside your inbox](https://portswigger.net/research/css-the-bomb-inside-your-inbox) - PortSwigger Research (68 code blocks)
- [CRLF-Powered Desync Attacks: Beheading HTTP Streams](https://portswigger.net/research/crlf-powered-desync-attacks) - PortSwigger Research (90 code blocks)
- [Can AI do novel security research? Meet the HTTP Terminator](https://portswigger.net/research/can-ai-do-novel-security-research) - PortSwigger Research (87 code blocks)
- [The Fragile Lock: Novel Bypasses For SAML Authentication](https://portswigger.net/research/the-fragile-lock) - PortSwigger Research (12 code blocks)
- [Achieving the impossible: XSS in innerHTML without equals](https://portswigger.net/research/achieving-the-impossible-xss-in-innerhtml-without-equals) - PortSwigger Research (75 code blocks)
- [Blind trust: stealing credentials through CSP](https://portswigger.net/research/blind-trust-stealing-credentials-through-csp) - PortSwigger Research (24 code blocks)
- [Making HTTP header injection critical with one prompt](https://portswigger.net/research/making-http-header-injection-critical-with-one-prompt) - PortSwigger Research (8 code blocks)
- [Probably Not Exploitable](https://projectdiscovery.io/blog/probably-not-exploitable) - ProjectDiscovery Blog
- [Introducing Neo Triage — ProjectDiscovery Blog](https://projectdiscovery.io/blog/introducing-neo-triage) - ProjectDiscovery Blog
- [Neo v1 is now available for everyone — ProjectDiscovery Blog](https://projectdiscovery.io/blog/neo-v1) - ProjectDiscovery Blog
- [Beyond the Model: Neo Hunts, Exploits, and Proves 22 Zero-Days.](https://projectdiscovery.io/blog/everyone-is-finding-vulns-the-hard-part-is-proving-them) - ProjectDiscovery Blog (63 code blocks)
- [Inside the benchmark: app architectures, walkthroughs of findings, and what each scanner actually caught](https://projectdiscovery.io/blog/inside-the-benchmark-pp-architectures-finding-walkthroughs-and-what-each-scanner-actually-caught) - ProjectDiscovery Blog (37 code blocks)
- [Nuclei Templates - April 2026](https://projectdiscovery.io/blog/nuclei-templates-april-2026) - ProjectDiscovery Blog (24 code blocks)
- [Open by design, trusted by enterprises: how we keep Nuclei templates reliable at scale](https://projectdiscovery.io/blog/open-by-design-trusted-by-enterprises-how-we-keep-nuclei-templates-reliable-at-scale) - ProjectDiscovery Blog
- [Nuclei Templates Monthly - May 2025](https://projectdiscovery.io/blog/nuclei-templates-monthly-may-2025) - ProjectDiscovery Blog (8 code blocks)
- [Hacking with AI: How to prevent your AI from going rogue](https://www.intigriti.com/researchers/blog/hacking-tools/hacking-with-ai-how-to-prevent-your-ai-from-going-rogue) - Intigriti
- [PHP2Shell revisited: What Intigriti’s insights tell us about real-world risk](https://www.intigriti.com/researchers/blog/news/php2shell-revisited-real-world-risk) - Intigriti (1 code blocks)
- [Intigriti Bug Bytes #241 - October 2026 🚀](https://www.intigriti.com/researchers/blog/bug-bytes/intigriti-bug-bytes-241-october-2026) - Intigriti (2 code blocks)
- [Exploiting LLM prompt injection vulnerabilities](https://www.intigriti.com/researchers/blog/hacking-tools/exploiting-advanced-llm-prompt-injection-vulnerabilities) - Intigriti (3 code blocks)
- [Understanding PHP2Shell: Everything you need to know about CVE-2026-109618 & CVE-2026-109619](https://www.intigriti.com/researchers/blog/news/php2shell) - Intigriti (11 code blocks)
- [The Exposure Debt Benchmark: What the 2026 Data Says About the Find-to-Fix Gap](https://www.hackerone.com/blog/exposure-management-find-to-fix-gap-2026) - HackerOne Blog
- [Make no mistakes: Blameless postmortems in an age of agents](https://www.hackerone.com/blog/make-no-mistakes-blameless-postmortems-in-an-age-of-agents) - HackerOne Blog
- [National Vulnerability Database Modernization in the Age of AI](https://www.hackerone.com/blog/nvd-modernization-vulnerability-prioritization) - HackerOne Blog
- [Your Releases Outpace Your Testing. It’s Time to Close the Gap.](https://www.hackerone.com/blog/continuous-security-validation-web-apps-apis) - HackerOne Blog
- [AI Security Has an Accountability Problem: What Our Latest Data Says About Who Owns the Call](https://www.hackerone.com/blog/ai-security-accountability) - HackerOne Blog
- [Measuring The Fix: How We Evaluate Frontier Models on Remediation Quality](https://www.hackerone.com/blog/measuring-the-fix-ctem-remediation-quality) - HackerOne Blog
- [Critical PHP Vulnerabilities: What Security Teams Need to Know](https://www.hackerone.com/blog/critical-php-vulnerabilities-hackerone-response) - HackerOne Blog
- [What’s New for HackerOne Researchers](https://www.hackerone.com/blog/whats-new-for-hackerone-researchers) - HackerOne Blog
- [How Model Evolution Has Reshaped Security AI Agents on H1 Platform](https://www.hackerone.com/blog/how-model-evolution-reshaped-ai-security-agents) - HackerOne Blog
- [Lost Book of the Forbidden Syscalls](https://0x00sec.org/deep-dive-series/) - 0x00sec
- [ZIP Parser Differentials and Mutable Encrypted Filenames - Part I](https://0x00sec.org/zip-parser-differentials-and-mutable-encrypted-filenames-part-i/) - 0x00sec (49 code blocks)
- [Lost Book of the Forbidden Syscalls](https://0x00sec.org/lbofs-debugging-and-anti-debugging-fun-with-ptrace-i/) - 0x00sec (122 code blocks)
- [reverse-engineering - 0x00sec](https://0x00sec.org/tag/reverse-engineering/) - 0x00sec
- [X86_64 Linux Remote Stack Overflow Exploitation — bypass PIE via format string information leak (Part 3)](https://0x00sec.org/x86_64-linux-remote-stack-overflow-exploitation-bypass-pie-via-format-string-information-leak-part-3/) - 0x00sec (31 code blocks)
- [X86_64 Linux Remote Stack Overflow Exploitation - ret2plt (part 2)](https://0x00sec.org/x86_64-linux-remote-stack-overflow-exploitation-ret2plt-part-2/) - 0x00sec (33 code blocks)
- [X86_64 Linux Remote Stack Overflow Exploitation -The Basic](https://0x00sec.org/x86_64-linux-remote-stack-overflow-exploitation-the-basic/) - 0x00sec
- [HackTricks](https://book.hacktricks.wiki/) - HackTricks (5 code blocks)

## Gaps and next passes

- Fewer than half of the threads have summaries. Run `extract.py` on the top URLs.
- Re-run monthly. Forum threads and tool stars move; disclosed reports age out of the first pages.
