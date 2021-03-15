from models.models import User
from sqlalchemy import and_

# 数据表操作的类
class User_Operation():
    def __init__(self):
        self.__fields__ = ["id", "username", "password", "phone","others"]
        self.__username__ = ["username"]

    def _all_user(self):
        #数据库查询
        user_list = User.query.all()
        return user_list

    def _reg(self):
        u = User(**kwargs)
        db.session.add(u)
        db.session.commit()
        return "register success"

    def _login(self,username,password):
        use = User.query.filter(and_(User.username==username, User.password==password))
        return use
