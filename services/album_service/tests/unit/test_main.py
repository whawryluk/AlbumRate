from fastapi.testclient import TestClient
from app.main import app

def test_app_creation(client: TestClient):
    client = TestClient(app)
    response = client.get("/albums/")
    assert response.status_code == 200
    assert response.json() == []