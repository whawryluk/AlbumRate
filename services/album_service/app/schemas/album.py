from pydantic import BaseModel, ConfigDict

class AlbumBase(BaseModel):
    title: str
    artist: str
    genre: str | None = None
    release_year: int | None = None
    
class AlbumCreate(AlbumBase):
    pass

class AlbumRead(BaseModel):
    id: int
    title: str
    artist: str
    release_year: int

    model_config = ConfigDict(from_attributes=True, strict=True)
