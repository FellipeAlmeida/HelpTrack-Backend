from fastapi import APIRouter, FastAPI
from app.database.database import SessionLocal
from app.seeds.categoria_chamado_seeds import create_categorias
from app.seeds.enum_perfis_seeds import create_perfis
from app.seeds.tipo_evento_seeds import create_tipos_eventos
from app.seeds.prioridade_chamado_seeds import create_prioridades
from app.seeds.status_chamado_seeds import create_status_chamados
from app.routes.user_route import user_routes
from app.routes.empresa_route import empresa_routes
from app.routes.auth_route import auth_routes
from app.routes.categories_route import category_routes
from app.exceptions.exceptions import (
    ModuleNotFound,
    UserBlocked,
    UserNotAuthorized,
    TokenError,
    CredentialsError,
    UserNotActive,
    InvalidData,
    ExistingModule
)

from app.exceptions.handlers import (
    user_blocked_handler,
    user_not_authorized_handler,
    token_error_handler,
    credentials_error_handler,
    user_not_active_handler,
    invalid_data_handler,
    existing_module_handler,
    module_not_found_handler
)

app = FastAPI()

# ---------------- HANDLERS PARA AS EXCEÇÕES ----------------

app.add_exception_handler(
    ModuleNotFound,
    module_not_found_handler
)

app.add_exception_handler(
    UserBlocked,
    user_blocked_handler
)

app.add_exception_handler(
    UserNotAuthorized,
    user_not_authorized_handler
)

app.add_exception_handler(
    TokenError,
    token_error_handler
)

app.add_exception_handler(
    CredentialsError,
    credentials_error_handler
)

app.add_exception_handler(
    UserNotActive,
    user_not_active_handler
)

app.add_exception_handler(
    InvalidData,
    invalid_data_handler
)

app.add_exception_handler(
    ExistingModule,
    existing_module_handler
)

# ---------------- HANDLERS PARA AS EXCEÇÕES ----------------

@app.on_event("startup")
def startup():
    db = SessionLocal()

    try:
        create_perfis(db)
        create_tipos_eventos(db)
        create_categorias(db)
        create_prioridades(db)
        create_status_chamados(db)
    except Exception as e:
        print("erro no seed: ", e)

    finally:
        db.close()

api_router = APIRouter(prefix='/api')

api_router.include_router(auth_routes)
api_router.include_router(user_routes)
api_router.include_router(empresa_routes)
api_router.include_router(category_routes)

app.include_router(api_router)

@app.get('/')
def root():
    return {'status_api': 'active'}

