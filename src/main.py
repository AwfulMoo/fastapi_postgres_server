from fastapi import FastAPI

from src.api.foo import router as foo_router
from src.api.bar import router as bar_router
from src.database import engine
from src.models.base import Base
from src.utils import get_logger

logger = get_logger(__name__)

app = FastAPI(title="Template FastAPI to PostgreSQL Server", version="1.0", docs_url="/")

app.include_router(bar_router)
app.include_router(foo_router)


async def start_db():
    async with engine.begin() as conn:
        # TODO: Remove Drop all from production version
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()


@app.on_event("startup")
async def startup_event():
    logger.info("Starting up")
    await start_db()


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down")
