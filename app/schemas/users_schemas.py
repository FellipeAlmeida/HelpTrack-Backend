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
    empresa_id: int

