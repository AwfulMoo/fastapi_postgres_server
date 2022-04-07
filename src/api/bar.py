from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.models.bar import Bar
from src.schemas.bar import BarResponse, BarSchema

router = APIRouter(
    prefix="/v1/bar"
)


@router.get("/{key}", response_model=BarResponse)
async def find_bar(key: str, db_session: AsyncSession = Depends(get_db)):
    return await Bar.find(db_session, key)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=BarResponse)
async def create_bar(payload: BarSchema, db_session: AsyncSession = Depends(get_db)):
    bar = Bar(key=payload.key, value=payload.value)
    await bar.save(db_session)
    return bar


@router.delete("/{key}")
async def delete_bar(key: str, db_session: AsyncSession = Depends(get_db)):
    bar = await Bar.find(db_session, key)
    return await Bar.delete(bar, db_session)


@router.patch("/{key}", response_model=BarResponse)
async def update_bar(payload: BarSchema, key: str, db_session: AsyncSession = Depends(get_db)):
    bar = await Bar.find(db_session, key)
    await bar.update(db_session, **payload.dict())
    return bar
