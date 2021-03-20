from flask_script import Command, Manager, Option
<<<<<<< HEAD
from app import User, Repository
=======
from app import User
>>>>>>> 9bc4c4b2c75483adc323708d8eb0545353e0c2a3

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
<<<<<<< HEAD
        for user in User.all_user():
            print(user)

class RepositoryFactory(Command):
    "插入一个倉庫至数据库"
    option_list = (
        Option('--name', '-n', dest='name'),
        Option('--owner', '-o', dest='owner'),
    )

    def run(self, name, owner):
       Repository.create_repo(reponame=name, owner=owner) 

class RepositoryList(Command):
    "显示所有仓库"
    
    def run(self):
        for repo in Repository.all_repo():
            print(repo)
=======
        User.show_user()
        
>>>>>>> 9bc4c4b2c75483adc323708d8eb0545353e0c2a3
