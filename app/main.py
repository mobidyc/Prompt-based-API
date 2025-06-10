from fastapi import FastAPI
from app.api.v1.routes import items
from app.core.config import settings
from app.core.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
)

# Inclure les routes
app.include_router(items.router, tags=["items"])
