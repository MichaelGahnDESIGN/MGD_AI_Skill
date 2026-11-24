# Vibecoding Setup

Ein kleiner, sicherer Einrichtungs-Assistent für den MGD-Vibe-Coding-Workflow.
Er installiert ausgewählte öffentliche MIT-Skills für ChatGPT Codex, Claude Code
oder kompatible Agenten. Der Standard ist ein Trockenlauf; bestehende Skills
werden nie überschrieben.

```bash
python3 scripts/install_mgd_skills.py --target codex --profile core
python3 scripts/install_mgd_skills.py --target codex --profile core --apply
```

Die Seite **Vibe Coding** auf [Michael-Gahn.de](https://michael-gahn.de) erklärt
den Workflow, die Skills und passende Startprompts.

## Profile

- `core`: Todo, DEV, Thread und Living Documentation.
- `studio`: zusätzlich Divi 5 Dev, Autopilot, PlayTest und ProjectClean.

Drittquellen wie ECC, Hallmark und Superpowers werden im Assistenten und auf der
Website separat erklärt. Sie sind nicht Teil einer automatischen Installation:
Lizenz, Kosten, Abhängigkeiten und Quelle sind vorher konkret zu prüfen.

## Lizenz

MIT
