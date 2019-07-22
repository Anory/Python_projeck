import os
import os.path

# 传入文件夹路径可获取文件夹里面的所有文件以列表形式返回
print(os.listdir())


print(os.path)

# 判断是否是目录
print(os.path.isdir("D:\Python_projeck\demo"))

# 判断是否是文件
print(os.path.isfile("D:\Python_projeck\demo\demo.py"))

# 判断文件是否存在
f = r"D:\Python_projeck\demo\demo.py"
print(os.path.exists(f))

# 获取文件目录
print("文件目录：", os.path.dirname(f))

# 将文件目录和文件名切割开(返回一个元组的数据结构)
print("文件目录和文件名元组：", os.path.split(f))

# 根据路径获取文件名
print("文件名：{}".format(os.path.basename(f)))

# 获取文件后缀（返回一个元组数据结构 os.path.splitext(f)）
print("文件名后缀：{}".format(os.path.splitext(f)[1]))

# 获取当前文件的绝对路径
abs_file = os.path.abspath(__file__)
print("当前文件的绝对路径：{}".format(abs_file))
# 获取当前文件目录
src_path = os.path.dirname(abs_file)
print("当前文件目录:{}".format(src_path))

# 目录拼接
test_file_path = os.path.join(src_path, "text_file")
print(test_file_path)

