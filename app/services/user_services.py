from math import ceil
from jose import jwt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from app.models.usuario_model import Usuario
from sqlalchemy.orm import Session
from sqlalchemy import update
from app.exceptions.exceptions import CredentialsError, UserBlocked, ExistingModule, ModuleNotFound
from sqlalchemy.orm import Session
from app.exceptions.exceptions import InvalidData
from app.models.usuario_model import Usuario
from werkzeug.security import generate_password_hash

load_dotenv()

SECRET = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("JWT_ALGORITHM")

# ------------------------- AUTH -------------------------

def criar_token_login(usuario):
    payload = {
        "email": usuario.email,
        "id": usuario.id,
        "perfil": usuario.perfil,
        "empresa_id": usuario.empresa_id,
        "type": "auth",
        "exp": datetime.utcnow() + timedelta(hours=2)
    }
    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)
    
# ------------------------- LOGICA BLOQUEIO -------------------------

def incrementar_tentativas(db: Session, email):
    query = (
        update(Usuario)
        .where(Usuario.email == email)
        .values(tentativas_login=Usuario.tentativas_login + 1)
        .returning(Usuario.tentativas_login)
    )

    result = db.execute(query)
    db.commit()

    tentativas = result.scalar_one_or_none()
    return tentativas


def logica_bloqueio(db: Session, senha_valida, user):

    agora = datetime.now()

    if not senha_valida:
        tentativas_login = incrementar_tentativas(db, user.email)

        if tentativas_login > 4:
            query = (
                update(Usuario)
                .where(Usuario.email == user.email)
                .values(vezes_bloqueado=Usuario.vezes_bloqueado + 1)
                .returning(Usuario.vezes_bloqueado)
            )

            result = db.execute(query)
            vezes_bloqueado = result.scalar_one_or_none()

            bloqueio_ate = agora + timedelta(milliseconds=30000 * vezes_bloqueado)
            bloqueio_em_milisegundos = 30000 * vezes_bloqueado
            bloqueio_em_minutos = (bloqueio_em_milisegundos / 1000) / 60

            query_bloqueio = (
                update(Usuario)
                .where(Usuario.email == user.email)
                .values(tempo_bloqueado=bloqueio_ate)
            )

            db.execute(query_bloqueio)

            db.commit()

            raise UserBlocked(bloqueio_em_minutos)
        raise CredentialsError()
    
    query_libera_bloqueio = (
        update(Usuario)
        .where(Usuario.email == user.email)
        .values(tempo_bloqueado=None, tentativas_login=0)
    )

    db.execute(query_libera_bloqueio)

    db.commit()

# ------------------------- LOGICA BLOQUEIO -------------------------

# ------------------------- CRIA -------------------------

def register_user(data, db):

    email = data.email.strip().lower()
    senha = data.senha
    nome = data.nome
    perfil = data.perfil.strip().lower()
    empresa_id = data.empresa_id

    if not email or not senha or not nome or not perfil or not empresa_id:
        raise InvalidData()

    user = db.query(Usuario).filter(Usuario.email == email).first()

    if user:
        raise ExistingModule('Usuário')

    novo_user = Usuario(
        email = email,
        nome = nome,
        perfil = perfil,
        empresa_id = empresa_id,
        senha = generate_password_hash(senha),
        ativo = True
    )

    db.add(novo_user)
    db.commit()
    db.close()

    return novo_user

# ------------------------- BUSCA -------------------------

def users_to_json(user:Usuario):
    return {
        'nome': user.nome,
        'perfil': user.perfil,
        'email': user.email,
        'empresa_id': user.empresa_id,
        'ativo': user.ativo,
        'criado_em': user.criado_em,
        'id': user.id
    }

def get_user_by_id_service(id, db):

    user = db.query(Usuario).filter(Usuario.id == id).first()

    if not user:
        raise ModuleNotFound('Usuário')

    return users_to_json(user)

# ------------------------- LISTA -------------------------

def get_all_users(page, size, db):
    total = db.query(Usuario).count

    users = (
        db.query(Usuario)
        .offset((page - 1) * size)
        .limit(size)
        .all()
    )

    return {
        "page": page,
        "size": size,
        "total": total,
        "total_pages": ceil(total / size) if total > 0 else 1,
        "items": [users_to_json(user) for user in users]
    }

# ------------------------- DESATIVA -------------------------

def desactivate_user_by_id(id, db):

    user = db.query(Usuario).filter(Usuario.id == id).first()

    if not user:
        raise ModuleNotFound('Usuário')

    user.ativo = False

    db.commit()
    db.refresh(user)