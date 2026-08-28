from fastapi import APIRouter, Depends
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.schemas.users_schemas import CreateUser, GetUserResponse, CreateUserResponse
from app.services.user_services import register_user, get_user_by_id_service
from app.middlewares.auth import autorizar_roles

user_routes = APIRouter(tags=["02. Users"], prefix='/users')

# ---------------------- CRIA ----------------------

@user_routes.post('/register', response_model=CreateUserResponse)
def create_user(data: CreateUser, db: Session = Depends(get_db)):

    register_user(data, db)
    return {'message': 'Usuário criado com sucesso!'}

# ---------------------- LISTA ----------------------

@user_routes.get('/{id}', response_model=GetUserResponse, dependencies=[Depends(autorizar_roles(["admin"]))])
def get_user_by_id(id: int, db: Session = Depends(get_db)):

    user = get_user_by_id_service(id, db)
    return user
