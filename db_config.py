# pip install flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)

#配置当前服务的数据库参数         //root:密码@ip:port/数据库名
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:3306/demo?charset=utf8"
db_init = SQLAlchemy(app)
SECRET_KEY = 'vhadgvkasbvksdkvbkjsdbvj'