# 字典传参
# def fun_dict(name, hiredate, tel, dept):
#
#     print("{}隶属于{}，电话：{}，入职时间：{}".format(name, dept, tel, hiredate))
#
#
# dict1 = {'name': '小葫芦', 'hiredate': '2017-9-23', 'tel': 18795642135, 'dept': '技术部'}
# # 使用字典dict1作为参数传入函数fun_dict
# fun_dict(**dict1)


# format.map方法,格式化字典
def fun_dict(info_dict):
    print("{name}隶属于{hiredate}，电话：{tel}，入职时间：{dept}".format_map(info_dict))


dict1 = {'name': '小葫芦', 'hiredate': '2017-9-23', 'tel': 18795642135, 'dept': '技术部'}
# 使用字典dict1作为参数传入函数fun_dict
fun_dict(dict1)
