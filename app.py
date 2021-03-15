from flask import Flask
# 导入user模块
from handler.user import user
# app = Flask(__name__)
from db_config import app
# 用户模块 user/login user/register user/changepwd
app.register_blueprint(user, url_prefix="/user")


# 商品模块

# 订单模块


@app.route('/')
def hello():
    return "hello"


if __name__ == '__main__':
    app.run()