from app.database.database import SessionLocal
from app.models.enum_perfis_model import EnumPerfis

def create_perfis():

    db = SessionLocal

    perfis = ['admin', 'tecnico', 'cliente', 'superadmin']

    for perfil in perfis:

        existe_perfil = db.query(EnumPerfis).filter(EnumPerfis.valor == perfil).first()

        if existe_perfil:
            db.close()
            return

        cria_perfil = EnumPerfis(valor=perfil)

        db.add(cria_perfil)
        db.commit()
        db.close()
