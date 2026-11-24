# Aufgabe 06 – API erweitern

## Auftrag
Ergänze optionalen completed-Query-Parameter und Filter. Registriere die vorbereitete formats-Funktion mit beiden Antwortformaten.

Datei: app/main.py; Modelle in app/models.py. Lies zuerst docs/api-vertrag.md. Aktualisiere /docs nach dem Speichern.

## Swagger UI: Abnahme
GET /todos?completed=false → nur offene; invalid → 422; /demo/formats?format=xml → XML.

## Automatisierter Test
`uv run pytest tests/test_06_filter.py -v`
