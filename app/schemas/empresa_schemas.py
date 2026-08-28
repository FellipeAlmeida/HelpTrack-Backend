from pydantic import BaseModel, EmailStr
from app.core.type_cnpj import CnpjStr

class CreateCompany(BaseModel):
    nome_empresa: str
    cnpj: CnpjStr

class GetCompanyResponse(BaseModel):
    id: int
    nome_empresa: str
    cnpj: CnpjStr