# 序列传参


# 1、列表传参
def add(a, b, c):
    num = a + b + c
    print(num)


list1 = [1, 2, 3]
add(*list1)


# 2、字典传参
def add2(a, b, c):
    num = a + b + c
    print(num)


# 俩个星号代表取value值， 一个星号代表取key值
dict1 = {"a": 1, "b": 2, "c": 3}
add2(**dict1)


# 3、返回多个数据,可以在函数体内将需要返回的信息写进一个数据结构内（多数写在字典内，字典内的value值可以用列表存放，列表内
# 可以再写字典储存数据）
def get_detail_info():
    info_dict = {
        "employee": [
            {"name": "张三", "salary": 2000},
            {"name": "李四", "salary": 5000}
        ],
        "other1": [{}],
        "other2": [{}]

    }
    return info_dict


print(get_detail_info())
info = get_detail_info()
name = info.get("employee")[0].get("name")
print(name)
