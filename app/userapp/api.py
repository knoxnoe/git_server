from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_httpauth import HTTPBasicAuth
from flask import g
from itsdangerous import BadSignature, SignatureExpired
from app.utils import *
from app.userapp.models import User
from app.utils import class2data, create_response

g_b = ""
SECRET_KEY = "vhadgvkasbvksdkvbkjsdbvj"

auth = HTTPBasicAuth()
# 查询用户模块
def list_user():
    data = User.all_user()
    result = class2data(data, User.__fields__)
    return create_response(0, "success", users=result)

def verify_password(nickname, password_hash):
    use = User.get_user(nickname, password_hash).first()
    if not use:
        return False
    else:
        return use.nickname


# 用户注册模块
def User_reg(nickname, password_hash):
    #校验名字是否重复
    status = 0
    result = User.get_nickname(nickname)
    res = class2data(result, ["nickname"])
    if not res:
        result = User.reg(nickname, password_hash)
    else:
        status = -1
        result = "用户名重复，注册失败"
    return create_response(status, result)

# 用户登录模块
def user_login():
    token = generate_auth_token(g.user_id)
    return create_response(0, "登陆成功", token=token.decode('ascii'))
