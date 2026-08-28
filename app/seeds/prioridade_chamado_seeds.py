from app.models.prioridade_chamado_model import PrioridadeChamado

def create_prioridades(db):

    prioridades = ['baixa', 'media', 'alta', 'critica']

    for prioridade in prioridades:

        existe_prioridade = db.query(PrioridadeChamado).filter(PrioridadeChamado.valor == prioridade).first()

        if existe_prioridade:
            db.close()
            return

        cria_prioridades = PrioridadeChamado(valor=prioridade)

        db.add(cria_prioridades)
        db.commit()
        db.close()
