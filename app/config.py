class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1/demo?charset=utf8mb4"
    JSON_AS_ASCII = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1/demo?charset=utf8mb4"
    DEBUG = True    

class TestConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:kn1Csadc6)@127.0.0.1/hellogit?charset=utf8mb4"

class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'test': TestConfig,
    'production': ProductionConfig,
    'default': Config
}
