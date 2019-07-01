

def pow_number(num_list):
    """
    通过给定列表计算里面每一个值的立方
    :param num_list: 列表
    :return: 列表
    """
    result_list = []
    for i in num_list:
        result_list.append(i * i * i)
    return result_list


def f(n):
    # 求给定数的立方
    return n * n * n


def pow_num_use_map(num_list):
    """
    使用map函数计算给定类表中每个值的立方
    :param num_list:列表
    :return:原来列表中每一项的立方
    """
    # 将列表中的每一项进行计算，完成之后返回一个map对象
    rest = map(f, num_list)
    return rest


def pow_num_use_lambda(num_list):
    """
    使用map函数/lambda函数计算给定类表中每个值的立方
    :param num_list:列表
    :return:原来列表中每一项的立方
    """
    # map方法相当于遍历接收到的列表将列表中的每一项赋值给 n 由lambda函数进行计算，最后返回一个map对象
    return map(lambda n: n * n * n, num_list)  # lambda函数相当于上面写的 f 方法


if __name__ == "__main__":
    m_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rest_list = pow_number(m_list)
    print(rest_list)
    print("==========================")
    rest_list2 = pow_num_use_map(m_list)
    print(list(rest_list2))
    print("==========================")
    rest_list3 = pow_num_use_lambda(m_list)
    print(list(rest_list3))
