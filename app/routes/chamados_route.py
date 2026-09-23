from fastapi import APIRouter, Depends, Query
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.middlewares.auth import autorizar_roles
from app.schemas.chamados_schemas import ChamadoCreateRequest, GetAllChamadosResponse, GetChamado, EditChamadoRequest
from app.services.chamados_services import create_chamado_service, get_all_chamados_service, get_chamado_service, delete_chamado_service, edit_chamado_service, get_my_chamados_service

chamados_routes = APIRouter(tags=["05. Chamados"], prefix='/chamado')

# ---------------------- CRIA ----------------------

@chamados_routes.post("/")
def create_chamado(data: ChamadoCreateRequest, db: Session = Depends(get_db), dependencies=[Depends(autorizar_roles(['cliente']))]):

    create_chamado_service(data, db)
    return {'message': 'Chamado criado com sucesso!'}

# ---------------------- LISTA ----------------------

@chamados_routes.get('/', response_model=GetAllChamadosResponse)
def get_all_chamados(page: int = Query(1, ge=1), size: int = Query(1, le=100), db: Session = Depends(get_db), dependencies=[Depends(autorizar_roles(['admin', 'superadmin', 'tecnico']))]):

    chamados = get_all_chamados_service(page, size, db)
    return chamados

# ---------------------- LISTA BY TOKEN ----------------------

@chamados_routes.get('/me', response_model=GetAllChamadosResponse)
def get_my_chamados(page: int = Query(1, ge=1), size: int = Query(1, le=100), db: Session = Depends(get_db), usuario_logado: dict = Depends(autorizar_roles(["admin", "superadmin", "cliente"]))):

    chamados = get_my_chamados_service(page, size, usuario_logado, db)
    return chamados

# ---------------------- BUSCA ----------------------

@chamados_routes.get('/{id}', response_model=GetChamado)
def get_chamado(id: int, db: Session = Depends(get_db), dependencies=[Depends(autorizar_roles(['admin', 'superadmin', 'tecnico']))]):

    chamado = get_chamado_service(id, db)
    return chamado

# ---------------------- EDIT ----------------------

@chamados_routes.patch('/{id}')
def edit_chamado(id: int, data: EditChamadoRequest, db: Session = Depends(get_db), dependencies=[Depends(autorizar_roles(['cliente', 'tecnico']))]):

    edit_chamado_service(id, data, db)
    return {'message': 'Chamado editado com sucesso!'}

# ---------------------- DELETE ----------------------

@chamados_routes.delete('/{id}')
def delete_chamado(id: int, db: Session = Depends(get_db), dependencies=[Depends(autorizar_roles(['cliente']))]):

    delete_chamado_service(id, db)  
    return {'message': 'Chamado deletado com sucesso!'}
