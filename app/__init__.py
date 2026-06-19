from flask import Flask
from config import config
from flask_smorest import Api
from app.auth.auth import blp as auth_bluprint

login_app = Flask(__name__)
login_app.config.from_object(config['Default'])
api = Api(login_app)
api.register_blueprint(auth_bluprint)