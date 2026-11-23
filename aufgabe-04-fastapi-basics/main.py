from fastapi import FastAPI

app = FastAPI(title="Todo API - Basics")


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


# TODO: Ergänze hier @app.get("/todos") mit einer statischen Liste von Todos
