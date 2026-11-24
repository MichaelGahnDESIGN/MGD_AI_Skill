#!/usr/bin/env python3
"""Installiert kuratierte öffentliche MGD-Skills erst nach sichtbarer Planung.

Das Skript führt keinen Inhalt aus den Git-Repositories aus. Es lädt ausschließlich
öffentliche Quellen per Git und kopiert die jeweilige Skill-Struktur in den vom
Nutzer ausgewählten lokalen Agenten-Pfad. Vorhandene Ordner bleiben unverändert.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Skill:
    """Beschreibt eine geprüfte, MIT-lizenzierte öffentliche Quelle."""

    alias: str
    repository: str
    source_path: str
    description: str


SKILLS: dict[str, Skill] = {
    "todo": Skill("todo", "MGD_Todo_SKILL", ".", "Aufgaben, Board und Wissenspflege ohne externen Dienst."),
    "dev": Skill("dev", "MGD_DEV_SKILL", "dev", "Playbooks, Tests, Git-, Release- und Deployment-Disziplin."),
    "thread": Skill("thread", "MGD_AI-Thread", ".", "Nachvollziehbare Übergaben vor einem Kontextwechsel."),
    "living-documentation": Skill("living-documentation", "MGD_Living-Documentation", "skills/living-documentation", "Entscheidungen, Risiken und offene Punkte festhalten."),
    "divi5-dev": Skill("divi5-dev", "MGD_Divi5-Dev_SKILL", ".", "WordPress- und Divi-5-Entwicklung mit Datenschutzleitplanken."),
    "autopilot": Skill("autopilot", "MGD_Autopilot_SKILL", ".", "Längere, klar abgegrenzte Abläufe mit Prüfung nach jedem Schritt."),
    "playtest": Skill("playtest", "MGD_AI-PlayTest_SKILL", ".", "Nutzerorientierte Prüfung von KI-erstellten Funktionen."),
    "projectclean": Skill("projectclean", "MGD_ProjectClean_SKILL", ".", "Abschluss: Version, Tests, Dokumentation und bereinigter Stand."),
}

PROFILES = {"core": ("todo", "dev", "thread", "living-documentation"), "studio": tuple(SKILLS)}
TARGETS = {"codex": Path.home() / ".codex" / "skills", "claude": Path.home() / ".claude" / "skills", "generic": Path.home() / ".agents" / "skills"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Installiert ausgewählte öffentliche MGD-Skills kontrolliert.")
    parser.add_argument("--target", choices=TARGETS, required=True)
    parser.add_argument("--profile", choices=PROFILES, default="core")
    parser.add_argument("--skills", help="Kommagetrennte Auswahl statt Profil, z. B. todo,dev")
    parser.add_argument("--apply", action="store_true", help="Installation nach der angezeigten Planung ausführen.")
    parser.add_argument("--yes", action="store_true", help="Rückfrage nur zusammen mit --apply überspringen.")
    return parser.parse_args()


def selected_skills(args: argparse.Namespace) -> tuple[Skill, ...]:
    names = tuple(args.skills.split(",")) if args.skills else PROFILES[args.profile]
    unknown = sorted(set(names).difference(SKILLS))
    if unknown:
        raise ValueError(f"Unbekannte Skill-Kürzel: {', '.join(unknown)}")
    return tuple(SKILLS[name] for name in names)


def print_plan(skills: tuple[Skill, ...], destination: Path) -> None:
    print(f"Ziel: {destination}")
    print("Quellen: öffentliche MIT-Repositories von MichaelGahnDESIGN")
    for skill in skills:
        status = "existiert bereits – wird übersprungen" if (destination / skill.alias).exists() else "bereit"
        print(f"- {skill.alias}: {skill.description} [{status}]")


def clone_and_copy(skill: Skill, destination: Path, workspace: Path) -> None:
    checkout = workspace / skill.repository
    subprocess.run(["git", "clone", "--depth", "1", f"https://github.com/MichaelGahnDESIGN/{skill.repository}.git", str(checkout)], check=True)
    source = checkout / skill.source_path
    if not (source / "SKILL.md").is_file():
        raise RuntimeError(f"{skill.alias}: erwartete SKILL.md fehlt in {skill.source_path}")
    shutil.copytree(source, destination / skill.alias)


def main() -> int:
    args = parse_args()
    if args.yes and not args.apply:
        print("--yes ist nur zusammen mit --apply sinnvoll.", file=sys.stderr)
        return 2
    try:
        skills = selected_skills(args)
    except ValueError as error:
        print(error, file=sys.stderr)
        return 2
    destination = TARGETS[args.target]
    print_plan(skills, destination)
    if not args.apply:
        print("Trockenlauf beendet. Mit --apply wird nach einer Rückfrage installiert.")
        return 0
    installable = tuple(skill for skill in skills if not (destination / skill.alias).exists())
    if not installable:
        print("Keine Installation nötig: Alle ausgewählten Skill-Ordner existieren bereits.")
        return 0
    if not args.yes:
        answer = input("Jetzt nur die als bereit markierten Skills installieren? [ja/Nein] ").strip().lower()
        if answer not in {"ja", "j", "yes", "y"}:
            print("Abgebrochen. Es wurden keine Dateien verändert.")
            return 0
    destination.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="vibecoding-setup-") as temporary:
        workspace = Path(temporary)
        for skill in installable:
            clone_and_copy(skill, destination, workspace)
            print(f"Installiert: {skill.alias}")
    print("Fertig. Starte für jede Agenten-Umgebung einen neuen Chat oder lade die Skills neu.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
