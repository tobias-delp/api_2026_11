# API-Testspezifikation (Todo-API)

Jeder Testfall folgt der 5-teiligen Struktur: **Ziel · Request · Erwarteter Status Code · Erwarteter Body · Begründung**.

## Testfall 1: Alle Todos abrufen (Beispiel)
* **Ziel:** Prüfen, ob die Todo-Liste korrekt zurückgegeben wird.
* **Request:** `GET /todos`
* **Erwarteter Status Code:** `200 OK`
* **Erwarteter Body:** JSON-Array mit Todo-Objekten (`id`, `title`, `completed`)
* **Begründung:** Basis-Lesezugriff auf die Collection-Ressource.

## Testfall 2: Neues Todo anlegen (Happy Path)
* **Ziel:**
* **Request:**
* **Erwarteter Status Code:**
* **Erwarteter Body:**
* **Begründung:**

## Testfall 3: Ungültige Eingabe (z. B. fehlender `title`)
* **Ziel:**
* **Request:**
* **Erwarteter Status Code:** `422 Unprocessable Content`
* **Erwarteter Body:** Strukturierte Validierungsfehlermeldung
* **Begründung:**

## Testfall 4: Unbekannte ID abrufen
* **Ziel:**
* **Request:**
* **Erwarteter Status Code:** `404 Not Found`
* **Erwarteter Body:**
* **Begründung:**

## Testfall 5: Todo teilweise aktualisieren oder löschen
* **Ziel:**
* **Request:**
* **Erwarteter Status Code:**
* **Erwarteter Body:**
* **Begründung:**
