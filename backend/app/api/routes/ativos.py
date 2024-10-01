from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ...models.domain.ativos import Ativos
from ..utils import get_db
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/ativos",
    tags=["ativos"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def read_ativos(db: Session = Depends(get_db)):
    query = select(Ativos).limit(1000)
    logger.debug(f"Querying database for all Ativos, {query}")
    ativos = db.exec(query).all()
    logger.debug(f"Found {len(ativos)} Ativos")
    return ativos