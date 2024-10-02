# album_service/tests/conftest.py
import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.database.session import get_async_session
from app.database.base import Base
from fastapi.testclient import TestClient
from app.main import app

DATABASE_URL = "sqlite+aiosqlite:///:memory:"

engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    future=True,
)

TestingSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

@pytest.fixture(scope="module")
async def async_session():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with TestingSessionLocal() as session:
        yield session

@pytest.fixture(scope="module")
def client(async_session):
    # Override dependency
    def override_get_async_session():
        yield async_session
    app.dependency_overrides[get_async_session] = override_get_async_session
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
