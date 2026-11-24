# API-Vertrag – UE 2 (Soll)
JSON-Ressource: id (positive Ganzzahl, serverseitig), title (String, 1–200 Zeichen, nicht nur Leerzeichen), completed (Boolean). IDs werden im Serverlauf nicht wiederverwendet. Startdaten: IDs 1–3.

| Methode | Pfad | Erfolg | Eingabe |
|---|---|---|---|
| GET | /health | 200 | – |
| GET | /todos | 200, Liste (auch leer) | optional completed=true/false |
| GET | /todos/{id} | 200, Todo | positive ID |
| POST | /todos | 201, Todo, Location | title, completed optional (false) |
| PUT | /todos/{id} | 200, Todo | title und completed erforderlich |
| PATCH | /todos/{id} | 200, Todo | title und/oder completed optional; {} ist No-op |
| DELETE | /todos/{id} | 204, kein Body | positive ID |
| GET | /demo/formats | 200 | format=json/xml, alternativ Accept |

Unbekannte ID: 404 mit detail „Todo nicht gefunden“. Ungültige Eingaben: 422 im FastAPI-Standardformat. Keine zusätzlichen Body-Felder, keine null-Werte. PUT legt keine neue Ressource an. Filter verwendet FastAPIs bool-Konvertierung (auch z. B. 1/0). Formatdemo: expliziter Parameter hat Vorrang; sonst exakter Accept-Wert application/xml, andernfalls JSON. Keine vollständige Content Negotiation. Daten gehen beim Neustart/Reload verloren. Nicht für parallele produktive Schreibzugriffe ausgelegt.
