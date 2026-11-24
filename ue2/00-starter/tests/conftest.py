import pytest
from fastapi.testclient import TestClient
from app.main import app
from app import storage
@pytest.fixture
def client():
    storage.reset()
    with TestClient(app) as c:
        yield c
