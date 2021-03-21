from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_httpauth import HTTPBasicAuth
from flask import g
from itsdangerous import BadSignature, SignatureExpired

from app.userapp.models import User
from app.utils import class2data, create_response

g_b = ""
SECRET_KEY = "vhadgvkasbvksdkvbkjsdbvj"

auth = HTTPBasicAuth()
# 查询用户模块
def list_user():
    data = User.all_user()
    result = class2data(data, User.__fields__)
    return create_response(0, "success", user_list=result)

# 用户登录模块
# 1. 生成token，有效时间为600min
def generate_auth_token(user_id, expiration=36000):
    s = Serializer(SECRET_KEY, expires_in=expiration)
    return s.dumps({'user_id': user_id})

# 2. 解析token
def verify_auth_token(token):
    s = Serializer(SECRET_KEY)
    # token正确
    try:
        data = s.loads(token)
        return data
    # token过期
    except SignatureExpired:
        return None
    except BadSignature:
        return None

# 3. 验证token 拦截方法
@auth.verify_password
def verify_password(nickname, password_hash):
    # 先验证token
    # print(">>> in verify_password {} {}".format(nickname, password_hash))
    user_id = verify_auth_token(nickname)
    # print(user_id)
    # 如果token不存在，验证用户名和密码是否匹配
    tem = user_id
    if not user_id:
        user = User.get_user(nickname, password_hash)
        # print(">>> in vp if {} ".format(user))
        user_id = class2data(user, ["nickname"])
        tem = user_id
        if not user_id:
            return False
    else:
        tem = tem['user_id']
    for k in tem[0]:
        te = tem[0][k]
    g.te = te
    g.user_id = user_id
    print(g.user_id)
    return True

#token验证失败
@auth.error_handler
def error_handler():
    status = -1	
    msg = "用户或者密码错误，失败，请重新登录"
    return create_response(status, msg)

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
