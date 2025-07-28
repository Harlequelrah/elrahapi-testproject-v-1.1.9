from fastapi import FastAPI
from elrahapi.middleware.error_middleware import ErrorHandlingMiddleware
from elrahapi.middleware.log_middleware import LoggerMiddleware
from elrahapi.middleware.middleware_helper import MiddlewareHelper
from .settings.models_metadata import target_metadata
from .settings.auth.configs import authentication_router
from .settings.auth.routers import user_router
from .settings.logger.model import LogModel
from .settings.auth.configs import authentication
# from .myapp.router import app_myapp
from .settings.database import database

database.create_tables(target_metadata=target_metadata)
app = FastAPI(
    root_path="/api"
)


@app.get("/")
async def hello():
    return {"message": "hello"}

app.include_router(authentication_router)
app.include_router(user_router)
middleware_helper=MiddlewareHelper(
    LogModel=LogModel,
    authentication=authentication
)
# app.include_router(app_myapp)
app.add_middleware(
    LoggerMiddleware,
    middleware_helper=middleware_helper
    )
app.add_middleware(
    ErrorHandlingMiddleware,
    middleware_helper=middleware_helper
)
