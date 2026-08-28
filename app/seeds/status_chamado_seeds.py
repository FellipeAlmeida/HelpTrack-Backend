from app.models.status_chamado_model import StatusChamado

def create_status_chamados(db):

    tipos_eventos = ['aberto', 'em_analise', 'em_andamento', 'resolvido', 'fechado', 'cancelado']

    for tipo_evento in tipos_eventos:

        existe_tipo_evento = db.query(StatusChamado).filter(StatusChamado.valor == tipo_evento).first()

        if existe_tipo_evento:
            db.close()
            return

        cria_tipo_evento = StatusChamado(valor=tipo_evento)

        db.add(cria_tipo_evento)
        db.commit()
        db.close()
