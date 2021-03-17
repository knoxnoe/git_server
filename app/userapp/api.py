from app.userapp.models import User
from app.utils import class2data


def list_user():
    data = User.all_user()
    result = class2data(data, User.__fields__)
    return result
