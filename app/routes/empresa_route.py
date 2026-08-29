from typing import List
from fastapi import APIRouter, Depends, Query
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.schemas.empresa_schemas import CreateCompany, GetCompanyResponse, EditCompanyRequest, ListCompanyResponse
from app.middlewares.auth import autorizar_roles
from app.services.empresa_services import create_company_service, get_company_by_id, edit_company_by_id, desactivate_company_by_id, get_all_companies, desactivate_company_by_token

empresa_routes = APIRouter(tags=["03. Empresa"], prefix='/empresa')

# ---------------------- CRIA ----------------------

@empresa_routes.post('/')
def create_company(data: CreateCompany, db: Session = Depends(get_db)):

    create_company_service(data, db)
    return {'message': 'Empresa criada com sucesso!', 'status_code': 201}

# ---------------------- LISTAR ----------------------

@empresa_routes.get('/list', response_model=ListCompanyResponse)
def get_all(page: int = Query(1, ge=1), size: int = Query(1, le=100), db: Session = Depends(get_db), usuario_logado: dict = Depends(autorizar_roles(["superadmin"]))):

    companies = get_all_companies(page, size, db)
    return companies

# ---------------------- BUSCA ----------------------

@empresa_routes.get('/{id}', response_model=GetCompanyResponse)
def get_company(id: int, db: Session = Depends(get_db), usuario_logado: dict = Depends(autorizar_roles(["superadmin"]))):

    company = get_company_by_id(id, db)
    return company

# ---------------------- EDITA ----------------------

@empresa_routes.patch('/edit')
def edit_company(data: EditCompanyRequest, db: Session = Depends(get_db), usuario_logado: dict = Depends(autorizar_roles(["admin"]))):

    company = edit_company_by_id(data, usuario_logado, db)
    return {'message': 'Empresa editada com sucesso!', 'company': company}

# ---------------------- DESATIVA POR ID ----------------------

@empresa_routes.patch('/{id}/desactivate')
def desactivate_company(id: int, db: Session = Depends(get_db), usuario_logado: dict = Depends(autorizar_roles(["superadmin"]))):

    company = desactivate_company_by_id(id, db)
    return {'message': 'Empresa desativada com sucesso', 'company': company}

# ---------------------- DESATIVA POR TOKEN ----------------------

@empresa_routes.patch('/')
def desactivate_company(db: Session = Depends(get_db), usuario_logado: dict = Depends(autorizar_roles(["admin"]))):

    desactivate_company_by_token(usuario_logado, db)
    return {'message': 'Sua empresa foi desativada com sucesso!'}

