from flask import Blueprint, request, jsonify, redirect
from app.userapp.api import *
from app.repositoryapp.api import *
repository = Blueprint('repository', __name__)

# 创建仓库接口 param:  reponame, desc nikename由token传入
@repository.route('/create', methods=['POST'])
@auth.login_required
def create():
    reponame = request.form.get('reponame')
    desc = request.form.get('desc')
    print(g.te)
    
    result = create_repo(g.te, reponame, desc)

    return result


