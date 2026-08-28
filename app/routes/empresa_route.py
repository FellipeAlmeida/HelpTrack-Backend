from fastapi import APIRouter, Depends
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.schemas.empresa_schemas import CreateCompany
from app.middlewares.auth import autorizar_roles
from app.services.empresa_services import create_company_service

empresa_routes = APIRouter(tags=["03. Empresa"], prefix='/empresa')

# ---------------------- CRIA ----------------------

@empresa_routes.post('/')
def create_company(data: CreateCompany, db: Session = Depends(get_db)):

    create_company_service(data, db)
    return {'message': 'Usuário criado com sucesso!', 'status_code': 201}



