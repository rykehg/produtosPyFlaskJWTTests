from flask import Flask, jsonify
from flask_restful import Api
from resources.produto import Produtos, Produto
from resources.usuario import (Usuario, UsuarioRegister, UsuarioLogin,
                               UsuarioLogout)
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST
from config import MySQL

app = Flask(__name__)
# to use sqlite data base uncomment the line below and comment mysql config
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# = 'mysql://NomeDoUsuario:SenhaDoBanco@EndereçoDoBanco(HOST)/NomeDoBanco
app.config['SQLALCHEMY_DATABASE_URI'] = ('mysql://' +
                                         MySQL["user"] + ":" +
                                         MySQL["password"] + "@" +
                                         MySQL["host"] + "/" +
                                         MySQL["database"])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'SecureKeyHere12345'
app.config['JWT_BLACKLIST_ENABLED'] = True
api = Api(app)
jwt = JWTManager(app)


@app.before_first_request
def create_database():
    database.create_all()


@jwt.token_in_blacklist_loader
def verifica_blacklist(token):
    return token['jti'] in BLACKLIST


@jwt.revoked_token_loader
def token_de_acesso_invalidado():
    return jsonify({'message': 'You have been logged out.'}), 401
    # unauthorized


api.add_resource(Produtos, '/produtos')
api.add_resource(Produto, '/produtos/<string:produto_id>')
api.add_resource(Usuario, '/usuarios/<int:usuario_id>')
api.add_resource(UsuarioRegister, '/cadastro')
api.add_resource(UsuarioLogin, '/login')
api.add_resource(UsuarioLogout, '/logout')

if __name__ == '__main__':
    from sql_alchemy import database
    database.init_app(app)
    app.run(debug=True)
