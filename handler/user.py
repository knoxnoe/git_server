from flask import Blueprint, request, jsonify
from api.user_api import *

user = Blueprint('user', __name__)

# 用户模块 user/login 

# 路由配置
@user.route('/list')
def user_list():
    #使用用户列表功能
    list = User_List()
    return jsonify(list)


# # GET 注册 username password phone others
# @user.route('/reg',methods=['GET'])
def reg():
    username = request.args.get("username")
    password = request.args.get("password")
    phone = request.args.get("phone")
    others = request.args.get("others")
    # 验证
    # 使用用户的注册功能
    result = User_reg({
        "username":username,
        "password":password,
        "phone":phone,
        "others":others
    })
    return jsonify(result)

@user.route('/login', methods=['GET'])
@auth.login_required
def login():
    token = generate_auth_token(g.user_id)
    return jsonify({'token': token.decode('ascii')})

