import datetime
from zoneinfo import ZoneInfo
from app.database.database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Boolean
)

def horario_br():
    return datetime.now(ZoneInfo("America/Sao_Paulo"))

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    nome = Column(String(100), nullable=False)

    perfil = Column(String(30), ForeignKey("enum_perfis.valor"), nullable=False)

    email = Column(String(100), unique=True ,nullable=False)
    senha = Column(String(255), nullable=False)

    ativo = Column(Boolean, nullable=False,)

    tentativas_login = Column(Integer, default=0, nullable=False)
    tempo_bloqueado = Column(DateTime)
    vezes_bloqueado = Column(Integer, default=0)

    token_verificacao = Column(String(255))

    empresa_id = Column(Integer, ForeignKey("empresa.id"), nullable=False)

    criado_em = Column(DateTime, default=horario_br)


