"""
计算1到100以内能被3或者7整除，但不能同时被3和7整除的数的个数，运行结果为39

"""
num = 1
count = 0
# 循环条件
while num <= 100:
    num = num + 1
    # 循环体，设置条件
    # 补全代码
    if (num % 3 == 0 or num % 7 == 0) and (num % 21 != 0):
        count = count + 1
print(count)


