import json
from pathlib import Path
from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="Todo API", version="1.0.0")


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


SEED_FILE = Path(__file__).parent.parent / "seed_todos.json"
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


@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int) -> dict:
    todo = find_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo nicht gefunden")
    return todo


@app.post("/todos", response_model=Todo, status_code=status.HTTP_201_CREATED)
def create_todo(payload: TodoCreate) -> dict:
    global next_id
    new_todo = {
        "id": next_id,
        "title": payload.title,
        "completed": payload.completed,
    }
    next_id += 1
    todos.append(new_todo)
    return new_todo


@app.patch("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, payload: TodoUpdate) -> dict:
    todo = find_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo nicht gefunden")

    updates = payload.model_dump(exclude_unset=True)
    todo.update(updates)
    return todo


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int) -> Response:
    todo = find_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo nicht gefunden")

    todos.remove(todo)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
