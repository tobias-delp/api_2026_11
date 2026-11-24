# Aufgabe 03 – Todos abrufen

## Auftrag
Implementiere get_todos gemeinsam, get_todo selbst. Registriere GET-Routen mit response_model, tags und 404-Dokumentation.

Datei: app/main.py; Modelle in app/models.py. Lies zuerst docs/api-vertrag.md. Aktualisiere /docs nach dem Speichern.

## Swagger UI: Abnahme
GET /todos → 200, drei Todos; /todos/1 → 200; /todos/999 → 404; /todos/abc → 422.

## Automatisierter Test
`uv run pytest tests/test_03_read.py -v`
