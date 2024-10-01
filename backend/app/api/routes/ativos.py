from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ...models.domain.ativos import Ativos
from ..utils import get_db

router = APIRouter(
    prefix="/ativos",
    tags=["ativos"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def read_ativos(db: Session = Depends(get_db)):
    ativos = db.exec(select(Ativos)).all()
    return ativos