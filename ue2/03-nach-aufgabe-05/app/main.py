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


@app.get(
    "/todos",
    response_model=list[Todo],
    tags=["Todos"],
    summary="Alle Todos abrufen",
)
def get_todos():
    """Alle gespeicherten Todos als Liste zurückgeben."""
    all_todos = []

    for todo in storage.todos.values():
        all_todos.append(todo)

    return all_todos


@app.get(
    "/todos/{id}",
    response_model=Todo,
    tags=["Todos"],
    responses=NOT_FOUND,
)
def get_todo(id: TodoId):
    """Ein Todo anhand seiner ID suchen."""
    if id not in storage.todos:
        # Die Ausnahme beendet die Anfrage mit HTTP-Status 404.
        raise HTTPException(status_code=404, detail="Todo nicht gefunden")

    return storage.todos[id]


@app.post(
    "/todos",
    response_model=Todo,
    status_code=201,
    tags=["Todos"],
    responses={
        201: {"headers": {"Location": {"schema": {"type": "string"}}}},
    },
)
def create_todo(data: TodoCreate, response: Response):
    """Ein Todo mit einer neuen ID anlegen und im Arbeitsspeicher speichern."""
    new_id = storage.allocate_id()
    todo = Todo(
        id=new_id,
        title=data.title,
        completed=data.completed,
    )
    storage.todos[new_id] = todo

    # HTTP 201 bedeutet „angelegt“. Location nennt die URL des neuen Todos.
    response.headers["Location"] = f"/todos/{new_id}"
    return todo


@app.put(
    "/todos/{id}",
    response_model=Todo,
    tags=["Todos"],
    responses=NOT_FOUND,
)
def replace_todo(id: TodoId, data: TodoReplace):
    """Titel und Erledigt-Status eines vorhandenen Todos vollständig ersetzen."""
    # Vor dem Ersetzen prüfen, ob die ID existiert; sonst folgt HTTP 404.
    get_todo(id)

    replacement = Todo(
        id=id,
        title=data.title,
        completed=data.completed,
    )
    storage.todos[id] = replacement
    return replacement


@app.patch(
    "/todos/{id}",
    response_model=Todo,
    tags=["Todos"],
    responses=NOT_FOUND,
)
def update_todo(id: TodoId, data: TodoUpdate):
    """Nur die Felder ändern, die in der Anfrage übermittelt wurden."""
    existing_todo = get_todo(id)

    # model_fields_set enthält die Namen der tatsächlich gesendeten Felder.
    # So bleibt etwa completed=true erhalten, wenn nur title gesendet wurde.
    title = existing_todo.title
    if "title" in data.model_fields_set:
        title = data.title

    completed = existing_todo.completed
    if "completed" in data.model_fields_set:
        completed = data.completed

    updated_todo = Todo(id=id, title=title, completed=completed)
    storage.todos[id] = updated_todo
    return updated_todo


@app.delete(
    "/todos/{id}",
    status_code=204,
    tags=["Todos"],
    responses=NOT_FOUND,
)
def delete_todo(id: TodoId):
    """Ein vorhandenes Todo löschen und ohne Antwortinhalt bestätigen."""
    get_todo(id)
    del storage.todos[id]

    # HTTP 204 bedeutet: erfolgreich, aber ohne Antwortinhalt.
    return Response(status_code=204)


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
