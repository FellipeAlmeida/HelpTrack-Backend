from fastapi import FastAPI
from app.database.database import SessionLocal
from app.seeds.categoria_chamado_seeds import create_categorias
from app.seeds.enum_perfis_seeds import create_perfis
from app.seeds.tipo_evento_seeds import create_tipos_eventos
from app.seeds.prioridade_chamado_seeds import create_prioridades
from app.seeds.status_chamado_seeds import create_status_chamados

app = FastAPI()

@app.on_event("startup")
def startup():
    db = SessionLocal()

    try:
        create_perfis()
        create_tipos_eventos()
        create_categorias()
        create_prioridades()
        create_status_chamados()
    except Exception as e:
        print("erro no seed: ", e)

    finally:
        db.close()

@app.get('/')
def root():
    return {'status_api': 'active'}

