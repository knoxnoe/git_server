import os
from flask import Blueprint, request, jsonify, redirect
from app.userapp.api import *
from app.repositoryapp.api import *
from app.utils import create_response

repository = Blueprint('repository', __name__)
GIT_ROOT = '/root/gitroot/'

# 创建仓库接口 param:  reponame, desc nikename由token传入
@repository.route('/create', methods=['POST'])
@auth.login_required
def create():
    reponame = request.form.get('reponame')
    desc = request.form.get('desc')
    print(g.te)
    
    result = create_repo(g.te, reponame, desc)

    return result

@repository.route('/<nickname>/<reponame>')
def show(nickname, reponame):
    repo_path = os.path.join(GIT_ROOT, nickname, reponame)
    return create_response(0, "success", files=os.listdir(repo_path))
