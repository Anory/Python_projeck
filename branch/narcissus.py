num = int(input("请输入一个三位数："))

# 分别求出三位数的个位，十位，百位
gw = int(num / 100)
sw = int(num / 10 % 10)
bw = int(num % 10)
# 定义变量total，保存各位数字立方和
total = gw ** 3 + sw ** 3 + bw ** 3
print(total)
if total == num:
    print("{}是水仙花数".format(str(num)))
else:
    print("{}不是水仙花数".format(str(num)))
