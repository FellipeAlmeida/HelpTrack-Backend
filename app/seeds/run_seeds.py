from app.database.database import SessionLocal
from app.seeds.enum_perfis_seeds import create_perfis
from app.seeds.tipo_evento_seeds import create_tipos_eventos
from app.seeds.categoria_chamado_seeds import create_categorias
from app.seeds.prioridade_chamado_seeds import create_prioridades
from app.seeds.status_chamado_seeds import create_status_chamados

db = SessionLocal()

try:
    create_perfis(db)
    create_tipos_eventos(db)
    create_categorias(db)
    create_prioridades(db)
    create_status_chamados(db)
    print("Seeds executadas com sucesso!")

except Exception:
    db.rollback()
    raise

finally:
    db.close()