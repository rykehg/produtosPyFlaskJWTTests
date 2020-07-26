from flask_restful import Resource, reqparse
from models.usuario import UsuarioModel
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST

attributes = reqparse.RequestParser()
attributes.add_argument('login', type=str, required=True,
                        help="The field 'login' cannot be left blank.")
attributes.add_argument('senha', type=str, required=True,
                        help="The field 'senha' cannot be left blank.")


class Usuario(Resource):
    # /usuarios/{usuario_id}
    @jwt_required
    def get(self, usuario_id):
        usuario = UsuarioModel.find_usuario(usuario_id)
        if usuario:
            return usuario.json()
        return {'message': 'Usuario not found.'}, 404

    @jwt_required
    def put(self, usuario_id):
        data = attributes.parse_args()

        usuario_encontrado = UsuarioModel.find_usuario(usuario_id)
        if usuario_encontrado:
            usuario_encontrado.update_usuario(**data)
            usuario_encontrado.save_usuario()
            return usuario_encontrado.json(), 200
        return {'message': 'Usuario not found.'}, 404

    @jwt_required
    def delete(self, usuario_id):
        usuario = UsuarioModel.find_usuario(usuario_id)
        if usuario:
            usuario.delete_usuario()
            return {'message': 'Usuario deleted.'}
        return {'message': 'Usuario not found.'}, 404


class UsuarioRegister(Resource):
    # /cadastro
    def post(self):
        dados = attributes.parse_args()

        if UsuarioModel.find_by_login(dados['login']):
            return {"message": "The login '{}' already exists."
                    .format(dados['login'])}

        usuario = UsuarioModel(**dados)
        usuario.save_usuario()
        return {'message': 'Usuario created successfully!'}, 201  # Created


class UsuarioLogin(Resource):
    # /login
    @classmethod
    def post(cls):
        dados = attributes.parse_args()

        usuario = UsuarioModel.find_by_login(dados['login'])

        if usuario and safe_str_cmp(usuario.senha, dados['senha']):
            token_de_acesso = create_access_token(identity=usuario.usuario_id)
            return {'access_token': token_de_acesso}, 200
        return {'message': 'The username or password is incorrect.'}, 401
        # Unauthorized


class UsuarioLogout(Resource):
    # /logout
    @jwt_required
    def post(self):
        jwt_id = get_raw_jwt()['jti']  # JWT Token Identifier
        BLACKLIST.add(jwt_id)
        return {'message': 'Logged out successfully!'}, 200
