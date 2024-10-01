from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session


TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
