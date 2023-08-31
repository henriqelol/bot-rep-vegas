import uuid
from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    String,
)
from sqlalchemy.dialects.postgresql import UUID

from .base_class import Base

class TaskDB(Base):
    __tablename__ = "tasks"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    last_keep = Column(DateTime, onupdate=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, onupdate=datetime.utcnow)
