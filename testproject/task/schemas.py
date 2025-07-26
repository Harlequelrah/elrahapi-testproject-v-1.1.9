from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal

# from .meta_models import TaskBaseModel

class TaskCreateModel(BaseModel):
    name : str = Field(example="Task", description="Name of the task")

class TaskUpdateModel(BaseModel):
    pass

class TaskPatchModel(BaseModel):
    pass

class TaskReadModel(BaseModel):
    id : int
    date_created: datetime
    date_updated: datetime
    class Config:
        from_attributes=True


class TaskFullReadModel(TaskReadModel):
    pass
    class Config:
        from_attributes=True
