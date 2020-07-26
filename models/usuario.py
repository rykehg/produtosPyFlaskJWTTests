from sql_alchemy import database


class UsuarioModel(database.Model):
    __tablename__ = 'usuarios'

    usuario_id = database.Column(database.Integer, primary_key=True)
    login = database.Column(database.String(40))
    senha = database.Column(database.String(40))

    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def json(self):
        return {
            'usuario_id': self.usuario_id,
            'login': self.login
            }

    @classmethod
    def find_usuario(cls, usuario_id):
        usuario = cls.query.filter_by(usuario_id=usuario_id).first()
        if usuario:
            return usuario
        return None

    @classmethod
    def find_by_login(cls, login):
        usuario = cls.query.filter_by(login=login).first()
        if usuario:
            return usuario
        return None

    def save_usuario(self):
        database.session.add(self)
        database.session.commit()

    def update_usuario(self, login, senha):
        self.login = login
        self.senha = senha

    def delete_usuario(self):
        database.session.delete(self)
        database.session.commit()
