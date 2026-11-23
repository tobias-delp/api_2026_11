# Aufgabe 05: Todo-API CRUD, Validierung & Vertragstest

## Auftrag
1. Starte das Starter-Projekt mit:
   ```bash
   cd aufgabe-05-todo-api-crud
   uv run fastapi dev main.py
   ```
2. Implementiere in `main.py` die fehlenden Endpoints gemäß deinem Vertrag aus Aufgabe 02:
   * `GET /todos` (Bonus: optionaler Query-Parameter `?completed=true|false`)
   * `GET /todos/{todo_id}` (mit `404 Not Found` bei unbekannter ID)
   * `POST /todos` (Status `201 Created`, Pydantic-Validierung)
   * `PATCH /todos/{todo_id}` (Teil-Update, `404` bei unbekannter ID)
   * `DELETE /todos/{todo_id}` (Status `204 No Content`, `404` bei unbekannter ID)
3. Teste **alle** Erfolgs- und Fehlerfälle aus `requests.http` und `aufgabe-03/testfaelle.md` gegen deine API sowie interaktiv über `http://localhost:8000/docs`.

## Ergebnis
Vollständige, validierte Todo-API im In-Memory-Speicher (initial geladen aus `seed_todos.json`), verifiziert gegen den API-Vertrag.
