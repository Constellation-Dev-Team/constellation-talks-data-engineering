from sqlmodel import Session
from ...db.db import get_sa_engine

engine = get_sa_engine()

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()