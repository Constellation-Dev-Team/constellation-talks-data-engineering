from sqlmodel import Field, SQLModel

class Price(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    date: str
    price: float
    ativo_id: int = Field(foreign_key="Ativos.id")
    price_open: float
    price_high: float
    price_low: float
    
    __tablename__ = "ativos_prices"