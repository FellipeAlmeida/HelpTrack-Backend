from app.models.empresa_model import Empresa
from app.exceptions.exceptions import InvalidData

def create_company_service(data, db):
    nome_empresa = data.nome_empresa
    cnpj = data.cnpj

    if not nome_empresa or not cnpj:
        return InvalidData()

    new_company = Empresa(
        nome_empresa = nome_empresa,
        cnpj = cnpj
    )

    db.add(new_company)
    db.commit()
    db.close()