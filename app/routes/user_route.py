from fastapi import APIRouter, Depends, Query
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.schemas.users_schemas import CreateUser, GetUserResponse, CreateUserResponse, ListUserResponse
from app.services.user_services import get_all_users, register_user, get_user_by_id_service, desactivate_user_by_id
from app.middlewares.auth import autorizar_roles

user_routes = APIRouter(tags=["02. Users"], prefix='/users')

# ---------------------- CRIA ----------------------

@user_routes.post('/register', response_model=CreateUserResponse)
def create_user(data: CreateUser, db: Session = Depends(get_db)):

    register_user(data, db)
    return {'message': 'Usuário criado com sucesso!'}

# ---------------------- LISTA ----------------------

@user_routes.get('/', response_model=ListUserResponse, dependencies=[Depends(autorizar_roles(["superadmin"]))])
def get_all(page: int = Query(1, ge=1), size: int = Query(1, le=100), db: Session = Depends(get_db)):

    users = get_all_users(page, size, db)
    return users

# ---------------------- BUSCA ----------------------

@user_routes.get('/{id}', response_model=GetUserResponse, dependencies=[Depends(autorizar_roles(["superadmin"]))])
def get_user_by_id(id: int, db: Session = Depends(get_db)):

    user = get_user_by_id_service(id, db)
    return user

# ---------------------- DESATIVAR ----------------------D ---

@user_routes.patch('/{id}')
def desactivate_user(id: int, db: Session = Depends(get_db)):

    desactivate_user_by_id(id, db)
    return {'message': 'Usuário desativo com sucesso!'}