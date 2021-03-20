import sys
from app import create_app, create_manager

sys.path.insert(0, "/root/flask-hellogit")

<<<<<<< HEAD
# 选择配置模式
app = create_app('development')    
=======

app = create_app('test')
>>>>>>> 9bc4c4b2c75483adc323708d8eb0545353e0c2a3
manager = create_manager(app)

if __name__ == "__main__":
    manager.run()
