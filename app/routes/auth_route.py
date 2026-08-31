from app.schemas.auth_schemas import LoginRequest, LoginResponse
from datetime import datetime
from app.models.usuario_model import Usuario
from app.exceptions.exceptions import CredentialsError, UserNotActive, UserBlocked
from fastapi import APIRouter, Depends
from app.database.database import get_db
from sqlalchemy.orm import Session
from werkzeug.security import check_password_hash
from app.services.user_services import logica_bloqueio, criar_token_login

auth_routes = APIRouter(tags=["01. Auth"], prefix='/auth')

# ---------------------- LOGIN ----------------------

@auth_routes.post('/login', response_model=LoginResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):

    agora = datetime.now()

    email = data.email.strip().lower()

    user = db.query(Usuario).filter(Usuario.email == email).first()

    if not user:
        raise CredentialsError()

    senha_valida = check_password_hash(user.senha, data.senha)

    if not user.ativo:
        raise UserNotActive()

    if user.tempo_bloqueado and user.tempo_bloqueado > agora:
        raise UserBlocked(user.tempo_bloqueado)

    logica_bloqueio(db, senha_valida, user)

    if not senha_valida:
        raise CredentialsError()
    
    token = criar_token_login(user)

    return {
        'message': 'Usuário logado com sucesso!',
        "access_token": token,
        "token_type": "bearer",
        "perfil": user.perfil
    }
