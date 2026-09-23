from fastapi import APIRouter, Depends, Query
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.middlewares.auth import autorizar_roles
from app.schemas.categories_schemas import CreateCategoryRequest, GetCategoryResponse, ListCategoryResponse, EditCategoryRequest
from app.services.categories_services import create_category_service, get_all_categories, get_category_service, edit_category_by_id, delete_category_by_id

category_routes = APIRouter(tags=["04. Categorias"], prefix='/categoria', dependencies=[Depends(autorizar_roles(['superadmin']))])

# ---------------------- CRIA ----------------------

@category_routes.post('/')
def create_category(data: CreateCategoryRequest, db: Session = Depends(get_db)):

    create_category_service(data, db)
    return {'message': 'Categoria criada com sucesso!'}

# ---------------------- LISTA ----------------------

@category_routes.get('/', response_model=ListCategoryResponse)
def list_categories(page: int = Query(1, ge=1), size: int = Query(1, le=100), db: Session = Depends(get_db)):

    categories = get_all_categories(page, size, db)
    return categories

# ---------------------- BUSCA ----------------------

@category_routes.get('/{id}', response_model=GetCategoryResponse)
def get_category(id: int, db: Session = Depends(get_db)):

    category = get_category_service(id, db)
    return category

# ---------------------- EDITA ----------------------

@category_routes.put('/{id}')
def edit_category(id: int, data: EditCategoryRequest, db: Session = Depends(get_db)):

    category = edit_category_by_id(id, data, db)
    return {'message': 'Categoria editada com sucesso!', 'category': category}

# ---------------------- EXCLUI ----------------------

@category_routes.delete('/{id}')
def delete_category(id: int, db: Session = Depends(get_db)):

    delete_category_by_id(id, db)
    return {'message': 'Categoria deletada com sucesso!'}
