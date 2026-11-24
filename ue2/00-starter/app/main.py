"""Todo-API: Jeder Endpunkt verarbeitet eine bestimmte HTTP-Anfrage.

Die Zeile mit @app legt HTTP-Methode und URL fest. Die Funktion darunter
führt die Anfrage aus. FastAPI prüft die Eingaben anhand der Typangaben
und wandelt zurückgegebene Todo-Objekte automatisch in JSON um.
"""

from pathlib import Path
from typing import Annotated, Literal

from fastapi import FastAPI, Header, HTTPException, Path as PathParam, Response
from fastapi.responses import FileResponse, JSONResponse

from app import storage
from app.models import Todo, TodoCreate, TodoReplace, TodoUpdate


app = FastAPI(title="Todo API – UE 2", version="1.0.0")

# Eine Todo-ID in der URL muss eine ganze Zahl größer als 0 sein.
TodoId = Annotated[int, PathParam(gt=0)]

# Diese Beschreibung erscheint in der API-Dokumentation.
# Die tatsächliche Fehlerantwort wird in get_todo ausgelöst.
NOT_FOUND = {404: {"description": "Todo nicht gefunden"}}


@app.get("/", include_in_schema=False)
def frontend():
    """Die HTML-Datei der Todo-Weboberfläche ausliefern."""
    html_file = Path(__file__).with_name("index.html")
    return FileResponse(html_file)


@app.get("/health", tags=["System"])
def health():
    """Mit einer einfachen Antwort zeigen, dass der Server läuft."""
    return {"status": "ok"}


# Aufgabe 03: Implementiere die Funktion und ergänze den FastAPI-Decorator gemäß Vertrag.
def get_todos():
    pass


# Aufgabe 03: Implementiere die Funktion und ergänze den FastAPI-Decorator gemäß Vertrag.
def get_todo(id: TodoId):
    pass


# Aufgabe 04: Implementiere die Funktion und ergänze den FastAPI-Decorator gemäß Vertrag.
def create_todo(data: TodoCreate, response: Response):
    pass


# Aufgabe 05: Implementiere die Funktion und ergänze den FastAPI-Decorator gemäß Vertrag.
def replace_todo(id: TodoId, data: TodoReplace):
    pass


# Aufgabe 05: Implementiere die Funktion und ergänze den FastAPI-Decorator gemäß Vertrag.
def update_todo(id: TodoId, data: TodoUpdate):
    pass


# Aufgabe 05: Implementiere die Funktion und ergänze den FastAPI-Decorator gemäß Vertrag.
def delete_todo(id: TodoId):
    pass


# Aufgabe 06: Registriere die vorbereitete Formatdemo.
def formats(
    format: Literal["json", "xml"] | None = None,
    accept: Annotated[str | None, Header()] = None,
):
    """Dieselben Beispieldaten wahlweise als JSON oder XML zurückgeben."""
    # Auswahl: zuerst der URL-Parameter, danach der Accept-Header,
    # ansonsten JSON. Dies ist eine vereinfachte Formatdemo für die Lehre.
    if format is not None:
        chosen_format = format
    elif accept == "application/xml":
        chosen_format = "xml"
    else:
        chosen_format = "json"

    if chosen_format == "xml":
        xml_content = (
            "<todo>"
            "<id>1</id>"
            "<title>API lernen</title>"
            "<completed>false</completed>"
            "</todo>"
        )
        return Response(content=xml_content, media_type="application/xml")

    example_todo = {"id": 1, "title": "API lernen", "completed": False}
    return JSONResponse(content=example_todo)
