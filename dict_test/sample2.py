# 字典的取值操作

employee = {
    "name": "杨过",
    "sex": "男",
    "hiredate": "1990-06-05",
    "grade": "A",
    "job": "销售",
}

# 字典的取值
name = employee["name"]
print(name)
sex = employee["sex"]
print(sex)

# get 方法可以为不存在的 key赋予默认的value
print(employee.get("name"))
print(employee.get("dept", "其他部门"))

# 遍历字典(1)
for key in employee:  # 遍历字典的key，在根据key值获取value
    v = employee[key]
    print(key, v)

# 直接遍历字典获取value
for value in employee.values():
    print("value", value)

# (2)
for k, v in employee.items():
    print(k, v)

