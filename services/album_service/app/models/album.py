from sqlalchemy import Column, Integer, String
from app.database.base import Base

class Album(Base):
    __tablename__ = "albums"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    artist = Column(String, index=True, nullable=False)
    genre = Column(String, index=True)
    release_year = Column(Integer)