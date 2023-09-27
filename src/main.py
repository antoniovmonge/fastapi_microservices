from fastapi import FastAPI
import logging

from src.config import settings
from src.database import db

logger = logging.getLogger(__name__)

def init_app():
    app = FastAPI(
        title="Orders App",
        description="Handling Orders",
        version="1",
    )

    @app.on_event("startup")
    def startup():
        db.connect(settings.database_url)

    @app.on_event("shutdown")
    async def shutdown():
        await db.disconnect()

    from src.api.router import router

    app.include_router(
        router,
        prefix="/api/v1",
    )

    return app

app = init_app()
