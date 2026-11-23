import json
from pathlib import Path
from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="Todo API", version="1.0.0")


# --- Pydantic Schemas (Vertrag im Code) ---
class TodoCreate(BaseModel):
    title: str = Field(min_length=1, description="Titel der Aufgabe darf nicht leer sein")
    completed: bool = False


class TodoUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1)
    completed: bool | None = None


class Todo(BaseModel):
    id: int
    title: str
    completed: bool


# --- In-Memory Datenspeicher (initial aus seed_todos.json geladen) ---
SEED_FILE = Path(__file__).parent / "seed_todos.json"
todos: list[dict] = json.loads(SEED_FILE.read_text(encoding="utf-8"))
next_id: int = max((t["id"] for t in todos), default=0) + 1


def find_todo(todo_id: int) -> dict | None:
    return next((t for t in todos if t["id"] == todo_id), None)


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/todos", response_model=list[Todo])
def list_todos(completed: bool | None = None) -> list[dict]:
    if completed is None:
        return todos
    return [t for t in todos if t["completed"] == completed]


# TODO 1: GET /todos/{todo_id} -> 200 oder 404 (HTTPException)

# TODO 2: POST /todos -> status_code=status.HTTP_201_CREATED, TodoCreate entgegennehmen

# TODO 3: PATCH /todos/{todo_id} -> TodoUpdate mit model_dump(exclude_unset=True) anwenden

# TODO 4: DELETE /todos/{todo_id} -> status_code=status.HTTP_204_NO_CONTENT
