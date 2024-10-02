import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app  # Ensure DATABASE_URL is set before this import

@pytest.mark.asyncio
async def test_create_album():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/albums/", json={
            "title": "The Dark Side of the Moon",
            "artist": "Pink Floyd",
            "year": 1973
        })
    assert response.status_code == 200
    assert response.json()["title"] == "The Dark Side of the Moon"
    assert response.json()["artist"] == "Pink Floyd"
    assert response.json()["year"] == 1973
    assert "id" in response.json()
