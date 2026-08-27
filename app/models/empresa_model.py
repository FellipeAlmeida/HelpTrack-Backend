from app.database.database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
)

class Empresa(Base):
    __tablename__ = "empresa"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome_empresa = Column(String(100), nullable=False)
    cnpj = Column(String(50), nullable=False)

