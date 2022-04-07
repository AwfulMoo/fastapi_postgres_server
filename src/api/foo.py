from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.models.foo import Foo
from src.schemas.foo import FooResponse, FooSchema

router = APIRouter(
    prefix="/v1/foo"
)


@router.get("/", response_model=FooResponse)
async def find_foo(key: str, db_session: AsyncSession = Depends(get_db)):
    return await Foo.find(db_session, key)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=FooResponse)
async def create_foo(payload: FooSchema, db_session: AsyncSession = Depends(get_db)):
    foo = Foo(**payload.dict())
    await foo.save(db_session)
    return foo


@router.delete("/")
async def delete_foo(key: str, db_session: AsyncSession = Depends(get_db)):
    foo = await Foo.find(db_session, key)
    return await foo.delete(foo, db_session)


@router.patch("/", response_model=FooResponse)
async def update_foo(payload: FooSchema, key: str, db_session: AsyncSession = Depends(get_db)):
    foo = await Foo.find(db_session, key)
    await foo.update(db_session, **payload.dict())
    return foo
