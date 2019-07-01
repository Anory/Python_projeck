def fun_dict(name,hiredate,tel,dept):

    print("{}隶属于{}，电话：{}，入职时间：{}".format(name, dept, tel, hiredate))


dict1 = {'name':'小葫芦','hiredate':'2017-9-23','tel':18795642135,'dept':'技术部'}
# 使用字典dict1作为参数传入函数fun_dict
fun_dict(**dict1)