import datetime
from zoneinfo import ZoneInfo
from app.database.database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Boolean,
    Text,
)

def horario_br():
    return datetime.now(ZoneInfo("America/Sao_Paulo"))

class Chamado(Base):
    __tablename__ = "chamado"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    titulo = Column(String(100), nullable=False)

    descricao = Column(Text)

    categoria_id = Column(Integer, ForeignKey('categorias_chamado.id'), nullable=False)
    cliente_id = Column(Integer, ForeignKey('usuario.id'),nullable=False)

    responsavel_id = Column(Integer, ForeignKey('usuario.id'))

    empresa_id = Column(Integer, ForeignKey('empresa.id'), nullable=False)
    prioridade_id = Column(Integer, ForeignKey('prioridade_chamado.id'), nullable=False)
    status_id = Column(Integer, ForeignKey('status_chamado.id'),nullable=False)

    criado_em = Column(DateTime, default=horario_br)

    atualizado_em = Column(DateTime)

    data_hora_fechamento = Column(DateTime)

