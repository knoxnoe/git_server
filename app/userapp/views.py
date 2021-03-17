from flask import Blueprint, request, jsonify
from app.userapp.api import *
user = Blueprint('user', __name__)

@user.route('/list')
@auth.login_required
def user_list():
    #使用用户列表功能
    list = list_user()
    return jsonify(list)

@user.route('/login', methods=['GET'])
@auth.login_required
def login():
    token = generate_auth_token(g.user_id)
    return jsonify({'token': token.decode('ascii')})
