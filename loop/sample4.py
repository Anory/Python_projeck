n = 1
# 使用while循环条件，控制输出的行数
while n <= 4:
    x = 1
    while x <= 4-n:
        print(" ", end="")
        x += 1

    y = 1
    while y <= 2*n-1:
        print("*", end="")
        y += 1
    print("")
    n += 1

x = 0
y = "*"
while x < 4:
    print(" " * (4 - x-1) + (2 * x + 1) * y)
    x = x + 1
