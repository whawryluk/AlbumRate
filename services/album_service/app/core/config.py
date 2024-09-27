from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://user:password@db:5432/album_db"

    class Config:
        case_sensitive = True

settings = Settings()
