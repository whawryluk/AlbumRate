from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.models.album import Album
from app.schemas.album import AlbumCreate, AlbumRead
from app.database.session import get_async_session
from sqlalchemy.future import select

router = APIRouter()

@router.get("/", response_model=List[AlbumRead])
async def read_albums(skip: int = 0, limit: int = 100, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Album).offset(skip).limit(limit))
    albums = result.scalars().all()
    return albums


@router.get("/{album_id}", response_model=AlbumRead)
async def read_album(album_id: int, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Album).where(Album.id == album_id))
    album = result.scalars().first()
    if album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    return album

@router.post("/", response_model=AlbumRead)
async def create_album(album: AlbumCreate, session: AsyncSession = Depends(get_async_session)):
    new_album = Album(**album.dict())
    session.add(new_album)
    await session.commit()
    await session.refresh(new_album)
    return new_album
