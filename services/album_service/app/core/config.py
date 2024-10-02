from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import ValidationError, validator
import sys

class Settings(BaseSettings):
    DATABASE_URL: str  # No default value, making it required

    model_config = SettingsConfigDict(
        env_prefix='',
        env_file=None,  # No env file since we're not using python-dotenv
    )

    @validator('DATABASE_URL')
    def check_database_url(cls, v):
        if not v.startswith("postgresql+asyncpg://"):
            raise ValueError("DATABASE_URL must start with 'postgresql+asyncpg://'")
        return v

def load_config():
    try:
        settings = Settings()
        return settings
    except ValidationError as e:
        print(f"Configuration validation error: {e}")
        sys.exit(1)

settings = load_config()
