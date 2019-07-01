# 斐波那契数列(从第三位数开始，每一位数都等于前两位数之和)

result = []
for i in range(0, 10):
    if i == 0 or i == 1:
        result.append(1)
    else:
        result.append(result[i - 1] + result[i - 2])  # 将最新列表的倒数第一位和第二位的和追加到定义好的列表
print(result)
