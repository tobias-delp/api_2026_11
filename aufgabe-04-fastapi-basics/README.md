# Aufgabe 04: FastAPI Basics mit `uv`

## Auftrag
1. Wechsle in diesen Ordner und starte den Entwicklungsserver:
   ```bash
   cd aufgabe-04-fastapi-basics
   uv run fastapi dev main.py
   ```
2. Rufe im Browser `http://localhost:8000/health` und die automatische Swagger UI unter `http://localhost:8000/docs` auf.
3. Ergänze in `main.py` einen ersten Endpoint `GET /todos`, der eine statische Liste von 2 Todos zurückgibt.
4. Teste den neuen Endpoint über `/docs`, `curl` oder deine `requests.http`.

## Ergebnis
Laufender FastAPI-Server mit automatischer OpenAPI-Dokumentation (`/docs`) und erstem Lese-Endpunkt.
