
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)

from ...config.config import settings


# Establecemos conexión con la base de datos
engine = create_async_engine(
    settings.ASYNC_DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,            
    echo=True,
)

async_session_factory  = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,         
    autoflush=False,              
    autocommit=False,
)