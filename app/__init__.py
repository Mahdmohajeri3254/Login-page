from flask import Flask
from config import config

login_app = Flask(__name__)
login_app.config.from_object(config['Default'])