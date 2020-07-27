from models.sql_alchemy import db


class ProdutoModel(db.Model):
    __tablename__ = 'produtos'
    db.get_tables_for_bind
    produto_id = db.Column(db.String(255), primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    quantidade = db.Column(db.Integer)
    valor = db.Column(db.Float(precision=2), nullable=False)
    descricao = db.Column(db.String(40))

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
        db.session.add(self)
        db.session.commit()

    def update_produto(self, nome, quantidade, valor, descricao):
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
        self.descricao = descricao

    def delete_produto(self):
        db.session.delete(self)
        db.session.commit()
