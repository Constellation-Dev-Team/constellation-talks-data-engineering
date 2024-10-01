from sqlmodel import Field, SQLModel

class Ativos(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    ticker: str
    company_name: str

    __tablename__ = "ativos"