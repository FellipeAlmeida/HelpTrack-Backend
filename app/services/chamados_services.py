from sqlalchemy.orm import Session
from app.exceptions.exceptions import InvalidData
from app.models.chamado_model import Chamado

# ---------------------- CRIA ----------------------

def create_chamado_service(data, db: Session):
    titulo = data.titulo
    descricao = data.descricao
    categoria_id = data.categoria_id
    cliente_id = data.cliente_id
    responsavel_id = data.responsavel_id
    empresa_id = data.empresa_id
    prioridade_id = data.prioridade_id
    status_id = data.status_id
    criado_em = data.criado_em
    atualizado_em = data.atualizado_em
    data_hora_fechamento = data.data_hora_fechamento

    if not titulo or not categoria_id or not cliente_id or not empresa_id or not prioridade_id or not status_id:
        raise InvalidData()

    novo_chamado = Chamado(
        titulo = titulo,
        descricao = descricao,
        categoria_id = categoria_id,
        cliente_id = cliente_id,
        responsavel_id = responsavel_id,
        empresa_id = empresa_id,
        prioridade_id = prioridade_id,
        status_id = status_id,
        criado_em = criado_em,
        atualizado_em = atualizado_em,
        data_hora_fechamento = data_hora_fechamento,
    )

    db.add(novo_chamado)
    db.commit()
    db.close()