from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand


# 单例模式
db = SQLAlchemy()
migrate = Migrate()