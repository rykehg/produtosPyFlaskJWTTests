from models.sql_alchemy import db


class UsuarioModel(db.Model):
    __tablename__ = 'usuarios'

    usuario_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)

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
        db.session.add(self)
        db.session.commit()

    def update_usuario(self, login, senha):
        self.login = login
        self.senha = senha

    def delete_usuario(self):
        db.session.delete(self)
        db.session.commit()
