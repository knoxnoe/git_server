import os
import shutil
from app.utils import class2data, create_response
from app.repositoryapp.models import Repository
from git import Repo
from flask import send_file, jsonify


GIT_ROOT = '/gitrepo'

# 创建仓库 api
def create_repo(nickname, reponame, desc):
    #校验仓库名字和拥有人是否重复
    ret = {
        "status": 0,
	    "msg": "",
	    "data": {}
    }
    result = Repository.ver_repeat(reponame, nickname)
    res = class2data(result, ["reponame"])
    if not res:
        repo = Repo.init(os.path.join(GIT_ROOT, nickname, reponame), bare=True)
       
        result = Repository.create_repo(reponame, nickname, desc)
    else:
        ret["status"] = -1	
        result = "当前用户仓库名重复，创建失败" 
    ret["msg"] = result    
    return ret 

def update_cloned_repo(nickname, reponame):
    bare_path = os.path.join(GIT_ROOT, nickname, reponame)
    cloned_path = os.path.join(bare_path, reponame)    
    clone_bare(bare_path, cloned_path)
    return cloned_path

def clone_bare(bare_path, cloned_path):
    repo = Repo(bare_path)
    print("bare_path", bare_path)
    print("cloned_path", cloned_path)
    if os.path.isdir(cloned_path):      
        cloned_mtime = os.stat(cloned_path).st_mtime
        objects_mtime = os.stat(os.path.join(bare_path, "objects")).st_mtime
        #if objects_mtime > cloned_mtime:
        #    shutil.rmtree(cloned_path) 
        #    repo.clone(cloned_path)
        shutil.rmtree(cloned_path)
        repo.clone(cloned_path)
    else:
        repo.clone(cloned_path)

def get_file_from_directory(nickname, reponame, path_from_url, branch):
    bare_path = os.path.join(GIT_ROOT, nickname, reponame)
    cloned_path = os.path.join(bare_path, reponame)
    clone_bare(bare_path, cloned_path) 
    file_path = os.path.join(cloned_path, path_from_url)
    
    cloned_repo = Repo(cloned_path)
    if cloned_repo.heads:
        git = cloned_repo.git
        git.checkout(branch)
   
    if os.path.isdir(file_path):
        files = [entry.name for entry in os.scandir(file_path) if not entry.is_dir()]
        dirs = [entry.name for entry in os.scandir(file_path) if entry.is_dir() and entry.name != '.git']
        return create_response(0, "success", files=files, directories=dirs)
    elif os.path.isfile(file_path):
        with open(file_path) as f:
            return create_response(0, "success", content=f.read())
    else:
        return create_response(-1, "No such file in your repository")
   
def get_branch_from_directory(nickname, reponame):
    bare_path = os.path.join(GIT_ROOT, nickname, reponame)
    repo = Repo(bare_path)
    branches = [str(branch) for branch in repo.heads]
    return create_response(0, "success", branches=branches)

def upload_file(nickname, reponame, innerpath, filename, bin_file, commit_msg, path_from_url=""):
    cloned_path = update_cloned_repo(nickname, reponame) 
    file_path = os.path.join(cloned_path, innerpath, filename)
    print("saved file_path: ", file_path)
    bin_file.save(file_path)
    cloned_repo = Repo(cloned_path)
    git = cloned_repo.git
    git.add('-A')
    git.commit('-am', commit_msg)  
    git.push()
    return create_response(0, "success")  

def download_repo(nickname, reponame):
    cloned_path = update_cloned_repo(nickname, reponame)
    print("download nickname", nickname, "reponame:", reponame)
    repo = Repo(cloned_path)
    tar_path = os.path.join('/tmp', reponame)
    tar_path += '.tar'
    with open(tar_path, 'wb') as fp:
        repo.archive(fp)
    return send_file(tar_path, as_attachment=True)

def fork_gitrepo(forker, owner ,reponame):
    forker_path = os.path.join(GIT_ROOT, forker, reponame)
    owner_path = os.path.join(GIT_ROOT, owner)
    print("forker_path", forker_path, "owner_path", owner_path)
    shutil.copytree(owner_path, forker_path)

def fork_gitrepo1(forker, owner, reponame):
    forker_path = os.path.join(GIT_ROOT, forker, reponame)
    owner_path = os.path.join(GIT_ROOT, owner, reponame)
    owner_repo = Repo(owner_path)
    
def fork_repo(owner, anoname, anorepo):
    '''
    owner: fork发起人
    anoname: 被fork的仓库拥有人
    anrepo: 仓库名
    '''
    ret = {
        "status": 0,
	    "msg": "",
	    "data": {}
    }

    result = Repository.ver_repeat(anorepo, anoname)
    des = class2data(result, ["description"])
    # print(des)
    if not des:
        ret['msg'] = "无此复刻仓库"
        ret['status'] = -1
        return ret

    
    des = des[0]['description']

    result = Repository.ver_repeat(anorepo, owner)
    res = class2data(result, ["reponame"])

    if not res:
        result = Repository.create_repo(anorepo, owner, des)
        fork_gitrepo(owner, anoname, anorepo)
    else:
        ret["status"] = -1	
        result = "当前用户仓库名重复，创建失败" 
    ret["msg"] = result    
    return jsonify(aet)
