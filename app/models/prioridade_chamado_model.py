from app.database.database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
)

class PrioridadeChamado(Base):
    __tablename__ = "prioridade_chamado"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    valor = Column(String(50), nullable=False)

