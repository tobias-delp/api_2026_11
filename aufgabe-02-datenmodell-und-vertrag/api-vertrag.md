# API-Vertrag: Todo-API (v1)

**Ressource:** `/todos` (Collection) bzw. `/todos/{id}` (einzelnes Todo)  
**Datenformat:** JSON *(Hinweis: Konkrete HTTP-Methoden und Statuscodes ergänzen wir in UE 2)*

## Operationen (CRUD)

### 1. Read All – Alle Todos abrufen
* **Operation:** Alle Todos lesen (`/todos`)
* **Eingabe:** Keine *(optional: Filter nach Status `completed`?)*
* **Erfolgsantwort:** Liste (Array) von Todo-Objekten

### 2. Read One – Einzelnes Todo abrufen
* **Operation:** Ein Todo anhand seiner `id` lesen (`/todos/{id}`)
* **Eingabe:** `id` (Integer)
* **Erfolgsantwort:** Einzelnes Todo-Objekt
* **Fehlerfall:** Unbekannte `id` → Meldung *„Todo nicht gefunden“*

### 3. Create – Neues Todo anlegen
*(Ergänzen: Ziel-Ressource, benötigte Eingabefelder, erwartete Rückgabe, Fehlerfall z. B. fehlender oder leerer `title`)*

### 4. Update – Todo aktualisieren
*(Ergänzen: Teil-Update vs. Voll-Update, Eingabefelder, erwartete Rückgabe, Fehlerfälle)*

### 5. Delete – Todo löschen
*(Ergänzen: Ziel-Ressource, Eingabe, erwartete Rückgabe, Fehlerfall bei unbekannter `id`)*
