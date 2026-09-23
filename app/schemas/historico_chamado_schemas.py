from datetime import datetime
from typing import List
from pydantic import BaseModel

class CreateHistoricoChamadoRequest(BaseModel):
    chamado_id: int
    cliente_id: int
    tipo_evento_id: int
    descricao: str
    criado_em: datetime
    atualizado_em: datetime

class GetHistoricoResponse(BaseModel):
    id: int
    chamado_id: int
    cliente_id: int
    tipo_evento_id: int
    descricao: str
    criado_em: datetime
    atualizado_em: datetime

class GetAllHistoricosResponse(BaseModel):
    page: int
    size: int
    total: int
    total_pages: int
    items: List[GetHistoricoResponse]

class EditHistoricoRequest(BaseModel):
    chamado_id: int | None = None
    cliente_id: int | None = None
    tipo_evento_id: int | None = None
    descricao: str | None = None
    criado_em: datetime | None = None
    atualizado_em: datetime | None = None