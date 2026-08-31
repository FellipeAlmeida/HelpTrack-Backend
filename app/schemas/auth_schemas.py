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