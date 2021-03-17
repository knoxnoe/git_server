from flask_script import Command, Manager, Option
from app import User

class UserFactory(Command):
    "插入一个用户至数据库"
    option_list = (
        Option('--name', '-n', dest='name'),
    )

    def run(self, name):
        User.make_user(name)
        
class UserList(Command):
    "显示数据库中所有用户"

    def run(self):
        User.show_user()
        
