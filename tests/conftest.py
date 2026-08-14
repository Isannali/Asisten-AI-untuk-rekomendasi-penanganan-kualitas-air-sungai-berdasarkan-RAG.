import ssl

import pytest_asyncio
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.config import settings


@pytest_asyncio.fixture
async def db_session():
    ssl_context = ssl.create_default_context()

    test_engine = create_async_engine(
        settings.database_url,
        connect_args={"ssl": ssl_context},
        echo=True,
    )

    TestSessionLocal = async_sessionmaker(
        bind=test_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with TestSessionLocal() as session:
        yield session

    await test_engine.dispose()