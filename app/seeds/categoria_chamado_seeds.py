from app.models.categorias_chamado_model import CategoriasChamado

def create_categorias(db):

    categorias = ['Hardware', 'Software', 'Rede', 'Acesso', 'Impressora', 'Sistema', 'Outros']

    for categoria in categorias:

        existe_categoria = db.query(CategoriasChamado).filter(CategoriasChamado.valor == categoria).first()

        if existe_categoria:
            db.close()
            return

        cria_categoria = CategoriasChamado(valor=categoria)

        db.add(cria_categoria)
        db.commit()
        db.close()
