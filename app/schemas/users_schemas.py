from typing import List
from datetime import datetime
from pydantic import BaseModel, EmailStr
from app.core.type_password import PasswordStr

class LoginRequest(BaseModel):
    email: EmailStr
    senha: PasswordStr

class LoginResponse(BaseModel):
    message: str
    access_token: str
    token_type: str
    perfil: str

class CreateUser(BaseModel):
    email: EmailStr
    senha: PasswordStr
    nome: str
    perfil: str
    empresa_id: int

class CreateUserResponse(BaseModel):
    message: str

class GetUserResponse(BaseModel):
    id: int
    email: EmailStr
    nome: str
    perfil: str
    ativo: bool
    criado_em: datetime | None = None
    empresa_id: int

class ListUserResponse(BaseModel):
    page: int
    size: int
    total: int
    total_pages: int
    items: List[GetUserResponse]
