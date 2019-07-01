# 嵌套列表，录入员工信息
emp_list = []
while True:
    info = input("请输入员工信息：")  # 逗号对应下面分割逗号
    info_list = info.split("，")  # 将用户输入的字符串转换成新的列表
    if info == "":
        print("程序结束")
        break

    elif len(info_list) != 3:
        print("格式输入错误，请重新输入")
        continue
    emp_list.append(info_list)
    # print(emp_list)
for emp in emp_list:
    print("{n}，年龄:{a}，薪资:{s}".format(n=emp[0], a=emp[1], s=emp[2]))