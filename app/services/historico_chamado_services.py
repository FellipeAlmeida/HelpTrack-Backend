from math import ceil

from app.exceptions.exceptions import InvalidData, ModuleNotFound
from app.models.historico_chamado_model import HistoricoChamado
from app.models.chamado_model import Chamado
from app.models.usuario_model import Usuario

# ---------------------- CRIA ----------------------

def create_historico_chamado_service(data, db):
    chamado_id = data.chamado_id
    cliente_id = data.cliente_id
    tipo_evento_id = data.tipo_evento_id
    descricao = data.descricao
    criado_em = data.criado_em
    atualizado_em = data.atualizado_em

    chamado = db.query(Chamado).filter(Chamado.id == chamado_id).first()
    cliente = db.query(Usuario).filter(Usuario.id == cliente_id).first()

    if not cliente:
        ModuleNotFound('Cliente')

    if not chamado:
        raise ModuleNotFound('Chamado')
    
    if not chamado_id or not cliente_id or not tipo_evento_id or not descricao:
        raise InvalidData()

    novo_historico = HistoricoChamado(
        chamado_id = chamado_id,
        cliente_id = cliente_id,
        tipo_evento_id = tipo_evento_id,
        descricao = descricao,
        criado_em = criado_em,
        atualizado_em = atualizado_em
    )

    db.add(novo_historico)
    db.commit()
    db.close()

# ---------------------- LISTA ----------------------

def historico_to_json(historico: HistoricoChamado):
    return {
        'id': historico.id,
        'chamado_id': historico.chamado_id,
        'cliente_id': historico.cliente_id,
        'tipo_evento_id': historico.tipo_evento_id,
        'descricao': historico.descricao,
        'criado_em': historico.criado_em,
        'atualizado_em': historico.atualizado_em
    }

def get_all_historicos_service(page, size, db):
    total = db.query(HistoricoChamado).count()

    historicos = (
        db.query(HistoricoChamado)
        .offset((page - 1) * size)
        .limit(size)
        .all()
    )

    return {
        "page": page,
        "size": size,
        "total": total,
        "total_pages": ceil(total / size) if total > 0 else 1,
        "items": [historico_to_json(historico) for historico in historicos]
    }

# ---------------------- BUSCA ----------------------

def get_historico_service(id, db):
    historico = db.query(HistoricoChamado).filter(HistoricoChamado.id == id).first()

    if not historico:
        raise ModuleNotFound('Chamado')

    return historico_to_json(historico)

# ---------------------- EDIT ----------------------

def edit_historico_service(id, data, db):
    chamado_id = data.chamado_id
    cliente_id = data.cliente_id
    tipo_evento_id = data.tipo_evento_id
    descricao = data.descricao
    criado_em = data.criado_em
    atualizado_em = data.atualizado_em

    historico = db.query(HistoricoChamado).filter(HistoricoChamado.id == id).first()

    if not historico:
        raise ModuleNotFound('Historico')

    if not chamado_id:
        raise ModuleNotFound('Chamado')
    
    if not cliente_id:
        raise ModuleNotFound('Cliente')

    if not descricao:
        raise ModuleNotFound('Descrição')

    historico.chamado_id = chamado_id
    historico.cliente_id = cliente_id
    historico.tipo_evento_id = tipo_evento_id
    historico.descricao = descricao
    historico.criado_em = criado_em
    historico.atualizado_em = atualizado_em

    db.commit()
    db.refresh(historico)

# ---------------------- DELETE ----------------------

def delete_historico_by_id(id, db):
    historico = db.query(HistoricoChamado).filter(HistoricoChamado.id == id).first()

    if not historico:
        raise ModuleNotFound('Historico')

    db.delete(historico)
    db.commit()