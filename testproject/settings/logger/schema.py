from elrahapi.middleware import models


class LogReadModel(models.MetaLogReadModel):
    user_id: int | None = None

    class setting:
        from_attributes = True
