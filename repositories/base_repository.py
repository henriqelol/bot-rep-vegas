from abc import ABC
from typing import (
    Generic,
    Optional,
    TypeVar,
)
import uuid
from datetime import datetime

from sqlalchemy import (
    delete,
    select,
    update,
)
from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar('T')
V = TypeVar('V')


class BaseRepository(ABC, Generic[T, V]):
    def __init__(self, data_model: T, session: AsyncSession):
        self.data_model = data_model
        self.session = session
        
    def insert_one(self, instance: T):
        self.session.add(instance)
        
    async def get_by_id(self, model_id: V) -> Optional[T]:
        return await self.session.get(self.data_model, model_id)

    async def get_all(self, offset: int, limit: int) -> list[T]:
        query = select(self.data_model).offset(offset).limit(limit)
        records = await self.session.scalars(query)
        return records.all()

    async def delete_by_id(self, uuid: uuid.UUID) -> None:
        stmt = (
            update(self.data_model)
            .where(self.data_model.id == uuid)
            .values({"deleted_at": datetime.utcnow()})
            .execution_options(synchronize_session="fetch")
        )
        await self.session.execute(stmt)

    async def delete_all(self) -> None:
        stmt = delete(self.data_model)
        await self.session.execute(stmt)
