from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse

from models.produtos import ProdutoModel


class Produtos(Resource):
    @jwt_required
    def get(self):
        # SELECT * FROM produtos

        produtos = ProdutoModel.query.all()
        return {'Produtos': [produto.json() for produto in
                produtos]}


class Produto(Resource):
    attributes = reqparse.RequestParser()
    attributes.add_argument('nome', type=str, required=True,
                            help="The field 'nome' cannot be left blank.")
    attributes.add_argument('quantidade')
    attributes.add_argument('valor', type=str, required=True,
                            help="The field 'valor' cannot be left blank.")
    attributes.add_argument('descricao')

    @jwt_required
    def get(self, produto_id):
        produto = ProdutoModel.find_produto(produto_id)
        if produto:
            return produto.json()
        return {'message': 'Produto not found.'}, 404

    @jwt_required
    def post(self, produto_id):
        if ProdutoModel.find_produto(produto_id):
            return {"message": "Produto id '{}' already exists."
                    .format(produto_id)}, 400  # Bad Request

        data = Produto.attributes.parse_args()
        if not (data['nome'] and data['valor']):
            return {'message': 'Request is missing required fields.'}, 400
        produto = ProdutoModel(produto_id, **data)
        produto.save_produto()

        return produto.json(), 201

    @jwt_required
    def put(self, produto_id):
        data = Produto.attributes.parse_args()
        if not (data['nome'] and data['valor']):
            return {'message': 'Request is missing required fields.'}, 400

        produto_encontrado = ProdutoModel.find_produto(produto_id)
        if produto_encontrado:
            produto_encontrado.update_produto(**data)
            produto_encontrado.save_produto()
            return produto_encontrado.json(), 200
        return {'message': 'Produto not found.'}, 404


    @jwt_required
    def delete(self, produto_id):
        produto = ProdutoModel.find_produto(produto_id)
        if produto:
            produto.delete_produto()
            return {'message': 'Produto deleted.'}
        return {'message': 'Produto not found.'}, 404
