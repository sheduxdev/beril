import os

FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    "OPENAI.md",
    "SKILL.md",
    "agents/router.md",
    "agents/front-desk.md",
    "agents/reverse-engineer.md",
    "agents/crash-triager.md",
    "agents/fuzzing-engineer.md",
    "agents/firmware-analyst.md",
    "agents/mentor.md",
    "references/techniques.md",
    "references/bug-method-matrix.md",
    "references/reverse-engineering.md",
    "references/vulnerability-research.md",
    "references/fuzzing.md",
    "references/exploit-development.md",
    "references/mobile-reverse.md",
    "references/firmware-iot.md",
    "references/ghidra-ecosystem.md",
    "references/rust-reverse.md",
    "references/re-plugin-index.md",
    "references/github-atlas.md",
    "references/claude-bughunter.md",
    "references/artex.md",
    "references/artex-flask.md",
    "references/curriculum.md",
    "references/exercises.md",
    "references/self-training.md",
    "references/books.md",
    "references/finding-schema.md",
    "references/maintainer-report.md",
    "docs/mastery.md",
    "docs/scan-artifacts.md",
    "docs/recon.md",
    "docs/reverse-engineering.md",
    "docs/training.md",
    "docs/agents.md",
    "docs/break-my-app.md",
    "docs/dashboard.md",
    "docs/memory.md",
    "knowledge/INDEX.md",
    "knowledge/GAPS.md",
    "docs/attacking.md",
    "docs/defending.md",
    "docs/report-format.md",
    "docs/verification.md",
    "docs/secrets.md",
    "docs/prompt-injection.md",
    "docs/bug-hunt.md",
    "docs/legal.md",
]

with open("llms-full.txt", "w", encoding="utf-8") as out:
    out.write("# Beril full context\n\n")
    out.write("Generated from the markdown sources. Prefer the split files when context is tight.\n\n")
    for path in dict.fromkeys(FILES):
        if not os.path.exists(path):
            continue
        out.write(f"\n\n<!-- ===== {path} ===== -->\n\n")
        with open(path, encoding="utf-8") as handle:
            out.write(handle.read())
print("wrote llms-full.txt")
