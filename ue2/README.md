# Todo API – UE 2 (ohne Git)

Jeder Unterordner ist ein vollständiges, eigenständiges Python-Projekt. Git ist nicht erforderlich.

| Ordner | Stand / nächster Schritt |
|---|---|
| `00-starter` | Aufgabe 03 beginnen |
| `01-nach-aufgabe-03` | Aufgabe 04 beginnen |
| `02-nach-aufgabe-04` | Aufgabe 05 beginnen |
| `03-nach-aufgabe-05` | Aufgabe 06 beginnen |
| `04-nach-aufgabe-06` | Aufgabe 07 beginnen |
| `05-musterloesung` | Vollständige Referenz |

## Start

ZIP entpacken, `00-starter` im Editor öffnen und im Terminal dieses Ordners ausführen:

```sh
uv sync
uv run fastapi dev app/main.py
```

Swagger UI: http://localhost:8000/docs

## Weiterarbeiten

Arbeite im Starter weiter, solange du mitkommst. Wenn du einen Zwischenstand benötigst, stoppe den Server mit Strg+C, öffne den passenden Ordner im Editor und führe dort dieselben Startbefehle aus. Deine bisherigen Dateien werden nicht überschrieben. Jeder Ordner hat seine eigene virtuelle Umgebung; uv richtet sie ein. Die Daten werden beim Serverwechsel zurückgesetzt.

Aufgaben liegen jeweils in `aufgaben/`, der Vertrag in `docs/api-vertrag.md`. Tests für noch nicht implementierte Aufgaben schlagen erwartungsgemäß fehl. Die Musterlösung enthält alle Lösungen; für eine eigenständige Bearbeitung zunächst nur den Starter verwenden.

Python 3.12 und uv werden vorausgesetzt. Eine Lockdatei ist nicht enthalten; uv löst die Abhängigkeiten beim ersten Start auf. Swagger UI benötigt standardmäßig Zugriff auf ein CDN.
