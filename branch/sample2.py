if 1 != 1:
    print("1不等于1")
else:
    print("1等于1")

b = 1 == 1
print(b)  # 返回True
print(1 == 1.0)  # 返回True
print("abc".lower() == "Abc".lower())  # 返回True
print(" abc".strip() == "abc")  # 返回True
print(1 == int("1"))  # 返回True

# 数字与布尔表达式的比较
# 数字0代表False 非0代表True

print(0 == False)  # 成立
print(1 == True)  # 成立

if 3 - 1:  # 返回True
    print("成立")
else:
    print("不成立")

