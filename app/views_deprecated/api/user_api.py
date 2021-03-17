def list_user():
    #数据库操作模块(SQL语句)：操作类，数据模型类
	result_data = User.all_user()
    # u_o = User_Operation()
    # result_data = u_o._all_user()
    # print(result_data)
    # 数据库操作的结果，不能直接返回
    # 处理成字典格式进行返回

    # list = "查询成功"
    result = class2data(result_data, u_o.__fields__)
    return result