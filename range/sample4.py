# 判断质数
num = int(input("请输入需要判断的数字："))
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
if is_prime == True:
    print("{}是质数".format(num))
else:
    print("{}不是质数".format(num))
