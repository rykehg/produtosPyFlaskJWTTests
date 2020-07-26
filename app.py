from flask import Flask
from flask_restful import Api
from resources.produto import Produtos, Produto

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def create_database():
    database.create_all()


api.add_resource(Produtos, '/produtos')
api.add_resource(Produto, '/produtos/<string:produto_id>')

if __name__ == '__main__':
    from sql_alchemy import database
    database.init_app(app)
    app.run(debug=True)
