# 遍历列表
name_list = ["张三", "李四", "王五", "赵六", "孙斌", "王五"]
# for 循环用于遍历列表
# for 迭代变量 in 可迭代对象（列表）

# 获取所有王五的正向索引值
i = 0
for n in name_list:
    if n == "王五":
        print(n, i)
    i += 1

# 获取所有王五的倒序索引值
count = len(name_list)
i = 0
for n in name_list:
    if n == "王五":
        ri = count * -1 + i  # count * -1 让值先变成负数（得出来的值刚好是列表第一个元素的倒序索引，加上 i 是每循环一次
        # 往后推一个数 ）
        print(n, i, ri)
    i += 1


# while 循环实现
i = 0
while i < len(name_list):
    n = name_list[i]  # 根据索引值获取列表元素
    ri = count * -1 + i
    if n == "王五":
        print(n, i, ri)
    i += 1


