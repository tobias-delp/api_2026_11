# Aufgabe 07 – Vertrag prüfen

## Auftrag
Partnerarbeit: Consumer liest nur den Vertrag, prüft alle vorherigen Fälle in Swagger UI. Prüft anschließend das Frontend und DevTools.

Datei: app/main.py; Modelle in app/models.py. Lies zuerst docs/api-vertrag.md. Aktualisiere /docs nach dem Speichern.

## Swagger UI: Abnahme
Alle Tests erfolgreich; Status, Header und Body stimmen mit Vertrag überein.

## Automatisierter Test
`uv run pytest tests/test_07_contract.py -v`
