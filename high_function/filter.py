

def use_filter(l):
    """
    使用filter函数返回元组/列表中的奇数
    :param l:列表/元组
    :return:过滤好的奇数列表
    """
    rest = filter(lambda n: n % 2 != 0, l)  # 返回的是一个filter的对象
    print(rest)
    return list(rest)  # 通过list方法转换为列表


if __name__ == "__main__":
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rest = use_filter(num_list)
    print(rest)
