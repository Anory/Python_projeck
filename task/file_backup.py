import os
import os.path


class BackupFile(object):
    def __init__(self, src, dist):
        """
        文件备份
        :param src: 要备份的文件目录
        :param dist: 备份到该目录
        """
        self.src = src
        self.dist = dist

    # 获取目录文件列表
    def read_list(self):
        """
        获取文件列表并遍历该列表传参给backup_file方法
        :return:
        """
        f_list = os.listdir(self.src)
        print(f_list)
        for i in f_list:
            self.backup_file(i)

    # 备份文件
    def backup_file(self, file_name):
        """
        文件备份
        :param file_name: 文件名字
        :return:
        """
        # 判断dist文件是否存在，如果不存在就创建
        if not os.path.exists(self.dist):
            os.makedirs(self.dist)
            print("指定目录不存在，创建完成")
        # 拼接文件路径用于后面判断是否是文件和打开文件
        src_file_path = os.path.join(self.src, file_name)
        dist_file_path = os.path.join(self.dist, file_name)
        # 判断是否为文件，然后借助文件的后缀进行文件类型判断
        if os.path.isfile(src_file_path) and os.path.splitext(src_file_path)[1].lower() == ".txt":
            with open(dist_file_path, "w", encoding="utf-8") as f_dist, open(src_file_path, "r", encoding="utf-8") as f_src:
                # 读取文件内容并写入到新的文件中
                while True:
                    # 循环读取指定字符长度的内容
                    r = f_src.read(10)
                    if not r:
                        break
                    f_dist.write(r)
                f_dist.flush()
                print("【{}】文件备份完成".format(file_name))
        else:
            print("文件类型不符合，跳过！")


if __name__ == "__main__":
    # 获取当前工程文件目录
    base_path = os.path.dirname(os.path.abspath(__file__))
    print(base_path)
    # 源目标文件目录
    src_path = os.path.join(base_path, "src")
    # 目标文件目录
    dist_path = os.path.join(base_path, "dist")
    bac = BackupFile(src_path, dist_path)
    bac.read_list()
