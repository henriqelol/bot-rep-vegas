import datetime
import uuid

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update

from repositories.base_repository import BaseRepository

from .postgresql.data_models import TaskDB
from .postgresql.db import get_session


class TaskRepository(BaseRepository[TaskDB, uuid.UUID]):
    def __init__(self, session: AsyncSession = Depends(get_session)):
        super().__init__(TaskDB, session)

    async def check(self, username: uuid.UUID, update_dict: dict) -> None:
        update_dict = {
            "last_keep": datetime.utcnow(), 
            "updated_at": datetime.utcnow(),    
        }
        stmt = (
            update(self.data_model)
            .where(self.data_model.username == username)
            .values(update_dict)
            .execution_options(synchronize_session="fetch")
        )
        await self.session.execute(stmt)
