from sqlalchemy import Column, ForeignKey, Integer

from sqlalchemy.orm import relationship
from ..database import database
from elrahapi.middleware.models import MetaLogModel


class LogModel(database.base, MetaLogModel):
    __tablename__ = "logs"
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    user = relationship("User", back_populates="user_logs")


# vous pouvez adapter à votre cas la colonne subject pour qu'elle corresponde à votre modèle de données
metadata = database.base.metadata
