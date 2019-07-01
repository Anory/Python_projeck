# 处理员工信息
source = "7782,CLARK,MANAGER,SALES,5000$7934,MILLER,SALESMAN,SALES,3000$7369,SMITH,ANALYST,RESEARCH,2000"
employee_list = source.split("$")
all_emp = {}
# 创建员工字典
for i in range(0, len(employee_list)):
    # 将单个员工信息的字符串切割成列表
    e = employee_list[i].split(",")
    # 创建单个员工信息的字典
    employee = {"no": e[0], "name": e[1], "job": e[2], "department": e[3], "salary": e[4]}
    # 每次循环都将新创建的字典添加到新的字典里面
    all_emp[employee["no"]] = employee

emp_no = input("请输入需要查询的员工编号：")
if emp_no in all_emp:
    emp = all_emp[emp_no]  # 字典取值
    print("工号：{no},姓名：{name},职位：{job},部门：{department},薪资：{salary}".format_map(emp))
else:
    print("编号错误，请重新输入！")



