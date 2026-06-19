from flask_smorest import Blueprint , abort
from flask.views import MethodView
from flask import render_template

blp = Blueprint('auth' , __name__)

@blp.route('/api/register')
class RegisterResources(MethodView) :
    def post(self , register_data):
        pass

@blp.route('/api/login')
class LoginResources(MethodView) :
    def post(self , login_data) :
        pass

class Page(MethodView) :
    def get(self) :
        return render_template('auth.html')

