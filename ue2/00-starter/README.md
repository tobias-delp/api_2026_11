# Entwicklungsstand: 00-starter

**Aufgabe 03 beginnen.** Dieser Ordner ist ein eigenständiges Projekt. Öffne ein Terminal in diesem Ordner. Stoppe einen eventuell laufenden Server aus einem anderen Ordner mit Strg+C.

# Todo API – UE 2
Python 3.12, uv, FastAPI. Im Projektordner:

```sh
uv sync
uv run fastapi dev app/main.py
```

Öffne http://localhost:8000/docs (Swagger UI), /openapi.json (Ist-Beschreibung), / (Frontend). Vertrag: docs/api-vertrag.md (Soll). In Swagger UI: Endpoint öffnen, Try it out, Eingaben setzen, Execute, Status und Body prüfen. Nach Codeänderung Seite aktualisieren; Reload setzt Daten zurück.

Tests: `uv run pytest -v`. Im Starter schlagen Tests zukünftiger Aufgaben absichtlich fehl. Einzelne Aufgaben: `uv run pytest tests/test_03_read.py -v` usw.

Terminal optional: `curl -i http://localhost:8000/health` (Windows: `curl.exe -i http://localhost:8000/health`). PowerShell POST: `$body = @{title='Test'} | ConvertTo-Json` und `Invoke-WebRequest -Uri http://localhost:8000/todos -Method Post -ContentType application/json -Body $body`.


Swagger UI lädt standardmäßig Assets von einem CDN; Internetzugang im Browser erforderlich. Keine Datenbank oder Authentifizierung. Die Anwendung ist ein lokales Lehrprojekt.

Eigene Änderungen bleiben im jeweiligen Ordner erhalten. Für die nächste Aufgabe kannst du im eigenen Projekt weiterarbeiten oder den passenden vorbereiteten Stand aus dem Nachbarordner öffnen.
