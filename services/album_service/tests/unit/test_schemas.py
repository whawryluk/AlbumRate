import pytest
from pydantic import ValidationError
from app.schemas.album import AlbumCreate, AlbumRead
from app.models.album import Album

def test_album_create_schema_valid():
    data = {"title": "Test Album",
            "artist": "Test Artist",
            "release_year": 2023}
    album = AlbumCreate(**data)
    assert album.title == "Test Album"
    assert album.artist == "Test Artist"
    assert album.release_year == 2023

def test_album_create_schema_invalid_year():
    data = {"title": "Test Album",
            "artist": "Test Artist",
            "release_year": "2023"}
    with pytest.raises(ValidationError):
        AlbumCreate(**data)

def test_album_read_schema_valid():
    data = {"id": 1,
            "title": "Test Album",
            "artist": "Test Artist",
            "release_year": 2023}
    album = AlbumRead(**data)
    assert album.id == 1
    assert album.title == "Test Album"
    assert album.artist == "Test Artist"
    assert album.release_year == 2023

def test_album_read_schema_missing_id():
    data = {"title": "Test Album",
            "artist": "Test Artist",
            "release_year": "2023"}
    with pytest.raises(ValidationError):
        AlbumRead(**data)

def test_album_read_schema_orm_mode():
    album_data = Album(id=1,
                       title="Test Album",
                       artist="Test Artist",
                       release_year=2023)
    album_read = AlbumRead.model_validate(album_data)
    assert album_read.id == 1
    assert album_read.title == "Test Album"
    assert album_read.artist == "Test Artist"
    assert album_read.release_year == 2023

def test_album_read_schema_orm_mode_invalid_types():
    with pytest.raises(ValidationError):
        album_data = Album(id="invalid_id",
                           title="Invalid Album",
                           artist="Invalid Artist",
                           release_year="invalid_year")
        AlbumRead.model_validate(album_data)