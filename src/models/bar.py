import uuid

from fastapi import HTTPException, status
from sqlalchemy import Column, String, select
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.base import Base


class Bar(Base):
    __tablename__ = "bar"
    id = Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4, autoincrement=True)
    key = Column(String, nullable=False, primary_key=True, unique=True)
    value = Column(String, nullable=False)

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value

    @classmethod
    async def find(cls, db_session: AsyncSession, key: str):
        """

        :param db_session:
        :param key:
        :return:
        """
        stmt = select(cls).where(cls.key == key)
        result = await db_session.execute(stmt)
        instance = result.scalars().first()
        if instance is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"Not found": f"There is no record for requested: {key=}"},
            )
        else:
            return instance
