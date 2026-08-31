from math import ceil
from app.models.empresa_model import Empresa
from app.exceptions.exceptions import InvalidData, ModuleNotFound, ExistingModule

# ---------------------- CRIA ----------------------

def create_company_service(data, db):
    nome_empresa = data.nome_empresa
    cnpj = data.cnpj

    if not nome_empresa or not cnpj:
        raise InvalidData()

    cnpj_existe = db.query(Empresa).filter(Empresa.cnpj == cnpj).first()

    if cnpj_existe:
        raise ExistingModule('Empresa')

    new_company = Empresa(
        nome_empresa = nome_empresa,
        cnpj = cnpj
    )

    db.add(new_company)
    db.commit()
    db.close()

# ---------------------- BUSCA ----------------------

def company_json(company: Empresa):
    return {
        'id': company.id,
        'nome_empresa': company.nome_empresa,
        'cnpj': company.cnpj,
        'ativo': company.ativo,
        'deleted_at': company.deleted_at
    }

def get_company_by_id(id, db):
    company = db.query(Empresa).filter(Empresa.id == id).first()

    if not company:
        raise ModuleNotFound('Empresa')

    return company_json(company)

# ---------------------- EDITA BY TOKEN ----------------------

def edit_company_by_id(data, usuario_logado, db):
    company = db.query(Empresa).filter(Empresa.id == usuario_logado['empresa_id']).first()

    if not company:
        raise ModuleNotFound('Empresa')

    nome_empresa = data.nome_empresa

    company.nome_empresa = nome_empresa

    db.commit()
    db.refresh(company)

    return company

# ---------------------- DESATIVA ----------------------

def desactivate_company_by_id(id, db):
    company = db.query(Empresa).filter(Empresa.id == id).first()

    if not company:
        raise ModuleNotFound('Empresa')

    company.ativo = False

    db.commit()
    db.refresh(company)

    return company


def desactivate_company_by_token(usuario_logado, db):

    company = db.query(Empresa).filter(Empresa.id == usuario_logado['empresa_id']).first()

    if not company:
        raise ModuleNotFound('Empresa')
    
    company.ativo = False

    db.commit()
    db.refresh(company)

# ---------------------- LISTA ----------------------

def get_all_companies(page, size, db):
    total = db.query(Empresa).count()

    companies = (
        db.query(Empresa)
        .offset((page - 1) * size)
        .limit(size)
        .all()
    )

    return {
        "page": page,
        "size": size,
        "total": total,
        "total_pages": ceil(total / size) if total > 0 else 1,
        "items": [company_json(company) for company in companies]
    }

    
