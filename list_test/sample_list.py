# 列表的操作
name_list = ["张三", "李四", "王五", "赵六", "孙斌", "王五"]
wangwu = name_list[2]  # 正向取值
print(wangwu)
wangwu = name_list[-3]  # 负向取值
print(wangwu)

# 范围取值：切片(左闭右开原则：包含左边的对应数据， 不包含右边的对应数据)
name_list1 = name_list[1:3]  # 从1开始到3（不包含3）
print(name_list1)

# 获取列表值的位置（index函数用于获取列表指定元素的索引值，注意：只会返回元素第一次出现的索引值）
wangwu_index = name_list.index("王五")
print(wangwu_index)

# 获取指定元素的索引值
for i in name_list:
    print(i)
    name_index = name_list.index(i)
    if i == "王五":
        print(name_index)
