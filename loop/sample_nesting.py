# 嵌套循环（debug看看运行顺序）
j = 0
while j < 4:
    i = 0
    while i < 4:
        print("口", end="")  # 结尾不换行
        i += 1
    j += 1
    print("")
