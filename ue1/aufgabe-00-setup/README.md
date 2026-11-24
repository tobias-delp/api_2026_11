# Aufgabe 00: Entwicklungsumgebung & erster API-Call mit `uv`

## Ziel
Wir richten `uv` ein und starten ein erstes Python-Skript, das ohne manuelles `pip install` oder `venv`-Einrichtung eine echte öffentliche API abfragt.

## Auftrag
1. Installiere `uv` (siehe Haupt-`README.md`), öffne ein **neues Terminal** und prüfe `uv --version`.
2. Wechsle in diesen Ordner:
   ```bash
   cd aufgabe-00-setup
   ```
3. Führe das Test-Skript aus:
   ```bash
   uv run check_setup.py
   ```
   *Beobachte, was `uv` dabei im Hintergrund tut (Python & Abhängigkeiten via PEP 723 Inline-Metadaten auflösen).*

## Ergebnis
In deinem Terminal erscheinen der HTTP-Statuscode `200`, der Header `Content-Type` und ein JSON-Todo-Objekt.
