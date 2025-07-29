from sqlalchemy import Column, ForeignKey, Integer, String
from ..database import database
from elrahapi.middleware.models import MetaLogModel

class LogModel(database.base, MetaLogModel):
    __tablename__ = "logs"
    subject = Column(Integer,ForeignKey('users.id'), nullable=True)

metadata = database.base.metadata
