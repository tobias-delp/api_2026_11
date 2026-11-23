# Aufgabe 03: HTTP erkunden, Request-Sammlung & Testfälle

## Auftrag
1. Sende über das Terminal (`curl -i`) oder Postman/Hoppscotch Requests an `https://jsonplaceholder.typicode.com/todos`:
   ```bash
   curl -i https://jsonplaceholder.typicode.com/todos/1
   curl -i -X POST https://jsonplaceholder.typicode.com/todos -H "Content-Type: application/json" -d '{"title":"HTTP testen","completed":false}'
   curl -i https://jsonplaceholder.typicode.com/ungueltig
   ```
   Notiere deine Beobachtungen kurz in `beobachtungen.md`.
2. Vervollständige die `requests.http` für **unsere eigene Todo-API** (`http://localhost:8000`) anhand deines Vertrags aus Aufgabe 02.
3. Formuliere in `testfaelle.md` mindestens **5 strukturierte Testfälle** (Erfolgsfälle + `404` / `422` Fehlerfälle).

## Ergebnis
Ausführbare `requests.http` und prüfbare `testfaelle.md` für die Implementierung.
