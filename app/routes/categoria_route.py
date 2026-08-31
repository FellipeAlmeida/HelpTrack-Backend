from fastapi import APIRouter, Depends, Query
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.schemas.empresa_schemas import CreateCompany, GetCompanyResponse, EditCompanyRequest, ListCompanyResponse
from app.middlewares.auth import autorizar_roles
from app.services.empresa_services import create_company_service, get_company_by_id, edit_company_by_id, desactivate_company_by_id, get_all_companies, desactivate_company_by_token

empresa_routes = APIRouter(tags=["04. Categoria"], prefix='/categoria')