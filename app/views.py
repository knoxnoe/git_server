from app.userapp.views import user
from app.repositoryapp.views import repository
DEFAULT_BLUEPRINT = (
    # 数据结构: (蓝本, 前缀)
    (user, '/user'),
    (repository, '/repository')
)