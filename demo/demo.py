import os


print(os.listdir())
print(os.path)
# 判断是否是目录
print(os.path.isdir("D:\Python_projeck\demo"))

# 判断是否是文件
print(os.path.isfile("D:\Python_projeck\demo"))

# 判断文件是否存在
f = r"D:\Python_projeck\demo\demo.py"
print(os.path.exists(f))

# 获取文件目录
print(os.path.dirname(f))

# 将文件目录和文件名切割开(返回一个元组的数据结构)
print(os.path.split(f))

# 根据路径获取文件名
print(os.path.basename(f))

# 获取文件后缀
print(os.path.splitext(f))

