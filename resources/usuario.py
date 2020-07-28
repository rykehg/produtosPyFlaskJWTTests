from flask_jwt_extended import create_access_token, get_raw_jwt, jwt_required
from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash, generate_password_hash

from blacklist import BLACKLIST
from models.usuario import UsuarioModel


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
        data = attributes.parse_args()
        if UsuarioModel.find_by_login(data['login']):
            return {"message": "The login '{}' already exists."
                    .format(data['login'])}

        if data['login'] and data['senha']:
            usuario = UsuarioModel(**data)
            usuario.senha = generate_password_hash(data['senha'])
            usuario.save_usuario()
            return {'message': 'Usuario created successfully!'}, 201  # Created
        return {'message': 'Request is missing required fields'}, 400


class UsuarioLogin(Resource):
    # /login
    @classmethod
    def post(cls):
        data = attributes.parse_args()
        usuario = UsuarioModel.find_by_login(data['login'])

        if usuario and check_password_hash(usuario.senha, data['senha']):
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
