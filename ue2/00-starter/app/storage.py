from app.models import Todo

def reset():
    global next_id
    todos.clear()
    for i, title in enumerate(['API Grundlagen wiederholen', 'FastAPI kennenlernen', 'Eigene REST-API implementieren'], 1):
        todos[i] = Todo(id=i, title=title, completed=i == 1)
    next_id = 4

todos: dict[int, Todo] = {}
reset()

def allocate_id():
    global next_id
    result = next_id
    next_id += 1
    return result
