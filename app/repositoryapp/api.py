import os
import shutil
from app.utils import class2data, create_response
from app.repositoryapp.models import Repository
from git import Repo

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

def clone_bare(bare_path, cloned_path):
    repo = Repo(bare_path)
    if os.path.isdir(cloned_path):      
        cloned_mtime = os.stat(cloned_path).st_mtime
        objects_mtime = os.stat(os.path.join(bare_path, "objects")).st_mtime
        if objects_mtime > cloned_mtime:
            shutil.rmtree(cloned_path) 
            repo.clone(cloned_path)
    else:
        repo.clone(cloned_path)

def get_data_from_directory(nickname, reponame, path_from_url):
    bare_path = os.path.join(GIT_ROOT, nickname, reponame)
    cloned_path = os.path.join(bare_path, reponame)
    clone_bare(bare_path, cloned_path) 
    file_path = os.path.join(cloned_path, path_from_url)

    if os.path.isdir(file_path):
        files = [entry.name for entry in os.scandir(file_path) if not entry.is_dir()]
        dirs = [entry.name for entry in os.scandir(file_path) if entry.is_dir() and entry.name != '.git']
        return create_response(0, "success", files=files, directories=dirs)
    elif os.path.isfile(file_path):
        with open(file_path) as f:
            return create_response(0, "success", content=f.read())
    else:
        return create_response(-1, "No such file in your repository")
   
