# Todo-Datenmodell (Version 1)

| Feld | Datentyp | Pflichtfeld? | Beschreibung |
| :--- | :--- | :--- | :--- |
| `id` | Integer | Automatisch (Server) | Eindeutige ID der Ressource |
| `title` | | | |
| `completed` | | | |

## Design-Entscheidungen
* *Warum gehören Felder wie `userId` oder `dueDate` (noch) nicht in V1?*
* *Welche Felder darf der Client beim Erstellen (`POST`) selbst senden, welche vergibt der Server?*
