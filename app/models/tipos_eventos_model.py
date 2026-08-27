from app.database.database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
)

class TiposEvento(Base):
    __tablename__ = "tipos_evento"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    valor = Column(String(50), nullable=False)

