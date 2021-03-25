from flask import Blueprint, request, jsonify, redirect
from app.repositoryapp.api import *
from app.utils import create_response, class2data, login_required
from app import User, Repository
from flask import g

repository = Blueprint('repository', __name__)

# 创建仓库接口 param:  reponame, desc nikename由token传入
@repository.route('/create', methods=['POST'])
@login_required
def create():
    reponame = request.form.get('reponame')
    desc = request.form.get('desc')
    nickname = g.user_name
    result = create_repo(nickname, reponame, desc)

    return result

@repository.route('/<nickname>/<reponame>/')
@repository.route('/<nickname>/<reponame>/<path:file_path>')
@repository.route('/<nickname>/<reponame>/tree/<branch>/')
@repository.route('/<nickname>/<reponame>/tree/<branch>/<path:file_path>')
def show(nickname, reponame, branch="master", file_path=""):
    response = get_file_from_directory(nickname, reponame, file_path, branch)
    return response

@repository.route('/<nickname>')
def get_repo(nickname):
    user = User.get_nickname(nickname).first()
    repositories = user.repositories
    result = class2data(repositories, Repository.__fields__) 
    response = create_response(0, "success", user_repositories=result)
    return response

@repository.route('/branch/<nickname>/<reponame>')
def get_branch(nickname, reponame):
    response = get_branch_from_directory(nickname, reponame) 
    return response 

@repository.route('/fork', methods=['POST'])
@login_required
def fork():
    owner = g.user_name
    anoname = request.form.get('nickname')
    anorepo = request.form.get('reponame')
    print("owner", owner, "anoname", anoname, "anrepo", anorepo)
    response = fork_repo(owner, anoname, anorepo)
    return response

@repository.route('/upload', methods=["GET", "POST"])
def upload():
    nickname = request.form.get('nickname')
    reponame = request.form.get('reponame')
    commit_msg = request.form.get('commit')
    bin_file = request.files['file']
    filepath = request.form.get('filepath')
    filename = request.form.get('filename')
    print("nickname", nickname ,"reponame", reponame, "commit_msg", commit_msg, "bin_file", bin_file)
    res = upload_file(nickname, reponame, filepath, filename, bin_file, commit_msg)
    return res

@repository.route('/download', methods=["POST", "GET"])
def download():
    nickname = request.form.get('nickname')
    reponame = request.form.get('reponame')
    print("nickname", nickname, "reponame", reponame)
    download_response = download_repo(nickname, reponame)
    return download_response 

