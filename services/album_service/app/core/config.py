from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/album_db"

    class Config:
        case_sensitive = True

settings = Settings()
