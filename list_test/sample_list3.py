# 列表的反转和排序
# name_list = ["张三", "李四", "王五", "赵六", "孙斌", "王五"]
# # 列表反转
# name_list.reverse()
# print(name_list)
#
# # 列表排序
# num_list = [34, 56, 32, 23, 90, 33]
# num_list.sort()  # 默认升序排序， reverse=True代表降序排序 （reverse 是倒序的意思）
# print(num_list)


# sort 的其他应用
stus = [
    {"name": "xm", "age": 18},
    {"name": "xw", "age": 20},
    {"name": "xl", "age": 15}
]
stus.sort(key=lambda x: x["age"])  # 类似遍历列表里面元素，debug查看运行情况
print(stus[1]["name"])


