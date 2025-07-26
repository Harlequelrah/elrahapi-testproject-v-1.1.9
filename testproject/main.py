from fastapi import FastAPI
from elrahapi.middleware.error_middleware import ErrorHandlingMiddleware
from .settings.models_metadata import target_metadata

# from .myapp.router import app_myapp
from .settings.database import database
from .settings.auth.routers import role_router,privilege_router

from .task.utils import task
print(task)

from .settings.auth.models import Role
from elrahapi.authorization.role.schemas import RoleCreateModel

role_create = RoleCreateModel(
    name="ADMIN",
    description="Administre le système",
    is_active=True
)
role_dumped = role_create.model_dump()
role = Role(**role_dumped)
print(role)
database.create_tables(target_metadata=target_metadata)
app = FastAPI(
    root_path="/api"
)
app.include_router(role_router)
app.include_router(privilege_router)

@app.get("/")
async def hello():
    return {"message": "hello"}


# app.include_router(app_myapp)
app.add_middleware(
    ErrorHandlingMiddleware,
)
