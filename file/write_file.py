import os

# 对文件夹下面所以的文件写入同样的内容
file_path = os.path.join("D:\\test_wirte")
file_list = os.listdir(file_path)
print(file_list)
for name in file_list:
    with open(file_path + "\\" + name, "w+", encoding="utf-8") as f:
        f.write("人生苦短，我用Python")
