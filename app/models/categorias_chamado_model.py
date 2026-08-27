from app.database.database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
)

class CategoriasChamado(Base):
    __tablename__ = "categorias_chamado"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    valor = Column(String(50), nullable=False)

