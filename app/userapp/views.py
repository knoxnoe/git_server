from flask import Blueprint, request, jsonify
from app.userapp.api import *
from app.utils import *
user = Blueprint('user', __name__)

# 查看用户列表接口
@user.route('/list')
@login_required
def user_list():
    list = list_user()
    return list


# 注册接口 param: nikename, password_hash
@user.route('/register', methods=['POST'])
def reg():
    # get_data = json.loads(request.get_data(as_text=True))
    nickname = request.form.get('nickname')
    password_hash = request.form.get('password_hash')
    # 使用用户的注册功能
    result = User_reg(nickname, password_hash)
    return result


@user.route('/login', methods=['POST'])
def login():
    result = {'data':'', 
              'msg':'', 
              'status':-1}
    obj = request.get_json(force=True)
    nickname= obj.get("nickname")
    password_hash = obj.get("password_hash")
    if not obj or not nickname or not password_hash:
        result['msg'] = "参数错误，请重新输入"
        return jsonify(result)

    res = verify_password(nickname, password_hash)
    if res == False:
        result['msg'] = "用户名密码错误，请重试"
        return jsonify(result)
    access_token = generate_access_token(user_name=nickname)
    refresh_token = generate_refresh_token(user_name=nickname)
    da = {"access_token": access_token, 
        "refresh_token": refresh_token}
    result['msg'] = "登录成功！"
    result['data'] = da
    result['status'] = 0
    return jsonify(result)

@user.route('/RefreshToken', methods=["GET"])
def test_refresh_token():
    """
    刷新token，获取新的数据获取token
    :return:
    """
    refresh_token = request.args.get("refresh_token")
    if not refresh_token:
        return "参数错误"
    payload = decode_auth_token(refresh_token)
    if not payload:
        return "请登陆"
    if "user_name" not in payload:
        return "请登陆"
    access_token = generate_access_token(user_name=payload["user_name"])
    data = {"access_token": access_token, "refresh_token": refresh_token}
    return jsonify(data)
