from resources.produto import Produto, Produtos
from resources.usuario import (Usuario, UsuarioLogin, UsuarioLogout,
                               UsuarioRegister)


def initialize_routes(api):
    api.add_resource(Produtos, '/produtos')
    api.add_resource(Produto, '/produtos/<string:produto_id>')

    api.add_resource(Usuario, '/usuarios/<int:usuario_id>')
    api.add_resource(UsuarioRegister, '/cadastro')
    api.add_resource(UsuarioLogin, '/login')
    api.add_resource(UsuarioLogout, '/logout')
