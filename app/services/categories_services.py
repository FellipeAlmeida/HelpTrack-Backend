from math import ceil
from app.models.categorias_chamado_model import CategoriasChamado
from app.exceptions.exceptions import InvalidData, ModuleNotFound, ExistingModule

# ---------------------- CRIA ----------------------

def create_category_service(data, db):
    valor = data.valor

    category_exists = db.query(CategoriasChamado).filter(CategoriasChamado.valor == valor.strip().lower()).first()

    if category_exists:
        raise ExistingModule('Categoria')

    if not valor:
        raise InvalidData()

    nova_categoria = CategoriasChamado(
        valor=valor
    )

    db.add(nova_categoria)
    db.commit()
    db.close()

# ---------------------- LISTA ----------------------

def category_to_json(category: CategoriasChamado):

    return {
        "id": category.id,
        "valor": category.valor
    }

def get_all_categories(page, size, db):
    total = db.query(CategoriasChamado).count()

    categories = (
        db.query(CategoriasChamado)
        .offset((page - 1) * size)
        .limit(size)
        .all()
    )

    return {
        "page": page,
        "size": size,
        "total": total,
        "total_pages": ceil(total / size) if total > 0 else 1,
        "items": [category_to_json(category) for category in categories]
        }

# ---------------------- BUSCA ----------------------

def get_category_service(id, db):
    category = db.query(CategoriasChamado).filter(CategoriasChamado.id == id).first()

    if not category:
        raise ModuleNotFound('Categoria')

    return category_to_json(category)

# ---------------------- EDITA ----------------------

def edit_category_by_id(id, data, db):
    category = db.query(CategoriasChamado).filter(CategoriasChamado.id == id).first()

    if not category:
        raise ModuleNotFound('Categoria')

    valor = data.valor

    category.valor = valor

    db.commit()
    db.refresh(category)

    return category

# ---------------------- EXCLUI ----------------------

def delete_category_by_id(id, db):
    category = db.query(CategoriasChamado).filter(CategoriasChamado.id == id).first()

    if not category:
        raise ModuleNotFound('Categoria')

    db.delete(category)
    db.commit()
