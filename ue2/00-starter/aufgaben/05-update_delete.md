# Aufgabe 05 – Todos bearbeiten

## Auftrag
PUT gemeinsam, PATCH und DELETE selbst. Verwende TodoReplace bzw. TodoUpdate; model_dump(exclude_unset=True); ID beibehalten. Registriere die Routen.

Datei: app/main.py; Modelle in app/models.py. Lies zuerst docs/api-vertrag.md. Aktualisiere /docs nach dem Speichern.

## Swagger UI: Abnahme
PUT mit title und completed → 200; PATCH mit completed → 200, Titel bleibt; DELETE → 204, danach GET → 404.

## Automatisierter Test
`uv run pytest tests/test_05_update_delete.py -v`
