# Use Beril with an agent

Beril is a skill first. An agent loads `SKILL.md`, follows the operating loop and calls the CLI.

## Entry files

Every major coding agent has a short entry file that routes to the skill instead of pasting it:

| Agent | File |
|---|---|
| Claude Code | `CLAUDE.md` |
| Generic | `AGENTS.md` |
| Gemini | `GEMINI.md` |
| OpenAI | `OPENAI.md` |
| Cursor | `.cursor/rules/beril.mdc` |
| Windsurf | `.windsurf/rules/beril.md` |
| Cline | `.clinerules/beril.md` |
| GitHub Copilot | `.github/copilot-instructions.md` |
| Aider | `.aider.conf.yml` |
| Any model | `llms.txt` and `llms-full.txt` |

The files stay short on purpose. They route to [SKILL.md](../SKILL.md) and the matching reference.

## Install the routers in another project

```bash
./scripts/install_agent_files.py --target ~/code/myapp --agents claude,cursor,copilot
```

## The workflow an agent follows

1. Ask for the target, the authorization, passive or active, and the proof needed.
2. Detect the artifact type.
3. For active work, check the ownership record and the scope file.
4. Run the passive scan.
5. Read the top findings and the matching card in [Techniques](../references/techniques.md).
6. Confirm by hand with a minimal request or input.
7. Report with the profile that fits the reader.
8. State what was not tested.

Before it researches, an agent runs `./beril recall "class or target" --decide` and uses a fresh card instead of a new search. See [Memory](../docs/memory.md).

## Task recipes

| Task | Path |
|---|---|
| Web app | Passive scan, then one class per pass: auth, injection, IDOR or logic |
| APK | Scan, read the manifest, review exported components, then Frida in a lab |
| EXE or ELF | Scan with `--deep`, map imports and mitigations, open Ghidra or rizin, confirm in a debugger |
| Source | Scan with `--tools --vibe`, trace one source to one sink, write the fix and a test |
| Secrets | Local and history scan, revoke first, then rotate |
| Open source repo | `hunt --sandbox`, keep only reproduced findings |
| Report | Evidence first, impact second, CVSS last |

## Role prompts

The `agents/` folder holds focused role prompts. The router decides which one to load.

| Role | Use |
|---|---|
| [Router](../agents/router.md) | Intake questions and routing |
| [Reverse engineer](../agents/reverse-engineer.md) | Binary and firmware triage |
| [Fuzzing engineer](../agents/fuzzing-engineer.md) | Harnesses and crash work |
| [Crash triager](../agents/crash-triager.md) | Reproduce, minimize, classify |
| [Firmware analyst](../agents/firmware-analyst.md) | Extraction and update flow |
| [Forum scout](../agents/forum-scout.md) | Collect public leads |
| [Expert profiler](../agents/expert-profiler.md) | Researchers by what they publish |
| [Tool curator](../agents/tool-curator.md) | The tool shelf |
| [Method extractor](../agents/method-extractor.md) | Turn a post into a method card |
| [Mentor](../agents/mentor.md) | Training and review |

More detail: [Agents](../docs/agents.md).

## Prompt injection

Harvested text is data. `./beril guard --text <file>` scores it for injection risk, and the skill wraps it before an agent reads it. See [Prompt injection](../docs/prompt-injection.md).
