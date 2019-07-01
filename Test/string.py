# 字符串位置查找，查找不到的情况下返回 -1
source = "Nice to meet you, I need you help."
index = source.find("ee", 17)
print(index)

# 查找指定字符是否在字符串中，返回 True 或 False
isexist = "ee" in source
print(isexist)

# 字符串替换
str1 = "This is string example"
str2 = str1.replace("is", "was")
print(str2)
