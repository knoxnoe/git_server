from flask import Blueprint, request, jsonify
from app.userapp.api import *
user = Blueprint('user', __name__)

# 查看用户列表接口
@user.route('/list')
@auth.login_required
def user_list():
    list = list_user()
    return list

# 登录接口 param: nikename, password_hash
@user.route('/login', methods=['POST'])
@auth.login_required
def login():
    result = user_login()
    return result

# 注册接口 param: nikename, password_hash
@user.route('/register', methods=['POST'])
def reg():
    # get_data = json.loads(request.get_data(as_text=True))
    nickname = request.form.get('nickname')
    password_hash = request.form.get('password_hash')
    # 使用用户的注册功能
    result = User_reg(nickname, password_hash)
    return result


