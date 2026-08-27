from app.database.database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
)

class EnumPerfis(Base):
    __tablename__ = "enum_perfis"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    valor = Column(String(50), nullable=False, unique=True)

