from fastapi.testclient import TestClient
from sqlmodel import SQLModel
from app.models.domain.prices import Price
from app.api.utils import get_db
from app.main import app
from .utils import override_get_db, engine, TestingSessionLocal
import pytest

client = TestClient(app)

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope='function')
def setup_teardown():
    SQLModel.metadata.create_all(engine)
    session = TestingSessionLocal()
    prices_item = Price(ativo_id=1, price=100.0, date='2021-01-01', price_open=100.0, price_high=100.0, price_low=100.0)
    session.add(prices_item)
    session.commit()
    session.close()

    yield

    SQLModel.metadata.drop_all(engine)

def test_read_prices(setup_teardown):
    response = client.get("/prices/1")
    assert response.status_code == 200
    assert response.json() == [{"ativo_id": 1, "price": 100.0, "date": "2021-01-01", "price_open": 100.0, "price_high": 100.0, "price_low": 100.0, 'id': 1}]
