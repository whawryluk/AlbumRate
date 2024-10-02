from pydantic import BaseModel, ConfigDict, conint
from typing import Optional

class AlbumBase(BaseModel):
    title: str
    artist: str
    genre: Optional[str] = None
    release_year: Optional[conint(strict=True)] = None
    description: Optional[str] = None

    model_config = ConfigDict(strict=True)

class AlbumCreate(AlbumBase):
    pass

class AlbumRead(BaseModel):
    id: int
    title: str
    artist: str
    genre: Optional[str] = None
    release_year: Optional[conint(strict=True)] = None
    description: Optional[str] = None

    model_config = ConfigDict(from_attributes=True, strict=True)
