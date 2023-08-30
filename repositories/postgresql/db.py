import logging
import re
from typing import Optional

from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.pool import QueuePool

from settings import get_settings

settings = get_settings()

log = logging.getLogger(__name__)

engine = create_async_engine(
    settings.POSTGRESQL_URL,
    poolclass=QueuePool,
    pool_recycle=settings.SQL_POOL_RECYCLE,
    pool_pre_ping=settings.SQL_POOL_PRE_PING,
    # https://docs.sqlalchemy.org/en/14/dialects/postgresql.html#disabling-the-postgresql-jit-to-improve-enum-datatype-handling
    connect_args={"server_settings": {"jit": "off", "timezone": "utc"}},
)

_db_conn: Optional[Engine]


async def open_database_connection_pools():
    global _db_conn
    log.info("connecting to database: %s" % re.findall("[^@]+$", settings.POSTGRESQL_URL))
    _db_conn = engine
    async with _db_conn.connect() as conn:
        await conn.execute(text("SELECT 1"))


async def close_database_connection_pools():
    global _db_conn
    if _db_conn:
        log.info("closing database connection...")
        await _db_conn.dispose()


def get_db_conn() -> Engine:
    global _db_conn
    assert _db_conn is not None
    return _db_conn


async def get_session(db_conn=Depends(get_db_conn)) -> AsyncSession:
    try:
        async with AsyncSession(db_conn, expire_on_commit=False) as session, session.begin():
            yield session
    except Exception as ex:
        log.error("The session commit has failed! %s", ex)


def get_test_session() -> AsyncSession:
    global _db_conn
    assert _db_conn is not None

    return AsyncSession(_db_conn, expire_on_commit=False)
