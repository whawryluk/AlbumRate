from app.models.album import Album

def test_album_model():
    album = Album(title="Test Album", artist="Test Artist", release_year=2023)
    assert album.title == "Test Album"
    assert album.artist == "Test Artist"
    assert album.release_year == 2023