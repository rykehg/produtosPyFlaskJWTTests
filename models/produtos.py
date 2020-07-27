from sql_alchemy import database


class ProdutoModel(database.Model):
    __tablename__ = 'produtos'

    produto_id = database.Column(database.String(255), primary_key=True)
    nome = database.Column(database.String(80))
    quantidade = database.Column(database.Integer)
    valor = database.Column(database.Float(precision=2))
    descricao = database.Column(database.String(40))

    def __init__(self, produto_id, nome, quantidade, valor, descricao):
        self.produto_id = produto_id
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
        self.descricao = descricao

    def json(self):
        return {
            'produto_id': self.produto_id,
            'nome': self.nome,
            'quantidade': self.quantidade,
            'valor': self.valor,
            'descricao': self.descricao
        }

    @classmethod
    def find_produto(cls, produto_id):
        produto = cls.query.filter_by(produto_id=produto_id).first()
        if produto:
            return produto
        return None

    def save_produto(self):
        database.session.add(self)
        database.session.commit()

    def update_produto(self, nome, quantidade, valor, descricao):
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
        self.descricao = descricao

    def delete_produto(self):
        database.session.delete(self)
        database.session.commit()
