import os
from functools import lru_cache
from pydantic import BaseSettings

from src.utils import get_logger

logger = get_logger(__name__)


class Settings(BaseSettings):
    """

    Create instance of Settings with Pydantic BaseSettings and validate data types.

    Parameters:
    pg_user (str):
    pg_pass (str):
    pg_database: (str):
    pg_port: (str):
    asyncpg_url: AnyUrl:

    Returns:
    instance of Settings

    """

    pg_user: str = os.getenv("PG_USER", "postgres")
    pg_pass: str = os.getenv("PG_PASSWORD", "password")
    pg_host: str = os.getenv("PG_HOST", "localhost")
    pg_database: str = os.getenv("PG_DB", "postgres")
    pg_port: str = os.getenv("PG_PORT", "5432")
    
    asyncpg_url: str = f"postgresql+asyncpg://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_database}"


@lru_cache
def get_settings():
    logger.info("Loading config file")
    return Settings()
