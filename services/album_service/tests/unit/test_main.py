from fastapi.testclient import TestClient
from app.main import app

async def test_app_creation(client: TestClient):
    response = client.get("/albums/")
    assert response.status_code == 200
    assert response.json() == []