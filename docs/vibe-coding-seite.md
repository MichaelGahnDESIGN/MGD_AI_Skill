# Vibe Coding

## KI-Agenten, die nicht nur Code schreiben – sondern sauber mitdenken.

Vibe Coding heißt bei Michael Gahn DESIGN nicht: „Mach mal schnell eine App.“
Es heißt: Ziel klären, Arbeit sichtbar planen, sicher umsetzen, prüfen und so
dokumentieren, dass der nächste Mensch oder Agent direkt weiterarbeiten kann.

**Die Regel:** Erst verstehen. Dann ändern. Danach beweisen, was wirklich
funktioniert.

**Startpunkt:** [Vibecoding Setup auf GitHub](https://github.com/MichaelGahnDESIGN/MGD_Vibecoding_Setup_SKILL)

---

## Der Ablauf in vier klaren Schritten

### 01 — Briefing statt Bauchgefühl

Sag dem Agenten, welches Ergebnis du brauchst, für wen es ist und was geschützt
bleiben muss. Gute Beispiele: „Nur Staging“, „bestehendes Design erhalten“,
„keine externe Analyse“, „vor Live-Änderungen Backup prüfen“.

### 02 — Ein Projekt, ein nachvollziehbarer Stand

Jedes Projekt bekommt klare Dateien, Git, Dokumentation und offene Aufgaben.
Der Agent prüft zuerst Regeln, Projektstatus und vorhandene Änderungen.

### 03 — Klein bauen, direkt prüfen

Keine riesigen Blindflüge: Änderungen werden in überschaubaren Schritten gebaut,
mit passenden Tests geprüft und visuell kontrolliert, wenn Gestaltung betroffen ist.

### 04 — Übergabe, nicht Gedächtnisverlust

Am Ende stehen echter Stand, Testnachweise, offene Punkte und der Rückweg bereit.
So bleibt ein Projekt auch nach einem neuen Chat oder einem Teamwechsel verständlich.

---

## Das Startpaket

### Aufgaben und Wissen

**[MGD ToDo Skill](https://github.com/MichaelGahnDESIGN/MGD_Todo_SKILL)**
ordnet Aufgaben, ein gemeinsames Board und Wissenspflege ohne Fremddienst.
Ideal, wenn mehr als ein Chat oder Mensch am Projekt arbeitet.

**[Living Documentation](https://github.com/MichaelGahnDESIGN/MGD_Living-Documentation)**
hält Entscheidungen, Risiken, offene Fragen und echte Prüfstände dauerhaft fest.

**[MGD AI Thread](https://github.com/MichaelGahnDESIGN/MGD_AI-Thread)**
schreibt vor einem Kontextwechsel eine ehrliche Übergabe statt einer vagen
Zusammenfassung.

### Umsetzung und Qualität

**[MGD DEV Skill](https://github.com/MichaelGahnDESIGN/MGD_DEV_SKILL)**
bringt Planung, Tests, Git, Releases, Backups und Dokumentation in einen
kontrollierten Ablauf.

**[MGD AI PlayTest](https://github.com/MichaelGahnDESIGN/MGD_AI-PlayTest_SKILL)**
prüft eine Funktion aus Sicht echter Nutzerinnen und Nutzer.

**[MGD ProjectClean](https://github.com/MichaelGahnDESIGN/MGD_ProjectClean_SKILL)**
hilft beim sauberen Abschluss: Version, Tests, Changelog, Dokumentation und
aufgeräumter Projektstand.

### Web, Plattformen und Spezialfälle

**[MGD Divi 5 Dev Skill](https://github.com/MichaelGahnDESIGN/MGD_Divi5-Dev_SKILL)**
ist der Weg für WordPress und Divi 5: mit lokalen Ressourcen, DSGVO-Leitplanken,
Staging und visueller Prüfung.

**[MGD Plattform-Builder](https://github.com/MichaelGahnDESIGN/MGD-Plattform-Builder)**
liefert ein Fundament für Plattformen und CMS-Projekte mit Versionierung,
Rechtstexten und Starter-Templates. Bitte vor der Nutzung die aktuelle Lizenz
und den Release-Stand im Repository prüfen.

**[MGD WordPress MCP](https://github.com/MichaelGahnDESIGN/MGD_WordPress-MCP)**
verbindet autorisierte KI-Agenten mit WordPress. Schreibrechte, Backups und
Berechtigungen bleiben bewusst getrennte Freigaben.

---

## Externe Werkzeuge, die gut dazu passen

**[ECC](https://github.com/affaan-m/ECC)** erweitert Coding-Agenten um
Spezialwissen, Review- und Sicherheitsabläufe. Die Open-Source-Basis ist MIT;
optionale Pro-Angebote sind davon getrennt.

**[Hallmark](https://github.com/Nutlope/hallmark)** hilft bei anspruchsvollen
Oberflächen: klare Informationshierarchie, keine KI-Standardoptik und überprüfbare
Redesigns.

**[Superpowers](https://github.com/obra/superpowers)** bündelt einen
agentischen Entwicklungsworkflow über die offiziellen Plugin-Marktplätze der
unterstützten Agenten.

Alle drei sind Ergänzungen, keine Pflicht. Vor einer Installation immer Quelle,
Lizenz, Kosten, Zielpfad und eventuelle Hooks prüfen.

---

## In zehn Minuten startklar

1. Öffne das [Vibecoding-Setup](https://github.com/MichaelGahnDESIGN/MGD_Vibecoding_Setup_SKILL).
2. Führe zuerst den Trockenlauf für deinen Agenten aus:

```bash
python3 scripts/install_mgd_skills.py --target codex --profile core
```

3. Lies die angezeigte Liste. Erst wenn sie passt:

```bash
python3 scripts/install_mgd_skills.py --target codex --profile core --apply
```

4. Starte einen neuen Chat und beginne mit einem klaren Projektauftrag.

Für Claude Code `--target claude` nutzen. Für kompatible andere Agenten ist
`--target generic` vorgesehen. Der Assistent überschreibt keine vorhandenen
Skill-Ordner und installiert keine Drittanbieter ungefragt.

---

## Kopierfertige Prompts

### Projektstart

```text
Ich möchte dieses Projekt professionell mit KI-Agenten aufsetzen.

Ziel: [konkretes Ergebnis]
Projektordner: [Pfad oder Repository]
Zielumgebung: [lokal / Staging / Live]
Geschützt: [bestehendes Design, Datenbank, Login, Kundendaten usw.]

Prüfe zuerst Projektregeln, Git-Status und vorhandene Dokumentation.
Lege dann einen kleinen, nachvollziehbaren Umsetzungsplan vor.
Ändere nichts Produktives ohne Rückfallpunkt und meine Freigabe.
Nutze Todo für offene Punkte, DEV für die Umsetzung und erstelle vor einem
Kontextwechsel eine Übergabe.
```

### Website oder Divi 5

```text
Überarbeite diese WordPress-/Divi-5-Seite: [URL oder Seitentitel].

Ziel: [z. B. neue Leistungsseite / bessere mobile Darstellung]
Umgebung: zuerst Staging.
Erhalte Header, Footer, SEO und bestehende Markenregeln, sofern ich nichts
anderes anfordere. Prüfe vor jeder Änderung den vorhandenen Aufbau und einen
Rückfallpunkt. Nutze zuerst native Divi-Module und lokale Ressourcen.
Prüfe anschließend Desktop und Mobil und berichte nur tatsächlich getestete
Ergebnisse.
```

### Fehler beheben

```text
Untersuche dieses Problem, ohne vorschnell etwas zu ändern:
[Fehlerbild, URL, Screenshot oder Log-Auszug]

Reproduziere den Fehler zuerst. Erkläre Ursache, betroffene Bereiche und den
kleinsten sicheren Fix. Berücksichtige vorhandene Änderungen anderer Personen.
Setze die Korrektur erst nach dieser Einordnung um und nenne danach die echten
Prüfschritte und offenen Risiken.
```

### Übergabe an einen neuen Agenten

```text
Erstelle eine ehrliche Übergabe für den nächsten Chat.
Nenne Projektwurzel, Ziel, erledigte Änderungen, Commit-/Deployment-Stand,
wirklich ausgeführte Tests, offene Punkte, Risiken und den nächsten sicheren
Schritt. Keine Zugangsdaten, Tokens oder privaten URLs aufnehmen.
```

---

## Beispiele aus der Praxis

### Neue Website-Funktion

Ein Kontaktbereich soll ergänzt werden. Der Agent liest zuerst die bestehende
Seite und Datenschutzvorgaben, baut die Änderung auf Staging, testet Formular,
Mobilansicht und Fehlermeldungen – und veröffentlicht erst nach Abnahme.

### Neue Plattform oder Kundenportal

Der Plattform-Builder gibt den Rahmen. Todo und Living Documentation halten
Entscheidungen fest. DEV arbeitet die Release-Schritte ab. ECC oder
Superpowers können ergänzen, aber nur nach klarer Prüfung ihres jeweiligen
Installationswegs.

### Mehrere Chats, ein Projekt

Das Board hält Aufgaben zentral. Vor dem Wechsel schreibt Thread eine Übergabe.
So kennt der nächste Agent nicht nur den Plan, sondern auch echte Tests,
unfertige Punkte und Grenzen der bisherigen Arbeit.

---

## Die wichtigste Regel

Ein guter Agent arbeitet schnell. Ein guter Workflow macht seine Arbeit sicher,
prüfbar und übertragbar.

> Vibe Coding ist kein Blindflug. Es ist gute Zusammenarbeit – mit klarer
> Richtung, sauberem Handwerk und einer Spur, die bleibt.
