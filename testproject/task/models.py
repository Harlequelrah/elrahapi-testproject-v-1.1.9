from sqlalchemy import (
    Boolean,
    Column,
    DECIMAL,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
    Table,
)
from ..settings.database import database

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Task(database.base):
    __tablename__ = 'entities'
    id = Column(Integer, primary_key=True)
    name=Column(String(100), nullable=False)
    date_created = Column(DateTime, default=func.now())
    date_updated = Column(DateTime,default=func.now(), onupdate=func.now())
metadata = database.base.metadata
database.target_metadata = metadata

