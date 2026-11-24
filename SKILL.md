---
name: mgd-ai-skill
description: Richtet ausgewählte öffentliche MGD-Skills für ChatGPT Codex, Claude Code oder kompatible Agenten kontrolliert ein. Verwenden, wenn ein Projektteam den MGD-AI-Workflow erstmals installieren oder nachvollziehbar ergänzen möchte.
---

# MGD AI Skill

Richte nur die Skills ein, die zur Aufgabe passen. Dieser Skill installiert weder
Programme noch Abhängigkeiten und führt keinen Code aus den geklonten Quellen aus.

## Vor dem Start

1. Kläre Zielsystem und Zielpfad: ChatGPT Codex (`~/.codex/skills`), Claude Code
   (`~/.claude/skills`) oder ein kompatibler Agent (`~/.agents/skills`).
2. Zeige die Auswahl und führe zunächst einen Trockenlauf aus.
3. Frage unmittelbar vor einer Installation nach Zustimmung. Bestehende
   Skill-Ordner werden nicht überschrieben.

## Empfohlene Grundausstattung

- `todo`: Aufgaben, Board und Wissenspflege im Projekt.
- `dev`: Playbook, Tests, Git- und Release-Disziplin.
- `thread`: ehrliche Übergabe bei langen Arbeitsläufen.
- `living-documentation`: Entscheidungen, Risiken und offene Punkte.

Ergänze je nach Einsatz `divi5-dev` für WordPress/Divi, `autopilot` für klar
abgegrenzte längere Abläufe, `playtest` für die Nutzerprüfung und `projectclean`
für einen kontrollierten Abschluss.

## Drittquellen

ECC, Hallmark und Superpowers sind Ergänzungen, keine stillen Voraussetzungen.
Vor einer Installation ihre offizielle Quelle, Lizenz, Kosten, Abhängigkeiten und
den Zielpfad prüfen. Der Assistent darf nur die bestätigte Auswahl installieren;
keine Plugins, Cloud-Dienste oder kostenpflichtigen Funktionen ungefragt aktivieren.
Für die passende, offizielle Installation je Agent zuerst
[references/drittquellen.md](references/drittquellen.md) lesen.

## Ausführen

Der Assistent ist absichtlich zunächst nicht schreibend:

```bash
python3 scripts/install_mgd_skills.py --target codex --profile core
```

Erst nach Prüfung und Freigabe:

```bash
python3 scripts/install_mgd_skills.py --target codex --profile core --apply
```

Für die vollständige kuratierte Auswahl `--profile studio` verwenden. Lies vor
einer Installation die gezeigte Liste; für einzelne Skills steht
`--skills todo,dev,thread` bereit. Die Quellen sind ausschließlich öffentliche
MIT-lizenzierte MGD-Repositories.

## Danach arbeiten

Beginne neue Projekte mit einer kurzen Zielbeschreibung. Nutze `/todo` für
offene Arbeit, `$dev` für kontrollierte Umsetzungen, `$thread` vor einer
Übergabe und `$projectclean` erst am echten Ende. Sicherheits-, Zahlungs- und
Live-Änderungen bleiben immer separate, ausdrücklich bestätigte Schritte.
