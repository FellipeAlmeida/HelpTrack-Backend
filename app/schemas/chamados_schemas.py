from pydantic import BaseModel
from datetime import datetime

class ChamadoCreateRequest(BaseModel):
    titulo: str
    descricao: str | None = None
    categoria_id: int
    cliente_id: int
    responsavel_id: int | None = None
    empresa_id: int
    prioridade_id: int
    status_id: int
    criado_em: datetime | None = None
    atualizado_em: datetime | None = None
    data_hora_fechamento: datetime | None = None