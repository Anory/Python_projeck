# 阶乘计算器
num = int(input("请输入要计算的数值（1-100）："))
if 1 <= num <= 100:
    i = 1
    result = 1
    while i <= num:
        # 1:result=1 i=1 结果=1
        # 1:result=1 i=2 结果=2
        # 1:result=2 i=3 结果=6
        # 1:result=6 i=4 结果=24
        # ...
        result = result * i
        if i % 5 == 0:
            print("{}:{}".format(i, result))
        i = i + 1
    print("最终计算的结果是：{}".format(result))
else:
    print("请输入1-100的数值。")


