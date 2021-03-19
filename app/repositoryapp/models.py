from sqlalchemy import and_
from app.extensions import db
from datetime import datetime

class Repository(db.Model): 
    __tablename__ = "repository"
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }
    __fields__ = ["id", "reponame", "description", "owner"]
    # 主键 自增
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 仓库名
    reponame = db.Column(db.String(128), nullable=False)
    # 仓库描述
    description = db.Column(db.String(512))
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now())
    # 创建者
    owner = db.Column(db.String(128), db.ForeignKey("user.nickname"))

    @classmethod
    def create_repo(cls, reponame, owner, description=None):
        # '''插入一个用户至数据库'''
        repo = Repository(reponame=reponame, owner=owner, description=description) 
        db.session.add(repo)
        db.session.commit()

    @classmethod
    def all_repo(cls):
        '''返回数据库中所有用户'''
        repos = Repository.query.all()
        return repos
    
    def __repr__(self):
        return "id={}\treponame={}\t\towner={}\tcreatetime={}".format(self.id, self.reponame, self.owner, self.create_time)
