# Drittquellen: Auswahl und Installation

Diese drei Ergänzungen sind MIT-lizenziert und öffentlich. Sie bedienen jedoch
unterschiedliche Zwecke und Installationskanäle. Vor jedem Befehl den Agenten,
den Zielpfad und mögliche Kosten bestätigen.

| Werkzeug | Wann sinnvoll | Offizielle Quelle | Wichtige Grenze |
| --- | --- | --- | --- |
| ECC | Viele spezialisierte Skills, Sicherheits- und Qualitätsabläufe | https://github.com/affaan-m/ECC | Die kostenlose OSS-Basis und optionale Pro-Angebote klar trennen. Nur einen ECC-Installationsweg pro Agent verwenden. |
| Hallmark | Design-Audit oder neue, hochwertige Oberflächen | https://github.com/Nutlope/hallmark | Browser-Renderchecks benötigen zusätzlich Chrome und Puppeteer; nicht ungefragt global installieren. |
| Superpowers | Planungs- und Entwicklungsworkflow in einem unterstützten Plugin-Marktplatz | https://github.com/obra/superpowers | Je Agent separat über dessen offiziellen Plugin-Marktplatz installieren. |

## Sichere Reihenfolge

1. Nur die offizielle URL öffnen und Lizenz sowie aktuelle Installationshinweise
   lesen.
2. Wenn möglich den offiziellen Trockenlauf ausführen. Für ECC etwa:
   `npx ecc-universal@2.2.3 install --guided --harness codex --dry-run`.
3. Die angezeigten Ziele, Hooks, Plugins und Kostenhinweise mit dem Nutzer
   bestätigen.
4. Genau einen bestätigten Installationsweg ausführen und danach den jeweiligen
   Agenten neu starten.

## Konkrete Startpunkte

- **ECC:** für Codex und Claude Code den offiziellen geführten Installer nutzen;
  bei mehreren Agenten `npx ecc-universal@2.2.3 install --guided`. Nie den
  manuellen Sync zusätzlich zur Marketplace-/Plugin-Installation stapeln.
- **Hallmark:** `npx skills add nutlope/hallmark -g` installiert global. Vorher
  Node 18+ und den gewünschten Agenten prüfen; ohne `-g` bleibt die Installation
  projektlokal.
- **Superpowers:** In Codex App das Plugin *Superpowers* im offiziellen
  Marketplace wählen. In Claude Code `/plugin install
  superpowers@claude-plugins-official` verwenden.

Die Befehle können sich ändern. Wenn der Nutzer eine Installation beauftragt,
die aktuellen Hinweise in den verlinkten offiziellen Quellen erneut prüfen.
