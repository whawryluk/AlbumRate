from app.schemas.album import AlbumCreate, AlbumRead

def test_album_create_schema():
    data = {"title": "Test Album", "artist": "Test Artist", "release_year": 2023}
    album = AlbumCreate(**data)
    assert album.title == "Test Album"
    assert album.artist == "Test Artist"
    assert album.release_year == 2023

def test_album_read_schema():
    data = {"id": 1, "title": "Test Album", "artist": "Test Artist", "release_year": 2023}
    album = AlbumRead(**data)
    assert album.id == 1
    assert album.title == "Test Album"
    assert album.artist == "Test Artist"
    assert album.release_year == 2023