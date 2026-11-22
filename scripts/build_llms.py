import os

FILES = [
    "AGENTS.md", "CLAUDE.md", "GEMINI.md", "SKILL.md", "agents/router.md",
    "agents/reverse-engineer.md", "agents/crash-triager.md", "agents/fuzzing-engineer.md",
    "agents/firmware-analyst.md", "agents/mentor.md",
    "references/techniques.md", "references/reverse-engineering.md",
    "references/vulnerability-research.md", "references/fuzzing.md",
    "references/exploit-development.md", "references/mobile-reverse.md",
    "references/firmware-iot.md", "references/curriculum.md",
    "references/exercises.md", "references/self-training.md",
    "references/scan-artifacts.md" if False else "docs/scan-artifacts.md",
    "docs/reverse-engineering.md", "docs/training.md", "docs/agents.md", "docs/break-my-app.md",
]

with open("llms-full.txt", "w", encoding="utf-8") as out:
    out.write("# Beril full context\n\n")
    out.write("Generated from the markdown sources. Prefer the split files when context is tight.\n\n")
    for path in FILES:
        if not os.path.exists(path):
            continue
        out.write(f"\n\n<!-- ===== {path} ===== -->\n\n")
        out.write(open(path, encoding="utf-8").read())
print("wrote llms-full.txt")
