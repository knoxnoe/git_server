from app.utils import class2data
from app.repositoryapp.models import Repository

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
        result = Repository.create_repo(reponame, nickname, desc)
    else:
        ret["status"] = -1	
        result = "当前用户仓库名重复，创建失败" 
    ret["msg"] = result    
    return ret 
