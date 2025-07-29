from elrahapi.middleware import models
class LogReadModel(models.MetaLogReadModel):
    subject: int | None = None
    class setting:
        from_attributes=True
