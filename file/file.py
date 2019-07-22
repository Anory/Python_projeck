

file_path = "C:\\Users\\win7\\Desktop\\test.txt"
# f = open(file_path)
# print(f)
# f.close()

# 打开文件并写入内容，操作完毕之后自动关闭文件， 不加 “w”的话默认为读模式
with open(file_path, "w") as f:
    f.write("nibuhao")
