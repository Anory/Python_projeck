# 创建字典

# 1、用{}
dict1 = {}  # 空字典
dict2 = {
    "name": "杨过",
    "sex": "男",
    "hiredate": "1990-06-05",
    "grade": "A",
    "job": "销售",
}
print(dict2)

# 利用dict创建字典
dict3 = dict(name="杨大", sex="男", job="造火箭")
print(dict3)
dict4 = dict.fromkeys(["name", "sex", "job"], "N/A")
print(dict4)