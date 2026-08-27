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

class HistoricoChamado(Base):
    __tablename__ = "historico_chamado"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    chamado_id = Column(Integer, ForeignKey('chamado.id'), nullable=False)

    descricao = Column(Text)

    tipo_evento_id = Column(Integer, ForeignKey('tipos_evento.id'), nullable=False)
    cliente_id = Column(Integer, ForeignKey('usuario.id'),nullable=False)


    criado_em = Column(DateTime, default=horario_br)

    atualizado_em = Column(DateTime)


