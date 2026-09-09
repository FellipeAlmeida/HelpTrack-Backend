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