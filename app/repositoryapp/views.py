from flask import Blueprint, request, jsonify, redirect
from app.repositoryapp.api import *
from app.utils import create_response, class2data
from app import User, Repository

repository = Blueprint('repository', __name__)

# 创建仓库接口 param:  reponame, desc nikename由token传入
@repository.route('/create', methods=['POST'])
def create():
    reponame = request.form.get('reponame')
    desc = request.form.get('desc')
    nickname = request.form.get('nickname')
    result = create_repo(nickname, reponame, desc)

    return result

@repository.route('/<nickname>/<reponame>/')
@repository.route('/<nickname>/<reponame>/<path:file_path>')
def show(nickname, reponame, file_path=""):
    response = get_data_from_directory(nickname, reponame, file_path)
    return response

@repository.route('/<nickname>')
def get_repo(nickname):
    user = User.get_nickname(nickname).first()
    repositories = user.repositories
    result = class2data(repositories, Repository.__fields__) 
    response = create_response(0, "success", user_repositories=result)
    return response
