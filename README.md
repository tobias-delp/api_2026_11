# APIs verstehen, testen und entwickeln (Python + uv + FastAPI)

Begleit-Repository für die 2-teilige Online-Vorlesung zum Thema **APIs**.
Wir verfolgen einen durchgängigen **API-First-Ansatz**: Vom ersten API-Vertrag über HTTP-Tests bis zur lauffähigen REST-API mit Python und FastAPI.

## Übersicht der Einheiten & Aufgaben

| Einheit | Ordner | Thema |
| :--- | :--- | :--- |
| **UE 1** | `aufgabe-00-setup` | `uv` installieren, Repo einrichten, erster Live-API-Call |
| **UE 1** | `aufgabe-01-api-inventur` | APIs im Alltag & im Browser-Network-Tab erkennen |
| **UE 1** | `aufgabe-02-datenmodell-und-vertrag` | Todo-Datenmodell (`todos.json`) & API-Vertrag definieren |
| **UE 2** | `aufgabe-03-http-und-testing` | HTTP erkunden (`curl`), `requests.http` & Testfälle |
| **UE 2** | `aufgabe-04-fastapi-basics` | Minimaler FastAPI-Server mit `uv` & Swagger UI (`/docs`) |
| **UE 2** | `aufgabe-05-todo-api-crud` | Vollständige Todo-CRUD-API, Validierung & Vertragstest |

## Voraussetzungen & Setup (wird in UE 1 gemeinsam gemacht)

1. **Git**, **curl** und ein Editor (**VS Code** empfohlen)
2. **`uv` installieren** (verwaltet Python-Versionen & Abhängigkeiten automatisch):
   * **macOS / Linux / WSL:**
     ```bash
     curl -LsSf https://astral.sh/uv/install.sh | sh
     ```
   * **Windows (PowerShell):**
     ```powershell
     powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
     ```
   * Danach **ein neues Terminal öffnen** und prüfen: `uv --version`

> **Fallback (falls lokal etwas blockiert ist):** Du kannst das Repo direkt im Browser über **GitHub Codespaces** (*Code → Codespaces → Create codespace on main*) starten.
