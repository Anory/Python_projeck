# 判断1000以内的质数, 质数又称素数。一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数；否则称为合数。
# j = 2  # 从2 开始检查
# while j <= 1000:
#     num = j
#     i = 2  # 从2开始除
#     is_prime = True  # 标识当前数字是否为质数，True - 是  False - 否
#     while i < num:
#         if num % i == 0:  # 检查当前数字是否能被i整除
#             is_prime = False
#             break
#         i += 1
#     if is_prime == True:
#         print("{}是质数".format(num))
#     j += 1


# 检查某个数是否为质数
num = int(input("请输入需要检查的数字："))
i = 2
is_prime = True
while i < num:
    if num % i == 0:
        is_prime = False
        print("{}不是质数".format(num))
        break
    i += 1
if is_prime == True:
    print("{}是质数".format(num))
