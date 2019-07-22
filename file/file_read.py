# 文件读写
def read_file():
    """
    读取文件
    :return:
    """
    file_name = "test.txt"  # 跟程序文件再同一个目录下的话可以使用相对路径和绝对路径
    file_path = "D:\\Python_projeck\\file\\test.txt"   # 跟程序文件不在同一个目录下的话要使用绝对路径
    f = open(file_path, encoding="utf-8")
    # 读取所有的内容
    # rest = f.read()

    # 读取指定字符长度内容
    # rest = f.read(8)
    # print(rest)
    # 再读8个的话就是接着上一次的末尾开始读起（run一下就明白了），文件很大的话可以写一个for循环一次读取指定长度内容
    # print(f.read(8))

    # 跳过指定字符长度（编码的问题，文件要换成英文文档test.txt2）
    # f.seek(10)
    # print(f.read(5))

    # 按行读取,也可以像read那样指定读取的字符长度效果跟read一样
    rest = f.readline()
    print(rest)
    # 再读取一次的话就是接着读取下一行了
    print(f.readline())

    # f.close()

    # 工作中建议使用with方法读写文件，可以不用担心忘记关闭文件
    with open(file_path, encoding="utf-8") as f:
        # 读取所有行返回一个列表
        rest = f.readlines()
        print(rest)
        for i in rest:
            print(i)



if __name__ == "__main__":
    read_file()