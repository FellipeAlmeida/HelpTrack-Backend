from jose import jwt, JWTError
from fastapi import Depends
from dotenv import load_dotenv
from typing import Literal
import os
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.usuario_model import Usuario
from app.exceptions.exceptions import TokenError, ModuleNotFound, UserNotActive, UserNotAuthorized

load_dotenv()

SECRET = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("JWT_ALGORITHM")
security = HTTPBearer()

Perfil = Literal["superadmin", "admin", 'cliente', 'tecnico']

def autentica(token: str):
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise TokenError()

# PEGA USUARIO ATUAL
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    token = credentials.credentials

    payload = autentica(token)

    user = db.query(Usuario).filter(
        Usuario.email == payload["email"]
    ).first()

    if not user:
        raise ModuleNotFound('Usuário')

    if not user.ativo:
        raise UserNotActive()

    return payload

# AUTORIZA PERFIS
def autorizar_roles(perfis_permitidos: list[Perfil]):
    def verificar(usuario=Depends(get_current_user)):
        if usuario.get("perfil") not in perfis_permitidos:
            raise UserNotAuthorized()
        
        return usuario

    return verificar