from app.database.database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
)

class StatusChamado(Base):
    __tablename__ = "status_chamado"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    valor = Column(String(50), nullable=False)

