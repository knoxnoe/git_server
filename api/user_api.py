from operation.db_operation import User_Operation
from utils.data_proccess import *
from db_config import SECRET_KEY
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_httpauth import HTTPBasicAuth
from flask import g
from itsdangerous import BadSignature, SignatureExpired

auth = HTTPBasicAuth()

# 所有用户相关的业务处理函数

# 返回用户列表方法
def User_List():
    #数据库操作模块(SQL语句)：操作类，数据模型类
    u_o = User_Operation()
    result_data = u_o._all_user()
    # print(result_data)
    # 数据库操作的结果，不能直接返回
    # 处理成字典格式进行返回

    # list = "查询成功"
    result = Class_To_Data(result_data, u_o.__fields__)
    return result
# 注册方法
def User_reg(kwargs):
    u_o = User_Operation()
    result = u_o._reg(kwargs)
    return result
# 登录方法
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
def verify_password(username, password):
    # 先验证token
    user_id = verify_auth_token(username)
    # 如果token不存在，验证用户名和密码是否匹配
    if not user_id:
        u_o = User_Operation()
        result_data = u_o._login(username, password)
        user_id = Class_To_Data(result_data, u_o.__username__)
        if not user_id:
            return False
    g.user_id = user_id
    return True



    
    


    