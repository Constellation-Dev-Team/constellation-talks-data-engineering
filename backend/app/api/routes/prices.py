from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ...models.domain.prices import Price
from ..utils import get_db

router = APIRouter(
    prefix="/prices",
    tags=["prices"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{ativo_id}")
def read_prices(ativo_id: int, db: Session = Depends(get_db)):
    prices = db.exec(select(Price).where(Price.ativo_id==ativo_id)).all()
    return prices


