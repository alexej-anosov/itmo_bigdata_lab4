from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from config import config


engine = create_async_engine(
    url=config.DB_URL,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,
)


session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as async_session:
        yield async_session
