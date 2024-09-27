from pydantic import BaseModel

class AlbumBase(BaseModel):
    title: str
    artist: str
    genre: str | None = None
    release_yea: int | None = None
    
class AlbumCreate(AlbumBase):
    pass


class AlbumRead(AlbumBase):
    id: int
    
    class Config:
        orm_mode = True
        