# Aufgabe 04 – Todos erstellen

## Auftrag
Ergänze create_todo mit TodoCreate, Response, ID-Zähler, Speicherung, Location und 201. Registriere POST.

Datei: app/main.py; Modelle in app/models.py. Lies zuerst docs/api-vertrag.md. Aktualisiere /docs nach dem Speichern.

## Swagger UI: Abnahme
POST /todos mit {"title":"Test"} → 201, ID 4 bei frischem Start; leerer Titel oder fehlender Titel → 422.

## Automatisierter Test
`uv run pytest tests/test_04_create.py -v`
