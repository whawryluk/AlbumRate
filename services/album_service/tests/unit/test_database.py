import pytest
from unittest.mock import AsyncMock, patch
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_async_session

@pytest.mark.asyncio
async def test_get_async_session():
    with patch('app.database.session.async_session') as mock_sessionmaker:
        mock_session = AsyncMock(spec=AsyncSession)
        mock_sessionmaker.return_value.__aenter__.return_value = mock_session

        # Iteracja przez asynchroniczny generator
        async for session in get_async_session():
            assert session is mock_session