from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api

from blacklist import BLACKLIST
from config import JwtBackList, JwtSecret, MySQL, SQLAlchemyMod
from models.sql_alchemy import db, initialize_db
from resources.routes import initialize_routes

app = Flask(__name__)

# To use sqlite data base uncomment the line below and comment mysql_uri line
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
mysql_uri = f"mysql://{MySQL['user']}:{MySQL['password']}@{MySQL['host']}/{MySQL['database']}"
app.config['SQLALCHEMY_DATABASE_URI'] = mysql_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLAlchemyMod
app.config['JWT_SECRET_KEY'] = JwtSecret["key"]
app.config['JWT_BLACKLIST_ENABLED'] = JwtBackList
api = Api(app)
jwt = JWTManager(app)
initialize_db(app)


@app.before_first_request
def create_database():
    db.create_all()


@jwt.token_in_blacklist_loader
def verifica_blacklist(token):
    return token['jti'] in BLACKLIST


@jwt.revoked_token_loader
def token_de_acesso_invalidado():
    return jsonify({'message': 'You have been logged out.'}), 401
    # unauthorized


# imports app routes initialize_routes(app)
initialize_routes(api)
