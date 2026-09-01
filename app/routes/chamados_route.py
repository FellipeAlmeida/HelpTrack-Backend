from fastapi import APIRouter, Depends, Query
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.schemas.chamados_schemas import ChamadoCreateRequest
from app.services.chamados_services import create_chamado_service

chamados_routes = APIRouter(tags=["05. Chamados"], prefix='/chamado')

# ---------------------- CRIA ----------------------

@chamados_routes.post("/")
def create_chamado(data: ChamadoCreateRequest, db: Session = Depends(get_db)):

    create_chamado_service(data, db)
    return {'message': 'Chamado criado com sucesso!'}