from fastapi import FastAPI
from sqlmodel import SQLModel
from .db.db import get_sa_engine
from .api.routes.prices import router as prices_router
from .api.routes.ativos import router as ativos_router
from .middlewares import apply_middlewares

engine = get_sa_engine()
SQLModel.metadata.create_all(engine)

app = FastAPI()

apply_middlewares(app)

app.include_router(prices_router)
app.include_router(ativos_router)