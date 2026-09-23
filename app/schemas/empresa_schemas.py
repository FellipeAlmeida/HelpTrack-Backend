from typing import List
from pydantic import BaseModel
from datetime import datetime
from app.core.type_cnpj import CnpjStr

class CreateCompanyRequest(BaseModel):
    nome_empresa: str
    cnpj: CnpjStr

class GetCompanyResponse(BaseModel):
    id: int
    nome_empresa: str
    cnpj: CnpjStr
    ativo: bool
    deleted_at: datetime | None = None

class EditCompanyRequest(BaseModel):
    nome_empresa: str

class ListCompanyResponse(BaseModel):
    page: int
    size: int
    total: int
    total_pages: int
    items: List[GetCompanyResponse]