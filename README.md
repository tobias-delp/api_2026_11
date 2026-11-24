# APIs verstehen, testen und entwickeln (Python + uv + FastAPI)

Begleit-Repository für die zweiteilige Online-Vorlesung zum Thema **APIs**.
Wir verfolgen einen durchgängigen **API-First-Ansatz**: vom Datenmodell und API-Vertrag bis zur getesteten REST-API mit Python und FastAPI.

## Aufbau

| Ordner | Inhalt |
| :--- | :--- |
| [ue1/aufgabe-00-setup](ue1/aufgabe-00-setup/README.md) | Entwicklungsumgebung einrichten und eine öffentliche API mit Python abfragen |
| [ue1/aufgabe-01-api-inventur](ue1/aufgabe-01-api-inventur/README.md) | APIs im Alltag und im Browser-Network-Tab erkennen |
| [ue1/aufgabe-02-datenmodell-und-vertrag](ue1/aufgabe-02-datenmodell-und-vertrag/README.md) | Todo-Datenmodell und API-Vertrag entwerfen |
| [ue2](ue2/README.md) | Todo-API schrittweise implementieren, erweitern und testen |
| [slides](slides/) | Vorlesungsfolien als PDF |

## Voraussetzungen und Setup

- **uv** zur Verwaltung von Python und Abhängigkeiten; die Projekte benötigen **Python 3.12 oder neuer**.
- Ein Editor, beispielsweise **VS Code**, und ein Terminal.
- Internetzugang für die Installation, den ersten öffentlichen API-Call und die CDN-Assets der Swagger UI.
- Git ist optional: Das Repository kann auch als ZIP heruntergeladen und entpackt werden. Für die Übungen in UE 2 sind keine Git-Befehle erforderlich.

**uv installieren:**

macOS / Linux / WSL:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Danach ein neues Terminal öffnen und prüfen:

```sh
uv --version
```

## UE 1: APIs verstehen und entwerfen

Die Aufgaben werden der Reihe nach in `ue1/` bearbeitet. Für den ersten API-Call im Stammordner des Repositorys ausführen:

```sh
cd ue1/aufgabe-00-setup
uv run check_setup.py
```

uv richtet Python und die im Skript angegebenen Abhängigkeiten ein. Das Skript fragt ein Todo von JSONPlaceholder ab und gibt Statuscode, Content-Type und JSON-Antwort aus.

Danach folgen die API-Inventur sowie das eigene Todo-Datenmodell und der API-Vertrag. Die Aufträge und Vorlagen stehen in den jeweiligen Aufgabenordnern.

## UE 2: Todo-API entwickeln und testen

Jeder Unterordner in `ue2/` ist ein eigenständiges Python-Projekt mit Aufgaben, API-Vertrag, Anwendung und Tests.

| Projekt | Entwicklungsstand / nächster Schritt |
| :--- | :--- |
| [00-starter](ue2/00-starter/README.md) | Aufgabe 03: Todos lesen (`GET`) |
| [01-nach-aufgabe-03](ue2/01-nach-aufgabe-03/README.md) | Aufgabe 04: Todos anlegen (`POST`) |
| [02-nach-aufgabe-04](ue2/02-nach-aufgabe-04/README.md) | Aufgabe 05: Todos ersetzen, ändern und löschen (`PUT`, `PATCH`, `DELETE`) |
| [03-nach-aufgabe-05](ue2/03-nach-aufgabe-05/README.md) | Aufgabe 06: Statusfilter und JSON-/XML-Formatdemo ergänzen |
| [04-nach-aufgabe-06](ue2/04-nach-aufgabe-06/README.md) | Aufgabe 07: Vertrag, Frontend und HTTP-Verhalten prüfen |
| [05-musterloesung](ue2/05-musterloesung/README.md) | Vollständige Referenzimplementierung |

### Starten

Vom Stammordner des Repositorys aus:

```sh
cd ue2/00-starter
uv sync
uv run fastapi dev app/main.py
```

Anschließend im Browser öffnen:

- [Swagger UI](http://localhost:8000/docs): Endpunkte ausprobieren und Antworten prüfen.
- [OpenAPI-Beschreibung](http://localhost:8000/openapi.json): automatisch erzeugte Beschreibung der implementierten API.
- [Todo-Weboberfläche](http://localhost:8000/): Frontend zum Ausprobieren der implementierten Todo-Endpunkte.
- [Health-Check](http://localhost:8000/health): prüfen, ob der Server läuft.

Im Starter sind Health-Check und Frontend bereits vorhanden; die Todo-Endpunkte werden in den Aufgaben ergänzt. Aufgaben stehen jeweils in `aufgaben/`, der Soll-Vertrag in `docs/api-vertrag.md`, der Anwendungscode in `app/`.

### Tests und Zwischenstände

Im jeweiligen Projektordner alle Tests oder gezielt die Tests einer Aufgabe ausführen:

```sh
uv run pytest -v
uv run pytest tests/test_03_read.py -v
```

Tests für noch nicht implementierte Aufgaben schlagen erwartungsgemäß fehl. Die Musterlösung enthält die vollständige Implementierung für alle Aufgaben.

Arbeite im Starter weiter oder wechsle bei Bedarf zu einem vorbereiteten Zwischenstand: Server mit **Strg+C** stoppen, den passenden Projektordner öffnen und dort dieselben Startbefehle ausführen. uv richtet für jeden Projektordner eine eigene virtuelle Umgebung ein; eigene Änderungen bleiben im bisherigen Ordner erhalten.

Die Todo-Daten liegen ausschließlich im Arbeitsspeicher. Ein Serverneustart, ein automatischer Reload nach Codeänderungen oder der Wechsel zu einem anderen Projektstand setzt sie auf die Beispieldaten zurück. Eine Datenbank und Authentifizierung sind nicht Teil des Lehrprojekts.
