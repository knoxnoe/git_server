from .main import mainapp
from .login import user

DEFAULT_BLUEPRINT = (
    # 数据结构: (蓝本, 前缀)
    (mainapp, ''),
    (user, '/user')
)