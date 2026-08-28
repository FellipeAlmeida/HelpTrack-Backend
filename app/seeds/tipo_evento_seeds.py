from app.models.tipos_eventos_model import TiposEvento

def create_tipos_eventos(db):

    tipos_evento = ['criacao', 'alteracao_status', 'alteracao_prioridade', 'atribuicao', 'fechamento', 'reabertura']

    for tipo_evento in tipos_evento:

        existe_tipo_evento = db.query(TiposEvento).filter(TiposEvento.valor == tipo_evento).first()

        if existe_tipo_evento:
            db.close()
            return

        cria_existe_tipo_evento = TiposEvento(valor=tipo_evento)

        db.add(cria_existe_tipo_evento)
        db.commit()
        db.close()
