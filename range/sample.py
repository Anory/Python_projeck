r1 = range(10, 20)
print(r1)
num = r1[0]  # 用到什么数据取什么数据，节省内存高效快速
print(num)

r2 = range(1, 10, 2)  # 1,3,5,7,9,11
print(r2[3:5])  # 生成一个新的range
