from fastapi import APIRouter, Depends, Query
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.schemas.historico_chamado_schemas import CreateHistoricoChamadoRequest, GetAllHistoricosResponse
from app.services.historico_chamado_services import create_historico_chamado_service, get_all_historicos_service, get_historico_service
from app.middlewares.auth import autorizar_roles

historico_routes = APIRouter(tags=["06. Histórico Chamado"], prefix='/historico')

# ---------------------- CRIA ----------------------
@historico_routes.post('/')
def create_historico(data: CreateHistoricoChamadoRequest, db: Session = Depends(get_db)):

    create_historico_chamado_service(data, db)
    return {'message': 'histórico registrado com sucesso!'}

# ---------------------- LISTA ----------------------
@historico_routes.get('/', response_model = GetAllHistoricosResponse)
def get_all_historicos(page: int = Query(1, ge=1), size: int = Query(1, le=100), db: Session = Depends(get_db)):

    chamados = get_all_historicos_service(page, size, db)
    return chamados

# ---------------------- BUSCA ----------------------
@historico_routes.get('/{id}')
def get_historico(id: int, db: Session = Depends(get_db)):

    chamado = get_historico_service(id, db)
    return chamado