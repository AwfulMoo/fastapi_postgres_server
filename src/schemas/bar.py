from uuid import UUID

from pydantic import BaseModel, Field


class BarSchema(BaseModel):
    key: str = Field(
        title="",
        value="",
    )
    value: str = Field(
        title="",
        value="",
    )

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "key": "Key for Some Bar",
                "value": "Some Bar Value",
            }
        }


class BarResponse(BaseModel):
    id: UUID = Field(
        title="Id",
        value="",
    )
    key: str = Field(
        title="",
        value="",
    )
    value: str = Field(
        title="",
        value="",
    )

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "config_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "key": "Key for Some Bar",
                "value": "Some Bar Value",
            }
        }
