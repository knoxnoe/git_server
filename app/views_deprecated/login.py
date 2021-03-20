from flask import Blueprint
from ..models
user = Blueprint('user', __name__)

@user.route('/login')
def login():
    return "sign in"

@user.route('/list')
def user_list():
    #使用用户列表功能
    list = list_user()
    return jsonify(list)