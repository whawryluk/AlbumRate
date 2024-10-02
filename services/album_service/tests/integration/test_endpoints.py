def test_create_album(client: TestClient):
    response = client.post("/albums/", json={
        "title": "Test Album",
        "artist": "Test Artist",
        "release_year": 2023
    })

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Album"
    assert data["artist"] == "Test Artist"
    assert data["release_year"] == 2023