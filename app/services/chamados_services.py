from math import ceil
from sqlalchemy.orm import Session
from app.exceptions.exceptions import InvalidData, ModuleNotFound
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

# ---------------------- LISTA ----------------------

def chamado_to_json(chamado: Chamado):
    return {
        "id": chamado.id,
        "titulo": chamado.titulo,
        "descricao": chamado.descricao,
        "categoria_id": chamado.categoria_id,
        "cliente_id": chamado.cliente_id,
        "responsavel_id": chamado.responsavel_id,
        "empresa_id": chamado.empresa_id,
        "prioridade_id": chamado.prioridade_id,
        "status_id": chamado.status_id,
        "criado_em": chamado.criado_em,
        "atualizado_em": chamado.atualizado_em,
        "data_hora_fechamento": chamado.data_hora_fechamento,
    }

def get_all_chamados_service(page, size, db):
    total = db.query(Chamado).count()

    chamados = (
        db.query(Chamado)
        .offset((page - 1) * size)
        .limit(size)
        .all()
    )

    return {
        'page': page,
        'size': size,
        'total': total,
        'total_pages': ceil(total / size) if total > 0 else 1,
        'items': [chamado_to_json(chamado) for chamado in chamados]
    }

# ---------------------- BUSCA ----------------------

def get_chamado_service(id, db):
    chamado = db.query(Chamado).filter(Chamado.id == id).first()

    if not chamado:
        raise ModuleNotFound('Chamado')

    return chamado_to_json(chamado)

# ---------------------- EDIT ----------------------

def edit_chamado_service(id, data, db):
    chamado = db.query(Chamado).filter(Chamado.id == id).first()

    if not chamado:
        raise ModuleNotFound('Chamado')

    titulo = data.titulo
    descricao = data.descricao
    categoria = data.categoria_id
    responsavel = data.responsavel_id
    prioridade = data.prioridade_id
    status = data.status_id

    chamado.titulo = titulo
    chamado.descricao = descricao
    chamado.categoria_id = categoria
    chamado.responsavel_id = responsavel
    chamado.prioridade_id = prioridade
    chamado.status_id = status
    
    db.commit()
    db.refresh(chamado)

# ---------------------- DELETE ----------------------

def delete_chamado_service(id, db):
    chamado = db.query(Chamado).filter(Chamado.id == id).first()

    if not chamado:
        raise ModuleNotFound('Chamado')

    db.delete(chamado)
    db.commit()

# ---------------------- LISTA BY TOKEN ----------------------

def get_my_chamados_service(page, size, usuario_logado, db):

    query = db.query(Chamado).filter(Chamado.cliente_id == usuario_logado['id'])

    total = query.count()

    chamados = (
        query
        .offset((page - 1) * size)
        .limit(size)
        .all()
    )

    return {
        'page': page,
        'size': size,
        'total': total,
        'total_pages': ceil(total / size) if total > 0 else 1,
        'items': [chamado_to_json(chamado) for chamado in chamados]
    }