from datetime import datetime
import random


def write_file():
    """
    向文件写入内容
    :return:
    """
    file_path = "D:\\Python_projeck\\file\\write.txt"
    # 文件不存在的情况下在写入内容的时候会自动创建文件并写入内容
    with open(file_path, "w") as f:
        # 写入一行内容（默认不换行的需要写入换行符号 \r  \n  \r\n）
        f.write("hello")
        # 换行
        f.write("\n")
        # 再写入一行内容
        f.write("world")


def write_mult_line():
    """
    向文件写入多行内容
    :return:
    """
    file_name = "write_line.txt"
    with open(file_name, "w", encoding="utf-8") as f:
        # \r\n 表示换一行空行再换一次行
        list_l = ["第一行", "\n", "第二行", "\r\n", "第三行"]
        # 向文件写入多行内容， 方法里面的参数需要是可迭代的数据类型（列表、元组等）
        f.writelines(list_l)


def write_user_log():
    """
    写入用户ID和访问时间
    :return:
    """
    user_log = ("用户ID：{}，访问时间：{}".format(random.randint(10000, 99999), datetime.now()))
    print(user_log)
    file_name = "user_log.txt"
    # a 文件内容追加模式， 每执行一次程序追加一条记录
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(user_log)
        f.write("\n")


def read_and_write():
    """
    对文件先读后写
    :return:
    """
    file_name = "read_and_write.txt"
    with open(file_name, "r+", encoding="utf-8") as f:
        rest = f.read()
        # 如果文件有1就写入aaaa
        # 如果没有1就写入bbbb
        if "1" in rest:
            f.write("aaaa")
        else:
            f.write("bbbb")
        f.write("\n")


if __name__ == "__main__":
    # write_file()
    # write_mult_line()
    # for i in range(5):
    #     write_user_log()
    read_and_write()
